---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/70297completegroups.html
---

## Stream: [maths](index.html)
### Topic: [complete_groups](70297completegroups.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 26 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134699334):
 I think the last file you didn't edit is the one you accidentally removed yesterday: `complete_groups.lean`. Currently it's only purpose is the proof of `extend_Z_bilin` which is the crucial ingredient to extend the multiplication of a topological ring to its Hausdorff completion. Note that the separation in `extend_Z_bilin` and `extend_Z_bilin_key` is mostly because the proof was too long to elaborate for Lean to be used interactively (at least on my computer). But also, the key part is actually where stuff happens while the rest is massaging information which is already there. I'd be curious to see whether you can simplify this (I don't mean turn everything into term mode, I mean actual Lean or maths simplification). This closely follows Bourbaki (I can send you the pdf in English if needed) except that the massaging is completely implicit in Bourbaki.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 26 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134699567):
I would also be very curious to know, now that you're almost done reviewing and editing my work on completions and topological groups, whether you think my work has been useful for mathlib or whether it would have been quicker for you to start from scratch. I won't be sad anyway, because all this was an important part of my Lean training.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 26 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134699920):
I have an electronic copy of Bourbaki General Topology, Ch. 1 -4 (from 1995).

Your work is useful for mathlib! While I renamed and refactored a lot of stuff, it is still helpful to have a developed theory. Then its not about how to prove some things, but more on how I think it fits into mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 26 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134700176):
having finally the general top-ring completion would be very nice. One thing I was thinking about is that `is_Z_bilin` is a duplication of the `is_bilinear_map` in tensor product. But we can merge both (or replace `is_Z_bilin`) when Mario finishes his module rewrite.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 26 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134700302):
Oh sure, `is_Z_bilin` was written very quickly in order to be able to state the theorem. It could be replaced very easily with anything else

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 26 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134700549):
I'll spend the next two days traveling, but hopefully we'll have ring completions next week!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 27 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134729620):
ring completions is finished. Using your `extend_Z_bilin`, then it was straight forward!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 27 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134730885):
I'm reading that on my phone in a train so I may be wrong but it looks like you assume the topological ring is separated. This is cheating.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 27 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134731681):
Hm, I see.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 27 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134731689):
I think I already wrote that but I can't see it. You also need my description of the separation relation for topological groups

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 27 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134731692):
This is a reason why it was so easy :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 27 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134731776):
No, the main reason is that all the difficulty is in extend_Z_bilin

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 27 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134731780):
`group_separation_rel` is in https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L333

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 27 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134731839):
Yes this is the lemma I'm referring to

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 27 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134731853):
so, can we proof that `separation` is a subring?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 27 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134731863):
It ensures multiplication descends (lifts in CS language)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 27 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134731911):
hm, but maybe its easier to do the lifting the proper way. i.e. combine `extend` and `quotient.lift`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 27 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134731917):
yes, that's how the completion of the group structure works.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 27 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134734638):
So this construction is not the one in Bourbaki, or is it? Do you have a reference explaining the proof to show that multiplication lifts?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 28 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134849540):
I'm back from traveling, so I can answer this question. This construction is almost the construction in Bourbaki except that, again, their construction of the Hausdorff completion of anything is slightly different: first they quotient by the separation relation, and they take the space of minimal Cauchy filters. When doing ring completions, they first make a separated ring as I explained, and then go to the space of minimal Cauchy filters. In our setup, we only need to construct a (functorial) isomorphism between `completion (quotient separation_setoid a)` and `completion a`. If I remember correctly, I did that carefully on paper but not yet in Lean. Then we'll be ready to chain our two constructions (going from separated assumption to the completion, relying on `extend_Z_bilin` and going from no assumption to separated using `group_separation_rel`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 28 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134850101):
More details about this separation stuff: in Bourbaki GT this is III.6.4 page 276 (English edition), the discussion after Proposition 5. Remember we know (from `group_separation_rel`) we want to quotient by the closure of zero. This closure is a two-sided ideal. Indeed left multiplication by any element is continuous so the image of closure of zero is contained in the closure of the image of zero, which is zero. Same works with right multiplication of course. Now assume `x` and `x'` are equivalent, and `y` and `y'` are equivalent. Hence `x-x'` and `y-y'` are in our ideal. Write `xy = (x-x')*y + x'*(y-y')+x'y'`. The first two terms in RHS are in our ideal, so `x'*y'` is equivalent to `x*y`. I'm too tired for Lean tonight, but I'll do that if you don't do it first.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 28 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134850360):
**there's an English edition?**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Sep 28 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134850521):
translation published in 1966 by Hermann

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 28 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134850963):
I discovered this as well last week

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 28 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134851049):
https://www.springer.com/us/book/9783540642411

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 28 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134851056):
The Hermann edition is probably hard to find nowadays

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 28 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134851073):
I mistakenly bought that volume in English (I noticed when I was back at home)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 29 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134896243):
https://github.com/leanprover-community/mathlib/commit/65fe82ac32a956340ce990e3eed7b1e85772e7c0

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 29 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134896314):
@**Johannes Hölzl**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134897500):
Is this "completion of a topological ring is a topological ring"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 30 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complete_groups/near/134898348):
We have the "completion of a topological Hausdorff ring is a topological ring". This is the essential step to remove the Hausdorff.


{% endraw %}
