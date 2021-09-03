# Simp

## Overview

In this document we will explain basic usage of Lean's simplifier
tactic [`simp`](https://leanprover-community.github.io/mathlib_docs/tactics.html#simp)
and the related tactic [`dsimp`](https://leanprover-community.github.io/mathlib_docs/tactics.html#dsimp).

We give some pointers for how to avoid "non-terminal `simp`s", and we
also give a short description of the configuration options for `simp`
and `dsimp`.

## Introduction

Lean has a "simplifier", called `simp`, that consults a database of
facts called *`simp` lemmas* to (hopefully) simplify hypotheses and
goals. The simplifier is what is known as a *conditional term
rewriting system*: all it does is repeatedly replace (or *rewrite*)
subterms of the form `A` by `B`, for all applicable facts of the form
`A = B` or `A ↔ B`.
The simplifier mindlessly rewrites until it can rewrite no more.  The
`simp` lemmas are all oriented, with left-hand sides always being
replaced by right-hand sides, and never vice versa.

Ideally, the database of facts would result in expressions being simplified
into a normal form.
In practice, this is often unachievable (normal forms may not exist, or there
may not exist a collection of rewrite rules that produce them),
but nevertheless we aim to approximate this ideal where possible.
Even better, we would like the database of facts to be *confluent*,
meaning the order in which the simplifier considers rewrites does not matter.
Again, we aim to be close to confluent where possible.

While this system is able to prove many simple statements completely
automatically, proving all simple statements is not part of its job
description, as disappointing as that might be.

Here is an example (using `mathlib`).

```lean
import algebra.group.defs

variables (G : Type) [group G] (a b c : G)

example : a * a⁻¹ * 1 * b = b * c * c⁻¹ :=
begin
  simp
end
```

How would a human solve that goal? They would notice that `a * a⁻¹ = 1`,
that `1 * 1 = 1`, and so on, until they had simplified the example
to `b = b`, which is obviously true.

This is also what the simplifier is doing.  Indeed, if you add
`set_option trace.simplify.rewrite true` above the example, then a
squiggly blue underline will appear under `simp` (in VS Code) and
clicking on this will show you the sequence of rewrites that `simp`
performed:
```
[mul_right_inv]: a * a⁻¹ ==> 1
[mul_one]: 1 * 1 ==> 1
[one_mul]: 1 * b ==> b
[mul_inv_cancel_right]: b * c * c⁻¹ ==> b
[eq_self_iff_true]: b = b ==> true
```
The `simp?` tactic is a useful way to extract the list of lemmas that `simp` applied.
It suggests
```lean
simp only [mul_one, one_mul, mul_right_inv, eq_self_iff_true, mul_inv_cancel_right]
```
which is an invocation of `simp` that makes use of this particular set of five lemmas.
A related tactic, `squeeze_simp`, will (after thinking *much* harder than `simp?` does)
come up with some set of simp lemmas that are sufficient.
In this case three suffice:
```lean
simp only [one_mul, mul_right_inv, mul_inv_cancel_right]
```

To see both those rewrites that work and those that fail during the simplification process,
you can use the more verbose option `set_option trace.simplify true`.

## Simp lemmas

So how did Lean's simplifier know that `a * a⁻¹ = 1`? It is because
there is a lemma in `algebra.group.defs` that is tagged with the
`simp` attribute:

```lean
@[simp] lemma mul_right_inv (a : G) : a * a⁻¹ = 1 := ...
```

We call lemmas tagged with the `simp` attribute "`simp` lemmas". Here
are some more examples of `simp` lemmas in mathlib:

```lean
@[simp] theorem nat.dvd_one {n : ℕ} : n ∣ 1 ↔ n = 1 := ...
@[simp] theorem mul_eq_zero {a b : ℕ} : a * b = 0 ↔ a = 0 ∨ b = 0 := ...
@[simp] theorem list.mem_singleton {a b : α} : a ∈ [b] ↔ a = b := ...
@[simp] theorem set.set_of_false : {a : α | false} = ∅ := ...
```

When the simplifier is attempting to simplify a term `T`, it looks
through the `simp` lemmas known to the system at that time, and if it
runs into an applicable lemma of the form `A = B` or `A ↔ B` for which
`A` appears as a subexpression in `T`, it rewrites the instance of `A` in `T` with `B`
and then starts again from the beginning. Note that `simp` starts on
innermost terms, working outward: it first simplifies the arguments of
a function before simplifying the function. Also, `simp` contains some
amount of cleverness to be able to avoid considering *all* `simp`
lemmas every time (there are over ten thousand of them currently in `mathlib`!).

The simplifier applies `simp` lemmas in one direction only: if `A = B` is a `simp`
lemma, then `simp` replaces `A`s with `B`s, but it doesn't replace
`B`s with `A`s. Hence a `simp` lemma should have the property that its
right-hand side is simpler than its left-hand side. In
particular, `=` and `↔` should not be viewed as symmetric operators in
this situation. The following would be a terrible `simp` lemma (if it
were even allowed):

```lean
@[simp] lemma mul_right_inv_bad (a : G) : 1 = a * a⁻¹ := ...
```

Replacing `1` with `a * a⁻¹` is not a sensible default direction to
travel. Even worse would be a lemma that causes expressions to grow
without bound, causing `simp` to loop forever:

```lean
@[simp] lemma even_worse_lemma: (1 : G) = 1 * 1⁻¹ := ...
```

When making a new definition, it is very common to also introduce
`simp` lemmas to put expressions involving the definition into a
sensible form. An example of this is in mathlib's
[data.complex.basic](https://github.com/leanprover-community/mathlib/blob/master/src/data/complex/basic.lean),
which has almost 100 `simp` lemmas. Even though they are true by definition, theorems such as
```lean
@[simp] lemma
add_re (z w : ℂ) : (z + w).re = z.re + w.re := rfl
```
are introduced because they give `simp` the ability to reduce expressions and then make use of pre-existing facts.
This one, for example, converts complex addition into real addition.
If you give `simp` permission to use commutativity of real addition, then it is able to
automatically prove `(z + w).re = (w + z).re` through `z.re + w.re =
w.re + z.re`, which is half of the proof that complex addition is commutative.

The Lean kernel itself is a rewrite system for lambda calculus, which has a definite
notion of forward progress.  With this in mind, a useful family of
`simp` lemmas are those that, in this sense, let `simp` partially evaluate an
expression. For example, if you have a structure type `foo` and
define a structure `my_foo` with that type,
```lean
structure foo := (n : ℕ)

def my_foo : foo := {n := 37}
```
then if you add a `simp` lemma that `my_foo.n = 37`, you give the simplifier the
ability to evaluate the `foo.n` projection for `my_foo`, which saves you from having
to unfold the definition of `my_foo` (by default `simp` does not unfold most definitions).
Creating these `simp` lemmas is so common that there is an attribute that creates
them all for you automatically:
```lean
@[simps] def my_foo : foo := {n := 37}
```
This generates the lemma `@[simp] lemma my_foo_n : my_foo.n = 37`.

## Basic usage 

* `simp` tries to simplify the goal using all `simp` lemmas known to
          Lean at that time.

* `simp [h1, h2]` uses all `simp` lemmas and also `h1` and `h2` (which can either be local hypotheses or other lemmas which are not tagged `simp` for some reason).

* `simp [← h]` uses all `simp` lemmas, and also `h : A = B` but in the form `B = A` (so `simp` rewrites `B`s to `A`s)

* `simp [-thm]` stops `simp` from using the `simp` lemma named `thm`.

* `simp *` uses all `simp` lemmas and also all current local hypotheses to try to simplify the goal.

* `simp at h` tries to simplify `h` using all `simp` lemmas.

* `simp [h1] at h2 ⊢` tries to simplify both `h2` and the goal using `h1` and all `simp` lemmas (note: type `⊢` with `\|-` or `\vdash` in VS Code).

* `simp * at *` : tries to simplify both the goal and all hypotheses, using all hypotheses and all `simp` lemmas. Sometimes worth a try.

* `simp only [h1, h2, ..., hn]` tells `simp` to use only the lemmas `h1`, `h2`, ..., rather than the full set of simp lemmas.
(It is acceptable to use `simp only [...]` in the middle of a proof, because subsequent changes to the `simp` set will not break the proof.)

Note that some `simp` lemmas have additional hypotheses that must be satisfied.
For example, a theorem about cancelling a factor on both sides of an equation would
only be valid under the hypothesis that the factor is non-zero. If `h`
is a proof of hypothesis `P` and `P → A = B` is a `simp` lemma, then
`simp [h]` will replace `A`'s with `B`'s in the goal. The fact that
`simp` considers additional hypotheses is the reason it is called a
*conditional* term rewriting system.

## Simp-normal form

There are sometimes several ways to say the same thing. For example,
if `n : ℕ` then the hypotheses `n ≠ 0`, `0 ≠ n`, `n > 0`, `0 < n`,
`1 ≤ n` and `n ≥ 1` are all logically equivalent. This can be
problematic for rewriting systems like the simplifier. The reason for this is
that the simplifier looks for subterms using *syntactic equality*. If the
simplifier is working on a term `T` and `A = B` is a `simp` lemma,
then, unless a subterm `A'` of `T` is syntactically the same as `A`
(approximately: they have literally the same textual representation), then `simp` won't
in general notice the rule applies, so it won't
be rewritten by `B`. Similarly, if nonzeroness of `n` (stated in
one way) is a precondition in a `simp` lemma of the form `A = B`, and `h` is a proof
of nonzeroness of `n` (stated in a different way), then `simp [h]` might
not replace `A`'s with `B`'s.

The way this issue is dealt with in `mathlib` is to fix once and for
all a *`simp` normal form* for the way something is to be expressed
(like `0 < n` for nonzeroness) and then sticking to this variant when
stating lemmas in Lean. This saves having to write duplicate lemmas
for every variant. To help the simplifier out, many times there are
normalizing lemmas whose only purpose is to put expressions into
`simp` normal form.

In general, if you are writing a lemma, you should know the "normal
form" way to express the ideas in the lemma. If you are writing a
lemma about a definition you made yourself, think about the normal
forms for ideas that can be expressed in more than one way.

An example of a `simp` normal form is a way of expressing nonemptiness
of a subset of a type.  If `α : Type` and `s : set α` then
nonemptiness of `s` can be expressed as both `s.nonempty` and `s ≠ ∅`.
In mathlib an effort is made to stick to `s.nonempty` as the normal
form.

Another example: every finite set `s : finset α` can be coerced
to `set α`, so for `a : α` one can write both `a ∈ s` and
`a ∈ (s : set α)` to mean the same thing.  The simp normal form for
membership in a finite set idea is `a ∈ s`, and moreover there is a
normalizing `simp` lemma
```lean
@[simp] lemma mem_coe {a : α} {s : finset α} : a ∈ (s : set α) ↔ a ∈ s := ...
```
to replace occurrences of `a ∈ (s : set α)` with the correct normal form.

Because the simplifier works from the inside out, simplifying
arguments of a function before simplifying the function, a `simp`
lemma should have the arguments to the function on its left-hand side in simp-normal
form. For example if `g 0` can be simplified, then `@[simp] lemma foo : f (g 0) = 0` will never be used.
Mathlib's `simp_nf` linter checks for this
(you can run mathlib's linters for a module yourself by putting `#lint` at the end of the file).

## `simpa`

The `simpa` tactic is a variation on `simp` for finishing a proof -- as a "finishing" tactic, it will fail
if it's unable to close the goal.  The basic usage is
```lean
simpa [h1, h2] using e
```
where `[h1, h2]` refers to an optional list of `simp` lemmas (using the same syntax as for `simp`)
and where `e` is an expression.  Commonly, `e` is the name of a hypothesis.
Both the type of `e` and the goal are simplified, and `simpa` succeeds if they are both simplified to the same thing.

Here is a simple example of `simpa`:
```lean
example (n : ℕ) (h : n + 1 - 1 ≠ 0) : n + 1 ≠ 1 :=
begin
  simpa using h,
end
```
Without `simpa`, we might do `simp at ⊢ h, exact h`.
So-called "non-terminal `simp`s", which are usages of `simp` that do not close a goal,
are best to be avoided (see the next section), and `simpa` is a way to avoid them.

If the `using` clause is not present, then `simpa` does the following three steps instead:

1. The goal is simplified.
2. If a hypothesis named `this` is in the local context, then its type is simplified.
3. The `assumption` tactic is applied.

Step 2 is to support a pattern where `simpa` follows a `have : P` or `suffices : P`, since
both of these default to using `this` as the name of the hypothesis they introduce.

## Non-terminal `simp`s

The behaviour of `simp` changes over time as `simp` lemmas are added
to (or removed from) the library.  This means that proofs that use
`simp` can break, and, unless you know how the set of `simp` lemmas has
changed, it can be difficult to fix a proof.

For example if a proof looked like
```lean
  ...
  simp,
  rw foo_eq_bar,
  ...
```
and then later someone added the `@[simp]` attribute to `foo_eq_bar`,
this rewrite would now fail.

While it is fine using `simp` in the middle of a proof during initial development
("non-terminal `simp`s"), the rule of thumb is that it is
easier to maintain Lean code when every `simp` closes a goal
completely.  When such a `simp` later breaks, this ensures that the
intended goal is known.

There are a few "approved" uses of `simp` for the middle of a proof:

1) `simp only [h1, h2, ..., hn]` to constrain `simp` to using only
lemmas from the given list, so it is not affected by changes to the
set of `simp` lemmas. Hint: use `squeeze_simp` or `simp?` to
automatically generate an appropriate `simp only`.

2) Use a construct like `have h : P, { ..., simp }` to introduce a
hypothesis proved by `simp`. The `have` expression might be in the
middle of a proof, but the `simp` is closing the goal it introduces.

3) If `simp` turns your goal into `P`, then you can write
   ```lean
     suffices : P,
     simpa,
   ```
   This adds a new goal of `P` after the current one, introduces a new
hypothesis `this : P`, simplifies both the goal and `this`,
then attempts to close the goal with `this`.  The `simpa` tactic *requires*
that a goal be closed, unlike `simp`, which makes it easier to know when it breaks.
The explicit `P` in the source code helps in finding a fix.

One way non-terminal `simp`s can appear is in a sequence of tactics like `simp at ⊢ h, exact h`.
These can be replaced by `simpa using h`.

## `dsimp`

`dsimp` is a variant of `simp` that only uses "definitional" `simp`
lemmas.  These are `simp` lemmas whose proof is `rfl` or `iff.rfl`,
that is, lemmas where the two sides are equal by definition.

Like `simp` it is recommended that you do not use it in the middle of
a proof.  However if `dsimp` turns your goal into `h` then `change h`
will likely do the same thing.  Another common use of `dsimp` is
```lean
dsimp only
```
which is short for `dsimp only []`, a `dsimp` with an empty set of `simp` lemmas.
This can be safely used in the middle of a proof, and it can be a useful
way to tidy up a goal: among other things, it does beta reduction for lambda expressions
(it will turn `(λ x, f x) 37` into `f 37`) and it will reduce structure projections
(it will turn `{to_fun := f, ...}.to_fun` into `f`).

## More advanced features

### Full syntax

This is the full syntax for the `dsimp` tactic:

> `dsimp` (`only`)? (`*` | `[` list of lemmas `]`)? (`with` simp sets)? (`at` locations)? (`{` configuration options `}`)?

where "( ... )?" means an optional part of the expression, and "|" gives mutually exclusive options.
The list of lemmas is similar to that of `rw`, but additionally `-lemma_name` means a lemma is excluded from the set of `simp` lemmas.
Configuration options are described in a following section.

This is the full syntax for the `simp` tactic:

> `simp` (`!`)? (`?`)? (`only`)? (`*` | `[` list of lemmas `]`)? (`with` simp sets)? (`at` locations)? (`{` configuration options `}`)?

If `!` is present, it adds `iota_eqn := tt` to the configuration options.
If `?` is present, it causes `simp` to suggest a set of `simp` lemmas that suffice.

This is the full syntax for the `simpa` tactic:

> `simpa` (`!`)? (`?`)? (`only`)? (`*` | `[` list of lemmas `]`)? (`with` simp sets)? (`using` expr)? (`{` configuration options `}`)?

The meanings are the same as for `simp`, but `using` can be given any expression, not just a local constant as required by `at`.

### Custom simp attributes

Using the command [`mk_simp_attribute`](https://leanprover-community.github.io/mathlib_docs/commands.html#mk_simp_attribute),
you can make your own `@[simp]`-like attribute, but with a key difference:
lemmas tagged with `@[new_attr]` are _not_ in the default set of `simp` lemmas.
Instead, they are included using the syntax `simp with new_attr`. This can often replace lengthy 
`simp only [...]` calls and facilitate easier-to-read code. Some examples of common usage are 
[`mfld_simps`](https://leanprover-community.github.io/mathlib_docs/find/simp_attr.mfld_simps/src),
and [`field_simps`](https://leanprover-community.github.io/mathlib_docs/find/simp_attr.field_simps/src).

### Configuration options

Both `simp` and `dsimp` can take additional configuration options using record syntax.
For example, `simp {single_pass := tt}` runs `simp` with the `single_pass` configuration option set to true.
One can use `single_pass` to avoid loops that might otherwise occur.

The core Lean file `init/meta/simp_tactic.lean` reveals other configuration options in
the `dsimp_config` and `simp_config` structures.
Most of them not very relevant for the average user,
and some of them are not fully documented.  These are reproduced in the
following table, where the default value for a configuration option
for `simp` or `dsimp` is given in the respective column -- if no
default value is present, that option is unavailable.
The "max" default value refers to `simp.default_max_steps`, which is currently `10000000`.

| Option | `simp` | `dsimp` | Description |
| --- | --- | --- | --- |
| `contextual` | `ff` | | Use additional `simp` lemmas based on the context of the current subexpression (see example below)  |
| `single_pass` | `ff` | `ff` | Visit each subterm no more than once |
| `md` | | `reducible` | Reduction mode: how aggressively constants are replaced with their definitions (`all`, `semireducible`, `instances`, `reducible`, or `none`) |
| `max_steps` | max | max | The maximum number of steps allowed before failing |
| `fail_if_unchanged` | `tt` | `tt` | Fail if no simplifications applied |
| `beta` | `tt` | `tt` | Do beta-reductions: `(λ x, a) y` ↝ `a[x := y]` |
| `eta` | `tt` | `tt` | Allow eta-equivalence: `(λ x, f x)` ↝ `f` |
| `zeta`| `tt` | `tt` | Do zeta-reductions: `let x := a in b` ↝ `b[x := a]` |
| `proj` | `tt` | `tt` | Reduce projections: `prod.fst (a, b)` ↝ `a` |
| `iota` | `tt` | `tt` | Reduce recursors: `nat.rec_on (succ n) Z R` ↝ `R n (nat.rec_on n Z R)` |
| `iota_eqn` | `ff` | | Reduce using all equation lemmas generated by the equation compiler |
| `unfold_reducible` | | `ff` | Unfold definitions with `reducible` transparency (delta-reduce) |
| `memoize` | `tt` | `tt` | Perform caching of simps of subterms |
| `lift_eq` | `tt` | | Prove reflexive relations using proofs of equality (?) |
| `use_axioms` | `tt` | | Allow using `propext` and `funext` to rewrite under binders and to use `A ↔ B` `simp` lemmas |
| `constructor_eq` | `tt` | | Use injectivity of constructors in equalities  |
| `canonize_instances` | `tt` | `tt` | Replace instances with a canonical defeq one |
| `canonize_proofs` | `ff` |  | Replace proofs with a canonical defeq one |
| `discharger` | fail | | Tactic used to discharge new subgoals created during simplification; if it fails, the simplifier tries to discharge them by simplifying |

The `b[x := a]` notation means to replace all free instances of `x` in `b` with `a`.

Setting `constructor_eq` to `tt` will reduce equations of the form
`X a1 a2... = Y b1 b2...` to false if `X` and `Y` are distinct
constructors for the same type, and to `a1 = b1 ∧ a2 = b2 ∧ ...` if
`X` and `Y` are the same constructor.

Another interesting option is `iota_eqn` (in fact, `simp!` is shorthand for
`simp {iota_eqn := tt}`). This adds equation lemmas generated by the
equation/pattern-matching compiler to the set of `simp` lemmas.

The `contextual` option gives `simp` the ability to consider
hypotheses as additional `simp` lemmas based on a subexpression's
surrounding context. For example, as it simplifies the consequent of an
implication it temporarily adds the antecedent as a `simp` lemma. This
is necessary for the following example:
```lean
example {x y : ℕ} : x = 0 → y = 0 → x = y :=
begin
  simp { contextual := tt},
end
```

Amusing trick: if you do `simp _` then Lean will interpret `_` as a placeholder for the configuration options.
Since it can't figure out the configuration options through unification, it will instead print an error
along with all the default configuration values.
This works for other tactics that take a configuration as well, such as `rw`.
