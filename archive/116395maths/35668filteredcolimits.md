---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/35668filteredcolimits.html
---

## Stream: [maths](index.html)
### Topic: [filtered colimits](35668filteredcolimits.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 21 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filtered%20colimits/near/152355333):
Has anyone been working with filtered colimits? Perhaps @**Ramon Fernandez Mir** @**Kevin Buzzard**?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 21 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filtered%20colimits/near/152355438):
In particular, I need the formula for a filtered colimit of sets shown at https://stacks.math.columbia.edu/tag/04AX before Lemma 4.19.2 and perhaps someone has already done this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 21 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filtered%20colimits/near/152361288):
We (and @**Kenny Lau** ) recently did arbitrary colimits via some tensor product construction. I think Kenny took filtered colimits of commutative rings at some point because even though I tried my hardest to avoid it, I think I ultimately needed them when defining the structure sheaf on Spec(A) (the issue is extending the sheaf from basic opens to an arbitrary open).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 21 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filtered%20colimits/near/152361924):
https://github.com/leanprover/mathlib/pull/118

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 21 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filtered%20colimits/near/152362009):
Minor discussion on 17th May about directed systems around line 25. Note that this PR got closed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 21 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filtered%20colimits/near/152362014):
Kenny -- will this PR be resurrected one day? I need it for schemes.

