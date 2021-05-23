# Lean Glossary

### abbreviation

### attribute

### beta reduction

A specific simplification operation in [dependent type
theory](#dependent-type-theory) (and Lean's implementation of it) which
may be performed as part of deciding whether two [terms](#term) are
[definitionally equal](#defeq).

More precisely, it is the process of simplifying an expression such as
`(λ x, x) a` by replacing appearances of the variable `x` with `a`.

#### See also

* [Section 2.3 of Theorem Proving in Lean](https://leanprover.github.io/theorem_proving_in_lean/dependent_type_theory.html#function-abstraction-and-evaluation)

### big operator

### binder

### bundled / unbundled

### carrier

### class

A class is a [structure](#structure), and therefore transitively an [inductive type](#inductive-type).

### coercion / ↑

### core Lean

### declaration

### defeq

### delaborator

### dependent type

### dependent type theory

### diamond

### elaborator

### eliminator

### equation compiler

### `equiv`

As distinct from mathematical equality,
[`equiv`](mathlib_docs/data/equiv/basic.html) allows for defining an
equivalence or congruence of types.

### eta reduction

### `ext` lemma

### heavy `refl`

https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refl.20taking.2020.20seconds

### ``Ioc``, ``Ico``, ``Ioo``, ``Icc``, ``Ici``, ``Ioi``

### inductive type

### instance

### `leanpkg`

### `leanproject`

A higher-level supporting tool for working with projects, particularly
mathlib, in Lean 3. It lives within the [community mathlib-tools
repository](https://github.com/leanprover-community/mathlib-tools/).

### lift

### lint

### locale

### motive

### metavariable

### mwe

*Minimum working example*, a way of making it easier to get help with a
snippet of Lean code by reducing it to its essential parts, whilst being
still runnable by others.

Further information can be found on [the mwe page](mwe.html).

### old structure

### pi type

### proof term

### recursor

### sigma type

### `simp` lemma

### `simp`-normal form

A convention within `mathlib` for expressing propositions with multiple
equivalent forms in a single conventional one.

Examples and further detail can found on [the `simp`
page](simp.html#simp-normal-form).

### structure

A structure is an [inductive type](#inductive-type).

### tactic mode

In Lean 3 it is often entered via a `begin...end` block.

#### See also

* [Section 5 of Theorem Proving in Lean](https://leanprover.github.io/theorem_proving_in_lean/tactics.html)

* [The mathlib tactics documentation](https://leanprover-community.github.io/mathlib_docs/tactics.html)

### term

### term mode

### terminal (or non-terminal) `simp`

### type annotation

### universe

### whnf
