---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72616Aboutmonotonicity.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [About monotonicity](https://leanprover-community.github.io/archive/113488general/72616Aboutmonotonicity.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Simon Hudon (Mar 16 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123813072):
<p>I'm currently working on monotonicity related simplification. In some places I consider associativity and commutativity with regards to monotonicity but let's leave that aside for now.</p>
<p>A general monotonicity law for addition looks like:</p>
<div class="codehilite"><pre><span></span>@[monotonic]
lemma add_mono {x₀ y₀ x₁ y₁ : α} [ordered_semiring α]
  (h : x₀ ≤ y₀)
  (h&#39; : x₁ ≤ y₁)
: x₀ + x₁ ≤ y₀ + y₁ := ...
</pre></div>


<p>Very straightforward, no side conditions. When I turn to multiplication, the lemmas multiply (fun definitely intended). I get one position monotonicity:</p>
<div class="codehilite"><pre><span></span>@[monotonic]
lemma mul_mono_nonneg_left {x y z : α} [ordered_semiring α]
  (h&#39; : 0 ≤ z)
  (h : x ≤ y)
: x * z ≤ y * z := ...

@[monotonic]
lemma mul_mono_nonneg_right {x y z : α} [ordered_semiring α]
  (h&#39; : 0 ≤ z)
  (h : x ≤ y)
: z * x ≤ z * y := ...
</pre></div>


<p>In total, 4 of them. The other 2 are left as an exercise <span class="emoji emoji-1f609" title="wink">:wink:</span>. When considering two position-monotonicity for multiplication, their number blows up: </p>
<div class="codehilite"><pre><span></span>@[monotonic]
lemma mul_mono_nonpos_nonpos_left {x₀ y₀ x₁ y₁ : α} [linear_ordered_ring α]
  [decidable_rel ((≤) : α → α → Prop)]
  (h : 0 ≥ x₀)
  (h : 0 ≥ y₁)
  (h₀ : y₀ ≤ x₀)
  (h₁ : y₁ ≤ x₁)
: x₀ * x₁ ≤ y₀ * y₁ := ...

@[monotonic]
lemma mul_mono_nonpos_nonpos_right {x₀ y₀ x₁ y₁ : α} [linear_ordered_ring α]
  [decidable_rel ((≤) : α → α → Prop)]
  (h : 0 ≥ y₀)
  (h : 0 ≥ x₁)
  (h₀ : y₀ ≤ x₀)
  (h₁ : y₁ ≤ x₁)
: x₀ * x₁ ≤ y₀ * y₁ := ...
</pre></div>


<p>The difference is in the side condition. They could be unified and make <code>(h : 0 ≥ x₀) (h : 0 ≥ x₁)</code> but that is stronger than required. I have additionally six more combinations of <code>nonpos</code> / <code>nonneg</code>. The goal of <code>mono</code> is that you don't have to remember those lemmas, it just applies the right one for you. With the explosion of possible side condition, the error messages might get long if they can't be discharged automatically (because <code>mono</code> will look in your assumptions, try <code>norm_num</code> and other to discharge side conditions and eliminate candidates).</p>
<p>Does anybody have an opinion on this large number of lemmas just for multiplication?</p>

#### [ Kevin Buzzard (Mar 16 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123816761):
<p>Don't all of these just follow from 0&lt;=x, 0&lt;=y implies 0&lt;=xy, a&lt;=b implies a+t &lt;= b+t and standard ring theory axioms?</p>

#### [ Simon Hudon (Mar 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123816943):
<p>Do you mean "do all those multiplication lemmas follow from ..."?</p>

#### [ Kevin Buzzard (Mar 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123816949):
<p>right</p>

#### [ Kevin Buzzard (Mar 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123816951):
<p>but presumably you're asking something else</p>

#### [ Kevin Buzzard (Mar 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123816956):
<p>I mean, I am saying that they should do</p>

#### [ Simon Hudon (Mar 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123816957):
<p>In any case, their truth is rather straightforward. What I'm wondering about is how usable they are.</p>

#### [ Kevin Buzzard (Mar 16 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817031):
<p>I have no feeling for this sort of thing. Does simp solve any of them? Presumably some cunning tactic would solve them all?</p>

#### [ Simon Hudon (Mar 16 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817048):
<p>For instance, if I don't split <code>mul_mono_nonpos_nonpos</code> into <code>mul_mono_nonpos_nonpos_left</code> and <code>mul_mono_nonpos_nonpos_right</code>, I get a simpler set of rules. However, some situations won't be addressed by monotonicity because <code>0 ≤ x0</code> and <code>0 ≤ x1</code> are stronger assumptions than what is strictly necessary</p>

#### [ Simon Hudon (Mar 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817116):
<p>I believe you are talking about proving them. Again, proving them is easy. I'm writing them up so that the monotonicity tactic will be able to decompose proofs of <code>x * y ≤ z * w</code> into simpler subgoals.</p>

#### [ Simon Hudon (Mar 16 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817216):
<p>The tricky part in doing that is remembering to have assumptions about some of your terms being non-negative or non-positive.</p>

#### [ Kevin Buzzard (Mar 16 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817225):
<p>But there are are lots of ways to deduce <code>x*y &lt;= z*w</code>, right?</p>

#### [ Simon Hudon (Mar 16 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817252):
<p>If you forget, <code>mono</code> will list all the ways in which <code>*</code> is monotonic with the corresponding side conditions</p>

#### [ Kevin Buzzard (Mar 16 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817255):
<p>e.g. <code>0&lt;=x&lt;=z and 0&lt;=y&lt;=w</code>, or <code>0&lt;=x&lt;=w and 0&lt;=y&lt;=z</code>, or...</p>

#### [ Simon Hudon (Mar 16 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817273):
<p>Exactly. That's why I have 12 monotonicity lemmas for multiplication. It seems like a lot to me but maybe it's justifiable</p>

#### [ Kevin Buzzard (Mar 16 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817275):
<p><code>z&lt;=x&lt;=0 and w&lt;=y&lt;=0...</code></p>

#### [ Kevin Buzzard (Mar 16 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817323):
<p>Do you care about <code>0&lt;=x and z&lt;=-x and 0&lt;=y and w&lt;=-y</code>?</p>

#### [ Kevin Buzzard (Mar 16 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817346):
<p><code>0&lt;=x&lt;=3z and 0&lt;=y&lt;=w/3</code>?</p>

#### [ Simon Hudon (Mar 16 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817350):
<p>I hadn't thought of it. Maybe I should care about that.</p>

#### [ Kevin Buzzard (Mar 16 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817354):
<p>I don't really know what your applications are.</p>

#### [ Kevin Buzzard (Mar 16 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817406):
<p>It's slightly disconcerting that there are so many!</p>

#### [ Simon Hudon (Mar 16 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817409):
<blockquote>
<p><code>0&lt;=x&lt;=3z and 0&lt;=y&lt;=w/3</code>?</p>
</blockquote>
<p>That, I will leave out.</p>

#### [ Simon Hudon (Mar 16 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817414):
<p>Let me give you an example</p>

#### [ Simon Hudon (Mar 16 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817589):
<p>Let's say that you have to prove:</p>
<div class="codehilite"><pre><span></span>⊢ x₀ * x₁ * x₂ * y₀ * x₃ * y₁ * x₄ * x₅ ≤ x₀ * x₁ * x₂ * z₀ * x₃ * z₁ * x₄ * x₅
</pre></div>


<p>I want it to be possible to call </p>
<div class="codehilite"><pre><span></span>mono*
</pre></div>


<p>and get the proof reduced to two goals:</p>
<div class="codehilite"><pre><span></span>⊢ y₀ ≤ z₀
⊢ y₁ ≤ z₁
</pre></div>


<p>provided that you have the right assumptions about <code>x₀</code>, <code>x₁</code>, <code>x₂</code>, <code>x₃</code>, <code>x₄</code>, <code>x₅</code>, namely, them being non-negative or non-positive.</p>

#### [ Kevin Buzzard (Mar 16 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817661):
<p>If there were a simp lemma that said <code>0&lt;x -&gt; (a&lt;=b iff x*a &lt;= x*b)</code> and similar for <code>0&gt;x</code> wouldn't simp get you as far as <code>y0*y1&lt;=z0*z1</code> or similar?</p>

#### [ Kevin Buzzard (Mar 16 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817706):
<p>and then you have no reason to believe y0&lt;=z0 and y1&lt;=z1 because maybe y0&lt;=3*z0 and y1&lt;=z1/3</p>

#### [ Simon Hudon (Mar 16 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817789):
<p>Of course, as a user, you're the one deciding to call <code>mono</code>. And if you want to keep <code>y</code> and <code>z</code> in the same goal <code>ac_mono</code> will get you the goal that you're mentioning. But <code>simp</code> can't get you there automatically because the choice of rewrite is not unique so marking those lemmas as <code>[simp]</code> would make your proofs brittle</p>

#### [ Simon Hudon (Mar 16 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817847):
<p>And if you only want a few steps of mono, you can use <code>mono^3</code> instead and it will stop after three applications of monotonicity laws</p>

#### [ Simon Hudon (Mar 16 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/About%20monotonicity/near/123817872):
<p>The point is, in a monotonic context, you can get rid of all lot of noise in one shot using <code>mono</code> or <code>ac_mono</code></p>


{% endraw %}
