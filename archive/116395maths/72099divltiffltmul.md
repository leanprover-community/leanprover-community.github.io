---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/72099divltiffltmul.html
---

## Stream: [maths](index.html)
### Topic: [div_lt_iff_lt_mul](72099divltiffltmul.html)

---

#### [Kevin Buzzard (Jan 15 2019 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155161891):
I just wanted to get from `a<b*c` to `a/c<b` (on the real  numbers) with a hypothesis that `c>0`. I was surprised to find that although all three of `div_lt_iff_lt_mul`, `lt_mul_of_div_lt` and `div_lt_of_lt_mul` were in Lean, they were in `data.int.basic` :-) and only applied to ints. This should be some general lemma about ordered monoids or some such thing, right? I might start doing what Chris always encourages me to do, which is to make a super-short PR, assuming that this is actually something missing from mathlib. But is it there and I missed it?

#### [Kevin Buzzard (Jan 15 2019 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155162157):
Currently struggling to find ordered monoids :-/ Do we only have ordered additive monoids?

#### [Mario Carneiro (Jan 15 2019 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155163224):
it should be in `ordered_field` somewhere

#### [Mario Carneiro (Jan 15 2019 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155163236):
`div_lt_iff`

#### [Mario Carneiro (Jan 15 2019 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155163385):
lean core has several more long winded unidirectional versions - `div_lt_of_mul_lt_of_pos` , I can't find the reverse direction

#### [Kevin Buzzard (Jan 15 2019 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155164568):
Aah! This is a theorem about multiplication and 0 (which is to do with addition) so indeed it's not about monoids. Maybe it's about ordered semirings? Thanks Mario.

#### [Mario Carneiro (Jan 15 2019 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155164872):
It's a theorem about fields because division

#### [Mario Carneiro (Jan 15 2019 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155164927):
division doesn't exist on monoids or groups

#### [Kevin Buzzard (Jan 15 2019 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155164929):
Oh of course. ok it all makes sense now :-)

#### [Kevin Buzzard (Jan 15 2019 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155164934):
Now I'm just annoyed that I didn't go through this thought process myself before asking.

#### [Kevin Buzzard (Jan 15 2019 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155164954):
Had I taken the trouble to try and formalise what statement I thought was true for ordered monoids I suspect I would have made more progress on my own...

#### [Mario Carneiro (Jan 15 2019 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155165038):
you might wonder why division isn't defined for groups, and this is one of the differences from add_groups, which have subtraction, but there is a difference between the total division on groups and the almost total division on fields and it doesn't seem to be helpful to unify them; lots of theorems overlap with a name conflict, but they are all proven differently

