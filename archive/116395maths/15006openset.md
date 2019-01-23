---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/15006openset.html
---

## Stream: [maths](index.html)
### Topic: [open_set](15006openset.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 09 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open_set/near/135489758):
@**Scott Morrison|110087** I'm curious why you reversed the direction of the arrows of `open_set`. I would rather put the contravariant-ness in the notion of (pre)sheaf.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open_set/near/135500583):
Ah, I hadn't seen this, and asked your opinion elsewhere. I'll reverse it again when I get there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open_set/near/135502013):
Yes Scott mentioned this before I think. Maybe he said something like he had ops everywhere at all times with no obvious purpose?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open_set/near/135502023):
I guess the point is that we never use the unopped category

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open_set/near/135511685):
Right, but once we start doing sheaves over sites we will want contravariant (pre)sheaves. And we also want those to specialise to "plain old" (pre)sheaves on open sets. So I vote for keeping the `op`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 10 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/open_set/near/135521274):
Another question of course is where you want the `op` -- source or target. It's funny this is coming up now. I distinctly remember Scott saying "eew there are `op`s everywhere, but I've had a brilliant idea -- if we just redefine the open set category then they all go away and it's much easier to use" and it was one of those moments where I just thought "yeah, it's not ideal but I can completely see his point. It removes all of them at once."

