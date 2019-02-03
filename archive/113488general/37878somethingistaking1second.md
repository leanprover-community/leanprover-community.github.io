---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37878somethingistaking1second.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [something is taking 1 second](https://leanprover-community.github.io/archive/113488general/37878somethingistaking1second.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Jul 23 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/something%20is%20taking%201%20second/near/130147638):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">multivariate_polynomial</span>

<span class="n">universes</span> <span class="n">u</span>

<span class="kn">namespace</span> <span class="n">mv_polynomial</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">σ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">σ</span><span class="o">]</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="n">σ</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">to_comm_ring</span>

<span class="kn">instance</span> <span class="n">C_is_ring_hom</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">mv_polynomial</span> <span class="n">σ</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">map_one</span> <span class="o">:=</span> <span class="n">C_1</span><span class="o">,</span>
  <span class="n">map_add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">single_add</span><span class="o">,</span>
  <span class="n">map_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="n">C_mul_monomial</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">mv_polynomial</span>
<span class="kn">open</span> <span class="n">mv_polynomial</span>

<span class="n">noncomputable</span> <span class="n">theory</span>
<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>

<span class="c1">-- def ℤpinv := {x ∈ ℚ | ∃ n : ℕ, ∃ y : ℤ, x * (p:ℚ)^n = y}</span>
<span class="kn">set_option</span> <span class="n">profiler</span> <span class="n">true</span>
<span class="kn">lemma</span> <span class="n">functorial_C_X</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">:</span> <span class="n">functorial</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">mv_polynomial</span> <span class="bp">ℕ</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="n">X</span> <span class="mi">0</span><span class="o">)</span> <span class="bp">=</span> <span class="n">X</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">functorial</span><span class="o">,</span><span class="n">X</span><span class="o">]</span>
<span class="kn">end</span>

<span class="bp">#</span><span class="kn">check</span> <span class="mi">2</span>
</pre></div>

#### [ Kenny Lau (Jul 23 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/something%20is%20taking%201%20second/near/130147646):
<div class="codehilite"><pre><span></span>elaboration of functorial_C_X took 975ms
</pre></div>

#### [ Johan Commelin (Jul 23 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/something%20is%20taking%201%20second/near/130147865):
<p>Over here it isn't even a proof...</p>

#### [ Kenny Lau (Jul 23 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/something%20is%20taking%201%20second/near/130147908):
<p>that's just the first step</p>

#### [ Johan Commelin (Jul 23 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/something%20is%20taking%201%20second/near/130147911):
<p>Ok</p>


{% endraw %}
