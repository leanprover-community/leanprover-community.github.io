---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08042partialfinsetfilter.html
---

## Stream: [general](index.html)
### Topic: [partial finset.filter?](08042partialfinsetfilter.html)

---


{% raw %}
#### [ Kenny Lau (Sep 07 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20finset.filter%3F/near/133493792):
<p>Currently:</p>
<div class="codehilite"><pre><span></span><span class="n">finset</span><span class="bp">.</span><span class="n">filter</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_3</span> <span class="o">:</span> <span class="n">decidable_pred</span> <span class="n">p</span><span class="o">],</span> <span class="n">finset</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">finset</span> <span class="n">α</span>
</pre></div>


<p>I wonder if there's a similar function, but instead of defining <code>p</code> everywhere, just define it on the input finset?</p>


{% endraw %}
