---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52942exactthis.html
---

## [general](index.html)
### [exact this](52942exactthis.html)

#### [Patrick Massot (Jul 26 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130305391):
Today I came across several instance of `have := stuff, exact this` closing a goal where `exact stuff` doesn't. I guess this is yet another elaboration subtlety, but I'd like to know if there is a nicer way to do this in one tactic.

#### [Mario Carneiro (Jul 26 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130314992):
I use Chris's trick: `exact (stuff : _)`

#### [Patrick Massot (Jul 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130327840):
Thanks!

#### [Patrick Massot (Jul 26 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130353906):
Could we get a mathlib tactic replacing `exact` which tries `exact` and then Chris's trick?

#### [Patrick Massot (Jul 26 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130353926):
@**Sebastian Ullrich** : is this a well known bug or a feature?

#### [Sebastian Ullrich (Jul 26 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130354033):
I'll go with feature

#### [Patrick Massot (Jul 26 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130354040):
Too easy...

#### [Patrick Massot (Jul 26 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130354069):
Seriously, what do I miss to understand this thing?

#### [Sebastian Ullrich (Jul 26 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130354309):
I mean, it's clear that omitting the expected type can lead to different elaboration results in some cases, and in some of these cases, the result without expected type may even be preferable. Whether that is something that could be improved in the elaborator can only be decided on a case by case basis.

#### [Patrick Massot (Jul 26 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130354494):
I sort of understand this. What I don't get is how `(stuff : _)` differs from not specifying the expected type of `stuff`. Here we really mean underscore, this is not an abbreviation for Zulip purposes.

#### [Sebastian Ullrich (Jul 26 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130355110):
Where do you not specify it? If you use `exact stuff`, the expected type is the goal.

#### [Sebastian Ullrich (Jul 26 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130355120):
In both `have := stuff` and `(stuff : _)`, there is no expected type

#### [Patrick Massot (Jul 26 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130355632):
I mean `exact stuff` versus `exact (stuff : _)`, both meant to close the current goal.

#### [Patrick Massot (Jul 26 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130355646):
Sometimes only the later succeeds

#### [Sebastian Ullrich (Jul 26 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130356150):
As I said, only in `exact stuff` do you have an expected type. It's the goal.

#### [Patrick Massot (Jul 26 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130356190):
Sorry I'm slow.

#### [Patrick Massot (Jul 26 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130356242):
But it's really really hot here

#### [Sebastian Ullrich (Jul 26 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130356283):
I'm very grateful to spend the remaining summer in the land of air conditioning :)

#### [Patrick Massot (Jul 26 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130356295):
USA?

#### [Sebastian Ullrich (Jul 26 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130356748):
Yes, I'm doing an internship under Leo until October

#### [Patrick Massot (Jul 26 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exact%20this/near/130356771):
Oooh, that sounds like a very good idea!

