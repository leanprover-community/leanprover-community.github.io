---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86914moduleandlatticesandetc.html
---

## Stream: [general](index.html)
### Topic: [module and lattices and etc](86914moduleandlatticesandetc.html)

---


{% raw %}
#### [ Kenny Lau (Nov 06 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20and%20lattices%20and%20etc/near/146859692):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">module_of_module_of_ring_hom</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span>
  <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">S</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span>
  <span class="o">{</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">M</span><span class="o">]</span> <span class="o">[</span><span class="n">module</span> <span class="n">S</span> <span class="n">M</span><span class="o">]</span> <span class="o">:</span> <span class="n">module</span> <span class="n">R</span> <span class="n">M</span> <span class="o">:=</span>
<span class="n">module</span><span class="bp">.</span><span class="n">of_core</span> <span class="o">{</span>
  <span class="n">smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">m</span><span class="o">,</span> <span class="n">f</span> <span class="n">r</span> <span class="err">•</span> <span class="n">m</span><span class="o">,</span>
  <span class="n">smul_add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span><span class="o">,</span> <span class="n">smul_add</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">add_smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">s</span> <span class="n">x</span><span class="o">,</span> <span class="k">show</span> <span class="n">f</span> <span class="o">(</span><span class="n">r</span> <span class="bp">+</span> <span class="n">s</span><span class="o">)</span> <span class="err">•</span> <span class="n">x</span> <span class="bp">=</span> <span class="bp">_</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_add</span> <span class="n">f</span><span class="o">,</span> <span class="n">add_smul</span><span class="o">],</span>
  <span class="n">mul_smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">r</span> <span class="n">s</span> <span class="n">x</span><span class="o">,</span> <span class="k">show</span> <span class="n">f</span> <span class="o">(</span><span class="n">r</span> <span class="bp">*</span> <span class="n">s</span><span class="o">)</span> <span class="err">•</span> <span class="n">x</span> <span class="bp">=</span> <span class="bp">_</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_mul</span> <span class="n">f</span><span class="o">,</span> <span class="n">mul_smul</span><span class="o">],</span>
  <span class="n">one_smul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">show</span> <span class="n">f</span> <span class="mi">1</span> <span class="err">•</span> <span class="n">x</span> <span class="bp">=</span> <span class="bp">_</span><span class="o">,</span>
    <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_one</span> <span class="n">f</span><span class="o">,</span> <span class="n">one_smul</span><span class="o">],</span>
<span class="o">}</span>
</pre></div>


<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> how should we call this?</p>

#### [ Kenny Lau (Nov 06 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20and%20lattices%20and%20etc/near/146892841):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Nov 06 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20and%20lattices%20and%20etc/near/146894746):
<p>module.of_ring_hom maybe?</p>


{% endraw %}
