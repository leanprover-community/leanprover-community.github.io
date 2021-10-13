# Lean Glossary

### abbreviation

In the context of editing Lean files, an abbreviation is a way of entering a symbol not generally found on standard keyboard layouts using a descriptive shortcut.

For instance, the not-equal symbol "≠" can be entered using the sequence `\neq`.

The full list of abbreviations (and their replacements) can be found [in the `vscode-lean` repository](https://github.com/leanprover/vscode-lean/blob/master/src/abbreviation/abbreviations.json).

### attribute

One or more tags or markings which may be applied to a Lean object, and which may affect either its behavior or the behavior of other Lean objects which interact with it. Attributes may be defined either within [core Lean](#core-lean), within [mathlib](#mathlib), or within any Lean code.

Applying an attribute to an object is done by prefixing its [declaration](#declaration) with `@[name-of-attribute]`, or by using the `attribute` command, as in `attribute [name-of-attribute] name-of-declaration`.

The `@[simp]` attribute, for example, tags an object (ostensibly a `lemma` or `theorem`) as being a [simp lemma](#simp-lemma).

For further details, including a list of commonly used attributes, see [this section of the Lean reference manual](https://leanprover.github.io/reference/other_commands.html#attributes).

### beta reduction

A specific simplification operation in [dependent type theory](#dependent-type-theory) (and Lean's implementation of it) which may be performed as part of deciding whether two [terms](#term) are [definitionally equal](#defeq).

More precisely, it is the process of simplifying an expression such as `(λ x, x) a` by replacing appearances of the variable `x` with `a`.

#### See also

* [Section 2.3 of Theorem Proving in Lean](https://leanprover.github.io/theorem_proving_in_lean/dependent_type_theory.html#function-abstraction-and-evaluation)

### big operators

A [locale](#locale) within [mathlib](#mathlib)'s [algebra library](https://leanprover-community.github.io/mathlib_docs/algebra/big_operators/basic.html), enabled via `open_locale big_operators`.

It defines notation for finite sums and products using the `∑` and `∏` characters.

### binder

Expressions such as `(a : α)`, `[a : α]` or `{a : α}` for any identifier(s) `a` and type `α` which, as part of various Lean syntactical elements -- [declarations](#declaration), `fun`, quantifiers and others -- represent identifiers which will be bound within the body of the syntactic element or declaration.

Each type of binder has different implications for whether it will be bound implicitly (without being passed by a caller), explicitly or via [typeclass inference](#typeclass-inference).

In some places, notably within a `def`, defining "simple" binders without surrounding brackets are allowed, such as a binder `a` (with no explicit type) for some identifier `a`.

### bundled vs unbundled

Given a mathematical object `O` with property `P`, bundling `P` refers to the creation of a Lean [structure](#structure) containing a proof of `P` as one of its fields in addition to those needed to structurally define `O`.

In contrast, an unbundled structure instead contains only the definition of `O`, and separately the creation of an `is_P` proposition which can be applied to terms of `O`.

As a concrete example, a [group homomorphism](https://en.wikipedia.org/wiki/Group_homomorphism) can be viewed as a map `φ: G → H` between groups, along with a proof `h : φ(a * b) = φ(a) * φ(b)`. A bundled group homomorphism would contain both `φ` and `h` as fields, whereas an unbundled one would instead consist only of `φ`, with a separate `is_group_homomorphism` [declaration](#declaration) for the proof of `h`.

There are performance, stylistic or implementation-related reasons to prefer bundling or unbundling.
Generally within [mathlib](#mathlib), bundled structures are preferred, but unbundled versions are often also present.

### cache

Normally, a reference to a shared pre-built set of [`olean` files](#olean-file) built by [mathlib](#mathlib)'s [continuous integration](#continuous-integration) each time a commit is pushed to its repository.

Its purpose is to alleviate the need for each [mathlib](#mathlib) user to build (or rebuild) the same Lean files locally, when doing so can take a significant number of time (multiple hours on a modest computer).

The cache is built within the aforementioned continuous integration, and normally users of mathlib retrieve its built files using [`leanproject`](#leanproject).

### carrier

For a [bundled](#bundled-vs-unbundled) mathematical subobject on a type `T`, it is the *set* of [terms of T](#term) considered within the subobject.

Lean (sub-)[structures](#structure) will often correspondingly name one of their fields as such (`carrier`).

### class

More fully, a *typeclass* (or *type class*).

A Lean [structure](#structure) whose [instances](#instance) can be retrieved via [typeclass inference](#typeclass-inference).

Distinct from the use of *class* in object oriented languages -- the word usage in functional programming languages comes from the [typeclasses of Haskell](https://en.wikipedia.org/wiki/Type_class).

### coercion / ↑

### code linter

A *code linter* is a [linter](#lint) concerned with how code works.
Concretely, this is [a collection of Lean programs](https://leanprover-community.github.io/mathlib_docs/tactic/lint/frontend.html) checking that... Errors are flagged in the [nolint file](https://github.com/leanprover-community/mathlib/blob/master/scripts/nolints.txt).

### concrete structure

### continuous integration

### core Lean

As differentiated from [mathlib](#mathlib) or other community-authored Lean code, core Lean (or the "core library") refers to the portions of Lean which ship with the distribution of Lean itself.

Historically, even the mathlib project itself was a part of "core Lean", and was split off into its own separately maintained project afterwards to facilitate development speed.

Some fundamental [declarations](#declarations) remain part of core Lean even after the split.
Occasionally additional lemmas and definitions are still removed or migrated from the core community Lean 3 repository and into mathlib, should they conflict with newly developed mathlib code.

The current portions of core Lean 3 can be found in the [Lean 3 community repository](https://github.com/leanprover-community/lean/tree/master/library), and for Lean 4 [similarly](https://github.com/leanprover/lean4/tree/master/src).

### declaration

A *declaration* is anything that starts with `def`, `lemma`, `theorem`.
This corresponds to creating an (or several) object in the background environment.

### defeq

### delaborator

### dependent type

### dependent type theory

### diamond

There are often many ways to turn a given structure into another one.
A *diamond* is a collection of such ways.
Diamonds are abundant because of [hierarchies](#hierarchy).
[Typeclass inference](#typeclass-inference) will unpredictably take one of the paths for a given diamond, so we want this path to not matter.
This amounts to making the [Type-valued](#Prop-vs-Type) fields of the different inferable structures [defeq](#defeq).
When this is the case, we have a *defeq diamond*.

### elaborator

### eliminator

### equation compiler

### `equiv`

As distinct from mathematical equality, [`equiv`](mathlib_docs/data/equiv/basic.html) allows for defining an equivalence or congruence of types.
One important thing to note is that an `equiv` [holds data instead of being merely a proof](#bundled-vs-unbundled).

### eta reduction

### `ext` lemma

### heavy `refl`

Some `refl` invocations take an obnoxiously long time.
There can be many reasons for this.
See [this Zulip discussion](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refl.20taking.2020.20seconds).

### hierarchy

A *hierarchy* is a collection of [typeclasses](#typeclass) which are more and more constraining.
In [mathlib](#mathlib), we have the *algebraic hierarchy* (`semiring`, `ring`, `field`, ...), the *order hierarchy* (`preorder`, `partial_order`, `linear_order`, ...), the *topological hierarchy* (`t1_space`, `t2_space`, `normal_space`, ...), the *categorical hierarchy* (`preadditive`, `abelian`, `monoidal`, ...) but also the *scalar hierarchy* (`mul_action`, `distrib_mul_action`, `module`, ...), the *norm hierarchy*, and intersection of previous ones like the *order-algebraic hierarchy*, the *topologico-algebraic hierarchy*, ...

### `Icc`, `Ico`, `Ioc`, `Ioo`, `Ici`, `Ioi`, `Iic`, `Iio`

There are `9` types of intervals, depending on whether the interval is **c**losed, **o**pen or runs to **i**nfinity at each end.
Names have been made compact by calling each interval `I` + how it ends on the left + how it ends on the right.

### import tree

### inductive type

### infoview

### instance

"instance" refers to two closely related concepts:
* An *instance* is a [class](#class) argument to a `def`/`lemma`.
They are put in square brackets `[]` for [typeclass inference](#typeclass-inference) to pick them up when processing the statement.
* An *instance* is an `instance` [declaration](#declaration). Instances For example, `ℝ` has a linear


### instance vs def

Some `def` in [mathlib](#mathlib) could be promoted to `instance`.
The reason they are not is usually because doing so would cause [non-defeq diamonds](#diamond).
One way to still use the problematic

### `leanpkg`

### `leanproject`

A higher-level supporting tool for working with projects, particularly [mathlib](#mathlib), in Lean 3.
It lives within the [community `mathlib-tools` repository](https://github.com/leanprover-community/mathlib-tools/).

### lift

### lint

A *linter* is a small program that looks for hard-to-spot mistakes in code.
For [mathlib](#mathlib), we use [style linters](#style-linter)* and [code linters](#code-linter).
Mathlib is linted at every [CI run](#continuous-integration) after being built.

### locale

A *locale* is akin to a mathematical environment. 

### mathlib

A [large, community maintained collection of mathematics](https://github.com/leanprover-community/mathlib) for Lean 3.

In addition to its breadth of mathematical objects and proofs, mathlib serves as the de facto standard (programmatic) library for Lean 3, containing additional functionality useful for non-mathematics related projects.

### module

A [mathlib](#mathlib) *module* is a file.
Not to be mistaken with `module` that represents a maths semimodule/module/vector space.

## module docstring

[Module](#module)-level comment summarizing what's to be found in the file.
We require that every file has one, but [some old files](https://github.com/leanprover-community/mathlib/blob/master/scripts/style-exceptions.txt) still don't.

### motive

### metavariable

### MWE

*Minimal Working Example*, a way of making it easier to get help with a snippet of Lean code by reducing it to its essential parts, whilst being still runnable by others.

Further information can be found on [the MWE page](mwe.html).

### non-terminal `simp`

A `simp` invocation is deemed *non-terminal* when it is not `simp only` nor is the last tactic invoked.
We avoid non-terminal `simp`s because they are hard to maintain.
See [Non-terminal `simp`s](https://leanprover-community.github.io/extras/simp.html#non-terminal-codesimpcodes)

### old structure

### olean file

Lean code has to be compiled.
The compiled version of file `x.lean` is file `x.olean` and all olean files together form the [cache](#cache).

### orange bar of hell

In VScode, the *orange bar of hell* refers to the orange bar that appears left to the current file when it persists.
The reason is that the Lean extension has to (re)compile all the imported files whose [cache](#cache) does not match.
Because of this, having branches that touch two files far apart (with respect to the [import tree](#import-tree)) related through imports is considered bad practice as **any** modification on the file upstream will force Lean to recompile all the files in the middle.

### pi type

### proof term

## propeq

*Proposition equality*. Two terms `a b : α` are *propositionally equal* if we can prove `a = b`.
This is weaker than [definitional](#defeq) and [syntactical](#syntactical-equality) equalities.

### `Prop` vs `Type`

### recursor

### sigma type

### `simp` lemma

### `simp`-normal form

A convention within [mathlib](#mathlib) for expressing propositions with multiple equivalent forms in a single conventional one.

Examples and further detail can found on [the `simp` page](simp.html#simp-normal-form).

### structure

A structure is an [inductive type](#inductive-type).

### style linter

A *style linter* is a [linter](#lint) concerned with how code looks.
Concretely, this is [a short Python program](https://github.com/leanprover-community/mathlib/blob/master/scripts/lint-style.py) checking that all lines are less than `100` characters long, that every file has a [module docstring](#module-docstring)... Errors are flagged in the [style exceptions file](https://github.com/leanprover-community/mathlib/blob/master/scripts/style-exceptions.txt).

### syntactical equality

### tactic mode

In Lean 3 it is often entered via a `begin...end` block.

#### See also

* [Section 5 of Theorem Proving in Lean](https://leanprover.github.io/theorem_proving_in_lean/tactics.html)

* [The mathlib tactics documentation](https://leanprover-community.github.io/mathlib_docs/tactics.html)

### term

### term mode

### type annotation

### typeclass inference

### unification

### universe

### whnf

A Lean expression is in *weak head normal form*, often abbreviated to `whnf`, if it meets a number of normalization criteria mentioned below.
Informally, expressions in whnf have had their outermost parts evaluated, though inner subexpressions may not have been evaluated.

Within [core Lean](#core-lean), it also may refer to a tactic helper which reduces expressions to this form.

#### See also

* [What is weak head normal form? - Stack Overflow](https://stackoverflow.com/questions/6872898/what-is-weak-head-normal-form)
* [Weak head normal form - The Haskell wiki](https://wiki.haskell.org/Weak_head_normal_form)

### well founded recursion

See [The equation compiler and `using_well_founded`](https://leanprover-community.github.io/extras/well_founded_recursion.html).
