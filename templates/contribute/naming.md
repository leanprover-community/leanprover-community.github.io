# Mathlib naming conventions

Author: [Jeremy Avigad](http://www.andrew.cmu.edu/user/avigad)

This guide is written for Lean 4.

## General conventions

Unlike Lean 3, in which the convention was that all declarations used `snake_case`,
in mathlib under Lean 4 we use a combination of `snake_case`, `lowerCamelCase` and
`UpperCamelCase` according to the following naming scheme.

1. Terms of `Prop`s (e.g. proofs, theorem names) use `snake_case`.
2. `Prop`s and `Type`s (or `Sort`) (inductive types, structures, classes) are in `UpperCamelCase`.
3. Functions are named the same way as their return values (e.g. a function of type `A → B → C` is named as though it is a term of type `C`).
4. All other terms of `Type`s (basically anything else) are in `lowerCamelCase`.
5. When something named with `UpperCamelCase` is part of something named with `snake_case`, it is referenced in `lowerCamelCase`.
6. Acronyms like `LE` are written upper-/lowercase as a group, depending on what the first character would be.
7. Rules 1-6 apply to fields of a structure or constructors of an inductive type in the same way.

There are some rare exceptions to preserve local naming symmetry: e.g., we use `Ne` rather than `NE` to follow the example of `Eq`; `outParam` has a `Sort` output but is not `UpperCamelCase`. Some other exceptions include intervals (`Set.Icc`, `Set.Iic`, etc.), where the `I`
is capitalized despite the fact that it should be `lowerCamelCase` according to the convention. Any such exceptions should be discussed on Zulip.

### Examples

```lean
-- follows rule 2
structure OneHom (M : Type _) (N : Type _) [One M] [One N] where
  toFun : M → N -- follows rule 4 via rule 3 and rule 7
  map_one' : toFun 1 = 1 -- follows rule 1 via rule 7

-- follows rule 2 via rule 3
class CoeIsOneHom [One M] [One N] : Prop where
  coe_one : (↑(1 : M) : N) = 1 -- follows rule 1 via rule 6

-- follows rule 1 via rule 3
theorem map_one [OneHomClass F M N] (f : F) : f 1 = 1 := sorry

-- follows rules 1 and 5
theorem MonoidHom.toOneHom_injective [MulOneClass M] [MulOneClass N] :
  Function.Injective (MonoidHom.toOneHom : (M →* N) → OneHom M N) := sorry
-- manual align is needed due to `lowerCamelCase` with several words inside `snake_case`
#align monoid_hom.to_one_hom_injective MonoidHom.toOneHom_injective

-- follows rule 2
class HPow (α : Type u) (β : Type v) (γ : Type w) where
  hPow : α → β → γ -- follows rule 3 via rule 6; note that rule 5 does not apply

-- follows rules 2 and 6
class LT (α : Type u) where
  lt : α → α → Prop -- follows rule 4 and 6

-- follows rules 1 and 6
theorem gt_iff_lt [LT α] {a b : α} : a > b ↔ b < a := sorry

-- follows rule 2; `Ne` is an exception to rule 6
class NeZero : Prop := sorry

-- follows rules 1 and 5
theorem neZero_iff {R : Type _} [Zero R] {n : R} : NeZero n ↔ n ≠ 0 := sorry
-- manual align is needed due to `lowerCamelCase` with several words inside `snake_case`
#align ne_zero_iff neZero_iff
```

### Names of symbols

When translating the statements of theorems into words, the following dictionary is often used.

#### Logic

| symbol | shortcut | name                      | notes                                                               |
|--------|----------|---------------------------|---------------------------------------------------------------------|
| `∨`    | `\or`    | `or`                      |                                                                     |
| `∧`    | `\and`   | `and`                     |                                                                     |
| `→`    | `\r`     | `of` / `imp`              | the conclusion is stated first and the hypotheses are often omitted |
| `↔`    | `\iff`   | `iff`                     | sometimes omitted along with the right hand side of the iff         |
| `¬`    | `\n`     | `not`                     |                                                                     |
| `∃`    | `\ex`    | `exists` / `bex`          | `bex` stands for "bounded exists"                                   |
| `∀`    | `\fo`    | `all` / `forall` / `ball` | `ball` stands for "bounded forall"                                  |
| `=`    |          | `eq`                      | often omitted                                                       |
| `≠`    | `\ne`    | `ne`                      |                                                                     |
| `∘`    | `\o`     | `comp`                    |                                                                     |

#### Set

| symbol                      | shortcut    | name                 | notes                                         |
|-----------------------------|-------------|----------------------|-----------------------------------------------|
| `∈`                         | `\in`       | `mem`                |                                               |
| `∪`                         | `\cup`      | `union`              |                                               |
| `∩`                         | `\cap`      | `inter`              |                                               |
| `⋃`                         | `\bigcup`   | `iUnion` / `biUnion` | `i` for "indexed", `bi` for "bounded indexed" |
| `⋂`                         | `\bigcap`   | `iInter` / `biInter` | `i` for "indexed", `bi` for "bounded indexed" |
| `⋃₀`                        | `\bigcup\0` | `sUnion`             | `s` for "set"                                 |
| `⋂₀`                        | `\bigcap\0` | `sInter`             | `s` for "set"                                 |
| `\`                         | `\\`        | `sdiff`              |                                               |
| `ᶜ`                         | `\^c`       | `compl`              |                                               |
| <code>{x &#124; p x}</code> |             | `setOf`              |                                               |
| `{x}`                       |             | `singleton`          |                                               |
| `{x, y}`                    |             | `pair`               |                                               |

#### Algebra

| symbol | shortcut              | name          | notes                                                       |
| ------ | --------------------- | ------------- | ----------------------------------------------------------- |
| `0`    |                       | `zero`        |                                                             |
| `+`    |                       | `add`         |                                                             |
| `-`    |                       | `neg` / `sub` | `neg` for the unary function, `sub` for the binary function |
| `1`    |                       | `one`         |                                                             |
| `*`    |                       | `mul`         |                                                             |
| `^`    |                       | `pow`         |                                                             |
| `/`    |                       | `div`         |                                                             |
| `•`    | `\bu`                 | `smul`        |                                                             |
| `⁻¹`   | `\-1`                 | `inv`         |                                                             |
| `⅟`    | `\frac1`              | `invOf`       |                                                             |
| `∣`    | <code>\\&#124;</code> | `dvd`         |                                                             |
| `∑`    | `\sum`                | `sum`         |                                                             |
| `∏`    | `\prod`               | `prod`        |                                                             |

#### Lattices

| symbol | shortcut | name                       | notes                            |
|--------|----------|----------------------------|----------------------------------|
| `<`    |          | `lt`                       |                                  |
| `≤`    | `\le`    | `le`                       |                                  |
| `⊔`    | `\sup`   | `sup`                      | a binary operator                |
| `⊓`    | `\inf`   | `inf`                      | a binary operator                |
| `⨆`    | `\supr`  | `iSup` / `biSup` / `ciSup` | `c` for "conditionally complete" |
| `⨅`    | `\infi`  | `iInf` / `biInf` / `ciInf` | `c` for "conditionally complete" |
| `⊥`    | `\bot`   | `bot`                      |                                  |
| `⊤`    | `\top`   | `top`                      |                                  |

### Dots

Dots are used for namespaces, and also for automatically generated names
like recursors, eliminators and structure projections. They can also be
introduced manually, for example, where projector notation is
useful. Thus they are used in all of the following situations.

Note: since `And` is a (binary function into) `Prop`, it is `UpperCamelCased`
according to the naming conventions, and so its namespace is `And.*`.
This may seem at odds with the dictionary `∧` --> `and` but because
upper camel case types get lower camel cased when they appear in names
of theorems, the dictionary is still valid in general. The same applies to
`Or`, `Iff`, `Not`, `Eq`, `HEq`, `Ne`, etc.

Intro, elim, and destruct rules for logical connectives, whether they
are automatically generated or not:

- `And.intro`
- `And.elim`
- `And.left`
- `And.right`
- `Or.inl`
- `Or.inr`
- `Or.intro_left`
- `Or.intro_right`
- `Iff.intro`
- `Iff.elim`
- `Iff.mp`
- `Iff.mpr`
- `Not.intro`
- `Not.elim`
- `Eq.refl`
- `Eq.rec`
- `Eq.subst`
- `HEq.refl`
- `HEq.rec`
- `HEq.subst`
- `Exists.intro`
- `Exists.elim`
- `True.intro`
- `False.elim`

Places where projection notation is useful, for example:

- `And.symm`
- `Or.symm`
- `Or.resolve_left`
- `Or.resolve_right`
- `Eq.symm`
- `Eq.trans`
- `HEq.symm`
- `HEq.trans`
- `Iff.symm`
- `Iff.refl`

It is useful to use dot notation even for types which are not
inductive types. For instance, we use:

- `LE.trans`
- `LT.trans_le`
- `LE.trans_lt`

### Axiomatic descriptions

Some theorems are described using axiomatic names, rather than
describing their conclusions.

- `def`  (for unfolding a definition)
- `refl`
- `irrefl`
- `symm`
- `trans`
- `antisymm`
- `asymm`
- `congr`
- `comm`
- `assoc`
- `left_comm`
- `right_comm`
- `mul_left_cancel`
- `mul_right_cancel`
- `inj`  (injective)

### Variable conventions

- `u`, `v`, `w`, ... for universes
- `α`, `β`, `γ`, ... for generic types
- `a`, `b`, `c`, ... for propositions
- `x`, `y`, `z`, ... for elements of a generic type
- `h`, `h₁`, ...     for assumptions
- `p`, `q`, `r`, ... for predicates and relations
- `s`, `t`, ...      for lists
- `s`, `t`, ...      for sets
- `m`, `n`, `k`, ... for natural numbers
- `i`, `j`, `k`, ... for integers

Types with a mathematical content are expressed with the usual
mathematical notation, often with an upper case letter
(`G` for a group, `R` for a ring, `K` or `𝕜` for a field, `E` for a vector space, ...).
This convention is not followed in older files, where greek letters are used
for all types. Pull requests renaming type variables in these files are welcome.

## Identifiers and theorem names

We adopt the following naming guidelines to make it easier for users
to guess the name of a theorem or find it using tab completion. Common
"axiomatic" properties of an operation like conjunction or
disjunction are put in a namespace that begins with the name of the
operation:

```lean
import Mathlib.Logic.Basic

#check And.comm
#check Or.comm
#check And.assoc
#check Or.assoc
```

In particular, this includes `intro` and `elim` operations for logical
connectives, and properties of relations:

```lean
import Mathlib.Logic.Basic

#check And.intro
#check And.elim
#check Or.intro_left
#check Or.intro_right
#check Or.elim

#check Eq.refl
#check Eq.symm
#check Eq.trans
```

Note however we do not do this for axiomatic arithmetic operations

```lean
import Mathlib.Algebra.Group.Basic

#check mul_comm
#check mul_assoc
#check @mul_left_cancel  -- multiplication is left cancelative
```

For the most part, however, we rely on descriptive names. Often the
name of theorem simply describes the conclusion:

```lean
import Mathlib.Algebra.Ring.Basic
open nat
#check succ_ne_zero
#check mul_zero
#check mul_one
#check @sub_add_eq_add_sub
#check @le_iff_lt_or_eq
```

If only a prefix of the description is enough to convey the meaning,
the name may be made even shorter:

```lean
import Mathlib.Algebra.Ring.Basic

#check @neg_neg
#check nat.pred_succ
```

When an operation is written as infix, the theorem names follow
suit. For example, we write `neg_mul_neg` rather than `mul_neg_neg` to
describe the patter `-a * -b`.

Sometimes, to disambiguate the name of theorem or better convey the
intended reference, it is necessary to describe some of the
hypotheses. The word "of" is used to separate these hypotheses:

```lean
import Mathlib.Algebra.Order.Ring.Lemmas

open Nat

#check lt_of_succ_le
#check lt_of_not_ge
#check lt_of_le_of_ne
#check add_lt_add_of_lt_of_le
```

The hypotheses are listed in the order they appear, _not_ reverse
order. For example, the theorem `A → B → C` would be named
`C_of_A_of_B`.

Sometimes abbreviations or alternative descriptions are easier to work
with. For example, we use `pos`, `neg`, `nonpos`, `nonneg` rather than
`zero_lt`, `lt_zero`, `le_zero`, and `zero_le`.

```lean
import Mathlib.Algebra.Order.Ring.Lemmas

open Nat

#check mul_pos
#check mul_nonpos_of_nonneg_of_nonpos
#check add_lt_of_lt_of_nonpos
#check add_lt_of_nonpos_of_lt
```

These conventions are not perfect. They cannot distinguish compound
expressions up to associativity, or repeated occurrences in a
pattern. For that, we make do as best we can. For example, `a + b - b = a`
could be named either `add_sub_self` or `add_sub_cancel`.

Sometimes the word "left" or "right" is helpful to describe variants
of a theorem.

```lean
import Mathlib.Algebra.Order.Ring.Lemmas

open Nat

#check add_le_add_left
#check add_le_add_right
#check le_of_mul_le_mul_left
#check le_of_mul_le_mul_right
```

## Naming of structural lemmas

We are trying to standardize certain naming patterns for structural lemmas.
At present these are not uniform across mathlib.

### Extensionality

A lemma of the form `(∀ x, f x = g x) → f = g` should be named `.ext`,
and labelled with the `@[ext]` attribute.
Often this type of lemma can be generated automatically by putting the
`@[ext]` attribute on a structure.
(However an automatically generated lemma will always be written in terms
of the structure projections, and often there is a better statement,
e.g. using coercions, that should be written by hand then marked with `@[ext]`.)

A lemma of the form `f = g ↔ ∀ x, f x = g x` should be named `.ext_iff`.

### Injectivity

Where possible, injectivity lemmas should be written in terms of an
`Function.Injective f` conclusion which use the full word `injective`, typically as `f_injective`.
The form `injective_f` still appears often in mathlib.

In addition to these, a variant should usually be provided as a bidirectional implication,
e.g. as `f x = f y ↔ x = y`, which can be obtained from `Function.Injective.eq_iff`.
Such lemmas should be named `f_inj`
(although if they are in an appropriate namespace `.inj` is good too).
Bidirectional injectivity lemmas are often good candidates for `@[simp]`.
There are still many unidirectional implications named `inj` in mathlib,
and it is reasonable to update and replace these as you come across them.

Note however that constructors for inductive types have
automatically generated unidirectional implications, named `.inj`,
and there is no intention to change this.
When such an automatically generated lemma already exists,
and a bidirectional lemma is needed, it may be named `.inj_iff`.

------
Copyright (c) 2016 Jeremy Avigad. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Jeremy Avigad
