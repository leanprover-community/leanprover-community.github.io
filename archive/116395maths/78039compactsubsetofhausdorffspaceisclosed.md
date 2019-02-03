---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/78039compactsubsetofhausdorffspaceisclosed.html
---

## Stream: [maths](index.html)
### Topic: [compact subset of hausdorff space is closed](78039compactsubsetofhausdorffspaceisclosed.html)

---


{% raw %}
#### [ Edward Ayers (Aug 14 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132127153):
<p>Hi everyone. I would really appreciate any comments on how to improve this proof. Also, is this result in the library?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="bp">.</span><span class="n">topological_space</span>
<span class="kn">open</span> <span class="n">set</span> <span class="n">filter</span> <span class="n">lattice</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span>

<span class="n">def</span> <span class="n">inclusion</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">s</span> <span class="bp">-&gt;</span> <span class="n">α</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span>
<span class="n">def</span> <span class="n">subspace_top</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">induced</span> <span class="o">(</span><span class="n">inclusion</span> <span class="n">s</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">not_bot_left</span> <span class="o">(</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">filter</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">f</span> <span class="err">⊓</span> <span class="n">g</span> <span class="bp">≠</span> <span class="err">⊥</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">≠</span> <span class="err">⊥</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">apply</span> <span class="n">neq_bot_of_le_neq_bot</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">H1</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">inf_le_left</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">compact_subset_of_t2space_is_closed</span>
    <span class="o">[</span><span class="n">t2_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">Y</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">sc</span> <span class="o">:</span> <span class="n">compact</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">is_closed</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">cases</span> <span class="n">is_closed_iff_nhds</span><span class="o">,</span> <span class="n">clear</span> <span class="n">mp</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">mpr</span><span class="o">,</span> <span class="n">clear</span> <span class="n">mpr</span><span class="o">,</span> <span class="n">intros</span><span class="o">,</span> <span class="n">rename</span> <span class="n">a</span> <span class="n">y</span><span class="o">,</span>
    <span class="k">let</span> <span class="n">f</span> <span class="o">:=</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">y</span> <span class="err">⊓</span> <span class="n">principal</span> <span class="n">Y</span><span class="o">),</span>
    <span class="k">have</span> <span class="n">H3</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">a</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">Y</span><span class="o">),</span> <span class="n">f</span> <span class="err">⊓</span> <span class="n">nhds</span> <span class="n">a</span> <span class="bp">≠</span> <span class="err">⊥</span><span class="o">),</span> <span class="k">from</span> <span class="n">sc</span> <span class="n">f</span> <span class="n">a_1</span> <span class="n">inf_le_right</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">exists</span><span class="bp">.</span><span class="n">elim</span> <span class="n">H3</span><span class="o">,</span>
    <span class="n">intros</span><span class="o">,</span> <span class="n">apply</span> <span class="n">exists</span><span class="bp">.</span><span class="n">elim</span> <span class="n">a_2</span><span class="o">,</span> <span class="n">intros</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">H5</span> <span class="o">:</span> <span class="n">nhds</span> <span class="n">a</span> <span class="err">⊓</span> <span class="n">nhds</span> <span class="n">y</span> <span class="bp">≠</span> <span class="err">⊥</span><span class="o">,</span>
        <span class="n">rewrite</span> <span class="n">inf_assoc</span> <span class="n">at</span> <span class="n">a_4</span><span class="o">,</span> <span class="c1">-- if I do inf_assoc first it fails?!</span>
        <span class="n">rewrite</span> <span class="n">inf_comm</span> <span class="n">at</span> <span class="n">a_4</span><span class="o">,</span>
        <span class="n">rewrite</span> <span class="n">inf_assoc</span> <span class="n">at</span> <span class="n">a_4</span><span class="o">,</span>
        <span class="n">rewrite</span> <span class="n">inf_comm</span> <span class="n">at</span> <span class="n">a_4</span><span class="o">,</span>
        <span class="n">apply</span> <span class="n">not_bot_left</span><span class="o">,</span> <span class="n">assumption</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">H4</span><span class="o">:</span>  <span class="n">a</span> <span class="bp">=</span> <span class="n">y</span><span class="o">,</span> <span class="k">from</span> <span class="n">eq_of_nhds_neq_bot</span> <span class="n">H5</span><span class="o">,</span>
    <span class="n">rewrite</span> <span class="n">H4</span> <span class="n">at</span> <span class="n">a_3</span><span class="o">,</span>
    <span class="n">assumption</span>
    <span class="kn">end</span>
</pre></div>

#### [ Edward Ayers (Aug 14 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132129134):
<p>Version 2:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">compact_subset_of_t2space_is_closed_2</span>
    <span class="o">[</span><span class="n">t2_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">Y</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">sc</span> <span class="o">:</span> <span class="n">compact</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">is_closed</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span>
    <span class="n">iff</span><span class="bp">.</span><span class="n">elim_right</span> <span class="n">is_closed_iff_nhds</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">y</span> <span class="n">H1</span><span class="o">,</span>
        <span class="k">let</span> <span class="n">f</span> <span class="o">:=</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">y</span> <span class="err">⊓</span> <span class="n">principal</span> <span class="n">Y</span><span class="o">)</span> <span class="k">in</span>
        <span class="n">exists</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="n">sc</span> <span class="n">f</span> <span class="n">H1</span> <span class="n">inf_le_right</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">H2</span><span class="o">,</span> <span class="n">exists</span><span class="bp">.</span><span class="n">elim</span> <span class="n">H2</span>
        <span class="o">(</span>
            <span class="k">assume</span> <span class="n">H3</span> <span class="n">H4</span><span class="o">,</span>
            <span class="n">suffices</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">a</span><span class="o">,</span> <span class="k">from</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">this</span><span class="bp">;</span> <span class="n">assumption</span><span class="o">,</span>
            <span class="n">suffices</span> <span class="n">nhds</span> <span class="n">y</span> <span class="err">⊓</span> <span class="n">nhds</span> <span class="n">a</span> <span class="err">⊓</span> <span class="n">principal</span> <span class="n">Y</span> <span class="bp">≠</span> <span class="err">⊥</span><span class="o">,</span> <span class="k">from</span> <span class="n">eq_of_nhds_neq_bot</span> <span class="err">$</span> <span class="n">not_bot_left</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">this</span><span class="o">,</span>
            <span class="k">by</span> <span class="n">cc</span>
        <span class="o">)</span>
    <span class="o">)</span>
<span class="o">)</span>
</pre></div>

#### [ Edward Ayers (Aug 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132133848):
<p>Found it in library: <code>closed_of_compact</code></p>

#### [ Edward Ayers (Aug 14 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132133886):
<p>Although I proved it with filters</p>

#### [ Kevin Buzzard (Aug 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132134882):
<p>First line of proof could be <code>is_closed_iff_nhds.2 (λ y H1,</code> (<code>iff</code> is a structure and you can access its elements with <code>.1</code>, <code>.2</code>). There's a mathlib style guide and you're not conforming to it (I don't think they like the one-bracket-on-a-line thing, and I know they like 2 spaces indent rather than 4).  <code>by rw this; assumption,</code> could be <code>by rwa this</code> (<code>rwa</code> = <code>rw ; assumption</code>, similarly <code>simpa</code>).</p>

#### [ Kevin Buzzard (Aug 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132134906):
<p>but it's certainly a darn sight better than I could have done :-)</p>

#### [ Patrick Massot (Aug 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132134941):
<p><code>simpa</code> is more than <code>simp ... ; assumption</code>, see <a href="https://github.com/leanprover/mathlib/blob/master/docs/tactics.md#simpa" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/tactics.md#simpa">https://github.com/leanprover/mathlib/blob/master/docs/tactics.md#simpa</a></p>

#### [ Kevin Buzzard (Aug 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135482):
<p>Instead of <code>λ a H2, exists.elim H2 ...</code> I wonder if you could have done <code>λ a ⟨H,H2⟩,</code> and then you can maybe avoid the <code>exists.elim</code></p>

#### [ Patrick Massot (Aug 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135502):
<p>Everybody dreams that could be possible, but no.</p>

#### [ Kevin Buzzard (Aug 14 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135570):
<div class="codehilite"><pre><span></span><span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="bp">⟨</span><span class="n">H3</span><span class="o">,</span><span class="n">H4</span><span class="bp">⟩</span><span class="o">,</span>
        <span class="o">(</span>
            <span class="n">suffices</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">a</span><span class="o">,</span> <span class="k">from</span> <span class="k">by</span> <span class="n">rwa</span> <span class="n">this</span><span class="o">,</span>
</pre></div>


<p>;-)</p>

#### [ Patrick Massot (Aug 14 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135580):
<p>Latest discussion is probably <a href="#narrow/stream/113488-general/topic/eta.20for.20structures" title="#narrow/stream/113488-general/topic/eta.20for.20structures">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta.20for.20structures</a></p>

#### [ Kevin Buzzard (Aug 14 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135586):
<p>I got lucky because he assumes <code>H3</code> and <code>H4</code></p>

#### [ Edward Ayers (Aug 14 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135629):
<blockquote>
<p>There's a mathlib style guide </p>
</blockquote>
<p>I should read that.</p>

#### [ Patrick Massot (Aug 14 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135806):
<p>Kevin, I don't understand what you wrote? Do you have something that compiles?</p>

#### [ Kevin Buzzard (Aug 14 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135863):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">compact_subset_of_t2space_is_closed_2</span>
  <span class="o">[</span><span class="n">t2_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">Y</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">sc</span> <span class="o">:</span> <span class="n">compact</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">is_closed</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">is_closed_iff_nhds</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">y</span> <span class="n">H1</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">f</span> <span class="o">:=</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">y</span> <span class="err">⊓</span> <span class="n">principal</span> <span class="n">Y</span><span class="o">)</span> <span class="k">in</span>
  <span class="n">exists</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="n">sc</span> <span class="n">f</span> <span class="n">H1</span> <span class="n">inf_le_right</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="bp">⟨_</span><span class="o">,</span><span class="bp">_⟩</span><span class="o">,</span>
    <span class="o">(</span> <span class="n">suffices</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">a</span><span class="o">,</span> <span class="k">from</span> <span class="k">by</span> <span class="n">rwa</span> <span class="n">this</span><span class="o">,</span>
      <span class="n">suffices</span> <span class="n">nhds</span> <span class="n">y</span> <span class="err">⊓</span> <span class="n">nhds</span> <span class="n">a</span> <span class="err">⊓</span> <span class="n">principal</span> <span class="n">Y</span> <span class="bp">≠</span> <span class="err">⊥</span><span class="o">,</span> <span class="k">from</span> <span class="n">eq_of_nhds_neq_bot</span> <span class="err">$</span> <span class="n">not_bot_left</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">this</span><span class="o">,</span>
      <span class="k">by</span> <span class="n">cc</span><span class="o">)))</span>
</pre></div>


<p>My attempt to conform to mathlib style guide but I'm not sure I am -- I don't normally do term mode</p>

#### [ Kevin Buzzard (Aug 14 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135967):
<p><a href="https://github.com/leanprover/mathlib/blob/master/docs/style.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/style.md">https://github.com/leanprover/mathlib/blob/master/docs/style.md</a></p>

#### [ Patrick Massot (Aug 14 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135972):
<p><code>from by</code> is redundant</p>

#### [ Patrick Massot (Aug 14 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135979):
<p><code>by</code> is enough</p>

#### [ Patrick Massot (Aug 14 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135997):
<p>how is it possible that <code>λ a ⟨_,_⟩,</code>? Someone lied to me!</p>

#### [ Kevin Buzzard (Aug 14 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136008):
<p>There's a problem with that idiom</p>

#### [ Mario Carneiro (Aug 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136024):
<p>use <code>$</code> to drop the parentheses and indents</p>

#### [ Kevin Buzzard (Aug 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136027):
<p>It doesn't unfold <em>at all</em> well</p>

#### [ Mario Carneiro (Aug 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136044):
<p>it unfolds exactly as well as <code>exists.elim</code></p>

#### [ Kevin Buzzard (Aug 14 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136071):
<p><a href="https://github.com/leanprover/mathlib/blob/master/docs/naming.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/naming.md">https://github.com/leanprover/mathlib/blob/master/docs/naming.md</a> explains why this lemma is called <code>closed_of_compact</code></p>

#### [ Kevin Buzzard (Aug 14 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136230):
<p>I should also say that I don't know if any of my suggested changes are _better_, I'm just observing that they exist :-)</p>

#### [ Mario Carneiro (Aug 14 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136347):
<p>there is worth in separating stylistic improvements from proof improvements</p>

#### [ Mario Carneiro (Aug 14 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136428):
<p>space after comma <code> ⟨_, _⟩,</code></p>

#### [ Mario Carneiro (Aug 14 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136501):
<p>you can use <code>let</code> match in place of <code>exists.elim</code></p>

#### [ Edward Ayers (Aug 14 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137333):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">compact_subset_of_t2space_is_closed_2</span>
  <span class="o">[</span><span class="n">t2_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">Y</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">sc</span> <span class="o">:</span> <span class="n">compact</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_closed</span> <span class="n">Y</span> <span class="o">:=</span>
<span class="n">is_closed_iff_nhds</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="k">assume</span> <span class="n">y</span> <span class="n">h₁</span><span class="o">,</span>
  <span class="k">let</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">h₂</span><span class="o">,</span> <span class="n">h₃</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">sc</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">y</span> <span class="err">⊓</span> <span class="n">principal</span> <span class="n">Y</span><span class="o">)</span> <span class="n">h₁</span> <span class="n">inf_le_right</span> <span class="k">in</span>
  <span class="n">suffices</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">a</span><span class="o">,</span> <span class="k">by</span> <span class="n">rwa</span> <span class="n">this</span><span class="o">,</span>
  <span class="n">suffices</span> <span class="n">nhds</span> <span class="n">y</span> <span class="err">⊓</span> <span class="n">nhds</span> <span class="n">a</span> <span class="err">⊓</span> <span class="n">principal</span> <span class="n">Y</span> <span class="bp">≠</span> <span class="err">⊥</span><span class="o">,</span>
    <span class="k">from</span> <span class="n">eq_of_nhds_neq_bot</span> <span class="err">$</span> <span class="n">not_bot_left</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">this</span><span class="o">,</span>
  <span class="k">by</span> <span class="n">cc</span>
</pre></div>

#### [ Mario Carneiro (Aug 14 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137444):
<p>I think you got everything</p>

#### [ Edward Ayers (Aug 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137466):
<p>Fabulous thanks so much for your help everyone.</p>

#### [ Mario Carneiro (Aug 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137479):
<p>oh, the name needs work</p>

#### [ Mario Carneiro (Aug 14 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137536):
<p>then again <code>closed_of_compact</code> is already taken, I hear</p>

#### [ Edward Ayers (Aug 14 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137637):
<p>Yes I found it in <code>continuity.lean</code>.</p>

#### [ Edward Ayers (Aug 14 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137712):
<p>My big problem with proving this was not knowing what lemmas were available. I would use vscodes find window with regex to find candidate lemmas. Are there any search tools in Lean?</p>

#### [ Patrick Massot (Aug 14 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137720):
<p>tactic.find in mathlib</p>

#### [ Patrick Massot (Aug 14 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137729):
<p><a href="https://github.com/leanprover/mathlib/blob/master/docs/tactics.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/tactics.md">https://github.com/leanprover/mathlib/blob/master/docs/tactics.md</a></p>

#### [ Patrick Massot (Aug 14 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137739):
<p>Reading mathlib doc would probably be a good idea</p>

#### [ Patrick Massot (Aug 14 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137748):
<p>That find tactic is from Sebastian btw</p>

#### [ Patrick Massot (Aug 15 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132142686):
<p>Let me try something more constructive than OS recommendations. Since you like term mode, why isn't the first lemma:<br>
<code>lemma not_bot_left (f g : filter α) (H1 : f ⊓ g ≠ ⊥) : f ≠ ⊥ := neq_bot_of_le_neq_bot H1 inf_le_left</code></p>

#### [ Patrick Massot (Aug 15 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132142828):
<p>and mathlib name would probably be closer to <code>neq_bot_of_inf_neq_bot_left</code></p>


{% endraw %}
