---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51326orderofinputstofunction.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [order of inputs to function](https://leanprover-community.github.io/archive/113488general/51326orderofinputstofunction.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Nov 14 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20of%20inputs%20to%20function/near/147668376):
<p>Sorry if this is already covered somewhere. What should the order of the inputs be in a definition such as</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">nth_root_pow_left</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">}</span> <span class="o">{</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">Hm</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">Hx</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="n">nth_root</span> <span class="n">x</span> <span class="n">m</span><span class="o">)</span> <span class="err">^</span> <span class="o">(</span><span class="n">m</span> <span class="bp">*</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">x</span> <span class="err">^</span> <span class="n">n</span> <span class="o">:=</span>
</pre></div>


<p>? I'm writing a little library about n'th roots and I've realised that I'm just putting the reals and nats and positivity facts in random and inconsistent orders.</p>

#### [ Kenny Lau (Nov 14 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20of%20inputs%20to%20function/near/147668608):
<p><code>x</code> before <code>m</code>, so <code>x</code> before <code>m</code></p>


{% endraw %}
