---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09684Orsaymeetingreport.html
---

## [general](index.html)
### [Orsay meeting report](09684Orsaymeetingreport.html)

#### [Patrick Massot (Aug 30 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Orsay meeting report/near/133061127):
We had a Lean user meeting in Laboratoire de Mathématiques d'Orsay on August 27-29th. Participants were 
Chris Hugues, Johan Commelin, Johannes Hölzl, Kevin Buzzard, Mario Carneiro, Patrick Massot, Reid Barton, Rob Lewis, and Scott Morrison. 

Johannes and Mario lectured on meta-programming in Lean, Rob showed his Lean-Mathematica bridge and his new linear arithmetic tactic, Scott showed his tidy tactic. We discussed many ongoing projects and open mathlib pull-requests. During those three days, 22 pull requests were merged, and 17 were opened (not counting PR unrelated to the meeting), 24 commits went into mathlib, adding about 2000 lines and removing 500. The topics of these commits include tactics (tidy, linear arithmetic, fix a little quirk in solve_by_elim), a little bit of documentation, category theory, arithmetic in rings, additional lemmas for filters, topological and uniform spaces in preparation for completions of topological rings, normed spaces and bounded linear maps (see https://github.com/leanprover/mathlib/pulse). We also worked towards splitting fields, noetherian modules,and sheaves, writing code that should land in mathlib very soon. We also talked about future project, writing a list of [potential project](https://github.com/leanprover-community/mathlib/wiki/Potential-projects) for formalization and a wish list of [VScode goodies](https://github.com/leanprover-community/mathlib/wiki/VScode-goodies). There is general agreement that meeting each other was nice, helped in merging work, and will be very useful to ease future collaboration.

#### [Johan Commelin (Aug 30 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Orsay meeting report/near/133061914):
A very nice summary!

#### [Reid Barton (Aug 30 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Orsay meeting report/near/133073012):
And now I'm reading everyone's messages in their own voices (including Kenny)

#### [Chris Hughes (Aug 30 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Orsay meeting report/near/133073724):
(deleted)

#### [Patrick Massot (Aug 30 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Orsay meeting report/near/133074254):
Yes! That's really nice

#### [Jeremy Avigad (Sep 02 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Orsay meeting report/near/133224728):
Wow, that is really impressive! It is great that you were able to sustain that level of productivity.

#### [Patrick Massot (Sep 02 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Orsay meeting report/near/133226474):
Yes, it worked really well. But of course it's difficult to precisely assess what happened. I took time to compute those numbers in case someone asks me what I did with the money, but they shouldn't be taken too seriously. These merges were possible because of earlier work that was not yet merged. On the other hand, those numbers also don't include things that began in Orsay but were merged later or are not yet merged (like the noetherian module stuff which is still in https://github.com/leanprover-community/mathlib/tree/noetherian). And more generally we clearly have a boost of productivity since the meeting, using the momentum acquired there. This boost will necessarily fade off at some point, but then I hope we will still have the diffuse motivation and communication benefits coming from knowing each others.

