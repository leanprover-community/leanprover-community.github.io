---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/91327producttopology.html
---

## [maths](index.html)
### [product topology](91327producttopology.html)

#### [Rohan Mitta (Jul 24 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130223243):
Hi! I'm trying to define the product topology and am running into issues. I may have made a silly mistake somewhere, but it seems  to me that "I" should have type set (set (α × β)), but I get a type mismatch error. Any help would be greatly appreciated.

```lean
import analysis.topology.continuity
import analysis.topology.topological_space
open set filter lattice classical


def product_top {α : Type*} {β : Type*} (X : topological_space α) (Y : topological_space β) : topological_space (α × β) :=
{is_open := λ (W : set (α × β), ∃ (I : (set_of (λ (b : set (α × β)), ∃ (U : set α) (V : set β), is_open U ∧ is_open V ∧ b = set.prod U V))), W = ⋃₀ I, 
 is_open_univ := sorry, is_open_inter := sorry, is_open_sUnion := sorry}
```

#### [Johan Commelin (Jul 24 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130223261):
This is already in mathlib. Did you know that?

#### [Kevin Buzzard (Jul 24 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130223528):
first error for me is at the comma after alpha x beta

#### [Kevin Buzzard (Jul 24 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130223543):
because it's expecting a close bracket

#### [Kevin Buzzard (Jul 24 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130223738):
Your I seems to have type `↥{b : set (α × β) | ∃ (U : set α) (V : set β), is_open U ∧ is_open V ∧ b = set.prod U V}`

#### [Kevin Buzzard (Jul 24 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130223994):
```lean
#check λ (α : Type) (β : Type) [topological_space α] [topological_space β], (set_of (λ (b : set (α × β)), 
           ∃ (U : set α) (V : set β), is_open U ∧ is_open V ∧ b = set.prod U V))
```

#### [Kevin Buzzard (Jul 24 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130224051):
that has type `Π (α β : Type) [_inst_1 : topological_space α] [_inst_2 : topological_space β], set (set (α × β))`

#### [Kevin Buzzard (Jul 24 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130224168):
So this term: `(set_of (λ (b : set (α × β)), 
           ∃ (U : set α) (V : set β), is_open U ∧ is_open V ∧ b = set.prod U V))` is the term which has type `set (set (α × β))`

#### [Kevin Buzzard (Jul 24 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130224281):
and in particular that's just a term. OK so when you ask that there exists a term `I` which has type [that term above], Lean says "wait, that's a term, not a type, how can he want a term of that type? Oh I know I'll turn that `set_of` term above into a subtype, and then `I` can be a term of that type.

#### [Kevin Buzzard (Jul 24 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130224737):
Yeah it all makes sense -- 
```lean
#check @set_of 
-- set_of : Π {α : Type u_1}, (α → Prop) → set α
```

`set_of` eventually produces a term `t` of type `set X` for some `X`, and your `I` is a term of type `t` so you're one layer too deep

#### [Rohan Mitta (Jul 24 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130235708):
Thanks, that's made it a lot clearer. I think I'll be able to figure it out from there.

#### [Rohan Mitta (Jul 24 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130235779):
Hi Johan,
```quote
This is already in mathlib. Did you know that?
```
I did not know that. Where can I find it?

#### [Luca Gerolla (Jul 24 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130240623):
Hi Rohan, it's an instance at line 909 of topological_space

#### [Luca Gerolla (Jul 24 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130240646):
```lean
instance [t₁ : topological_space α] [t₂ : topological_space β] : topological_space (α × β) :=
induced prod.fst t₁ ⊔ induced prod.snd t₂
```

#### [Luca Gerolla (Jul 25 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130240856):
Should be equivalent to the "canonical" product topology you defined, but don't know if that easy to prove :/

#### [Kevin Buzzard (Jul 25 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130242698):
In maths this says "define a topology on $$\alpha\times\beta$$ to be the smallest topology such that the following sets are all open: first all the $$U\times\beta$$ for $$U\subseteq\alpha$$ open, and second all the $$\alpha\times V$$ for $$V\subseteq\beta$$ open."

#### [Kevin Buzzard (Jul 25 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130242868):
The reason it says this is that the induced topology on $$\alpha\times\beta$$ coming from the projection down to $$\alpha$$ that's what `prod.fst` is) is precisely the one where the open sets are pre-images of opens in $$\alpha$$.

#### [Kevin Buzzard (Jul 25 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product topology/near/130242945):
And the reason that this is the product topology is first that all those sets are open in the product topology, and conversely that in any topology where these sets are all open, the intersection of two such sets is open, and that's precisely $$U\times V$$, so any such topology will contain all the sets which are open in the product topology.

