---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64142aorborcord.html
---

## [general](index.html)
### [a or b or c or d](64142aorborcord.html)

#### [Chris Hughes (Aug 04 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130900638):
If I have `a or b or c or d`, can I split into four goals in one go?

#### [Kenny Lau (Aug 04 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130900640):
`rcases [identifier] with H | H | H | H`

#### [Kenny Lau (Aug 04 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130900647):
I can't interpret "split into four goals". If it's a hypothesis then you get four hypotheses. If it's a goal then you get one goal.

#### [Simon Hudon (Aug 04 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130900700):
Alternatively, `casesm* [_ ∨ _]` also helps.

#### [Chris Hughes (Aug 04 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130900707):
Thanks

#### [Mario Carneiro (Aug 04 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130900812):
there is no brackets in `rcases`

#### [Kenny Lau (Aug 04 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130900816):
`[identifier]` is a placeholder

#### [Mario Carneiro (Aug 04 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130900836):
hm, it's hard to tell the difference between meta notation and lean notation... we need more brackets
```
rcases ⟅identifier⟆ with H | H | H | H
```

#### [Ali Sever (Aug 05 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130906775):
On a similar note, if you want to prove `∃ a b c,  ...` is there a way to do something like `existsi a b c`? I tried`repeat {constructor}` for fun, and I was surprised to see lean perfectly guess what a, b and c were.

#### [Ali Sever (Aug 05 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130906828):
Also, when I used `constructor,` three times, lean did not guess them.

#### [Simon Hudon (Aug 05 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130906831):
you could also do `existsi [a,b,c]` if you want to specify the witnesses yourself.

#### [Ali Sever (Aug 05 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130907028):
Ah thank you, I had not tried those brackets. Is there a rule to know which type is used where?

#### [Simon Hudon (Aug 05 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130907038):
Which types do you mean?

#### [Kevin Buzzard (Aug 05 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130907080):
which type of bracket?

#### [Kevin Buzzard (Aug 05 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130907085):
I guess you can look at the documentation for the tactic...

#### [Kevin Buzzard (Aug 05 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130907087):
(by hovering over it)

#### [Nicholas Scheel (Aug 05 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130907138):
brackets are syntax, so I don‘t think they can have _types_, nor kinds, nor sorts ... must be varieties, I guess? ;)

#### [Nicholas Scheel (Aug 05 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a or b or c or d/near/130907192):
we’re going to run out of variants of words soon to describe these things

