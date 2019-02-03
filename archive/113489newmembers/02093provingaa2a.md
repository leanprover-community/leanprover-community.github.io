---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/02093provingaa2a.html
---

## Stream: [new members](index.html)
### Topic: [proving a + a = 2* a](02093provingaa2a.html)

---


{% raw %}
#### [ Atze van der Ploeg (Jan 11 2019 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154909221):
<p>I'm trying to prove the shocking lemma ∀ n : ℕ, n + n = 2*n , how do i tell lean to unfold the definition of *?</p>

#### [ Kenny Lau (Jan 11 2019 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154909512):
<p>you don't; you just tell Lean what you want it to unfold to</p>

#### [ Chris Hughes (Jan 11 2019 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154909517):
<p>There's a lemma <code>nat.mul_succ</code></p>

#### [ Rob Lewis (Jan 11 2019 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154909526):
<p>You can use <code>simp only [(*)]</code>. This will unfold the notation, then you'll have to deal with the definition <code>nat.mul</code>.</p>

#### [ Chris Hughes (Jan 11 2019 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154909570):
<p>Sorry, <code>nat.succ_mul</code></p>

#### [ Rob Lewis (Jan 11 2019 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154909583):
<p>You can unfold that with the same method, or <code>unfold nat.mul</code>, but since it's defined by recursion on <code>n</code>, you'll have to use induction first.</p>

#### [ Chris Hughes (Jan 11 2019 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154909621):
<p>You can't actually unfold multiplication in this scenario, since it's defined by recursion on the second argument.</p>

#### [ Kenny Lau (Jan 11 2019 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154909625):
<p>well I imagined he would do induction on <code>n</code></p>

#### [ Atze van der Ploeg (Jan 11 2019 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154912689):
<p>Thanks, nat.succ_mul works fine, or using mul_comm but this requires me to know that nat.mul is defined by recursively on the second argument.</p>

#### [ Kevin Buzzard (Jan 11 2019 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154913474):
<p>You can just use the 'ring' tactic if you don't care about what the low level proof looks like</p>

#### [ Mark Dickinson (Jan 11 2019 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154936758):
<p>There's also <code>two_mul</code> in the standard library:</p>
<div class="codehilite"><pre><span></span><span class="n">two_mul</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">n</span>
</pre></div>


{% endraw %}
