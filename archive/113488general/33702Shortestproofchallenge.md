---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/33702Shortestproofchallenge.html
---

## Stream: [general](index.html)
### Topic: [Shortest proof challenge](33702Shortestproofchallenge.html)

---


{% raw %}
#### [ Chris Hughes (Apr 05 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shortest%20proof%20challenge/near/124686991):
<p><code>example (a b : ℕ) : a ≠ b →  0  &lt; a + b </code></p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shortest%20proof%20challenge/near/124688057):
<p><code>nat.rec (nat.pos_of_ne_zero) (λ n H I, nat.zero_lt_succ _) b</code> (or smaller if I'm allowed to open nat)</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shortest%20proof%20challenge/near/124688064):
<p>These games are slightly artificial because a lot depends on whether the things you want are already in lean.</p>

#### [ Kevin Buzzard (Apr 05 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shortest%20proof%20challenge/near/124688115):
<p><code>nat.rec (nat.pos_of_ne_zero) (λ_ H I, nat.zero_lt_succ _) b</code> cheating a character away</p>

#### [ Chris Hughes (Apr 05 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shortest%20proof%20challenge/near/124689279):
<p>Thanks. I need this one as well </p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span>  <span class="n">nat</span><span class="bp">.</span><span class="n">div_mul_le</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">{</span><span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">hb</span> <span class="o">:</span> <span class="mi">0</span>  <span class="bp">&lt;</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">/</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">a</span>
</pre></div>

#### [ Kevin Buzzard (Apr 05 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shortest%20proof%20challenge/near/124690034):
<p>I think induction on <code>b</code> might fare less well this time.</p>

#### [ Kenny Lau (Apr 06 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shortest%20proof%20challenge/near/124694848):
<blockquote>
<p><code>nat.rec (nat.pos_of_ne_zero) (λ_ H I, nat.zero_lt_succ _) b</code> cheating a character away</p>
</blockquote>
<p>you don't need parentheses to enclose something without space</p>


{% endraw %}
