---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73964findsupr.html
---

## Stream: [general](index.html)
### Topic: [find supr](73964findsupr.html)

---


{% raw %}
#### [ Johan Commelin (Nov 09 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20supr/near/147368449):
<p>I have found</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">supr_pos</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="err">⨆</span> <span class="n">h</span> <span class="o">:</span> <span class="n">p</span><span class="o">,</span> <span class="n">f</span> <span class="n">h</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">hp</span> <span class="o">:=</span>
<span class="n">le_antisymm</span> <span class="o">(</span><span class="n">supr_le</span> <span class="err">$</span> <span class="k">assume</span> <span class="n">h</span><span class="o">,</span> <span class="n">le_refl</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">le_supr</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
</pre></div>


<p>in the library. I would like to have</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">supr_xyzzy</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="err">⨆</span> <span class="n">h</span> <span class="o">:</span> <span class="n">p</span><span class="o">,</span> <span class="n">f</span> <span class="n">h</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">f</span> <span class="n">hp</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>I have never succesfully used find. Somehow it just doesn't give me any results. What should I type into VScode to find this lemma? (Assuming it is there...)</p>

#### [ Johan Commelin (Nov 09 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20supr/near/147372143):
<p>Ok, I've figured out that I should just use <code>supr_le</code> for this one.</p>

#### [ Johan Commelin (Nov 09 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20supr/near/147372222):
<p>Here is another one. Should there be a lemma called <code>mem_of_mem_supr</code>?<br>
It would state that if <code>x ∈ ⊔s ∈ S, s</code> then there is an <code>s ∈ S</code> such that <code>x ∈ s</code>.</p>


{% endraw %}
