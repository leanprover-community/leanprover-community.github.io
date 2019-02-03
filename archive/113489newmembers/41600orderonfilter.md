---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/41600orderonfilter.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [order on filter](https://leanprover-community.github.io/archive/113489newmembers/41600orderonfilter.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Oct 09 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order%20on%20filter/near/135489142):
<p>Why is the order on filter reverse inclusion instead of just inclusion?</p>

#### [ Mario Carneiro (Oct 09 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order%20on%20filter/near/135489824):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> will know. I +1 this question, it throws me off every time</p>

#### [ Kevin Buzzard (Oct 09 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order%20on%20filter/near/135490958):
<p>I just assumed it was because the set of subsets of X embeds into the set of filters on X via principal filters, and the smaller the subset the bigger the filter.</p>

#### [ Kenny Lau (Oct 09 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order%20on%20filter/near/135491024):
<p>interesting</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order%20on%20filter/near/135491228):
<p>Here is one way to look at it: the identity function is continuous on topologies when the topologies are <code>dom &lt;= cod</code>. In other words, the poset of topologies is embedded in the category of topological spaces by the functor <code>T -&gt; (X,T)</code></p>

#### [ Mario Carneiro (Oct 09 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order%20on%20filter/near/135491311):
<p>If you try to do the same thing with filters, the replacement for "continuous" is <code>tendsto</code>, and in order to keep the <code>&lt;=</code> relation going the same way we have to reverse the order of filters</p>

#### [ Mario Carneiro (Oct 09 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order%20on%20filter/near/135491420):
<p>That is, <code>tendsto id L1 L2</code> iff <code>L2 ⊆ L1</code></p>


{% endraw %}
