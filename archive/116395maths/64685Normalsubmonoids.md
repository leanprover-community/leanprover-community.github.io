---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/64685Normalsubmonoids.html
---

## Stream: [maths](index.html)
### Topic: [Normal submonoids](64685Normalsubmonoids.html)

---

#### [Mario Carneiro (Aug 10 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131229964):
Are these a thing? The natural definition of normal subgroup extends to the monoid case as `a + b \in S -> b + a \in S`

#### [Johan Commelin (Aug 10 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131229974):
Do we need them anywhere?

#### [Mario Carneiro (Aug 10 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131229977):
not particularly

#### [Mario Carneiro (Aug 10 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230045):
Do we need normal subgroups?

#### [Mario Carneiro (Aug 10 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230056):
I guess the answer is about the same

#### [Johan Commelin (Aug 10 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230120):
Well... I think the will be used quite a lot.

#### [Johan Commelin (Aug 10 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230124):
Isn't Kevin already using them?

#### [Mario Carneiro (Aug 10 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230139):
I'm working on porting the add_subgroup stuff now... I don't really get why we care about noncommutative additive groups

#### [Johan Commelin (Aug 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230230):
We don't care about those.

#### [Johan Commelin (Aug 10 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230284):
We just want the additive subgroups, so that we can have subrings.

#### [Kenny Lau (Aug 10 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230305):
subrings not

#### [Johan Commelin (Aug 10 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131230317):
And this seemed like a very straightforward translation exercise, which I performed without thinking about whether some lines could be removed...

#### [Kevin Buzzard (Aug 10 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131234329):
Normal subgroups are used all over the place in maths, they're exactly the kernels of morphisms in the category of groups. I thought a bit recently about why we would care about noncommutative additive groups, and the only half-decent answer I could come up with is that there is at least one example in maths where people use addition as a standard notation and it's not commutative, namely addition of ordinals (not that anyone outside of logic ever uses ordinals anyway). These do not form a group though. In number theory there is an implicit assumption that addition is commutative.

I am only using normal subgroups in the additive case and only in the situation where addition is commutative, so they're the same as subgroups. My only use case was that I need some lemmas about quotient rings, and I thought that the "correct" way to prove that a map R -> S whose kernel contains I induced a map R/I -> S would be to first construct the map using some universal property of quotient abelian groups and then to show it's a ring homomorphism. But I don't know whether I'm fussing over nothing and should just prove it directly. 

Didn't Chris make a quotient group PR recently? I was going to make one and then Chris told me he'd made one so I shouldn't PR because of potential conflicts.

https://github.com/leanprover/mathlib/pull/212

#### [Mario Carneiro (Aug 10 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131234411):
oops

#### [Andreas Swerdlow (Aug 10 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131842627):
I did some basic subring and subfield stuff here https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/inner_product_spaces/subrings_subfields.lean. Is this useful at all, or should it be linked to existing stuff in mathlib?

#### [Reid Barton (Aug 11 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131849326):
```quote
Normal subgroups are used all over the place in maths, they're exactly the kernels of morphisms in the category of groups.
```
And groups are special because the equivalence relation induced by a surjection ($$x \sim y$$ if $$f(x) = f(y)$$) is determined by the equivalence class of 0, i.e., the kernel. For general monoids, knowing the kernel of a map doesn't tell you about the behavior of the map away from 0 (consider the quotient of `nat` which identifies all the numbers greater than or equal to 3).
So, I don't think normal submonoids are of much interest.

#### [Scott Morrison (Aug 11 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131852250):
@**Andreas Swerdlow**, looks useful to me. How about you PR it?

#### [Scott Morrison (Aug 11 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131852257):
It might be worth doing a little renaming to get the functions as close as possible to following the pattern in `mathlib/group_theory/subgroup.lean`.

#### [Scott Morrison (Aug 11 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131852369):
I'm not entirely certainly where to put what you've written. My suggestion would be to be ambitious, and split it into two parts, putting them in `ring_theory/subring.lean` and `field_theory/subfield.lean`, parallel to the group situation: eventually we're going to need a fair bit of other stuff in both those directories. (Although `field_theory` sounds very wrong...)

#### [Scott Morrison (Aug 11 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131852441):
Probably it's best to create a new branch at <https://github.com/leanprover-community/mathlib>, so others can look at it first (announce here you want help?) and then once it's been tweaked a bit we can PR it to the official mathlib.

#### [Scott Morrison (Aug 11 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131852498):
(If you don't have commit access at leanprover-community, either ask here for it, or just do the work in your own fork of mathlib and send a PR to leanprover-community, and announce here and somewhere will merge it to a branch.)

#### [Johan Commelin (Aug 11 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/131937828):
```quote
I did some basic subring and subfield stuff here https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/inner_product_spaces/subrings_subfields.lean. Is this useful at all, or should it be linked to existing stuff in mathlib?
```
Hi @**Andreas Swerdlow** Additive subgroups have just been put into mathlib: https://github.com/leanprover/mathlib/blob/0f42b279865753eb3c79f3504783c7dbd81dfc7e/group_theory/subgroup.lean#L25. I think that it is useful if Lean knows that every subring is also an additive subgroup. Some time ago I wrote https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/subring.lean#L13, but there is nothing about fields in that file. I think a merge of your and my approach would be best.

#### [Andreas Swerdlow (Aug 13 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Normal%20submonoids/near/132038273):
@**Scott Morrison** @**Johan Commelin**  thanks for the help. I've rewritten the subfield part, so that it builds off of what Johan wrote for subrings, and created a fork of leanprover-community/mathlib with both Johan's subring file in ring_theory/subring.lean and the subfield stuff in field_theory/subfield.lean. The fork is here: https://github.com/amswerdlow/mathlib. Any suggestions are welcome before I PR

