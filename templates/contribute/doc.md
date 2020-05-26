# Documentation style

All pull requests must meet the following documentation standards. See
[the `doc-gen` repo](https://github.com/leanprover-community/doc-gen) for information about the
[automatically generated doc pages](https://leanprover-community.github.io/mathlib_docs/).

You can preview the markdown processing of a GitHub page or pull request
using the [Lean doc preview page](https://observablehq.com/@bryangingechen/github-lean-doc-preview).

## Header comment

Each mathlib file should start with:
* a header comment with copyright information;
* the list of imports;
* a module docstring containing general documentation, written using Markdown.

(See the example below.)

Headers use atx-style headers (with hash signs, no underlying dash).
The open and close delimiters `/-!` and `-/` should appear on their own lines.

The mandatory title of the file is a first level header. It is followed by a summary of the content
of the file.

The other sections, with second level headers are (in this order):
* *Main definitions* (optional, can be covered in the summary)
* *Main statements* (optional, can be covered in the summary)
* *Notations* (omitted only if no notation is introduced in this file)
* *Implementation notes* (description of important design decisions or interface features,
  including use of type classes and `simp` canonical form for new definitions)
* *References* (references to textbooks or papers, or Wikipedia pages)
* *Tags* (a list of keywords that could be useful when doing text search in mathlib to find where
  something is covered)

References should refer to bibtex entries in [the mathlib citations file](https://github.com/leanprover-community/mathlib/blob/master/docs/references.bib).

The following code block is an example of a file header.

```lean
/-
Copyright (c) 2018 Robert Y. Lewis. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Robert Y. Lewis
-/

import data.rat algebra.gcd_domain algebra.field_power
import ring_theory.multiplicity tactic.ring
import data.real.cau_seq
import tactic.norm_cast

/-!
# p-adic norm

This file defines the p-adic valuation and the p-adic norm on ℚ.

The p-adic valuation on ℚ is the difference of the multiplicities of `p` in the numerator and
denominator of `q`. This function obeys the standard properties of a valuation, with the appropriate
assumptions on p.

The valuation induces a norm on ℚ. This norm is a nonarchimedean absolute value.
It takes values in {0} ∪ {1/p^k | k ∈ ℤ}.

## Notations

This file uses the local notation `/.` for `rat.mk`.

## Implementation notes

Much, but not all, of this file assumes that `p` is prime. This assumption is inferred automatically
by taking (prime p) as a type class argument.

## References

* [F. Q. Gouêva, *p-adic numbers*][gouvea1997]
* https://en.wikipedia.org/wiki/P-adic_number

## Tags

p-adic, p adic, padic, norm, valuation
-/
```

## Doc strings

Every definition and major theorem is required to have a doc string.
(Doc strings on lemmas are also encouraged, particularly if the lemma has any mathematical content
or might be useful in another file.)
These are introduced using `/--` and closed by `-/` above the definition.
They can contain some markdown, e.g. backtick quotes. LaTeX can be included between single dollar
signs `$ ... $` to be rendered inline or double dollar signs `$$ ... $$` to be rendered in "display
mode" by MathJax in [the online mathlib docs](https://leanprover-community.github.io/mathlib_docs/).

Doc strings should convey the mathematical meaning of the definition. They are allowed to lie
slightly about the actual implementation. The following is a doc string example:

```lean
/--
If `q ≠ 0`, the p-adic norm of a rational `q` is `p ^ (-(padic_val_rat p q))`.
If `q = 0`, the p-adic norm of `q` is 0.
-/
def padic_norm (p : ℕ) (q : ℚ) : ℚ :=
if q = 0 then 0 else (p : ℚ) ^ (-(padic_val_rat p q))
```

An example that is slightly lying but still describes the mathematical content would be:

```lean
/--
For `p ≠ 1`, the p-adic valuation of an integer `z ≠ 0` is the largest natural number `n` such that
p^n divides z.
`padic_val_rat` defines the valuation of a rational `q` to be the valuation of `q.num` minus the
valuation of `q.denom`.
If `q = 0` or `p = 1`, then `padic_val_rat p q` defaults to 0.
-/
def padic_val_rat (p : ℕ) (q : ℚ) : ℤ :=
if h : q ≠ 0 ∧ p ≠ 1
then (multiplicity (p : ℤ) q.num).get
    (multiplicity.finite_int_iff.2 ⟨h.2, rat.num_ne_zero_of_ne_zero h.1⟩) -
  (multiplicity (p : ℤ) q.denom).get
    (multiplicity.finite_int_iff.2 ⟨h.2, by exact_mod_cast rat.denom_ne_zero _⟩)
else 0
```

The `#doc_blame` command can be run at the bottom of a file to list all definitions that do not have
doc strings. `#doc_blame!` will also list theorems and lemmas.

## Tactic doc entries

Interactive tactics, user commands, hole commands and user attributes should have doc strings
explaining how they can be used. The `add_tactic_doc` command should be invoked afterwards to add a
doc entry to the appropriate page in the online docs.

Example:
```lean
/--
describe what the command does here
-/
add_tactic_doc
{ name := "display name of the tactic",
  category := cat,
  decl_names := [`dcl_1, `dcl_2],
  tags := ["tag_1", "tag_2"]
}
```

The argument to `add_tactic_doc` is a structure of type `tactic_doc_entry`.
* `name` refers to the display name of the tactic; it is used as the header of the doc entry.
* `cat` refers to the category of doc entry.
  Options: `doc_category.tactic`, `doc_category.cmd`, `doc_category.hole_cmd`, `doc_category.attr`
* `decl_names` is a list of the declarations associated with this doc. For instance,
  the entry for `linarith` would set ``decl_names := [`tactic.interactive.linarith]``.
  Some entries may cover multiple declarations.
  It is only necessary to list the interactive versions of tactics.
* `tags` is an optional list of strings used to categorize entries.
* The doc string is the body of the entry. It can be formatted with markdown.
  What you are reading now is taken from the description of `add_tactic_doc`.

If only one related declaration is listed in `decl_names` and if this
invocation of `add_tactic_doc` does not have a doc string, the doc string of
that declaration will become the body of the tactic doc entry. If there are
multiple declarations, you can select the one to be used by passing a name to
the `inherit_description_from` field.

If you prefer a tactic to have a doc string that is different then the doc entry, then between
the `/--` `-/` markers, write the desired doc string first, then `---` surrounded by new lines,
and then the doc entry.

Note that providing a badly formed `tactic_doc_entry` to the command can result in strange error
messages.

## Sectioning comments

It is common to structure a file in sections, where each section contains related declarations.
By describing the sections with module documentation `/-! ... -/` at the beginning,
these sections can be seen in the documentation.

While these sectioning comments will often correspond to `section` or `namespace` commands,
this is not required. You can use sectioning comments inside of a section or namespace, and you can
have multiple sections or namespaces following one sectioning comment.

Sectioning comments are for display and readability only. They have no semantic meaning.

Third-level headers `###` should be used for titles inside sectioning comments.

If the comment is more than one line long, the delimiters `/-!` and `-/` should appear on their own
lines.

See [meta/expr.lean](https://github.com/leanprover-community/mathlib/blob/master/src/meta/expr.lean) for an example in practice.

```lean
namespace binder_info

/-!
### Declarations about `binder_info`

This section develops an extended API for the type `binder_info`.
-/

instance : inhabited binder_info := ⟨ binder_info.default ⟩

/-- The brackets corresponding to a given binder_info. -/
def brackets : binder_info → string × string
| binder_info.implicit        := ("{", "}")
| binder_info.strict_implicit := ("{{", "}}")
| binder_info.inst_implicit   := ("[", "]")
| _                           := ("(", ")")

end binder_info

namespace name

/-! ### Declarations about `name` -/

/-- Find the largest prefix `n` of a `name` such that `f n ≠ none`, then replace this prefix
with the value of `f n`. -/
def map_prefix (f : name → option name) : name → name
| anonymous := anonymous
| (mk_string s n') := (f (mk_string s n')).get_or_else (mk_string s $ map_prefix n')
| (mk_numeral d n') := (f (mk_numeral d n')).get_or_else (mk_numeral d $ map_prefix n')

```

## Theories documentation

In addition to documentation living in Lean files, we have [theories documentation](../theories.html)
where we give overviews spanning several Lean files, and
more mathematical explanations in cases where formalization requires slightly exotic points of view,
see for instance the [topology documentation](../theories/topology.html).

## Examples

The following files are maintained as examples of good documentation style:

* [data/padics/padic_norm](https://github.com/leanprover-community/mathlib/blob/master/src/data/padics/padic_norm.lean)
* [topology/basic](https://github.com/leanprover-community/mathlib/blob/master/src/topology/basic.lean)
* [analysis/calculus/times_cont_diff](https://github.com/leanprover-community/mathlib/blob/master/src/analysis/calculus/times_cont_diff.lean)
