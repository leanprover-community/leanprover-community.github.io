---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/11204tacticsinsidedefinitions.html
---

## Stream: [new members](index.html)
### Topic: [tactics inside definitions](11204tacticsinsidedefinitions.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 15 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/tactics%20inside%20definitions/near/135796356):
@**Kenny Lau** [said](https://github.com/leanprover/mathlib/pull/421#discussion_r225011707):
>You shouldn't use any tactics in a definition unless you know what you're doing, I think.

Why is this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 15 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/tactics%20inside%20definitions/near/135796362):
because it would be hxxx when you unfold the definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 15 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/tactics%20inside%20definitions/near/135796540):
The rule of thumb is: tactics generate weird proof terms. So sure use tactics when proving theorems (because the proof terms are forgotten) and you can even use tactics when defining complex things like `ring R` for the bits which are proofs (e.g. proof of associativity) -- but the moment you use a tactic as part of a definition of some data it's not going to unfold well, making the definition hard to use in general.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 15 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/tactics%20inside%20definitions/near/135797057):
Thanks, with the exception for "proof bits" of structures this makes much more sense. I just went through the code I've written and I've been more or less following this without knowing it.


{% endraw %}
