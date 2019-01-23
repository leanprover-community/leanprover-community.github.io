---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/18193extensions.html
---

## Stream: [maths](index.html)
### Topic: [extensions](18193extensions.html)

---

#### [Patrick Massot (Jul 16 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772133):
@**Johannes Hölzl**  At https://github.com/leanprover/mathlib/blob/master/analysis/topology/continuity.lean#L841-L843 do we really need that `[inhabited γ]`? It forces lots of other inhabited assumptions that seem unnecessary from a mathematical point of view. If γ is not inhabited then there shouldn't be that many `f : α → γ` to care about

#### [Mario Carneiro (Jul 16 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772434):
the inhabited is needed for `lim`

#### [Mario Carneiro (Jul 16 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772460):
because it takes a default value when the limit is not defined

#### [Patrick Massot (Jul 16 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772463):
I understand this

#### [Patrick Massot (Jul 16 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772485):
But one could hope for a definition not using `lim` then

#### [Mario Carneiro (Jul 16 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772566):
I recall puzzling over this definition a while ago; I also don't particularly like this style of definition

#### [Mario Carneiro (Jul 16 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772584):
it seems like we should already know that the limit is defined at this point

#### [Mario Carneiro (Jul 16 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772750):
I guess we need the assumption of `continuous_ext` to know the definition makes sense

#### [Mario Carneiro (Jul 16 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772839):
> It forces lots of other inhabited assumptions that seem unnecessary from a mathematical point of view. 

Do you have any particular examples?

#### [Patrick Massot (Jul 16 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772871):
Why? `ext de` is a function from `α → γ` to `β → γ`. Can't Lean be happy if both are uninhabited types and we don't write anything about the definition?

#### [Patrick Massot (Jul 16 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772922):
Examples are in my work in progress in the perfectoid project. I'm working on Hausdorff completions of uniform spaces.

#### [Mario Carneiro (Jul 16 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772943):
i mean maybe there is a way to pick an inhabitant in your setting

#### [Patrick Massot (Jul 16 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772945):
The completion functor, which is left-adjoint to the inclusion of Hausdorff and complete uniform spaces into all uniform spaces, is constructed on homs by extension

#### [Patrick Massot (Jul 16 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129772974):
If I assume the starting uniform space is inhabited then its completion is also inhabited, no problem. But it mean I keep assuming spaces are inhabited

#### [Mario Carneiro (Jul 16 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773022):
No, I mean somehow argue the empty case so it's not needed

#### [Patrick Massot (Jul 16 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773058):
If this is possible there, why isn't possible right in the definition of `dense_embedding.ext`

#### [Patrick Massot (Jul 16 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773067):
(by the way, this name is confusion since it has nothing to do with extensionality)

#### [Mario Carneiro (Jul 16 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773120):
Agreed. Do you have a suggestion?

#### [Patrick Massot (Jul 16 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773129):
about the name?

#### [Mario Carneiro (Jul 16 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773131):
yes

#### [Patrick Massot (Jul 16 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773136):
`dense_embedding.extension` maybe?

#### [Mario Carneiro (Jul 16 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773533):
I managed this definition:
```
def extend (de : dense_embedding e) (f : α → γ) (b : β) : γ :=
have nonempty γ, from
let ⟨_, ⟨_, a, _⟩⟩ := exists_mem_of_ne_empty
  (mem_closure_iff.1 (de.dense b) _ is_open_univ trivial) in ⟨f a⟩,
@lim _ (classical.inhabited_of_nonempty this) _ (map f (vmap e (nhds b)))
```

#### [Patrick Massot (Jul 16 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773551):
Scary! But I don't mind being scared by the definition: can you prove the expected properties?

#### [Mario Carneiro (Jul 16 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773631):
It's mostly just a proof getting stuck into the `inhabited γ` slot - it doesn't change any of the proofs

#### [Mario Carneiro (Jul 16 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773686):
all the proofs immediately after the definition still work, I may have to hunt down other uses

#### [Patrick Massot (Jul 16 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extensions/near/129773914):
and also hunt down the inhabited assumptions

