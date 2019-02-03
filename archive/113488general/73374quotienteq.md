---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73374quotienteq.html
---

## Stream: [general](index.html)
### Topic: [quotient.eq](73374quotienteq.html)

---


{% raw %}
#### [ Patrick Massot (Dec 15 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.eq/near/151846739):
<p>We have </p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">eq</span> <span class="o">[</span><span class="n">r</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="err">⟦</span><span class="n">x</span><span class="err">⟧</span> <span class="bp">=</span> <span class="err">⟦</span><span class="n">y</span><span class="err">⟧</span> <span class="bp">↔</span> <span class="n">x</span> <span class="bp">≈</span> <span class="n">y</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">quotient</span><span class="bp">.</span><span class="n">exact</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span><span class="bp">⟩</span>
</pre></div>


<p>Are we sure this is a good simp lemma?</p>


{% endraw %}
