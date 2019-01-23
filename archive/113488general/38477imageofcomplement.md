---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/38477imageofcomplement.html
---

## Stream: [general](index.html)
### Topic: [image of complement](38477imageofcomplement.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 13 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123655801):
Do we have `{α : Type*} {β : Type*} (f : α ≃ β) (s : set α) : f '' -s = -(f '' s)` in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Mar 13 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123655882):
I guess you want `f : A -> B`, its `preimage_compl`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 13 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656012):
No, I'd like what I stated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 13 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656014):
with direct image

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 13 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656016):
assuming bijectivity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 13 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656081):
I admit both the equiv and double apostrophes are hard to read on my screen too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 13 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656089):
you could use `preimage_compl` on the map in the other direction ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 13 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656124):
I'm pretty sure I can prove this lemma, I was asking about its current existence

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Mar 13 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656345):
Ah sorry. Then no: I think its not yet in mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 13 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656352):
Ok, I hope I'll be able to contribute this


{% endraw %}
