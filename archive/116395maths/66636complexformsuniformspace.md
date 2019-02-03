---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/66636complexformsuniformspace.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [complex forms uniform space](https://leanprover-community.github.io/archive/116395maths/66636complexformsuniformspace.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Oct 05 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135222007):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">real</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">complex</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj_sub</span> <span class="o">(</span><span class="n">z</span> <span class="n">w</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj</span> <span class="o">(</span><span class="n">z</span> <span class="bp">-</span> <span class="n">w</span><span class="o">)</span> <span class="bp">=</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj</span> <span class="n">z</span> <span class="bp">-</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj</span> <span class="n">w</span> <span class="o">:=</span>
<span class="n">complex</span><span class="bp">.</span><span class="n">conj_add</span> <span class="bp">_</span> <span class="bp">_</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_conj</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj</span> <span class="o">:=</span>
<span class="n">uniform_continuous_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span>
<span class="bp">λ</span> <span class="n">z</span> <span class="n">w</span> <span class="n">hzw</span><span class="o">,</span> <span class="k">show</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs</span> <span class="bp">_</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="o">,</span> <span class="k">by</span> <span class="n">rwa</span> <span class="o">[</span><span class="err">←</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj_sub</span><span class="o">,</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs_conj</span><span class="o">]</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_re</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">re</span> <span class="o">:=</span>
<span class="n">uniform_continuous_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">w</span> <span class="n">hzw</span><span class="o">,</span>
<span class="k">calc</span>  <span class="n">dist</span> <span class="n">z</span><span class="bp">.</span><span class="n">re</span> <span class="n">w</span><span class="bp">.</span><span class="n">re</span>
    <span class="bp">≤</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs</span> <span class="o">(</span><span class="n">z</span><span class="bp">-</span><span class="n">w</span><span class="o">)</span> <span class="o">:</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs_re_le_abs</span> <span class="o">(</span><span class="n">z</span><span class="bp">-</span><span class="n">w</span><span class="o">)</span>
<span class="bp">...</span> <span class="bp">&lt;</span> <span class="n">ε</span> <span class="o">:</span> <span class="n">hzw</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_im</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">im</span> <span class="o">:=</span>
<span class="n">uniform_continuous_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">w</span> <span class="n">hzw</span><span class="o">,</span>
<span class="k">calc</span>  <span class="n">dist</span> <span class="n">z</span><span class="bp">.</span><span class="n">im</span> <span class="n">w</span><span class="bp">.</span><span class="n">im</span>
    <span class="bp">≤</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs</span> <span class="o">(</span><span class="n">z</span><span class="bp">-</span><span class="n">w</span><span class="o">)</span> <span class="o">:</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs_im_le_abs</span> <span class="o">(</span><span class="n">z</span><span class="bp">-</span><span class="n">w</span><span class="o">)</span>
<span class="bp">...</span> <span class="bp">&lt;</span> <span class="n">ε</span> <span class="o">:</span> <span class="n">hzw</span><span class="bp">⟩</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">filter</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">cauchy</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="bp">≤</span> <span class="n">nhds</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">xr</span><span class="o">,</span> <span class="n">hxr</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">complete_space</span><span class="bp">.</span><span class="n">complete</span>
  <span class="o">(</span><span class="n">cauchy_map</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_re</span> <span class="n">hf</span><span class="o">)</span> <span class="k">in</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">xi</span><span class="o">,</span> <span class="n">hxi</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">complete_space</span><span class="bp">.</span><span class="n">complete</span>
  <span class="o">(</span><span class="n">cauchy_map</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_im</span> <span class="n">hf</span><span class="o">)</span> <span class="k">in</span>
<span class="bp">⟨⟨</span><span class="n">xr</span><span class="o">,</span> <span class="n">xi</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">sorry</span><span class="bp">⟩</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">state:</span>
<span class="cm">f : filter ℂ,</span>
<span class="cm">hf : cauchy f,</span>
<span class="cm">xr : ℝ,</span>
<span class="cm">hxr : filter.map complex.re f ≤ nhds xr,</span>
<span class="cm">xi : ℝ,</span>
<span class="cm">hxi : filter.map complex.im f ≤ nhds xi</span>
<span class="cm">⊢ f ≤ nhds {re := xr, im := xi}</span>
<span class="cm">-/</span>
</pre></div>


<p>half-completed proof</p>

#### [ Kenny Lau (Oct 05 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135222089):
<p><span class="user-mention" data-user-id="120943">@Andreas Swerdlow</span></p>

#### [ Kenny Lau (Oct 05 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135222945):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">real</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">complex</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj_sub</span> <span class="o">(</span><span class="n">z</span> <span class="n">w</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj</span> <span class="o">(</span><span class="n">z</span> <span class="bp">-</span> <span class="n">w</span><span class="o">)</span> <span class="bp">=</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj</span> <span class="n">z</span> <span class="bp">-</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj</span> <span class="n">w</span> <span class="o">:=</span>
<span class="n">complex</span><span class="bp">.</span><span class="n">conj_add</span> <span class="bp">_</span> <span class="bp">_</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_conj</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj</span> <span class="o">:=</span>
<span class="n">uniform_continuous_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span>
<span class="bp">λ</span> <span class="n">z</span> <span class="n">w</span> <span class="n">hzw</span><span class="o">,</span> <span class="k">show</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs</span> <span class="bp">_</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="o">,</span> <span class="k">by</span> <span class="n">rwa</span> <span class="o">[</span><span class="err">←</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj_sub</span><span class="o">,</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs_conj</span><span class="o">]</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_re</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">re</span> <span class="o">:=</span>
<span class="n">uniform_continuous_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">w</span> <span class="n">hzw</span><span class="o">,</span>
<span class="k">calc</span>  <span class="n">dist</span> <span class="n">z</span><span class="bp">.</span><span class="n">re</span> <span class="n">w</span><span class="bp">.</span><span class="n">re</span>
    <span class="bp">≤</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs</span> <span class="o">(</span><span class="n">z</span><span class="bp">-</span><span class="n">w</span><span class="o">)</span> <span class="o">:</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs_re_le_abs</span> <span class="o">(</span><span class="n">z</span><span class="bp">-</span><span class="n">w</span><span class="o">)</span>
<span class="bp">...</span> <span class="bp">&lt;</span> <span class="n">ε</span> <span class="o">:</span> <span class="n">hzw</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_im</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">im</span> <span class="o">:=</span>
<span class="n">uniform_continuous_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">w</span> <span class="n">hzw</span><span class="o">,</span>
<span class="k">calc</span>  <span class="n">dist</span> <span class="n">z</span><span class="bp">.</span><span class="n">im</span> <span class="n">w</span><span class="bp">.</span><span class="n">im</span>
    <span class="bp">≤</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs</span> <span class="o">(</span><span class="n">z</span><span class="bp">-</span><span class="n">w</span><span class="o">)</span> <span class="o">:</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs_im_le_abs</span> <span class="o">(</span><span class="n">z</span><span class="bp">-</span><span class="n">w</span><span class="o">)</span>
<span class="bp">...</span> <span class="bp">&lt;</span> <span class="n">ε</span> <span class="o">:</span> <span class="n">hzw</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_of_real</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">of_real</span> <span class="o">:=</span>
<span class="n">uniform_continuous_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">w</span> <span class="n">hzw</span><span class="o">,</span>
<span class="k">calc</span>  <span class="n">dist</span> <span class="o">(</span><span class="n">complex</span><span class="bp">.</span><span class="n">of_real</span> <span class="n">z</span><span class="o">)</span> <span class="o">(</span><span class="n">complex</span><span class="bp">.</span><span class="n">of_real</span> <span class="n">w</span><span class="o">)</span>
    <span class="bp">=</span> <span class="n">dist</span> <span class="n">z</span> <span class="n">w</span> <span class="o">:</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs_of_real</span> <span class="bp">_</span>
<span class="bp">...</span> <span class="bp">&lt;</span> <span class="n">ε</span> <span class="o">:</span> <span class="n">hzw</span><span class="bp">⟩</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">filter</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">cauchy</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="bp">≤</span> <span class="n">nhds</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">xr</span><span class="o">,</span> <span class="n">hxr</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">complete_space</span><span class="bp">.</span><span class="n">complete</span>
  <span class="o">(</span><span class="n">cauchy_map</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_re</span> <span class="n">hf</span><span class="o">)</span> <span class="k">in</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">xi</span><span class="o">,</span> <span class="n">hxi</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">complete_space</span><span class="bp">.</span><span class="n">complete</span>
  <span class="o">(</span><span class="n">cauchy_map</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_im</span> <span class="n">hf</span><span class="o">)</span> <span class="k">in</span>
<span class="k">have</span> <span class="n">hxr2</span> <span class="o">:</span> <span class="n">filter</span><span class="bp">.</span><span class="n">tendsto</span> <span class="o">(</span><span class="n">complex</span><span class="bp">.</span><span class="n">of_real</span> <span class="err">∘</span> <span class="n">complex</span><span class="bp">.</span><span class="n">re</span><span class="o">)</span> <span class="n">f</span> <span class="o">(</span><span class="n">nhds</span> <span class="o">(</span><span class="n">complex</span><span class="bp">.</span><span class="n">of_real</span> <span class="n">xr</span><span class="o">)),</span>
  <span class="k">from</span> <span class="n">filter</span><span class="bp">.</span><span class="n">tendsto</span><span class="bp">.</span><span class="n">comp</span> <span class="n">hxr</span> <span class="o">(</span><span class="n">continuous</span><span class="bp">.</span><span class="n">tendsto</span>
    <span class="o">(</span><span class="n">uniform_continuous</span><span class="bp">.</span><span class="n">continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_of_real</span><span class="o">)</span> <span class="n">xr</span><span class="o">),</span>
<span class="k">have</span> <span class="n">hxi2</span> <span class="o">:</span> <span class="n">filter</span><span class="bp">.</span><span class="n">tendsto</span> <span class="o">(</span><span class="n">complex</span><span class="bp">.</span><span class="n">of_real</span> <span class="err">∘</span> <span class="n">complex</span><span class="bp">.</span><span class="n">im</span><span class="o">)</span> <span class="n">f</span> <span class="o">(</span><span class="n">nhds</span> <span class="o">(</span><span class="n">complex</span><span class="bp">.</span><span class="n">of_real</span> <span class="n">xi</span><span class="o">)),</span>
  <span class="k">from</span> <span class="n">filter</span><span class="bp">.</span><span class="n">tendsto</span><span class="bp">.</span><span class="n">comp</span> <span class="n">hxi</span> <span class="o">(</span><span class="n">continuous</span><span class="bp">.</span><span class="n">tendsto</span>
    <span class="o">(</span><span class="n">uniform_continuous</span><span class="bp">.</span><span class="n">continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_of_real</span><span class="o">)</span> <span class="n">xi</span><span class="o">),</span>
<span class="k">have</span> <span class="n">filter</span><span class="bp">.</span><span class="n">tendsto</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span><span class="o">:</span><span class="n">ℂ</span><span class="o">,</span> <span class="o">(</span><span class="n">z</span><span class="bp">.</span><span class="n">re</span> <span class="bp">+</span> <span class="n">z</span><span class="bp">.</span><span class="n">im</span> <span class="bp">*</span> <span class="n">complex</span><span class="bp">.</span><span class="n">I</span><span class="o">:</span><span class="n">ℂ</span><span class="o">))</span> <span class="n">f</span> <span class="o">(</span><span class="n">nhds</span> <span class="bp">_</span><span class="o">),</span>
  <span class="k">from</span> <span class="n">tendsto_add</span> <span class="n">hxr2</span> <span class="o">(</span><span class="n">tendsto_mul</span> <span class="n">hxi2</span> <span class="o">(</span><span class="bp">@</span><span class="n">tendsto_const_nhds</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">complex</span><span class="bp">.</span><span class="n">I</span> <span class="bp">_</span><span class="o">)),</span>
<span class="bp">⟨</span><span class="o">(</span><span class="n">xr</span><span class="bp">+</span><span class="n">xi</span><span class="bp">*</span><span class="n">complex</span><span class="bp">.</span><span class="n">I</span><span class="o">),</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">funext</span> <span class="n">complex</span><span class="bp">.</span><span class="n">re_add_im</span><span class="o">]</span> <span class="n">at</span> <span class="n">this</span><span class="bp">;</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="o">(</span><span class="n">filter</span><span class="bp">.</span><span class="n">map_id</span> <span class="o">:</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">f</span><span class="o">)]</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">this</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Oct 05 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135222946):
<p>complete proof</p>

#### [ Andreas Swerdlow (Oct 05 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135224448):
<p>Wow thank you!</p>

#### [ Andreas Swerdlow (Oct 05 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135224468):
<p><span class="user-mention" data-user-id="122022">@Joseph Corneli</span> look what Kenny did</p>

#### [ Kenny Lau (Oct 05 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135224585):
<p>I should probably extract a lemma</p>

#### [ Mario Carneiro (Oct 05 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135224597):
<p>that proof looks like a good advertisement for bundling continuous functions</p>

#### [ Mario Carneiro (Oct 05 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135224662):
<p>For a while I was thinking that maybe we want to work with continuous functions as a predicate, but compositional proofs of continuity really suck from a readability standpoint</p>

#### [ Kenny Lau (Oct 05 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135224685):
<p>another thing to refactor :P</p>

#### [ Kenny Lau (Oct 05 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135225113):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">real</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">complex</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj_sub</span> <span class="o">(</span><span class="n">z</span> <span class="n">w</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj</span> <span class="o">(</span><span class="n">z</span> <span class="bp">-</span> <span class="n">w</span><span class="o">)</span> <span class="bp">=</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj</span> <span class="n">z</span> <span class="bp">-</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj</span> <span class="n">w</span> <span class="o">:=</span>
<span class="n">complex</span><span class="bp">.</span><span class="n">conj_add</span> <span class="bp">_</span> <span class="bp">_</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_conj</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj</span> <span class="o">:=</span>
<span class="n">uniform_continuous_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span>
<span class="bp">λ</span> <span class="n">z</span> <span class="n">w</span> <span class="n">hzw</span><span class="o">,</span> <span class="k">show</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs</span> <span class="bp">_</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="o">,</span> <span class="k">by</span> <span class="n">rwa</span> <span class="o">[</span><span class="err">←</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj_sub</span><span class="o">,</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs_conj</span><span class="o">]</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_re</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">re</span> <span class="o">:=</span>
<span class="n">uniform_continuous_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">w</span> <span class="n">hzw</span><span class="o">,</span>
<span class="k">calc</span>  <span class="n">dist</span> <span class="n">z</span><span class="bp">.</span><span class="n">re</span> <span class="n">w</span><span class="bp">.</span><span class="n">re</span>
    <span class="bp">≤</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs</span> <span class="o">(</span><span class="n">z</span><span class="bp">-</span><span class="n">w</span><span class="o">)</span> <span class="o">:</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs_re_le_abs</span> <span class="o">(</span><span class="n">z</span><span class="bp">-</span><span class="n">w</span><span class="o">)</span>
<span class="bp">...</span> <span class="bp">&lt;</span> <span class="n">ε</span> <span class="o">:</span> <span class="n">hzw</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_im</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">im</span> <span class="o">:=</span>
<span class="n">uniform_continuous_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">w</span> <span class="n">hzw</span><span class="o">,</span>
<span class="k">calc</span>  <span class="n">dist</span> <span class="n">z</span><span class="bp">.</span><span class="n">im</span> <span class="n">w</span><span class="bp">.</span><span class="n">im</span>
    <span class="bp">≤</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs</span> <span class="o">(</span><span class="n">z</span><span class="bp">-</span><span class="n">w</span><span class="o">)</span> <span class="o">:</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs_im_le_abs</span> <span class="o">(</span><span class="n">z</span><span class="bp">-</span><span class="n">w</span><span class="o">)</span>
<span class="bp">...</span> <span class="bp">&lt;</span> <span class="n">ε</span> <span class="o">:</span> <span class="n">hzw</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_of_real</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">of_real</span> <span class="o">:=</span>
<span class="n">uniform_continuous_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">w</span> <span class="n">hzw</span><span class="o">,</span>
<span class="k">calc</span>  <span class="n">dist</span> <span class="o">(</span><span class="n">complex</span><span class="bp">.</span><span class="n">of_real</span> <span class="n">z</span><span class="o">)</span> <span class="o">(</span><span class="n">complex</span><span class="bp">.</span><span class="n">of_real</span> <span class="n">w</span><span class="o">)</span>
    <span class="bp">=</span> <span class="n">dist</span> <span class="n">z</span> <span class="n">w</span> <span class="o">:</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs_of_real</span> <span class="bp">_</span>
<span class="bp">...</span> <span class="bp">&lt;</span> <span class="n">ε</span> <span class="o">:</span> <span class="n">hzw</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">continuous_conj</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">conj</span> <span class="o">:=</span>
<span class="n">uniform_continuous</span><span class="bp">.</span><span class="n">continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_conj</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">continuous_re</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">re</span> <span class="o">:=</span>
<span class="n">uniform_continuous</span><span class="bp">.</span><span class="n">continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_re</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">continuous_im</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">im</span> <span class="o">:=</span>
<span class="n">uniform_continuous</span><span class="bp">.</span><span class="n">continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_im</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">continuous_of_real</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">of_real</span> <span class="o">:=</span>
<span class="n">uniform_continuous</span><span class="bp">.</span><span class="n">continuous</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_of_real</span>

<span class="kn">theorem</span> <span class="n">complex</span><span class="bp">.</span><span class="n">filter_le_iff</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">filter</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">(</span><span class="n">z</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">f</span> <span class="bp">≤</span> <span class="n">nhds</span> <span class="n">z</span> <span class="bp">↔</span> <span class="n">filter</span><span class="bp">.</span><span class="n">tendsto</span> <span class="n">complex</span><span class="bp">.</span><span class="n">re</span> <span class="n">f</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">z</span><span class="bp">.</span><span class="n">re</span><span class="o">)</span> <span class="bp">∧</span> <span class="n">filter</span><span class="bp">.</span><span class="n">tendsto</span> <span class="n">complex</span><span class="bp">.</span><span class="n">im</span> <span class="n">f</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">z</span><span class="bp">.</span><span class="n">im</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">h</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">le_trans</span> <span class="o">(</span><span class="n">filter</span><span class="bp">.</span><span class="n">map_mono</span> <span class="n">h</span><span class="o">)</span>
    <span class="o">(</span><span class="n">continuous</span><span class="bp">.</span><span class="n">tendsto</span> <span class="n">complex</span><span class="bp">.</span><span class="n">continuous_re</span> <span class="n">z</span><span class="o">),</span>
  <span class="n">le_trans</span> <span class="o">(</span><span class="n">filter</span><span class="bp">.</span><span class="n">map_mono</span> <span class="n">h</span><span class="o">)</span>
    <span class="o">(</span><span class="n">continuous</span><span class="bp">.</span><span class="n">tendsto</span> <span class="n">complex</span><span class="bp">.</span><span class="n">continuous_im</span> <span class="n">z</span><span class="o">)</span><span class="bp">⟩</span><span class="o">,</span>
<span class="bp">λ</span> <span class="bp">⟨</span><span class="n">hr</span><span class="o">,</span> <span class="n">hi</span><span class="bp">⟩</span><span class="o">,</span>
<span class="k">have</span> <span class="n">hr2</span> <span class="o">:</span> <span class="n">filter</span><span class="bp">.</span><span class="n">tendsto</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span><span class="o">:</span><span class="n">ℂ</span><span class="o">,</span> <span class="o">(</span><span class="n">z</span><span class="bp">.</span><span class="n">re</span><span class="o">:</span><span class="n">ℂ</span><span class="o">))</span> <span class="n">f</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">z</span><span class="bp">.</span><span class="n">re</span><span class="o">),</span>
  <span class="k">from</span> <span class="n">filter</span><span class="bp">.</span><span class="n">tendsto</span><span class="bp">.</span><span class="n">comp</span> <span class="n">hr</span> <span class="o">(</span><span class="n">continuous</span><span class="bp">.</span><span class="n">tendsto</span>
    <span class="o">(</span><span class="n">complex</span><span class="bp">.</span><span class="n">continuous_of_real</span><span class="o">)</span> <span class="n">z</span><span class="bp">.</span><span class="n">re</span><span class="o">),</span>
<span class="k">have</span> <span class="n">hi2</span> <span class="o">:</span> <span class="n">filter</span><span class="bp">.</span><span class="n">tendsto</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span><span class="o">:</span><span class="n">ℂ</span><span class="o">,</span> <span class="o">(</span><span class="n">z</span><span class="bp">.</span><span class="n">im</span><span class="o">:</span><span class="n">ℂ</span><span class="o">))</span> <span class="n">f</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">z</span><span class="bp">.</span><span class="n">im</span><span class="o">),</span>
  <span class="k">from</span> <span class="n">filter</span><span class="bp">.</span><span class="n">tendsto</span><span class="bp">.</span><span class="n">comp</span> <span class="n">hi</span> <span class="o">(</span><span class="n">continuous</span><span class="bp">.</span><span class="n">tendsto</span>
    <span class="o">(</span><span class="n">complex</span><span class="bp">.</span><span class="n">continuous_of_real</span><span class="o">)</span> <span class="n">z</span><span class="bp">.</span><span class="n">im</span><span class="o">),</span>
<span class="k">have</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">tendsto_add</span> <span class="n">hr2</span> <span class="o">(</span><span class="n">tendsto_mul</span> <span class="n">hi2</span> <span class="o">(</span><span class="bp">@</span><span class="n">tendsto_const_nhds</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">complex</span><span class="bp">.</span><span class="n">I</span> <span class="bp">_</span><span class="o">)),</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">funext</span> <span class="n">complex</span><span class="bp">.</span><span class="n">re_add_im</span><span class="o">,</span> <span class="n">complex</span><span class="bp">.</span><span class="n">re_add_im</span><span class="o">]</span> <span class="n">at</span> <span class="n">this</span><span class="bp">;</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="o">(</span><span class="n">filter</span><span class="bp">.</span><span class="n">map_id</span> <span class="o">:</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">f</span><span class="o">)]</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">this</span><span class="bp">⟩</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">filter</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">cauchy</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="bp">≤</span> <span class="n">nhds</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">xr</span><span class="o">,</span> <span class="n">hxr</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">complete_space</span><span class="bp">.</span><span class="n">complete</span>
  <span class="o">(</span><span class="n">cauchy_map</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_re</span> <span class="n">hf</span><span class="o">)</span> <span class="k">in</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">xi</span><span class="o">,</span> <span class="n">hxi</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">complete_space</span><span class="bp">.</span><span class="n">complete</span>
  <span class="o">(</span><span class="n">cauchy_map</span> <span class="n">complex</span><span class="bp">.</span><span class="n">uniform_continuous_im</span> <span class="n">hf</span><span class="o">)</span> <span class="k">in</span>
<span class="bp">⟨⟨</span><span class="n">xr</span><span class="o">,</span><span class="n">xi</span><span class="bp">⟩</span><span class="o">,</span> <span class="o">(</span><span class="n">complex</span><span class="bp">.</span><span class="n">filter_le_iff</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">hxr</span><span class="o">,</span> <span class="n">hxi</span><span class="bp">⟩⟩</span>
</pre></div>

#### [ Kenny Lau (Oct 05 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135225115):
<p><span class="user-mention" data-user-id="120943">@Andreas Swerdlow</span></p>

#### [ Mario Carneiro (Oct 05 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135225373):
<p>I think there should be another way to say this in terms of the product topology</p>

#### [ Mario Carneiro (Oct 05 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135225386):
<p>That is, this should follow from the fact that C is homeomorphic to R x R with <code>re</code> and <code>im</code> as the projections</p>

#### [ Kenny Lau (Oct 05 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135225448):
<p>is this a fact yet? and will that be easier to use?</p>

#### [ Mario Carneiro (Oct 05 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135225459):
<p>that remains to be seen</p>

#### [ Mario Carneiro (Oct 05 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135225466):
<p>I don't think we have homeos yet (<span class="user-mention" data-user-id="110031">@Patrick Massot</span> ? <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> ?)</p>

#### [ Mario Carneiro (Oct 05 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135225526):
<p>But I think you can prove <code>filter_le_iff</code> pretty easily if you do it on a product space with fst and snd</p>

#### [ Mario Carneiro (Oct 05 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135225593):
<p>And in any case what you really need is just plain continuity of the relevant functions and I think you already have that</p>

#### [ Kenny Lau (Oct 05 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135225605):
<p>I see</p>

#### [ Mario Carneiro (Oct 05 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135225695):
<p>wait, does C have the metric topology or the product topology by definition?</p>

#### [ Kenny Lau (Oct 05 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135238089):
<p>metric</p>

#### [ Patrick Massot (Oct 05 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135238108):
<p>Those are meant to be defeq</p>

#### [ Kenny Lau (Oct 05 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135238160):
<p>C isn't even defined to be a product</p>

#### [ Patrick Massot (Oct 05 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135238183):
<p>I meant that product topology and metric topology on a product of metric spaces are defeq, I don't really know how C is constructed in Lean</p>

#### [ Mario Carneiro (Oct 05 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135238252):
<p>It is possible to state this theorem using <code>(co)map</code> on topologies. You want to say that the topology on C is induced by the map <code>\lam z, (z.re, z.im)</code>, or coinduced by <code>\lam p, p.1 + I p.2</code></p>

#### [ Kenny Lau (Oct 05 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135238944):
<blockquote>
<p>I meant that product topology and metric topology on a product of metric spaces are defeq, I don't really know how C is constructed in Lean</p>
</blockquote>
<p>are they?</p>

#### [ Kenny Lau (Oct 05 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135238945):
<p>isn't it a theorem?</p>

#### [ Kenny Lau (Oct 05 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135238948):
<p>that involves drawing a cirlce inside a square inside a circle inside a square?</p>

#### [ Johan Commelin (Oct 05 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135238959):
<blockquote>
<p>that involves drawing a cirlce inside a square inside a circle inside a square?</p>
</blockquote>
<p>Can Lean do that?</p>

#### [ Patrick Massot (Oct 05 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135238974):
<p>there is no circle in Lean. The product metric is defined as the max metric</p>

#### [ Kenny Lau (Oct 05 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135239022):
<p>oh well then it isn't defeq to the metric in C then</p>

#### [ Kenny Lau (Oct 05 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135239023):
<p>the metric in C is the circle metric</p>

#### [ Mario Carneiro (Oct 05 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135239046):
<p>the balls in C are circles because it uses the metric topology</p>

#### [ Johan Commelin (Oct 05 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135239110):
<p>Right, but not the product metric...</p>

#### [ Mario Carneiro (Oct 05 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135239123):
<p>if we wanted, we could define the topology on C as the product topology (or rather a mapping thereof), and then the typeclass would force us to prove this theorem</p>

#### [ Mario Carneiro (Oct 05 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135239177):
<p>but given that C has no pre-existing topology on it, it seems okay to just use the metric topology as the definition; but this means that we don't get any help with the homeo proof</p>

#### [ Kenny Lau (Oct 05 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135239231):
<p>I mean, my filter lemma <em>is</em> the homeomorphism</p>

#### [ Patrick Massot (Oct 05 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135239236):
<blockquote>
<p>I don't think we have homeos yet (Patrick Massot** ? Johannes Hölzl ?)</p>
</blockquote>
<p>This is not in mathlib, mostly because I don't know whether it should use the category theory stuff or be as in <a href="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/homeos.lean" target="_blank" title="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/homeos.lean">https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/homeos.lean</a></p>

#### [ Mario Carneiro (Oct 05 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135239319):
<p>no categories in the definition</p>

#### [ Mario Carneiro (Oct 05 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135239323):
<p>it should be 100% topology</p>

#### [ Patrick Massot (Oct 05 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135239329):
<p>do you want me to PR that file then?</p>

#### [ Mario Carneiro (Oct 05 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135239379):
<p>I don't see why not... I will leave the merging to Johannes though since he's been involved more</p>

#### [ Kenny Lau (Oct 05 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135239463):
<p>I really think the circle metric is the right one</p>

#### [ Kenny Lau (Oct 05 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135239471):
<p>hmm, never mind</p>

#### [ Mario Carneiro (Oct 05 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135239608):
<p>The circle <em>metric</em> is certainly the right one, but I wonder if the <em>topology</em> should be defined using something like <code>comap re \sqcap comap im</code></p>

#### [ Mario Carneiro (Oct 05 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex%20forms%20uniform%20space/near/135239681):
<p>which will make your filter theorem essentially by definition, and the bulk of that proof will be transferred to the construction of the metric_space instance</p>


{% endraw %}
