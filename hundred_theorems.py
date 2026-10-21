"""Separate Mathlib's theorem catalogue from website-owned external formalizations."""

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

import yaml


# Keep in sync with scripts/yaml_check.py in Mathlib, except for legacy links:
# deployed documentation can lag behind the removal of external metadata there.
@dataclass
class HundredTheorem:
    number: int
    title: str
    statement: str | None = None
    decl: str | None = None
    decls: list[str] | None = None
    authors: str | None = None
    date: str | None = None
    links: Mapping[str, str] | None = None
    note: str | None = None

    @property
    def in_mathlib(self):
        # Legacy authors/links alone must never count as a Mathlib proof.
        return bool(self.decl or self.decls)


@dataclass
class ExternalHundredTheorem:
    id: int
    title: str
    links: Mapping[str, str]
    authors: str | None = None
    date: str | None = None
    note: str | None = None


class UniqueKeysLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in result:
                raise ValueError(f"Duplicate external theorem data key: {key}")
            result[key] = self.construct_object(value_node, deep=deep)
        return result


def load_external_hundred(path: Path):
    """Read checked-in data on every build, including NODOWNLOAD builds."""
    with path.open(encoding="utf-8") as source:
        rows = yaml.load(source, Loader=UniqueKeysLoader)
    if not isinstance(rows, dict):
        raise TypeError("External theorem data must be a mapping")
    result = []
    for number, fields in rows.items():
        if type(number) is not int or not 1 <= number <= 100:
            raise ValueError(f"Invalid external theorem number: {number}")
        if not isinstance(fields, dict):
            raise TypeError(f"External theorem {number} must be a mapping")
        # This also rejects Mathlib declaration/statement fields and unknown keys.
        theorem = ExternalHundredTheorem(number, **fields)
        if not isinstance(theorem.title, str) or not theorem.title.strip():
            raise ValueError(f"External theorem {number} needs a title")
        if not isinstance(theorem.links, dict) or not theorem.links:
            raise ValueError(f"External theorem {number} needs proof links")
        for label, url in theorem.links.items():
            if not isinstance(label, str) or not isinstance(url, str):
                raise TypeError(f"Invalid proof link for external theorem {number}")
            parsed = urlsplit(url)
            if parsed.scheme not in ("https", "http") or not parsed.netloc:
                raise ValueError(f"Invalid proof URL for external theorem {number}")
        for key in ("authors", "note"):
            value = getattr(theorem, key)
            if value is not None and not isinstance(value, str):
                raise ValueError(f"External theorem {number} has invalid {key}")
        result.append(theorem)
    return sorted(result, key=lambda theorem: theorem.id)


def hundred_context(theorems, external):
    """Keep result lists separate, but count their union for overall Lean coverage."""
    theorems = list(theorems)
    if len(theorems) != 100 or {theorem.id for theorem in theorems} != set(
        range(1, 101)
    ):
        raise ValueError(
            "The Mathlib catalogue must contain the numbered titles 1 through 100"
        )
    internal = [theorem for theorem in theorems if theorem.proof_formalized]
    internal_ids = {theorem.id for theorem in internal}
    known_ids = internal_ids | {theorem.id for theorem in external}
    missing = [theorem for theorem in theorems if theorem.id not in known_ids]
    return {
        "mathlib_hundred_theorems": internal,
        "mathlib_hundred_ids": internal_ids,
        "external_hundred_theorems": external,
        "missing_hundred_theorems": missing,
        "mathlib_hundred_count": len(internal_ids),
        "lean_hundred_count": len(known_ids),
        "statement_only_hundred_count": sum(
            theorem.statement_formalized for theorem in missing
        ),
    }
