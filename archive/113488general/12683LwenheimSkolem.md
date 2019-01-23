---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/12683LwenheimSkolem.html
---

## Stream: [general](index.html)
### Topic: [Löwenheim-Skolem](12683LwenheimSkolem.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 09 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135492014):
Is Löwenheim-Skolem true in Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135492142):
isn't that 2 theorems?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135492171):
wait this is a theorem about model theory, right? Is model theory in Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135492186):
Can you formalise your question?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 09 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135492286):
Is there a countable model of ZFC in Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 10 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135553994):
This should be true. It shouldn't matter that the metatheory is type theory instead of set theory to prove Löwenheim-Skolem. 
There are students at the university of Pittsburgh who want to formalize forcing in Lean, and want to prove Löwenheim-Skolem along the way: https://github.com/flypitch/flypitch.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 11 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135583543):
oh, this is neat! I wanted to formalize independence of CH too at one point, so I'll definitely check this out

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135593457):
well there are a lot more sentences in Lean than in classical mathematical logic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 11 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135615282):
```quote
well there are a lot more sentences in Lean than in classical mathematical logic
```
Oh, you meant is Lowenheim-Skolem true for Lean as *object language*.
I thought you were talking about having Lean as meta language, and a regular first-order theory as object language. I have never heard of Lowenheim-Skolem for higher-order logics, but it is probably false for those, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 11 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135616391):
Kenny still has not formalised what he means, so we can but conjecture.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135616522):
that means we can define `r : nat -> nat -> Prop` such that the axioms of ZFC (interpreted using Lean) are satisifed with interpreting the membership symbol as `r`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 11 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135616749):
You want it computable? ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 11 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135616786):
there's no computable model of ZFC

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 11 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135616815):
So you're worried about that the "axiom schemes"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 11 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135616833):
You should ask Lotte or David Evans. They are actually real life model theorists who are easily accessible to you.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 11 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135616896):
Maybe Mario or Gabriel or one of the other experts that hang around here will just come and tell us the answer though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jeremy Avigad (Oct 11 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/L%C3%B6wenheim-Skolem/near/135617765):
For higher-order logic with standard semantics, of course, Löwenheim-Skolem is false; we can write down categorical axiomatizations of the reals. 
If you think of higher-order logic in a first-order way -- i.e. a model of higher-order logic is just a many-sorted theory (so each type is a sort) with operations for application and lambda abstraction satisfying the requisite comprehension axioms, Löwenheim-Skolem is true. These are sometimes called "Henkin models". I am sure all this will carry over to dependent type theory. The hard part is saying what a model is. But e.g. the usual term model is a countable model.


{% endraw %}
