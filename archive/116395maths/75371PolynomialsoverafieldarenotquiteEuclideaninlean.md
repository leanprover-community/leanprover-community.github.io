---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/75371PolynomialsoverafieldarenotquiteEuclideaninlean.html
---

## Stream: [maths](index.html)
### Topic: [Polynomials over a field are not quite Euclidean in lean](75371PolynomialsoverafieldarenotquiteEuclideaninlean.html)

---


{% raw %}
#### [ Chris Hughes (May 28 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127196752):
<p>I've been trying to prove polynomials over a field are a Euclidean domain. The only trouble is, they do not meet the axioms if I use degree as valuation since for two constant polynomials, degree (a % b) =  degree b. Does anyone have experience doing this in any other theorem prover and can recommend a sensible solution. The most obvious is to define<code>new_degree 0 = 0</code>, and <code>new_degree p = degree p + 1</code> for <code>p ≠ 0</code>. Is this the best option?</p>

#### [ Johannes Hölzl (May 28 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127196999):
<p>In Isabelle the size is not degree <code>d</code> itself but <code>2^d</code>, and 0 for the 0 polynomial. See <a href="http://isabelle.in.tum.de/dist/library/HOL/HOL-Computational_Algebra/Polynomial_Factorial.html" target="_blank" title="http://isabelle.in.tum.de/dist/library/HOL/HOL-Computational_Algebra/Polynomial_Factorial.html">http://isabelle.in.tum.de/dist/library/HOL/HOL-Computational_Algebra/Polynomial_Factorial.html</a> :</p>
<div class="codehilite"><pre><span></span><span class="k">definition</span> <span class="n">euclidean_size_field_poly</span> <span class="o">::</span> <span class="s">&quot;&#39;a :: field poly ⇒ nat&quot;</span> <span class="kp">where</span>
  <span class="s">&quot;euclidean_size_field_poly p = (if p = 0 then 0 else 2 ^ degree p)&quot;</span>
</pre></div>

#### [ Chris Hughes (May 28 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197047):
<p>Why <code>2^d</code>?</p>

#### [ Johan Commelin (May 28 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197113):
<p>I actually think that <code>valuation_remainder_lt</code> is not what mathematicians want</p>

#### [ Johan Commelin (May 28 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197124):
<p>It is a lot stronger than the usual condition</p>

#### [ Johan Commelin (May 28 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197126):
<p>They swapped two quantifiers, so to speak</p>

#### [ Mario Carneiro (May 28 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197131):
<p>what do you mean?</p>

#### [ Johan Commelin (May 28 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197179):
<p>Quote from wiki: (EF1) If a and b are in R and b is nonzero, then there are q and r in R such that a = bq + r and either r = 0 or f(r) &lt; f(b).</p>

#### [ Johannes Hölzl (May 28 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197180):
<blockquote>
<p>Why <code>2^d</code>?</p>
</blockquote>
<p>I guess you get the nice rule: <code>E(p * q) = E(p) * E (q)</code></p>

#### [ Mario Carneiro (May 28 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197186):
<p>oh, you need <code>a % b != 0</code> also as a precondition</p>

#### [ Johan Commelin (May 28 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197187):
<p>So it is about the existence of q and r, but this somehow requires it for all q and r</p>

#### [ Johannes Hölzl (May 28 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197188):
<p>(where <code>E  =  euclidean_size_field_poly</code>)</p>

#### [ Johan Commelin (May 28 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197191):
<p>Mario, I think that would also fix it, yes.</p>

#### [ Mario Carneiro (May 28 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197194):
<p>that's basically what wiki is saying, or you can have a disjunction at the end</p>

#### [ Johan Commelin (May 28 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197246):
<p>After all, the valuation of 0 is <code>37</code> according to <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Mario Carneiro (May 28 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197254):
<p>hey, with the new <code>with_zero</code> class you can now just say that <code>valuation</code> takes values in <code>with_zero nat</code></p>

#### [ Johan Commelin (May 28 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197272):
<p>Nooo! <code>with_zero nat</code> looks horrible... can we please have <code>with_bot</code> or something</p>

#### [ Mario Carneiro (May 28 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197317):
<p>it's the absorbing element of multiplication...</p>

#### [ Mario Carneiro (May 28 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197318):
<p>there is also with_bot, which has no algebraic interpretation</p>

#### [ Mario Carneiro (May 28 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197334):
<p>actually <code>valuation</code> looks like it doesn't need any algebraic interpretation, so I guess <code>with_bot</code> is fine</p>

#### [ Chris Hughes (May 28 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127197383):
<p>It could just be generalised to take any well founded relation, instead of a valuation</p>

#### [ Chris Hughes (May 28 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127215412):
<blockquote>
<p>hey, with the new <code>with_zero</code> class you can now just say that <code>valuation</code> takes values in <code>with_zero nat</code></p>
</blockquote>
<p>Where is this class defined? I definitely prefer the idea of option nat over 2^degree.</p>

#### [ Mario Carneiro (May 28 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Polynomials%20over%20a%20field%20are%20not%20quite%20Euclidean%20in%20lean/near/127218435):
<p><code>with_bot</code> is in <code>lattice.bounded_lattice</code>, <code>with_zero</code> is in <code>algebra.group</code>. Basically it should already be available if you have the basic mathlib lemmas</p>


{% endraw %}
