---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56604tacticunfreezelocalinstances.html
---

## [general](index.html)
### [tactic.unfreeze_local_instances](56604tacticunfreezelocalinstances.html)

#### [Kenny Lau (Oct 28 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136670895):
```lean
import analysis.topology.topological_space
universe u
open set
local attribute [instance] classical.prop_decidable
class t0_space (α : Type u) [topological_space α] : Prop :=
(t0 : ∀ x y, x ≠ y → ∃ U:set α, is_open U ∧ (xor (x ∈ U) (y ∈ U)))

theorem exists_open_singleton_of_fintype
  (α : Type u) [topological_space α] [t0_space α]
  [f : fintype α] [decidable_eq α] [ha : nonempty α] :
  ∃ x:α, is_open ({x}:set α) :=
have H : ∀ (T : finset α), T ≠ ∅ → ∃ x ∈ T, ∃ u, is_open u ∧ {x} = {y | y ∈ T} ∩ u :=
begin
  intro T,
  apply finset.case_strong_induction_on T,
  { intro h, exact (h rfl).elim },
  { intros x S hxS ih h,
    by_cases hs : S = ∅,
    { existsi [x, finset.mem_insert_self x S, univ, is_open_univ],
      rw [hs, inter_univ], refl },
    { rcases ih S (finset.subset.refl S) hs with ⟨y, hy, V, hv1, hv2⟩,
      by_cases hxV : x ∈ V,
      { cases t0_space.t0 x y (λ hxy, hxS $ by rwa hxy) with U hu,
        rcases hu with ⟨hu1, ⟨hu2, hu3⟩ | ⟨hu2, hu3⟩⟩,
        { existsi [x, finset.mem_insert_self x S, U ∩ V, is_open_inter hu1 hv1],
          apply set.ext,
          intro z,
          split,
          { intro hzx,
            rw set.mem_singleton_iff at hzx,
            rw hzx,
            exact ⟨finset.mem_insert_self x S, ⟨hu2, hxV⟩⟩ },
          { intro hz,
            rw set.mem_singleton_iff,
            rcases hz with ⟨hz1, hz2, hz3⟩,
            cases finset.mem_insert.1 hz1 with hz4 hz4,
            { exact hz4 },
            { have h1 : z ∈ {y : α | y ∈ S} ∩ V,
              { exact ⟨hz4, hz3⟩ },
              rw ← hv2 at h1,
              rw set.mem_singleton_iff at h1,
              rw h1 at hz2,
              exact (hu3 hz2).elim } } },
        { existsi [y, finset.mem_insert_of_mem hy, U ∩ V, is_open_inter hu1 hv1],
          apply set.ext,
          intro z,
          split,
          { intro hz,
            rw set.mem_singleton_iff at hz,
            rw hz,
            refine ⟨finset.mem_insert_of_mem hy, hu2, _⟩,
            have h1 : y ∈ {y} := set.mem_singleton y,
            rw hv2 at h1,
            exact h1.2 },
          { intro hz,
            rw set.mem_singleton_iff,
            cases hz with hz1 hz2,
            cases finset.mem_insert.1 hz1 with hz3 hz3,
            { rw hz3 at hz2,
              exact (hu3 hz2.1).elim },
            { have h1 : z ∈ {y : α | y ∈ S} ∩ V := ⟨hz3, hz2.2⟩,
              rw ← hv2 at h1,
              rw set.mem_singleton_iff at h1,
              exact h1 } } } },
      { existsi [y, finset.mem_insert_of_mem hy, V, hv1],
        apply set.ext,
        intro z,
        split,
        { intro hz,
          rw set.mem_singleton_iff at hz,
          rw hz,
          split,
          { exact finset.mem_insert_of_mem hy },
          { have h1 : y ∈ {y} := set.mem_singleton y,
            rw hv2 at h1,
            exact h1.2 } },
        { intro hz,
          rw hv2,
          cases hz with hz1 hz2,
          cases finset.mem_insert.1 hz1 with hz3 hz3,
          { rw hz3 at hz2,
            exact (hxV hz2).elim },
          { exact ⟨hz3, hz2⟩ } } } } }
end,
begin
  tactic.unfreeze_local_instances,
  cases ha with x,
  specialize H finset.univ (finset.ne_empty_of_mem $ finset.mem_univ x),
  rcases H with ⟨y, hyf, U, hu1, hu2⟩,
  existsi y,
  have h1 : {y : α | y ∈ finset.univ} = (univ : set α),
  { exact set.eq_univ_of_forall (λ x : α,
      by rw mem_set_of_eq; exact finset.mem_univ x) },
  rw h1 at hu2,
  rw set.univ_inter at hu2,
  rw hu2,
  exact hu1
end
```

#### [Kenny Lau (Oct 28 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136670896):
Why do I need `tactic.unfreeze_local_instances` there?

#### [Kenny Lau (Oct 28 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136670937):
(working example, but clearly not minimal)

#### [Mario Carneiro (Oct 28 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136671127):
because it's a typeclas arg left of the colon

#### [Mario Carneiro (Oct 28 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136671141):
you can use `unfreezeI` for short

#### [Kenny Lau (Oct 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136671337):
I don't understand

#### [Kenny Lau (Oct 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136671338):
isn't every typeclass argument left of colon?

#### [Chris Hughes (Oct 28 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136672307):
You don't usually do `cases ` on type class args

#### [Kenny Lau (Oct 28 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136672310):
yeah even if I don't do cases it still messes up

#### [Mario Carneiro (Oct 28 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136672815):
anything that disrupts the context past the position of the colon will require `unfreezeI`

#### [Mario Carneiro (Oct 28 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136672827):
in this case you can do `cases id ha with a` if you don't want to clear the hypothesis in the context

#### [Kenny Lau (Oct 28 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136672869):
oh, I get it now

#### [Kenny Lau (Oct 28 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136672878):
oh and how would you golf the proof?

#### [Mario Carneiro (Oct 28 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136672888):
I've been thinking about that... that proof is a little scary long

#### [Mario Carneiro (Oct 28 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136672900):
Maybe you can find a maximal element in the specialization preorder?

#### [Kenny Lau (Oct 28 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673208):
I don't understand what you mean by the specialization preorder

#### [Mario Carneiro (Oct 28 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673248):
okay, I refreshed my memory on the [specialization preorder](https://en.wikipedia.org/wiki/Specialization_(pre)order) and indeed this proof should work (although it is a minimal element by wiki's definition)

#### [Mario Carneiro (Oct 28 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673257):
it's basically finite zorn's lemma

#### [Kevin Buzzard (Oct 28 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673318):
A point x specialises to a point y if y is in the closure of x

#### [Mario Carneiro (Oct 28 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673388):
I think that's the reverse of wiki's terminology?

#### [Mario Carneiro (Oct 28 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673398):
they say y is a specialization of x in that case

#### [Mario Carneiro (Oct 28 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673422):
they also say that the orientation is contentious

#### [Kevin Buzzard (Oct 28 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673448):
Darn Zulip app doesn't show me new posts when they arrive

#### [Kevin Buzzard (Oct 28 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673490):
Including my own

#### [Kevin Buzzard (Oct 28 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673513):
Right -- x specialises to y, so y is a specialisation of x.

#### [Mario Carneiro (Oct 28 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673520):
okay, I wasn't sure about the active verb there

#### [Kevin Buzzard (Oct 29 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673587):
This is how the words are used in algebraic geometry at least

#### [Mario Carneiro (Oct 29 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673661):
You should look at the wiki page and decide which order of le makes sense

#### [Mario Carneiro (Oct 29 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673675):
I'm leaning to the first definition, `x <= y` means x is a specialization of y, because the evidence from algebraic geometry using Spec R smacks of that order-reversing filter thing

#### [Reid Barton (Oct 29 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136674194):
The ordering I have seen is the one which is equivalent to x \le y if closure({x}) is a subset of closure({y})

#### [Reid Barton (Oct 29 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136674320):
Actually, I'm not sure which way it goes now and my source is at home

#### [Mario Carneiro (Oct 29 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136674734):
I'm not sure why this argument doesn't extend to the infinite case by zorn's lemma though

#### [Mario Carneiro (Oct 29 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136674742):
Obviously it's not true for R so I'm missing a part of the argument

#### [Kenny Lau (Oct 29 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136680702):
https://github.com/leanprover/mathlib/pull/448

#### [Kevin Buzzard (Oct 29 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136690249):
```quote
Obviously it's not true for R so I'm missing a part of the argument
```
For sensible spaces like R the preorder is just "x<=y iff x=y". So there are maximal and minimal elements, but these do not correspond to open singletons.

#### [Reid Barton (Oct 29 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136702815):
Okay, the paper where I've encountered this actually says "... so that $$\le_X$$ is the well-known [4] reflexive and transitive relation $$y \in \{x\}^-$$", so I did have this backwards.

#### [Reid Barton (Oct 29 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136708004):
After being confused by this for a while, my conclusion is that the "$$x$$ specializes to $$y$$" relation is actually different in algebraic geometry and in domain theory

#### [Reid Barton (Oct 29 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136708039):
one of them has to do with closed sets, the other with open sets

#### [Reid Barton (Oct 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136708108):
Because of the duality between open and closed sets, this appears as a reversal of the order

#### [Kevin Buzzard (Oct 29 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136715016):
In algebraic geometry, a "generic point" of an irreducible algebraic variety is a rigorous notion of the intuitive idea of how a general point on the variety behaves. Historically this was done in a vague way -- we had the "actual points" and then "it's true for a generic point" just meant "most points satisfy this" with several, sometimes competing definitions of "most", but with Grothendieck's approach we have the luxury of the generic point actually being a point in the top space, whose topological closure is the entire variety. The idea is that a generic point can specialise to a random "actual point", which is then a specialisation of the generic point. Perhaps the simplest example of this is the two-point topological space with one closed and one open point. A fruitful mental model of this space in geometry is that the whole space is the open unit disc, the closed point is the origin, and the open point is all the other points --  a "general" point in the open disc. If $$\eta$$ is the generic point and $$s$$ the closed point then the sequence $$\eta,\eta,\eta,\ldots$$ converges to $$s$$ (as well as to $$\eta$$), which is the specialisation in action. One cna think of it as a bunch of points in the punctured disc tending to the origin.

