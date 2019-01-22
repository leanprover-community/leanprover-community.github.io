---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/49659Fixedpoint.html
---

## [new members](index.html)
### [Fixed point](49659Fixedpoint.html)

#### [Alistair Tucker (Nov 21 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148111493):
I'd like to define a function E from ℝ^n to ℝ^n as the fixed point of a contraction mapping (or equivalently I think as the solution to a variational inequality). Is this easy to do? What files should I be looking at?

#### [Kevin Buzzard (Nov 21 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112396):
One of my students proved the contraction mapping theorem for metric spaces... @**Luca Gerolla** did you ever PR this?

#### [Patrick Massot (Nov 21 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112403):
It's currently not easy. There is a pending PR on contraction mapping, but I don't remember what is proved there exactly

#### [Patrick Massot (Nov 21 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112412):
https://github.com/leanprover/mathlib/pull/428

#### [Alistair Tucker (Nov 21 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112567):
Thanks! I'll have a look at that but if it's not easy I might just declare it as a constant :)

#### [Patrick Massot (Nov 21 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112635):
That PR needs to be reworked to use https://github.com/leanprover/mathlib/commit/4a013fb04d6e504be8582ad610016d8dcce3e5f3

#### [Patrick Massot (Nov 21 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112646):
and probably extract more lemmas out of the big proofs

#### [Patrick Massot (Nov 21 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112661):
compare https://github.com/leanprover/mathlib/pull/428/files#diff-6f3fee1c28d757f0199c3512ffc8e5e9R83 and https://github.com/leanprover/mathlib/commit/4a013fb04d6e504be8582ad610016d8dcce3e5f3#diff-5edb379056f11c116887dcff6e8bed0dR366 for instance

#### [Alistair Tucker (Nov 21 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112740):
If I think I can help with that I will but I suspect it'll be beyond me.

#### [Sebastien Gouezel (Nov 21 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112771):
Yes, I think everything in the file `analysis/topology/metric_sequences.lean` of the PR is now already in the library. But the result on the Banach contraction is not.

#### [Patrick Massot (Nov 21 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112823):
Alistair, updating that PR in order to replace stuff that came to mathlib in the meantime should be a nice exercise

#### [Patrick Massot (Nov 21 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112887):
Refactoring the big proof is much more difficult

#### [Kevin Buzzard (Nov 21 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148126734):
Luca reminds me that it was in fact @**Rohan Mitta** who was doing the contraction mapping theorem.

