---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08701simplifybrickswithfunctioninjective.html
---

## Stream: [general](index.html)
### Topic: [simplify bricks with function.injective](08701simplifybrickswithfunctioninjective.html)

---


{% raw %}
#### [ Kenny Lau (Sep 10 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20bricks%20with%20function.injective/near/133641530):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">injective</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">function</span><span class="bp">.</span><span class="n">injective</span><span class="o">]</span> <span class="n">at</span> <span class="n">H</span>
</pre></div>


<p>trace:</p>
<div class="codehilite"><pre><span></span>--------------
[simplify] iff: function.injective f
[simplify] eq: function.injective f
[simplify] eq: f
[simplify] eq: function.injective
109. [simplify.rewrite] [function.injective.equations._eqn_1]: function.injective f ==&gt; ∀ ⦃a₁ a₂ : α⦄, f a₁ = f a₂ → a₁ = a₂
[simplify] eq: f a₁ = f a₂ → a₁ = a₂
[simplify] eq: f a₁ = f a₂
[simplify] eq: f a₁
[simplify] eq: a₁
[simplify] eq: f
[simplify] eq: f a₂
[simplify] eq: a₂
[simplify] eq: f
[simplify] eq: eq
111. [simplify.rewrite_failure] fail to match &#39;ite_eq_ff_distrib&#39;:
f a₁ = f a₂
=?=
ite ?x_0 ?x_2 ?x_3 = ff
--------------
</pre></div>


<p>ad nauseam</p>


{% endraw %}
