---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/179818LeanTogether2019/22669smallscalereflection.html
---

## Stream: [Lean Together 2019](index.html)
### Topic: [small scale reflection](22669smallscalereflection.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 10 2019 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/small%20scale%20reflection/near/154824750):
Assia is talking about small scale reflection. 

The following is reflection. Imagine we have `variable A : Type` and `variable add : A -> A -> A` and a hypothesis that `A` is associative. Then given some term of type `A`, of the form `(a + (b + c)) + d` or whatever, one could ask for a method of moving all the parentheses to the left (with perhaps an added theorem that the original term equals the "normalised" term). But you cannot write Lean code to do this! Lean interprets `(a + (b + c)) + d` as just some term of type `A`.

To write code which moves brackets around, one has to make a new data structure, in this case a tree type with nodes and leaves (leaves indexed by `nat` say), and a "put into normal form" function `norm` which sends `node (t1 (node t2 t3))`to `node (node t1 t2) t3` and generally sends a tree to its "normal form" with all the brackets on the left. "Reification" is the small amount of meta code which one has to write which looks at the actual expression corresponding to a term of type `A` and turns it into a tree. One also has an `eval` evaluation function sending a tree plus some "association list" (saying which elements of `A` the leaves correspond to) to `A`. One then proves a "correctness theorem" that says that given a tree and a list of `A`'s, the evaluation of `t` and its normalisation are equal.

"Reflection" (or "the two level approach" as Henk used to call it) is exactly this situation, where terms of type A constructed using only `+`, and terms of this abstract tree structure, reflect each other.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 10 2019 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/small%20scale%20reflection/near/154825434):
A really cool reflection would be between `Prop` and `bool`! `bool` is a nice easy type and we can calculate with it. There's a nice function from `bool` to `Prop` sending `b` to `b = tt` (which is an equation, which is great because it means we can rewrite). Unfortunately, writing meta code which interprets an arbitrary `Prop` as a `bool` is asking a bit much.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jan 10 2019 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/small%20scale%20reflection/near/154825975):
We actually have a conversion from Prop to bool for decidable Props


{% endraw %}
