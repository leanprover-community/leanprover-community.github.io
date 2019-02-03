---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/00350Classicallogic.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Classical logic](https://leanprover-community.github.io/archive/113489newmembers/00350Classicallogic.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Alexandru-Andrei Bosinta (Nov 21 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148124896):
<p>What is the problem with classical logic in Lean? Why does one have to use <code>open classical</code> in order to use the law of the excluded middle? Also what is up with all the <code>decidable</code> that I see in some theorems? Does classical logic (somehow) create any problems to computation (aka it slows down the computation)?</p>

#### [ Patrick Massot (Nov 21 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125000):
<p>There is no problem, and classical logic does not slow down computation, it prevents computation</p>

#### [ Patrick Massot (Nov 21 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125191):
<p>Let me define a function for you, from natural to numbers to natural numbers. It sends every natural number to 0 if Riemann hypothesis is true, to 1 otherwise. This function is well defined because Riemann hypothesis is either true or false. How would you expect your computer to compute this function?</p>

#### [ Patrick Massot (Nov 21 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125207):
<p>This is not specific to Lean in any way</p>

#### [ Abhimanyu Pallavi Sudhir (Nov 21 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125231):
<blockquote>
<p>What is the problem with classical logic in Lean? Why does one have to use <code>open classical</code> in order to use the law of the excluded middle? Also what is up with all the <code>decidable</code> that I see in some theorems? Does classical logic (somehow) create any problems to computation (aka it slows down the computation)?</p>
</blockquote>
<p>There's no problem -- classical logic just introduces the axiom of choice into the system.</p>
<p>As for opening classical, this is just so that you don't need to use "<code>classical.</code>" before everything you use from the <code>classical.lean</code> file. It's just like writing <code>open complex</code> or open anything.</p>

#### [ Patrick Massot (Nov 21 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125305):
<p>Not necessarily axiom of choice. The law of excluded middle is already an extra, for reasons I just explained</p>

#### [ Abhimanyu Pallavi Sudhir (Nov 21 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125385):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> I'm reading <code>classical.lean</code>, and the only thing introduced as an axiom seems to be choice.</p>

#### [ Abhimanyu Pallavi Sudhir (Nov 21 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125392):
<p>The law of the excluded middle is proven from it.</p>

#### [ Patrick Massot (Nov 21 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125406):
<p>Oh maybe. Who cares? We assume all this anyway</p>

#### [ Patrick Massot (Nov 21 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125426):
<p>But I'm pretty sure you could also define EM as an axiom without assuming choice</p>

#### [ Alexandru-Andrei Bosinta (Nov 21 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148126372):
<p>Oh, this makes sense. So then, is there a reason to try harder to find a proof without using classical logic? Or is it perfectly fine either way?</p>

#### [ Johan Commelin (Nov 21 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148126481):
<p>Depends on what you want...</p>

#### [ Johan Commelin (Nov 21 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148126518):
<p>But, I would start out by not caring at all.</p>

#### [ Johan Commelin (Nov 21 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148126592):
<p>And then, at some point you'll realise that you'dd like certain things to compute</p>

#### [ Mario Carneiro (Nov 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148127501):
<p>yeah, I think you are talking to the wrong crowd - lean is not making any attempts to be intuitionistic, although some of this heritage comes from the fact that it is built on dependent type theory so that LEM has a different character than the other axioms. Plus some people care about computation and lean will track it for you</p>

#### [ Mario Carneiro (Nov 21 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148127528):
<p>Most of the library is not avoiding classical logic</p>

#### [ Floris van Doorn (Nov 21 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148129380):
<p>One example why proving decidability of (some) propositions is useful, instead of just assuming that all propositions are decidable, is that you can run the proofs. For example, in <code>core</code> there is a proof that <code>&lt;</code> on <code>nat</code> is decidable. This means that you can prove <code>3 &lt; 5</code> by saying "run the proof of decidability, and check that it is true" (the notation for this is <code>dec_trivial</code>).</p>


{% endraw %}
