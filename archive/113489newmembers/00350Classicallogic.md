---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/00350Classicallogic.html
---

## Stream: [new members](index.html)
### Topic: [Classical logic](00350Classicallogic.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alexandru-Andrei Bosinta (Nov 21 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148124896):
What is the problem with classical logic in Lean? Why does one have to use `open classical` in order to use the law of the excluded middle? Also what is up with all the `decidable` that I see in some theorems? Does classical logic (somehow) create any problems to computation (aka it slows down the computation)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 21 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125000):
There is no problem, and classical logic does not slow down computation, it prevents computation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 21 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125191):
Let me define a function for you, from natural to numbers to natural numbers. It sends every natural number to 0 if Riemann hypothesis is true, to 1 otherwise. This function is well defined because Riemann hypothesis is either true or false. How would you expect your computer to compute this function?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 21 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125207):
This is not specific to Lean in any way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Nov 21 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125231):
```quote
What is the problem with classical logic in Lean? Why does one have to use `open classical` in order to use the law of the excluded middle? Also what is up with all the `decidable` that I see in some theorems? Does classical logic (somehow) create any problems to computation (aka it slows down the computation)?
```
 There's no problem -- classical logic just introduces the axiom of choice into the system.

As for opening classical, this is just so that you don't need to use "`classical.`" before everything you use from the `classical.lean` file. It's just like writing `open complex` or open anything.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 21 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125305):
Not necessarily axiom of choice. The law of excluded middle is already an extra, for reasons I just explained

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Nov 21 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125385):
@**Patrick Massot** I'm reading `classical.lean`, and the only thing introduced as an axiom seems to be choice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Nov 21 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125392):
The law of the excluded middle is proven from it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 21 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125406):
Oh maybe. Who cares? We assume all this anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 21 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148125426):
But I'm pretty sure you could also define EM as an axiom without assuming choice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alexandru-Andrei Bosinta (Nov 21 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148126372):
Oh, this makes sense. So then, is there a reason to try harder to find a proof without using classical logic? Or is it perfectly fine either way?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 21 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148126481):
Depends on what you want...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 21 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148126518):
But, I would start out by not caring at all.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 21 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148126592):
And then, at some point you'll realise that you'dd like certain things to compute

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148127501):
yeah, I think you are talking to the wrong crowd - lean is not making any attempts to be intuitionistic, although some of this heritage comes from the fact that it is built on dependent type theory so that LEM has a different character than the other axioms. Plus some people care about computation and lean will track it for you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 21 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148127528):
Most of the library is not avoiding classical logic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Nov 21 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Classical%20logic/near/148129380):
One example why proving decidability of (some) propositions is useful, instead of just assuming that all propositions are decidable, is that you can run the proofs. For example, in `core` there is a proof that `<` on `nat` is decidable. This means that you can prove `3 < 5` by saying "run the proof of decidability, and check that it is true" (the notation for this is `dec_trivial`).


{% endraw %}
