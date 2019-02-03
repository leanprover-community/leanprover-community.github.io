---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/70542intcoenatmulisntnatcastmul.html
---

## Stream: [maths](index.html)
### Topic: [int.coe_nat_mul isn't nat.cast_mul](70542intcoenatmulisntnatcastmul.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 01 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.coe_nat_mul%20isn%27t%20nat.cast_mul/near/130677240):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_mul</span> <span class="c1">-- int.coe_nat_mul : ∀ (m n : ℕ), ↑(m * n) = ↑m * ↑n -- this is in ℤ</span>
<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_mul</span> <span class="c1">-- nat.cast_mul : ∀ {α : Type u_1} [_inst_1 : semiring α] (m n : ℕ), ↑(m * n) = ↑m * ↑n</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">semiring</span> <span class="bp">ℤ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="c1">-- fine</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="err">↑</span><span class="o">(</span><span class="n">m</span> <span class="bp">*</span> <span class="n">n</span><span class="o">):</span><span class="bp">ℤ</span><span class="o">)</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">m</span> <span class="bp">*</span> <span class="err">↑</span><span class="n">n</span> <span class="o">:=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_mul</span> <span class="n">m</span> <span class="n">n</span> <span class="c1">-- fails</span>

<span class="c">/-</span><span class="cm"> full error with pp.all true:</span>
<span class="cm">synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized</span>
<span class="cm">  @coe_to_lift.{1 1} nat int (@coe_base.{1 1} nat int int.has_coe)</span>
<span class="cm">inferred</span>
<span class="cm">  @coe_to_lift.{1 1} nat int</span>
<span class="cm">    (@coe_base.{1 1} nat int</span>
<span class="cm">       (@nat.cast_coe.{0} int (@mul_zero_class.to_has_zero.{0} int (@semiring.to_mul_zero_class.{0} int int.semiring))</span>
<span class="cm">          (@monoid.to_has_one.{0} int (@semiring.to_monoid.{0} int int.semiring))</span>
<span class="cm">          (@distrib.to_has_add.{0} int (@semiring.to_distrib.{0} int int.semiring))))</span>
<span class="cm">-/</span>
</pre></div>


<p>It seems that the coercion from nat to int isn't the one from nat to a general semiring. This means that I am having to write a bunch of functions twice, e.g.</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_pow</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="err">^</span> <span class="n">m</span> <span class="bp">=</span> <span class="o">(</span><span class="n">n</span> <span class="err">^</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_one</span><span class="bp">.</span><span class="n">symm</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">d</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="k">show</span> <span class="err">↑</span><span class="n">n</span> <span class="bp">*</span> <span class="err">↑</span><span class="n">n</span> <span class="err">^</span> <span class="n">d</span> <span class="bp">=</span> <span class="err">↑</span><span class="o">(</span><span class="n">n</span> <span class="err">^</span> <span class="n">d</span> <span class="bp">*</span> <span class="n">n</span><span class="o">),</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_pow</span><span class="o">,</span><span class="n">mul_comm</span><span class="o">,</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_mul</span><span class="o">]</span>

<span class="kn">theorem</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_pow&#39;</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="err">^</span> <span class="n">m</span> <span class="bp">=</span> <span class="o">(</span><span class="n">n</span> <span class="err">^</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_one</span><span class="bp">.</span><span class="n">symm</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">d</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="k">show</span> <span class="err">↑</span><span class="n">n</span> <span class="bp">*</span> <span class="err">↑</span><span class="n">n</span> <span class="err">^</span> <span class="n">d</span> <span class="bp">=</span> <span class="err">↑</span><span class="o">(</span><span class="n">n</span> <span class="err">^</span> <span class="n">d</span> <span class="bp">*</span> <span class="n">n</span><span class="o">),</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_pow&#39;</span><span class="o">,</span><span class="n">mul_comm</span><span class="o">,</span><span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_mul</span><span class="o">]</span>
</pre></div>


<p>Maybe the last one should be <code>int.coe_nat_pow</code> or something? Am I missing a trick? I'm trying to move smoothly between the naturals, the integers, and the integers mod p.</p>

#### [ Kevin Buzzard (Aug 01 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.coe_nat_mul%20isn%27t%20nat.cast_mul/near/130677411):
<p>[I'm threatening to add some of these functions to my brief <code>nat</code> PR by the way]</p>

#### [ Mario Carneiro (Aug 01 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.coe_nat_mul%20isn%27t%20nat.cast_mul/near/130682881):
<p>Yes. There are two coercions from N to Z, with different names. They are proven the same, so given one theorem the other isn't far away, but you have to have both sets of theorems</p>

#### [ Mario Carneiro (Aug 01 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.coe_nat_mul%20isn%27t%20nat.cast_mul/near/130682992):
<p>There are also two power functions N -&gt; N -&gt; N, with different names, the specialization of <code>monoid.pow</code> and <code>nat.pow</code>, again they are proven the same and a simp lemma will translate one to the other</p>

#### [ Mario Carneiro (Aug 01 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.coe_nat_mul%20isn%27t%20nat.cast_mul/near/130683031):
<p>In both cases you can put the blame on the fact that the special case is defined in lean core and mathlib can't undefine it, although I'm not sure I would remove <code>int.coe_nat</code> if I could</p>


{% endraw %}
