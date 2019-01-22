---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10826Newrecord.html
---

## [general](index.html)
### [New record](10826Newrecord.html)

#### [Patrick Massot (Jan 05 2019 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New record/near/154473192):
I think we have a new record:
[50_PR.png](/user_uploads/3121/J7QL1y-Fi-LLiwjUiJbZUq5J/50_PR.png) 
It's a bit unfair to take advantage of Mario traveling to add five more PR...

#### [Patrick Massot (Jan 05 2019 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New record/near/154473468):
@**Johannes Hölzl** an easy way to make sure Mario won't be depressed by this when landing  would be to  incorporate #573 into #568, merge the later and close the former

#### [Chris Hughes (Jan 05 2019 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New record/near/154475852):
I've been making gazillions of hopefully quite easy ones, so it's not that bad.

#### [Johannes Hölzl (Jan 05 2019 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New record/near/154476613):
I'm not sure about the namespace `metric`, newly introduced namespaces are usually type oriented

#### [Mario Carneiro (Jan 05 2019 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New record/near/154477440):
I agree. Although some of the theorems could benefit from a namespace, most are already disambiguated in the name by referring to `dist` or `metric`

#### [Mario Carneiro (Jan 05 2019 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New record/near/154477453):
and the basic algebraic theorems in groups and rings are all in the root namespace

#### [Mario Carneiro (Jan 05 2019 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New record/near/154477455):
In particular, `metric_space` should *not* be in a namespace

#### [Mario Carneiro (Jan 05 2019 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New record/near/154480237):
I put a counter proposal at https://github.com/leanprover/mathlib/compare/master...leanprover-community:metric_namespace . @**Johannes Hölzl** @**Sebastien Gouezel** @**Patrick Massot**  Let me know what you think - I'm not planning on forcing this if people don't like it. The gist of it is: stuff about `dist` and `edist` are in the root namespace, stuff about topological characterizations in a metric space are in `metric` namespace, `ball`, `closed_ball`, `bounded` are all in the `metric` namespace. Similar for the `emetric` namespace.

#### [Mario Carneiro (Jan 05 2019 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New record/near/154480284):
I tried putting stuff in the `metric_space` namespace instead, but then there are collisions with metric space axioms

#### [Mario Carneiro (Jan 05 2019 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New record/near/154480297):
things like `cauchy_of_metric` are renamed to `metric.cauchy_iff`

#### [Sebastien Gouezel (Jan 05 2019 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New record/near/154480731):
Looks very good to me. I felt the need for a `metric` namespace when I started introducing more concepts, like isometries: it felt wrong to put them in the root namespace. Things that could have a different meaning in a different context, like bounded or balls, should also definitely go in the namespace, just like you do in your proposal. I also tried first with a `metric_space` namespace, but it created collisions as you just mentioned.

#### [Patrick Massot (Jan 05 2019 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New record/near/154481527):
I think the root namespace should be really clean. But of course it's much less important in mathlib than in core's `init` since you can always choose what to import (especially after we'll split those huge files). And `metric_space` sounds uncontroversial, so Mario's version looks good to me.

#### [Patrick Massot (Jan 05 2019 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New record/near/154484507):
Hoho, a big merging wave is in progress!

#### [Johan Commelin (Jan 05 2019 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New record/near/154487485):
Oops, we're down to 38...

#### [Patrick Massot (Jan 05 2019 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New record/near/154487497):
But I still can't shuffle files because the metric namespace PR is not merged. @**Johannes Hölzl** ?

