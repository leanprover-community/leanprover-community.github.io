---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/15096eliminatingimpossiblecases.html
---

## Stream: [general](index.html)
### Topic: [eliminating impossible cases](15096eliminatingimpossiblecases.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 20 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eliminating%20impossible%20cases/near/152279702):
If I have `hi : i < 0` as a hypothesis (`i` is a `nat`), what tactic will let me solve the goal most efficiently?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 20 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eliminating%20impossible%20cases/near/152279750):
Is `exact absurd hi (nat.not_lt_zero _)` really the easiest way?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eliminating%20impossible%20cases/near/152279761):
`cases hi`

