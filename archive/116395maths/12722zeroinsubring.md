---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/12722zeroinsubring.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [zero in subring](https://leanprover-community.github.io/archive/116395maths/12722zeroinsubring.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Sep 18 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20in%20subring/near/134172339):
<p>I just added to the perfectoid project:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">subring_has_zero</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">R</span><span class="o">)</span> <span class="o">[</span><span class="n">HS</span> <span class="o">:</span> <span class="n">is_subring</span> <span class="n">S</span><span class="o">]</span> <span class="o">:</span> <span class="n">has_zero</span> <span class="n">S</span> <span class="o">:=</span>
<span class="bp">⟨⟨</span><span class="mi">0</span><span class="o">,</span> <span class="n">is_add_submonoid</span><span class="bp">.</span><span class="n">zero_mem</span> <span class="n">S</span><span class="bp">⟩⟩</span>
</pre></div>


<p>It seems this used to be unnecessary. Any idea what happened? Trying <code>apply_instance</code> loops forever</p>


{% endraw %}
