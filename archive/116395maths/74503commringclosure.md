---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/74503commringclosure.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [comm_ring.closure](https://leanprover-community.github.io/archive/116395maths/74503commringclosure.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Oct 09 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135495590):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Do you secretely have <code>comm_ring.closure</code> with a <code>subring</code> instance somewhere in your repositories?</p>

#### [ Kenny Lau (Oct 09 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135495611):
<p>I don't think so.</p>

#### [ Patrick Massot (Oct 09 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135495859):
<p>Too bad. Do you want to sprint through it?</p>

#### [ Kenny Lau (Oct 09 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135495873):
<p>sure</p>

#### [ Patrick Massot (Oct 09 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135495989):
<p>I began with</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">ring_theory</span><span class="bp">.</span><span class="n">subring</span>

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
<span class="n">sorry</span>
<span class="kn">end</span> <span class="n">add_group</span>

<span class="kn">namespace</span> <span class="n">comm_ring</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span>

<span class="n">def</span> <span class="n">closure</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">closure</span> <span class="o">(</span><span class="n">monoid</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span><span class="o">)</span>

<span class="kn">instance</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">R</span><span class="o">}</span> <span class="o">:</span> <span class="n">is_subring</span> <span class="o">(</span><span class="n">closure</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">dunfold</span> <span class="n">closure</span><span class="o">,</span>
  <span class="n">exact</span>
    <span class="o">{</span> <span class="n">zero_mem</span> <span class="o">:=</span> <span class="n">is_add_submonoid</span><span class="bp">.</span><span class="n">zero_mem</span> <span class="bp">_</span><span class="o">,</span>
      <span class="n">add_mem</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">ha</span> <span class="n">hb</span><span class="o">,</span> <span class="n">is_add_submonoid</span><span class="bp">.</span><span class="n">add_mem</span> <span class="n">ha</span> <span class="n">hb</span><span class="o">,</span>
      <span class="n">neg_mem</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">h</span><span class="o">,</span> <span class="n">is_add_subgroup</span><span class="bp">.</span><span class="n">neg_mem</span> <span class="n">h</span><span class="o">,</span>
      <span class="n">one_mem</span> <span class="o">:=</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">mem_closure</span> <span class="o">(</span><span class="n">is_submonoid</span><span class="bp">.</span><span class="n">one_mem</span> <span class="bp">_</span><span class="o">),</span>
      <span class="n">mul_mem</span> <span class="o">:=</span> <span class="k">begin</span>
        <span class="n">intros</span> <span class="n">a</span> <span class="n">b</span> <span class="n">a_in</span> <span class="n">b_in</span><span class="o">,</span>
        <span class="n">rcases</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">exists_list_of_mem_closure</span> <span class="n">a_in</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">la</span><span class="o">,</span> <span class="n">hla</span><span class="o">,</span> <span class="n">sum_a</span><span class="bp">⟩</span><span class="o">,</span>
        <span class="n">rcases</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">exists_list_of_mem_closure</span> <span class="n">b_in</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">lb</span><span class="o">,</span> <span class="n">hlb</span><span class="o">,</span> <span class="n">sum_b</span><span class="bp">⟩</span><span class="o">,</span>
        <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">sum_a</span><span class="o">,</span> <span class="err">←</span><span class="n">sum_b</span><span class="o">],</span>
        <span class="n">sorry</span><span class="o">,</span>
      <span class="kn">end</span> <span class="o">}</span>
<span class="kn">end</span>

<span class="kn">end</span> <span class="n">comm_ring</span>
</pre></div>

#### [ Patrick Massot (Oct 09 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135496035):
<p>But I lost courage because of <a href="#narrow/stream/116395-maths/subject/to_additive.20multiplicative/near/135470227" title="#narrow/stream/116395-maths/subject/to_additive.20multiplicative/near/135470227">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/to_additive.20multiplicative/near/135470227</a> and sum manipulations</p>

#### [ Patrick Massot (Oct 09 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135496067):
<p>The trouble is that the big_operator stuff in mathlib is all about sums over finset, not lists</p>

#### [ Patrick Massot (Oct 09 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135496121):
<p>(here I mean the trouble with the final sorry, the <code>to_additive</code> stuff is simply total mystery)</p>

#### [ Kenny Lau (Oct 09 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497365):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">ring_theory</span><span class="bp">.</span><span class="n">subring</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">add_monoid</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">add_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span>
  <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">add_monoid</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">C</span> <span class="mi">0</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H3</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">add_monoid</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">add_monoid</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">))</span> <span class="o">:</span>
  <span class="n">C</span> <span class="n">a</span> <span class="o">:=</span>
<span class="n">monoid</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">H</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">H1</span><span class="o">)</span> <span class="n">H2</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">H3</span><span class="o">)</span>

<span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span>
  <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">C</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">H3</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="bp">-</span><span class="n">a</span><span class="o">))</span>
  <span class="o">(</span><span class="n">H4</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">))</span> <span class="o">:</span>
  <span class="n">C</span> <span class="n">a</span> <span class="o">:=</span>
<span class="n">group</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">H</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">H1</span><span class="o">)</span> <span class="n">H2</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">H3</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">H4</span><span class="o">)</span>

<span class="kn">namespace</span> <span class="n">comm_ring</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span>

<span class="n">def</span> <span class="n">closure</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">closure</span> <span class="o">(</span><span class="n">monoid</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span><span class="o">)</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">closure</span>

<span class="kn">instance</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">R</span><span class="o">}</span> <span class="o">:</span> <span class="n">is_subring</span> <span class="o">(</span><span class="n">closure</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">zero_mem</span> <span class="o">:=</span> <span class="n">is_add_submonoid</span><span class="bp">.</span><span class="n">zero_mem</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">add_mem</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">ha</span> <span class="n">hb</span><span class="o">,</span> <span class="n">is_add_submonoid</span><span class="bp">.</span><span class="n">add_mem</span> <span class="n">ha</span> <span class="n">hb</span><span class="o">,</span>
  <span class="n">neg_mem</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">h</span><span class="o">,</span> <span class="n">is_add_subgroup</span><span class="bp">.</span><span class="n">neg_mem</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">one_mem</span> <span class="o">:=</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">mem_closure</span> <span class="o">(</span><span class="n">is_submonoid</span><span class="bp">.</span><span class="n">one_mem</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">mul_mem</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">ha</span> <span class="n">hb</span><span class="o">,</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">hb</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span> <span class="n">hb</span><span class="o">,</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">ha</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">ha</span><span class="o">,</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">subset_closure</span> <span class="o">(</span><span class="n">is_submonoid</span><span class="bp">.</span><span class="n">mul_mem</span> <span class="n">ha</span> <span class="n">hb</span><span class="o">))</span>
      <span class="o">((</span><span class="n">zero_mul</span> <span class="n">b</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">is_add_submonoid</span><span class="bp">.</span><span class="n">zero_mem</span> <span class="bp">_</span><span class="o">)</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">ha</span> <span class="n">hab</span><span class="o">,</span> <span class="o">(</span><span class="n">neg_mul_eq_neg_mul</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="bp">▸</span> <span class="n">is_add_subgroup</span><span class="bp">.</span><span class="n">neg_mem</span> <span class="n">hab</span><span class="o">)</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">c</span> <span class="n">ha</span> <span class="n">hc</span> <span class="n">hab</span> <span class="n">hcb</span><span class="o">,</span> <span class="o">(</span><span class="n">add_mul</span> <span class="n">a</span> <span class="n">c</span> <span class="n">b</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">is_add_submonoid</span><span class="bp">.</span><span class="n">add_mem</span> <span class="n">hab</span> <span class="n">hcb</span><span class="o">))</span>
    <span class="o">((</span><span class="n">mul_zero</span> <span class="n">a</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">is_add_submonoid</span><span class="bp">.</span><span class="n">zero_mem</span> <span class="bp">_</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span> <span class="n">hb</span> <span class="n">hab</span><span class="o">,</span> <span class="o">(</span><span class="n">neg_mul_eq_mul_neg</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="bp">▸</span> <span class="n">is_add_subgroup</span><span class="bp">.</span><span class="n">neg_mem</span> <span class="n">hab</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span> <span class="n">c</span> <span class="n">hb</span> <span class="n">hc</span> <span class="n">hab</span> <span class="n">hac</span><span class="o">,</span> <span class="o">(</span><span class="n">mul_add</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">is_add_submonoid</span><span class="bp">.</span><span class="n">add_mem</span> <span class="n">hab</span> <span class="n">hac</span><span class="o">)</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">comm_ring</span>
</pre></div>

#### [ Kenny Lau (Oct 09 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497371):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span></p>

#### [ Patrick Massot (Oct 09 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497490):
<p>Thanks!</p>

#### [ Patrick Massot (Oct 09 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497506):
<p>Could we still get the list statements analogue to what is already in mathlib for monoids?</p>

#### [ Patrick Massot (Oct 09 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497537):
<p>Is the reducible attribute purely intended to save a couple of <code>dunfold</code> in the instance building?</p>

#### [ Kenny Lau (Oct 09 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497735):
<blockquote>
<p>Is the reducible attribute purely intended to save a couple of <code>dunfold</code> in the instance building?</p>
</blockquote>
<p>yes</p>

#### [ Patrick Massot (Oct 09 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497881):
<p>Why do you get <code>monoid.in_closure.rec_on</code> for free when defining <code>monoid.in_closure</code> but need to write <code>add_monoid.in_closure.rec_on</code>?</p>

#### [ Patrick Massot (Oct 09 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497906):
<p>Is it because of the multiplicative to additive magic?</p>

#### [ Patrick Massot (Oct 09 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497918):
<p>which is not magic enough?</p>

#### [ Kenny Lau (Oct 09 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498021):
<p>because <code>add_monoid.closure</code> is not defined using <code>to_additive</code></p>

#### [ Patrick Massot (Oct 09 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498278):
<p>And why isn't it defined using <code>to_additive</code>?</p>

#### [ Patrick Massot (Oct 09 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498343):
<p>The definition is really weird. At some point earlier Lean was completely confused and asked me to prove stuff involving 1 in an additive context</p>

#### [ Patrick Massot (Oct 09 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498464):
<p>I would have never thought of proving that instance using these nested inductions. The real world proof manipulating sums is so easy, it seems beyond masochistic to write your proof.</p>

#### [ Kenny Lau (Oct 09 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498625):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">exists_list_of_mem_closure</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">closure</span> <span class="n">s</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">∃</span><span class="n">l</span><span class="o">:</span><span class="n">list</span> <span class="n">α</span><span class="o">,</span> <span class="o">(</span><span class="bp">∀</span><span class="n">x</span><span class="err">∈</span><span class="n">l</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">∨</span> <span class="bp">-</span><span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">)</span> <span class="bp">∧</span> <span class="n">l</span><span class="bp">.</span><span class="n">sum</span> <span class="bp">=</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">group</span><span class="bp">.</span><span class="n">exists_list_of_mem_closure</span> <span class="n">h</span>
</pre></div>

#### [ Patrick Massot (Oct 09 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498664):
<p>this is even more confusing</p>

#### [ Patrick Massot (Oct 09 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498756):
<p>I thought you would be using your custom recursor</p>

#### [ Kenny Lau (Oct 09 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498770):
<p>me too</p>

#### [ Kenny Lau (Oct 09 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498777):
<p>and halfway I realized</p>

#### [ Patrick Massot (Oct 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498839):
<p>Do you understand what's going on with this way of turning multiplicative stuff into additive one?</p>

#### [ Kenny Lau (Oct 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498846):
<p>somewhat.</p>

#### [ Patrick Massot (Oct 09 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500038):
<p>What about the <code>exists_lists_of_mem_closure</code> in the ring case?</p>

#### [ Patrick Massot (Oct 09 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500057):
<p>something like</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">exists_list_of_mem_closure</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">R</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">R</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">closure</span> <span class="n">s</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">∃</span> <span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">list</span> <span class="n">R</span><span class="o">),</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">l</span> <span class="err">∈</span> <span class="n">L</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">l</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">∨</span> <span class="bp">-</span><span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">map</span> <span class="n">list</span><span class="bp">.</span><span class="n">prod</span> <span class="n">L</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="bp">=</span> <span class="n">a</span><span class="o">)</span>
</pre></div>

#### [ Patrick Massot (Oct 09 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500098):
<p>I guess I would try to use the previous theorems but you'll run crazy inductions...</p>

#### [ Kenny Lau (Oct 09 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500174):
<p>why do we need <code>list (list R)</code>?</p>

#### [ Kenny Lau (Oct 09 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500189):
<p>ah I see</p>

#### [ Kenny Lau (Oct 09 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500217):
<p>maybe we should prove the recursor for comm_ring.closure first</p>

#### [ Patrick Massot (Oct 09 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500248):
<p>of course the maths proof is not at all by induction</p>

#### [ Patrick Massot (Oct 09 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500297):
<p>but in Lean it would probably be easier by induction</p>

#### [ Kenny Lau (Oct 09 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500313):
<p>oh how do you prove it in maths?</p>

#### [ Patrick Massot (Oct 09 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500454):
<p>The maths proof starts with <code>  rcases add_group.exists_list_of_mem_closure h with ⟨L1, hL1, L1sum⟩,</code></p>

#### [ Patrick Massot (Oct 09 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500482):
<p>Then you need to apply <code>monoid.exists_list_of_mem_closure</code> everywhere you see monoid.closure in hL1</p>

#### [ Patrick Massot (Oct 09 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500500):
<p>of course it's already beyond my Lean fu, because of the binder</p>

#### [ Patrick Massot (Oct 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500566):
<p>and this get you get your list of lists</p>

#### [ Patrick Massot (Oct 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500573):
<p>except for the substractions</p>

#### [ Patrick Massot (Oct 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500579):
<p>I guess my statement is wrong</p>

#### [ Patrick Massot (Oct 09 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500610):
<p>no, it's ok</p>

#### [ Reid Barton (Oct 09 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500677):
<p>I think it is wrong, because of -1. <code>s</code> could even be empty.</p>

#### [ Patrick Massot (Oct 09 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500702):
<p>edge cases...</p>

#### [ Patrick Massot (Oct 09 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500707):
<p>who cares about those?</p>

#### [ Patrick Massot (Oct 09 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500809):
<p>I clearly need to sleep though. I'm sure the <code>Kenny</code> tactic can fix the statement while writing the proof</p>

#### [ Kenny Lau (Oct 09 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500845):
<p>of what?</p>

#### [ Patrick Massot (Oct 09 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135501115):
<p><code>ring.exists_list_of_mem_closure</code></p>

#### [ Kenny Lau (Oct 26 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534435):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">ring_theory</span><span class="bp">.</span><span class="n">subring</span>

<span class="kn">universe</span> <span class="n">u</span>

<span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">add_monoid</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">add_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span>
  <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">add_monoid</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">C</span> <span class="mi">0</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H3</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">add_monoid</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">add_monoid</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">))</span> <span class="o">:</span>
  <span class="n">C</span> <span class="n">a</span> <span class="o">:=</span>
<span class="n">monoid</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">H</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">H1</span><span class="o">)</span> <span class="n">H2</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">H3</span><span class="o">)</span>

<span class="bp">@</span><span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">C</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span>
  <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">C</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">H3</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="bp">-</span><span class="n">a</span><span class="o">))</span>
  <span class="o">(</span><span class="n">H4</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">C</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">C</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">))</span> <span class="o">:</span>
  <span class="n">C</span> <span class="n">a</span> <span class="o">:=</span>
<span class="n">group</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">H</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">H1</span><span class="o">)</span> <span class="n">H2</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">H3</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">H4</span><span class="o">)</span>

<span class="kn">instance</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_hom</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">cast</span> <span class="o">:</span> <span class="bp">ℤ</span> <span class="bp">→</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">int</span><span class="bp">.</span><span class="n">cast_one</span><span class="o">,</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_mul</span><span class="o">,</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_add</span><span class="bp">⟩</span>

<span class="kn">instance</span> <span class="n">int</span><span class="bp">.</span><span class="n">coe_hom</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">coe</span> <span class="o">:</span> <span class="bp">ℤ</span> <span class="bp">→</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">int</span><span class="bp">.</span><span class="n">cast_one</span><span class="o">,</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_mul</span><span class="o">,</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_add</span><span class="bp">⟩</span>

<span class="kn">namespace</span> <span class="n">comm_ring</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span>

<span class="n">def</span> <span class="n">closure</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">closure</span> <span class="o">(</span><span class="n">monoid</span><span class="bp">.</span><span class="n">closure</span> <span class="n">s</span><span class="o">)</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">closure</span>

<span class="kn">theorem</span> <span class="n">exists_list_of_mem_closure</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">R</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">R</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">closure</span> <span class="n">s</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">∃</span> <span class="n">L</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">list</span> <span class="n">R</span><span class="o">),</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">l</span> <span class="err">∈</span> <span class="n">L</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">l</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">∨</span> <span class="bp">-</span><span class="n">x</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">-</span><span class="mi">1</span><span class="o">:</span><span class="n">R</span><span class="o">))</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">L</span><span class="bp">.</span><span class="n">map</span> <span class="n">list</span><span class="bp">.</span><span class="n">prod</span><span class="o">)</span><span class="bp">.</span><span class="n">sum</span> <span class="bp">=</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">add_group</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">h</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">hx</span><span class="o">,</span> <span class="k">match</span> <span class="n">x</span><span class="o">,</span> <span class="n">monoid</span><span class="bp">.</span><span class="n">exists_list_of_mem_closure</span> <span class="n">hx</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">L</span><span class="o">,</span> <span class="n">h1</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="o">[</span><span class="n">L</span><span class="o">],</span> <span class="n">list</span><span class="bp">.</span><span class="n">forall_mem_singleton</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">r</span> <span class="n">hr</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="o">(</span><span class="n">h1</span> <span class="n">r</span> <span class="n">hr</span><span class="o">)),</span> <span class="n">zero_add</span> <span class="bp">_⟩</span>
    <span class="kn">end</span><span class="o">)</span>
  <span class="bp">⟨</span><span class="o">[],</span> <span class="n">list</span><span class="bp">.</span><span class="n">forall_mem_nil</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span> <span class="bp">_</span> <span class="n">ih</span><span class="o">,</span> <span class="k">match</span> <span class="n">b</span><span class="o">,</span> <span class="n">ih</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">L1</span><span class="o">,</span> <span class="n">h1</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">L1</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">cons</span> <span class="o">(</span><span class="bp">-</span><span class="mi">1</span><span class="o">)),</span>
      <span class="bp">λ</span> <span class="n">L2</span> <span class="n">h2</span><span class="o">,</span> <span class="k">match</span> <span class="n">L2</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">mem_map</span><span class="bp">.</span><span class="mi">1</span> <span class="n">h2</span> <span class="k">with</span>
        <span class="bp">|</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">L3</span><span class="o">,</span> <span class="n">h3</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">list</span><span class="bp">.</span><span class="n">forall_mem_cons</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="err">$</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">rfl</span><span class="o">,</span> <span class="n">h1</span> <span class="n">L3</span> <span class="n">h3</span><span class="bp">⟩</span>
        <span class="kn">end</span><span class="o">,</span>
      <span class="k">by</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">list</span><span class="bp">.</span><span class="n">map_map</span><span class="o">,</span> <span class="o">(</span><span class="err">∘</span><span class="o">),</span> <span class="n">list</span><span class="bp">.</span><span class="n">prod_cons</span><span class="o">,</span> <span class="n">neg_one_mul</span><span class="o">]</span><span class="bp">;</span>
      <span class="n">exact</span> <span class="n">list</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">L1</span> <span class="n">neg_zero</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">hd</span> <span class="n">tl</span> <span class="n">ih</span><span class="o">,</span>
        <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">list</span><span class="bp">.</span><span class="n">map_cons</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">sum_cons</span><span class="o">,</span> <span class="n">ih</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">map_cons</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">sum_cons</span><span class="o">,</span> <span class="n">neg_add</span><span class="o">])</span><span class="bp">⟩</span>
    <span class="kn">end</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">r1</span> <span class="n">r2</span> <span class="n">hr1</span> <span class="n">hr2</span> <span class="n">ih1</span> <span class="n">ih2</span><span class="o">,</span> <span class="k">match</span> <span class="n">r1</span><span class="o">,</span> <span class="n">r2</span><span class="o">,</span> <span class="n">ih1</span><span class="o">,</span> <span class="n">ih2</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">L1</span><span class="o">,</span> <span class="n">h1</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">L2</span><span class="o">,</span> <span class="n">h2</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">L1</span> <span class="bp">++</span> <span class="n">L2</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">forall_mem_append</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">h1</span><span class="o">,</span> <span class="n">h2</span><span class="bp">⟩</span><span class="o">,</span>
      <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">list</span><span class="bp">.</span><span class="n">map_append</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">sum_append</span><span class="o">]</span><span class="bp">⟩</span>
    <span class="kn">end</span><span class="o">)</span>

<span class="kn">instance</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">R</span><span class="o">}</span> <span class="o">:</span> <span class="n">is_subring</span> <span class="o">(</span><span class="n">closure</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">zero_mem</span> <span class="o">:=</span> <span class="n">is_add_submonoid</span><span class="bp">.</span><span class="n">zero_mem</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">add_mem</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">ha</span> <span class="n">hb</span><span class="o">,</span> <span class="n">is_add_submonoid</span><span class="bp">.</span><span class="n">add_mem</span> <span class="n">ha</span> <span class="n">hb</span><span class="o">,</span>
  <span class="n">neg_mem</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">h</span><span class="o">,</span> <span class="n">is_add_subgroup</span><span class="bp">.</span><span class="n">neg_mem</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">one_mem</span> <span class="o">:=</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">mem_closure</span> <span class="o">(</span><span class="n">is_submonoid</span><span class="bp">.</span><span class="n">one_mem</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">mul_mem</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">ha</span> <span class="n">hb</span><span class="o">,</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">hb</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span> <span class="n">hb</span><span class="o">,</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">in_closure</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">ha</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">ha</span><span class="o">,</span> <span class="n">add_group</span><span class="bp">.</span><span class="n">subset_closure</span> <span class="o">(</span><span class="n">is_submonoid</span><span class="bp">.</span><span class="n">mul_mem</span> <span class="n">ha</span> <span class="n">hb</span><span class="o">))</span>
      <span class="o">((</span><span class="n">zero_mul</span> <span class="n">b</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">is_add_submonoid</span><span class="bp">.</span><span class="n">zero_mem</span> <span class="bp">_</span><span class="o">)</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">ha</span> <span class="n">hab</span><span class="o">,</span> <span class="o">(</span><span class="n">neg_mul_eq_neg_mul</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="bp">▸</span> <span class="n">is_add_subgroup</span><span class="bp">.</span><span class="n">neg_mem</span> <span class="n">hab</span><span class="o">)</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">c</span> <span class="n">ha</span> <span class="n">hc</span> <span class="n">hab</span> <span class="n">hcb</span><span class="o">,</span> <span class="o">(</span><span class="n">add_mul</span> <span class="n">a</span> <span class="n">c</span> <span class="n">b</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">is_add_submonoid</span><span class="bp">.</span><span class="n">add_mem</span> <span class="n">hab</span> <span class="n">hcb</span><span class="o">))</span>
    <span class="o">((</span><span class="n">mul_zero</span> <span class="n">a</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">is_add_submonoid</span><span class="bp">.</span><span class="n">zero_mem</span> <span class="bp">_</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span> <span class="n">hb</span> <span class="n">hab</span><span class="o">,</span> <span class="o">(</span><span class="n">neg_mul_eq_mul_neg</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="bp">▸</span> <span class="n">is_add_subgroup</span><span class="bp">.</span><span class="n">neg_mem</span> <span class="n">hab</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">b</span> <span class="n">c</span> <span class="n">hb</span> <span class="n">hc</span> <span class="n">hab</span> <span class="n">hac</span><span class="o">,</span> <span class="o">(</span><span class="n">mul_add</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">is_add_submonoid</span><span class="bp">.</span><span class="n">add_mem</span> <span class="n">hab</span> <span class="n">hac</span><span class="o">)</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">comm_ring</span>
</pre></div>

#### [ Kenny Lau (Oct 26 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534452):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> will you PR this?</p>

#### [ Patrick Massot (Oct 26 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534702):
<p>I can do it if you don't want to do it</p>

#### [ Patrick Massot (Oct 26 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534707):
<p>But it would make more sense if you do it yourself</p>

#### [ Patrick Massot (Oct 26 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534710):
<p>otherwise git won't credit you</p>

#### [ Kenny Lau (Oct 26 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534715):
<p>where should I put it?</p>

#### [ Patrick Massot (Oct 26 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534762):
<p>Maybe in the subgroup and subring files?</p>

#### [ Kenny Lau (Oct 26 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534767):
<p>maybe it'll just go to limbo like <a href="https://github.com/leanprover/mathlib/pull/425" target="_blank" title="https://github.com/leanprover/mathlib/pull/425">https://github.com/leanprover/mathlib/pull/425</a></p>

#### [ Patrick Massot (Oct 26 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534791):
<p>This is much smaller scope</p>

#### [ Patrick Massot (Oct 26 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534800):
<p>It should be an easy merge</p>

#### [ Kenny Lau (Oct 28 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136646441):
<p><a href="https://github.com/leanprover/mathlib/pull/444" target="_blank" title="https://github.com/leanprover/mathlib/pull/444">https://github.com/leanprover/mathlib/pull/444</a></p>

#### [ Kenny Lau (Oct 28 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136646444):
<p>done <span class="user-mention" data-user-id="110031">@Patrick Massot</span></p>


{% endraw %}
