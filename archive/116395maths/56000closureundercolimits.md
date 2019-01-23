---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/56000closureundercolimits.html
---

## Stream: [maths](index.html)
### Topic: [closure under colimits](56000closureundercolimits.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 08 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/closure%20under%20colimits/near/151163961):
Suppose C is a `category.{u v}` that `has_colimits` and I have a family A_i of objects of C indexed by a `Type v`. I also have (let's say for simplicity) a fixed J which is a `small_category.{v}`. I want to construct the closure of the objects A_i under colimits of shape J, as a new family also indexed on a `Type v`. Is it possible?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 08 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/closure%20under%20colimits/near/151164115):
I was going to use an inductive type of course, but in order to write down the data needed in the inductive constructor, I also need to know what the actual objects in C are (that is, the values of the indexed family), because a diagram involves morphisms in C between those objects. So I end up with an inductive-recursive definition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 08 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/closure%20under%20colimits/near/151164176):
I thought about adding the value of the object as an index of the type, but then it won't live in the right universe.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 08 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/closure%20under%20colimits/near/151164310):
The only thing I can think of is to do some manual transfinite recursion up to an ordinal of large enough cofinality (I know... that's my solution to everything).


{% endraw %}
