---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10826Newrecord.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [New record](https://leanprover-community.github.io/archive/113488general/10826Newrecord.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jan 05 2019 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20record/near/154473192):
<p>I think we have a new record:<br>
<a href="/user_uploads/3121/J7QL1y-Fi-LLiwjUiJbZUq5J/50_PR.png" target="_blank" title="50_PR.png">50_PR.png</a> <br>
It's a bit unfair to take advantage of Mario traveling to add five more PR...</p>
<div class="message_inline_image"><a href="/user_uploads/3121/J7QL1y-Fi-LLiwjUiJbZUq5J/50_PR.png" target="_blank" title="50_PR.png"><img src="/user_uploads/3121/J7QL1y-Fi-LLiwjUiJbZUq5J/50_PR.png"></a></div>

#### [ Patrick Massot (Jan 05 2019 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20record/near/154473468):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> an easy way to make sure Mario won't be depressed by this when landing  would be to  incorporate <a href="https://github.com/leanprover/mathlib/issues/573" target="_blank" title="https://github.com/leanprover/mathlib/issues/573">#573</a> into <a href="https://github.com/leanprover/mathlib/issues/568" target="_blank" title="https://github.com/leanprover/mathlib/issues/568">#568</a>, merge the later and close the former</p>

#### [ Chris Hughes (Jan 05 2019 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20record/near/154475852):
<p>I've been making gazillions of hopefully quite easy ones, so it's not that bad.</p>

#### [ Johannes Hölzl (Jan 05 2019 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20record/near/154476613):
<p>I'm not sure about the namespace <code>metric</code>, newly introduced namespaces are usually type oriented</p>

#### [ Mario Carneiro (Jan 05 2019 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20record/near/154477440):
<p>I agree. Although some of the theorems could benefit from a namespace, most are already disambiguated in the name by referring to <code>dist</code> or <code>metric</code></p>

#### [ Mario Carneiro (Jan 05 2019 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20record/near/154477453):
<p>and the basic algebraic theorems in groups and rings are all in the root namespace</p>

#### [ Mario Carneiro (Jan 05 2019 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20record/near/154477455):
<p>In particular, <code>metric_space</code> should <em>not</em> be in a namespace</p>

#### [ Mario Carneiro (Jan 05 2019 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20record/near/154480237):
<p>I put a counter proposal at <a href="https://github.com/leanprover/mathlib/compare/master...leanprover-community:metric_namespace" target="_blank" title="https://github.com/leanprover/mathlib/compare/master...leanprover-community:metric_namespace">https://github.com/leanprover/mathlib/compare/master...leanprover-community:metric_namespace</a> . <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> <span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span> <span class="user-mention" data-user-id="110031">@Patrick Massot</span>  Let me know what you think - I'm not planning on forcing this if people don't like it. The gist of it is: stuff about <code>dist</code> and <code>edist</code> are in the root namespace, stuff about topological characterizations in a metric space are in <code>metric</code> namespace, <code>ball</code>, <code>closed_ball</code>, <code>bounded</code> are all in the <code>metric</code> namespace. Similar for the <code>emetric</code> namespace.</p>

#### [ Mario Carneiro (Jan 05 2019 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20record/near/154480284):
<p>I tried putting stuff in the <code>metric_space</code> namespace instead, but then there are collisions with metric space axioms</p>

#### [ Mario Carneiro (Jan 05 2019 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20record/near/154480297):
<p>things like <code>cauchy_of_metric</code> are renamed to <code>metric.cauchy_iff</code></p>

#### [ Sebastien Gouezel (Jan 05 2019 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20record/near/154480731):
<p>Looks very good to me. I felt the need for a <code>metric</code> namespace when I started introducing more concepts, like isometries: it felt wrong to put them in the root namespace. Things that could have a different meaning in a different context, like bounded or balls, should also definitely go in the namespace, just like you do in your proposal. I also tried first with a <code>metric_space</code> namespace, but it created collisions as you just mentioned.</p>

#### [ Patrick Massot (Jan 05 2019 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20record/near/154481527):
<p>I think the root namespace should be really clean. But of course it's much less important in mathlib than in core's <code>init</code> since you can always choose what to import (especially after we'll split those huge files). And <code>metric_space</code> sounds uncontroversial, so Mario's version looks good to me.</p>

#### [ Patrick Massot (Jan 05 2019 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20record/near/154484507):
<p>Hoho, a big merging wave is in progress!</p>

#### [ Johan Commelin (Jan 05 2019 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20record/near/154487485):
<p>Oops, we're down to 38...</p>

#### [ Patrick Massot (Jan 05 2019 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/New%20record/near/154487497):
<p>But I still can't shuffle files because the metric namespace PR is not merged. <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> ?</p>


{% endraw %}
