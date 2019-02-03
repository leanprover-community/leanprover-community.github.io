---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/97444naminghelp.html
---

## Stream: [general](index.html)
### Topic: [naming help](97444naminghelp.html)

---


{% raw %}
#### [ Sean Leather (Jul 24 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20help/near/130194006):
<p>What names would you give these definitions?</p>
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="n">def</span> <span class="n">unknown₁</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">∀</span> <span class="o">⦃</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">sigma</span> <span class="n">β</span><span class="o">⦄</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span><span class="o">),</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">h</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span> <span class="o">:</span> <span class="n">β</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">2</span>

<span class="n">def</span> <span class="n">unknown₂</span> <span class="o">{</span><span class="n">α₁</span> <span class="n">α₂</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β₁</span> <span class="o">:</span> <span class="n">α₁</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="n">β₂</span> <span class="o">:</span> <span class="n">α₂</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">sigma</span> <span class="n">β₁</span> <span class="bp">→</span> <span class="n">sigma</span> <span class="n">β₂</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">∀</span> <span class="o">⦃</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">sigma</span> <span class="n">β₁</span><span class="o">⦄,</span> <span class="o">(</span><span class="n">f</span> <span class="n">s</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">=</span> <span class="o">(</span><span class="n">f</span> <span class="n">t</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">→</span> <span class="n">s</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="mi">1</span>
</pre></div>

#### [ Sean Leather (Jul 24 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20help/near/130194079):
<p>The first says a <code>sigma β</code> should be considered a function: equal arguments (<code>fst</code>s) produce equal results (<code>snd</code>s).</p>

#### [ Sean Leather (Jul 24 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20help/near/130194091):
<p>The second says that a function on <code>sigma</code>s preserves (injective) equality on the <code>fst</code>s.</p>


{% endraw %}
