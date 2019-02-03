---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08589resetI.html
---

## Stream: [general](index.html)
### Topic: [resetI](08589resetI.html)

---


{% raw %}
#### [ Simon Hudon (Apr 11 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resetI/near/124910648):
<p>Is there any reason <code>resetI</code> wouldn't work in the latest nightly? I have a very short proof with <code>intro ; resetI</code> in it and I get:</p>
<div class="codehilite"><pre><span></span>excessive memory consumption detected at &#39;vm&#39; (potential solution: increase memory consumption threshold)
</pre></div>

#### [ Simon Hudon (Apr 11 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resetI/near/124911049):
<p>Ok, I found the problem. I had a local definition of <code>resetI</code> that just called <code>mathlib</code>'s <code>resetI</code> but it wasn't fully qualified so it just worked as a recursive function ...</p>

#### [ Mario Carneiro (Apr 11 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resetI/near/124911339):
<p>oh thank god... fixing <code>resetI</code> was giving me nightmares</p>

#### [ Simon Hudon (Apr 11 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/resetI/near/124911556):
<p>It doesn't seem to give you much leeway in how you use it, am I wrong?</p>


{% endraw %}
