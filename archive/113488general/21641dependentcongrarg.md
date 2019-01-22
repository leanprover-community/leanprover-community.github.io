---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21641dependentcongrarg.html
---

## [general](index.html)
### [dependent congr_arg?](21641dependentcongrarg.html)

#### [Kevin Buzzard (Apr 23 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575693):
I am assuming this is provable: `example (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) := sorry`

#### [Kevin Buzzard (Apr 23 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575733):
The goal is `P f H2 = P g _`, and we have `H1 : f = g`

#### [Kevin Buzzard (Apr 23 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575737):
but I can't rewrite

#### [Kevin Buzzard (Apr 23 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575741):
because `H2` is a proof of something involving f

#### [Simon Hudon (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575781):
Have you tried `congr`?

#### [Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575786):
I would have to rewrite `f` and `H2` simultaneously.

#### [Mario Carneiro (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575789):
use congr

#### [Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575795):
:-)

#### [Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575798):
Thanks!

#### [Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575806):
So what does congr do?

#### [Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575814):
By which I mean

#### [Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575818):
how would I do this in term mode

#### [Mario Carneiro (Apr 23 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575829):
simp should also work here

#### [Kevin Buzzard (Apr 23 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575836):
I thought I tried it and it failed

#### [Kevin Buzzard (Apr 23 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575846):
simp doesn't work

#### [Kevin Buzzard (Apr 23 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575849):
that was what made me ask

#### [Patrick Massot (Apr 23 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575853):
Kevin, you should spend more time reading documentation

#### [Kevin Buzzard (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575856):
?

#### [Patrick Massot (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575895):
`example (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) := by cc`

#### [Kenny Lau (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575903):
you win

#### [Kevin Buzzard (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575907):
:-)

#### [Patrick Massot (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575908):
https://github.com/leanprover/mathlib/pull/114

#### [Kevin Buzzard (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575911):
Yes, I saw it, and I even read Gabriel's explanation of what cc did

#### [Patrick Massot (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575913):
Oh, Gabriel wrote some comment

#### [Kevin Buzzard (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575916):
But the bottom line is that I still don't know what's going on

#### [Kevin Buzzard (Apr 23 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575926):
all I know is that I'm relieved to find that I'm trying to prove something which is true

#### [Kevin Buzzard (Apr 23 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575941):
Some months ago I would just have been happy to accept the magic

#### [Kevin Buzzard (Apr 23 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575945):
but now I am more interested in knowing how the magic works

#### [Kenny Lau (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575981):
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
(H1 ▸ λ _, rfl : ∀ h, P f H2 = P g h) _
```

#### [Kevin Buzzard (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575987):
For example I don't see how to use `congr_arg` or `congr_fun`

#### [Kenny Lau (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125575994):
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
eq.drec_on H1 rfl
```

#### [Kevin Buzzard (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576000):
Thanks Kenny

#### [Kevin Buzzard (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576007):
I was about to say "how do you prove this from `eq.rec`

#### [Kenny Lau (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576008):
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
by subst H1
```

#### [Kenny Lau (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576011):
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
by simp [H1]
```

#### [Kevin Buzzard (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576012):
what is this `subst`?

#### [Kenny Lau (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576016):
tactic

#### [Kenny Lau (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576026):
takes hypothesis of the form `[expr] = h` or `h = [expr]`

#### [Kenny Lau (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576029):
where `h` is any variable

#### [Kenny Lau (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576035):
and discharge the hypothesis while substituting everything

#### [Kevin Buzzard (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576037):
I like the subst proof best, in some sense, because it is closest to how I am thinking about what needs to be done

#### [Kevin Buzzard (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576052):
@**Mario Carneiro** I now realise that `simp` by itself had no chance of working :-)

#### [Kenny Lau (Apr 23 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576134):
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
by subst H1

#print test

/-
theorem test : ∀ (f g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type), P f H2 = P g _ :=
λ (f g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type),
  eq.drec (eq.refl (P f H2)) H1
-/
```

#### [Kenny Lau (Apr 23 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576217):
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
eq.drec rfl H1
```

#### [Kenny Lau (Apr 23 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576221):
should be the shortest term mode solution

#### [Mario Carneiro (Apr 23 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576226):
The subst proof only works because one side is a variable here, but it is able to avoid the DTT problems that many other tactics have to face in this situation

#### [Kenny Lau (Apr 23 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576287):
```lean
theorem test : ∀ (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type), P f H2 = P g (H1 ▸ H2)
| _ _ rfl _ _ := rfl
```

#### [Kenny Lau (Apr 23 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576298):
what is so funny about that

#### [Mario Carneiro (Apr 23 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576299):
`simp` and `congr` both work by using congruence lemmas. These are generated on the fly and the term for them is a bit complicated but the structure is similar: from `a = b` and `c = d` derive `f a c = f a b`.

#### [Mario Carneiro (Apr 23 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576321):
The real power is that the generated congruence lemma automatically makes use of subsingletons to avoid hypotheses, meaning that if `c` and `d` are proofs then you only have one hypothesis there

#### [Mario Carneiro (Apr 23 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576372):
the `rfl` proof there is the term mode equivalent of `by subst`

#### [Kenny Lau (Apr 23 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576377):
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
by cases H1; refl
```

#### [Kenny Lau (Apr 23 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576409):
```quote
the `rfl` proof there is the term mode equivalent of `by subst`
```
depends on what you mean by equivalent

#### [Kevin Buzzard (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576448):
```quote
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
(H1 ▸ λ _, rfl : ∀ h, P f H2 = P g h) _
```
```
This one is my favourite :-)

#### [Mario Carneiro (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576451):
and `subst` is basically the same as `cases` or `induction` on an equality (although it does additional equality specific stuff like symmetry)

#### [Kevin Buzzard (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576459):
Oh I just saw the `|` one :-)

#### [Kenny Lau (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576460):
I think the `rfl` proof is equivalent to `by cases`

#### [Kenny Lau (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576472):
and the `by subst` one is equivalent to `eq.drec`

#### [Kenny Lau (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576475):
(because `eq.drec` is the proof generated by `by subst`)

#### [Kenny Lau (Apr 23 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576482):
(and the `| rfl` one is really invoking the inductive type and equality between constructors

#### [Mario Carneiro (Apr 23 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576487):
like I said, they are all the same

#### [Kenny Lau (Apr 23 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576501):
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
by cases H1; refl

#print test

/-
theorem test : ∀ (f g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type), P f H2 = P g _ :=
λ (f g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type),
  eq.dcases_on H1
    (λ (H_1 : g = f), eq.rec (λ (H1 : f = f) (H_2 : H1 == eq.refl f), eq.refl (P f H2)) (eq.symm H_1) H1)
    (eq.refl g)
    (heq.refl H1)
-/
```

#### [Kenny Lau (Apr 23 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576512):
```lean
theorem test : ∀ (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type), P f H2 = P g (H1 ▸ H2)
| _ _ rfl _ _ := rfl

#print test

/-
theorem test : ∀ (f g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type), P f H2 = P g _ :=
λ (f g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type),
  eq.dcases_on H1
    (λ (H_1 : g = f), eq.rec (λ (H1 : f = f) (H_2 : H1 == eq.refl f), id_rhs (P f H2 = P f H2) rfl) (eq.symm H_1) H1)
    (eq.refl g)
    (heq.refl H1)
-/
```

#### [Kenny Lau (Apr 23 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576514):
they're exactly the same

#### [Mario Carneiro (Apr 23 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576562):
`eq.dcases_on` is the same as `eq.drec` I believe

#### [Kevin Buzzard (Apr 23 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576565):
no there's an id_rhs` in one but not the other

#### [Kenny Lau (Apr 23 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576583):
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
eq.dcases_on H1 rfl
```

#### [Mario Carneiro (Apr 23 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576588):
I think you would get the exact same term if you use `by refl` instead of `rfl` in the term proof

#### [Kenny Lau (Apr 23 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576593):
```quote
no there's an id_rhs` in one but not the other
```
aha

#### [Kevin Buzzard (Apr 23 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576615):
I like the `|` proof because it is a really powerful way of doing the substitution.

#### [Kenny Lau (Apr 23 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576657):
the term mode equivalent is `cases`

#### [Mario Carneiro (Apr 23 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576680):
If you replace `f` and `g` by constants this proof won't work

#### [Kenny Lau (Apr 23 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576691):
right

#### [Kenny Lau (Apr 23 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576696):
you'd need to generalize

#### [Mario Carneiro (Apr 23 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576705):
or simp

#### [Mario Carneiro (Apr 23 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576716):
simp uses congr, so it can do dependent rewrite

#### [Kenny Lau (Apr 23 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576757):
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
by congr; from H1

#print test

/-
theorem test : ∀ (f g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type), P f H2 = P g _ :=
λ (f g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type),
  (λ (h h_1 : ℕ → ℕ) (e_1 : h = h_1) (a : h 0 = 0) (a_1 : h_1 0 = 0),
     (λ (h h_1 : ℕ → ℕ) (e_1 : h = h_1) (a : h 0 = 0), eq.drec (eq.refl (P h (eq.rec a (eq.refl h)))) e_1) h h_1
       e_1
       a)
    f
    g
    H1
    H2
    (H1 ▸ H2)
-/
```

#### [Mario Carneiro (Apr 23 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576787):
I think that's the same proof term after some beta reduction

#### [Kenny Lau (Apr 23 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576799):
as what?

#### [Mario Carneiro (Apr 23 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576806):
the last few

#### [Kenny Lau (Apr 23 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576812):
every proof is equal because of proof irrelevance

#### [Mario Carneiro (Apr 23 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576822):
Well, modulo `#reduce` reduction I think all proofs so far are the same

#### [Kenny Lau (Apr 23 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576901):
church rosser much

#### [Mario Carneiro (Apr 23 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576913):
did you check out my paper? C-R is false in lean

#### [Kenny Lau (Apr 23 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125576916):
I couldn't find your paper

#### [Kevin Buzzard (Apr 23 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125587726):
Kenny: https://github.com/digama0/lean-type-theory/releases/

#### [Kevin Buzzard (Apr 23 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125587729):
and the reason I'm reviving this thread is that I discovered that in my use case, not all of the solutions worked.

#### [Kevin Buzzard (Apr 23 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125587794):
my actual goal is `extend_map_of_im_unit (g ∘ of_comm_ring R S) _ = extend_map_of_im_unit (of_comm_ring R S) H` where `of_comm_ring R S` is a ring homomorphism, so quite a bit more structurally complicated than my toy MWE

#### [Kevin Buzzard (Apr 23 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125587818):
and `congr` gave me three random goals, one of which was `loc R S = (R × ↥S)` and that might not even be true.

#### [Kevin Buzzard (Apr 23 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125587820):
`cc` also didn't work

#### [Kevin Buzzard (Apr 23 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125587878):
but Kenny's `eq.drec_on H1 rfl` worked.

#### [Kevin Buzzard (Apr 23 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125587883):
simp didn't work

#### [Kevin Buzzard (Apr 23 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125587896):
both subst and simp complained that H1 wasn't an appropriate lemma

#### [Kevin Buzzard (Apr 23 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125587898):
even though it was of the form X = Y

#### [Kevin Buzzard (Apr 23 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125587957):
I realise now that I am using tactics less and less, I am on the whole doing quite abstract maths and the arguments are in some sense straightforward to show from first principles, so I don't really need any tactics beyond `rw`.

#### [Kevin Buzzard (Apr 23 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125588601):
aargh actually none of them worked :-/ the `eq.drec` approach looks like it works, but an error appears elsewhere. `cases H1` gave me an error I'd never seen before :-)

#### [Kevin Buzzard (Apr 23 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125588610):
```
cases tactic failed, unsupported equality between type and constructor indices
(only equalities between constructors and/or variables are supported, try cases on the indices):
(λ (x : R), g (of_comm_ring R S x)) = λ (r : R), ⟦(r, ⟨1, _⟩)⟧

```

#### [Kevin Buzzard (Apr 23 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125588683):
that's surprising because H1 is `of_comm_ring R S = g ∘ of_comm_ring R S`.

#### [Kevin Buzzard (Apr 23 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent congr_arg?/near/125588685):
I don't need this lemma, I might give up on it.

