---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58179thetypeofapitype.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [the type of a pi type.](https://leanprover-community.github.io/archive/113488general/58179thetypeofapitype.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Adam Kurkiewicz (Mar 15 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123762898):
<p>After a few months break I am revisiting lean basics. I'm looking back at dependent types.</p>
<p>I understand why this typechecks: <code>((λ k: nat, eq.refl k) : (Π k : nat, k = k))</code> essentially we have a function, which returns a type, which depends on the parameter the function takes. We need this because we want to have a family of proofs 0 = 0, 1 = 1, etc.</p>
<p>But I don't get why these typecheck: <code>((Π k : nat, k = k) : Prop)</code> or <code>((Π k: nat, Prop) : Type)</code>. The rule seems to be that the type signature of any pi type "forgets" the parameters that the type on the left depends on  and behaves as if it was a simple type.</p>
<p>Are there any particular reasons of why that is or is it just the way it is?</p>

#### [ Simon Hudon (Mar 15 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763082):
<p>Yes. Let's look at the non-dependent case first. Let's first notice that everything has a type:</p>
<div class="codehilite"><pre><span></span>(λ n : ℕ, n+1) : ℕ → ℕ
ℕ → ℕ : Type 0
Type 0 : Type 1
-- and so on
</pre></div>

#### [ Kenny Lau (Mar 15 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763084):
<p><span class="user-mention" data-user-id="111040">@Adam Kurkiewicz</span> if A has type u and B has type v, then <code>A -&gt; B</code> has type <code>max u v</code></p>

#### [ Simon Hudon (Mar 15 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763161):
<p>And <code>ℕ → ℕ</code> is basically syntactic sugar for <code>Π n : ℕ, ℕ</code></p>

#### [ Simon Hudon (Mar 15 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763501):
<blockquote>
<p>The rule seems to be that the type signature of any pi type "forgets" the parameters that the type on the left depends on and behaves as if it was a simple type.</p>
</blockquote>
<p>That's correct. </p>
<blockquote>
<p>Are there any particular reasons of why that is or is it just the way it is?</p>
</blockquote>
<p>For one thing it is useful. But let's look at an alternative:</p>
<div class="codehilite"><pre><span></span>(Π k : nat, k = k) : nat -&gt; Prop
</pre></div>


<p>That means that that proposition is not true on its own. It would be true about a given number. But that's not the case. <code>Π</code> is the same as <code>∀</code>. The statement is not "if you give me a number, I'll state that it is equal to itself". It is "every number is equal to itself". If you want the first, you'll use <code>(λ k : nat, k = k) : nat -&gt; Prop</code>. It is not an assertion on its own. You feed it a natural number and then the result will state something about that natural number.</p>

#### [ Adam Kurkiewicz (Mar 15 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763607):
<p>I see. So it doesn't forget the type of the parameter, it just takes the maximum of the type of the parameter and the type of the type. So <code>Prop</code> is effectively <code>Type -1</code>, right? And since <code>nat : Type 0</code>, then <code>k : Type -1</code> and <code>k = k : Type -1</code> is <code>Type -1</code>, so the total result is <code>Type max -1 -1</code>, which is <code>Type -1</code>, which is <code>Prop</code>. This might be a little bit barbarian, but I think I'm getting it.</p>

#### [ Simon Hudon (Mar 15 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763673):
<p>A less barbarian way of seeing is that <code>Prop</code> and <code>Type</code> are both syntactic sugar for <code>Sort</code>: <code>Prop = Sort 0</code> and <code>Type u = Sort (u+1)</code></p>

#### [ Moses Schönfinkel (Mar 15 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763727):
<p>I am surprised you would care so much about universes (given that you are a beginner I assume). This information is not very useful in my opinion :).</p>

#### [ Adam Kurkiewicz (Mar 15 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763751):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> I actually do not think that my original statement was correct. The type of the parameter is not forgotten, it's the maximum like <span class="user-mention" data-user-id="110064">@Kenny Lau</span> said, for example this typechecks <code>#check ((Π k: Type 0, Prop) : Type 1)</code></p>

#### [ Simon Hudon (Mar 15 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763757):
<p>Really? For small proofs maybe but as soon as you have types within types, you have to start caring about universes</p>

#### [ Moses Schönfinkel (Mar 15 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763803):
<p>Not quite. You can rely on <code>Type*</code> to do the work for you.</p>

#### [ Simon Hudon (Mar 15 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763826):
<blockquote>
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> I actually do not think that my original statement was correct. The type of the parameter is not forgotten, it's the maximum like <span class="user-mention" data-user-id="110064">@Kenny Lau</span> said, for example this typechecks <code>#check ((Π k: Type 0, Prop) : Type 1)</code></p>
</blockquote>
<p>That's true, in that sense, it does not forget. More specifically, it does not forget the universe of the parameter. The type itself becomes unavailable though</p>

#### [ Adam Kurkiewicz (Mar 15 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763874):
<p>I've largely ignored universes so far, and most of the underlying type theory, but given that I might be teaching lean to others from next semester I'm trying to make sure I know at least a little bit of the foundations.</p>

#### [ Simon Hudon (Mar 15 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763883):
<p>Interesting detail:</p>
<div class="codehilite"><pre><span></span>#check ((Π k: Type 7, k = k) : Prop)
</pre></div>


<p>If the result type is Prop, the whole thing can stay in Prop</p>

#### [ Moses Schönfinkel (Mar 15 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763889):
<p>I think you've done well to ignore them for the most part :P!</p>

#### [ Simon Hudon (Mar 15 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123763932):
<p>I think I agree. I don't particularly like to have to specify them. I wonder what justify that design choice</p>

#### [ Moses Schönfinkel (Mar 15 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123764002):
<p>I use <code>Type*</code> and only think about it once I run into issues. From my experience, I find it not too difficult to fix them post-facto. I have yet to encounter a case where I wish I had considered it beforehand. But perhaps I avoid the kinds of things that might require more universe-thought. I mostly write certificates of functional programs.</p>

#### [ Adam Kurkiewicz (Mar 15 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123764081):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> hmm... So it turns out it's not <code>max u v</code>after all? It can't be, since in this case it would have to be <code>Type 7</code> as opposed to <code>Prop</code>?</p>

#### [ Reid Barton (Mar 15 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123764133):
<p>It's actually <code>imax u v</code> which is 0 if <code>v</code> is 0, and otherwise <code>max u v</code>.</p>

#### [ Moses Schönfinkel (Mar 15 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123764146):
<p>&lt;deleted&gt;</p>

#### [ Reid Barton (Mar 15 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123764165):
<p>Useful to know mainly because you might see <code>imax</code> in Lean output/error messages and wonder what it means, I think.</p>

#### [ Adam Kurkiewicz (Mar 15 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123764339):
<p>Thanks <span class="user-mention" data-user-id="110032">@Reid Barton</span>, this will definitely come useful at some point.</p>
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> I really like your example with natural numbers. I think it's another productive way of thinking about Pi types.</p>

#### [ Simon Hudon (Mar 15 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/the%20type%20of%20a%20pi%20type./near/123764351):
<p>Do you mean that <code>nat -&gt; Prop</code> example?</p>


{% endraw %}
