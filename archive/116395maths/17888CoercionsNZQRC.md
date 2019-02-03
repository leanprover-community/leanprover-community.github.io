---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/17888CoercionsNZQRC.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Coercions N->Z->Q->R->C](https://leanprover-community.github.io/archive/116395maths/17888CoercionsNZQRC.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Aug 03 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130849802):
<p>My students want to move freely between these five basic objects, sometimes because they have made poor design decisions but sometimes for genuine reasons. I figured I'd try to get to the bottom of why they were having problems.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">complex</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">definition</span> <span class="n">has_coe_NZ</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="bp">ℕ</span> <span class="bp">ℤ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">definition</span> <span class="n">has_coe_NQ</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="bp">ℕ</span> <span class="n">ℚ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">definition</span> <span class="n">has_coe_NR</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="bp">ℕ</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">definition</span> <span class="n">has_coe_NC</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="bp">ℕ</span> <span class="n">ℂ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">definition</span> <span class="n">has_coe_ZQ</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="bp">ℤ</span> <span class="n">ℚ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">definition</span> <span class="n">has_coe_ZR</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="bp">ℤ</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">definition</span> <span class="n">has_coe_ZC</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="bp">ℤ</span> <span class="n">ℂ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="c1">-- definition has_coe_QR : has_coe ℚ ℝ := by apply_instance -- fails</span>
<span class="n">noncomputable</span> <span class="kn">definition</span> <span class="n">has_coe_QR</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="n">ℚ</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="c1">-- definition has_coe_QC : has_coe ℚ ℂ := by apply_instance -- fails</span>
<span class="n">noncomputable</span> <span class="kn">definition</span> <span class="n">has_coe_QC</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="n">ℚ</span> <span class="n">ℂ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">definition</span> <span class="n">has_coe_RC</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="n">ℝ</span> <span class="n">ℂ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>

<span class="kn">definition</span> <span class="n">coe_NZ</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℤ</span> <span class="o">:=</span> <span class="n">has_coe_NZ</span><span class="bp">.</span><span class="n">coe</span>
<span class="kn">definition</span> <span class="n">coe_NQ</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">ℚ</span> <span class="o">:=</span> <span class="n">has_coe_NQ</span><span class="bp">.</span><span class="n">coe</span>
<span class="kn">definition</span> <span class="n">coe_NR</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="n">has_coe_NR</span><span class="bp">.</span><span class="n">coe</span>
<span class="kn">definition</span> <span class="n">coe_NC</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">ℂ</span> <span class="o">:=</span> <span class="n">has_coe_NC</span><span class="bp">.</span><span class="n">coe</span>
<span class="kn">definition</span> <span class="n">coe_ZQ</span> <span class="o">:</span> <span class="bp">ℤ</span> <span class="bp">→</span> <span class="n">ℚ</span> <span class="o">:=</span> <span class="n">has_coe_ZQ</span><span class="bp">.</span><span class="n">coe</span>
<span class="kn">definition</span> <span class="n">coe_ZR</span> <span class="o">:</span> <span class="bp">ℤ</span> <span class="bp">→</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="n">has_coe_ZR</span><span class="bp">.</span><span class="n">coe</span>
<span class="kn">definition</span> <span class="n">coe_ZC</span> <span class="o">:</span> <span class="bp">ℤ</span> <span class="bp">→</span> <span class="n">ℂ</span> <span class="o">:=</span> <span class="n">has_coe_ZC</span><span class="bp">.</span><span class="n">coe</span>
<span class="n">noncomputable</span> <span class="kn">definition</span> <span class="n">coe_QR</span> <span class="o">:</span> <span class="n">ℚ</span> <span class="bp">→</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="n">has_coe_QR</span><span class="bp">.</span><span class="n">coe</span>
<span class="n">noncomputable</span> <span class="kn">definition</span> <span class="n">coe_QC</span> <span class="o">:</span> <span class="n">ℚ</span> <span class="bp">→</span> <span class="n">ℂ</span> <span class="o">:=</span> <span class="n">has_coe_QC</span><span class="bp">.</span><span class="n">coe</span>
<span class="kn">definition</span> <span class="n">coe_RC</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="n">ℂ</span> <span class="o">:=</span> <span class="n">has_coe_RC</span><span class="bp">.</span><span class="n">coe</span>

<span class="c1">-- The ten theorems below are what I would like to access easily in Lean.</span>
<span class="c1">-- I don&#39;t know what to call them; the current names are just placeholders.</span>

<span class="c1">-- N to Z is never a problem</span>
<span class="kn">theorem</span> <span class="n">NZQ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">coe_ZQ</span> <span class="o">(</span><span class="n">coe_NZ</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">coe_NQ</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="kn">theorem</span> <span class="n">NZR</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">coe_ZR</span> <span class="o">(</span><span class="n">coe_NZ</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">coe_NR</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="kn">theorem</span> <span class="n">NZC</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">coe_ZC</span> <span class="o">(</span><span class="n">coe_NZ</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">coe_NC</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="c1">-- the problems start now</span>
<span class="kn">theorem</span> <span class="n">ZQR</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">coe_QR</span> <span class="o">(</span><span class="n">coe_ZQ</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">coe_ZR</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="c1">-- simp fails</span>
<span class="kn">theorem</span> <span class="n">QRC</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:</span> <span class="n">coe_RC</span> <span class="o">(</span><span class="n">coe_QR</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">coe_QC</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="c1">-- simp fails</span>
<span class="kn">theorem</span> <span class="n">ZRC</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">coe_RC</span> <span class="o">(</span><span class="n">coe_ZR</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">coe_ZC</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="c1">-- simp fails</span>

<span class="kn">theorem</span> <span class="n">NQR</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">coe_QR</span> <span class="o">(</span><span class="n">coe_NQ</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">coe_NR</span> <span class="n">x</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">NZQ</span><span class="o">,</span><span class="n">ZQR</span><span class="o">,</span><span class="err">←</span><span class="n">NZR</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">ZQC</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">coe_QC</span> <span class="o">(</span><span class="n">coe_ZQ</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">coe_ZC</span> <span class="n">x</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">QRC</span><span class="o">,</span><span class="err">←</span><span class="n">ZRC</span><span class="o">,</span><span class="err">←</span><span class="n">ZQR</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">NQC</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">coe_QC</span> <span class="o">(</span><span class="n">coe_NQ</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">coe_NC</span> <span class="n">x</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">NZC</span><span class="o">,</span><span class="err">←</span><span class="n">NZQ</span><span class="o">,</span><span class="err">←</span><span class="n">ZQC</span><span class="o">]</span>
<span class="kn">theorem</span> <span class="n">NRC</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">coe_RC</span> <span class="o">(</span><span class="n">coe_NR</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">coe_NC</span> <span class="n">x</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">NQC</span><span class="o">,</span><span class="err">←</span><span class="n">QRC</span><span class="o">,</span><span class="err">←</span><span class="n">NQR</span><span class="o">]</span>

<span class="c1">-- cool stuff my stuents constantly want to be able to do</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="o">((</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">ZQR</span> <span class="n">x</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="k">let</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:=</span> <span class="err">↑</span><span class="n">x</span> <span class="k">in</span> <span class="k">let</span> <span class="o">(</span><span class="n">z</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="err">↑</span><span class="n">y</span> <span class="k">in</span> <span class="n">z</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">x</span> <span class="o">:=</span> <span class="n">ZQR</span> <span class="n">x</span>
</pre></div>


<p>Q1) Is there a good reason for the noncomputable coercions being noncomputable? </p>
<p>Q2) How do I prove the sorried coercion theorems?</p>
<p>Q3) What are the correct names for these theorems that enable me to cancel <code>↑↑</code> in these specific cases?</p>

#### [ Gabriel Ebner (Aug 03 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130850810):
<p>You need to use the right syntax, then everything works out of the box <span class="emoji emoji-263a" title="smile">:smile:</span> </p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">ZQR</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="o">((</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>
<span class="kn">theorem</span> <span class="n">QRC</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:</span> <span class="o">((</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>
<span class="kn">theorem</span> <span class="n">ZRC</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="o">((</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>
</pre></div>

#### [ Gabriel Ebner (Aug 03 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130850898):
<p>You can use <code>set_option trace.simplify.rewrite true</code> to find the corresponding lemmas.</p>

#### [ Kevin Buzzard (Aug 03 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130851433):
<p>Oh many thanks Gabriel! I think I can take it from here</p>

#### [ Chris Hughes (Aug 03 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130852441):
<p>Q - &gt; R is noncomputable, I'm guessing because it's defined to any field using division and the integer coercion and division is noncomputable on the reals. There is a computable function Q-&gt;R, the constant sequence, but that would be less general than the current Q coercion, and computable reals are useless anyway.</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882150):
<p>"computable reals are useless anyway" -- maybe to you. But to a beginner, I think</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="mi">1</span><span class="bp">/</span><span class="mi">2</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">definition &#39;x&#39; is noncomputable, it depends on &#39;real.division_ring&#39;</span>
<span class="cm">-/</span>
</pre></div>


<p>is very confusing. What's so noncomputable about 1/2?</p>

#### [ Kenny Lau (Aug 04 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882160):
<p>I hear they have a computable division by positive numbers</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882206):
<p>there is a manual coercion from Q if you really care about defining 1/2 computably, but the point is that it's not the object but the way it is defined that makes it noncomputable</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882208):
<p>The default coercion from nat to int isn't the generic one from nat to any semiring, it's the constructor, and my understanding was that this decision was made for efficiency reasons.</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882217):
<p>Is there a similar argument saying that the default coercion from Q to R should be the one that's staring you in the face rather than the generic one?</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882218):
<p>i.e. the constant series</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882221):
<p>These are implementation issues I guess, which I of course know nothing about in practice</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882261):
<p>Short answer yes</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882268):
<p>But this road leads to the same confusion as why <code>int.coe_nat_*</code> and <code>nat.cast_*</code> have parallel but apparently identical statements</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882313):
<p>look ma, no <code>noncomputable</code></p>
<div class="codehilite"><pre><span></span>import data.real.basic
def one_half : ℝ := real.of_rat (1/2)
theorem one_half_eq : one_half = 1/2 := by simp [one_half]
</pre></div>

#### [ Kevin Buzzard (Aug 04 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882432):
<blockquote>
<p>But this road leads to the same confusion as why <code>int.coe_nat_*</code> and <code>nat.cast_*</code> have parallel but apparently identical statements</p>
</blockquote>
<p>Right. And as you know I've been thinking about this recently (I'm trying to write some undergraduate example sheets which look like maths but are actually not hard to do in Lean for a beginner). A decision was made to not use the generic coercion, this then causes some issues like <code>int.coe_nat...</code> v <code>nat.cast...</code>, these are solved by the devs, the right simp lemmas are proved, people like me learn (in my case, yesterday) that if you use <code>\u</code> then everything should be fine, and then we move on. The devs could do the same for Q -&gt; R, right? Chris seems to think there's no point because who cares about computable reals, but I'm suggesting that there might be a point which has something to do with efficiency somehow.</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882438):
<blockquote>
<p>this decision was made for efficiency reasons</p>
</blockquote>
<p>Actually it's the opposite. Efficiency would dictate using <code>real.of_rat</code> because it has the more natural implementation, and is exponentially faster if you actually run it. The decision was made for uniformity of the library - in the lean 2 library we had all 10 coercions N-&gt;Z-&gt;Q-&gt;R-&gt;C and 10 sets of lemmas about them (plus some extras for the 15 ways to combine them), while the <code>nat.cast</code> approach requires only 4 coercions and sets of lemmas</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882490):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">one_half</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="n">real</span><span class="bp">.</span><span class="n">of_rat</span> <span class="o">(</span><span class="mi">1</span><span class="bp">/</span><span class="mi">2</span><span class="o">)</span>
<span class="kn">theorem</span> <span class="n">one_half_eq</span> <span class="o">:</span> <span class="n">one_half</span> <span class="bp">=</span> <span class="mi">1</span><span class="bp">/</span><span class="mi">2</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">one_half</span><span class="o">]</span>

<span class="n">noncomputable</span> <span class="n">def</span> <span class="n">real_half</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">one_half</span> <span class="bp">=</span> <span class="n">real_half</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">one_half</span><span class="o">]</span> <span class="c1">-- fails</span>
</pre></div>


<p>aargh. Lean why u hate me</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882491):
<p>If you work with reals and don't want to be surprised by <code>noncomputable</code> markings, just put <code>noncomputable theory</code> at the top. It's not worth the digression for newbies</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882497):
<p>Oh that's a good idea.</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882536):
<p>you have to unfold both</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882544):
<blockquote>
<p>you have to unfold both</p>
</blockquote>
<p>I know that <code>rw</code> won't unfold. <code>simp</code> is the same? If I had to simplify something, I think I'd be tempted to start unfolding right at the start.</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882591):
<p>again, you should remember gabriel's advice from yesterday: <code>simp</code> cares about how you write things, so if you hide something behind a definition you can break some <code>simp</code> proofs</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882594):
<p>yes exactly.</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882595):
<p><code>simp</code> will only unfold things you tell it to</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882598):
<p>I feel like I really understand how to use <code>rw</code> now but I'm still getting the hang of <code>simp</code>. There is an art to all these things.</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882643):
<p>I don't want to work with reals at all, it's just that the 250 people in front of me in October are all familiar with them (at some level -- at some other level they don't have a clue what they are, and don't have a clue that they don't know, but I don't mean that; I mean they're not scared of them). So it's very natural to use them whenever I want a random big set. They show up on the first example sheet. I've been looking back at my work from last October when I was working on my own example sheets. It took me 150 lines of code to prove that 1/2 : real wasn't an integer :-)</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882651):
<p>I honestly think you can use <code>Q</code> for all those types of theorems and have a much better day</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882653):
<p>I honestly believe you.</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882693):
<p>I had a principle back then -- "don't change the example sheets; that would be a compromise"</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882697):
<p>just say "there are some complications with using reals so we'll use Q for now" at the start of class and come back to it when you are ready (or not at all)</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882704):
<p><a href="https://github.com/kbuzzard/xena/blob/master/M1F/2016-17/example_sheets/exsht1.pdf" target="_blank" title="https://github.com/kbuzzard/xena/blob/master/M1F/2016-17/example_sheets/exsht1.pdf">https://github.com/kbuzzard/xena/blob/master/M1F/2016-17/example_sheets/exsht1.pdf</a></p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882712):
<p>Sheet 1 Q6 -- I was told "this is not possible in Lean because your sets are stupid"</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882713):
<p>I had to start compromising pretty quickly</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882758):
<p>Heh - I could show you how to define that using inductive types</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882761):
<p>or trees</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882762):
<p><a href="https://github.com/kbuzzard/xena/blob/2bf7737bc0fbcd3943ddadfb513bd19c1eea14a3/xenalib/half_not_an_integer.lean#L116" target="_blank" title="https://github.com/kbuzzard/xena/blob/2bf7737bc0fbcd3943ddadfb513bd19c1eea14a3/xenalib/half_not_an_integer.lean#L116">https://github.com/kbuzzard/xena/blob/2bf7737bc0fbcd3943ddadfb513bd19c1eea14a3/xenalib/half_not_an_integer.lean#L116</a></p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882768):
<p>triumphant proof that 1/2 wasn't an integer, so I could do Q7 part (i)</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882769):
<p>Kind of amazing that I didn't give up there and then</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882772):
<p>to do example sheet 2 I had to write my own square root function</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882815):
<p>it occurs to me that it is really easy to prove that over Q</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882816):
<p>since 1/2 has denom 2 and integers have denom 1</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882817):
<p>right</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882821):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">lemma</span> <span class="n">rational_half_not_an_integer</span> <span class="o">:</span> <span class="bp">¬</span> <span class="bp">∃</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="o">(</span><span class="mi">1</span><span class="bp">/</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="c1">-- proof by contradiction</span>
  <span class="n">rintros</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span><span class="n">Hn</span><span class="bp">⟩</span><span class="o">,</span> <span class="c1">-- n is an integer, Hn the proof that 1/2 = n</span>
  <span class="c1">-- goal is &quot;false&quot;</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">rat</span><span class="bp">.</span><span class="n">coe_int_denom</span> <span class="n">n</span><span class="o">,</span> <span class="c1">-- H says denominator of n is 1</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">Hn</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span> <span class="c1">-- H now says denominator of 1/2 is 1...</span>
  <span class="n">revert</span> <span class="n">H</span><span class="o">,</span><span class="n">exact</span> <span class="n">dec_trivial</span> <span class="c1">-- ...but denominator of 1/2 isn&#39;t 1.</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">real_half_not_an_integer</span> <span class="o">:</span> <span class="bp">¬</span> <span class="bp">∃</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="o">(</span><span class="mi">1</span><span class="bp">/</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rintro</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span><span class="n">Hn</span><span class="bp">⟩</span><span class="o">,</span> <span class="c1">-- n is an integer, Hn the proof that it&#39;s 1/2</span>
  <span class="n">apply</span> <span class="n">rational_half_not_an_integer</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="n">n</span><span class="o">,</span>
  <span class="c1">-- now our hypothesis is that 1/2 = n as reals, and we want to</span>
  <span class="c1">-- deduce 1/2 = n as rationals!</span>
  <span class="c1">-- This is possible by some messing around with coercionc</span>
  <span class="c1">-- from integers to rationals to reals.</span>
  <span class="n">rw</span> <span class="err">←</span><span class="bp">@</span><span class="n">rat</span><span class="bp">.</span><span class="n">cast_inj</span> <span class="n">ℝ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">(</span><span class="k">show</span> <span class="o">((</span><span class="n">n</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="k">by</span> <span class="n">simp</span><span class="o">),</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">Hn</span><span class="o">,</span>
  <span class="n">simp</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Aug 04 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882823):
<p>Current version of 2018 proof</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882828):
<p>no having to define my own floor function in sight!</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882830):
<p>and a lot less than 150 lines too</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882831):
<p>and Gabriel's proof right there at the end</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882870):
<p>There is a name for that lemma</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882872):
<p>you don't have to <code>show by simp</code></p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882873):
<p>yes, I even looked it up</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882875):
<p>as Gabriel suggested</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882881):
<p>in fact did you know that whenever you use simp, you can actually replace it with lemmas which have names?</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882883):
<p>;-)</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882894):
<p>the advantage of <code>simp</code> is when there are a lot of lemmas, applied in complicated positions</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882934):
<p>I am sort-of confused by this. I never know whether to write <code>assumption</code> or <code>exact H27</code>...</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882938):
<p>when the theorem name is shorter than the statement I prefer <code>rw</code></p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882939):
<p>...and I never know whether to write <code>simp</code> or to write <code>simp</code> and then look what it did and write that instead.</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882952):
<p>Hmm, so maybe the answer is "it depends"</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130882959):
<p>I prefer <code>exact H27</code> over <code>assumption</code>, indeed I rarely use <code>assumption</code> because it is longer, less descriptive, and possibly time consuming if it normalizes an irrelevant hypothesis</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883098):
<p>This code above has a rather strange role to play. My current idea is to present the example sheet questions and at the top have a list of lemmas which the students might find helpful. This is example sheet 1 so I'll probably get a lot of people trying it; many will have given up by sheet 2. My plan as I say was to list useful lemmas at the top which they will need, and then hopefully they can prove all the parts of Q7 with rewrites and exact. One of the lemmas I was going to offer them was the proof that 1/2 wasn't an integer, because they need it for Q7(i). But I was going to say "don't worry about these lemmas, just assume them, however anyone interested in what is going on here might want to take a look at them". So I was thinking that the code above would only be seen by people who were interested in what Lean was doing but knew nothing about Lean at all; hence the comments everywhere and the decision to use simp instead of a lemma with a to-them-incomprehensible name</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883113):
<p>My goal was to stick with R but to give them the lemmas they need and then to see how well they did.</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883158):
<p>I was going to get my xena undergrads to test out the problems in Sept and report back.</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883160):
<p>example of <code>assumption</code> going wrong:</p>
<div class="codehilite"><pre><span></span>example {p : Prop} (h1 : if 10^4 = 10^4 then true else true)
  (hp : p) : p := by assumption
</pre></div>

#### [ Kevin Buzzard (Aug 04 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883165):
<p>I will happily never use <code>assumption</code> again.</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883168):
<p>except for those funny cases when you prove lots of cases at once after a semicolon</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883179):
<p>a somewhat nicer form of <code>assumption</code> which you may not know is the french quotes <code>‹p›</code></p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883183):
<p>Whenever I see people using that I always figure that they should be doing something else</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883240):
<p>I have started using the french quotes to refer to instances that I don't want to name, when I need to refer to them directly for some reason</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883243):
<p>Actually I think that's not assumption going wrong</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883255):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="k">if</span> <span class="mi">10</span><span class="err">^</span><span class="mi">4</span> <span class="bp">=</span> <span class="mi">10</span><span class="err">^</span><span class="mi">4</span> <span class="k">then</span> <span class="n">true</span> <span class="k">else</span> <span class="n">true</span><span class="o">)</span>
  <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="o">:=</span>
  <span class="k">begin</span>

  <span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Aug 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883259):
<p>already times out</p>

#### [ Kevin Buzzard (Aug 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883261):
<p>but I do believe you</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883269):
<p>That is a recently discovered mystery for me</p>

#### [ Mario Carneiro (Aug 04 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883340):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> Do you know what preprocessing is done on the context before a <code>begin end</code> block and why? This also came up with the person who was trying to pattern match on a beta redex in the goal only to find it was already reduced before the tactic got to it</p>

#### [ Mario Carneiro (Aug 04 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883470):
<p>this is a better example</p>
<div class="codehilite"><pre><span></span>example {n : ℕ} (h1 : (if 10^4 = 10^4 then 1 else 1) = 1)
  (hp : n = 1) : n = 1 := by assumption
</pre></div>

#### [ Mario Carneiro (Aug 04 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883516):
<p>in the original example the timeout is because <code>h1</code> has a type which is not obviously even a type, so it has to do the expensive evaluation to find out if it is a type</p>

#### [ Mario Carneiro (Aug 04 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883597):
<p>Wow, even this times out</p>
<div class="codehilite"><pre><span></span>def q : Prop := if 10^4 = 10^4 then true else true
example (h : q) : q := h
</pre></div>

#### [ Mario Carneiro (Aug 04 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883599):
<p>but <code>example : q → q := id</code> is okay</p>

#### [ Mario Carneiro (Aug 04 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130883891):
<p>Here is an example of an interesting partial reduction:</p>
<div class="codehilite"><pre><span></span>example : (λ x, x ∧ x) ((λ x, x) true) :=
by tactic.target &gt;&gt;= tactic.trace
-- (λ (x : Prop), x) true ∧ (λ (x : Prop), x) true
</pre></div>


<p>It looks like the goal has whnf applied first</p>

#### [ Sebastian Ullrich (Aug 04 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130898994):
<p>I wouldn't even know where to start looking for the whnf</p>

#### [ Mario Carneiro (Aug 04 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Coercions%20N-%3EZ-%3EQ-%3ER-%3EC/near/130899271):
<p>My guess is that it is making sure it is a sort first</p>


{% endraw %}
