---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/29791finsuppmodules.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [finsupp modules](https://leanprover-community.github.io/archive/116395maths/29791finsuppmodules.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Nov 22 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finsupp%20modules/near/148149210):
<p>I think the module part of finsupp is broken. For example in</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">sum_smul_index</span> <span class="o">[</span><span class="n">ring</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">add_comm_monoid</span> <span class="n">γ</span><span class="o">]</span> <span class="o">{</span><span class="n">g</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span><span class="err">₀</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">h</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">}</span>
  <span class="o">(</span><span class="n">h0</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">i</span><span class="o">,</span> <span class="n">h</span> <span class="n">i</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">b</span> <span class="err">•</span> <span class="n">g</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="n">h</span> <span class="bp">=</span> <span class="n">g</span><span class="bp">.</span><span class="n">sum</span> <span class="o">(</span><span class="bp">λ</span><span class="n">i</span> <span class="n">a</span><span class="o">,</span> <span class="n">h</span> <span class="n">i</span> <span class="o">(</span><span class="n">b</span> <span class="bp">*</span> <span class="n">a</span><span class="o">))</span> <span class="o">:=</span>
<span class="n">finsupp</span><span class="bp">.</span><span class="n">sum_map_range_index</span> <span class="n">h0</span>
</pre></div>


<p>the <code>g</code> takes values in the ring <code>\beta</code>. But what is realy interesting is if <code>g</code> takes values in a module over the ring.</p>


{% endraw %}
