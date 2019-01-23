---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/66292semiringhomomorphisms.html
---

## Stream: [maths](index.html)
### Topic: [semiring homomorphisms](66292semiringhomomorphisms.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 08 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126249853):
There is a class for ring homomorphisms: https://github.com/leanprover/mathlib/blob/7d1ab388bb097db5d631d11892e8f110e1f2e9cd/algebra/ring.lean#L60
But there is no class for semiring homomorphisms. Does it make sense to change broaden this class into semiring homomorphisms?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 08 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126249910):
You need to preserve zero for a semiring homomorphism

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 08 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126249917):
in fact, I guess it's just the same as a monoid homomorphism which is also an additive monoid homo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 08 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250020):
Aah, yes. That is not automatic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 08 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250030):
Ok, so, shall I add a new class for semiring homs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 08 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250073):
if you like

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 08 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250095):
What is a natural place for it? I am a bit surprised that the definition of a semiring is in core...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 08 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250098):
Otherwise it would be natural to add it after the definition of semiring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 08 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250099):
the mathlib file for ring-like stuff is `algebra/ring.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 08 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250139):
Ok, I will find some place in that file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 08 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250142):
semiring is defined in core because nat is a semiring and that defines all the operations on nat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 08 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250145):
I think this will change in lean 4 though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 08 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250197):
Ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 08 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250257):
Aah, and it seems like monoid_homs are also not yet there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 08 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250694):
Does this have anything to do with the "algebraic hierarchy" that I sometimes hear people talking about?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 08 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250713):
At the moment there is a class for homomorphisms between two `group`s but if one (or both) of my groups are additive, there is no class for homomorphisms. Does this mean we need 4 classes to cover all the possibilities?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 08 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250760):
let's just say that is a point of discussion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 08 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250763):
One option is to use `multiplicative` to interpret an additive group as a multiplicative group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 08 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250772):
We have not made any significant effort to have a full complement of morphisms between the various available structures in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 08 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250811):
the ones that exist have basically been added ad-hoc as people needed them, and I'm fine with that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 08 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250812):
Ok, I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 08 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250820):
Am I correct that parametricity could help here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 08 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250859):
Well, `transport_to_additive` can be seen as a special case of parametricity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 08 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/semiring%20homomorphisms/near/126250863):
but there is also a lot of renaming to be done by the tactic


{% endraw %}
