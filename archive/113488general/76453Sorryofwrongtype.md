---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/76453Sorryofwrongtype.html
---

## Stream: [general](index.html)
### Topic: [Sorry of wrong type!](76453Sorryofwrongtype.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 21 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004577):
Heh...
```lean
type mismatch at field 'le_refl'
  sorry
has type
  ∀ (a : α), ?m_1 a a
but is expected to have type
  ∀ (a : α), a ≤ a
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 21 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004587):
did you put `sorry` for the definition of `le` as well?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004627):
`le := _, le_refl := sorry` will error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004630):
Yes :). I just sorried everything to build it incrementally, I know I don' goof'd, it's just amusing that sorry can actually fail to typecheck.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004634):
Indeed! :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 21 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004641):
It's the first time I've seen `sorry` being red-squiggled in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 21 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004706):
I think it is having difficulty unifying the types, this would happen also if you tried to use something of type `\forall {x : Type*}. x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 21 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004853):
So I guess  sorry first needs to know the type and then gives you a bogus term thereof, rather than just "closing the goal" as if by magic? Would the latter behaviour lead to weirdness in scenarios where something depends on a (presumably temporary) sorry?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 21 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004895):
I think the problem has to do with unresolved metavariables in the type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 21 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124004947):
You should always be able to sorry everything, but you have to work from the beginning, from the nondependent `sorry`s to the dependent ones

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 21 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124005016):
Right. It's just interesting that sorry cares about anything at all :)! So for example, `{ le := sorry, le_refl := sorry ... }` would work but `{ le := _, le_refl := sorry ... }` would not.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 21 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124005487):
I got sorry red-squiggled about 2 weeks ago, for probably the first time. I awarded myself an achievement.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 21 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124005556):
It's like the dual problem of proving an inconsistency :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 21 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sorry%20of%20wrong%20type%21/near/124006030):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/too.20many.20axioms.20in.20comm_ring.20class/near/123391025


{% endraw %}
