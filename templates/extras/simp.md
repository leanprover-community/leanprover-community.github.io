# Simp

## Overview

In this document we will explain basic usage of Lean's simplifier
tactic [`simp`](https://leanprover-community.github.io/mathlib_docs/tactics.html#simp),
and the related tactic [`dsimp`](https://leanprover-community.github.io/mathlib_docs/tactics.html#dsimp).

## Introduction

Lean has a "simplifier", called `simp`, that consults a database of
facts called *`simp` lemmas* to (hopefully) simplify hypotheses and
goals. The simplifier is what is known as a *conditional term
rewriting system*: all it does is repeatedly replace (or *rewrite*)
subterms of the form `A` by `B`, for all applicable facts of the form
`A = B` or `A ↔ B`.

The simplifier mindlessly rewrites until it can rewrite no more.  The
`simp` lemmas are all oriented, with left-hand sides always being
rewritten by right-hand sides, and never vice versa. The database of
facts is curated such that things are put into some approximation of a normal
form, and (at least ideally) the facts are *confluent*, meaning the
order in which the simplifier considers rewrites does not matter.

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

This is also what the simplifier is doing. Indeed, if you add
`set_option trace.simplify.rewrite true` above the example, then a
squiggly blue underline will appear under `simp` (in VS Code) and
clicking on this will show you the sequence of rewrites that `simp`
performed.

The more verbose option `set_option trace.simplify true` shows
both the rewrites which works and those which failed during the
simplification process.

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

When the simplifier is attempting to simplify a term `T` it looks
through the `simp` lemmas known to the system at that time, and if it
runs into an applicable lemma of the form `A = B` or `A ↔ B` for which
`A` shows up in `T`, it rewrites the instance of `A` in `T` with `B`
and then starts again from the beginning. Note that `simp` starts on
innermost terms, working outward: it first simplifies the arguments of
a function before simplifying the function. Also, `simp` contains a some
amount of cleverness to be able to avoid considering *all* `simp`
lemmas every time (there are over ten thousand of them currently in `mathlib`!).

The simplifier works in one direction only: if `A = B` is a `simp`
lemma, then `simp` replaces `A`s with `B`s, but it doesn't replace
`B`s with `A`s. Hence a `simp` lemma should have the property that its
right-hand side should be simpler than its left-hand side. In
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

## Basic usage 

* `simp` tries to simplify the goal using all `simp` lemmas known to
          Lean at that time.

* `simp [h1, h2]` uses all `simp` lemmas and also `h1` and `h2` (which can either be local hypotheses or other lemmas which are not tagged `simp` for some reason).

* `simp [← h]` uses all `simp` lemmas, and also `h : A = B` but in the form `B = A` (so `simp` rewrites `B`s to `A`s)

* `simp [-thm]` stops `simp` from using the simp lemma `thm`.

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
```
@[simp] lemma mem_coe {a : α} {s : finset α} : a ∈ (s : set α) ↔ a ∈ s := ...
```
to replace occurrences of `a ∈ (s : set α)` by the correct normal form.

Because the simplifier works from the inside out, simplifying
arguments of a function before simplifying the function, a `simp`
lemma should have the arguments to the function on its left-hand side in simp-normal
form. For example if `g 0` can be simplified, then `@[simp] lemma foo : f (g 0) = 0` will never be used.
Mathlib's `simp_nf` linter checks for this
(you can run mathlib's linters for a module yourself by putting `#lint` at the end of the file).

## Non-terminal `simp`s, and `simpa`

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

While it is fine using `simp` in the middle of a proof when developing
a proof ("non-terminal `simp`s"), the rule of thumb is that it is
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
hypothesis called `this` into the current one, simultaneously
simplifies both the goal and `this`, then attempts to close the goal
with `this`.  The `simpa` tactic *requires* that a goal be closed, unlike
`simp`, which makes it easier to know when it breaks.
The explicit `P` in the source code helps with finding a fix.

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
way to tidy up a goal: it does beta reduction for lambda expressions
(it will turn `(λ x, f x) 37` into `f 37`) and it will reduce structure projections
(it will turn `{to_fun := f, ...}.to_fun` into `f`).

## More advanced features

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
One can use `single_pass` to avoid loops which would otherwise occur.

Searching for `structure dsimp_config` and `structure simp_config` in
the core Lean file `init/meta/simp_tactic.lean` reveals other
configuration options.  Most of them not very relevant for the average user,
and some of them are not fully documented.  These are reproduced in the
following table, where the default value for a configuration option
for `simp` or `dsimp` is given in the respective column -- if no
default value is present, that option is unavailable.
The "max" default value refers to `simp.default_max_steps`, which is currently `10000000`.

| Option | `simp` | `dsimp` | Description |
| --- | --- | --- | --- |
| `md` | | `reducible` | Reduction mode: how aggressively constants are replaced with their definitions (`all`, `semireducible`, `instances`, `reducible`, or `none`) |
| `max_steps` | max | max | The maximum number of steps allowed before failing |
| `canonize_instances` | `tt` | `tt` | Replace each instance with a canonical defeq one |
| `canonize_proofs` | `ff` |  |  |
| `single_pass` | `ff` | `ff` | Visit each subterm no more than once |
| `fail_if_unchanged` | `tt` | `tt` | Fail if no simplifications applied |
| `eta` | `tt` | `tt` | Allow eta-equivalence: `(λ x, F x)` ↝ `F` |
| `zeta`| `tt` | `tt` | Do zeta-reductions: `let x : a := b in c` ↝ `c[x/b]` |
| `beta` | `tt` | `tt` | Do beta-reductions: `(λ x, E) y` ↝ `E[x/y]` |
| `proj` | `tt` | `tt` | Reduce projections: `⟨a, b⟩.1` ↝ `a` |
| `iota` | `tt` | `tt` | Reduce recursors: `nat.rec_on (succ n) Z R` ↝ `R n (nat.rec_on n Z R)` |
| `iota_eqn` | `ff` | | Reduce using all equation lemmas generated by the equation compiler |
| `unfold_reducible` | | `ff` | Unfold definitions with `reducible` transparency (delta-reduce) |
| `memoize` | `tt` | `tt` | Perform caching of simps of subterms |
| `contextual` | `ff` | | |
| `lift_eq` | `tt` | | |
| `use_axioms` | `tt` | | |
| `constructor_eq` | `tt` | | Use injectivity of constructors in equalities  |

The `c[x/b]` notation means to replace all free instances of `x` in `c` with `b`.

Setting `constructor_eq` to `tt` will reduce equations of the form
`X a1 a2... = Y b1 b2...` to false if `X` and `Y` are distinct
constructors for the same type, and to `a1 = b1 ∧ a2 = b2 ∧ ...` if
`X = Y` are the same constructor.

Another interesting option is `iota_eqn` (in fact, `simp!` is shorthand for
`simp {iota_eqn := tt}`). This adds equation lemmas generated by the
equation/pattern-matching compiler to the set of `simp` lemmas.
