---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98055lambdatemptation.html
---

## [general](index.html)
### [lambda temptation](98055lambdatemptation.html)

#### [Patrick Massot (Apr 24 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125641452):
Do I get kicked out of this forum by CS people if I use
```lean
notation ` ` binders `↦` F:(scoped f, f) := F
#check (x y) ↦ x + y + 1
```

#### [Patrick Massot (Apr 24 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125641513):
I learned to much about notations on Saturday

#### [Patrick Massot (Apr 24 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125641523):
With great power comes great responsibility

#### [Reid Barton (Apr 25 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125642990):
I like it. Makes things a little friendlier for mathematicians who aren't used to `λx y,`

#### [Simon Hudon (Apr 25 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125646078):
Actually, the CS people had a meeting and your past violations are already sufficient to get you booted out

#### [Simon Hudon (Apr 25 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125646299):
But seriously, I understand it's tempting because it's a more traditional notation but I think it's worth re-examining conventions every now and then. In mathematics, the same idea (bound variables) seems to be reinvented over and over and over. If you look at notations like indexed unions, `argmax` and sums, there are a lot of vary different conventions in application. I think it's worth streamlining those notations and writing conceptually similar things with similar notations.

#### [Mario Carneiro (Apr 25 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125647689):
I'm not sure I'm ready to give up `↦` as an available notation, arrows are hard to come by

#### [Scott Morrison (Apr 25 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125649077):
I actually agree with Simon, that it's not a bad thing to ask mathematicians to get used to using lambdas. Conversely, I would be upset by Mario using `↦ ` for something other than "maps to"! :-)

#### [Mario Carneiro (Apr 25 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125649299):
It's conceivable that something that is morally "maps to" but isn't literally lambda could come up, like ZFC maps to producing a Set

#### [Patrick Massot (Apr 25 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lambda%20temptation/near/125659462):
Actually I think the unicode thin space at the beginning of the notation is worse than the Church sacrilege. But I don't know another way. Maybe I don't know enough about notations in the end.

