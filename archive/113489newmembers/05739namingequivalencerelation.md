---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/05739namingequivalencerelation.html
---

## Stream: [new members](index.html)
### Topic: [naming equivalence relation](05739namingequivalencerelation.html)

---


{% raw %}
#### [ Ali Sever (Jul 18 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129879693):
<p>I have a function <code>eqd : point → point → point → point → Prop</code>, and I have made an equivalence relation on <code>point × point</code>. Instead of using <code>setoid.r (a,b) (c,d)</code>, is it possible to change the notation to be <code>(a,b) ≡ (c,d)</code>?</p>

#### [ Reid Barton (Jul 18 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129879836):
<p>Yes.<br>
You can already use <code>≈</code> as notation for <code>setoid.r</code>, if you don't mind using that instead.</p>

#### [ Reid Barton (Jul 18 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129879955):
<p>Otherwise, you can define <code>local infix ≡ := setoid.r</code>, or a number of variations on this.</p>

#### [ Reid Barton (Jul 18 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129879991):
<p><code>local</code> is optional, depending on whether you want the notation to be in effect everywhere or only in the current file/section</p>

#### [ Ali Sever (Jul 18 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129881273):
<p>I'm assuming it's not possible to make the notation <code>a b ≡ c d</code>.</p>

#### [ Kevin Buzzard (Jul 18 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129882842):
<p>I don't know if the parser can handle that. You want more than an infix operator -- you want an operator which eats two things on both sides. I wonder if <code>(a b ≡ c d)</code> would be possible somehow?</p>

#### [ Patrick Massot (Jul 18 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129882911):
<p>Depends on your alignment. Chaotic evil players are allowed to use tricky unicode blank characters to achieve what you want.</p>

#### [ Reid Barton (Jul 18 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129882947):
<p>I don't think you can have two arguments to the notation separated only by whitespace.<br>
The way to test this is to try out things like <code>notation a b ` ≡ ` c d := a + b</code>. That gives an error on <code>b</code>.</p>

#### [ Reid Barton (Jul 18 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129882955):
<p>Yes, I should have been more careful and specified which sort of whitespace I meant. :)</p>

#### [ Reid Barton (Jul 18 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/naming%20equivalence%20relation/near/129883881):
<p>Another option for the chaotic player is to define a <code>has_coe_to_fun</code> from <code>point</code> to <code>point -&gt; (point, point)</code> which sends <code>a</code> to <code>\lam b, (a, b)</code>.</p>


{% endraw %}
