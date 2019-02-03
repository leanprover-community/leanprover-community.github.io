---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/70527prime617challenge.html
---

## Stream: [maths](index.html)
### Topic: [prime 617 challenge](70527prime617challenge.html)

---


{% raw %}
#### [ Kevin Buzzard (Jul 26 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130359176):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">prime</span>

<span class="kn">open</span> <span class="n">nat</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">prime</span> <span class="mi">617</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>I tried <code>dec_trivial</code> with <code>local attribute [instance] decidable_prime_1</code> but it times out on my machine. There is a lemma that says p is prime iff no factors &lt;= sqrt(p) -- can one somehow persuade Lean to use this?</p>

#### [ Kevin Buzzard (Jul 26 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130359652):
<p>The reason this is even a thing is that a question on the number theory example sheet that students are working on asks them to use quadratic reciprocity to evaluate whether something is a square mod 617. They managed to solve the question assuming quadratic reciprocity and that 617 was prime :-) The smaller numbers we can handle</p>

#### [ Rob Lewis (Jul 26 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130360645):
<p>It looks like <code>decidable_prime</code> already does this: <a href="https://github.com/leanprover/mathlib/blob/master/data/nat/prime.lean#L90" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/nat/prime.lean#L90">https://github.com/leanprover/mathlib/blob/master/data/nat/prime.lean#L90</a></p>

#### [ Rob Lewis (Jul 26 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130360660):
<p>Why are you trying to use <code>decidable_prime_1</code>?</p>

#### [ Rob Lewis (Jul 26 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130360768):
<p><code>#eval if nat.prime 617 then tt else ff</code> is  instant without adding the local instance.</p>

#### [ Mario Carneiro (Jul 26 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130361003):
<p>You can also use <code>#eval to_bool (nat.prime 617)</code> for the same purpose</p>

#### [ Kevin Buzzard (Jul 26 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130361928):
<p>I want a proof!</p>

#### [ Kevin Buzzard (Jul 26 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130361929):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">prime</span>

<span class="kn">open</span> <span class="n">nat</span>

<span class="kn">theorem</span> <span class="n">sqrt617</span> <span class="o">:</span> <span class="n">sqrt</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">24</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">symmetry</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">eq_sqrt</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">dec_trivial</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">prime617iff</span> <span class="o">:</span> <span class="n">prime</span> <span class="mi">617</span> <span class="bp">↔</span> <span class="bp">∀</span> <span class="n">m</span><span class="o">,</span> <span class="mi">2</span> <span class="bp">≤</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">m</span> <span class="bp">≤</span> <span class="mi">24</span> <span class="bp">→</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">m</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="n">prime_def_le_sqrt</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">sqrt617</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">and_iff_right</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">dec_trivial</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">prime617</span> <span class="o">:</span> <span class="n">prime</span> <span class="mi">617</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="n">prime617iff</span><span class="o">,</span>
  <span class="k">show</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="mi">2</span> <span class="bp">≤</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">m</span> <span class="bp">≤</span> <span class="mi">24</span> <span class="bp">→</span> <span class="bp">¬</span><span class="n">m</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">dec_trivial</span> <span class="c1">-- times out :-(</span>
<span class="kn">end</span>
</pre></div>


<p>Is it possible to work out how close I got?</p>

#### [ Kevin Buzzard (Jul 26 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130362377):
<p>Hmm, I think I only make it up to 6 :-/</p>

#### [ Kevin Buzzard (Jul 26 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130362737):
<p>Ok I have a strat. I can prove 617 = 154 * 4 + 1 using norm_num and then use some lemmas about division to reduce non-divisibility of 617 by 4 to non-divisibility of 1 by 4, which I can prove with <code>dec_trivial</code>. I then repeat up to 24. I write a python script which generates the code I want.</p>

#### [ Kevin Buzzard (Jul 26 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130363560):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span>
<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">prime</span>

<span class="kn">open</span> <span class="n">nat</span>

<span class="kn">theorem</span> <span class="n">sqrt617</span> <span class="o">:</span> <span class="n">sqrt</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">24</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">symmetry</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">eq_sqrt</span><span class="o">,</span>
  <span class="n">norm_num</span><span class="o">,</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">prime617iff</span> <span class="o">:</span> <span class="n">prime</span> <span class="mi">617</span> <span class="bp">↔</span> <span class="bp">∀</span> <span class="n">m</span><span class="o">,</span> <span class="mi">2</span> <span class="bp">≤</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">m</span> <span class="bp">≤</span> <span class="mi">24</span> <span class="bp">→</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">m</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="n">prime_def_le_sqrt</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">sqrt617</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">and_iff_right</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">dec_trivial</span>
<span class="kn">end</span>


<span class="kn">theorem</span> <span class="n">prime617</span> <span class="o">:</span> <span class="n">prime</span> <span class="mi">617</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="n">prime617iff</span><span class="o">,</span>
  <span class="k">show</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="mi">2</span> <span class="bp">≤</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">m</span> <span class="bp">≤</span> <span class="mi">24</span> <span class="bp">→</span> <span class="bp">¬</span><span class="n">m</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">m</span> <span class="n">hm1</span> <span class="n">hm2</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">m</span><span class="o">,</span><span class="n">cases</span> <span class="n">hm1</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">m</span><span class="o">,</span><span class="n">cases</span> <span class="n">hm1</span><span class="o">,</span><span class="n">cases</span> <span class="n">hm1_a</span><span class="o">,</span> <span class="c1">-- m = 1</span>
  <span class="n">cases</span> <span class="n">m</span><span class="o">,</span><span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">2</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">308</span> <span class="bp">*</span> <span class="mi">2</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">m</span><span class="o">,</span><span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">3</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">+</span> <span class="mi">205</span> <span class="bp">*</span> <span class="mi">3</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">4</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">154</span> <span class="bp">*</span> <span class="mi">4</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">5</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">+</span> <span class="mi">123</span> <span class="bp">*</span> <span class="mi">5</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">6</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">5</span> <span class="bp">+</span> <span class="mi">102</span> <span class="bp">*</span> <span class="mi">6</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">7</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">88</span> <span class="bp">*</span> <span class="mi">7</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">8</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">77</span> <span class="bp">*</span> <span class="mi">8</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">9</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">5</span> <span class="bp">+</span> <span class="mi">68</span> <span class="bp">*</span> <span class="mi">9</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">10</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">7</span> <span class="bp">+</span> <span class="mi">61</span> <span class="bp">*</span> <span class="mi">10</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">11</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">56</span> <span class="bp">*</span> <span class="mi">11</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">12</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">5</span> <span class="bp">+</span> <span class="mi">51</span> <span class="bp">*</span> <span class="mi">12</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">13</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">6</span> <span class="bp">+</span> <span class="mi">47</span> <span class="bp">*</span> <span class="mi">13</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">14</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">44</span> <span class="bp">*</span> <span class="mi">14</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">15</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">+</span> <span class="mi">41</span> <span class="bp">*</span> <span class="mi">15</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">16</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">9</span> <span class="bp">+</span> <span class="mi">38</span> <span class="bp">*</span> <span class="mi">16</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">17</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">5</span> <span class="bp">+</span> <span class="mi">36</span> <span class="bp">*</span> <span class="mi">17</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">18</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">5</span> <span class="bp">+</span> <span class="mi">34</span> <span class="bp">*</span> <span class="mi">18</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">19</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">9</span> <span class="bp">+</span> <span class="mi">32</span> <span class="bp">*</span> <span class="mi">19</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">20</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">17</span> <span class="bp">+</span> <span class="mi">30</span> <span class="bp">*</span> <span class="mi">20</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">21</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">8</span> <span class="bp">+</span> <span class="mi">29</span> <span class="bp">*</span> <span class="mi">21</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">22</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">28</span> <span class="bp">*</span> <span class="mi">22</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">23</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">19</span> <span class="bp">+</span> <span class="mi">26</span> <span class="bp">*</span> <span class="mi">23</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">m</span><span class="o">,</span> <span class="k">show</span> <span class="bp">¬</span> <span class="o">(</span><span class="mi">24</span> <span class="err">∣</span> <span class="mi">617</span><span class="o">),</span> <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">617</span> <span class="bp">=</span> <span class="mi">17</span> <span class="bp">+</span> <span class="mi">25</span> <span class="bp">*</span> <span class="mi">24</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span><span class="n">rw</span> <span class="n">h</span><span class="o">,</span><span class="n">intro</span> <span class="n">h2</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">mod_eq_zero_of_dvd</span> <span class="n">h2</span><span class="o">,</span><span class="n">rw</span> <span class="n">add_mul_mod_self_right</span> <span class="n">at</span> <span class="n">h3</span><span class="o">,</span><span class="n">cases</span> <span class="n">h3</span><span class="o">,</span>
<span class="n">revert</span> <span class="n">hm2</span><span class="o">,</span><span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jul 26 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130363563):
<p>There's a proper proof.</p>

#### [ Mario Carneiro (Jul 26 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130363582):
<p>I'm on it...</p>

#### [ Kevin Buzzard (Jul 26 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130363741):
<p>/me thinks that <code>#eval</code> should be renamed <code>#evil</code></p>

#### [ Rob Lewis (Jul 26 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130364211):
<p>Ah, sorry, I shouldn't try to read this while listening to talks.</p>

#### [ Rob Lewis (Jul 26 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130364221):
<p>I end up missing obvious things in both places!</p>

#### [ Mario Carneiro (Jul 28 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130449391):
<p>Challenge accepted</p>
<div class="codehilite"><pre><span></span>example : nat.prime 617 := by norm_num
</pre></div>

#### [ Kenny Lau (Jul 28 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130451800):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">prime</span>

<span class="kn">theorem</span> <span class="n">prime_617</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">prime</span> <span class="mi">617</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">norm_num failed to simplify</span>
<span class="cm">state:</span>
<span class="cm">⊢ nat.prime 617</span>
<span class="cm">-/</span>
</pre></div>

#### [ Johan Commelin (Jul 28 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130453651):
<p>A wonderful example of the theorem that examples aren't theorems.</p>

#### [ Kevin Buzzard (Jul 28 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130455413):
<p>Maybe you should have tried 57</p>

#### [ Kevin Buzzard (Jul 28 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130455453):
<p>Looks like I need to update my blog post :-)</p>

#### [ Kevin Buzzard (Jul 28 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130455877):
<blockquote>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">prime</span>

<span class="kn">theorem</span> <span class="n">prime_617</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">prime</span> <span class="mi">617</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">norm_num failed to simplify</span>
<span class="cm">state:</span>
<span class="cm">⊢ nat.prime 617</span>
<span class="cm">-/</span>
</pre></div>


</blockquote>
<p>Kenny it works for me. Did you update your mathlib? This is code that Mario just wrote.</p>

#### [ Kevin Buzzard (Jul 28 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130455927):
<p>And thanks Mario! I think my students were going to have some trouble with the example sheet questions if they couldn't get as far as 617.</p>


{% endraw %}
