#!/usr/bin/env python3

from pathlib import Path
import sys
import subprocess
from dataclasses import dataclass, field
from typing import List, Mapping, Optional
from datetime import datetime

import yaml
from staticjinja import Site
import jinja2.ext
from jinja2 import Environment, FileSystemLoader
import pybtex.database
from mistletoe import Document, block_token
from mistletoe_renderer import CustomHTMLRenderer
from pylatexenc.latex2text import LatexNodes2Text
import urllib.request
import json
import gzip
import os
from github import Github
from slugify import slugify

class MarkdownExtension(jinja2.ext.Extension):
    tags = set(['markdown'])

    def __init__(self, environment):
        super().__init__(environment)
        environment.extend(
            markdowner=CustomHTMLRenderer()
        )

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        body = parser.parse_statements(
            ['name:endmarkdown'],
            drop_needle=True
        )
        return jinja2.nodes.CallBlock(
            self.call_method('_markdown_support'),
            [],
            [],
            body
        ).set_lineno(lineno)

    def _markdown_support(self, caller):
        return self.environment.markdowner.render(Document(caller())).strip()

markdown_renderer = CustomHTMLRenderer()

def render_markdown(src: str) -> str:
    return markdown_renderer.render_md(src)

ROOT = Path(__file__).parent
DATA = ROOT/'data'
TEMPLATE_SRC = str(ROOT/'templates')

@dataclass
class MenuItem:
    title: str
    url: str

    @classmethod
    def from_dict(cls, dic):
        return cls(*next(iter(dic.items())))

@dataclass
class Menu:
    title: str
    items: List[MenuItem]

    @classmethod
    def from_dict(cls, dic):
        return cls(dic['title'], [MenuItem.from_dict(item)
                                  for item in dic['items']])


with (DATA/'menus.yaml').open('r', encoding='utf-8') as menu_file:
    menus = [Menu.from_dict(menu) for menu in yaml.safe_load(menu_file)]

presentation = (DATA/'presentation.md').read_text(encoding='utf-8')

what_is = (DATA/'what_is.md').read_text(encoding='utf-8')


with (DATA/'teaching.yaml').open('r', encoding='utf-8') as t_file:
    courses = yaml.safe_load(t_file).values()


def render_site(target: Path, base_url: str):
    default_context = {
            'base_url': base_url,
            'menus': menus,
            }
    def url(raw: str):
        return raw if raw.startswith('http') else base_url + raw

    latexnodes2text = LatexNodes2Text()
    def clean_tex(src: str) -> str:
        return latexnodes2text.latex_to_text(src)

    env = Environment(loader=FileSystemLoader(TEMPLATE_SRC), extensions=[MarkdownExtension])
    env.filters={ 'url': url, 'md': render_markdown, 'tex': clean_tex }
    tpl = env.get_template('teaching.html')
    tpl.stream({'introduction': (DATA/'teaching.md').read_text(encoding='utf-8'), 'courses': courses, **default_context}).dump(str(target/'teaching.html'))

    for folder in ['css', 'js', 'img']:
        subprocess.call(['rsync', '-a', folder, str(target).rstrip('/')])

if __name__ == '__main__':
    base_url = f"file://{(Path(__file__).parent/'build').absolute()}/"
    render_site(ROOT/'build', base_url)
