---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85479leminofmem.html
---

## Stream: [general](index.html)
### Topic: [le_min_of_mem](85479leminofmem.html)

---


{% raw %}
#### [ Kenny Lau (Jul 28 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_min_of_mem/near/130485616):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">le_min_of_mem</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="n">h₂</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span><span class="bp">.</span><span class="n">min</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rcases</span> <span class="bp">@</span><span class="n">inf_le</span> <span class="o">(</span><span class="n">with_top</span> <span class="n">α</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">h₁</span> <span class="bp">_</span> <span class="n">rfl</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">b&#39;</span><span class="o">,</span> <span class="n">hb</span><span class="o">,</span> <span class="n">ab</span><span class="bp">⟩;</span>
   <span class="n">cases</span> <span class="n">h₂</span><span class="bp">.</span><span class="n">symm</span><span class="bp">.</span><span class="n">trans</span> <span class="n">hb</span><span class="bp">;</span> <span class="n">assumption</span>
</pre></div>

#### [ Kenny Lau (Jul 28 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_min_of_mem/near/130485617):
<p>looks like <code>min_le_of_mem</code> to me</p>

#### [ Chris Hughes (Jul 28 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_min_of_mem/near/130485669):
<p>PR it.</p>

#### [ Chris Hughes (Jul 28 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_min_of_mem/near/130485715):
<p>my guess is someone copied the name <code>le_max_of_mem</code> and didn't notice the word order needed changing</p>


{% endraw %}
