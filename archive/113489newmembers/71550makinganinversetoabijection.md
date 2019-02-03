---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/71550makinganinversetoabijection.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [making an inverse to a bijection](https://leanprover-community.github.io/archive/113489newmembers/71550makinganinversetoabijection.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sebastian Zimmer (Oct 14 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135775250):
<p>Is there something in mathlib that lets you (constructively) make an inverse to a bijection between two fintypes with decidably equality?</p>
<p>It feels to me like it should be possible without axioms.</p>

#### [ Mario Carneiro (Oct 14 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135775318):
<p>You are right that it is possible without axioms, but I don't think we have exactly that</p>

#### [ Sebastian Zimmer (Oct 14 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135775361):
<p>How about unique choice in a fintype?</p>

#### [ Mario Carneiro (Oct 14 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135775365):
<p>There is <code>encodable.choose</code>, but a fintype isn't actually <code>encodable</code> because it doesn't have an ordering</p>

#### [ Mario Carneiro (Oct 14 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135775368):
<p>but as you say for unique choice it doesn't matter</p>

#### [ Mario Carneiro (Oct 14 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135775374):
<p>That's something that makes sense to define, but you would have to write it yourself (and PR to mathlib)</p>

#### [ Sebastian Zimmer (Oct 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135790982):
<p>I've implemented this. Should I make a PR to leanprover-community or directly to leanprover/mathlib?</p>

#### [ Bryan Gin-ge Chen (Oct 14 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135793320):
<p>You should PR directly to mathlib. leanprover-community is typically used as a collaborative staging area for larger PR's that multiple people work on; you can get contributor access to it if you ask Mario or Simon Hudon.</p>

#### [ Mario Carneiro (Oct 14 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135793395):
<p>I don't know your github username</p>

#### [ Bryan Gin-ge Chen (Oct 14 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135793496):
<p>It looks like Sebastian has already opened a PR to leanprover-community:</p>
<p><a href="https://github.com/leanprover-community/mathlib/pull/7" target="_blank" title="https://github.com/leanprover-community/mathlib/pull/7">https://github.com/leanprover-community/mathlib/pull/7</a></p>

#### [ Sebastian Zimmer (Oct 15 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/135795680):
<p>ok, I've opened a PR directly to mathlib here <a href="https://github.com/leanprover/mathlib/pull/421" target="_blank" title="https://github.com/leanprover/mathlib/pull/421">https://github.com/leanprover/mathlib/pull/421</a></p>

#### [ Sebastian Zimmer (Oct 21 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/making%20an%20inverse%20to%20a%20bijection/near/136213925):
<p>I made a bunch of changes in reponse to the comments on it</p>


{% endraw %}
