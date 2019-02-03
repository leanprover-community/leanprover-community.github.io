---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/52882Proofdependingonnmod2.html
---

## Stream: [maths](index.html)
### Topic: [Proof depending on n mod 2](52882Proofdependingonnmod2.html)

---


{% raw %}
#### [ Johan Commelin (Jul 16 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129743513):
<p>I need to prove a fact about <code>(-a)^n</code>, with <code>n : nat</code>. I would like to split into two cases, depending on whether <code>n</code> is odd or even. What is the best way to do this in mathlib?</p>

#### [ Kenny Lau (Jul 16 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744299):
<p>what is it that you want to prove?</p>

#### [ Kenny Lau (Jul 16 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744303):
<p>you might be able to rewrite <code>n</code> into <code>(n/2)*2 + (n%2)</code> if you use the division algorithm</p>

#### [ Chris Hughes (Jul 16 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744396):
<p><code>nat.mod_two_eq_zero_or_one</code> I believe</p>

#### [ Kenny Lau (Jul 16 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744408):
<p>my point is, sometimes you don't need to split into two cases</p>

#### [ Johan Commelin (Jul 16 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744766):
<p>Ok, I'll try that.</p>

#### [ Johan Commelin (Jul 16 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744770):
<p>So, here is another substep that I currently have:</p>
<div class="codehilite"><pre><span></span><span class="n">rw</span> <span class="k">show</span> <span class="n">v</span> <span class="bp">*</span> <span class="o">(</span><span class="bp">-</span><span class="n">a</span><span class="o">)</span><span class="err">^</span><span class="n">n</span> <span class="bp">=</span> <span class="o">((</span><span class="bp">-</span><span class="mi">1</span><span class="o">)</span><span class="err">^</span><span class="n">n</span> <span class="bp">*</span> <span class="n">v</span><span class="o">)</span> <span class="bp">*</span> <span class="n">a</span><span class="err">^</span><span class="n">n</span><span class="o">,</span>
    <span class="k">begin</span>
      <span class="n">rw</span> <span class="o">[</span><span class="n">neg_eq_neg_one_mul</span><span class="o">,</span> <span class="n">mul_pow</span><span class="o">],</span> <span class="n">ring</span><span class="o">,</span>
    <span class="kn">end</span><span class="o">,</span>
</pre></div>

#### [ Kenny Lau (Jul 16 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744815):
<p>could you include the types of <code>v</code> and <code>a</code>?</p>

#### [ Johan Commelin (Jul 16 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744818):
<p>Should <code>ring</code> be able to do those rewrites itself? I think it would make sense to me to teach <code>ring</code> about negatives...</p>

#### [ Johan Commelin (Jul 16 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744829):
<p><code>v</code> and <code>a</code> live in some comm ring.</p>

#### [ Kenny Lau (Jul 16 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744918):
<p>it isn't about negatives</p>

#### [ Kenny Lau (Jul 16 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744920):
<p>it's about powers</p>

#### [ Kenny Lau (Jul 16 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744924):
<p><code>ring</code> can't prove this:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">x</span><span class="err">^</span><span class="n">n</span> <span class="bp">*</span> <span class="n">y</span><span class="err">^</span><span class="n">n</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span><span class="err">^</span><span class="n">n</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">ring</span>
</pre></div>

#### [ Johan Commelin (Jul 16 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129745010):
<p>Should ring be able to prove it, by <code>rw mul_pow</code> whenever possible?</p>

#### [ Kenny Lau (Jul 16 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129745014):
<p>I don't know what <code>ring</code> knows</p>

#### [ Johan Commelin (Jul 16 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129745076):
<p>My "Should" was a <em>moral</em> should. As in, does it make sense to give <code>ring</code> these extra powers?</p>

#### [ Mario Carneiro (Jul 16 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129745230):
<p>No. It is not a rewrite system, it is a decision procedure for polynomial equalities. <code>x^n</code> is not a polynomial (of two variables <code>x</code>, <code>n</code>)</p>

#### [ Kenny Lau (Jul 16 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129745235):
<p>fair enough</p>

#### [ Johan Commelin (Jul 16 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129745425):
<p>Mario, so would it make sense to rename <code>ring</code> into <code>semiring</code>, and have a <code>ring</code> tactic that is <code>semiring</code> + some other superpowers?</p>

#### [ Mario Carneiro (Jul 16 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129745483):
<p><code>ring</code> deals with commutative rings and commutative semirings</p>

#### [ Mario Carneiro (Jul 16 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129745495):
<p>Negatives are supported</p>

#### [ Johan Commelin (Jul 16 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129746954):
<p>Ok, so what is the fastest way to prove <code>H : ∀ {n : ℕ}, ((-1 : R)^n = 1) ∨ ((-1 : R)^n = -1)</code>, where <code>R</code> is a <code>comm_ring</code>.</p>

#### [ Mario Carneiro (Jul 16 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747046):
<p>that could probably go in <code>group_power.lean</code></p>

#### [ Patrick Massot (Jul 16 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747062):
<p>That's the fastest way: have Mario write it in mathlib</p>

#### [ Mario Carneiro (Jul 16 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747072):
<p>but you can prove it either by induction or by quotient remainder theorem like kenny suggested</p>

#### [ Johan Commelin (Jul 16 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747095):
<p>I'm halfway a proof by induction, but everytime I need a stupid little fact from mathlib it costs me 15 minutes to find it...</p>

#### [ Kenny Lau (Jul 16 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747269):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="kn">universe</span> <span class="n">u</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">((</span><span class="bp">-</span><span class="mi">1</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span><span class="err">^</span><span class="n">n</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">∨</span> <span class="o">((</span><span class="bp">-</span><span class="mi">1</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span><span class="err">^</span><span class="n">n</span> <span class="bp">=</span> <span class="bp">-</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span> <span class="n">ih</span><span class="o">,</span> <span class="o">{</span><span class="n">simp</span><span class="o">},</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">pow_succ</span><span class="o">,</span> <span class="n">neg_one_mul</span><span class="o">,</span> <span class="n">neg_inj&#39;</span><span class="o">,</span> <span class="n">neg_eq_iff_neg_eq</span><span class="o">,</span> <span class="n">eq_comm</span><span class="o">,</span> <span class="n">or_comm</span><span class="o">],</span>
  <span class="n">assumption</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Jul 16 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747273):
<p>that's 7 minutes :P</p>

#### [ Kenny Lau (Jul 16 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747459):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="kn">universe</span> <span class="n">u</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">((</span><span class="bp">-</span><span class="mi">1</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span><span class="err">^</span><span class="n">n</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">∨</span> <span class="o">((</span><span class="bp">-</span><span class="mi">1</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span><span class="err">^</span><span class="n">n</span> <span class="bp">=</span> <span class="bp">-</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span> <span class="n">ih</span><span class="o">,</span> <span class="o">{</span><span class="n">simp</span><span class="o">},</span>
  <span class="n">cases</span> <span class="n">ih</span> <span class="k">with</span> <span class="n">ih</span> <span class="n">ih</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">right</span><span class="o">,</span> <span class="n">simp</span> <span class="o">[</span><span class="n">pow_succ</span><span class="o">,</span> <span class="n">ih</span><span class="o">]</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">left</span><span class="o">,</span> <span class="n">simp</span> <span class="o">[</span><span class="n">pow_succ</span><span class="o">,</span> <span class="n">ih</span><span class="o">]</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Jul 16 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747482):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="kn">universe</span> <span class="n">u</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">((</span><span class="bp">-</span><span class="mi">1</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span><span class="err">^</span><span class="n">n</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">∨</span> <span class="o">((</span><span class="bp">-</span><span class="mi">1</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span><span class="err">^</span><span class="n">n</span> <span class="bp">=</span> <span class="bp">-</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span> <span class="n">ih</span><span class="o">,</span> <span class="o">{</span><span class="n">simp</span><span class="o">},</span>
  <span class="n">cases</span> <span class="n">ih</span> <span class="k">with</span> <span class="n">ih</span> <span class="n">ih</span><span class="bp">;</span> <span class="o">[</span><span class="n">right</span><span class="o">,</span> <span class="n">left</span><span class="o">]</span><span class="bp">;</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">pow_succ</span><span class="o">,</span> <span class="n">ih</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Jul 16 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747491):
<p>You win (-;</p>

#### [ Mario Carneiro (Jul 16 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747550):
<p>Now you are just showing off :P</p>

#### [ Mario Carneiro (Jul 16 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747557):
<p>What's it look like using the equation compiler for the induction?</p>

#### [ Kenny Lau (Jul 16 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747574):
<p>not much difference, I think</p>

#### [ Mario Carneiro (Jul 16 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747711):
<p>I think it's a bit neater</p>
<div class="codehilite"><pre><span></span>theorem neg_one_pow_eq_or {R} [comm_ring R] : ∀ n : ℕ, ((-1 : R)^n = 1) ∨ ((-1 : R)^n = -1)
| 0     := by simp
| (n+1) := by cases neg_one_pow_eq_or n; simp [pow_succ, h]
</pre></div>


<p>also <code>left</code> and <code>right</code> are unnecessary</p>

#### [ Kenny Lau (Jul 16 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747723):
<p>I see</p>

#### [ Kenny Lau (Jul 16 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747746):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="kn">universe</span> <span class="n">u</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">((</span><span class="bp">-</span><span class="mi">1</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span><span class="err">^</span><span class="n">n</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">∨</span> <span class="o">((</span><span class="bp">-</span><span class="mi">1</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span><span class="err">^</span><span class="n">n</span> <span class="bp">=</span> <span class="bp">-</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mod_two_eq_zero_or_one</span> <span class="n">n</span><span class="bp">;</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mod_add_div</span> <span class="n">n</span> <span class="mi">2</span><span class="o">,</span> <span class="n">pow_add</span><span class="o">,</span> <span class="n">pow_mul</span><span class="o">,</span> <span class="n">h</span><span class="o">]</span><span class="bp">;</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">pow_two</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>


{% endraw %}
