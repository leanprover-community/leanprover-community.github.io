---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/69945Hausdorffification.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Hausdorffification](https://leanprover-community.github.io/archive/116395maths/69945Hausdorffification.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Oct 18 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026443):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">continuity</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">t</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span>
<span class="n">include</span> <span class="n">t</span>

<span class="n">def</span> <span class="n">Hausdorffification</span><span class="bp">.</span><span class="n">setoid</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">r</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">t2_space</span> <span class="o">(</span><span class="n">quotient</span> <span class="n">s</span><span class="o">)],</span> <span class="bp">@</span><span class="n">setoid</span><span class="bp">.</span><span class="n">r</span> <span class="n">α</span> <span class="n">s</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span>
  <span class="n">iseqv</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="bp">_</span> <span class="n">s</span> <span class="bp">_</span><span class="o">,</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span> <span class="n">s</span> <span class="n">ht2</span><span class="o">,</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="bp">@</span><span class="n">H</span> <span class="n">s</span> <span class="n">ht2</span><span class="o">),</span>
    <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H1</span> <span class="n">H2</span> <span class="n">s</span> <span class="n">ht2</span><span class="o">,</span> <span class="n">s</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="bp">@</span><span class="n">H1</span> <span class="n">s</span> <span class="n">ht2</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">H2</span> <span class="n">s</span> <span class="n">ht2</span><span class="o">)</span><span class="bp">⟩</span> <span class="o">}</span>

<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">Hausdorffification</span><span class="bp">.</span><span class="n">setoid</span>

<span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">def</span> <span class="n">Hausdorffification</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="o">:=</span>
<span class="n">quotient</span> <span class="o">(</span><span class="n">Hausdorffification</span><span class="bp">.</span><span class="n">setoid</span> <span class="n">α</span><span class="o">)</span>

<span class="kn">instance</span> <span class="n">Hausdorffification</span><span class="bp">.</span><span class="n">t2_space</span> <span class="o">:</span>
  <span class="n">t2_space</span> <span class="o">(</span><span class="n">Hausdorffification</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">t2</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on₂</span> <span class="n">x</span> <span class="n">y</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">m</span> <span class="n">n</span> <span class="n">H</span><span class="o">,</span>
    <span class="k">begin</span>
      <span class="n">letI</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span><span class="o">,</span>
      <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">ne</span><span class="bp">.</span><span class="n">def</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">eq</span><span class="o">,</span> <span class="o">(</span><span class="bp">≈</span><span class="o">),</span> <span class="n">setoid</span><span class="bp">.</span><span class="n">r</span><span class="o">,</span> <span class="n">not_forall</span><span class="o">]</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
      <span class="n">rcases</span> <span class="n">H</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">r</span><span class="o">,</span> <span class="n">ht2</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">resetI</span><span class="o">,</span>
      <span class="k">let</span> <span class="n">f</span> <span class="o">:</span> <span class="n">Hausdorffification</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">quotient</span> <span class="n">r</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">refine</span> <span class="bp">λ</span> <span class="n">e</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">lift_on&#39;</span> <span class="n">e</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span> <span class="bp">_</span><span class="o">,</span>
        <span class="n">intros</span> <span class="n">a</span> <span class="n">b</span> <span class="n">H</span><span class="o">,</span> <span class="n">apply</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span><span class="o">,</span> <span class="n">apply</span> <span class="n">H</span> <span class="o">},</span>
      <span class="k">have</span> <span class="n">hf</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">f</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">intros</span> <span class="n">s</span> <span class="n">hs</span><span class="o">,</span>
        <span class="n">change</span> <span class="n">is_open</span> <span class="o">(</span><span class="n">quotient</span><span class="bp">.</span><span class="n">mk</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="bp">_</span><span class="o">),</span>
        <span class="n">rw</span> <span class="err">←</span> <span class="n">set</span><span class="bp">.</span><span class="n">preimage_comp</span><span class="o">,</span>
        <span class="n">exact</span> <span class="n">hs</span> <span class="o">},</span>
      <span class="n">rcases</span> <span class="n">t2_separation</span> <span class="o">(</span><span class="n">mt</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">exact</span> <span class="n">H</span><span class="o">)</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">u</span><span class="o">,</span> <span class="n">v</span><span class="o">,</span> <span class="n">h1</span><span class="o">,</span> <span class="n">h2</span><span class="o">,</span> <span class="n">h3</span><span class="o">,</span> <span class="n">h4</span><span class="o">,</span> <span class="n">h5</span><span class="bp">⟩</span><span class="o">,</span>
      <span class="n">refine</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span> <span class="n">hf</span> <span class="bp">_</span> <span class="n">h1</span><span class="o">,</span> <span class="n">hf</span> <span class="bp">_</span> <span class="n">h2</span><span class="o">,</span> <span class="n">h3</span><span class="o">,</span> <span class="n">h4</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">eq_empty_of_subset_empty</span> <span class="bp">_⟩</span><span class="o">,</span>
      <span class="n">exact</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">H</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">eq_empty_iff_forall_not_mem</span><span class="bp">.</span><span class="mi">1</span> <span class="n">h5</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="n">H</span>
    <span class="kn">end</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Oct 18 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026483):
<p>Is there any way to do this constructively?</p>

#### [ Johannes Hölzl (Oct 18 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026590):
<p>usually the relation is defined as "define $a \sim b$ if any open set containing $a$ intersects any open set containing $b$". maybe this works constructively?</p>

#### [ Kenny Lau (Oct 18 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026600):
<p>you need to iterate that transfinitely many times to have a T2 space</p>

#### [ Kenny Lau (Oct 18 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026609):
<p>and that would involve induction-recursion (is the name right?) which is stronger than Lean</p>

#### [ Mario Carneiro (Oct 18 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026660):
<p>Why? What is the idea behind this definition</p>

#### [ David Michael Roberts (Oct 18 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026664):
<p><a href="https://ncatlab.org/nlab/show/Hausdorff+space#in_constructive_mathematics" target="_blank" title="https://ncatlab.org/nlab/show/Hausdorff+space#in_constructive_mathematics">https://ncatlab.org/nlab/show/Hausdorff+space#in_constructive_mathematics</a></p>

#### [ Mario Carneiro (Oct 18 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026689):
<p>by the way, I think that the definition of T2 in mathlib is contrapositive of the right one</p>

#### [ Mario Carneiro (Oct 18 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026771):
<p>which apparently nLab calls "weakly Hausdorff"</p>

#### [ Mario Carneiro (Oct 18 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136026901):
<p>also, I don't see any nonconstructivity in that proof</p>

#### [ Kenny Lau (Oct 18 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136042314):
<p>I used not_forall</p>

#### [ Kenny Lau (Oct 18 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136049981):
<blockquote>
<p>Why? What is the idea behind this definition</p>
</blockquote>
<p>quotient a lot until you get a T2 space, but don't quotient more than necessary</p>

#### [ Mario Carneiro (Oct 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136049993):
<p>what's the problem with Johannes's definition</p>

#### [ Kenny Lau (Oct 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136050007):
<p>that it doesn't produce a T2 space</p>

#### [ Mario Carneiro (Oct 18 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136050017):
<p>why</p>

#### [ Mario Carneiro (Oct 18 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136050064):
<p>like where does the proof break down</p>

#### [ Kenny Lau (Oct 18 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136050068):
<p><a href="https://topospaces.subwiki.org/wiki/Hausdorffization#Example_to_illustrate_why_one_step_isn.27t_enough" target="_blank" title="https://topospaces.subwiki.org/wiki/Hausdorffization#Example_to_illustrate_why_one_step_isn.27t_enough">https://topospaces.subwiki.org/wiki/Hausdorffization#Example_to_illustrate_why_one_step_isn.27t_enough</a></p>

#### [ Mario Carneiro (Oct 18 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136061666):
<blockquote>
<p>you need to iterate that transfinitely many times to have a T2 space<br>
and that would involve induction-recursion (is the name right?) which is stronger than Lean</p>
</blockquote>
<p>You don't need proof principles stronger than lean. You just need to know that the process stops eventually, by bounding the space of possible relations</p>

#### [ Mario Carneiro (Oct 18 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136061871):
<p>although topospaces wiki is shamefully cavalier about defining an ordinal indexed sequence of topological spaces with direct limits and then just saying "take <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>h</mi><mi mathvariant="normal">∞</mi></msup></mrow><annotation encoding="application/x-tex">h^\infty</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.69444em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">h</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">∞</span></span></span></span></span></span></span></span></span></span></span>" as if that were well defined</p>

#### [ Mario Carneiro (Oct 18 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136061992):
<p>In lean, it is an interesting example of an inductive predicate that is positive but not strictly positive</p>

#### [ Mario Carneiro (Oct 18 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136062288):
<div class="codehilite"><pre><span></span>inductive hausify : α → α → Prop
| refl : ∀ x, hausify x x
| trans : ∀ x y z, hausify x y → hausify y z → hausify x z
| haus : ∀x y, (∀ u v : set α, is_open u → is_open v →
   x ∈ u → y ∈ v → ∃ z w, z ∈ u ∧ w ∈ v ∧ hausify z w) → hausify x y
</pre></div>


<p>This definition is monotone but not syntactically</p>

#### [ Mario Carneiro (Oct 18 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136062874):
<p>So here's how you can do the transfinite induction construction:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">hausify1</span> <span class="o">(</span><span class="n">haus</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">trans</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="n">hausify1</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">→</span> <span class="n">hausify1</span> <span class="n">y</span> <span class="n">z</span> <span class="bp">→</span> <span class="n">hausify1</span> <span class="n">x</span> <span class="n">z</span>
<span class="bp">|</span> <span class="n">haus</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">u</span> <span class="n">v</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">is_open</span> <span class="n">u</span> <span class="bp">→</span> <span class="n">is_open</span> <span class="n">v</span> <span class="bp">→</span>
   <span class="n">x</span> <span class="err">∈</span> <span class="n">u</span> <span class="bp">→</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">v</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">z</span> <span class="n">w</span><span class="o">,</span> <span class="n">z</span> <span class="err">∈</span> <span class="n">u</span> <span class="bp">∧</span> <span class="n">w</span> <span class="err">∈</span> <span class="n">v</span> <span class="bp">∧</span> <span class="n">haus</span> <span class="n">z</span> <span class="n">w</span><span class="o">)</span> <span class="bp">→</span> <span class="n">hausify1</span> <span class="n">x</span> <span class="n">y</span>

<span class="kn">inductive</span> <span class="n">hausify_transfinite</span> <span class="o">:</span> <span class="o">(</span><span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">zero</span> <span class="o">:</span> <span class="n">hausify_transfinite</span> <span class="n">eq</span>
<span class="bp">|</span> <span class="n">succ</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">r</span><span class="o">,</span> <span class="n">hausify_transfinite</span> <span class="n">r</span> <span class="bp">→</span> <span class="n">hausify_transfinite</span> <span class="o">(</span><span class="n">hausify1</span> <span class="n">r</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">lim</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">R</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">),</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">r</span> <span class="err">∈</span> <span class="n">R</span><span class="o">,</span> <span class="n">hausify_transfinite</span> <span class="n">r</span><span class="o">)</span> <span class="bp">→</span>
  <span class="n">hausify_transfinite</span> <span class="o">(</span><span class="n">hausify1</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">r</span> <span class="err">∈</span> <span class="n">R</span><span class="o">,</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="n">x</span> <span class="n">y</span><span class="o">))</span>

<span class="n">def</span> <span class="n">hausify</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">r</span><span class="o">,</span> <span class="n">hausify_transfinite</span> <span class="n">r</span> <span class="bp">∧</span> <span class="n">r</span> <span class="n">x</span> <span class="n">y</span>
</pre></div>


<p>Needless to say I prefer your definition</p>

#### [ Kenny Lau (Oct 18 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136066103):
<p>I prefer yours</p>

#### [ Mario Carneiro (Oct 18 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136066687):
<p>this whole construction is doing something similar to yours, quotienting by all relations that are hausdorffish</p>

#### [ Mario Carneiro (Oct 18 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136066706):
<p>it's easier to say <code>t2_space (quotient r)</code> than all this</p>

#### [ Kenny Lau (Oct 19 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136074995):
<p>can you define ε_0 using that?</p>

#### [ Kenny Lau (Oct 19 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075001):
<p>oh wait you already defined ordinal notations inductively</p>

#### [ Kenny Lau (Oct 19 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075035):
<p>wait no I'm confused</p>

#### [ Mario Carneiro (Oct 19 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075791):
<p>This allows you to do transfinite iteration over a fixed type</p>

#### [ Mario Carneiro (Oct 19 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075805):
<p>the key is the fact that it is all taking place in one complete lattice</p>

#### [ Kenny Lau (Oct 19 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075818):
<p>I see</p>

#### [ Kenny Lau (Oct 19 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075820):
<p>So you can't define ordinals using this zero-lim-succ</p>

#### [ Mario Carneiro (Oct 19 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075869):
<p>You have to build an inductive <code>Type</code> to do that</p>

#### [ Mario Carneiro (Oct 19 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075877):
<p>by the way epsilon_0 is the supremum of all ordinals with <code>ordinal_notation</code></p>

#### [ Mario Carneiro (Oct 19 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075881):
<p>in case you wanted to define it</p>

#### [ Mario Carneiro (Oct 19 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075909):
<p>It is possible to extend ordinal notations to epsilon_0 and beyond using the veblen hierarchy, but I don't think anyone around here cares about large countable ordinals</p>

#### [ Mario Carneiro (Oct 19 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136075974):
<p>I think we also have what we need to define omega_1^CK using computable functions</p>

#### [ Kevin Buzzard (Oct 19 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorffification/near/136093605):
<p>Is this a reflection?</p>


{% endraw %}
