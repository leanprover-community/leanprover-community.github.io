---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/85433toadditivemultiplicative.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [to_additive multiplicative](https://leanprover-community.github.io/archive/116395maths/85433toadditivemultiplicative.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Oct 09 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/to_additive%20multiplicative/near/135470227):
<p>This is again a question about the machinery allowing to transfer stuff from multiplicative monoids/groups to additive. I'm trying to get a version of <a href="https://github.com/leanprover/mathlib/blob/master/group_theory/submonoid.lean#L112-L142" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/group_theory/submonoid.lean#L112-L142">https://github.com/leanprover/mathlib/blob/master/group_theory/submonoid.lean#L112-L142</a> for groups. I tried:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">group_theory</span><span class="bp">.</span><span class="n">subgroup</span>

<span class="kn">namespace</span> <span class="n">group</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">group</span> <span class="n">α</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">exists_list_of_mem_closure</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">closure</span> <span class="n">s</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">∃</span><span class="n">l</span><span class="o">:</span><span class="n">list</span> <span class="n">α</span><span class="o">,</span> <span class="o">(</span><span class="bp">∀</span><span class="n">x</span><span class="err">∈</span><span class="n">l</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">∨</span> <span class="n">x</span><span class="bp">⁻¹</span> <span class="err">∈</span> <span class="n">s</span><span class="o">)</span> <span class="bp">∧</span> <span class="n">l</span><span class="bp">.</span><span class="n">prod</span> <span class="bp">=</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">case</span> <span class="n">in_closure</span><span class="bp">.</span><span class="n">basic</span> <span class="o">:</span> <span class="n">a</span> <span class="n">ha</span> <span class="o">{</span> <span class="n">existsi</span> <span class="o">([</span><span class="n">a</span><span class="o">]),</span> <span class="n">simp</span> <span class="o">[</span><span class="n">ha</span><span class="o">]</span> <span class="o">},</span>
  <span class="n">case</span> <span class="n">in_closure</span><span class="bp">.</span><span class="n">one</span> <span class="o">{</span> <span class="n">existsi</span> <span class="o">([]),</span> <span class="n">simp</span> <span class="o">},</span>
  <span class="n">case</span> <span class="n">in_closure</span><span class="bp">.</span><span class="n">mul</span> <span class="o">:</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">ha</span> <span class="n">hb</span> <span class="o">{</span>
    <span class="n">rcases</span> <span class="n">ha</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">la</span><span class="o">,</span> <span class="n">ha</span><span class="o">,</span> <span class="n">eqa</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">rcases</span> <span class="n">hb</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">lb</span><span class="o">,</span> <span class="n">hb</span><span class="o">,</span> <span class="n">eqb</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">existsi</span> <span class="o">(</span><span class="n">la</span> <span class="bp">++</span> <span class="n">lb</span><span class="o">),</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">eqa</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span> <span class="n">eqb</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span> <span class="n">or_imp_distrib</span><span class="o">],</span>
    <span class="n">exact</span> <span class="k">assume</span> <span class="n">a</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ha</span> <span class="n">a</span><span class="o">,</span> <span class="n">hb</span> <span class="n">a</span><span class="bp">⟩</span>
  <span class="o">},</span>
  <span class="n">case</span> <span class="n">in_closure</span><span class="bp">.</span><span class="n">inv</span> <span class="o">:</span> <span class="n">a</span> <span class="n">a_in_clo</span> <span class="n">hlist</span> <span class="o">{</span>
    <span class="n">rcases</span> <span class="n">hlist</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">la</span><span class="o">,</span> <span class="n">ha</span><span class="o">,</span> <span class="n">eqa</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">existsi</span> <span class="o">(</span><span class="n">la</span><span class="bp">.</span><span class="n">reverse</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="bp">⁻¹</span><span class="o">)),</span>
    <span class="n">split</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">x</span> <span class="n">x_in</span><span class="o">,</span>
      <span class="n">rw</span> <span class="n">list</span><span class="bp">.</span><span class="n">mem_map</span> <span class="n">at</span> <span class="n">x_in</span><span class="o">,</span>
      <span class="n">rcases</span> <span class="n">x_in</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span> <span class="n">b_in</span><span class="o">,</span> <span class="n">hb</span><span class="bp">⟩</span><span class="o">,</span>
      <span class="n">rw</span> <span class="n">list</span><span class="bp">.</span><span class="n">mem_reverse</span> <span class="n">at</span> <span class="n">b_in</span><span class="o">,</span>
      <span class="n">specialize</span> <span class="n">ha</span> <span class="n">b</span> <span class="n">b_in</span><span class="o">,</span>
      <span class="k">have</span> <span class="n">hb&#39;</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">x</span><span class="bp">⁻¹</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="err">←</span><span class="n">hb</span> <span class="bp">;</span> <span class="n">simp</span><span class="o">,</span>
      <span class="n">rw</span> <span class="o">[</span><span class="n">hb</span><span class="o">,</span> <span class="n">hb&#39;</span><span class="o">]</span> <span class="n">at</span> <span class="n">ha</span><span class="o">,</span>
      <span class="n">cc</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">eqa</span><span class="o">,</span> <span class="n">inv_prod</span> <span class="n">la</span><span class="o">]</span> <span class="o">}</span> <span class="o">}</span>
<span class="kn">end</span>
<span class="kn">end</span> <span class="n">group</span>

<span class="kn">namespace</span> <span class="n">add_group</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">α</span><span class="o">]</span>

<span class="kn">theorem</span> <span class="n">exists_list_of_mem_closure</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">closure</span> <span class="n">s</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">∃</span><span class="n">l</span><span class="o">:</span><span class="n">list</span> <span class="n">α</span><span class="o">,</span> <span class="o">(</span><span class="bp">∀</span><span class="n">x</span><span class="err">∈</span><span class="n">l</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">∨</span> <span class="bp">-</span><span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">)</span> <span class="bp">∧</span> <span class="n">l</span><span class="bp">.</span><span class="n">sum</span> <span class="bp">=</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">group</span><span class="bp">.</span><span class="n">exists_list_of_mem_closure</span> <span class="o">(</span><span class="n">multiplicative</span> <span class="n">α</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span>

<span class="kn">end</span> <span class="n">add_group</span>
</pre></div>

#### [ Patrick Massot (Oct 09 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/to_additive%20multiplicative/near/135470239):
<p>But Lean doesn't accept the second statement</p>


{% endraw %}
