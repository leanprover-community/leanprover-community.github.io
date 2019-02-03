---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89367naturalsinreals.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [naturals_in_reals](https://leanprover-community.github.io/archive/113488general/89367naturalsinreals.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Guillermo Barajas Ayuso (Sep 11 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133730371):
<p>Hi guys, how would you express the natural numbers as a subtype of the reals?</p>

#### [ Kevin Buzzard (Sep 11 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133731041):
<p>I guess you could just do</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">def</span> <span class="n">N</span> <span class="o">:=</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">//</span> <span class="bp">∃</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">n</span><span class="o">}</span>
</pre></div>


<p>but then the term of type <code>equiv N nat</code> would be noncomputable. Is there a computable way?</p>

#### [ Kenny Lau (Sep 11 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133731224):
<p>it's computable</p>

#### [ Kenny Lau (Sep 11 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133731235):
<p>(but Lean doesn't know it yet)</p>

#### [ Chris Hughes (Sep 11 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133734407):
<p>How do you do that computably?</p>

#### [ Mario Carneiro (Sep 11 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133752152):
<p>It's not computable. It would be if cauchy sequences defining real numbers had a modulus of convergence</p>

#### [ Mario Carneiro (Sep 11 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133752221):
<p>this is why I've taken to calling our definition of the reals "computable but not really"</p>

#### [ Mario Carneiro (Sep 11 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133752463):
<p>Suppose you have a real number that is known to equal some natural number, and you want to guess which. The convergence criterion says that at some point all the rational numbers will be closer to one natural than any other, and then you can round to get the number, but you don't know when that point is. A more constructive approach would be a sequence of rationals that converges at a specific rate (usually exponential), so you can ask "give me an n-digit approximation of this number", or at least a sequence of rationals together with a function that tells you how long the sequence takes to reach a certain level of approximation</p>

#### [ Kenny Lau (Sep 11 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133752494):
<p>fair enough. I thought wrongly.</p>

#### [ Johan Commelin (Sep 11 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133752892):
<p>Is our definition of <code>rat</code> "computable but not rationally"?</p>

#### [ Mario Carneiro (Sep 11 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133753216):
<p>To answer the original question, the standard way to talk about natural numbers inside the reals is to use the coercion. If you want to talk about the whole set of reals-that-are-natural, you can use <code>set.range (coe : ℕ → ℝ)</code> which is basically the same as Kevin's suggestion.</p>

#### [ Guillermo Barajas Ayuso (Sep 12 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133797345):
<p>I see, thaks a lot! Also how would you prove the following?</p>
<div class="codehilite"><pre><span></span>example (h : n &lt; m) : (n : ℝ) &lt; (m : ℝ) := sorry
</pre></div>

#### [ Guillermo Barajas Ayuso (Sep 12 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133797368):
<p>Sorry I forgot to define n and m</p>
<div class="codehilite"><pre><span></span>example {n m : ℕ} (h : n &lt; m) : (n : ℝ) &lt; (m : ℝ) := sorry
</pre></div>

#### [ Kenny Lau (Sep 12 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133797477):
<p>nat.cast_lt or something</p>

#### [ Kenny Lau (Sep 12 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133797482):
<p>(alternatively, induct on <code>h</code>)</p>

#### [ Guillermo Barajas Ayuso (Sep 12 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133797598):
<p>Ok, thanks!</p>


{% endraw %}
