---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/70528introducingvariables.html
---

## Stream: [new members](index.html)
### Topic: [introducing variables](70528introducingvariables.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Jul 19 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/129956826):
If I have a Prop that says `∃ a b c, p`, whats the quickest way of introducing a b c and p? In tactic mode, I have to use `cases` three times to obtain all of them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/129957010):
mathlib has `rcases` for this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/129957025):
`rcases h with ⟨a, b, c, hp⟩`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/129957121):
there is also `rintro` for introducing and casing at the same time, `rintro ⟨a, b, c, hp⟩` takes a goal of the form `(∃ a b c, p) -> q` and splits off the parts and has `q` as subgoal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Jul 19 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/129957266):
Is there a similar thing for term mode?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/129957292):
`let ⟨a, b, c, hp⟩ := h in ...` is the equivalent of `rcases` and `λ ⟨a, b, c, hp⟩,` is the equivalent of `rintro`. Neither of those require mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Jul 21 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130049223):
I have `def col (a b c : point) : Prop := B a b c ∨ B b c a ∨ B c a b`. I want to prove `col a b c ∧ (some other stuff) → col a' b' c'`. Depending on the cases of `col a b c`, all the proofs are the same. So can I name `{a, b, c} = {x, y, z}` such that `B x y z` is true. So that when I prove `B x' y' z'`,  I will have proven `col a' b' c'`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130049272):
what is the relation between `x',y',z'` and `a',b',c'`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130049324):
One option is to prove as a lemma/`have` something like `\forall x y z, B x y z ∧ (some other stuff) → B x' y' z'` (where presumably `x'` is a function of `x` or something), and then instantiate it three times for the final proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Jul 21 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130049325):
I can prove `B a b c → B a' b' c'` for any order of a,b and c. So if `x  = a`, `x' = a'`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Jul 21 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130049374):
Ah, and then when I do cases, I can just use `lemma _ _ _` and let lean guess the order.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130049381):
Depending on how often you need this, it might even be worth making a lemma to abstract this proof pattern

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130049389):
By the way, from your two questions I have a pretty good idea what you are working on ;)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 21 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130050497):
@**Ali Sever** Are you aware of http://geocoq.github.io/GeoCoq/?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130050501):
wow that's a nice project page

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 21 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130050605):
Yes, mathlib could use a webdesigner

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Jul 21 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130050654):
Yes, I looked around and I found out they were using the same book I was. I don't know exactly how Coq works, but when I get better at lean, I hope to write some interesting tactics.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 21 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/introducing%20variables/near/130050695):
But the message for Ali was rather more: beware that formalizing elementary geometry can be a lifetime project, especially because of the kind of symmetry issues that appeared in your question. See in particular https://hal.inria.fr/hal-00989781v2

