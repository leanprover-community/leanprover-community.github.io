---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/31111Coercingtooption.html
---

## Stream: [new members](index.html)
### Topic: [Coercing to option](31111Coercingtooption.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155204948):
Where can I find lemmas about coercing to option (e.g. `ℕ` to `option ℕ`)? I want basic things like `↑(n - m) = ↑n - ↑m`.

#### [ Mario Carneiro (Jan 15 2019 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155204961):
what does subtraction mean?

#### [ Mario Carneiro (Jan 15 2019 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155204982):
I don't think option has a `has_sub` instance

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205154):
But option N does.

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205221):
Oh wait, you mean `↑n - ↑m` won't be defined at all.

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205251):
What about something like `1 + ↑(n - 1) = ↑n`? That's what I actually need to prove.

#### [ Mario Carneiro (Jan 15 2019 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205270):
option doesn't have an add or 1 either

#### [ Mario Carneiro (Jan 15 2019 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205286):
what are you doing?

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205303):
Degrees of polynomials.

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205315):
You can add degrees of polynomials, but they're defined via option.

#### [ Mario Carneiro (Jan 15 2019 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205329):
Isn't it `with_bot N` or something?

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205336):
Yeah.

#### [ Mario Carneiro (Jan 15 2019 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205346):
that's a different thing

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205412):
Ok, because `with_bot` has additional structure.

#### [ Mario Carneiro (Jan 15 2019 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205415):
`with_bot` has an addition, `option` doesn't

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205416):
But how do I coerce to `with_bot`?

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205423):
I mean, are there lemmas about it in mathlib?

#### [ Mario Carneiro (Jan 15 2019 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205548):
I think you want `with_bot.coe_add`

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205551):
Ah, I see.

#### [ Mario Carneiro (Jan 15 2019 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205560):
the lemmas are in `algebra.ordered_group`

#### [ Mario Carneiro (Jan 15 2019 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205587):
but if `n : nat` then `1 + \u(n - 1) = \u n` is false at 0

#### [ Abhimanyu Pallavi Sudhir (Jan 15 2019 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205616):
Yeah, I have an `n > 1` hypothesis, that's alright.

#### [ Mario Carneiro (Jan 15 2019 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205634):
if you cases on `n` then the zero case is impossible and the succ case is by refl

#### [ Mario Carneiro (Jan 15 2019 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155205704):
oh wait, not refl, you have to commute the 1+ first

#### [ Kevin Buzzard (Jan 15 2019 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coercing%20to%20option/near/155206605):
```quote
that's a different thing
```
 It's a definitionally equal thing. Definitional equality is a subtle beast. At times you should just treat definitionally equal things as the same, but at other times you shouldn't, and this is one of those times. This came up today in my M1P1 talk. We tried `linarith` to finish the proof that any two limits of a sequence were equal, and it failed, because we had hypotheses of the form `l < m -> false`. When we changed them to the definitionally equal `\not (l < m)` linarith suddenly worked! What is going on, I guess, is that linarith is looking at what "kind" of an expression it can see, and `l < m -> false` is "just some function" to linarith, whereas `\not (l < m)` is "a linear inequality that I can use". Similarly type class inference for + is going to trigger on `with_bot nat` but perhaps not on `option nat` even though they're definitionally equal. I hope I've got this mostly right. These things might be definitionally equal, but they are different expressions so tactics or other bits of Lean might treat them in different ways. For unification they will be the same but for rewrites they won't. etc etc.


{% endraw %}
