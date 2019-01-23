---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71528ext1vsext1.html
---

## Stream: [general](index.html)
### Topic: [ext1 vs ext : 1](71528ext1vsext1.html)

---

#### [Patrick Massot (Sep 28 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847162):
Is there any difference between `ext1` and `ext : 1`?

#### [Simon Hudon (Sep 28 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847229):
None

#### [Patrick Massot (Sep 28 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847278):
Do we want to advertise `ext1` then? This is different from asking whether it should exist as an internal  part of `ext`

#### [Patrick Massot (Sep 28 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847351):
Do we have other tactics taking a natural  number parameter introduced by `:`?

#### [Simon Hudon (Sep 28 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847490):
```quote
Do we have other tactics taking a natural  number parameter introduced by `:`?
```
Not that I know of.

#### [Simon Hudon (Sep 28 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847505):
```quote
Do we want to advertise `ext1` then? This is different from asking whether it should exist as an internal  part of `ext`
```
What do you mean by advertise?

#### [Patrick Massot (Sep 28 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847541):
It's an interactive tactic, and it's mentioned in the docs

#### [Patrick Massot (Sep 28 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847587):
I'm a bit worried that we have more and more tactics to learn (thanks!) and redundancy may become a small problem

#### [Simon Hudon (Sep 28 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847624):
So if we were to stop advertising it, we'd take it out of `tactic.interactive` and remove it from the docs? Or maybe just mention it as part of the doc of `ext`?

#### [Simon Hudon (Sep 28 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847664):
I think you're right about redundancy.

#### [Mario Carneiro (Sep 28 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847867):
Is there really no difference? I would have guessed `ext1` forces an application of extensionality

#### [Simon Hudon (Sep 28 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134847959):
Initially that was the difference but @**Scott Morrison|110524** found it more useful if `ext` would fail if it can't apply at least one extentionality lemma

#### [Simon Hudon (Sep 28 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134848009):
With regards to learning tactics, we way want to categorize the ones that we have to make them a bit easier to learn

#### [Scott Morrison (Sep 29 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134858565):
Categorizing them is a good idea. Our approach to documenting new tactics introduced in mathlib so far has been essentially an append-only list of paragraphs describing tactics. :-)

#### [Simon Hudon (Sep 29 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134858690):
It's still better than before @**Patrick Massot** started his crusade: most are now documented :D

#### [Scott Morrison (Sep 29 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ext1%20vs%20ext%20%3A%201/near/134858714):
Absolutely! :-)

