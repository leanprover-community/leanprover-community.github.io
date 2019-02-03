---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/05189letinstatements.html
---

## Stream: [maths](index.html)
### Topic: [let in statements](05189letinstatements.html)

---


{% raw %}
#### [ Patrick Massot (Dec 19 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/let%20in%20statements/near/152207819):
<p>How does mathlib like using <code>let</code> in order to unclutter a statement, as in:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">uniform_continuous₂_iff</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">γ</span><span class="o">]</span>
<span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">}</span>  <span class="o">:</span>
<span class="k">let</span> <span class="n">π_α</span> <span class="o">:</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)</span> <span class="bp">×</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">α</span> <span class="o">:=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">p</span><span class="o">,</span> <span class="o">(</span><span class="n">p</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">1</span><span class="o">)),</span>
    <span class="n">π_β</span> <span class="o">:</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)</span> <span class="bp">×</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">×</span> <span class="n">β</span> <span class="o">:=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">p</span><span class="o">,</span> <span class="o">(</span><span class="n">p</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span><span class="o">)),</span>
    <span class="n">F</span>   <span class="o">:</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)</span> <span class="bp">×</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)</span> <span class="bp">→</span> <span class="n">γ</span> <span class="bp">×</span> <span class="n">γ</span> <span class="o">:=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">p</span><span class="o">,</span> <span class="o">(</span><span class="n">f</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="mi">1</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span> <span class="n">f</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">1</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span><span class="o">))</span> <span class="k">in</span>
<span class="n">uniform_continuous₂</span> <span class="n">f</span> <span class="bp">↔</span> <span class="n">map</span> <span class="n">F</span> <span class="o">(</span><span class="n">comap</span> <span class="n">π_α</span> <span class="n">uniformity</span> <span class="err">⊓</span> <span class="n">comap</span> <span class="n">π_β</span> <span class="n">uniformity</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">uniformity</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">uniform_continuous</span><span class="o">,</span><span class="n">uniformity_prod</span><span class="o">,</span> <span class="n">tendsto</span><span class="o">]</span>
</pre></div>

#### [ Patrick Massot (Dec 19 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/let%20in%20statements/near/152207833):
<p>Of course this is done in a file having <code>set_option eqn_compiler.zeta true</code></p>

#### [ Patrick Massot (Dec 19 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/let%20in%20statements/near/152207931):
<p>Note that the above snippet also use full type ascriptions in lets in order to clarify what are those functions without reading their obscure definition</p>

#### [ Scott Morrison (Dec 19 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/let%20in%20statements/near/152212620):
<p>Seems like a good idea.</p>


{% endraw %}
