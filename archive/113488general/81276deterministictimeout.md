---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/81276deterministictimeout.html
---

## Stream: [general](index.html)
### Topic: [deterministic timeout](81276deterministictimeout.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jun 28 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deterministic%20timeout/near/128748875):
In general, how to solve "(deterministic) timeout" error?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Zesen Qian (Jun 28 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deterministic%20timeout/near/128749202):
I have tried increasing the timeout limit, so it must be my code.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 28 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deterministic%20timeout/near/128751744):
Yes and it depends on the tactics that you use. Often, `simp` is the offender. When you give it a list of rules that do not converge, it will just keep going.

