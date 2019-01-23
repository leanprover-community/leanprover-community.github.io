---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28591instanceloop.html
---

## Stream: [general](index.html)
### Topic: [instance loop?](28591instanceloop.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 22 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136284768):
I made an instance `instance normal_of_compact_t2 [topological_space α] [t2_space α] [compact_space α] : normal_space α` where `normal_space` extends `t2_space`. Apparently this was a bad idea because Lean now thinks that the way it should try to prove a space is T2 is to use `normal_space.to_t2_space` and use this instance to reduce the problem to showing the space is T2 and compact...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 22 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136284802):
Is there a way to work around this kind of issue? Or do I just not get to write the instance `normal_of_compact_t2`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 22 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136284881):
I would have hoped that maybe Lean wouldn't try to solve a goal which is the same as one it was trying to solve higher up in the recursion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 22 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136284920):
Concretely the issue is that there's also another class `regular_space` which extends `t2_space`, and Lean is unable to see that a `regular_space` is T2 because it falls into this loop instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Oct 22 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136284937):
That would be a relatively expensive check. And of course not sufficient to prevent all loops

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 22 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136285034):
Doesn't Lean already have some kind of cache it checks for instances in, so couldn't it insert constraints that are in the process of being solved as "gray" nodes in the cache?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 22 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136285068):
I guess it would still be somewhat expensive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 22 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136285420):
What's the general restriction here? If I have class B which extends class A, I can't write an instance which says that A + something else gives me B?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 22 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136285593):
I'm a little confused because somehow I was under the impression that there were actually lots of instance loops and somehow the class inference engine was able to handle them


{% endraw %}
