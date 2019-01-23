---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78443implicitconvcongr.html
---

## Stream: [general](index.html)
### Topic: [implicit conv congr](78443implicitconvcongr.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 06 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20conv%20congr/near/135318034):
In conv mode, is there a version of `congr`/`skip` which allow traverse implicit arguments?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 07 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20conv%20congr/near/135366301):
@**Mario Carneiro** did you see this question?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20conv%20congr/near/135372046):
I don't think `congr` decides things based on whether they are implicit, but rather whether they are dependent on other arguments

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 08 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20conv%20congr/near/135389727):
I made a few tests, and it seems you're right. So my new question is: how to you conv or rw dependent arguments? I guess this is the same issue I have when I want to use assumptions stating that two uniform structures are the same


{% endraw %}
