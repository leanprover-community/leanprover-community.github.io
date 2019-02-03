---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86798wellfoundedfix.html
---

## Stream: [general](index.html)
### Topic: [well_founded.fix](86798wellfoundedfix.html)

---


{% raw %}
#### [ Kenny Lau (Jul 28 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded.fix/near/130481709):
<div class="codehilite"><pre><span></span><span class="n">attribute</span> <span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">well_founded</span><span class="bp">.</span><span class="n">fix</span>
</pre></div>

#### [ Kenny Lau (Jul 28 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded.fix/near/130481714):
<p>can we put this somewhere in mathlib?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded.fix/near/130482868):
<p>What does it do?</p>

#### [ Kenny Lau (Jul 28 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded.fix/near/130482873):
<p>well-founded recursion</p>

#### [ Kenny Lau (Jul 28 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded.fix/near/130482875):
<p>oh, it makes sure that the motive is computed</p>

#### [ Kenny Lau (Jul 28 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded.fix/near/130482917):
<p>you need <code>elab_as_eliminator</code> in things like <code>rec_on</code></p>


{% endraw %}
