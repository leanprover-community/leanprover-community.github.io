---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68329definitiondependingontheorem.html
---

## Stream: [general](index.html)
### Topic: [definition depending on theorem](68329definitiondependingontheorem.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/definition%20depending%20on%20theorem/near/135382946):
For my Lean-talk I would like a good example of a definition that depends on a (non-trivial) theorem. I don't want to use perfectoid spaces because that is way too advanced. I want to use this thread to collect a list of cute examples.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 08 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/definition%20depending%20on%20theorem/near/135383090):
How about: the dimension of a vector space depending on the fact that all bases have the same cardinality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/definition%20depending%20on%20theorem/near/135383347):
technically, the definition doesn't need this assumption, because it is defined as the *minimum* of such cardinalities. Instead, a proof is required to show that a minimum of cardinalities is well defined

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 08 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/definition%20depending%20on%20theorem/near/135384058):
convergence of exponential series. Also proof that the polynomial division algorithm is well founded took me a while. All of these can be done without any proofs technically, with some `dite` statement.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/definition%20depending%20on%20theorem/near/135384131):
at the expense of computability of course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 08 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/definition%20depending%20on%20theorem/near/135387000):
The definition of an affine scheme needs the fact that the structure sheaf on $$Spec(A)$$ is actually a sheaf, which took us quite some time to prove.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/definition%20depending%20on%20theorem/near/135387024):
Yes, but I will be talking to an audience that partly doesn't know what a sheaf is...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 08 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/definition%20depending%20on%20theorem/near/135387944):
What about the definition of addition of real numbers? Or even addition or integers

