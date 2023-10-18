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

@dataclass
class Formalization:
    title: str
    authors: str
    abstract: str
    url: str

with (DATA/'formalizations.yaml').open('r', encoding='utf-8') as f_file:
    formalizations = [Formalization(**form) for form in yaml.safe_load(f_file)]

@dataclass
class People:
    name: str
    descr: str = ''
    img: str = ''

with (DATA/'people.yaml').open('r', encoding='utf-8') as m_file:
    peoples = {mtr['name']: People(**mtr) for mtr in yaml.safe_load(m_file)}

@dataclass
class Team:
    name: str
    short_description: str
    description: str
    url: str
    members: List[People]
    use_biography: bool = False

with (DATA/'teams.yaml').open('r', encoding='utf-8') as t_file:
    teams = [Team(team['name'], team['short_description'],
                  team['description'], team['url'],
                  [peoples.get(name, People(name)) for name in sorted(team['members'])],
                  use_biography=team.get('use_biography', True))
             for team in yaml.safe_load(t_file)]

@dataclass
class DocDecl:
    name: str
    decl_header_html: str
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

@dataclass
class Event:
    title: str
    location: str
    type: str
    url: str = 'TBA'
    start_date: str = ''
    end_date: str = ''
    date_range: str = 'TBA'

@dataclass
class Course:
    name: str
    instructor: str
    location: str
    website: str
    repo: Optional[str] = None
    material: Optional[str] = None
    notes : Optional[str] = None
    tags: List[str] = field(default_factory=list)
    year: int = 2023
    summary : Optional[str] = None
    experiences : Optional[str] = None

header_data = dict()

@dataclass
class HeaderDataEntry:
    @dataclass
    class InfoEntry:
        sourceLink: str
        name: str
        line: int
        kind: str
        docLink: str
        doc: str
    info: InfoEntry
    header: str

declarations = {
    k: HeaderDataEntry(
        info=HeaderDataEntry.InfoEntry(**d['info']),
        header=d['header'],
    ) for k, d in header_data.items()
}

num_thms = len([d for d in declarations if declarations[d].info.kind == 'theorem'])
num_defns = len(declarations) - num_thms

hundred_theorems = []

def replace_link(name, id):
    if name == '':
        return name
    elif '/' in name:
        return '/mathlib4_docs/' + name
    else:
        try:
            # note: the `.bmp` data files use doc-relative links
            return '/mathlib4_docs/' + declarations[name].info.docLink
        except KeyError:
            raise KeyError(f'Error: overview item {id} refers to a nonexistent declaration {name}')

@dataclass
class Overview:
    id: str
    depth: int
    title: str
    decl: Optional[str] = None
    url: Optional[str] = None
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

    @property
    def nonempty_children(self) -> List['Overview']:
        return [item for item in self.children if item.is_nonempty]

    @property
    def missing_children(self) -> List['Overview']:
        return [item for item in self.children if item.has_missing_child]

    @property
    def slug(self) -> str:
        return slugify(self.title)

    @classmethod
    def from_node(cls, identifier: str, title: str, children, depth: int, parent: 'Overview' = None) -> 'Overview':
        is_leaf = not isinstance(children, dict)
        decl = None
        url = None
        if is_leaf:
            if children and 'http' in children:
                url = children
            else:
                decl = replace_link((children or '').strip(), identifier)
        node = cls(
                id=identifier,
                depth=depth,
                title=title,
                decl=decl,
                url=url,
                parent=parent,
                children=[])

        if not is_leaf:
            node.children = [cls.from_node(f"{identifier}-{index}", title, subchildren, depth + 1, parent=node) for index, (title, subchildren) in enumerate(children.items())]

        return node

    @classmethod
    def from_top_level(cls, index: int, title: str, children) -> 'Overview':
        return cls.from_node(f"{index}", title, children, 0)


overviews = []
undergrad_overviews = []
theories = []
events = []

with (DATA/'courses.yaml').open('r', encoding='utf-8') as h_file:
    courses = [Course(**e) for e in yaml.safe_load(h_file)]
courses.sort(key=lambda c: (0 if 'lean4' in c.tags else 1, -c.year, c.name))
for course in courses:
    for field in ['experiences', 'notes', 'summary', 'experiences']:
        val = getattr(course, field)
        if isinstance(val, str):
            setattr(course, field, render_markdown(val))
        elif isinstance(val, list):
            setattr(course, field, render_markdown("\n".join(map(lambda v: "* " + v, val))))

def format_date_range(event):
    if event.start_date and event.end_date:
        start_date = datetime.strptime(event.start_date, '%B %d %Y').date()
        end_date = datetime.strptime(event.end_date, '%B %d %Y').date()
        if start_date.year != end_date.year:
            return f'{start_date.strftime("%B %-d, %Y")}–{end_date.strftime("%B %-d, %Y")}'
        elif start_date.month != end_date.month:
            return f'{start_date.strftime("%B %-d")}–{end_date.strftime("%B %-d, %Y")}'
        elif start_date.day != end_date.day:
            return f'{start_date.strftime("%B %-d")}–{end_date.strftime("%-d, %Y")}'
        else:
            return start_date.strftime("%B %-d, %Y")
    else:
        return 'TBA'

present = datetime.now().date()
old_events = sorted((e for e in events if e.end_date and datetime.strptime(e.end_date, '%B %d %Y').date() < present), key=lambda e: datetime.strptime(e.end_date, '%B %d %Y').date(), reverse=True)
new_events = sorted((e for e in events if (not e.end_date) or datetime.strptime(e.end_date, '%B %d %Y').date() >= present), key=lambda e: datetime.strptime(e.end_date, '%B %d %Y').date())

for e in old_events + new_events:
    e.date_range = format_date_range(e)


@dataclass
class Project:
    name: str
    organization: str
    description: str
    maintainers: List[str]
    stars: int


projects = []

num_contrib = 0

project_history = dict()
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
        elif (('archivePrefix' in data.fields and data.fields['archivePrefix'] == 'arXiv') or
            ('eprinttype' in data.fields and data.fields['eprinttype'] == 'arXiv')):
            url = 'https://arxiv.org/abs/'+eprint
        else:
            url = eprint
    else:
        raise ValueError(f"Couldn't find a url for bib item {key}")
    if url.startswith(r'\url'):
        url = url[4:].strip('{}')
    url = url.replace(r'\_', '_')
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
            'menus': menus,
            }

    def render_content(env, template, **kwargs):
        """Render a markdown template."""
        content_template = env.get_template("_markdown.html")
        path = Path(template.name)
        title = path.with_suffix('').name
        (target/path.parent).mkdir(parents=True, exist_ok=True)
        content_template.stream(**kwargs).dump(str(target/path.parent/title)+'.html')

    def get_contents(template):
        src = Path(template.filename).read_text(encoding='utf-8').replace('img/',
                base_url+'/img/')
        doc = Document(src)
        content = render_markdown(src).strip()
        title = ''
        for child in doc.children:
            if isinstance(child, block_token.Heading):
                title = child.children[0].content
                break

        return { 'content': content, 'name': template.name,
                 'title': title }

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
                ('meet.html', {'community': (DATA/'community.md').read_text(encoding='utf-8')}),
                ('mathlib-overview.html', {'overviews': overviews, 'theories': theories}),
                ('undergrad.html', {'overviews': undergrad_overviews}),
                ('undergrad_todo.html', {'overviews': undergrad_overviews}),
                ('mathlib_stats.html', {'num_defns': num_defns, 'num_thms': num_thms, 'num_contrib': num_contrib}),
                ('lean_projects.html', {'projects': projects}),
                ('events.html', {'old_events': old_events, 'new_events': new_events}),
                ('courses.html', {'courses': courses}),
                ('teams.html', {'introduction': (DATA/'teams_intro.md').read_text(encoding='utf-8'), 'teams': teams}),
                ('.*.md', get_contents)
                ],
            filters={ 'url': url, 'md': render_markdown, 'tex': clean_tex },
            mergecontexts=True)


    site.render(use_reloader=reloader)

if __name__ == '__main__':
    if '--local' in sys.argv:
        base_url = f"file://{(Path(__file__).parent/'build').absolute()}/"
    else:
        base_url = 'https://leanprover-community.github.io/'
    render_site(ROOT/'build', base_url, reloader='--reload' in sys.argv)
