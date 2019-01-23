---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53477cancelisos.html
---

## Stream: [general](index.html)
### Topic: [cancel isos](53477cancelisos.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 23 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132617646):
@**Scott Morrison** Somehow, `cancel_epi` with `f = ↑i` (`i : x ≅ y`) doesn't work any more.
I managed to track this down far enough to find that adding the line (which used to be in `tidy.tidy`)
```lean
attribute [reducible] lift_t coe_t coe_b
```
makes it work again. But I don't really understand what is going on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 23 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132620408):
@**Reid Barton**, thanks for all these requests. I am giving a demo in a few hours of parts of `obviously` and my category theory library, and right after that I will address these three issues!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 23 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132620460):
The last one is a bit interesting: I'm now very careful to have my automation _not_ unfold too much, and `cancel_epi` is having trouble seeing through a coercion that formerly someone else was unfolding.  I'll have to find another solution. If you have a MWE showing the cancel_epi issue that would be great.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 23 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132645544):
Yes, I think the situation with `cancel_epi` makes sense to me now. Probably the right thing to do is just to add a second instance which matches `↑i` (in addition to the existing instance which matches `i.hom`).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 25 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132751886):
Okay, this issue should be fixed in https://github.com/leanprover/mathlib/pull/278/commits/ccb1adf8a0fba114c5cbcad0169212d4775517d7, which is part of https://github.com/leanprover/mathlib/pull/278.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 25 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132751892):
I'm happy to see you are enjoying your Paris sightseeing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 25 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132751968):
:-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 25 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132751971):
I went out and ate lots of pastries and cheese this morning. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 25 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132752029):
Also I can see the Notre Dame from where I'm sitting.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 25 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cancel%20isos/near/132753363):
Cheese, Notre-Dame and Lean seems to be a good combination

