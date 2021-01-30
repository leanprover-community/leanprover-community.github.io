# Simp

## Overview

In this document we will explain basic usage of Lean's simplifier,
`simp`, and the related tactic `dsimp`.

## Introduction

Lean has a "simplifier", called `simp`. This is a tactic whose job,
unfortunately for beginners, is *not* to prove an arbitrary simple
statement. Lean's simplifier is what is called a "conditional term
rewriting system". Rewriting is the act of changing a goal of the form
`P(A)` into `P(B)`, given a hypothesis of the form `A = B` or `A ↔
B`. The simplifier's job is to try and prove, or at least simplify,
goals or hypotheses, by using repeated rewrites. Here is an example
(using `mathlib`).

```lean
import algebra.group.defs

variables (G : Type) [group G] (a b c : G)

example : a * a⁻¹ * 1 * b = b * c * c⁻¹ :=
begin
  simp
end
```

How would a human solve that goal? They would notice that `a * a⁻¹ =
1`, that `1 * 1 = 1` and so on, until they had simplified the example
to `b = b`, which is obviously true.

This is also what the simplifier is doing. Indeed, if you add
`set_option trace.simplify.rewrite true` above the example, then a
squiggly blue underline will appear under `simp` (in VS Code) and
clicking on this will show you the sequence of rewrites that `simp`
discovered.

The more verbose option `set_option trace.simplify true` shows
both the rewrites which works and those which failed during the
simplification process.

## Simp lemmas

So how did Lean's simplifier know that `a * a⁻¹ = 1`? It is because
the corresponding lemma in `algebra.group.defs` is tagged with the
`simp` attribute:

```lean
@[simp] lemma mul_right_inv (a : G) : a * a⁻¹ = 1 := ...
```

This `@[simp]` at the beginning just "tags" `mul_right_inv` with the
`simp` attribute. We call lemmas tagged in this way "`simp`
lemmas". Here are some examples of `simp` lemmas in mathlib:

```lean
@[simp] theorem nat.dvd_one {n : ℕ} : n ∣ 1 ↔ n = 1 := ...
@[simp] theorem mul_eq_zero {a b : ℕ} : a * b = 0 ↔ a = 0 ∨ b = 0 := ...
@[simp] theorem list.mem_singleton {a b : α} : a ∈ [b] ↔ a = b := ...
@[simp] theorem set.set_of_false : {a : α | false} = ∅ := ...
```

When the simplifier is attempting to simplify a term `T` it looks
through the `simp` lemmas known to the system at that time, in a
sensible way (there are over ten thousand of them currently in
`mathlib`!), and if it runs into a lemma of the form `A = B` or `A ↔
B`, for which `A` shows up in `T`, it rewrites the lemma at `T` to
replace it with a `B`, and starts again. Note that `simp` works
frmo the inside out: it first simplifies the arguments of a function before
simplifying the function.

The simplifier works in one direction only: if `A = B` is a
`simp` lemma, then `simp` replaces `A`s with `B`s, but it doesn't
replace `B`s with `A`s. Hence a `simp` lemma should have the property
that its right hand side should be simpler than its left hand side. In
particular, `=` and `↔` should not be viewed as symmetric operators in
this situation. The following lemma

```lean
@[simp] lemma mul_right_inv_bad (a : G) : 1 = a * a⁻¹ := ...
```

would be a terrible `simp` lemma; the simplifier would then attempt to
replace `1` with `a * a⁻¹`, which is usually not a sensible direction
of travel. Furthermore, if both `mul_right_inv` and
`mul_right_inv_bad` are tagged with `simp` then this would cause the
simplifier to loop.

When making a new definition, it is very common to have `@[simp]`
lemmas which train the simplifier how to use the definition in a
sensible manner. An example of this is in mathlib's
[data.complex.basic](https://github.com/leanprover-community/mathlib/blob/master/src/data/complex/basic.lean),
which has almost 100 `simp` lemmas in. Theorems such as `@[simp] lemma
add_re (z w : ℂ) : (z + w).re = z.re + w.re := rfl` are proved in that
file, even though they are true by definition, because they are
important `simp` lemmas. The very slick proof in that file that the
complex numbers are a commutative ring uses `simp` at a key moment to
reduce goals such as `(z + w).re = (w + z).re` into `z.re + w.re =
w.re + z.re`, which is a statement about real numbers which the `ring`
tactic can solve.

## Basic usage 

`simp` -- tries to simplify the goal using all `simp` lemmas known to
          Lean at that time.

`simp [h1, h2]` -- uses all `simp` lemmas and also `h1` and `h2`
                   (which can either be local hypotheses or other lemmas which
		   are not tagged `simp` for some reason).

`simp [← h]` -- uses all `simp` lemmas, and also `h : A = B` but in
                 the form `B = A` (so `simp` rewrites `B`s to `A`s)

`simp [-thm]` -- stops `simp` from using the simp lemma `thm`.

`simp *` -- uses all `simp` lemmas and also all current local
            hypotheses to try to simplify the goal.

`simp at h` -- tries to simplify `h` using all `simp` lemmas.

`simp [h1] at h2 ⊢` -- tries to simplify both `h2` and the goal using
                       `h1` and all `simp` lemmas (note: type `⊢` with
                       `\|-` or `\vdash` in VS Code).

`simp * at *` -- tries to simplify both the goal and all hypotheses,
                 using all hypotheses and all `simp` lemmas. Sometimes
                 worth a try.

`simp only [h1, h2, ..., hn]` -- don't use all `simp` lemmas, but only
                                 the lemmas `h1`, `h2`, ... .


Note that some `simp` lemmas have preconditions. For example, a
theorem about cancelling a factor on both sides of an equation would
only be valid under the hypothesis that the factor is non-zero. If `h`
is a proof of hypothesis `P` and `P → A = B` is a `simp` lemma then
`simp [h]` will replace `A`'s with `B`'s in the goal. The fact that
`simp` works with preconditions is the reason it is called a
*conditional* term rewriting system.

## Simp-normal form

There are sometimes several ways to say the same thing. For example,
if `n : ℕ` then the hypotheses `n ≠ 0`, `0 ≠ n`, `n > 0`, `0 < n`, `1
≤ n` and `n ≥ 1` are all ways to say the same thing. This can be
problematic for rewriting systems like the simplifier. The reason is
that the simplifier works up to *syntactic equality*. If the
simplifier is working on a term `T`, and `A = B` is a `simp` lemma,
and there is a subterm `A'` in `T` which is logically equal or
equivalent to `A`, but not literally the same string of characters as
`A`, then the simplifier will in general not replace it with
`B`. Similarly, if nonzeroness of `n` (stated in one way) is a
precondition in a `simp` lemma of the form `A = B`, and `h` is a proof
of nonzeroness of `n` stated in a different way, then `simp [h]` might
not replace `A`'s with `B`'s.

A bad solution to this would be to write essentially the same lemma
many times, so each possible invariant is covered. Clearly this is not
ideal. The way this issue is dealt with in `mathlib` is to fix once
and for all a so-called "simp normal form" for a way of expressing
something such that `n ≠ 0` above, and then trying to stick to this
variant when stating lemmas in Lean. For example, most lemmas which
assume a natural is non-zero do it via the hypothesis `0 < n`.

In general, if you are writing a lemma, you should know the "normal
form" way to express the ideas in the lemma. If you are writing a
lemma about a definition you made yourself, you might want to make
your own design decision about the "normal form" way of expressing any
idea which can be naturally expressed in more than one way.

An example of a simp-normal form is a way of expressing nonemptiness
of a subset of a type.  If `α : Type` and `s : set α` then
nonemptiness of `s` can be expressed as `s.nonempty` and as `s ≠ ∅`.
In mathlib an effort is made to stick to `s.nonempty` as the normal
form.

Another example: if `s : finset α` and `a : α` then `a ∈ s` is defined
to mean `a ∈ (s : set α)`. The simp normal form for this idea is `a ∈
s`, and moreover the `simp` lemma

```
@[simp] lemma mem_coe {a : α} {s : finset α} : a ∈ (s : set α) ↔ a ∈ s := ...
```

will attempt to turn any occurrences of `a ∈ (s : set α)` into the
correct normal form.

Because the simplifier works from the inside out, simplifying arguments
of a function before simplifying the function, a `simp` lemma should
always have all of its arguments already in simp-normal form. Mathlib's
`simp_nf` linter check for this (you can run mathlib's linters by putting
`#lint` in a file).

## non-terminal `simp`s, and `simpa`

The behaviour of `simp` can change over time. More precisely, as more
`simp` lemmas are added to a repository, the smarter `simp` gets. This
means that updates to your code can cause proofs which use `simp` in
the middle, to break. For example if a proof looked like

```
  ...
  simp,
  rw foo_eq_bar,
  ...
```

and then later on someone added the `@[simp]` tag to `foo_eq_bar`,
then this rewrite would now fail, and errors like this can at times be
quite confusing to fix. If you really want to apply `simp` in the
middle of a proof and not close a goal completely, there are several
"approved" ways to do it:

1) Use `squeeze_simp` instead of `simp`. This produces output of the
form `simp only [h1, h2, ..., hn]`, which can be used instead of
`simp` to perform the same task. `simp only` is much safer to use in
the middle of a proof, because the simplifier is now constrained to
only using the lemmas in the list, so will not be affected by changes
to the `simp` set (the collection of lemmas tagged `simp`).

2) `simpa`. If `simp` turns your goal into `P`, then you can write
```
suffices : P,
  simpa,
```

which will add an extra goal of `P`, and then prove it using `simp`
and the hypothesis `this`, which is the proof of `P` which the
`suffices` tactic adds.

## `dsimp`

`dsimp` is a variant of `simp` which only uses `simp` lemmas whose
proof is `rfl` or `iff.rfl`, i.e. lemmas of the form `A = B` or `A ↔ B`
where `A` and `B` are equal by definition. Like `simp` it is not
recommended to use it in the middle of a proof, however if `dsimp`
turns your goal into `h` then `change h` might well do the same thing.
Another common use of `dsimp` is

```
dsimp only
```

which can be a very useful way of tidying up a goal. It can be safely
used in the middle of a proof because of the `only`. This command
tidies up lambdas (it will turn `(λ x, f x) 37` into `f 37`), and
structure projections (it will turn `{to_fun := f, ...}.to_fun`
into `f`).

## More advanced features.

`simp {single_pass := tt}` -- this `single_pass` is a config option,
one of around 16 at the time of writing. One can use `single_pass` to
avoid loops which would otherwise occur.

Searching for `structure simp_config` in the file
`init/meta/simp_tactic.lean` in core Lean reveals other config
options, not all of them documented, and most of them not very
relevant for the average user.

```lean
(max_steps : nat           := simp.default_max_steps)
(contextual : bool         := ff)
(lift_eq : bool            := tt)
(canonize_instances : bool := tt)
(canonize_proofs : bool    := ff)
(use_axioms : bool         := tt)
(zeta : bool               := tt)
(beta : bool               := tt)
(eta  : bool               := tt)
(proj : bool               := tt) -- reduce projections
(iota : bool               := tt)
(iota_eqn : bool           := ff) -- reduce using all equation lemmas generated by equation/pattern-matching compiler
(constructor_eq : bool     := tt)
(single_pass : bool        := ff)
(fail_if_unchanged         := tt)
(memoize                   := tt)
```

Setting `constructor_eq` to true will reduce equations of the form `X
a1 a2... = Y b1 b2...` to false if `X` and `Y` are distinct
constructors for the same type, and to `a1 = b1 and a2 = b2 and...` if
`X = Y` are the same constructor. Another interesting example is
`iota_eqn`. In fact `simp!` is shorthand for `simp {iota_eqn :=
tt}`. This adds non-trivial equation lemmas generated by the
equation/pattern-matching compiler to simp's list of simp lemmas.
