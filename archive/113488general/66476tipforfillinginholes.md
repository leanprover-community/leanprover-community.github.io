---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66476tipforfillinginholes.html
---

## Stream: [general](index.html)
### Topic: [tip for filling in holes](66476tipforfillinginholes.html)

---

#### [Kevin Buzzard (Apr 20 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125425455):
Sometimes in Lean you sit down to write a definition or a theorem, knowing that it will be really easy and fun. I was just in that situation. I need to write down some maps between localized rings and prove that they have some properties, but now I know that the localization interface is excellent and that pretty much every single one of my proofs will look like `name_of_function _ _ _ _ _`.

#### [Kevin Buzzard (Apr 20 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125425597):
However, I have run into an unexpected annoyance.

#### [Kevin Buzzard (Apr 20 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125425716):
Here is my skeleton set-up.

#### [Kevin Buzzard (Apr 20 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125425811):
```lean
definition localization.loc_loc_is_loc {R : Type u} [comm_ring R] {f g : R} (H : Spec.D' g ⊆ Spec.D' f) :
(localization.away g) ≃ᵣ localization.away (localization.of_comm_ring R (powers f) g) := 
{ to_fun := _,
  inv_fun := _,
  left_inv := _,
  right_inv := _,
  is_ring_hom := _
}
```

#### [Kevin Buzzard (Apr 20 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426022):
The idea now is that I just fill in all the holes one by one.

#### [Kevin Buzzard (Apr 20 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426090):
But I want the holes to have red squiggles under them!

#### [Kevin Buzzard (Apr 20 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426138):
And for some reason, only the last one does

#### [Kevin Buzzard (Apr 20 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426449):
and the associated complaint is full of metavariables

#### [Kevin Buzzard (Apr 20 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426465):
because it depends on some earlier holes

#### [Kenny Lau (Apr 20 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426472):
begin end

#### [Kevin Buzzard (Apr 20 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426501):
and then remove it later?

#### [Kevin Buzzard (Apr 20 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426565):
because it's a def

#### [Kenny Lau (Apr 20 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426587):
i just fill in stuff in front of begin end

#### [Kenny Lau (Apr 20 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426641):
I mean, replace your _ with begin end

#### [Kenny Lau (Apr 20 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426744):
I can show you that in person next week ^^

#### [Kevin Buzzard (Apr 20 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426832):
`begin exact _ end`

#### [Kevin Buzzard (Apr 20 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426834):
:-)

#### [Kevin Buzzard (Apr 20 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426835):
Many thanks Kenny!

#### [Kevin Buzzard (Apr 20 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125427174):
I feel like there are so many little tips like this, and it's unclear to me where they should be put.

#### [Kenny Lau (Apr 20 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125427447):
you don’t need exact _

