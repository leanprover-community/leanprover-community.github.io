#!/usr/bin/env python3

from pathlib import Path
import sys
import subprocess
from dataclasses import dataclass, field
from typing import List, Mapping, Optional
import re

import yaml
from staticjinja import Site
import jinja2.ext
import pybtex.database
from mistletoe import Document, HTMLRenderer
from pylatexenc.latex2text import LatexNodes2Text
import urllib.request
import json
import gzip

class CustomHTMLRenderer(HTMLRenderer):
    """
    Override the default heading to provide links like in GitHub.
    """
    def render_heading(self, token) -> str:
        template = '<h{level} id="{anchor}" class="markdown-heading">{inner} <a class="hover-link" href="#{anchor}">#</a></h{level}>'
        inner: str = self.render_inner(token)
        # generate anchor following what github does
        # See info and links at https://gist.github.com/asabaylus/3071099
        anchor = inner.strip().lower()
        anchor = re.sub(r'[^\w\- ]+', '', anchor).replace(' ', '-')
        return template.format(level=token.level, inner=inner, anchor=anchor)

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


with (DATA/'menus.yaml').open('r', encoding='utf-8') as menu_file:
    menus = [Menu.from_dict(menu) for menu in yaml.safe_load(menu_file)]

presentation = (DATA/'presentation.md').read_text(encoding='utf-8')

what_is = (DATA/'what_is.md').read_text(encoding='utf-8')

@dataclass
class Formalization:
    title: str
    authors: str
    abstract: str
    url: str

with (DATA/'formalizations.yaml').open('r', encoding='utf-8') as f_file:
    formalizations = [Formalization(**form) for form in yaml.safe_load(f_file)]

@dataclass
class Maintainer:
    name: str
    descr: str
    img: str

with (DATA/'maintainers.yaml').open('r', encoding='utf-8') as m_file:
    maintainers = [Maintainer(**mtr) for mtr in yaml.safe_load(m_file)]

@dataclass
class DocDecl:
    name: str
    args: List[str]
    tp: str
    docs_link: str
    src_link: str

@dataclass
class HundredTheorem:
    number: str
    title: str
    decl: Optional[str] = None
    decls: Optional[List[str]] = None
    doc_decls: Optional[List[DocDecl]] = None
    author: Optional[str] = None
    links: Optional[Mapping[str, str]] = None
    note: Optional[str] = None

urllib.request.urlretrieve('https://leanprover-community.github.io/mathlib_docs/export_db.json.gz', 'export_db.json.gz')
with gzip.GzipFile('export_db.json.gz', 'r') as json_file:
    json_bytes = json_file.read()
    json_file.close()

decl_loc_map = json.loads(json_bytes.decode('utf-8'), strict=False)

def undecorate_arg(arg):
    return ''.join(
        match[4] if match[0] == '' else
        match[1] + match[2] + match[3]
        for match in re.findall(r'\ue000(.+?)\ue001(\s*)(.*?)(\s*)\ue002|([^\ue000]+)', arg))

with (DATA/'100.yaml').open('r', encoding='utf-8') as h_file:
    hundred_theorems = [HundredTheorem(thm,**content) for (thm,content) in yaml.safe_load(h_file).items()]
    for h in hundred_theorems:
        if h.decl:
            assert not h.decls
            h.decls = [h.decl]
        if h.decls:
            doc_decls = []
            for decl in h.decls:
                try:
                    decl_info = decl_loc_map[decl]
                except KeyError:
                    print(f'Error: 100 theorems entry {h.number} refers to a nonexistent declaration {decl}')
                    continue
                doc_decls.append(DocDecl(
                    name=decl,
                    args=[undecorate_arg(arg['arg']) for arg in decl_info['args']],
                    tp=undecorate_arg(decl_info['type']),
                    docs_link=decl_info['docs_link'],
                    src_link=decl_info['src_link']))
            h.doc_decls = doc_decls
        else:
            h.doc_decls = []


def replace_link(name, id):
    if name == '':
        return name
    elif '/' in name:
        return '/mathlib_docs/' + name
    else:
        try:
            return decl_loc_map[name]['docs_link']
        except KeyError:
            print(f'Error: overview item {id} refers to a nonexistent declaration {name}')

@dataclass
class Overview:
    id: str
    depth: int
    title: str
    decl: Optional[str] = None
    parent: Optional['Overview'] = None
    children: List['Overview'] = field(default_factory=list)

    @property
    def has_missing_child(self) -> bool:
        if self.children:
            return any(child.has_missing_child for child in self.children)
        else:
            return not bool(self.decl)

    @property
    def is_nonempty(self) -> bool:
        if self.children:
            return any(child.is_nonempty for child in self.children)
        else:
            return bool(self.decl)

    @classmethod
    def from_node(cls, identifier: str, title: str, children, depth: int, parent: 'Overview' = None) -> 'Overview':
        node = cls(
                id=identifier,
                depth=depth,
                title=title,
                decl=replace_link((children or '').strip(), identifier) if not isinstance(children, dict) else None,
                parent=parent,
                children=[])

        if isinstance(children, dict):
            node.children = [cls.from_node(f"{identifier}-{index}", title, subchildren, depth + 1, parent=node) for index, (title, subchildren) in enumerate(children.items())]

        return node


    @classmethod
    def from_top_level(cls, index: int, title: str, children) -> 'Overview':
        return cls.from_node(f"{index}", title, children, 0)

with (DATA/'overview.yaml').open('r', encoding='utf-8') as h_file:
    overviews = [Overview.from_top_level(index, title, elements) for index, (title, elements) in enumerate(yaml.safe_load(h_file).items())]

bib = pybtex.database.parse_file('lean.bib')

about_lean_dic = {}
about_mathlib_dic = {}
formalization_papers_dic = {}

for key, data in bib.entries.items():
    if 'tags' not in data.fields:
        continue
    tags = list(map(str.strip, data.fields.get('tags', '').split(',')))

    data.fields['tags'] = tags
    if 'about-lean' in tags:
        data.fields['tags'].remove('about-lean')
        about_lean_dic[key] = data
    if 'about-mathlib' in tags:
        data.fields['tags'].remove('about-mathlib')
        about_mathlib_dic[key] = data
    if 'formalization' in tags:
        data.fields['tags'].remove('formalization')
        formalization_papers_dic[key] = data

    if 'link' in data.fields:
        url = data.fields['link'][5:-1]
    elif 'url' in data.fields:
        url = data.fields['url']
    elif 'eprint' in data.fields:
        eprint = data.fields['eprint']
        if eprint.startswith('arXiv:'):
            url = 'https://arxiv.org/abs/'+eprint[6:]
        else:
            url = eprint
    else:
        raise ValueError(f"Couldn't find a url for bib item {key}")
    if url.startswith(r'\url'):
        url = url[4:].strip('{}')
    if 'journal' in data.fields and data.fields['journal'] != 'CoRR':
        journal = data.fields['journal']
    elif 'booktitle' in data.fields:
        journal = data.fields['booktitle']
    else:
        journal = None
    data.fields['url'] = url
    data.fields['journal'] = journal

paper_lists = [('Papers about Lean',
                sorted(about_lean_dic.values(),
                    key=lambda e: e.fields['year'],
                    reverse=True)),
               ('Papers about mathlib',
                sorted(about_mathlib_dic.values(),
                    key=lambda e: e.fields['year'],
                    reverse=True)),
               ('Formalization papers using Lean',
                sorted(formalization_papers_dic.values(),
                    key=lambda e: e.fields['year'],
                    reverse=True))]



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
        return { 'content': Path(template.filename).read_text(encoding='utf-8').replace('img/',
            base_url+'/img/'), 'name': template.name }

    def url(raw: str):
        return raw if raw.startswith('http') else base_url + raw

    latexnodes2text = LatexNodes2Text()
    def clean_tex(src: str) -> str:
        return latexnodes2text.latex_to_text(src)

    subprocess.run(['bibtool', '--preserve.key.case=on', '--preserve.keys=on',
        '--delete.field={website}', '--delete.field={tags}', '-s', '-i', 'lean.bib', '-o',
        str(target/'lean.bib')])

    site = Site.make_site(
            searchpath=TEMPLATE_SRC,
            outpath=str(target),
            extensions=[MarkdownExtension],
            rules = [
                ('.*.md', render_content)],
            contexts=[
                ('.*', default_context),
                ('index.html', {'presentation': presentation,
                                'what_is': what_is,
                                'formalizations': formalizations}),
                ('papers.html', {'paper_lists': paper_lists}),
                ('100.html', {'hundred_theorems': hundred_theorems}),
                ('100-missing.html', {'hundred_theorems': hundred_theorems}),
                ('meet.html', {'maintainers': maintainers,
                               'community': (DATA/'community.md').read_text( encoding='utf-8')}),
                ('undergrad.html', {'overviews': overviews}),
                ('undergrad_todo.html', {'overviews': overviews}),
                ('.*.md', get_contents)
                ],
            filters={ 'url': url, 'md': render_markdown, 'tex': clean_tex },
            mergecontexts=True)

    for folder in ['css', 'js', 'img', 'papers']:
        subprocess.call(['rsync', '-a', folder, str(target).rstrip('/')])
    subprocess.call(['rsync', '-a', 'googlef0c00cb4d31b246f.html', str(target).rstrip('/')])

    site.render(use_reloader=reloader)

if __name__ == '__main__':
    if '--local' in sys.argv:
        base_url = f"file://{(Path(__file__).parent/'build').absolute()}/"
    else:
        base_url = 'https://leanprover-community.github.io/'
    render_site(ROOT/'build', base_url, reloader='--reload' in sys.argv)
