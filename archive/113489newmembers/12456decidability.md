---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/12456decidability.html
---

## Stream: [new members](index.html)
### Topic: [decidability](12456decidability.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 12 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/decidability/near/147521031):
How can you ask lean to decide something which is decidable? e.g. `prime n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 12 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/decidability/near/147521350):
`dec_trivial` will do it in theory, but for primes it might well time out in practice and you're better off using `norm_num`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 12 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/decidability/near/147521438):
ok thanks Kevin

