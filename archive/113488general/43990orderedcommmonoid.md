---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43990orderedcommmonoid.html
---

## Stream: [general](index.html)
### Topic: [ordered_comm_monoid](43990orderedcommmonoid.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 29 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134890643):
Why is `ordered_comm_monoid` additive? I thought `{x : real | x ≥ 1}` is a really nice ordered commutative monoid...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 29 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134890739):
Because most ordered comm monoids are additive, like reals, ints, nats, rats, with_bot nat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 29 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134890797):
Sure, but we could still have the `add` in the name right? And I think there are enough examples where they aren't additive, like positive reals, nats, positive rats...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134894040):
That makes sense. Btw, isn't `{x : real | x ≥ 1}` a commutative group?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134894089):
inverse?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Zimmer (Sep 29 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134894526):
Is your group operation (x, y) -> (x - 1)(y - 1) + 1 or something crazy like that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 29 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134894577):
that would make 1 have no inverse

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Zimmer (Sep 29 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134894578):
ah good point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 29 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134894978):
Right, somehow, the fact that the inverse is less than one escaped me. You'd need { x : real | x > 0 } for a group.

