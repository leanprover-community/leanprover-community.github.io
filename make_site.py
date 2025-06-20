#!/usr/bin/env python3

from enum import Enum, auto
from pathlib import Path
import shutil
import sys
import subprocess
import pickle
import re
from dataclasses import dataclass, field
from typing import List, Mapping, Optional, Any, Callable, TypeVar, Union
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

import zulip

FilePath = Union[str, Path]

DOWNLOAD = not 'NODOWNLOAD' in os.environ

def download(url: str, dest: Path) -> None:
    if DOWNLOAD:
        urllib.request.urlretrieve(url, dest)

DATA_CACHE = Path(__file__).parent/'data_cache'
DATA_CACHE.mkdir(exist_ok=True)

if not DOWNLOAD:
    print(f'NODOWNLOAD environment variable set, will try to recover data from {DATA_CACHE}')


def pkl_dump(filename: str, data: Any) -> None:
    """
    Dump the given data using pickle.
    """
    with open(DATA_CACHE/filename, 'wb') as pkl:
        pickle.dump(data, pkl, pickle.HIGHEST_PROTOCOL)

def pkl_load(filename: str, default: Any) -> Any:
    """
    Load data from the given file and return it or print a warning and return the default value.
    """
    if (DATA_CACHE/filename).exists():
        with open(DATA_CACHE/filename, 'rb') as pkl:
            return pickle.load(pkl)
    else:
        print(f"Warning: NODOWNLOAD environment variable set but couldn't find previously downloaded data {filename}.\nWill use default value {default}")
        return default

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
    """
    Data for a documentation entry for a single declaration.
    DocDecl objects are created from data in `header-data.json` and processed into HTML
    in `templates/100.html` and `templates/1000.html`.
    """

    name: str
    """Fully qualified name of the declaration"""
    decl_header_html: str
    """Full HTML code for this declaration's entry on its generated documentation page."""
    docs_link: str
    """URL of this declaration's entry in the generated documentation.
    This is site-relative, and starts with "/mathlib4_docs/"."""
    src_link: str
    """URL for this declaration's generated source entry: currently,
    is simply a link to the right revision of the mathlib source code."""

# keep in sync with scripts/yaml_check.py in the mathlib4 repo
@dataclass
class HundredTheorem:
    """Data of an entry about a single theorem in Freek's 100 theorems list:
    the webpages 100.html and 100-missing.html are generated automatically
    using this data."""
    # this theorem's number in Freek's 100 theorems list
    number: str
    # a human-readable title
    title: str
    # If a theorem is merely *stated* in mathlib, the name of the declaration
    statement: Optional[str] = None
    # if a theorem is formalized in mathlib, the archive or counterexamples,
    # the name of the corresponding declaration (optional)
    decl: Optional[str] = None
    # like |decl|, but a list of declarations (if one theorem is split into multiple declarations) (optional)
    decls: Optional[List[str]] = None
    # name(s) of the author(s) of this formalization (optional)
    authors: Optional[str] = None
    # Date of the formalization, in the form `YYYY`, `YYYY-MM` or `YYYY-MM-DD` (optional)
    date: Optional[str] = None
    links: Optional[Mapping[str, str]] = None
    note: Optional[str] = None

# keep in sync with scripts/yaml_check.py in the mathlib4 repo
# These field names match the names in the data files of the 1000+ theorems project upstream.
# See https://github.com/1000-plus/1000-plus.github.io/blob/main/README.md#file-format
# for the specification. Compared to the README,
# - this |wikidata| field concatenates the upstream fielcs |wikidata| and |id_suffix|
# - we omit some fields (for now), e.g. the msc classification, and only care about Lean formalizations
@dataclass
class ThousandPlusTheorem:
    """
    Data of an entry about a single theorem in Freek's experimental
    1000+ theorems project: the webpages 1000.html and 1000-missing.html
    are generated automatically using this data.
    """
    # Wikidata identifier (the letter Q followed by a string as digits),
    # optionally followed by a letter (such as "A", "B" or "X" for disambiguation).
    # "Q1008566" and "Q4724004A" are valid identifiers, for example.
    wikidata: str
    # a human-readable title
    title: str
    # If a theorem is merely *stated* in mathlib, the name of the declaration
    statement: Optional[str] = None
    # if a theorem is formalized in mathlib, the archive or counterexamples,
    # the name of the corresponding declaration (optional)
    decl: Optional[str] = None
    # like |decl|, but a list of declarations (if one theorem is split into multiple declarations) (optional)
    decls: Optional[List[str]] = None
    # name(s) of the author(s) of this formalization (optional)
    authors: Optional[str] = None
    # Date of the formalization, in the form `YYYY`, `YYYY-MM` or `YYYY-MM-DD` (optional)
    date: Optional[str] = None
    # for external projects, an URL referring to the result
    url: Optional[str] = None
    # any additional notes or comments
    comment: Optional[str] = None


@dataclass
class TheoremForWebpage:
    """
    Common abstraction for a theorem in the 100 or 1000+ theorems project lists.

    Both lists have slightly different formats, but very similar
    overall structure: this class allows sharing (almost) the same
    template for the webpage, while retaining the different input
    formats in both projects.

    Compared to just the theorems list, this class contains *additional*
    information, namely the full HTML source code for the generated
    documentation entries for all mathlib/archive/counterexamples
    declarations referenced there.
    """
    id: str
    title: str
    # Whether just the theorem statement has been formalized
    statement_formalized: bool
    # Whether this theorem's proof has been formalized
    proof_formalized: bool
    # The HTML source code for the generated documentation entries
    # for the declaration associated to this theorem.
    doc_decls: Optional[List[DocDecl]]
    links: Optional[Mapping[str, str]] = None
    # See above for the meaning of |authors|, |date| and |note|.
    authors: Optional[str] = None
    date: Optional[str] = None
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
    institution: str
    lean_version: int
    website: Optional[str] = None
    repo: Optional[str] = None
    material: Optional[str] = None
    notes : Optional[str] = None
    tags: List[str] = field(default_factory=list)
    year: int = 2023
    summary : Optional[str] = None
    experiences : Optional[str] = None

if DOWNLOAD:
    print('Downloading header-data.json...') #  This is a slow operation, so let's inform readers.
    # header-data.json contains information for every single declaration in mathlib
    # which has a generated documentation entry (e.g., skipping private declarations by default).
    # The resulting file is huge (several hundred MB), hence we use a small HACK:
    # doc-gen4 uploads this file as a .bmp file, so GitHub's servers will serve it in
    # compressed form. When downloading it locally, we save it (decompressed) with the correct extension.
    download(
        'https://leanprover-community.github.io/mathlib4_docs/declarations/header-data.bmp',
        DATA/'header-data.json'
    )
    print('Downloaded.')
if (DATA/'header-data.json').exists():
    print('Parsing header-data.json...') #  This is a slow operation, so let's inform readers.
    with (DATA/'header-data.json').open('r', encoding='utf-8') as h_file:
        header_data = json.load(h_file)
    print('Parsed.')
else:
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

class NTheorems(Enum):
    Hundred = auto()
    ThousandPlus = auto()

def download_N_theorems(kind: NTheorems) -> dict:
    if kind == NTheorems.Hundred:
        (fname, Type, name) = ('100.yaml', HundredTheorem, 'hundred_theorems')
    else:
        (fname, Type, name) = ('1000.yaml', ThousandPlusTheorem, 'thousand_theorems')
    if DOWNLOAD:
        download(f'https://leanprover-community.github.io/mathlib4_docs/{fname}', DATA/fname)
        with (DATA/fname).open('r', encoding='utf-8') as h_file:
            n_theorems = [Type(thm, **content) for (thm, content) in yaml.safe_load(h_file).items()]
            theorems = []
            for h in n_theorems:
                assert not (h.decl and h.decls)
                assert not (h.statement and (h.decl or h.decls))
                statement_formalized = False
                if kind == NTheorems.Hundred:
                    (id, links, thms, note) = (h.number, h.links, '100 theorems', h.note)
                else:
                    (id, links, thms, note) = (h.wikidata, {'url': h.url} if h.url else {}, '1000+ theorems', h.comment)
                    if h.statement:
                        statement_formalized = True
                # A theorem's proof counts as formalized if the authors or `decl`(s) field is non-empty.
                proof_formalized = bool(h.authors) or h.decls or h.decl
                decls = h.decls or ([h.decl] if h.decl else []) or ([h.statement] if h.statement else [])
                doc_decls = []
                if decls:
                    for decl in decls:
                        try:
                            decl_info = declarations[decl]
                        except KeyError:
                            print(f'Error: {thms} entry {id} refers to a nonexistent declaration {decl}')
                            continue
                        # note: the `header-data.json` data file uses doc-relative links
                        header = decl_info.header.replace('href="./Mathlib/', 'href="./mathlib4_docs/Mathlib/')
                        doc_decls.append(DocDecl(
                            name=decl,
                            decl_header_html = header,
                            # note: the `header-data.json` data file uses doc-relative links
                            docs_link='/mathlib4_docs/' + decl_info.info.docLink,
                            src_link=decl_info.info.sourceLink))

                theorems.append(TheoremForWebpage(id, h.title, statement_formalized, proof_formalized, doc_decls, links, h.authors, h.date, note))
        pkl_dump(name, theorems)
    else:
        theorems = pkl_load(name, dict())
    return theorems
hundred_theorems = download_N_theorems(NTheorems.Hundred)
thousand_theorems = download_N_theorems(NTheorems.ThousandPlus)

def replace_link(name, id):
    if name == '':
        return name
    elif '/' in name:
        return '/mathlib4_docs/' + name
    else:
        try:
            # note: the `header-data.json` data file uses doc-relative links
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

if DOWNLOAD:
    download(
        'https://leanprover-community.github.io/mathlib4_docs/overview.yaml',
        DATA/'overview.yaml')
    with (DATA/'overview.yaml').open('r', encoding='utf-8') as h_file:
        overviews = [Overview.from_top_level(index, title, elements) for index, (title, elements) in enumerate(yaml.safe_load(h_file).items())]
    pkl_dump('overviews', overviews)
else:
    overviews = pkl_load('overviews', [])

if DOWNLOAD:
    download(
        'https://leanprover-community.github.io/mathlib4_docs/undergrad.yaml',
        DATA/'undergrad.yaml')
    with (DATA/'undergrad.yaml').open('r', encoding='utf-8') as h_file:
        undergrad_overviews = [Overview.from_top_level(index, title, elements) for index, (title, elements) in enumerate(yaml.safe_load(h_file).items())]
    pkl_dump('undergrad_overviews', undergrad_overviews)
else:
    undergrad_overviews = pkl_load('undergrad_overviews', [])

with (DATA/'theories_index.yaml').open('r', encoding='utf-8') as h_file:
    theories = yaml.safe_load(h_file)

with (DATA/'events.yaml').open('r', encoding='utf-8') as h_file:
    events = [Event(**e) for e in yaml.safe_load(h_file)]

with (DATA/'courses.yaml').open('r', encoding='utf-8') as h_file:
    courses = [Course(**e) for e in yaml.safe_load(h_file)]
courses_tags = set()
courses.sort(key=lambda c: (-c.lean_version, -c.year, c.name))
for course in courses:
    courses_tags.update(course.tags)
    course.tags.sort()
    course.tags.append(f'lean{course.lean_version}')
    for field in ['experiences', 'notes', 'summary', 'experiences']:
        val = getattr(course, field)
        if isinstance(val, str):
            setattr(course, field, render_markdown(val))
        elif isinstance(val, list):
            setattr(course, field, render_markdown("\n".join(map(lambda v: "* " + v, val))))
courses_tags = ['lean4', 'lean3'] + sorted(list(courses_tags))

# Cannot use %-d format code on windows
def format_month_day(date_obj):
    return f"{date_obj.strftime('%B')} {date_obj.day}"
def format_month_day_year(date_obj):
    return f"{date_obj.strftime('%B')} {date_obj.day}, {date_obj.year}"
def format_day_year(date_obj):
    return f"{date_obj.day}, {date_obj.year}"

def format_date_range(event):
    if event.start_date and event.end_date:
        start_date = datetime.strptime(event.start_date, '%B %d %Y').date()
        end_date = datetime.strptime(event.end_date, '%B %d %Y').date()
        if start_date.year != end_date.year:
            return f'{format_month_day_year(start_date)}–{format_month_day_year(end_date)}'
        elif start_date.month != end_date.month:
            return f'{format_month_day(start_date)}–{format_month_day_year(end_date)}'
        elif start_date.day != end_date.day:
            return f'{format_month_day(start_date)}–{format_day_year(end_date)}'
        else:
            return format_month_day_year(start_date)
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

github = Github(os.environ.get('GITHUB_TOKEN', None))

if DOWNLOAD:
    download(
        'https://leanprover-contrib.github.io/leanprover-contrib/projects/projects.yml',
        DATA/'projects.yaml')
    with (DATA/'projects.yaml').open('r', encoding='utf-8') as h_file:
        oprojects = yaml.safe_load(h_file)
    pkl_dump('oprojects', oprojects)
else:
    oprojects = pkl_load('oprojects', [])


projects = []
if DOWNLOAD:
    for name, project in oprojects.items():
        if project.get('display', True):
            github_repo = github.get_repo(project['organization'] + '/' + name)
            stars = github_repo.stargazers_count
            descr = render_markdown(project['description'])
            projects.append(Project(name, project['organization'], descr, project['maintainers'], stars))
            projects.sort(key = lambda p: p.stars, reverse=True)
    pkl_dump('projects', projects)
else:
    projects = pkl_load('projects', [])

if DOWNLOAD:
    # We used to use this count but it didn't include mathlib3 contributors
    # num_contrib = github.get_repo('leanprover-community/mathlib4').get_contributors(anon=True).totalCount
    # The `contributor-count` file is uploaded by the github workflow in the mathlib_stats repo:
    download(
        'https://leanprover-community.github.io/mathlib_stats/contributor-count',
        DATA/'contributor-count')
    with (DATA/'contributor-count').open('r', encoding='utf-8') as h_file:
        # we could just display the file contents directly,
        # but better to try to convert to a number and error out if something unexpected is there
        num_contrib = int(h_file.readline().strip())
    pkl_dump('num_contrib', num_contrib)
else:
    num_contrib = pkl_load('num_contrib', 0)

if DOWNLOAD:
    download(
        'https://leanprover-contrib.github.io/leanprover-contrib/version_history.yml',
        DATA/'project_history.yaml')
    with (DATA/'project_history.yaml').open('r', encoding='utf-8') as h_file:
        project_history = yaml.safe_load(h_file)
    pkl_dump('project_history', project_history)
else:
    project_history = pkl_load('project_history', dict())


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

@dataclass
class User:
    fullname: str
    lon: float
    lat: float
    github: Optional[str] = None
    website: Optional[str] = None

if DOWNLOAD and 'ZULIP_KEY' in os.environ:
    client = zulip.Client(
        email='map-scraper-bot@leanprover.zulipchat.com',
        site='https://leanprover.zulipchat.com',
        api_key=os.environ.get('ZULIP_KEY'))
else:
    client = None

# Zulip custom profile fields are tracked by ID, not by name
profile_data_fields = {
    'website': '5151',
    'latitude': '5148',
    'longitude': '5149',
    'github': '3658'
}

def get_user_field(user, field):
    field_id = profile_data_fields[field]
    try:
        return user['profile_data'][field_id]['value']
    except KeyError:
        return None


def httpize_website(user):
    website = get_user_field(user, 'website')
    if website is not None and not website.startswith('http'):
        return 'https://' + website
    else:
        return website

if client is None:
    # Here we don't use pkl_load because its potential failure
    # message would be confusing in the absence of a Zulip API key.
    if (DATA_CACHE/'users').exists():
        with open(DATA_CACHE/'users', 'rb') as pkl:
            users = pickle.load(pkl)
    else:
        print(f"Warning: Could not find Zulip authentication information and couldn't find previously downloaded data. \nWill use an empty users list.")
        users = []
else:
    users = []
    for user in client.get_members({"include_custom_profile_fields": True})['members']:
        if user['is_bot'] or not user['is_active']:
            continue
        try:
            lat = float(get_user_field(user, 'latitude'))
            lon = float(get_user_field(user, 'longitude'))
        except Exception:
            continue
        users.append(User(
            fullname=user['full_name'],
            lon=lon,
            lat=lat,
            github=get_user_field(user, 'github'),
            website=httpize_website(user)))
    pkl_dump('users', users)

class LeanSite(Site):
    """
    Very light customization of the staticjinja Site class that allow
    template filtering.
    """
    def __init__(
        self,
        environment: Environment,
        searchpath: FilePath,
        outpath: FilePath = ".",
        encoding = "utf8",
        contexts= None,
        rules = None,
        staticpaths = None,
        mergecontexts = False,
        template_filter: Callable[[str], bool] = lambda s: True
    ) -> None:
        super().__init__(environment, searchpath, outpath, encoding, contexts, rules, staticpaths, mergecontexts)
        self.template_filter = template_filter

    @classmethod
    def make_site(
        cls,
        searchpath: FilePath = "templates",
        outpath: FilePath = ".",
        contexts = None,
        rules = None,
        encoding = "utf8",
        followlinks = True,
        extensions = None,
        staticpaths = None,
        filters = {},
        env_globals = {},
        env_kwargs = None,
        mergecontexts: bool = False,
        template_filter: Callable[[str], bool] = lambda s: True
    ):
        site = super().make_site(searchpath, outpath, contexts, rules, encoding, followlinks, extensions, staticpaths, filters, env_globals, env_kwargs, mergecontexts)
        site.template_filter = template_filter
        return site

    @property
    def template_names(self) -> List[str]:
        return self.env.list_templates(filter_func=lambda s: self.is_template(s) and self.template_filter(s))

def render_site(target: Path, base_url: str, reloader=False, only: Optional[str] = None):
    default_context = lambda: {
            'base_url': base_url,
            'menus': menus,
            }
    target.mkdir(parents=True, exist_ok=True)

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

    try:
        subprocess.run(['bibtool', '--preserve.key.case=on', '--preserve.keys=on',
            '--delete.field={website}', '--delete.field={tags}', '-s', '-i', 'lean.bib', '-o',
            str(target/'lean.bib')], check=True)
    except FileNotFoundError:
        print("Warning: bibtool not found. Copying lean.bib without processing.")
        shutil.copy2('lean.bib', target/'lean.bib')

    def read_md(src: str) -> str:
        return (DATA/src).read_text(encoding='utf-8')

    if only:
        tpl_filter_re = re.compile(only)
        template_filter = tpl_filter_re.match
    else:
        template_filter = lambda n: True

    site = LeanSite.make_site(
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
                ('1000.html', {'thousand_theorems': thousand_theorems}),
                ('1000-missing.html', {'thousand_theorems': thousand_theorems}),
                ('meet.html', {'users': users,
                               'community': read_md('community.md')
                               }),
                ('mathlib-overview.html', {'overviews': overviews, 'theories': theories}),
                ('undergrad.html', {'overviews': undergrad_overviews}),
                ('undergrad_todo.html', {'overviews': undergrad_overviews}),
                ('mathlib_stats.html', {'num_defns': num_defns, 'num_thms': num_thms, 'num_contrib': num_contrib}),
                ('lean_projects.html', {'projects': projects}),
                ('events.html', {'old_events': old_events, 'new_events': new_events}),
                ('teaching/courses.html', {'courses': courses, 'tags': courses_tags}),
                ('teams.html', {'introduction': read_md('teams_intro.md'), 'teams': teams}),
                ('.*.md', get_contents)
                ],
            filters={ 'url': url, 'md': render_markdown, 'tex': clean_tex },
            mergecontexts=True,
            template_filter=template_filter)

    # Now build the individual team pages
    (target/'teams').mkdir(exist_ok=True)
    env = Environment(loader=FileSystemLoader('templates'))
    env.filters={ 'url': url, 'md': render_markdown, 'tex': clean_tex }
    team_tpl = env.get_template('_team.html')
    for team in teams:
        with (target/'teams'/(team.url + '.html')).open('w') as tgt_file:
            team_tpl.stream(team=team, menus=menus, base_url=base_url).dump(tgt_file)


    for folder in ['css', 'js', 'img', 'papers', str(target/'teams')]:
        subprocess.call(['rsync', '-a', folder, str(target).rstrip('/')])
    subprocess.call(['rsync', '-a', 'googlef0c00cb4d31b246f.html', str(target).rstrip('/')])
    subprocess.call(['rsync', '-a', 'robots.txt', str(target).rstrip('/')])

    site.render(use_reloader=reloader)

if __name__ == '__main__':
    try:
        only = sys.argv[sys.argv.index('--only')+1]
    except:
        only = None
    if '--local' in sys.argv:
        base_url = f"file://{(Path(__file__).parent/'build').absolute()}/"
    else:
        base_url = 'https://leanprover-community.github.io/'
    render_site(ROOT/'build', base_url, reloader='--reload' in sys.argv, only=only)
