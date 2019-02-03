---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/50225characterisationofreals.html
---

## Stream: [maths](index.html)
### Topic: [characterisation of reals](50225characterisationofreals.html)

---


{% raw %}
#### [ Kevin Buzzard (Nov 17 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/characterisation%20of%20reals/near/147869830):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">archimedean</span>
<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="c1">-- non-empty and bounded -&gt; LUB</span>
<span class="kn">definition</span> <span class="n">is_complete</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">has_le</span> <span class="n">k</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">∀</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">k</span><span class="o">),</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">S</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">S</span><span class="o">,</span> <span class="n">y</span> <span class="bp">≤</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span>
  <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">y</span><span class="o">,</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">y</span> <span class="bp">↔</span> <span class="bp">∀</span> <span class="n">z</span> <span class="err">∈</span> <span class="n">S</span><span class="o">,</span> <span class="n">z</span> <span class="bp">≤</span> <span class="n">y</span>

<span class="c1">-- this is already in Lean</span>
<span class="kn">theorem</span> <span class="n">real</span><span class="bp">.</span><span class="n">complete</span> <span class="o">:</span> <span class="n">is_complete</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">S</span><span class="o">,</span> <span class="n">real</span><span class="bp">.</span><span class="n">exists_sup</span> <span class="n">S</span>

<span class="c1">-- have I got this right?</span>
<span class="kn">theorem</span> <span class="n">characterisation_of_reals_first_attempt</span>
<span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">linear_ordered_field</span> <span class="n">k</span><span class="o">]</span> <span class="o">[</span><span class="n">archimedean</span> <span class="n">k</span><span class="o">]</span> <span class="o">:</span>
<span class="n">is_complete</span> <span class="n">k</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">f</span> <span class="o">:</span> <span class="n">k</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">,</span> <span class="n">function</span><span class="bp">.</span><span class="n">bijective</span> <span class="n">f</span> <span class="bp">∧</span> <span class="n">is_ring_hom</span> <span class="n">f</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>I remember talking about this sort of thing with Patrick and others several months ago. I was teaching this stuff recently and I meant to get around to looking at this, but we ended up doing constructions of the reals via Dedekind cuts and Cauchy sequences and proving basic stuff like existence of floor function and density of rationals in reals from the completeness axiom instead. </p>
<p>Is this already in mathlib?</p>


{% endraw %}
