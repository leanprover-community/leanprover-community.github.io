---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/71550makinganinversetoabijection.html
---

## Stream: [new members](index.html)
### Topic: [making an inverse to a bijection](71550makinganinversetoabijection.html)

---

#### [Sebastian Zimmer (Oct 14 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135775250):
Is there something in mathlib that lets you (constructively) make an inverse to a bijection between two fintypes with decidably equality?

It feels to me like it should be possible without axioms.

#### [Mario Carneiro (Oct 14 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135775318):
You are right that it is possible without axioms, but I don't think we have exactly that

#### [Sebastian Zimmer (Oct 14 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135775361):
How about unique choice in a fintype?

#### [Mario Carneiro (Oct 14 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135775365):
There is `encodable.choose`, but a fintype isn't actually `encodable` because it doesn't have an ordering

#### [Mario Carneiro (Oct 14 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135775368):
but as you say for unique choice it doesn't matter

#### [Mario Carneiro (Oct 14 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135775374):
That's something that makes sense to define, but you would have to write it yourself (and PR to mathlib)

#### [Sebastian Zimmer (Oct 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135790982):
I've implemented this. Should I make a PR to leanprover-community or directly to leanprover/mathlib?

#### [Bryan Gin-ge Chen (Oct 14 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135793320):
You should PR directly to mathlib. leanprover-community is typically used as a collaborative staging area for larger PR's that multiple people work on; you can get contributor access to it if you ask Mario or Simon Hudon.

#### [Mario Carneiro (Oct 14 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135793395):
I don't know your github username

#### [Bryan Gin-ge Chen (Oct 14 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135793496):
It looks like Sebastian has already opened a PR to leanprover-community:

https://github.com/leanprover-community/mathlib/pull/7

#### [Sebastian Zimmer (Oct 15 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135795680):
ok, I've opened a PR directly to mathlib here https://github.com/leanprover/mathlib/pull/421

#### [Sebastian Zimmer (Oct 21 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/136213925):
I made a bunch of changes in reponse to the comments on it

