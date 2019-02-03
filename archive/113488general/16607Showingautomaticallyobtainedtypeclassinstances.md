---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16607Showingautomaticallyobtainedtypeclassinstances.html
---

## Stream: [general](index.html)
### Topic: [Showing automatically obtained typeclass instances](16607Showingautomaticallyobtainedtypeclassinstances.html)

---


{% raw %}
#### [ Seul Baek (May 29 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127225600):
<p>Is it possible to show which instance Lean is using when it successfully performs a typeclass inference? </p>
<p>For instance, I know from the fact that I can use <code>neg_le_neg</code> with integers that Lean has silently performed a typeclass inference and found an instance of type <code>ordered_comm_group int</code>. But I don't know exactly <em>which</em> instance Lean has found. Is there a way to display this information, similar to how I can jump to definitions using f12?</p>

#### [ Kenny Lau (May 29 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127225655):
<p>you can print the proof of your theorem</p>

#### [ Kenny Lau (May 29 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127225656):
<p>using <code>#print</code></p>

#### [ Kenny Lau (May 29 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127225695):
<p>and you can <code>set pp.implicit true</code> (there may be a better option) to see the implicit arguments, including the proof of the typeclass inference</p>

#### [ Scott Morrison (May 29 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127225696):
<p><code>set_option trace.class_instances true</code></p>

#### [ Kenny Lau (May 29 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127225699):
<p>well that displays too much information</p>

#### [ Seul Baek (May 29 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127225853):
<p>Thanks!</p>

#### [ Mario Carneiro (May 29 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127228102):
<p>you can also test instance problems with</p>
<div class="codehilite"><pre><span></span>theorem T : ordered_comm_group int := by apply_instance
#print T
</pre></div>

#### [ Kenny Lau (May 29 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127228104):
<p><code>#check (by apply_instance : ordered_comm_group int)</code></p>

#### [ Kenny Lau (May 29 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127228105):
<p>do I win?</p>

#### [ Mario Carneiro (May 29 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127228146):
<p>clever</p>


{% endraw %}
