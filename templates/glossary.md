# Lean Glossary

This document collects short explanations of terminology one may encounter within the Lean community.

Whilst many of the entries below have precise technical definitions, preference is given below to explanations of their conversational use, with additional references linked for further information.

A small number of interlinks below represent entries which have not yet been added, and will therefore not lead to entry definitions until they are completed.
To request that an additional entry be added to this glossary, feel free to [file an issue](https://github.com/leanprover-community/leanprover-community.github.io/issues/new?title=Add%20a%20glossary%20entry%20for%20).

The entries on this page can be linked to via anchor links (e.g. `https://leanprover-community.github.io/glossary.html#widget`).
For some entries, there are additional easier-to-type anchors which can be found just before the entry heading -- e.g. [`#heavy-rfl`](#heavy-rfl) will lead to the "heavy `rfl` / heavy `refl`" entry.
Authors of new glossary entries should consider adding these additional anchors if the entry title is long, contains backticks, or is otherwise hard to type.

### attribute

One or more tags or markings which may be applied to a Lean [declaration](#declaration), and which may affect either its behavior or the behavior of other Lean objects which interact with it. Attributes may be defined either within [core Lean](#core-lean), within [mathlib](#mathlib), or within any Lean code.

Applying an attribute is done either by prefixing a declaration command with `@[name-of-attribute]`, or afterwards by using the `attribute` command, as in `attribute [name-of-attribute] name-of-declaration`.

The `@[simp]` attribute, for example, tags a declaration (typically a `lemma`, `theorem` or `def`) as being a [simp lemma](#simp-lemma).

#### See also

* [The mathlib attributes documentation](https://leanprover-community.github.io/mathlib_docs/attributes.html), for a list of those defined and used throughout [mathlib](#mathlib)

* [Section 5.4 of *The Lean Reference Manual*](https://leanprover.github.io/reference/other_commands.html#attributes), for a list of those defined within [core lean](#core-lean)

### beta reduction

A specific simplification operation in [dependent type theory](#dependent-type-theory) (and Lean's implementation of it) which may be performed as part of deciding whether two [terms](#term) are [definitionally equal](#defeq).

More precisely, it is the process of simplifying an expression such as `(λ x, t) a` to `t[a/x]`, where appearances of the variable `x` in `t` have been replaced with `a`.

#### See also

* [Section 2.3 of Theorem Proving in Lean](https://leanprover.github.io/theorem_proving_in_lean/dependent_type_theory.html#function-abstraction-and-evaluation)

### big operators

A [locale](#locale) within [mathlib](#mathlib)'s [algebra library](https://leanprover-community.github.io/mathlib_docs/algebra/big_operators/basic.html), enabled via `open_locale big_operators`.

It defines notation for finite sums and products using the `∑` and `∏` characters.

### binder

Expressions such as `(a : α)`, `[a : α]` or `{a : α}` for any identifier(s) `a` and type `α` which, as part of various Lean syntactical elements -- [declarations](#declaration), `fun`, quantifiers and others -- represent identifiers which will be bound within the body of the syntactic element or declaration.

Each type of binder has different implications for whether it will be bound implicitly (without being passed by a caller), explicitly, or via [typeclass inference](#typeclass-inference).

In some places, notably within a `def`, defining "simple" binders without surrounding brackets are allowed, such as a binder `a` (with no explicit type) for some identifier `a`.

### bundled vs unbundled

Given a mathematical object `O` with property `P`, bundling `P` refers to the creation of a Lean [structure](#structure) containing a proof of `P` as one of its fields in addition to those needed to structurally define `O`.

In contrast, an unbundled structure instead contains only the definition of `O`, and separately the creation of an `is_P` proposition which can be applied to terms of `O`.

As a concrete example, a [group homomorphism](https://en.wikipedia.org/wiki/Group_homomorphism) can be viewed as a map `φ: G → H` between groups, along with a proof `h : φ(a * b) = φ(a) * φ(b)`. A bundled group homomorphism would contain both `φ` and `h` as fields, whereas an unbundled one would instead consist only of `φ`, with a separate `is_group_homomorphism` [declaration](#declaration) for the proof of `h`.

There are performance, stylistic or implementation-related reasons to prefer bundling or unbundling, as well as shades of grey which partially bundle some parts of a structure whilst leaving others unbundled.
[Type classes](#class) within [mathlib](#mathlib) are primarily semi-bundled, generally unbundling only the [carrier](#carrier) type itself.
Morphisms within mathlib are more often fully bundled, though traces of both approaches are present and discussed in the resource below.

#### See also

* Section 4.1.1 (Bundled Type Classes) and 4.1.2 (Bundled Morphisms), from [The Lean Mathematical Library](https://arxiv.org/pdf/1910.09336.pdf) (PDF), a paper by the mathlib community describing many of [mathlib](#mathlib)'s architecture and design choices.

### cache

Normally, a reference to a shared pre-built set of [`olean` files](#olean-file) built by [mathlib](#mathlib)'s [continuous integration](#continuous-integration) each time a commit is pushed to its repository.

Its purpose is to alleviate the need for each [mathlib](#mathlib) user to build (or rebuild) the same Lean files locally when doing so can take a significant amount of time (multiple hours on a modest computer).

The cache is built within the aforementioned continuous integration, and normally users of mathlib retrieve its built files using [`leanproject`](#leanproject).

### `calc` mode

A [mode](#mode) which consists of sequences of successive transformations of expressions involving a transitive relation such as `=`, `<` or others tagged with `trans` [attributes](#attribute).
It is entered via the `calc` keyword.

#### See also

* [The `calc` mode community documentation](https://leanprover-community.github.io/extras/calc.html)

### carrier

For a Lean [structure](#structure) which [bundles](#bundled-vs-unbundled) a type `T` along with some additional mathematical structure represented as additional fields (e.g. [`Group`](https://leanprover-community.github.io/mathlib_docs/algebra/category/Group/basic.html#Group)), it is the type `T` of underlying elements.

For a Lean [structure](#structure) which [bundles](#bundled-vs-unbundled) a set `S` along with some additional properties represented as additional fields (e.g. [`subgroup`](https://leanprover-community.github.io/mathlib_docs/group_theory/subgroup/basic.html#subgroup)), it is the underlying set `S`.

### class

More fully, a *typeclass* (or *type class*).

A Lean [structure](#structure) whose [instances](#instance) can be retrieved via [typeclass inference](#typeclass-inference).

Distinct from the use of *class* in object oriented languages -- the word usage in functional programming languages comes from the [typeclasses of Haskell](https://en.wikipedia.org/wiki/Type_class).

### code linter

A *code linter* is a [linter](#lint) which attempts to find unintentional mistakes in Lean code within [mathlib](#mathlib).
Concretely, mathlib includes [a collection of Lean programs](https://leanprover-community.github.io/mathlib_docs/tactic/lint/frontend.html) which check for a variety of potential issues which may be introduced in new mathlib code.
New linters are occasionally introduced to detect additional classes of mistakes.
Mathlib's [continuous integration](#continuous-integration) ensures that any new such code passes the defined linters.
Linting can be disabled for a particular piece of code by using the `nolint` [attribute](#attribute). Some linter failures that predate the CI code linters are indicated in an autogenerated [nolint file](https://github.com/leanprover-community/mathlib/blob/master/scripts/nolints.txt); the length of this file should tend to zero over time as these errors are fixed.

### `conv` mode

A submode of [tactic mode](#tactic-mode) which facilitates navigating within assumptions or [goals](#goal), in order to rewrite or simplify targeted portions of them.
It is entered from tactic mode via the `conv` keyword.

#### See also

* [The `conv` mode community documentation](https://leanprover-community.github.io/extras/conv.html)

### core Lean

As differentiated from [mathlib](#mathlib) or other community-authored Lean code, core Lean (or the "core library") refers to the portions of Lean which ship with the distribution of Lean itself.

Historically, even the mathlib project itself was a part of core Lean, and was split off into its own separately maintained project afterwards to facilitate development speed.

Some fundamental [declarations](#declarations) remain part of core Lean even after the split.
Occasionally additional lemmas and definitions are still removed or migrated from the core community Lean 3 repository and into mathlib, should they conflict with newly developed mathlib code.

The current portions of core Lean 3 can be found in the [Lean 3 community repository](https://github.com/leanprover-community/lean/tree/master/library), and for Lean 4 [similarly](https://github.com/leanprover/lean4/tree/master/src).

### declaration

A single Lean runtime object within a Lean environment.

Or, ambiguously, any of a number of Lean commands which may define or declare such objects.

Examples of such commands are the `def`, `theorem`, `constant` or `example` commands (and in Lean 3, the `lemma` command), amongst others.

Further detail can be found in the [Lean documentation](https://leanprover.github.io/lean4/doc/declarations.html#basic-declarations).

### diamond

The existence of multiple conflicting [terms](#term) of a [class](#class) found within the typeclass [instance](#instance) graph.
A diamond is likely to cause issues during [typeclass inference](#typeclass-inference), which attempts to construct a single term of the class and may therefore be unable to do so.
When unqualified, "diamond" refers most often to this undesirable case, where non-[defeq](#defeq) terms in the diamond may cause errors, lead to [goals](#goal) which are not provable via `refl`, or potentially ones not provably equal at all.
Within [mathlib](#mathlib), diamonds are abundant because of its many [hierarchies](#hierarchy).
Fixing or mitigating diamonds often involves refactoring the fields or instance priorities for the offending class.
Diamonds which cross library boundaries -- such as ones in which part of the typeclass graph lives within mathlib and part within a library depending on mathlib which adds new instances or classes -- may be particularly hard to fix or avoid without modification.

#### See Also

* [mathlib's Design note on `add_monoid` and `monoid`](https://leanprover-community.github.io/mathlib_docs/algebra/group/defs.html#design-note-on-codeadd_monoidcode-and-codemonoidcode), for a specific example of evading a diamond

* [Forgetful Inheritance](https://leanprover-community.github.io/mathlib_docs/notes.html#forgetful%20inheritance), also from the mathlib documentation, for a discussion on a general pattern for avoiding diamonds in the case of "richer" and poorer structures on a type

### `equiv`

As distinct from mathematical equality, [`equiv`](mathlib_docs/data/equiv/basic.html) allows for defining an equivalence or congruence of types.
One important thing to note is that an `equiv` [holds data instead of being merely a proof](#bundled-vs-unbundled).

### goal

Within the context of interactively proving theorems in Lean, each targeted statement whose proof is in-progress.

Or more broadly, type theoretically, an individual type for which a [term](#term) is to be exhibited.
For propositions, exhibiting a [term](#term) reduces equivalently to the aforementioned idea of proof.

### golfing

An attempt or effort to make a particular working piece of code as short as possible; within the context of Lean, often it is a proof's length which is golfed or optimized.
Golfed proofs often make use of [term mode](#term-mode), and in general prioritize terseness over readability.
This obfuscation often is used intentionally or advantageously to signal to readers that a proof is mechanical or trivial.

<a name="heavy-rfl"></a>

### heavy `rfl` / heavy `refl`

A use of `rfl` (or `refl`) which performs slowly when it is evaluated by Lean.
A heavy `rfl` occurs when `rfl` is asked to perform many steps of definitional reduction at once, resulting in a proof term which is small but which requires Lean to do a lot of computation to ensure that it type checks.

[This Zulip discussion](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/refl.20taking.2020.20seconds) has a particularly slow example.

### hierarchy

A collection of successively more constrained [typeclasses](#typeclass) within a related area of mathematics.
In [mathlib](#mathlib), we have the *algebraic hierarchy* (`semiring`, `ring`, `field`, ...), the *order hierarchy* (`preorder`, `partial_order`, `linear_order`, ...), the *topological hierarchy* (`t1_space`, `t2_space`, `normal_space`, ...), the *categorical hierarchy* (`preadditive`, `abelian`, `monoidal`, ...) but also the *scalar hierarchy* (`mul_action`, `distrib_mul_action`, `module`, ...), the *norm hierarchy*, and intersections of previous ones like the *order-algebraic hierarchy*, the *topologico-algebraic hierarchy*, and others.

<a name="intervals"></a>

### `Icc`, `Ico`, `Ioc`, `Ioo`, `Ici`, `Ioi`, `Iic`, `Iio`

Shorthand notation used within [mathlib](#mathlib) for referring to one of 8 kinds of mathematical intervals.
There are `8` types of intervals, depending on whether the interval is *c*losed, *o*pen or runs to *i*nfinity at each end.
Names have been made compact by calling each interval `I` + how it ends on the left + how it ends on the right.
`Iii`, which in the naming convention would refer to an interval infinite at both ends, is not in use.

#### See also

* [mathlib's `data.set.intervals.unordered_interval`](https://leanprover-community.github.io/mathlib_docs/data/set/intervals/unordered_interval.html), which builds unordered intervals (where the endpoints may be specified in either order) on top of these intervals.

### infoview

Within the context of interactively editing Lean files, a window or interface which displays incremental [goal](#goal) state, diagnostics, errors and Lean [widgets](#widget) output.

### instance

One of two closely related concepts:

* A [class](#class) argument taken by a `def`, `lemma` or other [declaration](#declaration) which is enclosed by square brackets (`[]`) such that it is resolved by the [typeclass inference](#typeclass-inference) system when the declaration is used.
* A [declaration](#declaration) created with the eponymous `instance` command, or equivalently one marked with the `instance` [attribute](#attributes), either of which register the declaration with the typeclass inference system for use in the above. As a concrete example, [mathlib](#mathlib) defines an instance of `linear_order` for `ℝ`, enabling reals to be compared with `<`.

### Lean Together

An [annual meeting](https://leanprover-community.github.io/lt2021/) for the Lean user community, its [mathlib](#mathlib) library users, as well as the broader theorem prover community.

Previous talks or presentations from the events have been [shared on the community YouTube channel](https://www.youtube.com/channel/UCWe5B7Ikr0AI9727doEUxPg).

### `leanproject`

A higher-level supporting tool for working with projects, particularly [mathlib](#mathlib), in Lean 3.
It lives within the [community `mathlib-tools` repository](https://github.com/leanprover-community/mathlib-tools/).

### lint

A *linter* is a small program that looks for hard-to-spot mistakes in code.
[mathlib](#mathlib) defines both [style linters](#style-linter) and [code linters](#code-linter).
Mathlib is linted on every [CI run](#continuous-integration) when pull requests are submitted.

### mathlib

A [large, community maintained collection of mathematics](https://github.com/leanprover-community/mathlib) for Lean 3.

In addition to its breadth of mathematical objects and proofs, mathlib serves as the de facto standard (programmatic) library for Lean 3, containing additional functionality useful for non-mathematics related projects.

### mathlib4

An [experimental attempt](https://github.com/leanprover-community/mathlib4/) to port portions of [mathlib](#mathlib) to Lean 4.
mathlib4 is a manual, exploratory attempt to suss out points of difficulty, identify areas for redesign, and prepare for a more targeted effort which will occur as part of moving mathlib to Lean 4.
Learnings from both the mathlib4 effort as well as from [mathport](#mathport) often lead to backported changes to mathlib, to bring Lean 3 code into more future-compatible states.

### mathport

An [in-development tool](https://github.com/leanprover/mathport/) for automated or semi-automated translation of Lean 3 code into Lean 4 code.
It consists of both fully automated generation of Lean 4 [olean files](#olean-file) from Lean 3 source files (*binport*), as well as best-effort source-to-source translation of Lean 3 to Lean 4 source code (*synport*).
Learnings from both the mathport effort as well as from [mathlib4](#mathlib4) often lead to backported changes to mathlib, to bring Lean 3 code into more future-compatible states.

### mode

In the context of writing Lean code, a set of related syntactical elements or keywords which make a particular style of formal reasoning or construction of [proof terms](#proof-term) efficient.
Lean, especially as restricted to [mathlib](#mathlib), has a small number of such modes -- [tactic mode](#tactic-mode), [term mode](#term-mode), [calc mode](#calc-mode) and [conv-mode](#conv-mode).
A particular mode may make progress towards specific kinds of [goals](#goal) easier.
A proof may often, however, mix various modes in the course of constructing a [proof term](#proof-term).

### module

A single file containing Lean source code.

Not to be mistaken with a `module` within mathematics, i.e. the generalization of a vector space.

## module docstring

[Module](#module)-level comment summarizing what's to be found in the file.
We require that every file has one, but [some old files](https://github.com/leanprover-community/mathlib/blob/master/scripts/style-exceptions.txt) still don't.

### MWE

*Minimal Working Example*, a way of making it easier to get help with a snippet of Lean code by reducing it to its essential parts, whilst being still runnable by others.

Further information can be found on [the MWE page](mwe.html).

### non-terminal `simp`

An invocation of the `simp` tactic which is not the last tactic invoked on a particular [subgoal](#goal), nor uses `simp only` to explicitly limit which [simp lemmas](#simp-lemma) it considers.
Non-terminal `simp`s are avoided because they are hard to maintain, given that their behavior or runtime will change as mathlib adds or modifies the set of `simp` lemmas over time.

#### See also

The ["non-terminal `simp`" section](https://leanprover-community.github.io/extras/simp.html#non-terminal-codesimpcodes) of the `simp` documentation

### olean file

Lean code has to be compiled.
The compiled version of file `x.lean` is file `x.olean` and all olean files together form the [cache](#cache).

### orange bar of hell

Interactive editing of Lean in VSCode (or other editors) is typically fairly responsive.

*Orange bars of hell*, however, refer to occasional instances where orange bars in the sidebar alongside a Lean file do not disappear or update.
Normally these bars indicate which parts of a file Lean is still evaluating, but if these bars persist, it indicates that progress isn't being made.
Fixing these bars can often be done by closing any inactive editor tabs, followed by opening the VSCode Command Palette (`ctrl-shift-p` or `cmd-shift-p`) and running `Lean: Restart`.
Another common reason this occurs is if Lean is having to (re)compile all imported [mathlib](#mathlib) files due to a mismatched set of [cached](#cache) [olean files](#olean-file).
In these cases, ensuring that the mathlib cache is properly downloaded via `leanpkg configure && leanproject get-mathlib-cache` should fix the issue.

## propeq

*Propositional equality*. Two [term](#term)s `a b : α` are propositionally equal if we can prove `a = b`.
This is weaker than [definitional](#defeq) and [syntactical](#syntactical-equality) equalities.

#### See also

[Equality, specifications and implementations](https://xenaproject.wordpress.com/2020/07/03/equality-specifications-and-implementations/), from the Xena Project

### `simp` lemma

A lemma which has been tagged with an [attribute](#attribute) which enables it for use with the `simp` tactic.

Good `simp` lemmas guide the `simp` tactic towards reducing complex expressions into simpler ones, often to the point where the `simp` tactic is able to close many goals itself.

Further details can be found in the [`simp` documentation of mathlib](https://leanprover-community.github.io/extras/simp.html#simp-lemmas).

### `simp`-normal form

A convention within [mathlib](#mathlib) for expressing propositions with multiple equivalent forms in a single conventional one.

Examples and further detail can found on [the `simp` page](simp.html#simp-normal-form).

### style linter

A *style linter* is a [linter](#lint) which attempt to ensure uniform appearance or style of code within [mathlib](#mathlib), without affecting its working behavior.
Concretely, mathlib includes [a short Python program](https://github.com/leanprover-community/mathlib/blob/master/scripts/lint-style.py) which checks for instance that lines are less than 100 characters long, that every file has a [module docstring](#module-docstring), et cetera.
Mathlib's [continuous integration](#continuous-integration) ensures that new code passes the defined linters.
Allowed style linting exceptions are stored in a [style exceptions file](https://github.com/leanprover-community/mathlib/blob/master/scripts/style-exceptions.txt) within the repository.

### tactic mode

A Lean [mode](#mode) characterized by its reliance on sequences of [tactics](#tactic) which often facilitate proofs quite similar to paper-based reasoning, albeit often with the use of sophisticated tactics which automate tedious portions of a proof.
There are various means to [enter tactic mode](https://leanprover.github.io/theorem_proving_in_lean/tactics.html#entering-tactic-mode).
It may be entered using the `by` keyword from [term mode](#term-mode), though in Lean 3 it is most often entered via a `begin...end` block whenever its body is made up of multiple commands.
Other modes can also be interspersed within it, often to collaboratively produce an understandable, efficient, short or readable overall proof.
Ultimately, the result of a tactic mode block is a [term](#term), assembled via the tactics within it.

#### See also

* [Section 5 of Theorem Proving in Lean](https://leanprover.github.io/theorem_proving_in_lean/tactics.html), which discusses tactics, as well as moving into and out of tactic mode

* [The `show_term` tactic](https://leanprover-community.github.io/mathlib_docs/tactic/show_term.html) which can reveal the assembled [term](#term)

* [The mathlib tactics documentation](https://leanprover-community.github.io/mathlib_docs/tactics.html), with a comprehensive list of tactics

### term mode

A Lean [mode](#mode) which assembles a single [term](#term) through the use of functional subexpressions.
In contrast to [tactic mode](#tactic-mode), term mode proofs are often short in length, though potentially harder to read for humans.
There are various means to enter term mode.
The body of a [declaration](#declaration) begins in term mode, or within [tactic mode](#tactic-mode) it is often entered using the `exact` [tactic](#tactic).
Efficient term mode proofs often contribute to [code golfing](#golfing).

Commands such as `have`, `suffices`, and `show` can be used to write structured term mode proofs that are more legible than bare proof terms.

### unicode abbreviation

In the context of editing Lean files, an abbreviation is a way of entering a symbol not generally found on standard keyboard layouts using a descriptive shortcut.

For instance, the not-equal symbol "≠" can be entered using the sequence `\neq`.

The full list of abbreviations (and their replacements) can be found [in the `vscode-lean` repository](https://github.com/leanprover/vscode-lean/blob/master/src/abbreviation/abbreviations.json).

### whnf

A Lean expression is in *weak head normal form*, often abbreviated to `whnf`, if it meets a number of normalization criteria mentioned in the resources linked below.
Informally, expressions in whnf have had their outermost parts evaluated, though inner subexpressions may not have been evaluated.

It also may refer to a command which reduces expressions to this form.

#### See also

* [Section 8.4 of Programming in Lean](https://leanprover.github.io/programming_in_lean/#08_Writing_Tactics.html), which is still in progress, but will cover `whnf`
* [What is weak head normal form? - Stack Overflow](https://stackoverflow.com/questions/6872898/what-is-weak-head-normal-form)
* [Weak head normal form - The Haskell wiki](https://wiki.haskell.org/Weak_head_normal_form)

### widget

An extensible framework for defining interactive, componentized graphical elements via Lean code, which render in [infoviews](#infoview) during interactive theorem proving.

A widget may also refer to an individual graphical element being rendered by the aforementioned framework.

Widgets provide a mechanism to show additional context or information which updates in the course of interactive theorem proving.

Support is present both in Lean 3 and Lean 4, albeit with different out-of-the-box functionality.

#### See also

* [Lean Together 2021: Widgets, interactive output in VSCode](https://www.youtube.com/watch?v=8NUBQEZYuis), a presentation by Edward Ayers from [Lean Together 2021](#lean-together) which shows off some of the capabilities widgets enable
* [The Lean 3 Widget Server Protocol](https://github.com/leanprover-community/lean/blob/master/doc/widget_server.md), a document intended for low-level protocol information more suitable for learning about widget implementation details
