---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/02588uniformcontinuouscontinuous.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [uniform_continuous.continuous](https://leanprover-community.github.io/archive/116395maths/02588uniformcontinuouscontinuous.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Dec 20 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242464):
<p>Still trying to clean up topology stuff, I realized the proof that <a href="https://github.com/leanprover/mathlib/blob/caa2076038e2d5a84fd05e9988fbe31d01a7f6ba/analysis/topology/uniform_space.lean#L487-L500" target="_blank" title="https://github.com/leanprover/mathlib/blob/caa2076038e2d5a84fd05e9988fbe31d01a7f6ba/analysis/topology/uniform_space.lean#L487-L500">uniform continuous functions are continuous</a> is pretty hard to read. <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> how do you like the following proof:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">uniform_continuous</span><span class="bp">.</span><span class="n">continuous</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span>
  <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">f</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="n">continuous_iff_tendsto</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">a</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">key</span> <span class="o">:</span> <span class="n">prod</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="err">∘</span> <span class="n">f</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">p</span> <span class="o">:</span> <span class="n">α</span><span class="bp">×</span><span class="n">α</span><span class="o">,</span> <span class="o">(</span><span class="n">f</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">f</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="o">))</span> <span class="err">∘</span> <span class="n">prod</span><span class="bp">.</span><span class="n">mk</span> <span class="n">a</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">tendsto_iff_comap</span><span class="o">,</span> <span class="n">nhds_eq_comap_uniformity</span><span class="o">,</span> <span class="n">nhds_eq_comap_uniformity</span><span class="o">,</span> <span class="n">comap_comap_comp</span><span class="o">,</span> <span class="n">key</span><span class="o">],</span>
  <span class="n">conv_rhs</span> <span class="o">{</span> <span class="n">rw</span> <span class="err">←</span><span class="n">comap_comap_comp</span> <span class="o">},</span>
  <span class="n">apply</span> <span class="n">comap_mono</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">map_le_iff_le_comap</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">hf</span>
<span class="kn">end</span>
</pre></div>

#### [ Johannes Hölzl (Dec 20 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242558):
<p>I don't like this at all. I'm okay with adding <code>show</code> or similar to the original proof. But replacing it with an arbitrary sequence of tactic calls doesn't make it more readable.</p>

#### [ Patrick Massot (Dec 20 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242570):
<p>The main difference is I use <a href="https://github.com/leanprover/mathlib/blob/caa2076038e2d5a84fd05e9988fbe31d01a7f6ba/analysis/topology/uniform_space.lean#L261" target="_blank" title="https://github.com/leanprover/mathlib/blob/caa2076038e2d5a84fd05e9988fbe31d01a7f6ba/analysis/topology/uniform_space.lean#L261">nhds x = uniformity.comap (prod.mk x)</a> instead of <a href="https://github.com/leanprover/mathlib/blob/caa2076038e2d5a84fd05e9988fbe31d01a7f6ba/analysis/topology/uniform_space.lean#L267" target="_blank" title="https://github.com/leanprover/mathlib/blob/caa2076038e2d5a84fd05e9988fbe31d01a7f6ba/analysis/topology/uniform_space.lean#L267">nhds x = uniformity.lift' (λs:set (α×α), {y | (x, y) ∈ s})</a></p>

#### [ Patrick Massot (Dec 20 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242582):
<p>It's not all about using tactic instead of term mode, it's a math difference</p>

#### [ Patrick Massot (Dec 20 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242624):
<p>I can rewrite it using calc if you prefer</p>

#### [ Johannes Hölzl (Dec 20 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242626):
<p>This is indeed a good change. But it would be nice if the proof structure wouldn't be hidden behind the tactics.</p>

#### [ Johannes Hölzl (Dec 20 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242631):
<p>Yes, this would be good!</p>

#### [ Patrick Massot (Dec 20 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242736):
<p>The key annoyance (here and elsewhere in this corner of mathlib) is how Lean notation is far less legible that paper notation when it comes to pull-back and push-forward. And also we don't have notation for <code>(λ p : α×α, (f p.1, f p.2))</code> (this one is probably solvable) Compare <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>U</mi><mi>α</mi></msub><mo>≤</mo><mo>(</mo><mi>f</mi><mo>×</mo><mi>f</mi><msup><mo>)</mo><mo>∗</mo></msup><msub><mi>U</mi><mi>β</mi></msub></mrow><annotation encoding="application/x-tex">U_\alpha \leq (f \times f)^*U_\beta</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1.036108em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:-0.10903em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.0037em;">α</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mrel">≤</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mbin">×</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.688696em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">∗</span></span></span></span></span></span></span></span><span class="mord"><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3361079999999999em;"><span style="top:-2.5500000000000003em;margin-left:-0.10903em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.05278em;">β</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span></span></span></span> and <code>uniformity ≤ comap (λ p : α×α, (f p.1, f p.2)) uniformity</code></p>

#### [ Mario Carneiro (Dec 20 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152242990):
<p>isn't this <code>prod.map f f</code>?</p>

#### [ Patrick Massot (Dec 20 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152243305):
<p>Indeed it is! But not by definition <span class="emoji emoji-2639" title="sad">:sad:</span></p>

#### [ Patrick Massot (Dec 20 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152243322):
<p>Johannes, do you think we should rewrite everything using this <code>prod.map</code> in the definition of uniform continuity?</p>

#### [ Johannes Hölzl (Dec 20 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152243445):
<p>ouch, I think <code>prod.map</code> should have a different def, <code>(prod.map f g p).1 = f p.1</code> should be defeq</p>

#### [ Johannes Hölzl (Dec 20 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152243470):
<p>what about adding <code>def prod.map₂ {α β} (f : α → β) (p : α × α) : β × β := (f p.1, f p.2)</code></p>

#### [ Patrick Massot (Dec 20 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152243537):
<p>This clever guy noticed how  I love subscript 2 those days.</p>

#### [ Mario Carneiro (Dec 20 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152243552):
<p>I guess this can be <code>map₂ f = map f f</code> once the definition of <code>map</code> is fixed</p>

#### [ Alistair Tucker (Dec 20 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152244491):
<p>I used prod.map for a reformulation of cauchy_seq in the contraction mapping stuff, but it didn't seem well-supported with theorems. I also had to define a partial order on products.</p>

#### [ Patrick Massot (Dec 20 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform_continuous.continuous/near/152245261):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> see <a href="#narrow/stream/113488-general/subject/calc.20iff/near/152245238" title="#narrow/stream/113488-general/subject/calc.20iff/near/152245238">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/calc.20iff/near/152245238</a></p>


{% endraw %}
