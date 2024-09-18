"""
This module contains a class CustomHTMLRenderer, which uses
mistletoe to generate HTML from markdown.

Extra features include:
- Linkifying raw URLs
- Managing LaTeX so that MathJax will be able to process it in the browser
- Syntax highlighting with Pygments
"""
import re

from mistletoe import Document, HTMLRenderer, span_token
from pygments import highlight
from pygments.lexers import get_lexer_by_name as get_lexer
from pygments.formatters.html import HtmlFormatter

from mathjax_editing import remove_math, replace_math

class RawUrl(span_token.SpanToken):
    """
    Detect raw URLs.
    """
    parse_inner = False
    # regex to extract raw URLs from Markdown from:
    # https://github.com/trentm/python-markdown2/wiki/link-patterns#converting-links-into-links-automatically
    pattern = re.compile(
        r'((([A-Za-z]{3,9}:(?:\/\/)?)'  # scheme
        r'(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:\[0-9]+)?'  # user@hostname:port
        r'|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)'  # www.|user@hostname
        r'((?:\/[\+~%\/\.\w\-]*)?'  # path
        r'\??(?:[\-\+=&;%@\.\w]*)'  # query parameters
        r'#?(?:[\.\!\/\\\w\-]*))?)'  # fragment
        r'(?![^<]*?(?:<\/\w+>|\/?>))'  # ignore anchor HTML tags
        r'(?![^\(]*?\))'  # ignore links in brackets (Markdown links and images)
    )

    def __init__(self, match):
        self.url = match.group(1)

class CustomHTMLRenderer(HTMLRenderer):
    """
    The main rendering function is `render_md`.
    """
    def __init__(self):
        super().__init__(RawUrl)

    def render_md(self, ds):
        """
        A wrapper for this class's .render() function.

        Input is a string containing markdown with LaTeX,
        Output is a string containing HTML.

        Uses `mathjax_editing` to strip out sections of the text
        which potentially contain LaTeX and then splice them back in.
        """
        ds_no_math, math = remove_math(ds, '$')
        # We have to run `mathjax_editing.replace_math` on the text in code
        # blocks before passing it to Pygments (see `render_block_code`),
        # otherwise `replace_math` will be confused by the added syntax
        # highlighting `<span>`s and won't be able to splice in those blocks.
        self.math = math
        html = self.render(Document(ds_no_math))
        return replace_math(html, self.math)

    def render_heading(self, token) -> str:
        """
        Override the default heading to provide links like in GitHub.

        TODO: populate a list of table of contents in the `.toc_html` field of the body
        """
        template = '<h{level} id="{anchor}" class="markdown-heading">{inner} <a class="hover-link" href="#{anchor}">#</a></h{level}>'
        inner: str = self.render_inner(token)
        # generate anchor following what github does
        # See info and links at https://gist.github.com/asabaylus/3071099
        # We additionally "coarsely" attempt to strip out HTML tags from
        # anchors so that foo <code>bar</code> baz becomes foo-bar-baz not
        # foo-codebarcode-baz.
        anchor = inner.strip().lower()
        anchor = re.sub(r'<[^>]+>([^<]*)</[^>]+>', r'\1', anchor)
        anchor = re.sub(r'[^\w\- ]+', '', anchor).replace(' ', '-')
        return template.format(level=token.level, inner=inner, anchor=anchor)

    # Use pygments highlighting.
    # https://github.com/miyuchina/mistletoe/blob/8f2f0161b2af92f8dd25a0a55cb7d437a67938bc/contrib/pygments_renderer.py
    # HTMLCodeFormatter class copied from markdown2:
    # https://github.com/trentm/python-markdown2/blob/2c58d70da0279fe19d04b3269b04d360a56c01ce/lib/markdown2.py#L1826
    class HtmlCodeFormatter(HtmlFormatter):
        def _wrap_code(self, inner):
            """A function for use in a Pygments Formatter which
            wraps in <code> tags.
            """
            yield 0, "<code>"
            for tup in inner:
                yield tup
            yield 0, "</code>"

        def wrap(self, source):
            """Return the source with a code, pre, and div."""
            return self._wrap_div(self._wrap_pre(self._wrap_code(source)))

    # `cssclass` here should agree with what we have in pygments.css
    formatter = HtmlCodeFormatter(cssclass='codehilite')

    def render_block_code(self, token):
        # replace math before highlighting
        code = replace_math(token.children[0].content, self.math)
        # render mermaid code separately so that the javascript renderer can detect it properly
        if token.language == 'mermaid':
            s = '<pre class="mermaid">'
            s += code
            s += '</pre>'
            return s
        try:
            # default to 'lean' if no language is specified
            lexer = get_lexer(
                token.language) if token.language else get_lexer('lean')
        except:
            lexer = get_lexer('text')
        return highlight(code, lexer, self.formatter)

    def render_raw_url(self, token):
        """
        Linkify raw URLs.
        """
        return f'<a href="{token.url}">{token.url}</a>'
