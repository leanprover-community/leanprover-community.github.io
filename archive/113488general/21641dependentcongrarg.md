---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21641dependentcongrarg.html
---

## Stream: [general](index.html)
### Topic: [dependent congr_arg?](21641dependentcongrarg.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575693):
I am assuming this is provable: `example (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) := sorry`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575733):
The goal is `P f H2 = P g _`, and we have `H1 : f = g`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575737):
but I can't rewrite

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575741):
because `H2` is a proof of something involving f

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575781):
Have you tried `congr`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575786):
I would have to rewrite `f` and `H2` simultaneously.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575789):
use congr

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575795):
:-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575798):
Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575806):
So what does congr do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575814):
By which I mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575818):
how would I do this in term mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575829):
simp should also work here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575836):
I thought I tried it and it failed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575846):
simp doesn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575849):
that was what made me ask

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575853):
Kevin, you should spend more time reading documentation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575856):
?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575895):
`example (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) := by cc`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575903):
you win

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575907):
:-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575908):
https://github.com/leanprover/mathlib/pull/114

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575911):
Yes, I saw it, and I even read Gabriel's explanation of what cc did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575913):
Oh, Gabriel wrote some comment

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575916):
But the bottom line is that I still don't know what's going on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575926):
all I know is that I'm relieved to find that I'm trying to prove something which is true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575941):
Some months ago I would just have been happy to accept the magic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575945):
but now I am more interested in knowing how the magic works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575981):
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
(H1 ▸ λ _, rfl : ∀ h, P f H2 = P g h) _
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575987):
For example I don't see how to use `congr_arg` or `congr_fun`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125575994):
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
eq.drec_on H1 rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576000):
Thanks Kenny

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576007):
I was about to say "how do you prove this from `eq.rec`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576008):
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
by subst H1
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576011):
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
by simp [H1]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576012):
what is this `subst`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576016):
tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576026):
takes hypothesis of the form `[expr] = h` or `h = [expr]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576029):
where `h` is any variable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576035):
and discharge the hypothesis while substituting everything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576037):
I like the subst proof best, in some sense, because it is closest to how I am thinking about what needs to be done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576052):
@**Mario Carneiro** I now realise that `simp` by itself had no chance of working :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576134):
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

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576217):
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
eq.drec rfl H1
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576221):
should be the shortest term mode solution

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576226):
The subst proof only works because one side is a variable here, but it is able to avoid the DTT problems that many other tactics have to face in this situation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576287):
```lean
theorem test : ∀ (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type), P f H2 = P g (H1 ▸ H2)
| _ _ rfl _ _ := rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576298):
what is so funny about that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576299):
`simp` and `congr` both work by using congruence lemmas. These are generated on the fly and the term for them is a bit complicated but the structure is similar: from `a = b` and `c = d` derive `f a c = f a b`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576321):
The real power is that the generated congruence lemma automatically makes use of subsingletons to avoid hypotheses, meaning that if `c` and `d` are proofs then you only have one hypothesis there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576372):
the `rfl` proof there is the term mode equivalent of `by subst`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576377):
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
by cases H1; refl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576409):
```quote
the `rfl` proof there is the term mode equivalent of `by subst`
```
depends on what you mean by equivalent

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576448):
```quote
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
(H1 ▸ λ _, rfl : ∀ h, P f H2 = P g h) _
```
```
This one is my favourite :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576451):
and `subst` is basically the same as `cases` or `induction` on an equality (although it does additional equality specific stuff like symmetry)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576459):
Oh I just saw the `|` one :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576460):
I think the `rfl` proof is equivalent to `by cases`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576472):
and the `by subst` one is equivalent to `eq.drec`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576475):
(because `eq.drec` is the proof generated by `by subst`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576482):
(and the `| rfl` one is really invoking the inductive type and equality between constructors

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576487):
like I said, they are all the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576501):
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

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576512):
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

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576514):
they're exactly the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576562):
`eq.dcases_on` is the same as `eq.drec` I believe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576565):
no there's an id_rhs` in one but not the other

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576583):
```lean
theorem test (f : ℕ → ℕ) (g : ℕ → ℕ) (H1 : f = g) (H2 : f 0 = 0) (P : Π (h : ℕ → ℕ), h 0 = 0 → Type) : P f H2 = P g (H1 ▸ H2) :=
eq.dcases_on H1 rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576588):
I think you would get the exact same term if you use `by refl` instead of `rfl` in the term proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576593):
```quote
no there's an id_rhs` in one but not the other
```
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576615):
I like the `|` proof because it is a really powerful way of doing the substitution.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576657):
the term mode equivalent is `cases`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576680):
If you replace `f` and `g` by constants this proof won't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576691):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576696):
you'd need to generalize

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576705):
or simp

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576716):
simp uses congr, so it can do dependent rewrite

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576757):
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

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576787):
I think that's the same proof term after some beta reduction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576799):
as what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576806):
the last few

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576812):
every proof is equal because of proof irrelevance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576822):
Well, modulo `#reduce` reduction I think all proofs so far are the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576901):
church rosser much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 23 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576913):
did you check out my paper? C-R is false in lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 23 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125576916):
I couldn't find your paper

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587726):
Kenny: https://github.com/digama0/lean-type-theory/releases/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587729):
and the reason I'm reviving this thread is that I discovered that in my use case, not all of the solutions worked.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587794):
my actual goal is `extend_map_of_im_unit (g ∘ of_comm_ring R S) _ = extend_map_of_im_unit (of_comm_ring R S) H` where `of_comm_ring R S` is a ring homomorphism, so quite a bit more structurally complicated than my toy MWE

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587818):
and `congr` gave me three random goals, one of which was `loc R S = (R × ↥S)` and that might not even be true.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587820):
`cc` also didn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587878):
but Kenny's `eq.drec_on H1 rfl` worked.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587883):
simp didn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587896):
both subst and simp complained that H1 wasn't an appropriate lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587898):
even though it was of the form X = Y

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125587957):
I realise now that I am using tactics less and less, I am on the whole doing quite abstract maths and the arguments are in some sense straightforward to show from first principles, so I don't really need any tactics beyond `rw`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125588601):
aargh actually none of them worked :-/ the `eq.drec` approach looks like it works, but an error appears elsewhere. `cases H1` gave me an error I'd never seen before :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125588610):
```
cases tactic failed, unsupported equality between type and constructor indices
(only equalities between constructors and/or variables are supported, try cases on the indices):
(λ (x : R), g (of_comm_ring R S x)) = λ (r : R), ⟦(r, ⟨1, _⟩)⟧

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125588683):
that's surprising because H1 is `of_comm_ring R S = g ∘ of_comm_ring R S`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 23 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20congr_arg%3F/near/125588685):
I don't need this lemma, I might give up on it.

