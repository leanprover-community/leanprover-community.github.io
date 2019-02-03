---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48331isthischoicecomputable.html
---

## Stream: [general](index.html)
### Topic: [is this choice computable?](48331isthischoicecomputable.html)

---


{% raw %}
#### [ Kenny Lau (Sep 04 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20choice%20computable%3F/near/133307935):
<p>Can the two <code>sorry</code>s be filled in?</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">ι</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="n">ι</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">has_zero</span> <span class="o">(</span><span class="n">β</span> <span class="n">i</span><span class="o">)]</span>

<span class="n">def</span> <span class="n">pointed_sigma</span><span class="bp">.</span><span class="n">aux</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span> <span class="o">:=</span>
<span class="n">option</span> <span class="err">Σ</span> <span class="n">i</span><span class="o">,</span> <span class="n">β</span> <span class="n">i</span>

<span class="kn">inductive</span> <span class="n">pointed_sigma</span><span class="bp">.</span><span class="n">r</span> <span class="o">:</span> <span class="n">pointed_sigma</span><span class="bp">.</span><span class="n">aux</span> <span class="n">ι</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">pointed_sigma</span><span class="bp">.</span><span class="n">aux</span> <span class="n">ι</span> <span class="n">β</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">refl</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">x</span><span class="o">,</span> <span class="n">pointed_sigma</span><span class="bp">.</span><span class="n">r</span> <span class="n">x</span> <span class="n">x</span>
<span class="bp">|</span> <span class="n">zero_left</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">pointed_sigma</span><span class="bp">.</span><span class="n">r</span> <span class="n">none</span> <span class="o">(</span><span class="n">some</span> <span class="bp">⟨</span><span class="n">i</span><span class="o">,</span> <span class="mi">0</span><span class="bp">⟩</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">zero_right</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">pointed_sigma</span><span class="bp">.</span><span class="n">r</span> <span class="o">(</span><span class="n">some</span> <span class="bp">⟨</span><span class="n">i</span><span class="o">,</span> <span class="mi">0</span><span class="bp">⟩</span><span class="o">)</span> <span class="n">none</span>
<span class="bp">|</span> <span class="n">zero</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">i</span> <span class="n">j</span><span class="o">,</span> <span class="n">pointed_sigma</span><span class="bp">.</span><span class="n">r</span> <span class="o">(</span><span class="n">some</span> <span class="bp">⟨</span><span class="n">i</span><span class="o">,</span> <span class="mi">0</span><span class="bp">⟩</span><span class="o">)</span> <span class="o">(</span><span class="n">some</span> <span class="bp">⟨</span><span class="n">j</span><span class="o">,</span> <span class="mi">0</span><span class="bp">⟩</span><span class="o">)</span>

<span class="kn">instance</span> <span class="n">pointed_sigma</span><span class="bp">.</span><span class="n">setoid</span> <span class="o">:</span> <span class="n">setoid</span> <span class="o">(</span><span class="n">pointed_sigma</span><span class="bp">.</span><span class="n">aux</span> <span class="n">ι</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">pointed_sigma</span><span class="bp">.</span><span class="n">r</span> <span class="n">ι</span> <span class="n">β</span><span class="o">,</span>
  <span class="n">iseqv</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">refine</span> <span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">h</span><span class="o">,</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="n">h1</span> <span class="n">h2</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">constructor</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">cases</span> <span class="n">h</span><span class="bp">;</span> <span class="n">constructor</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">cases</span> <span class="n">h1</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">h2</span><span class="bp">;</span> <span class="n">constructor</span> <span class="o">}</span>
  <span class="kn">end</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">pointed_sigma</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span> <span class="o">:=</span>
<span class="n">quotient</span> <span class="o">(</span><span class="n">pointed_sigma</span><span class="bp">.</span><span class="n">setoid</span> <span class="n">ι</span> <span class="n">β</span><span class="o">)</span>

<span class="kn">namespace</span> <span class="n">pointed_sigma</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_zero</span> <span class="o">(</span><span class="n">pointed_sigma</span> <span class="n">ι</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="err">⟦</span><span class="n">none</span><span class="err">⟧</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">of</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">ι</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">β</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="n">pointed_sigma</span> <span class="n">ι</span> <span class="n">β</span> <span class="o">:=</span>
<span class="err">⟦</span><span class="n">some</span> <span class="bp">⟨</span><span class="n">i</span><span class="o">,</span> <span class="n">x</span><span class="bp">⟩</span><span class="err">⟧</span>

<span class="n">def</span> <span class="n">choice</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">i</span> <span class="n">j</span> <span class="o">:</span> <span class="n">ι</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">β</span> <span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">y</span><span class="o">,</span> <span class="n">of</span> <span class="n">ι</span> <span class="n">β</span> <span class="n">i</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">of</span> <span class="n">ι</span> <span class="n">β</span> <span class="n">j</span> <span class="n">y</span><span class="o">),</span> <span class="n">β</span> <span class="n">j</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">theorem</span> <span class="n">choice_eq</span> <span class="o">(</span><span class="n">i</span> <span class="n">j</span> <span class="o">:</span> <span class="n">ι</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">β</span> <span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span><span class="o">)</span> <span class="o">:</span> <span class="n">of</span> <span class="n">ι</span> <span class="n">β</span> <span class="n">i</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">of</span> <span class="n">ι</span> <span class="n">β</span> <span class="n">j</span> <span class="o">(</span><span class="n">choice</span> <span class="n">ι</span> <span class="n">β</span> <span class="n">i</span> <span class="n">j</span> <span class="n">x</span> <span class="n">H</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">end</span> <span class="n">pointed_sigma</span>
</pre></div>

#### [ Kenny Lau (Sep 04 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20choice%20computable%3F/near/133307990):
<p>So I have a bunch of pointed types, indexed by the type <code>ι</code>.</p>

#### [ Kenny Lau (Sep 04 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20choice%20computable%3F/near/133308002):
<p>I'm building the pointed union of these pointed types.</p>

#### [ Kenny Lau (Sep 04 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20choice%20computable%3F/near/133308007):
<p>(The point is represented by zero.)</p>

#### [ Kenny Lau (Sep 04 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20choice%20computable%3F/near/133308016):
<p>So for each <code>i : ι</code>, I have a function from the pointed set indexed by <code>i</code> to the union.</p>

#### [ Kenny Lau (Sep 04 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20choice%20computable%3F/near/133308037):
<p>I'm wondering if I can reverse this operation, i.e. given an element of the pointed union, with a proof that it is from some element of the pointed set indexed by <code>i</code>, I would like to give back this element of the pointed set.</p>

#### [ Reid Barton (Sep 04 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20choice%20computable%3F/near/133312135):
<p>I suspect you need decidable equality on I</p>

#### [ Kenny Lau (Sep 04 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20this%20choice%20computable%3F/near/133312361):
<p>that's also what I suspect, but I can't prove</p>


{% endraw %}
