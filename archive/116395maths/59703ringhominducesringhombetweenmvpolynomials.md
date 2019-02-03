---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/59703ringhominducesringhombetweenmvpolynomials.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [ring hom induces ring hom between mv_polynomials](https://leanprover-community.github.io/archive/116395maths/59703ringhominducesringhombetweenmvpolynomials.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Jul 24 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130203646):
<p>I am stuck.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">multivariate_polynomial</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span>

<span class="c1">-- ### FOR_MATHLIB</span>
<span class="c1">-- everything in this section should move to other files</span>

<span class="kn">section</span> <span class="n">ring_hom_commutes_with_stuff</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">S</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">i</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">X</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">R</span><span class="o">)</span>

<span class="kn">open</span> <span class="n">finset</span>

<span class="kn">lemma</span> <span class="n">ring_hom_sum</span> <span class="o">:</span> <span class="n">i</span> <span class="o">(</span><span class="n">sum</span> <span class="n">s</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="n">sum</span> <span class="n">s</span> <span class="o">(</span><span class="n">i</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">finset</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">s</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">repeat</span> <span class="o">{</span> <span class="n">rw</span> <span class="n">sum_empty</span> <span class="o">},</span>
    <span class="n">exact</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_zero</span> <span class="n">i</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">intros</span> <span class="n">x</span> <span class="n">s&#39;</span> <span class="n">hx</span> <span class="n">ih</span><span class="o">,</span>
    <span class="n">repeat</span> <span class="o">{</span> <span class="n">rw</span> <span class="n">sum_insert</span> <span class="n">hx</span> <span class="o">},</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_add</span> <span class="n">i</span><span class="o">,</span> <span class="err">←</span><span class="n">ih</span><span class="o">]</span> <span class="o">}</span>
<span class="kn">end</span>

<span class="kn">end</span> <span class="n">ring_hom_commutes_with_stuff</span>

<span class="kn">namespace</span> <span class="n">mv_polynomial</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">σ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">σ</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">S</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">S</span><span class="o">]</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="n">σ</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">to_comm_ring</span>

<span class="kn">instance</span> <span class="n">C_is_ring_hom</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">mv_polynomial</span> <span class="n">σ</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">map_one</span> <span class="o">:=</span> <span class="n">C_1</span><span class="o">,</span>
  <span class="n">map_add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">single_add</span><span class="o">,</span>
  <span class="n">map_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="n">C_mul_monomial</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="n">functorial_is_ring_hom</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">i</span><span class="o">]</span> <span class="o">:</span>
<span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">functorial</span> <span class="n">i</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="n">σ</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">mv_polynomial</span> <span class="n">σ</span> <span class="n">S</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">map_one</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">functorial</span><span class="o">],</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">map_range</span><span class="o">],</span>
    <span class="c1">-- simp [function.comp],</span>
    <span class="n">apply</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">ext</span><span class="o">,</span>
    <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">on_finset_apply</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="bp">*</span><span class="o">,</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">single_apply</span><span class="o">],</span>
    <span class="n">sorry</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">map_add</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">intros</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">functorial</span><span class="o">,</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">map_range</span><span class="o">,</span><span class="n">function</span><span class="bp">.</span><span class="n">comp</span><span class="o">],</span>
    <span class="n">apply</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">ext</span><span class="o">,</span>
    <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="bp">*</span><span class="o">,</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">single_apply</span><span class="o">],</span>
    <span class="n">rw</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_add</span> <span class="n">i</span><span class="o">,</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">map_mul</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">intros</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">functorial</span><span class="o">,</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">map_range</span><span class="o">,</span><span class="n">function</span><span class="bp">.</span><span class="n">comp</span><span class="o">,</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">mul_def</span><span class="o">,</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">sum</span><span class="o">],</span>
    <span class="n">apply</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">ext</span><span class="o">,</span>
    <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="bp">*</span><span class="o">,</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">single_apply</span><span class="o">],</span>
    <span class="n">rw</span> <span class="n">ring_hom_sum</span> <span class="n">i</span><span class="o">,</span>
    <span class="n">sorry</span><span class="o">,</span>
  <span class="kn">end</span> <span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Jul 24 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130203649):
<p>There are two <code>sorry</code>s in that bit of code. I don't know how to get rid of them.</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204295):
<p>I think you are going about this the wrong way, at least if you want a clean proof at the end</p>

#### [ Johan Commelin (Jul 24 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204348):
<p>Hmmm, so what is the right way?</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204353):
<p>You should break the proof into smaller and more useful parts rather than just attacking the whole thing at once</p>

#### [ Johan Commelin (Jul 24 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204372):
<p>Ok, but I think I don't even really see the smaller useful parts...</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204416):
<p>here's the first thing I would prove:</p>
<div class="codehilite"><pre><span></span>theorem map_monomial (f : α → β) [is_ring_hom f]
  (s : σ →₀ ℕ) (a : α) : map f (monomial s a) = monomial s (f a) :=
sorry
</pre></div>

#### [ Mario Carneiro (Jul 24 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204420):
<p>(I renamed <code>functorial</code> to <code>map</code>)</p>

#### [ Johan Commelin (Jul 24 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204431):
<p>It is still called <code>functorial</code> in mathlib right?</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204437):
<p>not in my local copy as of a minute ago</p>

#### [ Johan Commelin (Jul 24 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204440):
<p>Aaah...</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204444):
<p>you can use <code>functorial</code> if it's easier</p>

#### [ Johan Commelin (Jul 24 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204565):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">map_monomial</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">i</span><span class="o">]</span>
  <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">σ</span> <span class="bp">→</span><span class="err">₀</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">:</span> <span class="n">functorial</span> <span class="n">i</span> <span class="o">(</span><span class="n">monomial</span> <span class="n">x</span> <span class="n">r</span><span class="o">)</span> <span class="bp">=</span> <span class="n">monomial</span> <span class="n">x</span> <span class="o">(</span><span class="n">i</span> <span class="n">r</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">functorial</span><span class="o">,</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">map_range</span><span class="o">,</span><span class="n">function</span><span class="bp">.</span><span class="n">comp</span><span class="o">,</span><span class="n">monomial</span><span class="o">],</span>
  <span class="n">apply</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">ext</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="bp">*</span><span class="o">,</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">single_apply</span><span class="o">],</span>
  <span class="n">split_ifs</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">refl</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">apply</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_zero</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Jul 24 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204574):
<p>I am suspicious still</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204577):
<p>that proof is too complicated</p>

#### [ Johan Commelin (Jul 24 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204579):
<p>Hmmm, ok, I'll try to golf it.</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204583):
<p>it should be a one liner about the composition of <code>map_range</code> with <code>single</code></p>

#### [ Chris Hughes (Jul 24 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204641):
<p>Incidentally is <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>  planning on removing the use of <code>monomial</code> for <code>mv_polynomial</code>s like he did for univariate polys?</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204650):
<p>I don't know anything about this</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204658):
<p>oh, I see he just uses <code>single</code></p>

#### [ Chris Hughes (Jul 24 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204702):
<p>The idea is to use <code>C a * X^n</code> instead of <code>monomial</code></p>

#### [ Mario Carneiro (Jul 24 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204707):
<p>For foundational stuff that's no good</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204716):
<p>because the theorems about <code>C a</code> and <code>X</code> come from a theorem on <code>single</code></p>

#### [ Chris Hughes (Jul 24 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204737):
<p>Yeah, but once the foundations are done, users are supposed to use <code>C a * X^n</code> I think.</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204772):
<p>sure</p>

#### [ Johan Commelin (Jul 24 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204773):
<p>/me seems to be a user who has to do some foundational stuff...</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204777):
<p>Johan Commelin has stumbled on a gap in mathlib</p>

#### [ Johan Commelin (Jul 24 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204785):
<p>That's the same thing right?</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204789):
<p>not always</p>

#### [ Johan Commelin (Jul 24 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204793):
<p>fair enough</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204794):
<p>well, I guess that depends on what qualifies as "foundational"</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204803):
<p>in this case the API is clearly lacking, and there is even an "unfinished" comment</p>

#### [ Johan Commelin (Jul 24 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204843):
<p>Written by?</p>

#### [ Johan Commelin (Jul 24 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204847):
<p>Johan Commelin (-;</p>

#### [ Johan Commelin (Jul 24 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204851):
<p>So, I can only blame myself</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204856):
<p><a href="https://github.com/leanprover/mathlib/blob/master/linear_algebra/multivariate_polynomial.lean#L183" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/linear_algebra/multivariate_polynomial.lean#L183">https://github.com/leanprover/mathlib/blob/master/linear_algebra/multivariate_polynomial.lean#L183</a></p>

#### [ Johan Commelin (Jul 24 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204857):
<p>But you can guess why I wrote that comment... because back then I would have been even worse at proving this lemma.</p>

#### [ Johan Commelin (Jul 24 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204864):
<p>Yeah, the <code>git blame</code> is not accurate.</p>

#### [ Kenny Lau (Jul 24 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204865):
<p>I've removed 1 sorry (en hep nok 4 toegevoegt):</p>

#### [ Kenny Lau (Jul 24 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204868):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">multivariate_polynomial</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span> <span class="n">u₁</span>

<span class="c1">-- ### FOR_MATHLIB</span>
<span class="c1">-- everything in this section should move to other files</span>

<span class="kn">section</span> <span class="n">ring_hom_commutes_with_stuff</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">S</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">i</span><span class="o">]</span>

<span class="kn">section</span> <span class="n">finset</span>

<span class="kn">open</span> <span class="n">finset</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">X</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">R</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">ring_hom_sum</span><span class="bp">.</span><span class="n">finset</span> <span class="o">:</span> <span class="n">i</span> <span class="o">(</span><span class="n">sum</span> <span class="n">s</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="n">sum</span> <span class="n">s</span> <span class="o">(</span><span class="n">i</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">finset</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">s</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">repeat</span> <span class="o">{</span> <span class="n">rw</span> <span class="n">sum_empty</span> <span class="o">},</span>
    <span class="n">exact</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_zero</span> <span class="n">i</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">intros</span> <span class="n">x</span> <span class="n">s&#39;</span> <span class="n">hx</span> <span class="n">ih</span><span class="o">,</span>
    <span class="n">repeat</span> <span class="o">{</span> <span class="n">rw</span> <span class="n">sum_insert</span> <span class="n">hx</span> <span class="o">},</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_add</span> <span class="n">i</span><span class="o">,</span> <span class="err">←</span><span class="n">ih</span><span class="o">]</span> <span class="o">}</span>
<span class="kn">end</span>

<span class="kn">end</span> <span class="n">finset</span>

<span class="kn">section</span> <span class="n">finsupp</span>

<span class="kn">open</span> <span class="n">finsupp</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u₁</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_monoid</span> <span class="n">β</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">β</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span><span class="err">₀</span> <span class="n">β</span><span class="o">)</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">hf1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">f</span> <span class="n">a</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">hf2</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">b₁</span> <span class="n">b₂</span> <span class="o">:</span> <span class="n">β</span><span class="o">),</span> <span class="n">f</span> <span class="n">a</span> <span class="o">(</span><span class="n">b₁</span> <span class="bp">+</span> <span class="n">b₂</span><span class="o">)</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">a</span> <span class="n">b₁</span> <span class="bp">+</span> <span class="n">f</span> <span class="n">a</span> <span class="n">b₂</span><span class="o">)</span>
<span class="n">include</span> <span class="n">hf1</span> <span class="n">hf2</span>

<span class="kn">lemma</span> <span class="n">ring_hom_sum</span><span class="bp">.</span><span class="n">finsupp</span> <span class="o">:</span> <span class="n">i</span> <span class="o">(</span><span class="n">sum</span> <span class="n">s</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="n">sum</span> <span class="n">s</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">i</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span> <span class="n">b</span><span class="o">))</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">induction</span> <span class="n">s</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">repeat</span> <span class="o">{</span> <span class="n">rw</span> <span class="n">sum_zero_index</span> <span class="o">},</span>
    <span class="n">exact</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_zero</span> <span class="n">i</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">intros</span> <span class="n">a</span> <span class="n">b</span> <span class="n">f&#39;</span> <span class="n">H1</span> <span class="n">H2</span> <span class="n">ih</span><span class="o">,</span>
    <span class="n">repeat</span> <span class="o">{</span> <span class="n">rw</span> <span class="n">sum_add_index</span> <span class="o">},</span>
    <span class="n">repeat</span> <span class="o">{</span> <span class="n">rw</span> <span class="n">sum_single_index</span> <span class="o">},</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_add</span> <span class="n">i</span><span class="o">,</span> <span class="err">←</span> <span class="n">ih</span><span class="o">],</span>
    <span class="o">{</span> <span class="n">rw</span> <span class="n">hf1</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_zero</span> <span class="n">i</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">apply</span> <span class="n">hf1</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">intros</span><span class="o">,</span> <span class="n">rw</span> <span class="n">hf1</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_zero</span> <span class="n">i</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">intros</span><span class="o">,</span> <span class="n">rw</span> <span class="n">hf2</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_add</span> <span class="n">i</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">apply</span> <span class="n">hf1</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">apply</span> <span class="n">hf2</span> <span class="o">}</span> <span class="o">}</span>
<span class="kn">end</span>

<span class="kn">end</span> <span class="n">finsupp</span>

<span class="kn">end</span> <span class="n">ring_hom_commutes_with_stuff</span>

<span class="kn">namespace</span> <span class="n">mv_polynomial</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">σ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">σ</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">S</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">S</span><span class="o">]</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="n">σ</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">to_comm_ring</span>

<span class="kn">instance</span> <span class="n">C_is_ring_hom</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">mv_polynomial</span> <span class="n">σ</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">map_one</span> <span class="o">:=</span> <span class="n">C_1</span><span class="o">,</span>
  <span class="n">map_add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">single_add</span><span class="o">,</span>
  <span class="n">map_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="n">C_mul_monomial</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="n">functorial_is_ring_hom</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">i</span><span class="o">]</span> <span class="o">:</span>
<span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">functorial</span> <span class="n">i</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="n">σ</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">mv_polynomial</span> <span class="n">σ</span> <span class="n">S</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">map_one</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">functorial</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">map_range</span><span class="o">],</span>
    <span class="n">ext</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">on_finset_apply</span><span class="o">],</span>
    <span class="k">have</span> <span class="n">H1</span> <span class="o">:</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="n">σ</span> <span class="n">R</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="o">(</span><span class="n">σ</span> <span class="bp">→</span><span class="err">₀</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">→</span><span class="err">₀</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">H2</span> <span class="o">:</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="n">σ</span> <span class="n">S</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="o">(</span><span class="n">σ</span> <span class="bp">→</span><span class="err">₀</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">→</span><span class="err">₀</span> <span class="n">S</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">H1</span><span class="o">,</span> <span class="n">H2</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">one_def</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">one_def</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">single_apply</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">single_apply</span><span class="o">],</span>
    <span class="n">split_ifs</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">apply</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_one</span> <span class="n">i</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">apply</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_zero</span> <span class="n">i</span> <span class="o">}</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">map_add</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">intros</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">functorial</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">map_range</span><span class="o">],</span>
    <span class="n">ext</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">single_apply</span><span class="o">,</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_add</span> <span class="n">i</span><span class="o">]</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">map_mul</span> <span class="o">:=</span>
  <span class="k">begin</span>
    <span class="n">intros</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">functorial</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">map_range</span><span class="o">],</span>
    <span class="n">ext</span><span class="o">,</span>
    <span class="n">dsimp</span> <span class="o">[</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">on_finset_apply</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">mul_def</span><span class="o">],</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">sum_apply</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">sum_apply</span><span class="o">,</span> <span class="n">ring_hom_sum</span><span class="bp">.</span><span class="n">finsupp</span> <span class="n">i</span><span class="o">],</span>
    <span class="n">sorry</span><span class="o">,</span> <span class="n">sorry</span><span class="o">,</span> <span class="n">sorry</span><span class="o">,</span> <span class="n">sorry</span><span class="o">,</span> <span class="n">sorry</span>
  <span class="kn">end</span> <span class="o">}</span>

<span class="kn">end</span> <span class="n">mv_polynomial</span>
</pre></div>

#### [ Johan Commelin (Jul 24 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204870):
<p>I wrote that stuff, but didn't actually know what I was doing. So Johannes took my stuff and transformed it into something mathlib-ready.</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204912):
<p>I didn't realize you were an author of the file, you aren't credited if so</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130204920):
<p>I added you as an author</p>

#### [ Johan Commelin (Jul 24 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205097):
<p>Does that bring responsibilities with it? Does that mean I should now be able to answer foundational questions about this file?</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205103):
<p>Not really</p>

#### [ Johan Commelin (Jul 24 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205235):
<p>By the way... I already had:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">functorial_ring_hom_X</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">i</span><span class="o">]</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">σ</span><span class="o">)</span>
 <span class="o">:</span> <span class="n">functorial</span> <span class="n">i</span> <span class="o">(</span><span class="n">X</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">X</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">functorial</span><span class="o">,</span><span class="n">X</span><span class="o">,</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">map_range</span><span class="o">,</span><span class="n">function</span><span class="bp">.</span><span class="n">comp</span><span class="o">,</span><span class="n">C</span><span class="o">,</span><span class="n">monomial</span><span class="o">,</span><span class="bp">*</span><span class="o">],</span>
  <span class="n">apply</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">ext</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="bp">*</span><span class="o">,</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">single_apply</span><span class="o">],</span>
  <span class="n">split_ifs</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">apply</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_one</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">apply</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_zero</span> <span class="o">}</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">functorial_ring_hom_C</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">i</span><span class="o">]</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span>
<span class="o">:</span> <span class="n">functorial</span> <span class="n">i</span> <span class="o">(</span><span class="n">C</span> <span class="n">r</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">C</span> <span class="o">(</span><span class="n">i</span> <span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="n">mv_polynomial</span> <span class="n">σ</span> <span class="n">S</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">functorial</span><span class="o">,</span><span class="n">X</span><span class="o">,</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">map_range</span><span class="o">,</span><span class="n">function</span><span class="bp">.</span><span class="n">comp</span><span class="o">,</span><span class="n">C</span><span class="o">,</span><span class="n">monomial</span><span class="o">,</span><span class="bp">*</span><span class="o">],</span>
  <span class="n">apply</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">ext</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="bp">*</span><span class="o">,</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">single_apply</span><span class="o">],</span>
  <span class="n">split_ifs</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">refl</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">apply</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_zero</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Jul 24 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205239):
<p>But I didn't see how to use them.</p>

#### [ Johan Commelin (Jul 24 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205241):
<p>But maybe I'm learning, because I think it was pretty close to your suggestion about monomials.</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205242):
<p>almost there:</p>
<div class="codehilite"><pre><span></span>-- `mv_polynomial σ` is a functor (incomplete)
def map : mv_polynomial σ α → mv_polynomial σ β :=
map_range f (is_ring_hom.map_zero f)

theorem map_monomial (s : σ →₀ ℕ) (a : α) : map f (monomial s a) = monomial s (f a) :=
map_range_single

theorem map_C (f : α → β) [is_ring_hom f] (a : α) : map f (C a : mv_polynomial σ α) = C (f a) :=
map_monomial _ _ _

theorem map_one (f : α → β) [is_ring_hom f] : map f (1 : mv_polynomial σ α) = 1 :=
(map_C _ _).trans $ by simp [is_ring_hom.map_one f]

theorem map_add (f : α → β) [is_ring_hom f] (p q : mv_polynomial σ α) :
  map f (p + q) = map f p + map f q :=
by simp [map]; ext a; simp [is_ring_hom.map_add f]

theorem map_mul (f : α → β) [is_ring_hom f] (p q : mv_polynomial σ α) :
  map f (p * q) = map f p * map f q :=
sorry
</pre></div>

#### [ Johan Commelin (Jul 24 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205248):
<p>Ok, please add <code>map_X</code>. It will turn out to be really useful.</p>

#### [ Johan Commelin (Jul 24 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205296):
<p>/me wonders when he will ever approximate the overlord-powers of Mario... <span class="emoji emoji-1f914" title="thinking face">:thinking_face:</span></p>

#### [ Mario Carneiro (Jul 24 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205297):
<div class="codehilite"><pre><span></span>theorem map_X (f : α → β) [is_ring_hom f] (n : σ) : map f (X n : mv_polynomial σ α) = X n :=
(map_monomial _ _ _).trans $ by simp [is_ring_hom.map_one f]
</pre></div>

#### [ Mario Carneiro (Jul 24 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205313):
<p>oh wait that doesn't work</p>
<div class="codehilite"><pre><span></span>theorem map_X (f : α → β) [is_ring_hom f] (n : σ) : map f (X n : mv_polynomial σ α) = X n :=
by simp [X, map_monomial, is_ring_hom.map_one f]
</pre></div>

#### [ Johan Commelin (Jul 24 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205321):
<p>You fixed it and made it shorter! Double win.</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205398):
<p>mul is probably the hard one</p>

#### [ Johan Commelin (Jul 24 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205402):
<p>Last man standing (-;</p>

#### [ Johan Commelin (Jul 24 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205492):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I wouldn't be surprised if you need the <code>section ring_hom_commutes_with_stuff</code></p>

#### [ Johan Commelin (Jul 24 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205497):
<p>See Kenny's post a few lines up.</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205500):
<p>I was planning on using induction</p>

#### [ Johan Commelin (Jul 24 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205508):
<p>Right, that's what we did in that section.</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205509):
<p>no I mean to prove <code>map_mul</code></p>

#### [ Johan Commelin (Jul 24 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205570):
<p>Yes, but that might mean duplicating effort... I don't know.</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205580):
<p>well, commuting with <code>sum</code> still leaves commuting over <code>^</code></p>

#### [ Johan Commelin (Jul 24 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205770):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">ring_hom_powers</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">i</span><span class="o">(</span><span class="n">x</span><span class="err">^</span><span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">i</span> <span class="n">x</span><span class="o">)</span><span class="err">^</span><span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span> <span class="n">ih</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">simp</span> <span class="o">[</span><span class="n">pow_zero</span><span class="o">,</span><span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_one</span> <span class="n">i</span><span class="o">]</span> <span class="o">},</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">pow_succ</span><span class="o">,</span><span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_mul</span> <span class="n">i</span><span class="o">,</span><span class="n">ih</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Jul 24 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205774):
<p>Was already in my file, but didn't copy it into the MWE.</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205840):
<p>I was hoping that <code>map</code> was defined using <code>eval</code>, but unfortunately it's a bit circular</p>

#### [ Johan Commelin (Jul 24 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205866):
<p>How would you define it using <code>eval</code>?</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205923):
<p>I was thinking something along the lines of "evaluate the constants using <code>C o f</code> and the variables using <code>X</code>"</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205943):
<p>but <code>eval</code> doesn't work like that; it maps everything into the coefficient ring rather than some other ring across a ring hom</p>

#### [ Johan Commelin (Jul 24 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205993):
<p>True. So either you need a beefed up <code>eval</code>, or you need <code>map</code>.</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130205995):
<p>exactly</p>

#### [ Johan Commelin (Jul 24 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206015):
<p>Oooh, while you are editing that file. I was also thinking that the <code>instance</code> that <code>eval</code> is a ring hom should get a name. Because <code>C</code> is also a useful ring hom in that context.</p>

#### [ Johan Commelin (Jul 24 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206033):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">C_is_ring_hom</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">mv_polynomial</span> <span class="n">σ</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">map_one</span> <span class="o">:=</span> <span class="n">C_1</span><span class="o">,</span>
  <span class="n">map_add</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">single_add</span><span class="o">,</span>
  <span class="n">map_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="n">C_mul_monomial</span> <span class="o">}</span>
</pre></div>

#### [ Mario Carneiro (Jul 24 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206077):
<p>I saw that</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206082):
<p>I agree that it is useful</p>

#### [ Johan Commelin (Jul 24 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206098):
<p>Yes, I'm currently using <code>map C</code> all over the place.</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206125):
<p>I think I will define beefed up <code>eval</code>, what should it be called?</p>

#### [ Johan Commelin (Jul 24 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206277):
<p>Hmm, I don't know a TLA...</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206281):
<p>oh dear, I need semiring homs</p>

#### [ Johan Commelin (Jul 24 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206285):
<p>You're kidding me (-;</p>

#### [ Johan Commelin (Jul 24 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206294):
<p>You don't <em>need</em> them. You only <em>want</em> them.</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206301):
<p>if I use beefed up eval to define eval, it won't work on semiring like it does now</p>

#### [ Johan Commelin (Jul 24 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206305):
<p>Mathematicians have survived over 3000 years without needing them.</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206308):
<p>I'm sorry, but they really do come up in lean, a lot</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206311):
<p><code>nat</code> is a semiring, <code>ennreal</code> is a semiring. These get lots of use</p>

#### [ Johan Commelin (Jul 24 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206312):
<p>Only trolling (-;. I guess you stumbled on a gap in mathlib?</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206360):
<p>maybe because it was written by a bunch of blithe mathematicians ;)</p>

#### [ Mario Carneiro (Jul 24 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206367):
<p>who think semirings have no value</p>

#### [ Johan Commelin (Jul 24 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206786):
<p>You mean the definition of <code>is_ring_hom</code>? Lol. We really need <span class="user-mention" data-user-id="110087">@Scott Morrison</span> and you guys (Mario + <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> ) to get categories into mathlib. You will be amazed at how many <code>is_X_hom</code> definitions will be added by a bunch of blithe mathematicians (-;</p>

#### [ Mario Carneiro (Jul 24 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206793):
<p>Well, category theory doesn't save you from having to define the homs</p>

#### [ Johan Commelin (Jul 24 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206947):
<p>No, I agree. But all of a sudden we will want to define a bunch of categories. And then we'll define the homs as well (-;</p>

#### [ Johan Commelin (Jul 24 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130206988):
<p>Although maybe we will forget about the category of semirings...</p>

#### [ Johan Commelin (Jul 24 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130207579):
<p>Aaaahrg, now I need to make sure that <code>eval</code> of polynomials is associative...</p>

#### [ Johan Commelin (Jul 24 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130211457):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> How 's it going with <code>eval_on_steroids</code>?</p>

#### [ Kevin Buzzard (Jul 24 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130220081):
<blockquote>
<p><code>nat</code> is a semiring, <code>ennreal</code> is a semiring. These get lots of use</p>
</blockquote>
<p><span class="user-mention" data-user-id="120256">@Ali Sever</span> (the guy formalising Euclid/Tarski geometry in Lean) was saying that he wanted to be able to say "the distance from a to b is q times the distance from c to d" where q&gt;=0 is rational. There is no formal definition of distance, we just have a predicate <code>eqd a b c d</code> interpreted as "dist(a,b)=dist(c,d)", but we defined distance anyway as point x point / equiv reln (formally these are "attainable distances") and they should indeed be a semi-vector space over the semi-ring of non-negative rationals.</p>

#### [ Mario Carneiro (Jul 25 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130259206):
<p>I'm going to have to get back to you on <code>eval_on_steroids</code>, conferences tend to be a time sink so probably not until the weekend</p>

#### [ Johan Commelin (Jul 25 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130259252):
<p>Too bad. Have fun!</p>

#### [ Kevin Buzzard (Jul 25 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130263243):
<p>William Stein reported that he'd met Mario, so Mario at conferences does have advantages :-)</p>

#### [ Johan Commelin (Jul 27 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130403696):
<p>Mario, since you said you would take a stab at these problems, may I suggest you also consider <a href="https://gist.github.com/jcommelin/0e401d47ac3e0b7291c27d3313ea850f" target="_blank" title="https://gist.github.com/jcommelin/0e401d47ac3e0b7291c27d3313ea850f">https://gist.github.com/jcommelin/0e401d47ac3e0b7291c27d3313ea850f</a> while you're going at it...?</p>

#### [ Johan Commelin (Jul 27 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130403711):
<p>Oooh, and <code>s/functorial/map/</code>.</p>

#### [ Johan Commelin (Aug 02 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130766236):
<p>Hi Mario, any news here? Do you have a definition about which I could try to prove some lemmas?</p>

#### [ Mario Carneiro (Aug 05 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130908402):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>  News is here. I didn't prove the assoc lemmas but all the assoc lemmas on <code>eval</code> and <code>map</code> follow from the obvious composition lemma for <code>map2</code></p>

#### [ Mario Carneiro (Aug 06 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/130953117):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> I think the second associativity lemma is false:</p>
<div class="codehilite"><pre><span></span>theorem eval_assoc₂_false
  {α} [comm_semiring α] [decidable_eq α]
  {σ} [decidable_eq σ]
  {τ} [decidable_eq τ]
  (f : σ → mv_polynomial τ α) (g : τ → α)
  (H : ∀ (p : mv_polynomial σ (mv_polynomial τ α)),
    C ((p.eval f).eval g) = p.eval (C ∘ eval g ∘ f))
  (a : τ) : C (g a) = X a :=
by simpa using H (C (X a))
</pre></div>

#### [ Johan Commelin (Aug 07 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023083):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Cool! This is adding a lot of flexibility. Do you think it makes sense to add <code>map2_neg</code> and <code>map2_sub</code>?</p>

#### [ Mario Carneiro (Aug 07 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023091):
<p>Sure. They should be direct applications of the <code>is_ring_hom</code> instance</p>

#### [ Johan Commelin (Aug 07 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023142):
<p>Ok, do you want me to do that? Or have you already done it (-;</p>

#### [ Mario Carneiro (Aug 07 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023151):
<p>I haven't done it, it's up to you</p>

#### [ Johan Commelin (Aug 07 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023155):
<p>Ok, I'll add them.</p>

#### [ Johan Commelin (Aug 07 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023374):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Is <code>rw</code> the "morally" correct way to prove such a thing?</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">map₂_sub</span> <span class="o">:</span> <span class="o">(</span><span class="n">p</span> <span class="bp">-</span> <span class="n">q</span><span class="o">)</span><span class="bp">.</span><span class="n">map₂</span> <span class="n">f</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">p</span><span class="bp">.</span><span class="n">map₂</span> <span class="n">f</span> <span class="n">g</span> <span class="bp">-</span> <span class="n">q</span><span class="bp">.</span><span class="n">map₂</span> <span class="n">f</span> <span class="n">g</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">map_sub</span> <span class="o">(</span><span class="n">map₂</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Aug 07 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023381):
<p>you should be able to just apply the theorem, right? Does <code>is_ring_hom.map_sub _</code> work as a proof?</p>

#### [ Johan Commelin (Aug 07 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023437):
<p>Yes, it does. Thanks! Do you want a 5 line PR?</p>

#### [ Mario Carneiro (Aug 07 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023448):
<p>sure</p>

#### [ Mario Carneiro (Aug 07 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023451):
<p>You should have the same theorems for <code>eval</code> and <code>map</code> too</p>

#### [ Mario Carneiro (Aug 07 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023496):
<p>and <code>C</code></p>

#### [ Johan Commelin (Aug 07 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023578):
<p>Ok, I'll add those too</p>

#### [ Johan Commelin (Aug 07 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023734):
<p><code>map_add</code> and <code>map_mul</code> are simp lemmas</p>

#### [ Johan Commelin (Aug 07 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023735):
<p>But the corresponding lemmas for <code>map2</code> are not.</p>

#### [ Johan Commelin (Aug 07 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023737):
<p>Is there a reason for this?</p>

#### [ Johan Commelin (Aug 07 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023962):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> If you can tell me which ones should be simp lemmas, then I think I'm done.</p>

#### [ Mario Carneiro (Aug 07 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023966):
<p>I think there was, but I don't think it was a good reason. Just make them all simp lemmas</p>

#### [ Mario Carneiro (Aug 07 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023976):
<p><code>eval</code> too</p>

#### [ Johan Commelin (Aug 07 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023985):
<p>And <code>C</code> as well</p>

#### [ Mario Carneiro (Aug 07 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131023991):
<p>There probably isn't any point in having the <code>_sub</code> theorems be simp lemmas, since the LHS is not in simp normal form</p>

#### [ Johan Commelin (Aug 07 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131024076):
<p>Hmm, I don't think I know what that means. Nevertheless, it would be cool if <code>simp</code> would just do all those rewrites for me...</p>

#### [ Johan Commelin (Aug 07 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131024219):
<p>PR'd</p>

#### [ Johan Commelin (Aug 07 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131028888):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Ok, so now there are some merge conflicts... The renaming is straightforward.</p>

#### [ Johan Commelin (Aug 07 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131028928):
<p>Shall I make the <code>add</code> and <code>mul</code> lemmas into simp lemmas?</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131028937):
<p>yeah, same as the last version of your PR</p>

#### [ Johan Commelin (Aug 07 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131028949):
<p>Ok!</p>

#### [ Johan Commelin (Aug 07 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20hom%20induces%20ring%20hom%20between%20mv_polynomials/near/131033604):
<p>Updated the PR</p>


{% endraw %}
