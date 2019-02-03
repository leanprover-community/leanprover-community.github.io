---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09015detectingsorry.html
---

## Stream: [general](index.html)
### Topic: [detecting sorry](09015detectingsorry.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 02 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177763):
<p>I am assuming that the following should be easy, or at least possible.</p>

#### [ Kevin Buzzard (Mar 02 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177765):
<p>I have a "definition" of an affine scheme in Lean</p>

#### [ Kevin Buzzard (Mar 02 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177766):
<p>but it's not yet complete because it relies on a definition</p>

#### [ Kevin Buzzard (Mar 02 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177768):
<p>which uses another definition</p>

#### [ Kevin Buzzard (Mar 02 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177810):
<p>which uses another definition</p>

#### [ Kevin Buzzard (Mar 02 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177811):
<p>which uses sorry</p>

#### [ Patrick Massot (Mar 02 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177812):
<p><code>leanpkg build</code> will tell you about this</p>

#### [ Kevin Buzzard (Mar 02 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177814):
<p>I was expecting to be able to spot this in VS Code (or emacs)</p>

#### [ Kevin Buzzard (Mar 02 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177821):
<p>but <code>#print affine_scheme</code> and <code>#check affine_scheme</code> don't seem to mention this</p>

#### [ Gabriel Ebner (Mar 02 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177962):
<p><code>#print axioms affine_scheme</code> should do the trick</p>

#### [ Kevin Buzzard (Mar 02 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177968):
<p>Aah yes, thanks</p>

#### [ Kevin Buzzard (Mar 02 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177969):
<p>I knew there was a way.</p>

#### [ Kevin Buzzard (Mar 02 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177972):
<p>I used the powerful <code>sorry</code> axiom.</p>

#### [ Kevin Buzzard (Mar 02 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123178001):
<p>I wonder why they didn't make this part of ZFC.</p>

#### [ Kevin Buzzard (Mar 02 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123178022):
<p>&lt;close topic&gt;</p>

#### [ Gabriel Ebner (Mar 02 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123178029):
<p>IIRC it's a very well known large cardinal axiom.</p>

#### [ Kevin Buzzard (Mar 05 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123321180):
<p>Oh wait there's still something I don't understand</p>

#### [ Kevin Buzzard (Mar 05 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123321186):
<div class="codehilite"><pre><span></span>definition foo : ℕ → ℕ := sorry

structure bar :=
(baz : ℕ → ℕ)
(H : baz = foo)

#print axioms bar
</pre></div>

#### [ Kevin Buzzard (Mar 05 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123321193):
<p>Claims no axioms</p>

#### [ Kevin Buzzard (Mar 05 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123321247):
<p>What I am hoping to find is either a method for detecting when my definition is finished</p>

#### [ Kevin Buzzard (Mar 05 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123321248):
<p>or a proof that this can't be done</p>

#### [ Kevin Buzzard (Mar 05 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123321253):
<p>but in my mind bar is not yet finished because it relies on unfinished foo</p>

#### [ Mario Carneiro (Mar 06 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123330439):
<div class="codehilite"><pre><span></span>#print axioms bar.mk
</pre></div>


<p>seems to work</p>


{% endraw %}
