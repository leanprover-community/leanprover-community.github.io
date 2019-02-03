---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/33072consoverload.html
---

## Stream: [general](index.html)
### Topic: [cons overload](33072consoverload.html)

---


{% raw %}
#### [ Kenny Lau (Apr 18 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cons%20overload/near/125243066):
<p>kinda annoyed by the fact that <code>list.cons</code> and <code>multiset.cons</code> both use <code>::</code></p>

#### [ Kevin Buzzard (Apr 18 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cons%20overload/near/125243144):
<p>Yes, that's the other instance of overloading other than <code>^</code></p>

#### [ Kevin Buzzard (Apr 18 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cons%20overload/near/125243150):
<p>Mario has commented on this in the past. It's a great example of something which Mario would love to change but which Leo is not interested in changing.</p>

#### [ Kenny Lau (Apr 18 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cons%20overload/near/125243189):
<p>I see</p>

#### [ Kevin Buzzard (Apr 18 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cons%20overload/near/125243191):
<p>In the past the philosophy was always "wait".</p>

#### [ Kevin Buzzard (Apr 18 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cons%20overload/near/125243206):
<p>Now we have Lean 3.4 we can again raise the possibility of a fork plus a one-time patch, to give Lean 3.400001 "modded by Mario"</p>

#### [ Kevin Buzzard (Apr 18 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cons%20overload/near/125243213):
<p>Leo again made it clear that he would have no objection to a fork.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cons%20overload/near/125243219):
<p>My instinct is to wait a while and to see how many commits to Lean 3.4 actually do occur in the next month or so</p>

#### [ Kevin Buzzard (Apr 18 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cons%20overload/near/125243258):
<p>If things really are going to slow down then this is really exciting</p>

#### [ Kevin Buzzard (Apr 18 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cons%20overload/near/125243272):
<p>because it means that Mario will not have to take time out about once a week and spend time (and possibly a highly non-trivial amount of time) fixing up mathlib because of changes in core.</p>

#### [ Kevin Buzzard (Apr 18 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cons%20overload/near/125243289):
<p>You saw yourself how frustrated I got when the changes to <code>^</code> broke our stacks project code and stopped me working on the project for several days because I was not capable of fixing the code that you and Chris had written and you two had other things on your mind (completely understandably).</p>

#### [ Kevin Buzzard (Apr 18 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cons%20overload/near/125243293):
<p>Why not open an issue in mathlib?</p>

#### [ Kevin Buzzard (Apr 18 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cons%20overload/near/125243340):
<p>If Lean 4 is not going to be compatible with Lean 3 then this is an argument for not fussing too much about simple changes such as this.</p>


{% endraw %}
