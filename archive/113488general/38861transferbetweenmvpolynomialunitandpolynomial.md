---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/38861transferbetweenmvpolynomialunitandpolynomial.html
---

## Stream: [general](index.html)
### Topic: [transfer between mv_polynomial unit and polynomial](38861transferbetweenmvpolynomialunitandpolynomial.html)

---


{% raw %}
#### [ Johan Commelin (Sep 03 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transfer%20between%20mv_polynomial%20unit%20and%20polynomial/near/133275790):
<p>Suppose I want to build a slick machine to move back and forth between <code>mv_polynomial unit</code> and <code>polynomial</code>. Does it make sense to start with</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">rel_unit</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="n">unit</span> <span class="bp">→</span> <span class="n">X</span><span class="o">)</span> <span class="bp">→</span> <span class="n">X</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="n">unit</span><span class="bp">.</span><span class="n">star</span> <span class="bp">=</span> <span class="n">x</span>
</pre></div>


<p>More generally, what goes into building a "transfer API"?</p>

#### [ Chris Hughes (Sep 03 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transfer%20between%20mv_polynomial%20unit%20and%20polynomial/near/133277005):
<p>I thought about this a bit, and I think the function should take an element of an indexing type as an argument. I think this makes it easier if I want to multiply two univariate polynomials together to get a MV poly in two variables.</p>

#### [ Chris Hughes (Sep 03 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transfer%20between%20mv_polynomial%20unit%20and%20polynomial/near/133277077):
<p>I think the transfer API just has all the lemmas about preserving evaluation, degree, multiplication etc.</p>


{% endraw %}
