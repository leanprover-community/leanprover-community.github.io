---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98018mathlib.html
---

## Stream: [general](index.html)
### Topic: [mathlib](98018mathlib.html)

---


{% raw %}
#### [ Scott Morrison (Apr 10 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871039):
<p>Is it strange that we have <code>monoid.pow</code> and <code>gpow</code> (for groups)? Can we make these more uniform?</p>

#### [ Mario Carneiro (Apr 10 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871398):
<p>you mean the names? Do you have a better idea?</p>

#### [ Scott Morrison (Apr 10 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871470):
<p><code>group.pow</code>?</p>

#### [ Mario Carneiro (Apr 10 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871581):
<p>eh, I think the reason I didn't do that to begin with is because that puts all the group.pow theorems in the <code>group</code> namespace, which makes stuff longer since it's usually not open.</p>

#### [ Scott Morrison (Apr 10 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871623):
<p>I would generally vote for longer over obscure, but I don't have a sense of how bad this would be here.</p>

#### [ Kevin Buzzard (Apr 10 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871671):
<p>So why isn't this an argument for <code>mpow</code>, thus not putting all the <code>monoid.pow</code> theorems in the <code>monoid</code> namespace, which is also usually not oen?</p>

#### [ Kenny Lau (Apr 10 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871681):
<blockquote>
<p>So why isn't this an argument for <code>mpow</code>, thus not putting all the <code>monoid.pow</code> theorems in the <code>monoid</code> namespace, which is also usually not open?</p>
</blockquote>
<p>you win</p>

#### [ Mario Carneiro (Apr 10 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871716):
<p>you will notice that I only use the <code>monoid</code> namespace when I need to in theorems, as disambiguation</p>

#### [ Mario Carneiro (Apr 10 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871722):
<p>but I didn't say the current way is at all consistent, nor am I averse to changing it</p>

#### [ Kevin Buzzard (Apr 10 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124874371):
<p>I am not suggesting it be changed, I was just being a pedant.</p>


{% endraw %}
