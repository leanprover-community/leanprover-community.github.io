---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78443implicitconvcongr.html
---

## Stream: [general](index.html)
### Topic: [implicit conv congr](78443implicitconvcongr.html)

---


{% raw %}
#### [ Patrick Massot (Oct 06 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20conv%20congr/near/135318034):
<p>In conv mode, is there a version of <code>congr</code>/<code>skip</code> which allow traverse implicit arguments?</p>

#### [ Patrick Massot (Oct 07 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20conv%20congr/near/135366301):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> did you see this question?</p>

#### [ Mario Carneiro (Oct 08 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20conv%20congr/near/135372046):
<p>I don't think <code>congr</code> decides things based on whether they are implicit, but rather whether they are dependent on other arguments</p>

#### [ Patrick Massot (Oct 08 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20conv%20congr/near/135389727):
<p>I made a few tests, and it seems you're right. So my new question is: how to you conv or rw dependent arguments? I guess this is the same issue I have when I want to use assumptions stating that two uniform structures are the same</p>


{% endraw %}
