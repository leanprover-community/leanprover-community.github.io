---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28591instanceloop.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [instance loop?](https://leanprover-community.github.io/archive/113488general/28591instanceloop.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Oct 22 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136284768):
<p>I made an instance <code>instance normal_of_compact_t2 [topological_space α] [t2_space α] [compact_space α] : normal_space α</code> where <code>normal_space</code> extends <code>t2_space</code>. Apparently this was a bad idea because Lean now thinks that the way it should try to prove a space is T2 is to use <code>normal_space.to_t2_space</code> and use this instance to reduce the problem to showing the space is T2 and compact...</p>

#### [ Reid Barton (Oct 22 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136284802):
<p>Is there a way to work around this kind of issue? Or do I just not get to write the instance <code>normal_of_compact_t2</code>?</p>

#### [ Reid Barton (Oct 22 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136284881):
<p>I would have hoped that maybe Lean wouldn't try to solve a goal which is the same as one it was trying to solve higher up in the recursion</p>

#### [ Reid Barton (Oct 22 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136284920):
<p>Concretely the issue is that there's also another class <code>regular_space</code> which extends <code>t2_space</code>, and Lean is unable to see that a <code>regular_space</code> is T2 because it falls into this loop instead</p>

#### [ Sebastian Ullrich (Oct 22 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136284937):
<p>That would be a relatively expensive check. And of course not sufficient to prevent all loops</p>

#### [ Reid Barton (Oct 22 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136285034):
<p>Doesn't Lean already have some kind of cache it checks for instances in, so couldn't it insert constraints that are in the process of being solved as "gray" nodes in the cache?</p>

#### [ Reid Barton (Oct 22 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136285068):
<p>I guess it would still be somewhat expensive</p>

#### [ Reid Barton (Oct 22 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136285420):
<p>What's the general restriction here? If I have class B which extends class A, I can't write an instance which says that A + something else gives me B?</p>

#### [ Reid Barton (Oct 22 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20loop%3F/near/136285593):
<p>I'm a little confused because somehow I was under the impression that there were actually lots of instance loops and somehow the class inference engine was able to handle them</p>


{% endraw %}
