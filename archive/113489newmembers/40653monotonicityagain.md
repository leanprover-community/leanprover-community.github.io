---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/40653monotonicityagain.html
---

## [new members](index.html)
### [monotonicity again](40653monotonicityagain.html)

#### [Simon Hudon (Aug 04 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/monotonicity again/near/130874956):
I just gave another shot to implementing `mono` and `ac_mono` (for reasoning with monotonicity with and without considerations for associativity / commutativity). For those who would like to use those, I'd love to hear if it's useful as it is. I have written a lot of examples, I hope it will be informative.

https://github.com/cipher1024/mathlib/blob/monotonicity/tests/monotonicity.lean
https://github.com/cipher1024/mathlib/tree/monotonicity/docs

#### [Johan Commelin (Aug 04 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/monotonicity again/near/130876196):
This seems quite useful! I wonder if it would help with proving some of my stuff on simplicial sets: https://github.com/jcommelin/mathlib/blob/ece70f307edc5fdebe7aed154ab8aaa3a12bb5a3/algebraic_topology/simplex_category.lean#L33 or https://github.com/jcommelin/mathlib/blob/ece70f307edc5fdebe7aed154ab8aaa3a12bb5a3/algebraic_topology/simplex_category.lean#L67

#### [Johan Commelin (Aug 04 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/monotonicity again/near/130876208):
(Also, wrong stream? Or do you propose `mono` and `ac_mono` as "new members" of the community?)

#### [Simon Hudon (Aug 04 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/monotonicity again/near/130876506):
*cough cough* of course they would be! They're just such awesome tactics :D

#### [Simon Hudon (Aug 04 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/monotonicity again/near/130876631):
I'm not sure how they would help for those proofs though. I'm really targeting goals of the shape `x + y ≤ w + z` for some relation `≤`.

#### [Johan Commelin (Aug 04 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/monotonicity again/near/130877226):
Ok, I see. Well, maybe at some point `cooper` will turn my proofs into a 1-liner.

#### [Simon Hudon (Aug 04 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/monotonicity again/near/130877412):
Isn't `cooper` mostly about integer arithmetic?

#### [Johan Commelin (Aug 04 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/monotonicity again/near/130877614):
It is, but I think so are my proofs.

#### [Simon Hudon (Aug 04 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/monotonicity again/near/130877706):
Ok, I squinted at them and started to see integers. I wonder if `fin` will make it harder. Does Presburger arithmetic include modulo?

#### [Mario Carneiro (Aug 04 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/monotonicity again/near/130877768):
modulo by constants yes

#### [Johan Commelin (Aug 04 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/monotonicity again/near/130887896):
There is no modular arithmetic in my code. `fin` should just unpack to some inequalities, and `cooper` should be able to deal with those...

