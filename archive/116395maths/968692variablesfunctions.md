---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/968692variablesfunctions.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [2 variables functions](https://leanprover-community.github.io/archive/116395maths/968692variablesfunctions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Dec 15 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/2%20variables%20functions/near/151852102):
<p>Is it evil to do something like:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">function</span><span class="bp">.</span><span class="n">comp₂</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">δ</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">δ</span> <span class="o">:=</span> <span class="bp">λ</span>  <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span>

<span class="kn">notation</span> <span class="n">g</span> <span class="bp">`</span><span class="err">∘₂</span><span class="bp">`</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">function</span><span class="bp">.</span><span class="n">comp₂</span> <span class="n">f</span> <span class="n">g</span>

<span class="n">def</span> <span class="n">uniform_continuous₂</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">uniform_continuous</span> <span class="o">(</span><span class="n">function</span><span class="bp">.</span><span class="n">uncurry</span> <span class="n">f</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">uniform_continuous₂</span><span class="bp">.</span><span class="n">comp</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">}</span> <span class="o">{</span><span class="n">g</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">δ</span><span class="o">}</span>
  <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">uniform_continuous₂</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">hg</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">g</span><span class="o">)</span> <span class="o">:</span>
<span class="n">uniform_continuous₂</span> <span class="o">(</span><span class="n">g</span> <span class="err">∘₂</span> <span class="n">f</span><span class="o">)</span>
</pre></div>

#### [ Patrick Massot (Dec 15 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/2%20variables%20functions/near/151852103):
<p>etc.</p>

#### [ Patrick Massot (Dec 15 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/2%20variables%20functions/near/151852144):
<p>It seems to be very convenient, but I fear there may be a reason why such a thing is not already used in mathlib</p>

#### [ Mario Carneiro (Dec 16 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/2%20variables%20functions/near/151854577):
<p>you will notice that even regular <code>∘</code> is rarely used</p>

#### [ Mario Carneiro (Dec 16 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/2%20variables%20functions/near/151854580):
<p>because it doesn't unfold as eagerly as one would like</p>

#### [ Mario Carneiro (Dec 16 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/2%20variables%20functions/near/151854627):
<p>it's not particularly evil to make the definition (although you could use the crazy version <code>(∘) ∘ (∘)</code>)</p>

#### [ Kevin Buzzard (Dec 16 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/2%20variables%20functions/near/151874113):
<p>Cue link to my blog post</p>


{% endraw %}
