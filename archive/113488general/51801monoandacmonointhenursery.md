---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51801monoandacmonointhenursery.html
---

## [general](index.html)
### [mono and ac_mono in the nursery](51801monoandacmonointhenursery.html)

#### [Simon Hudon (Aug 22 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132589831):
My `mono` and `ac_mono` are, I believe, ready for use. I have put them in the nursery https://github.com/leanprover-community/mathlib-nursery so that people can try them out as I get them merged into mathlib.

#### [Patrick Massot (Aug 22 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132597919):
Why is there so much meta and lemmas in the test file? Is it meant to be part of mathlib?

#### [Simon Hudon (Aug 22 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598001):
It is. It's meant to test individual parts of the tactics. Maybe I should split it into `test` and `example`

#### [Patrick Massot (Aug 22 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598015):
I see

#### [Patrick Massot (Aug 22 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598091):
I always find it hard to read your examples or tests which actually don't prove anything, either because the announced statement is `true` or because it ends with `admit`

#### [Patrick Massot (Aug 22 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598207):
Where is monotonicity when the target is an equality as in https://github.com/leanprover-community/mathlib-nursery/blob/master/test/tactic/monotonicity.lean#L326?

#### [Simon Hudon (Aug 22 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598248):
In that case, monotonicity is a generalization of `congr`

#### [Patrick Massot (Aug 22 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598313):
Maybe you could explain that in the documentation (and add a couple of example there too)

#### [Patrick Massot (Aug 22 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598325):
It looks very useful

#### [Simon Hudon (Aug 22 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598383):
I see what you mean with `true`. I state those theorems using `suffices : x * y < w * z, trivial,` just so that I don't have to complete all the proofs. I could use assumptions instead of `guard_target` maybe , that would be clearer

#### [Simon Hudon (Aug 22 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598410):
Thanks for the advice, I'll try to select the ones that illustrate best the obvious use cases

#### [Simon Hudon (Aug 22 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598587):
```quote
It looks very useful
```
I'm hoping it will be. Please report any trouble you run across, I feel like I must have overlooked lots of cases and lots of lemmas.

#### [Patrick Massot (Aug 22 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598785):
Unfortunately  I don't think any of my current projects will need this, but certainly I will need it at some point.

