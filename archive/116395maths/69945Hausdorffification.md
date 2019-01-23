---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/69945Hausdorffification.html
---

## Stream: [maths](index.html)
### Topic: [Hausdorffification](69945Hausdorffification.html)

---


{% raw %}
#### [ Kenny Lau (Oct 18 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026443):
```lean
import analysis.topology.continuity

universes u v

variables (α : Type u) [t : topological_space α]
include t

def Hausdorffification.setoid : setoid α :=
{ r := λ x y, ∀ (s : setoid α) [t2_space (quotient s)], @setoid.r α s x y,
  iseqv := ⟨λ _ s _, s.2.1 _, λ _ _ H s ht2, s.2.2.1 (@H s ht2),
    λ _ _ _ H1 H2 s ht2, s.2.2.2 (@H1 s ht2) (@H2 s ht2)⟩ }

local attribute [instance] Hausdorffification.setoid

@[reducible] def Hausdorffification : Type u :=
quotient (Hausdorffification.setoid α)

instance Hausdorffification.t2_space :
  t2_space (Hausdorffification α) :=
{ t2 := λ x y, quotient.induction_on₂ x y $ λ m n H,
    begin
      letI := classical.prop_decidable,
      simp only [ne.def, quotient.eq, (≈), setoid.r, not_forall] at H,
      rcases H with ⟨r, ht2, H⟩, resetI,
      let f : Hausdorffification α → quotient r,
      { refine λ e, quotient.lift_on' e quotient.mk _,
        intros a b H, apply quotient.sound, apply H },
      have hf : continuous f,
      { intros s hs,
        change is_open (quotient.mk ⁻¹' _),
        rw ← set.preimage_comp,
        exact hs },
      rcases t2_separation (mt quotient.exact H) with ⟨u, v, h1, h2, h3, h4, h5⟩,
      refine ⟨_, _, hf _ h1, hf _ h2, h3, h4, set.eq_empty_of_subset_empty _⟩,
      exact λ x H, set.eq_empty_iff_forall_not_mem.1 h5 (f x) H
    end }
```

#### [ Kenny Lau (Oct 18 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026483):
Is there any way to do this constructively?

#### [ Johannes Hölzl (Oct 18 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026590):
usually the relation is defined as "define $a \sim b$ if any open set containing $a$ intersects any open set containing $b$". maybe this works constructively?

#### [ Kenny Lau (Oct 18 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026600):
you need to iterate that transfinitely many times to have a T2 space

#### [ Kenny Lau (Oct 18 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026609):
and that would involve induction-recursion (is the name right?) which is stronger than Lean

#### [ Mario Carneiro (Oct 18 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026660):
Why? What is the idea behind this definition

#### [ David Michael Roberts (Oct 18 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026664):
https://ncatlab.org/nlab/show/Hausdorff+space#in_constructive_mathematics

#### [ Mario Carneiro (Oct 18 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026689):
by the way, I think that the definition of T2 in mathlib is contrapositive of the right one

#### [ Mario Carneiro (Oct 18 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026771):
which apparently nLab calls "weakly Hausdorff"

#### [ Mario Carneiro (Oct 18 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026901):
also, I don't see any nonconstructivity in that proof

#### [ Kenny Lau (Oct 18 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136042314):
I used not_forall

#### [ Kenny Lau (Oct 18 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136049981):
```quote
Why? What is the idea behind this definition
```
quotient a lot until you get a T2 space, but don't quotient more than necessary

#### [ Mario Carneiro (Oct 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136049993):
what's the problem with Johannes's definition

#### [ Kenny Lau (Oct 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136050007):
that it doesn't produce a T2 space

#### [ Mario Carneiro (Oct 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136050017):
why

#### [ Mario Carneiro (Oct 18 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136050064):
like where does the proof break down

#### [ Kenny Lau (Oct 18 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136050068):
https://topospaces.subwiki.org/wiki/Hausdorffization#Example_to_illustrate_why_one_step_isn.27t_enough

#### [ Mario Carneiro (Oct 18 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136061666):
> you need to iterate that transfinitely many times to have a T2 space
> and that would involve induction-recursion (is the name right?) which is stronger than Lean

You don't need proof principles stronger than lean. You just need to know that the process stops eventually, by bounding the space of possible relations

#### [ Mario Carneiro (Oct 18 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136061871):
although topospaces wiki is shamefully cavalier about defining an ordinal indexed sequence of topological spaces with direct limits and then just saying "take $$h^\infty$$" as if that were well defined

#### [ Mario Carneiro (Oct 18 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136061992):
In lean, it is an interesting example of an inductive predicate that is positive but not strictly positive

#### [ Mario Carneiro (Oct 18 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136062288):
```
inductive hausify : α → α → Prop
| refl : ∀ x, hausify x x
| trans : ∀ x y z, hausify x y → hausify y z → hausify x z
| haus : ∀x y, (∀ u v : set α, is_open u → is_open v →
   x ∈ u → y ∈ v → ∃ z w, z ∈ u ∧ w ∈ v ∧ hausify z w) → hausify x y
```
This definition is monotone but not syntactically

#### [ Mario Carneiro (Oct 18 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136062874):
So here's how you can do the transfinite induction construction:
```lean
inductive hausify1 (haus : α → α → Prop) : α → α → Prop
| trans : ∀ x y z, hausify1 x y → hausify1 y z → hausify1 x z
| haus : ∀x y, (∀ u v : set α, is_open u → is_open v →
   x ∈ u → y ∈ v → ∃ z w, z ∈ u ∧ w ∈ v ∧ haus z w) → hausify1 x y

inductive hausify_transfinite : (α → α → Prop) → Prop
| zero : hausify_transfinite eq
| succ : ∀ r, hausify_transfinite r → hausify_transfinite (hausify1 r)
| lim : ∀ R : set (α → α → Prop), (∀ r ∈ R, hausify_transfinite r) →
  hausify_transfinite (hausify1 (λ x y, ∃ r ∈ R, (r : α → α → Prop) x y))

def hausify (x y : α) : Prop := ∃ r, hausify_transfinite r ∧ r x y
```
Needless to say I prefer your definition

#### [ Kenny Lau (Oct 18 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136066103):
I prefer yours

#### [ Mario Carneiro (Oct 18 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136066687):
this whole construction is doing something similar to yours, quotienting by all relations that are hausdorffish

#### [ Mario Carneiro (Oct 18 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136066706):
it's easier to say `t2_space (quotient r)` than all this

#### [ Kenny Lau (Oct 19 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136074995):
can you define ε_0 using that?

#### [ Kenny Lau (Oct 19 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075001):
oh wait you already defined ordinal notations inductively

#### [ Kenny Lau (Oct 19 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075035):
wait no I'm confused

#### [ Mario Carneiro (Oct 19 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075791):
This allows you to do transfinite iteration over a fixed type

#### [ Mario Carneiro (Oct 19 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075805):
the key is the fact that it is all taking place in one complete lattice

#### [ Kenny Lau (Oct 19 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075818):
I see

#### [ Kenny Lau (Oct 19 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075820):
So you can't define ordinals using this zero-lim-succ

#### [ Mario Carneiro (Oct 19 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075869):
You have to build an inductive `Type` to do that

#### [ Mario Carneiro (Oct 19 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075877):
by the way epsilon_0 is the supremum of all ordinals with `ordinal_notation`

#### [ Mario Carneiro (Oct 19 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075881):
in case you wanted to define it

#### [ Mario Carneiro (Oct 19 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075909):
It is possible to extend ordinal notations to epsilon_0 and beyond using the veblen hierarchy, but I don't think anyone around here cares about large countable ordinals

#### [ Mario Carneiro (Oct 19 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075974):
I think we also have what we need to define omega_1^CK using computable functions

#### [ Kevin Buzzard (Oct 19 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136093605):
Is this a reflection?


{% endraw %}
