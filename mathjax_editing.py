# Ported / adapted from <https://dev.sstatic.net/Js/mathjax-editing.en.js>

# The MIT License (MIT)
#
# Copyright (c) 2016 Stack Exchange
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
This module contains two functions useful for working with markdown strings
that may contain LaTeX that should be processed with MathJax.

`remove_math` strips out parts of the markdown that could potentially contain
math and `replace_math` puts the math back in.
"""

import re
from typing import Match, List

SPLIT = re.compile(r'(\$\$?|\\(?:begin|end)\{[a-z]*\*?\}|\\[\\{}$]|[{}]|(?:\n\s*)+|@@\d+@@|`+)', re.I)

def remove_math(text: str, inline: str) -> dict:
    """
    text: input markdown string
    inline: symbol for inline math (usually '$')

    returns a tuple (stripped_text, math)

    stripped_text: the input string with math replaced by @@number@@
    math: a list of the removed math strings

    Break up the text into its component parts and search
    through them for math delimiters, braces, linebreaks, etc.
    Math delimiters must match and braces must balance.
    Don't allow math to pass through a double linebreak
    (which will be a paragraph).
    Handle backticks (don't do math inside them)
    """

    def process_math(i: int, j: int) -> None:
        """
        The math is in blocks i through j, so
        collect it into one block and clear the others.
        # Replace &, <, and > by named entities.
        Clear the current math positions and store the index of the
        math, then push the math string onto the storage array.
        """
        nonlocal blocks, start, end, last
        # TODO: replacing >, <, & seems to screw up code blocks
        # block = re.sub(r'>',"&gt;",
        #     re.sub(r'<',"&lt;",
        #     re.sub(r'&',"&amp;",
        #     "".join(blocks[i:j+1]))))
        block = "".join(blocks[i:j+1])
        if indent:
            block = re.sub(r'\n    ', '\n', block)
        while j > i:
            blocks[j] = ""
            j -= 1
        blocks[i] = f"@@{len(math)}@@"
        math.append(block)
        start = None
        end = None
        last = None

    start = None
    end = None
    last = None
    indent = None # for tracking math delimiters
    braces = None
    math: List[str] = [] # stores math strings for latter

    blocks: List[str] = re.split(SPLIT, re.sub(r'\r\n?', "\n", text))

    i = 1
    m = len(blocks)
    while i < m:
        block = blocks[i]
        if block[0] == "@":
            #
            # Things that look like our math markers will get
            # stored and then retrieved along with the math.
            #
            blocks[i] = f"@@{len(math)}@@"
            math.append(block)
        elif start:
            #
            # If we are in math or backticks,
            #   look for the end delimiter,
            #   but don't go past double line breaks,
            #   and balance braces within the math,
            #   but don't process math inside backticks.
            #
            if block == end:
                if braces > 0:
                    last = i
                elif braces == 0:
                    process_math(start, i)
                else:
                    start = None
                    end = None
                    last = None
            elif re.search(r'\n.*\n', block) or i + 2 >= m:
                if last:
                    i = last
                    if braces >= 0:
                        process_math(start, i)
                start = None
                end = None
                last = None
                braces = 0
            elif block == "{" and braces >= 0:
                braces += 1
            elif block == "}" and braces > 0:
                braces -= 1
        else:
            #
            # Look for math start delimiters and when
            #   found, set up the end delimiter.
            #
            if block == inline or block == "$$":
                start = i
                end = block
                braces = 0
            elif block[1:6] == "begin":
                start = i
                end = "\\end" + block[6:]
                braces = 0
            elif block[0] == "`":
                start = i
                last = i
                end = block
                braces = -1 # no brace balancing
            elif block[0] == "\n":
                if re.search(r'    $', block):
                    indent = True
        i += 2

    if last:
        process_math(start, last)


    def double_escape_delimiters(text: str, inline: str) -> str:
        """
        the commonmark renderer will render any `\$` as a simple `$`
        which could become a problem if `$` is used as a mathjax inline delimiter
        because then even escaped equations (starting with `\$`) would be detected
        as mathjax equations. Let's double-escape to make sure we still have a `\$`
        after commonmark did its conversion.
        """
        if not inline.startswith("\\"):
            return re.sub(r'\\\$', '\\\\$', text)
        return text

    return (double_escape_delimiters("".join(blocks), inline), math)


def replace_math(input: str, math: List[str]) -> str:
    """
    input: a string, already processed into HTML by some markdown renderer;
    may contain @@number@@ blocks indicating where math was removed by
    remove_math.

    math: a list of strings containing math blocks to be spliced back into input

    Put back the math strings that were saved
    """

    def replacer(match: Match):
        index = int(match.group(1))
        return math[index]

    text = re.sub(r'@@(\d+)@@', replacer, input)
    return text
