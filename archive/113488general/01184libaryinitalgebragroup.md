---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01184libaryinitalgebragroup.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [libary/init/algebra/group](https://leanprover-community.github.io/archive/113488general/01184libaryinitalgebragroup.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 22 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509188):
<p>L165:</p>
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm"> αdditive &quot;sister&quot; structures.</span>
</pre></div>


<p>alpha-dditive??</p>

#### [ Kenny Lau (Apr 22 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509229):
<p>is that an easter egg</p>

#### [ Mario Carneiro (Apr 22 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509785):
<p>I tried to PR that almost a year ago and of course it was rejected</p>

#### [ Kenny Lau (Apr 22 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509787):
<p>lol</p>

#### [ Kenny Lau (Apr 22 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509788):
<p>what was the reason</p>

#### [ Mario Carneiro (Apr 22 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509835):
<p>Leo doesn't want to hear about tiny changes</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509877):
<p>that one must be hard to review or something</p>

#### [ Patrick Massot (Apr 22 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509879):
<p>That one was provocation</p>

#### [ Mario Carneiro (Apr 22 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509880):
<p>It's not an easter egg, it's a bad find-replace job when we moved from using <code>A B C</code> to <code>α β γ</code> for types</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509881):
<p>it's a pretty spectacular bad find-replace job!</p>

#### [ Patrick Massot (Apr 22 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509887):
<p>We'll need to be much more careful when we'll to the <code>s/α/G/g</code> in all group theory files</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509888):
<p>Did they change every A to an alpha and then change 100 alpha's back to A's?</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509927):
<p>put it in the pile for the one time patch</p>

#### [ Mario Carneiro (Apr 22 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509930):
<p>an easter egg would be replacing <code>A</code> with a capital alpha</p>

#### [ Patrick Massot (Apr 22 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509980):
<p><code>variables (Α : Type) (A : Type)</code></p>

#### [ Patrick Massot (Apr 22 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509981):
<p>Yeah!</p>

#### [ Patrick Massot (Apr 22 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509983):
<p>Lean doesn't complain</p>

#### [ Mario Carneiro (Apr 22 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509984):
<p>no, that's shadowing</p>

#### [ Mario Carneiro (Apr 22 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509986):
<p>but universe shadowing is disallowed for some reason...</p>

#### [ Patrick Massot (Apr 22 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509991):
<p>No, I the first one wasn't a capital alpha Lean would complain</p>

#### [ Mario Carneiro (Apr 22 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125510030):
<p>I stand corrected</p>

#### [ Patrick Massot (Apr 22 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125510031):
<p>Anyway, I should be sleeping</p>

#### [ Patrick Massot (Apr 22 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125510041):
<p>See you!</p>

#### [ Kenny Lau (Apr 22 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125510125):
<p>I just woke up</p>


{% endraw %}
