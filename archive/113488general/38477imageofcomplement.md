---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/38477imageofcomplement.html
---

## Stream: [general](index.html)
### Topic: [image of complement](38477imageofcomplement.html)

---


{% raw %}
#### [ Patrick Massot (Mar 13 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123655801):
Do we have `{α : Type*} {β : Type*} (f : α ≃ β) (s : set α) : f '' -s = -(f '' s)` in mathlib?

#### [ Johannes Hölzl (Mar 13 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123655882):
I guess you want `f : A -> B`, its `preimage_compl`.

#### [ Patrick Massot (Mar 13 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656012):
No, I'd like what I stated

#### [ Patrick Massot (Mar 13 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656014):
with direct image

#### [ Patrick Massot (Mar 13 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656016):
assuming bijectivity

#### [ Patrick Massot (Mar 13 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656081):
I admit both the equiv and double apostrophes are hard to read on my screen too

#### [ Kevin Buzzard (Mar 13 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656089):
you could use `preimage_compl` on the map in the other direction ;-)

#### [ Patrick Massot (Mar 13 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656124):
I'm pretty sure I can prove this lemma, I was asking about its current existence

#### [ Johannes Hölzl (Mar 13 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656345):
Ah sorry. Then no: I think its not yet in mathlib.

#### [ Patrick Massot (Mar 13 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/image%20of%20complement/near/123656352):
Ok, I hope I'll be able to contribute this


{% endraw %}
