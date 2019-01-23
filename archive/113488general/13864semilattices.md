---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/13864semilattices.html
---

## Stream: [general](index.html)
### Topic: [semilattices](13864semilattices.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semilattices/near/125457488):
I'm looking for a kind of semilattice with a bottom, and I'd like to be able to take the limit of a monotonically increasing series. Does it exist, is it in `mathlib` and what is it called?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 21 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semilattices/near/125471273):
This is often called a chain-complete partial order. I don't think it is in mathlib yet. I have a very old theory about the fixed construction,  but it doesn't compile anymore (see https://gist.github.com/johoelzl/900ec0250f46a2ac4070bfc4f4fd0405 )

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 21 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semilattices/near/125491615):
Cool! Thanks! Do you mind if I fix it up and PR it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 23 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semilattices/near/125557833):
Of course! Go on.

