---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/90259mathlibintegerdocsgcdexample.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [mathlib integer docs gcd example](https://leanprover-community.github.io/archive/113489newmembers/90259mathlibintegerdocsgcdexample.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Bryan Gin-ge Chen (Aug 09 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20integer%20docs%20gcd%20example/near/131176076):
<p>The final <code>example</code> in <a href="https://github.com/leanprover/mathlib/blob/master/docs/theories/integers.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/theories/integers.md">this file from the mathlib docs</a> (I guess it originally comes from <a href="https://xenaproject.wordpress.com/maths-in-lean-integers/" target="_blank" title="https://xenaproject.wordpress.com/maths-in-lean-integers/">this page on the xena blog</a>) doesn't seem to typecheck for me:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">gcd</span>
<span class="kn">open</span> <span class="n">nat</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">int</span><span class="bp">.</span><span class="n">gcd</span> <span class="n">m</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">*</span> <span class="o">(</span><span class="n">gcd_a</span> <span class="n">m</span> <span class="n">n</span><span class="o">)</span> <span class="bp">+</span> <span class="n">n</span> <span class="bp">*</span> <span class="o">(</span><span class="n">gcd_b</span> <span class="n">m</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">gcd_eq_gcd_ab</span>
</pre></div>


<p>I get this:</p>
<div class="codehilite"><pre><span></span><span class="n">type</span> <span class="n">mismatch</span> <span class="n">at</span> <span class="n">application</span>
  <span class="n">m</span> <span class="bp">*</span> <span class="n">gcd_a</span> <span class="n">m</span> <span class="n">n</span>
<span class="n">term</span>
  <span class="n">gcd_a</span> <span class="n">m</span> <span class="n">n</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="bp">ℤ</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="bp">ℕ</span>
</pre></div>


<p>and something similar for the other summand.</p>

#### [ Mario Carneiro (Aug 09 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20integer%20docs%20gcd%20example/near/131177735):
<p>that should be</p>
<div class="codehilite"><pre><span></span>example (m n : ℕ) : (nat.gcd m n : ℤ) = m * (gcd_a m n) + n * (gcd_b m n) := gcd_eq_gcd_ab m n
</pre></div>

#### [ Kevin Buzzard (Aug 09 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20integer%20docs%20gcd%20example/near/131177872):
<p>[what Mario said]</p>

#### [ Bryan Gin-ge Chen (Aug 09 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20integer%20docs%20gcd%20example/near/131178041):
<p>Thanks! I was having trouble figuring out the fix by myself...</p>

#### [ Patrick Massot (Aug 09 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20integer%20docs%20gcd%20example/near/131181859):
<p><a href="https://github.com/leanprover/mathlib/pull/244" target="_blank" title="https://github.com/leanprover/mathlib/pull/244">https://github.com/leanprover/mathlib/pull/244</a></p>

#### [ Patrick Massot (Aug 09 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20integer%20docs%20gcd%20example/near/131181958):
<p>It would be really nice to find a workflow making sure examples in the docs are correct. The manual way would be to copy them to a <code>tests/docs/</code> directory, and hope things will stay synced.</p>

#### [ Patrick Massot (Aug 09 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mathlib%20integer%20docs%20gcd%20example/near/131182072):
<p>Thanks Mario! I wonder if this is my new merge time record. I already hit some similar score a long time ago.</p>


{% endraw %}
