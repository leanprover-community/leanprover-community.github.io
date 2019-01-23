---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45015calclhsrhs.html
---

## Stream: [general](index.html)
### Topic: [calc lhs/rhs](45015calclhsrhs.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 20 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20lhs/rhs/near/148043376):
When writing `calc` blocks, it would be very convenient if we could have some special symbol that refers to the lhs/rhs of the original goal. Because currently I try to copy paste stuff from the goal, and then Lean starts moaning that it can't figure out the type etc...
I guess it might be tricky to use literal `lhs`, because people might want to use that as variable name. But maybe something can be done?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 20 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20lhs/rhs/near/148043505):
I've been using `_` to start / end `calc` blocks with the lhs / rhs.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 20 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20lhs/rhs/near/148043761):
Hmm, I fear that it will then start moaning about `X` in `_ = X`... But I'll try.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 20 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20lhs/rhs/near/148044194):
Meeh, it's not really working...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 20 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20lhs/rhs/near/148044384):
MWE?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 20 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20lhs/rhs/near/148044572):
Well... I don't really know how to produce a MWE. I'm not going to trim down my `sheaf` branch... I guess I could just enable `pp.all` and copy-paste the lhs into the calc-block. It's just more convenient if there would be a shorthand for it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 20 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20lhs/rhs/near/148044697):
Fail... `pp.all` is trimming my output. It is too long :rolling_on_the_floor_laughing:

