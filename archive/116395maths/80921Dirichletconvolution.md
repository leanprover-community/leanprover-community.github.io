---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/80921Dirichletconvolution.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Dirichlet convolution](https://leanprover-community.github.io/archive/116395maths/80921Dirichletconvolution.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Elliott Macneil (Aug 15 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182031):
<p>I'm trying to define the Dirichlet convolution on two arithmetic functions f,g but I'm having difficulty with writing the following sum in Lean.</p>
<p><span class="katex-display"><span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="normal">Σ</mi><mrow><mi>d</mi><mo>∣</mo><mi>n</mi></mrow></msub><mi>f</mi><mo>(</mo><mi>d</mi><mo>)</mo><mi>g</mi><mo>(</mo><mi>n</mi><mi mathvariant="normal">/</mi><mi>d</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\Sigma_{d \mid n } f(d) g(n/d)</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1.1052em;vertical-align:-0.3551999999999999em;"></span><span class="base"><span class="mord"><span class="mord mathrm">Σ</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.34480000000000005em;"><span style="top:-2.5198em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">d</span><span class="mrel mtight">∣</span><span class="mord mathit mtight">n</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.3551999999999999em;"></span></span></span></span></span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit">d</span><span class="mclose">)</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mord mathrm">/</span><span class="mord mathit">d</span><span class="mclose">)</span></span></span></span></span></p>
<p>Could anyone possibly  write this in Lean?</p>

#### [ Kevin Buzzard (Aug 15 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182207):
<p>Elliott I pushed a function which did this this morning.</p>

#### [ Kevin Buzzard (Aug 15 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182215):
<p>What does this mean if n=0?</p>

#### [ Kevin Buzzard (Aug 15 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182218):
<p>I stuck to <code>pnat</code></p>

#### [ Kevin Buzzard (Aug 15 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182242):
<p><a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/M3P14/sum_over_divisors.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/M3P14/sum_over_divisors.lean">https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/M3P14/sum_over_divisors.lean</a></p>

#### [ Kevin Buzzard (Aug 15 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182326):
<p>so it's <code>\lam (n : pnat), divisor_sum (\lam d, f d * g (n / d)) n</code></p>

#### [ Mario Carneiro (Aug 15 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182441):
<div class="codehilite"><pre><span></span>lemma mem_factors_iff_divides (d : ℕ+) (e : ℕ) : e ∈ factors d ↔ e ∣ d :=
by simp [factors, -add_comm, nat.lt_succ_iff];
   exact and_iff_right_of_imp (le_of_dvd d.2)
</pre></div>

#### [ Mario Carneiro (Aug 15 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182491):
<p>see, <code>logic.basic</code> is useful</p>

#### [ Mario Carneiro (Aug 15 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182531):
<p>you can also define <code>factors</code> using <code>finset.filter</code> to avoid the nodup proof</p>

#### [ Kevin Buzzard (Aug 15 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132185364):
<p>Thanks and thanks! I was surprised that the divisors function (sending a pnat to a finset of its divisors) wasn't there, but Chris said he hadn't seen it (he had seen <code>factors</code> which in my mind is synonymous, however he said <code>factors</code> was the list of prime factors of n, which is not how the word is usually used in mathematics: factor does not imply prime).</p>

#### [ Mario Carneiro (Aug 15 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132185538):
<p>I had the same train of thought</p>

#### [ Mario Carneiro (Aug 15 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132185596):
<p>maybe it should be called <code>factorization</code></p>

#### [ Mario Carneiro (Aug 15 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132185612):
<p>note that it is not just the set of prime factors, it is like a multiset</p>

#### [ Kevin Buzzard (Aug 15 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132185688):
<p>I should use simp for iff statements more...</p>

#### [ Elliott Macneil (Aug 15 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132191813):
<p>Thanks for the help!</p>


{% endraw %}
