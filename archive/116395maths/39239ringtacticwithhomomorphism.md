---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/39239ringtacticwithhomomorphism.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [ring tactic with homomorphism](https://leanprover-community.github.io/archive/116395maths/39239ringtacticwithhomomorphism.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Apr 30 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125892370):
<p>Consider the following MWE</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>
<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">open</span> <span class="n">real</span>

<span class="n">def</span> <span class="n">f</span> <span class="o">:</span> <span class="bp">ℤ</span> <span class="bp">→</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">3</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">4</span><span class="o">)</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">10</span> <span class="bp">+</span> <span class="mi">7</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span>
<span class="o">:=</span> <span class="k">by</span> <span class="n">ring</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">3</span><span class="o">)</span> <span class="bp">*</span> <span class="n">f</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">4</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">f</span> <span class="n">n</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">f</span> <span class="n">n</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">10</span> <span class="bp">+</span> <span class="mi">7</span> <span class="bp">*</span> <span class="o">(</span><span class="n">f</span> <span class="n">n</span><span class="o">)</span> <span class="bp">+</span> <span class="n">f</span> <span class="mi">2</span>
<span class="o">:=</span> <span class="k">by</span> <span class="n">ring</span> <span class="c1">-- fails</span>
</pre></div>

#### [ Johan Commelin (Apr 30 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125892380):
<p>How hard would it be to teach the <code>ring</code> tactic to use the axioms for ring homomorphisms?</p>

#### [ Kevin Buzzard (Apr 30 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125897415):
<p>You could start by making f part of the <code>is_ring_hom</code> class.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125897515):
<p><code>instance f_is_a_ring_hom : is_ring_hom f := { map_add := sorry,map_mul := sorry,map_one := sorry}</code> is how to start</p>

#### [ Kevin Buzzard (Apr 30 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125897567):
<p>and then you need to fill in the proofs, which are all already there, with names I can't quite remember yet, hang on.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125897592):
<p>They are probably called things like <code>cast_mul</code>, <code>cast_add</code> and <code>cast_one</code>.</p>

#### [ Chris Hughes (Apr 30 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125900450):
<p>I think the difficult part is getting <code>ring</code> to recognize <code>f 2 + f3 = f 5</code>. Apart from the problem with literals you can just <code>simp[is_ring_hom.map_add]</code> etc first.</p>

#### [ Johan Commelin (Apr 30 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125902537):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Right..., so maybe instead of defining <code>f</code>, I should actually just assume that it is a ring hom. Maybe Lean should be able to deduce itself that this determines <code>f</code> completely!</p>

#### [ Johan Commelin (Apr 30 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125902564):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> Yes, I understand. But I really want Lean to deal with these things using only one straightforward tactic. After all, it is one of these “mathematically trivial” steps.</p>

#### [ Chris Hughes (Apr 30 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125902597):
<p>I'm saying that it should be easy to add it to the ring tactic, if all it requires is a <code>simp</code> in the definition of <code>ring</code></p>

#### [ Johan Commelin (Apr 30 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125902666):
<p>Aaah, I see. Yes, that is true.</p>

#### [ Mario Carneiro (May 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20tactic%20with%20homomorphism/near/125920901):
<p>I'm not so sure about adding this to <code>ring</code>. This is outside the scope of <code>ring</code> as I see it, which is to solve equations in the first order theory of rings. If you want something like this it should be a different tactic; as Chris says it may be as simple as just <code>simp</code> with an appropriate simp set followed by <code>ring</code>.</p>


{% endraw %}
