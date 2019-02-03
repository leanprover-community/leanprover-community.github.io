---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25036golfchallenge.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [golf challenge](https://leanprover-community.github.io/archive/113488general/25036golfchallenge.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Jan 29 2019 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20challenge/near/157091599):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span><span class="bp">.</span><span class="n">basic</span> <span class="n">data</span><span class="bp">.</span><span class="n">polynomial</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">multivariate_polynomial</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span>

<span class="kn">namespace</span> <span class="n">mv_polynomial</span>

<span class="kn">variables</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">β</span><span class="o">]</span>

<span class="n">def</span> <span class="n">option_ring_equiv_aux11</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">polynomial</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="n">β</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">polynomial</span><span class="bp">.</span><span class="n">C</span> <span class="err">∘</span> <span class="n">C</span>

<span class="kn">instance</span> <span class="n">option_ring_equiv_aux12</span> <span class="o">:</span> <span class="n">ring</span> <span class="o">(</span><span class="n">polynomial</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="n">β</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">comm_ring</span><span class="bp">.</span><span class="n">to_ring</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">comm_ring</span>

<span class="kn">instance</span> <span class="n">option_ring_equiv_aux13</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">polynomial</span><span class="bp">.</span><span class="n">C</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="n">β</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">polynomial</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="n">β</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">apply</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">C</span><span class="bp">.</span><span class="n">is_ring_hom</span>

<span class="kn">instance</span> <span class="n">option_ring_equiv_aux14</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">option_ring_equiv_aux11</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">comp</span> <span class="bp">_</span> <span class="bp">_</span>

<span class="kn">instance</span> <span class="n">option_ring_equiv_aux15</span> <span class="o">:</span> <span class="n">is_semiring_hom</span> <span class="o">(</span><span class="n">option_ring_equiv_aux11</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">is_semiring_hom</span> <span class="bp">_</span>

<span class="n">def</span> <span class="n">option_ring_equiv_aux1</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="o">(</span><span class="n">option</span> <span class="n">β</span><span class="o">)</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">polynomial</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="n">β</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">eval₂</span> <span class="o">(</span><span class="n">option_ring_equiv_aux11</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">option</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">x</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">X</span> <span class="o">(</span><span class="n">polynomial</span><span class="bp">.</span><span class="n">C</span> <span class="err">∘</span> <span class="n">X</span><span class="o">))</span>

<span class="n">def</span> <span class="n">option_ring_equiv_aux21</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="n">β</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">mv_polynomial</span> <span class="o">(</span><span class="n">option</span> <span class="n">β</span><span class="o">)</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">eval₂</span> <span class="n">C</span> <span class="o">(</span><span class="n">X</span> <span class="err">∘</span> <span class="n">some</span><span class="o">)</span>

<span class="kn">instance</span> <span class="n">option_ring_equiv_aux22</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">option_ring_equiv_aux21</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">convert</span> <span class="n">eval₂</span><span class="bp">.</span><span class="n">is_ring_hom</span> <span class="bp">_</span> <span class="bp">_;</span> <span class="n">apply_instance</span>

<span class="kn">instance</span> <span class="n">option_ring_equiv_aux23</span> <span class="o">:</span> <span class="n">is_semiring_hom</span> <span class="o">(</span><span class="n">option_ring_equiv_aux21</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">is_semiring_hom</span> <span class="bp">_</span>

<span class="n">def</span> <span class="n">option_ring_equiv_aux2</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="n">β</span> <span class="n">α</span><span class="o">)</span> <span class="bp">→</span> <span class="n">mv_polynomial</span> <span class="o">(</span><span class="n">option</span> <span class="n">β</span><span class="o">)</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">polynomial</span><span class="bp">.</span><span class="n">eval₂</span> <span class="o">(</span><span class="n">option_ring_equiv_aux21</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">X</span> <span class="n">none</span><span class="o">)</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">}</span>
<span class="kn">set_option</span> <span class="n">class</span><span class="bp">.</span><span class="n">instance_max_depth</span> <span class="mi">5</span>
<span class="kn">theorem</span> <span class="n">option_ring_equiv_aux3</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="o">(</span><span class="n">option</span> <span class="n">β</span><span class="o">)</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">option_ring_equiv_aux2</span> <span class="n">α</span> <span class="n">β</span> <span class="o">(</span><span class="n">option_ring_equiv_aux1</span> <span class="n">α</span> <span class="n">β</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">:=</span>
<span class="n">induction_on</span> <span class="n">f</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">r</span><span class="o">,</span> <span class="k">calc</span> <span class="n">option_ring_equiv_aux2</span> <span class="n">α</span> <span class="n">β</span> <span class="o">(</span><span class="n">option_ring_equiv_aux1</span> <span class="n">α</span> <span class="n">β</span> <span class="o">(</span><span class="n">C</span> <span class="n">r</span><span class="o">))</span>
           <span class="bp">=</span> <span class="n">option_ring_equiv_aux2</span> <span class="n">α</span> <span class="n">β</span> <span class="o">(</span><span class="n">option_ring_equiv_aux11</span> <span class="n">α</span> <span class="n">β</span> <span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="k">by</span> <span class="n">congr&#39;</span> <span class="mi">1</span><span class="bp">;</span> <span class="n">convert</span> <span class="n">eval₂_C</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_;</span> <span class="n">convert</span> <span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">option_ring_equiv_aux15</span> <span class="n">α</span> <span class="n">β</span>
       <span class="bp">...</span> <span class="bp">=</span> <span class="n">option_ring_equiv_aux21</span> <span class="n">α</span> <span class="n">β</span> <span class="o">(</span><span class="n">C</span> <span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="k">by</span> <span class="n">convert</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">eval₂_C</span> <span class="bp">_</span> <span class="bp">_;</span> <span class="n">apply_instance</span>
       <span class="bp">...</span> <span class="bp">=</span> <span class="n">C</span> <span class="n">r</span> <span class="o">:</span> <span class="k">by</span> <span class="n">convert</span> <span class="n">eval₂_C</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_;</span> <span class="n">apply_instance</span><span class="o">)</span>
  <span class="n">sorry</span>
  <span class="n">sorry</span>

<span class="kn">end</span> <span class="n">mv_polynomial</span>
</pre></div>

#### [ Kenny Lau (Jan 29 2019 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20challenge/near/157091612):
<p>challenge: shorten this code, but keep the compiling time low</p>

#### [ Kenny Lau (Jan 29 2019 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20challenge/near/157091663):
<p>(yes, the <code>set_option class.instance_max_depth 5</code> line is there to keep the compiling time low)</p>

#### [ Kenny Lau (Jan 29 2019 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20challenge/near/157091668):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span></p>

#### [ Kenny Lau (Jan 29 2019 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20challenge/near/157101129):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span></p>

#### [ Johannes Hölzl (Jan 30 2019 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20challenge/near/157194471):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span>  I think we have a problem either with the ring homomorphisms, or some of the mv_polynomial instances... I changed the proof to <code>mv_polynomial (β ⊕ γ) α ≃r mv_polynomial β (mv_polynomial γ α)</code>, allowing also the symmetric variant.</p>

#### [ Kenny Lau (Jan 30 2019 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20challenge/near/157194503):
<p>are you planning to put this into mathlib? I'm about to prove the same theorem</p>

#### [ Johannes Hölzl (Jan 30 2019 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20challenge/near/157194621):
<p>its already in master</p>

#### [ Johannes Hölzl (Jan 30 2019 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20challenge/near/157194636):
<p><a href="https://github.com/leanprover/mathlib/commit/f7b9d6b43e478661eb87fef36c75e8e4ffc08499" target="_blank" title="https://github.com/leanprover/mathlib/commit/f7b9d6b43e478661eb87fef36c75e8e4ffc08499">https://github.com/leanprover/mathlib/commit/f7b9d6b43e478661eb87fef36c75e8e4ffc08499</a></p>

#### [ Kenny Lau (Jan 30 2019 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20challenge/near/157194647):
<p>oh nice!</p>

#### [ Johan Commelin (Jan 30 2019 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/golf%20challenge/near/157194863):
<p>Aah, using <code>rename</code> we might be able to slightly cleanup the <code>mv_polynomial</code> adjunction that I PR'd a while ago.</p>


{% endraw %}
