import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from types import SimpleNamespace

from jinja2 import ChoiceLoader, DictLoader, Environment, FileSystemLoader

from hundred_theorems import HundredTheorem, hundred_context, load_external_hundred
from mistletoe_renderer import CustomHTMLRenderer

ROOT = Path(__file__).resolve().parents[1]


def catalogue(external):
    titles = {t.id: t.title for t in external}
    external_only = set(titles) - {96, 100}
    return [
        SimpleNamespace(
            id=n,
            title=titles.get(n, f"Theorem {n}"),
            proof_formalized=n not in external_only,
            statement_formalized=n == 33,
            authors="Mathlib Author" if n not in external_only else None,
            doc_decls=[
                SimpleNamespace(
                    decl_header_html=f"<code>mathlib_proof_{n}</code>",
                    docs_link=f"/mathlib4_docs/test.html#proof_{n}",
                    src_link=f"https://github.com/leanprover-community/mathlib4/blob/master/Test.lean#L{n}",
                )
            ]
            if n not in external_only
            else [],
            links=None,
            note=None,
        )
        for n in range(1, 101)
    ]


class Page(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.ids = []
        self.sections = {}
        self.current_section = None
        self.hrefs = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            identifier = attrs["id"]
            self.ids.append(identifier)
            if tag == "h2":
                self.current_section = identifier
            self.sections[identifier] = self.current_section
        if tag == "a":
            self.hrefs.append(attrs.get("href"))


class DataTests(unittest.TestCase):
    def test_legacy_external_authors_do_not_count_as_mathlib(self):
        external = HundredTheorem(
            5,
            "Prime Number Theorem",
            authors="External author",
            links={"proof": "https://example.com/proof"},
        )
        self.assertFalse(external.in_mathlib)
        self.assertFalse(
            HundredTheorem(33, "Fermat", statement="FermatLastTheorem").in_mathlib
        )
        self.assertTrue(
            HundredTheorem(1, "Sqrt", decl="irrational_sqrt_two").in_mathlib
        )
        self.assertTrue(
            HundredTheorem(7, "Reciprocity", decls=["quadratic_reciprocity"]).in_mathlib
        )

    def load_text(self, text):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "external.yaml"
            path.write_text(text)
            return load_external_hundred(path)

    def test_rejects_duplicate_numbers_and_fields(self):
        for text in (
            '5: {title: PNT, links: {proof: "https://example.com"}}\n5: {}',
            '5: {title: PNT, title: Other, links: {proof: "https://example.com"}}',
        ):
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.load_text(text)

    def test_rejects_missing_proofs_invalid_numbers_and_urls(self):
        for text in (
            '101: {title: Invalid, links: {proof: "https://example.com"}}',
            "5: {title: PNT, links: {}}",
            '5: {title: PNT, links: {proof: "javascript:alert(1)"}}',
        ):
            with self.subTest(text=text), self.assertRaises(ValueError):
                self.load_text(text)

    def test_internal_declarations_do_not_belong_in_external_data(self):
        for key in ("decl", "decls", "statement"):
            with self.subTest(key=key), self.assertRaises(TypeError):
                self.load_text(
                    '5: {title: PNT, links: {proof: "https://example.com"}, '
                    + key
                    + ": x}"
                )

    def test_rereads_local_data_without_a_download_cache(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "external.yaml"
            path.write_text(
                '5: {title: PNT, links: {proof: "https://example.com/old"}}'
            )
            first = load_external_hundred(path)
            path.write_text(
                '5: {title: PNT, links: {proof: "https://example.com/new"}}'
            )
            second = load_external_hundred(path)
            self.assertNotEqual(first[0].links, second[0].links)

    def test_checked_in_authors_exclude_models_and_notes_preserve_provenance(self):
        external = load_external_hundred(ROOT / "data/100-external.yaml")
        for theorem in external:
            with self.subTest(number=theorem.id):
                self.assertNotRegex(
                    theorem.authors or "", r"Claude|ChatGPT|Codex|Aristotle|Grok"
                )
        pascal = next(t for t in external if t.id == 28)
        self.assertIn("Aristotle", pascal.note)
        self.assertIn("ChatGPT", pascal.note)


class ContextTests(unittest.TestCase):
    def setUp(self):
        self.external = load_external_hundred(ROOT / "data/100-external.yaml")
        self.theorems = catalogue(self.external)

    def test_union_counts_overlapping_formalizations_once(self):
        context = hundred_context(self.theorems, self.external)
        self.assertEqual(context["mathlib_hundred_count"], 78)
        self.assertEqual(len(context["external_hundred_theorems"]), 24)
        self.assertEqual(context["lean_hundred_count"], 100)
        self.assertEqual(context["missing_hundred_theorems"], [])

    def test_missing_considers_both_lists_and_statement_only_entries(self):
        external = [t for t in self.external if t.id != 33]
        context = hundred_context(self.theorems, external)
        self.assertEqual([t.id for t in context["missing_hundred_theorems"]], [33])
        self.assertEqual(context["statement_only_hundred_count"], 1)
        self.assertEqual(context["lean_hundred_count"], 99)

    def test_rejects_incomplete_or_duplicate_mathlib_numbering(self):
        for theorems in (self.theorems[:-1], self.theorems[:-1] + [self.theorems[0]]):
            with self.assertRaises(ValueError):
                hundred_context(theorems, self.external)


class RenderingTests(unittest.TestCase):
    def setUp(self):
        self.external = load_external_hundred(ROOT / "data/100-external.yaml")
        self.theorems = catalogue(self.external)
        self.env = Environment(
            loader=ChoiceLoader(
                [
                    DictLoader(
                        {
                            "_base.html": "<html><head><title>{% block title %}{% endblock %}</title>"
                            "</head><body>{% block content %}{% endblock %}</body></html>"
                        }
                    ),
                    FileSystemLoader(str(ROOT / "templates")),
                ]
            )
        )
        self.env.filters["md"] = CustomHTMLRenderer().render_md

    def render(self, template, external=None):
        context = hundred_context(
            self.theorems, self.external if external is None else external
        )
        return self.env.get_template(template).render(**context)

    def test_separate_sections_unique_and_stable_anchors(self):
        html = self.render("100.html")
        page = Page(html)
        self.assertEqual(len(page.ids), len(set(page.ids)))
        for n in range(1, 101):
            self.assertIn(str(n), page.ids)
        self.assertEqual(page.sections["47"], "in-mathlib")
        self.assertEqual(page.sections["5"], "other-lean-projects")
        self.assertEqual(page.sections["96"], "in-mathlib")
        self.assertEqual(page.sections["external-96"], "other-lean-projects")
        self.assertEqual(page.sections["external-100"], "other-lean-projects")
        self.assertIn("78 are proved in Mathlib and 100", html)

    def test_preserves_every_external_proof_link_and_credit(self):
        html = self.render("100.html")
        page = Page(html)
        for theorem in self.external:
            with self.subTest(number=theorem.id):
                for url in theorem.links.values():
                    self.assertIn(url, page.hrefs)
                if theorem.authors:
                    self.assertIn(theorem.authors, html)
        self.assertIn("Aristotle", html)
        self.assertIn("ChatGPT-5.2 Pro", html)
        self.assertIn("mathlib_proof_47", html)

    def test_missing_page_has_no_false_negatives_for_external_proofs(self):
        html = self.render("100-missing.html")
        self.assertIn("All 100 theorems have a listed Lean formalization", html)
        self.assertNotIn("<li>", html)
        html = self.render("100-missing.html", [t for t in self.external if t.id != 33])
        self.assertIn("33: Fermat", html)
        self.assertNotIn("All 100", html)


if __name__ == "__main__":
    unittest.main()
