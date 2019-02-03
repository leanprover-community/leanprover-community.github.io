---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/03321Inverseimageoftheindicatorfunction.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Inverse image of the indicator function](https://leanprover-community.github.io/archive/116395maths/03321Inverseimageoftheindicatorfunction.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Koundinya Vajjha (Jan 10 2019 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20of%20the%20indicator%20function/near/154825505):
<p>I'm struggling to get a hold of the inverse image of the indicator function:</p>
<div class="codehilite"><pre><span></span><span class="n">s</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span>

<span class="n">def</span> <span class="n">indicator</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">set</span> <span class="n">s</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">s</span><span class="o">),</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">a</span><span class="o">)]</span>
<span class="o">:=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="n">s</span><span class="o">,</span> <span class="k">if</span> <span class="o">(</span><span class="n">x</span> <span class="err">∈</span> <span class="n">a</span><span class="o">)</span> <span class="k">then</span> <span class="o">(</span><span class="mi">1</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)</span> <span class="k">else</span> <span class="mi">0</span><span class="o">)</span>
</pre></div>


<p>I want to say that if  <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi><mo>=</mo><msub><mn mathvariant="bold">1</mn><mi>A</mi></msub></mrow><annotation encoding="application/x-tex">X = \mathbf{1}_A</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mrel">=</span><span class="mord"><span class="mord"><span class="mord mathbf">1</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">A</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>X</mi><mrow><mo>−</mo><mn>1</mn></mrow></msup><mo>(</mo><mi>B</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">X^{-1}(B)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:1.064108em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.05017em;">B</span><span class="mclose">)</span></span></span></span> is one of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span></span></span></span> ,<span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>A</mi><mi>c</mi></msup></mrow><annotation encoding="application/x-tex"> A^c</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">A</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">c</span></span></span></span></span></span></span></span></span></span></span>, <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">∅</mi></mrow><annotation encoding="application/x-tex">\emptyset</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:0.80556em;vertical-align:-0.05556em;"></span><span class="base"><span class="mord mathrm">∅</span></span></span></span> or <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi mathvariant="normal">∅</mi><mi>c</mi></msup></mrow><annotation encoding="application/x-tex">\emptyset^c</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:0.80556em;vertical-align:-0.05556em;"></span><span class="base"><span class="mord"><span class="mord mathrm">∅</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">c</span></span></span></span></span></span></span></span></span></span></span>. <br>
Any help would be appreciated.</p>

#### [ Koundinya Vajjha (Jan 10 2019 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20of%20the%20indicator%20function/near/154825541):
<p>Also, how do I LaTeX?</p>

#### [ Johan Commelin (Jan 10 2019 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20of%20the%20indicator%20function/near/154825620):
<p>LaTeX with double dollars: <code>$$ blah $$</code></p>

#### [ Joey van Langen (Jan 10 2019 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20of%20the%20indicator%20function/near/154825689):
<p>You can get the inverse image with the symbol <code> ⁻¹' </code>, which is \inv ' in lean</p>

#### [ Joey van Langen (Jan 10 2019 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20of%20the%20indicator%20function/near/154825717):
<p>It is in mathlib/data/set/basic</p>

#### [ Koundinya Vajjha (Jan 10 2019 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20of%20the%20indicator%20function/near/154825808):
<p>Yes I saw that, but I'm not able to state what I want to prove...</p>

#### [ Johan Commelin (Jan 10 2019 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20of%20the%20indicator%20function/near/154825867):
<p>What have you tried? Can you give your attempt (+ error?)</p>

#### [ Koundinya Vajjha (Jan 10 2019 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20of%20the%20indicator%20function/near/154826020):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">indicator_inv</span> <span class="o">(</span><span class="n">a</span><span class="o">:</span> <span class="n">set</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">set</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">s</span><span class="o">),</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">a</span><span class="o">)]</span> <span class="o">:</span>
<span class="n">indicator</span> <span class="n">s</span> <span class="n">a</span> <span class="bp">⁻¹</span><span class="err">&#39;</span>  <span class="o">(</span><span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="o">{</span> <span class="c1">-- what goes here ? }</span>
</pre></div>

#### [ Johan Commelin (Jan 10 2019 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20of%20the%20indicator%20function/near/154826164):
<p>I see. I think you want 4 lemmas</p>

#### [ Johan Commelin (Jan 10 2019 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20of%20the%20indicator%20function/near/154826179):
<p>But maybe it depends on why you want this, and how you want to use this.</p>

#### [ Joey van Langen (Jan 10 2019 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20of%20the%20indicator%20function/near/154826285):
<p>How about this:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="kn">variable</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span>

<span class="n">def</span> <span class="n">indicator</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">set</span> <span class="n">s</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">s</span><span class="o">),</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">a</span><span class="o">)]</span>
<span class="o">:=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="n">s</span><span class="o">,</span> <span class="k">if</span> <span class="o">(</span><span class="n">x</span> <span class="err">∈</span> <span class="n">a</span><span class="o">)</span> <span class="k">then</span> <span class="o">(</span><span class="mi">1</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)</span> <span class="k">else</span> <span class="mi">0</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">preimage_indicator</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">set</span> <span class="n">s</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">s</span><span class="o">),</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">a</span><span class="o">)]</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">set</span> <span class="n">ℝ</span><span class="o">):</span>
<span class="o">(</span><span class="n">indicator</span> <span class="n">s</span> <span class="n">a</span><span class="o">)</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">∨</span> <span class="o">(</span><span class="n">indicator</span> <span class="n">s</span> <span class="n">a</span><span class="o">)</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">b</span> <span class="bp">=</span> <span class="err">∅</span> <span class="bp">∨</span>
<span class="o">(</span><span class="n">indicator</span> <span class="n">s</span> <span class="n">a</span><span class="o">)</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">b</span> <span class="bp">=</span> <span class="bp">-</span> <span class="n">a</span> <span class="bp">∨</span> <span class="o">(</span><span class="n">indicator</span> <span class="n">s</span> <span class="n">a</span><span class="o">)</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">b</span> <span class="bp">=</span> <span class="bp">-</span><span class="err">∅</span> <span class="o">:=</span>
<span class="n">sorry</span>
</pre></div>

#### [ Koundinya Vajjha (Jan 10 2019 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20of%20the%20indicator%20function/near/154826344):
<p>I'm trying to prove that the indicator function of an event is a random variable.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">is_random_variable</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">measurable_space</span> <span class="n">s</span><span class="o">]</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">measurable</span> <span class="n">X</span>


<span class="kn">lemma</span> <span class="n">is_random_variable_indicator</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">set</span> <span class="n">s</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="o">(</span><span class="n">set</span> <span class="n">s</span><span class="o">)]</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">s</span><span class="o">),</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">a</span><span class="o">)]:</span>
<span class="n">is_random_variable</span> <span class="o">(</span><span class="n">indicator</span> <span class="bp">_</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">intros</span> <span class="n">b</span> <span class="n">h</span><span class="o">,</span>
<span class="n">unfold</span> <span class="n">measurable_space</span><span class="bp">.</span><span class="n">map</span><span class="o">,</span>
<span class="n">unfold</span> <span class="n">set</span><span class="bp">.</span><span class="n">preimage</span><span class="o">,</span> <span class="n">dsimp</span><span class="o">,</span>
<span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Koundinya Vajjha (Jan 10 2019 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20of%20the%20indicator%20function/near/154826454):
<p>I'm stuck at </p>
<div class="codehilite"><pre><span></span><span class="n">s</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">measurable_space</span> <span class="n">s</span><span class="o">,</span>
<span class="n">a</span> <span class="o">:</span> <span class="n">set</span> <span class="n">s</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_2</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="o">(</span><span class="n">set</span> <span class="n">s</span><span class="o">),</span>
<span class="bp">_</span><span class="n">inst_3</span> <span class="o">:</span> <span class="n">decidable_pred</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">s</span><span class="o">),</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">a</span><span class="o">),</span>
<span class="n">b</span> <span class="o">:</span> <span class="n">set</span> <span class="n">ℝ</span><span class="o">,</span>
<span class="n">h</span> <span class="o">:</span> <span class="n">measurable_space</span><span class="bp">.</span><span class="n">is_measurable</span> <span class="o">(</span><span class="n">measure_theory</span><span class="bp">.</span><span class="n">borel</span> <span class="n">ℝ</span><span class="o">)</span> <span class="n">b</span>
<span class="err">⊢</span> <span class="n">measurable_space</span><span class="bp">.</span><span class="n">is_measurable</span> <span class="bp">_</span><span class="n">inst_1</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">s</span> <span class="bp">|</span> <span class="n">indicator</span> <span class="n">s</span> <span class="n">a</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">b</span><span class="o">}</span>
</pre></div>

#### [ Koundinya Vajjha (Jan 10 2019 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20of%20the%20indicator%20function/near/154826480):
<p>I want to prove a lemma which would possibly rewrite the <code>{x : s | indicator s a x ∈ b}</code> maybe...</p>

#### [ Koundinya Vajjha (Jan 10 2019 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse%20image%20of%20the%20indicator%20function/near/154826609):
<p><span class="user-mention" data-user-id="143810">@Joey van Langen</span>  thanks I'll try that.</p>


{% endraw %}
