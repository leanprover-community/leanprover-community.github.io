---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56604tacticunfreezelocalinstances.html
---

## Stream: [general](index.html)
### Topic: [tactic.unfreeze_local_instances](56604tacticunfreezelocalinstances.html)

---


{% raw %}
#### [ Kenny Lau (Oct 28 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136670895):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_space</span>
<span class="kn">universe</span> <span class="n">u</span>
<span class="kn">open</span> <span class="n">set</span>
<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>
<span class="n">class</span> <span class="n">t0_space</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">t0</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">y</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">U</span><span class="o">:</span><span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">is_open</span> <span class="n">U</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">xor</span> <span class="o">(</span><span class="n">x</span> <span class="err">∈</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span> <span class="err">∈</span> <span class="n">U</span><span class="o">)))</span>

<span class="kn">theorem</span> <span class="n">exists_open_singleton_of_fintype</span>
  <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">t0_space</span> <span class="n">α</span><span class="o">]</span>
  <span class="o">[</span><span class="n">f</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">ha</span> <span class="o">:</span> <span class="n">nonempty</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span>
  <span class="bp">∃</span> <span class="n">x</span><span class="o">:</span><span class="n">α</span><span class="o">,</span> <span class="n">is_open</span> <span class="o">({</span><span class="n">x</span><span class="o">}:</span><span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">T</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">),</span> <span class="n">T</span> <span class="bp">≠</span> <span class="err">∅</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">T</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">u</span><span class="o">,</span> <span class="n">is_open</span> <span class="n">u</span> <span class="bp">∧</span> <span class="o">{</span><span class="n">x</span><span class="o">}</span> <span class="bp">=</span> <span class="o">{</span><span class="n">y</span> <span class="bp">|</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">T</span><span class="o">}</span> <span class="err">∩</span> <span class="n">u</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">T</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">finset</span><span class="bp">.</span><span class="n">case_strong_induction_on</span> <span class="n">T</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">h</span><span class="o">,</span> <span class="n">exact</span> <span class="o">(</span><span class="n">h</span> <span class="n">rfl</span><span class="o">)</span><span class="bp">.</span><span class="n">elim</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">intros</span> <span class="n">x</span> <span class="n">S</span> <span class="n">hxS</span> <span class="n">ih</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">by_cases</span> <span class="n">hs</span> <span class="o">:</span> <span class="n">S</span> <span class="bp">=</span> <span class="err">∅</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">existsi</span> <span class="o">[</span><span class="n">x</span><span class="o">,</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_insert_self</span> <span class="n">x</span> <span class="n">S</span><span class="o">,</span> <span class="n">univ</span><span class="o">,</span> <span class="n">is_open_univ</span><span class="o">],</span>
      <span class="n">rw</span> <span class="o">[</span><span class="n">hs</span><span class="o">,</span> <span class="n">inter_univ</span><span class="o">],</span> <span class="n">refl</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">rcases</span> <span class="n">ih</span> <span class="n">S</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">refl</span> <span class="n">S</span><span class="o">)</span> <span class="n">hs</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">hy</span><span class="o">,</span> <span class="n">V</span><span class="o">,</span> <span class="n">hv1</span><span class="o">,</span> <span class="n">hv2</span><span class="bp">⟩</span><span class="o">,</span>
      <span class="n">by_cases</span> <span class="n">hxV</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">V</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">cases</span> <span class="n">t0_space</span><span class="bp">.</span><span class="n">t0</span> <span class="n">x</span> <span class="n">y</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">hxy</span><span class="o">,</span> <span class="n">hxS</span> <span class="err">$</span> <span class="k">by</span> <span class="n">rwa</span> <span class="n">hxy</span><span class="o">)</span> <span class="k">with</span> <span class="n">U</span> <span class="n">hu</span><span class="o">,</span>
        <span class="n">rcases</span> <span class="n">hu</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">hu1</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">hu2</span><span class="o">,</span> <span class="n">hu3</span><span class="bp">⟩</span> <span class="bp">|</span> <span class="bp">⟨</span><span class="n">hu2</span><span class="o">,</span> <span class="n">hu3</span><span class="bp">⟩⟩</span><span class="o">,</span>
        <span class="o">{</span> <span class="n">existsi</span> <span class="o">[</span><span class="n">x</span><span class="o">,</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_insert_self</span> <span class="n">x</span> <span class="n">S</span><span class="o">,</span> <span class="n">U</span> <span class="err">∩</span> <span class="n">V</span><span class="o">,</span> <span class="n">is_open_inter</span> <span class="n">hu1</span> <span class="n">hv1</span><span class="o">],</span>
          <span class="n">apply</span> <span class="n">set</span><span class="bp">.</span><span class="n">ext</span><span class="o">,</span>
          <span class="n">intro</span> <span class="n">z</span><span class="o">,</span>
          <span class="n">split</span><span class="o">,</span>
          <span class="o">{</span> <span class="n">intro</span> <span class="n">hzx</span><span class="o">,</span>
            <span class="n">rw</span> <span class="n">set</span><span class="bp">.</span><span class="n">mem_singleton_iff</span> <span class="n">at</span> <span class="n">hzx</span><span class="o">,</span>
            <span class="n">rw</span> <span class="n">hzx</span><span class="o">,</span>
            <span class="n">exact</span> <span class="bp">⟨</span><span class="n">finset</span><span class="bp">.</span><span class="n">mem_insert_self</span> <span class="n">x</span> <span class="n">S</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">hu2</span><span class="o">,</span> <span class="n">hxV</span><span class="bp">⟩⟩</span> <span class="o">},</span>
          <span class="o">{</span> <span class="n">intro</span> <span class="n">hz</span><span class="o">,</span>
            <span class="n">rw</span> <span class="n">set</span><span class="bp">.</span><span class="n">mem_singleton_iff</span><span class="o">,</span>
            <span class="n">rcases</span> <span class="n">hz</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">hz1</span><span class="o">,</span> <span class="n">hz2</span><span class="o">,</span> <span class="n">hz3</span><span class="bp">⟩</span><span class="o">,</span>
            <span class="n">cases</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_insert</span><span class="bp">.</span><span class="mi">1</span> <span class="n">hz1</span> <span class="k">with</span> <span class="n">hz4</span> <span class="n">hz4</span><span class="o">,</span>
            <span class="o">{</span> <span class="n">exact</span> <span class="n">hz4</span> <span class="o">},</span>
            <span class="o">{</span> <span class="k">have</span> <span class="n">h1</span> <span class="o">:</span> <span class="n">z</span> <span class="err">∈</span> <span class="o">{</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">|</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">S</span><span class="o">}</span> <span class="err">∩</span> <span class="n">V</span><span class="o">,</span>
              <span class="o">{</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="n">hz4</span><span class="o">,</span> <span class="n">hz3</span><span class="bp">⟩</span> <span class="o">},</span>
              <span class="n">rw</span> <span class="err">←</span> <span class="n">hv2</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
              <span class="n">rw</span> <span class="n">set</span><span class="bp">.</span><span class="n">mem_singleton_iff</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
              <span class="n">rw</span> <span class="n">h1</span> <span class="n">at</span> <span class="n">hz2</span><span class="o">,</span>
              <span class="n">exact</span> <span class="o">(</span><span class="n">hu3</span> <span class="n">hz2</span><span class="o">)</span><span class="bp">.</span><span class="n">elim</span> <span class="o">}</span> <span class="o">}</span> <span class="o">},</span>
        <span class="o">{</span> <span class="n">existsi</span> <span class="o">[</span><span class="n">y</span><span class="o">,</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_insert_of_mem</span> <span class="n">hy</span><span class="o">,</span> <span class="n">U</span> <span class="err">∩</span> <span class="n">V</span><span class="o">,</span> <span class="n">is_open_inter</span> <span class="n">hu1</span> <span class="n">hv1</span><span class="o">],</span>
          <span class="n">apply</span> <span class="n">set</span><span class="bp">.</span><span class="n">ext</span><span class="o">,</span>
          <span class="n">intro</span> <span class="n">z</span><span class="o">,</span>
          <span class="n">split</span><span class="o">,</span>
          <span class="o">{</span> <span class="n">intro</span> <span class="n">hz</span><span class="o">,</span>
            <span class="n">rw</span> <span class="n">set</span><span class="bp">.</span><span class="n">mem_singleton_iff</span> <span class="n">at</span> <span class="n">hz</span><span class="o">,</span>
            <span class="n">rw</span> <span class="n">hz</span><span class="o">,</span>
            <span class="n">refine</span> <span class="bp">⟨</span><span class="n">finset</span><span class="bp">.</span><span class="n">mem_insert_of_mem</span> <span class="n">hy</span><span class="o">,</span> <span class="n">hu2</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">,</span>
            <span class="k">have</span> <span class="n">h1</span> <span class="o">:</span> <span class="n">y</span> <span class="err">∈</span> <span class="o">{</span><span class="n">y</span><span class="o">}</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">mem_singleton</span> <span class="n">y</span><span class="o">,</span>
            <span class="n">rw</span> <span class="n">hv2</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
            <span class="n">exact</span> <span class="n">h1</span><span class="bp">.</span><span class="mi">2</span> <span class="o">},</span>
          <span class="o">{</span> <span class="n">intro</span> <span class="n">hz</span><span class="o">,</span>
            <span class="n">rw</span> <span class="n">set</span><span class="bp">.</span><span class="n">mem_singleton_iff</span><span class="o">,</span>
            <span class="n">cases</span> <span class="n">hz</span> <span class="k">with</span> <span class="n">hz1</span> <span class="n">hz2</span><span class="o">,</span>
            <span class="n">cases</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_insert</span><span class="bp">.</span><span class="mi">1</span> <span class="n">hz1</span> <span class="k">with</span> <span class="n">hz3</span> <span class="n">hz3</span><span class="o">,</span>
            <span class="o">{</span> <span class="n">rw</span> <span class="n">hz3</span> <span class="n">at</span> <span class="n">hz2</span><span class="o">,</span>
              <span class="n">exact</span> <span class="o">(</span><span class="n">hu3</span> <span class="n">hz2</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span><span class="bp">.</span><span class="n">elim</span> <span class="o">},</span>
            <span class="o">{</span> <span class="k">have</span> <span class="n">h1</span> <span class="o">:</span> <span class="n">z</span> <span class="err">∈</span> <span class="o">{</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">|</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">S</span><span class="o">}</span> <span class="err">∩</span> <span class="n">V</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">hz3</span><span class="o">,</span> <span class="n">hz2</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
              <span class="n">rw</span> <span class="err">←</span> <span class="n">hv2</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
              <span class="n">rw</span> <span class="n">set</span><span class="bp">.</span><span class="n">mem_singleton_iff</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
              <span class="n">exact</span> <span class="n">h1</span> <span class="o">}</span> <span class="o">}</span> <span class="o">}</span> <span class="o">},</span>
      <span class="o">{</span> <span class="n">existsi</span> <span class="o">[</span><span class="n">y</span><span class="o">,</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_insert_of_mem</span> <span class="n">hy</span><span class="o">,</span> <span class="n">V</span><span class="o">,</span> <span class="n">hv1</span><span class="o">],</span>
        <span class="n">apply</span> <span class="n">set</span><span class="bp">.</span><span class="n">ext</span><span class="o">,</span>
        <span class="n">intro</span> <span class="n">z</span><span class="o">,</span>
        <span class="n">split</span><span class="o">,</span>
        <span class="o">{</span> <span class="n">intro</span> <span class="n">hz</span><span class="o">,</span>
          <span class="n">rw</span> <span class="n">set</span><span class="bp">.</span><span class="n">mem_singleton_iff</span> <span class="n">at</span> <span class="n">hz</span><span class="o">,</span>
          <span class="n">rw</span> <span class="n">hz</span><span class="o">,</span>
          <span class="n">split</span><span class="o">,</span>
          <span class="o">{</span> <span class="n">exact</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_insert_of_mem</span> <span class="n">hy</span> <span class="o">},</span>
          <span class="o">{</span> <span class="k">have</span> <span class="n">h1</span> <span class="o">:</span> <span class="n">y</span> <span class="err">∈</span> <span class="o">{</span><span class="n">y</span><span class="o">}</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">mem_singleton</span> <span class="n">y</span><span class="o">,</span>
            <span class="n">rw</span> <span class="n">hv2</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
            <span class="n">exact</span> <span class="n">h1</span><span class="bp">.</span><span class="mi">2</span> <span class="o">}</span> <span class="o">},</span>
        <span class="o">{</span> <span class="n">intro</span> <span class="n">hz</span><span class="o">,</span>
          <span class="n">rw</span> <span class="n">hv2</span><span class="o">,</span>
          <span class="n">cases</span> <span class="n">hz</span> <span class="k">with</span> <span class="n">hz1</span> <span class="n">hz2</span><span class="o">,</span>
          <span class="n">cases</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_insert</span><span class="bp">.</span><span class="mi">1</span> <span class="n">hz1</span> <span class="k">with</span> <span class="n">hz3</span> <span class="n">hz3</span><span class="o">,</span>
          <span class="o">{</span> <span class="n">rw</span> <span class="n">hz3</span> <span class="n">at</span> <span class="n">hz2</span><span class="o">,</span>
            <span class="n">exact</span> <span class="o">(</span><span class="n">hxV</span> <span class="n">hz2</span><span class="o">)</span><span class="bp">.</span><span class="n">elim</span> <span class="o">},</span>
          <span class="o">{</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="n">hz3</span><span class="o">,</span> <span class="n">hz2</span><span class="bp">⟩</span> <span class="o">}</span> <span class="o">}</span> <span class="o">}</span> <span class="o">}</span> <span class="o">}</span>
<span class="kn">end</span><span class="o">,</span>
<span class="k">begin</span>
  <span class="n">tactic</span><span class="bp">.</span><span class="n">unfreeze_local_instances</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">ha</span> <span class="k">with</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">specialize</span> <span class="n">H</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">ne_empty_of_mem</span> <span class="err">$</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_univ</span> <span class="n">x</span><span class="o">),</span>
  <span class="n">rcases</span> <span class="n">H</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">hyf</span><span class="o">,</span> <span class="n">U</span><span class="o">,</span> <span class="n">hu1</span><span class="o">,</span> <span class="n">hu2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="n">y</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">h1</span> <span class="o">:</span> <span class="o">{</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">|</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span><span class="o">}</span> <span class="bp">=</span> <span class="o">(</span><span class="n">univ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">),</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="n">set</span><span class="bp">.</span><span class="n">eq_univ_of_forall</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span>
      <span class="k">by</span> <span class="n">rw</span> <span class="n">mem_set_of_eq</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">finset</span><span class="bp">.</span><span class="n">mem_univ</span> <span class="n">x</span><span class="o">)</span> <span class="o">},</span>
  <span class="n">rw</span> <span class="n">h1</span> <span class="n">at</span> <span class="n">hu2</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">set</span><span class="bp">.</span><span class="n">univ_inter</span> <span class="n">at</span> <span class="n">hu2</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">hu2</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">hu1</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Oct 28 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136670896):
<p>Why do I need <code>tactic.unfreeze_local_instances</code> there?</p>

#### [ Kenny Lau (Oct 28 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136670937):
<p>(working example, but clearly not minimal)</p>

#### [ Mario Carneiro (Oct 28 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136671127):
<p>because it's a typeclas arg left of the colon</p>

#### [ Mario Carneiro (Oct 28 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136671141):
<p>you can use <code>unfreezeI</code> for short</p>

#### [ Kenny Lau (Oct 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136671337):
<p>I don't understand</p>

#### [ Kenny Lau (Oct 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136671338):
<p>isn't every typeclass argument left of colon?</p>

#### [ Chris Hughes (Oct 28 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136672307):
<p>You don't usually do <code>cases </code> on type class args</p>

#### [ Kenny Lau (Oct 28 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136672310):
<p>yeah even if I don't do cases it still messes up</p>

#### [ Mario Carneiro (Oct 28 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136672815):
<p>anything that disrupts the context past the position of the colon will require <code>unfreezeI</code></p>

#### [ Mario Carneiro (Oct 28 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136672827):
<p>in this case you can do <code>cases id ha with a</code> if you don't want to clear the hypothesis in the context</p>

#### [ Kenny Lau (Oct 28 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136672869):
<p>oh, I get it now</p>

#### [ Kenny Lau (Oct 28 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136672878):
<p>oh and how would you golf the proof?</p>

#### [ Mario Carneiro (Oct 28 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136672888):
<p>I've been thinking about that... that proof is a little scary long</p>

#### [ Mario Carneiro (Oct 28 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136672900):
<p>Maybe you can find a maximal element in the specialization preorder?</p>

#### [ Kenny Lau (Oct 28 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673208):
<p>I don't understand what you mean by the specialization preorder</p>

#### [ Mario Carneiro (Oct 28 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673248):
<p>okay, I refreshed my memory on the <a href="https://en.wikipedia.org/wiki/Specialization_(pre)order" target="_blank" title="https://en.wikipedia.org/wiki/Specialization_(pre)order">specialization preorder</a> and indeed this proof should work (although it is a minimal element by wiki's definition)</p>

#### [ Mario Carneiro (Oct 28 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673257):
<p>it's basically finite zorn's lemma</p>

#### [ Kevin Buzzard (Oct 28 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673318):
<p>A point x specialises to a point y if y is in the closure of x</p>

#### [ Mario Carneiro (Oct 28 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673388):
<p>I think that's the reverse of wiki's terminology?</p>

#### [ Mario Carneiro (Oct 28 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673398):
<p>they say y is a specialization of x in that case</p>

#### [ Mario Carneiro (Oct 28 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673422):
<p>they also say that the orientation is contentious</p>

#### [ Kevin Buzzard (Oct 28 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673448):
<p>Darn Zulip app doesn't show me new posts when they arrive</p>

#### [ Kevin Buzzard (Oct 28 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673490):
<p>Including my own</p>

#### [ Kevin Buzzard (Oct 28 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673513):
<p>Right -- x specialises to y, so y is a specialisation of x.</p>

#### [ Mario Carneiro (Oct 28 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673520):
<p>okay, I wasn't sure about the active verb there</p>

#### [ Kevin Buzzard (Oct 29 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673587):
<p>This is how the words are used in algebraic geometry at least</p>

#### [ Mario Carneiro (Oct 29 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673661):
<p>You should look at the wiki page and decide which order of le makes sense</p>

#### [ Mario Carneiro (Oct 29 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136673675):
<p>I'm leaning to the first definition, <code>x &lt;= y</code> means x is a specialization of y, because the evidence from algebraic geometry using Spec R smacks of that order-reversing filter thing</p>

#### [ Reid Barton (Oct 29 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136674194):
<p>The ordering I have seen is the one which is equivalent to x \le y if closure({x}) is a subset of closure({y})</p>

#### [ Reid Barton (Oct 29 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136674320):
<p>Actually, I'm not sure which way it goes now and my source is at home</p>

#### [ Mario Carneiro (Oct 29 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136674734):
<p>I'm not sure why this argument doesn't extend to the infinite case by zorn's lemma though</p>

#### [ Mario Carneiro (Oct 29 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136674742):
<p>Obviously it's not true for R so I'm missing a part of the argument</p>

#### [ Kenny Lau (Oct 29 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136680702):
<p><a href="https://github.com/leanprover/mathlib/pull/448" target="_blank" title="https://github.com/leanprover/mathlib/pull/448">https://github.com/leanprover/mathlib/pull/448</a></p>

#### [ Kevin Buzzard (Oct 29 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136690249):
<blockquote>
<p>Obviously it's not true for R so I'm missing a part of the argument</p>
</blockquote>
<p>For sensible spaces like R the preorder is just "x&lt;=y iff x=y". So there are maximal and minimal elements, but these do not correspond to open singletons.</p>

#### [ Reid Barton (Oct 29 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136702815):
<p>Okay, the paper where I've encountered this actually says "... so that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mo>≤</mo><mi>X</mi></msub></mrow><annotation encoding="application/x-tex">\le_X</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.63597em;"></span><span class="strut bottom" style="height:0.7859700000000001em;vertical-align:-0.15em;"></span><span class="base"><span class="mrel"><span class="mrel">≤</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.32833099999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.07847em;">X</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> is the well-known [4] reflexive and transitive relation <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>y</mi><mo>∈</mo><mo>{</mo><mi>x</mi><msup><mo>}</mo><mo>−</mo></msup></mrow><annotation encoding="application/x-tex">y \in \{x\}^-</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.771331em;"></span><span class="strut bottom" style="height:1.021331em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mrel">∈</span><span class="mopen">{</span><span class="mord mathit">x</span><span class="mclose"><span class="mclose">}</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.771331em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">−</span></span></span></span></span></span></span></span></span></span></span>", so I did have this backwards.</p>

#### [ Reid Barton (Oct 29 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136708004):
<p>After being confused by this for a while, my conclusion is that the "<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi></mrow><annotation encoding="application/x-tex">x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">x</span></span></span></span> specializes to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>y</mi></mrow><annotation encoding="application/x-tex">y</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">y</span></span></span></span>" relation is actually different in algebraic geometry and in domain theory</p>

#### [ Reid Barton (Oct 29 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136708039):
<p>one of them has to do with closed sets, the other with open sets</p>

#### [ Reid Barton (Oct 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136708108):
<p>Because of the duality between open and closed sets, this appears as a reversal of the order</p>

#### [ Kevin Buzzard (Oct 29 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.unfreeze_local_instances/near/136715016):
<p>In algebraic geometry, a "generic point" of an irreducible algebraic variety is a rigorous notion of the intuitive idea of how a general point on the variety behaves. Historically this was done in a vague way -- we had the "actual points" and then "it's true for a generic point" just meant "most points satisfy this" with several, sometimes competing definitions of "most", but with Grothendieck's approach we have the luxury of the generic point actually being a point in the top space, whose topological closure is the entire variety. The idea is that a generic point can specialise to a random "actual point", which is then a specialisation of the generic point. Perhaps the simplest example of this is the two-point topological space with one closed and one open point. A fruitful mental model of this space in geometry is that the whole space is the open unit disc, the closed point is the origin, and the open point is all the other points --  a "general" point in the open disc. If <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>η</mi></mrow><annotation encoding="application/x-tex">\eta</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">η</span></span></span></span> is the generic point and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>s</mi></mrow><annotation encoding="application/x-tex">s</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">s</span></span></span></span> the closed point then the sequence <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>η</mi><mo separator="true">,</mo><mi>η</mi><mo separator="true">,</mo><mi>η</mi><mo separator="true">,</mo><mo>…</mo></mrow><annotation encoding="application/x-tex">\eta,\eta,\eta,\ldots</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">η</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.03588em;">η</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.03588em;">η</span><span class="mpunct">,</span><span class="minner">…</span></span></span></span> converges to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>s</mi></mrow><annotation encoding="application/x-tex">s</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">s</span></span></span></span> (as well as to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>η</mi></mrow><annotation encoding="application/x-tex">\eta</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">η</span></span></span></span>), which is the specialisation in action. One cna think of it as a bunch of points in the punctured disc tending to the origin.</p>


{% endraw %}
