---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21598Precedenceoffunctionapplication.html
---

## [general](index.html)
### [Precedence of function application](21598Precedenceoffunctionapplication.html)

#### [Joe Hendrix (Aug 08 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Precedence of function application/near/131073950):
Can notation bind tighter than function application?  e.g. For an operator `^` make `f x ^ y` parse as `f (x ^ y)`?

#### [Chris Hughes (Aug 08 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Precedence of function application/near/131074272):
I think not.

#### [Kevin Buzzard (Aug 08 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Precedence of function application/near/131074274):
I think that (a) function application has super-high binding power and (b) if you want to use notation which already exists in Lean (like `^`) then, whilst you can define it to mean new things, you cannot change its default binding power, which is lower than the super-high binding power of functions. So at the very least you would have to use notation which is not already used in Lean, e.g. `\clubsuit` or some random thing like that.

#### [Joe Hendrix (Aug 08 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Precedence of function application/near/131074958):
Yes, I meant "^" as a placeholder.   It looks like I can, but it was a much higher binding power than I tested at first.

#### [Joe Hendrix (Aug 08 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Precedence of function application/near/131075107):
This seemed to work,  but if the precedence is any lower it doesn't.

```
set_option pp.all true

infix ` <> `:1025 := and
constant f : Prop → Prop
#check f true <> false
```

Anyways, thanks for suggesting the "super-high" binding power.

#### [Mario Carneiro (Aug 08 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Precedence of function application/near/131077736):
Yes, you can. The binding power of application is `max = 1024`, which despite the name is not the maximum possible bonding power; you can see `max+10` used in the `core.lean` file.

#### [François G. Dorais (Aug 08 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Precedence of function application/near/131078180):
BTW: `max_plus` is useful, it evaluates to 1034 (aka `max+10`) and avoids silly incidents like `max+11` (aka `max_spinal_tap`).

