---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/64252Splittingtopology.html
---

## Stream: [maths](index.html)
### Topic: [Splitting topology](64252Splittingtopology.html)

---


{% raw %}
#### [ Patrick Massot (Jan 22 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156605219):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> <span class="user-mention" data-user-id="110032">@Reid Barton</span> I continued moving on the topology reorganization project. The next step was to split <code>topology.basic</code> and <code>topology.continuity</code> while gathering the basics of continuity and the basics of topological spaces. My current result is at <a href="https://github.com/leanprover-community/mathlib/tree/top_split" target="_blank" title="https://github.com/leanprover-community/mathlib/tree/top_split">https://github.com/leanprover-community/mathlib/tree/top_split</a> I need comments before moving on. My next step would be to reorganize uniform spaces and topological structures, still following the general scheme discussed in Amsterdam</p>

#### [ Patrick Massot (Jan 22 2019 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156605761):
<p>Recall that one goal was to have files with less than 1000 lines, and lighters dependencies for stuff needing only the basics of topological spaces and continuous functions. The current lines counts are</p>
<div class="codehilite"><pre><span></span>  1927 basic.lean
   460 bounded_continuous_function.lean
   118 compact_open.lean
  1568 continuity.lean
   271 stone_cech.lean
</pre></div>


<p>my proposal has:</p>
<div class="codehilite"><pre><span></span>   206 bases.lean
   591 basic.lean
   460 bounded_continuous_function.lean
   118 compact_open.lean
   957 constructions.lean
   359 maps.lean
   132 opens.lean
   573 order.lean
   280 separation.lean
   272 stone_cech.lean
   468 subset_properties.lean
</pre></div>


<p>you can still see I got tired with <code>constructions.lean</code> (which has products, sum, quotients, pi...). That one could probably be split more</p>

#### [ Patrick Massot (Jan 22 2019 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156606107):
<p>Damn, I  forgot to move homeomorphisms from constructions to map</p>

#### [ Patrick Massot (Jan 22 2019 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156606162):
<p>That will improve the balance for about 100 lines</p>

#### [ Johannes Hölzl (Jan 22 2019 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156606359):
<p>Hm the homeomorphisms should be in <code>basic</code>. And I should mention that I don't like to goal of keeping the files less than 1000 lines. This is quiet arbitrary and doesn't tell anybody where to find a specific definition/proof</p>

#### [ Johannes Hölzl (Jan 22 2019 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156606384):
<p>But looking through the changeset it looks very sensible</p>

#### [ Patrick Massot (Jan 22 2019 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156607124):
<p>We know you don't like reducing line counts. This was very clear from reading the topology part of mathlib, and also from the Amsterdam discussion. But I think this is still a nice goal, especially when we find out there are sensible cutting points. And of course the 1000 number is totally arbitrary, although there is a certain psychological impact above that threshold.</p>

#### [ Patrick Massot (Jan 22 2019 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156644076):
<p>So, should I open a PR?</p>

#### [ Johannes Hölzl (Jan 22 2019 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156645505):
<p>Yes, I think this is a good PR</p>

#### [ Reid Barton (Jan 23 2019 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156691525):
<p>I made this little ASCII art diagram of the proposed import structure (hopefully I caught everything):</p>
<div class="codehilite"><pre><span></span>basic-------------------
|                      |
order---------         subset_properties
|            |         |
separation   bases     |
|            |  |      |
maps         |  opens  |
|            |         |
constructions-----------
</pre></div>

#### [ Patrick Massot (Jan 23 2019 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156701508):
<p>This is probably correct. The fact that <code>constructions</code> uses (almost) everything else is probably proving that it was not split enough. There are other files in this directory that import <code>constructions</code></p>

#### [ Patrick Massot (Jan 23 2019 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting%20topology/near/156701576):
<p>Reid, do you want to work some more on this effort?</p>


{% endraw %}
