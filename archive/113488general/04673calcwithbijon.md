---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04673calcwithbijon.html
---

## Stream: [general](index.html)
### Topic: [calc with bij_on](04673calcwithbijon.html)

---

#### [Reid Barton (Jun 06 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127674091):
Is there a way I could use `calc` to chain together `bij_on_comp`?
`bij_on_comp : bij_on g b c → bij_on f a b → bij_on (g ∘ f) a c`

#### [Reid Barton (Jun 06 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127674456):
wow, it actually works! ``local notation a ` ~~ ` b := bij_on _ a b``, and define a `@[trans]` version of `bij_on_comp` with arguments in the right order

#### [Kevin Buzzard (Jun 06 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127676519):
Yeah we took apart calc recently and found out that it was just reading from left to right and attempting to prove a R b S c -> a T c by using results tagged with @trans

#### [Kevin Buzzard (Jun 06 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127676710):
https://github.com/kbuzzard/mathlib/blob/master/docs/extras/calc.md

#### [Kevin Buzzard (Jun 06 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127676713):
Calc is great.

#### [Reid Barton (Jun 06 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127676725):
I wasn't sure whether it would also be able to handle the accumulation going on in the first parameter of `bij_on`

#### [Reid Barton (Jun 06 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127676729):
but apparently it doesn't care

#### [Kevin Buzzard (Jun 06 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127676731):
Oh I see

#### [Kevin Buzzard (Jun 06 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127676784):
You should add a comment to the docs :-)

#### [Kevin Buzzard (Jun 06 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20with%20bij_on/near/127676823):
I guess the elaborator just does its best. This software is so cool

