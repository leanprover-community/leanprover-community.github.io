---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73720failedtoadddeclaration.html
---

## Stream: [general](index.html)
### Topic: [failed to add declaration](73720failedtoadddeclaration.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 15 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20add%20declaration/near/134011400):
Has anyone ever seen the error `failed to add declaration 'xxxx.my_defn' to environment, type has metavariables` while writing a tactic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 15 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20add%20declaration/near/134011412):
How can I see what the metavariables are?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 15 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20add%20declaration/near/134023923):
`mathlib` has `list_meta_vars` in `tactic.basic`. It may be enough to just `instantiate_mvars` before adding your definition.

