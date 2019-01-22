---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/54381inducedcoinduced.html
---

## [maths](index.html)
### [induced, coinduced, ...](54381inducedcoinduced.html)

#### [Kenny Lau (Jun 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116033):
If I have a function f:A->B with a topology on B, are the following two topologies on A x A the same?
1. equip A with the induced topology, and then do the product topology
2. build fxf:AxA->BxB and then use the induced topology, where BxB has the product topology

#### [Kenny Lau (Jun 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116036):
@**Mario Carneiro**

#### [Mario Carneiro (Jun 15 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116082):
They are equal but not defeq

#### [Kenny Lau (Jun 15 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116170):
@**Mario Carneiro** how do you suggest I prove it?

#### [Mario Carneiro (Jun 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116227):
you should be able to use some nonsense in the lattice of top spaces to prove it relatively easily

#### [Kenny Lau (Jun 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116242):
we have `induced_le` but not `le_induced`, so...

#### [Mario Carneiro (Jun 15 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116294):
isn't `induced` defined as some kind of supremum? That gives you a proof approach

#### [Kenny Lau (Jun 15 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116297):
i'll try

#### [Kenny Lau (Jun 15 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116302):
(no, prod is supremum, induced isn't)

#### [Kenny Lau (Jun 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116321):
oh and is there an idiom to obtain the categorical product of two functions?

#### [Mario Carneiro (Jun 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116410):
not particularly, `embedding_prod_mk` just uses `(λx:α×γ, (f x.1, g x.2))`

#### [Kenny Lau (Jun 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116416):
is that an idiom?

#### [Mario Carneiro (Jun 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116420):
I suppose

#### [Mario Carneiro (Jun 15 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116471):
I think `induced_sup` will help

#### [Mario Carneiro (Jun 15 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116474):
and `induced_compose`

#### [Kenny Lau (Jun 15 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116482):
why are they in `continuity` @_@

#### [Mario Carneiro (Jun 15 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116486):
because `induced` is really talking about continuous functions

#### [Mario Carneiro (Jun 15 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116491):
consider `continuous_iff_induced_le`

#### [Mario Carneiro (Jun 15 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116539):
also the proofs use continuity arguments

#### [Kenny Lau (Jun 15 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116668):
@**Mario Carneiro** oh my god I just realized I have been asking the wrong question

#### [Kenny Lau (Jun 15 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116683):
f:A->B be a set-theoretic function, and a topology on A. Are the following two topologies on BxB the same?
1. equip B with coinduced, and then product
2. coinduced from fxf:AxA->BxB, where AxA has the product topology

#### [Kenny Lau (Jun 15 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128116684):
let's say f is surjective

#### [Mario Carneiro (Jun 15 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128117009):
I expect so, try to prove it and find out

#### [Reid Barton (Jun 15 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128118668):
I'm almost certain they are not the same in general.

#### [Reid Barton (Jun 15 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128118746):
If A->B is a quotient map, then XxA->XxB need not be a quotient map. But I don't know the counterexample off-hand.

#### [Kenny Lau (Jun 15 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128118753):
I just proved it with one extra assumption

#### [Reid Barton (Jun 15 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128118770):
It's true if X is locally compact, or in your original question if A and B are

#### [Reid Barton (Jun 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128118814):
what was your extra assumption?

#### [Kenny Lau (Jun 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128118818):
```lean
example (α : Type*) (β : Type*)
  [t : topological_space α] (f : α → β)
  (hf1 : function.surjective f)
  (hf2 : ∀ S, is_open S → is_open (f ⁻¹' (f '' S))) :
  @prod.topological_space β β
        (@topological_space.coinduced α β f t)
        (@topological_space.coinduced α β f t)
    = @topological_space.coinduced (α × α) (β × β)
        (λ p, (f p.1, f p.2)) prod.topological_space :=
have H1 : prod.fst ∘ (λ p : α × α, (f p.1, f p.2)) = f ∘ prod.fst,
  from rfl,
have H2 : prod.snd ∘ (λ p : α × α, (f p.1, f p.2)) = f ∘ prod.snd,
  from rfl,
have H3 : topological_space.induced f (topological_space.coinduced f t) ≤ t,
  from induced_le_iff_le_coinduced.2 $ le_refl _,
by letI := topological_space.coinduced f t;
from le_antisymm
  (lattice.sup_le
    (induced_le_iff_le_coinduced.1 (by rw [induced_compose, H1, ← induced_compose];
      from le_trans (induced_mono H3) lattice.le_sup_left))
    (induced_le_iff_le_coinduced.1 (by rw [induced_compose, H2, ← induced_compose];
      from le_trans (induced_mono H3) lattice.le_sup_right)))
  (λ S hs, is_open_prod_iff.2 $ λ x y hxy,
  let ⟨m, hm⟩ := hf1 x, ⟨n, hn⟩ := hf1 y in
  let ⟨u, v, hu, hv, hmu, hnv, H⟩ := is_open_prod_iff.1 hs m n (by simpa [hm, hn] using hxy) in
  ⟨f '' u, f '' v, hf2 u hu, hf2 v hv, ⟨m, hmu, hm⟩, ⟨n, hnv, hn⟩,
    λ ⟨p, q⟩ ⟨⟨P, hp1, hp2⟩, ⟨Q, hq1, hq2⟩⟩,
    by simp at hp2 hq2; rw [← hp2, ← hq2]; from @H (P, Q) ⟨hp1, hq1⟩⟩)
```

#### [Kenny Lau (Jun 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/induced%2C%20coinduced%2C%20.../near/128118820):
that the map be open

