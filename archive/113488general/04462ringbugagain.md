---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04462ringbugagain.html
---

## Stream: [general](index.html)
### Topic: [ring bug again?](04462ringbugagain.html)

---


{% raw %}
#### [ Patrick Massot (Jul 31 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20bug%20again%3F/near/130644147):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a&#39;</span> <span class="n">b&#39;</span> <span class="n">a₁</span> <span class="n">b₁</span> <span class="n">a₂</span> <span class="n">b₂</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span>
    <span class="n">a₂</span><span class="bp">*</span><span class="n">b₂</span> <span class="bp">-</span> <span class="n">a₁</span><span class="bp">*</span><span class="n">b₁</span> <span class="bp">=</span> <span class="o">(</span><span class="n">a₂</span> <span class="bp">-</span> <span class="n">a₁</span><span class="o">)</span><span class="bp">*</span><span class="n">b&#39;</span> <span class="bp">+</span> <span class="o">(</span><span class="n">a₂</span> <span class="bp">-</span> <span class="n">a₁</span><span class="o">)</span><span class="bp">*</span><span class="o">(</span><span class="n">b₂</span> <span class="bp">-</span> <span class="n">b&#39;</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b₂</span> <span class="bp">-</span> <span class="n">b₁</span><span class="o">)</span><span class="bp">*</span><span class="n">a&#39;</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b₂</span> <span class="bp">-</span> <span class="n">b₁</span><span class="o">)</span><span class="bp">*</span><span class="o">(</span><span class="n">a₁</span> <span class="bp">-</span> <span class="n">a&#39;</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intros</span><span class="o">,</span>
  <span class="n">ring</span><span class="o">,</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p><span class="emoji emoji-1f61e" title="disappointed">:disappointed:</span></p>

#### [ Johan Commelin (Jul 31 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20bug%20again%3F/near/130644291):
<p><code>comm_ring</code>?</p>

#### [ Patrick Massot (Jul 31 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20bug%20again%3F/near/130644301):
<p>oh yes</p>

#### [ Patrick Massot (Jul 31 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20bug%20again%3F/near/130644306):
<p>Good observation</p>

#### [ Johan Commelin (Jul 31 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20bug%20again%3F/near/130644361):
<p>"In the following file, all rings are assumed commutative"</p>

#### [ Patrick Massot (Jul 31 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20bug%20again%3F/near/130644369):
<p>I blame Kevin who is always writing all rings are commutative</p>

#### [ Kevin Buzzard (Jul 31 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20bug%20again%3F/near/130646253):
<p>It's true by definition! It's a bug in Lean -- they missed commutativity out</p>


{% endraw %}
