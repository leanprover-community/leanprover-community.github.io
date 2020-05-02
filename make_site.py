#!/usr/bin/env python

from pathlib import Path
import sys
import subprocess
from dataclasses import dataclass
from typing import List

import yaml
from staticjinja import Site
import jinja2.ext
import pybtex.database
from mistletoe import Document, HTMLRenderer

class MarkdownExtension(jinja2.ext.Extension):
    tags = set(['markdown'])

    def __init__(self, environment):
        super().__init__(environment)
        environment.extend(
            markdowner=HTMLRenderer()
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

markdown_renderer = HTMLRenderer()

def render_markdown(src: str) -> str:
    return markdown_renderer.render(Document(src))

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
    right: bool = False

    @property
    def class_right(self):
        return ' dropdown-menu-right' if self.right else ''

    @classmethod
    def from_dict(cls, dic):
        return cls(dic['title'], [MenuItem.from_dict(item)
                                  for item in dic['items']],
                                  dic['open_right'])


with (DATA/'menus.yaml').open('r') as menu_file:
    menus = [Menu.from_dict(menu) for menu in yaml.safe_load(menu_file)]

presentation = (DATA/'presentation.md').read_text()

@dataclass
class Formalization:
    title: str
    authors: str
    abstract: str
    url: str

with (DATA/'formalizations.yaml').open('r') as f_file:
    formalizations = [Formalization(**form) for form in yaml.safe_load(f_file)]

@dataclass
class Maintainer:
    name: str
    descr: str
    img: str

with (DATA/'maintainers.yaml').open('r') as m_file:
    maintainers = [Maintainer(**mtr) for mtr in yaml.safe_load(m_file)]

def render_site(target: Path, base_url: str, reloader=False):
    default_context = lambda: {
            'base_url': base_url,
            'menus': menus
            }

    def render_content(env, template, **kwargs):
        """Render a markdown template."""
        content_template = env.get_template("_markdown.html")
        path = Path(template.name)
        title = path.with_suffix('').name
        content_template.stream(**kwargs).dump(str(target/path.parent/title)+'.html')

    def get_contents(template):
        return { 'content': Path(template.filename).read_text().replace('img/',
            base_url+'/img/') }

    def url(raw: str):
        return raw if raw.startswith('http') else base_url + raw

    site = Site.make_site(
            searchpath=TEMPLATE_SRC,
            outpath=str(target),
            extensions=[MarkdownExtension],
            rules = [
                ('.*.md', render_content)],
            contexts=[
                ('.*', default_context),
                ('index.html', {'presentation': presentation,
                                'formalizations': formalizations}),
                ('papers.html', {'papers': pybtex.database.parse_file('lean.bib').entries,
                                 'paper_section': (DATA/'papers.md').read_text()}),
                ('meet.html', {'maintainers': maintainers,
                               'community': (DATA/'community.md').read_text()}),
                ('.*.md', get_contents)
                ],
            filters={ 'url': url, 'md': render_markdown },
            mergecontexts=True)

    for folder in ['css', 'js', 'img', 'bundles']:
        subprocess.call(['rsync', '-a', folder, str(target).rstrip('/')])
    site.render(use_reloader=reloader)

if __name__ == '__main__':
    if '--local' in sys.argv:
        base_url = f"file://{(Path(__file__).parent/'build').absolute()}/"
    else:
        base_url = 'https://leanprover-community.github.io/'
    render_site(ROOT/'build', base_url, reloader='--reload' in sys.argv)
