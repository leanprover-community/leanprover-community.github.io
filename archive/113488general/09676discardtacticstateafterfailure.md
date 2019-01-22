---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09676discardtacticstateafterfailure.html
---

## [general](index.html)
### [discard tactic_state after failure?](09676discardtacticstateafterfailure.html)

#### [Scott Morrison (Oct 03 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/discard%20tactic_state%20after%20failure%3F/near/135090187):
Is there an existing tactic that runs a tactic, then restores the original tactic_state if it fails?

#### [Patrick Massot (Oct 03 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/discard%20tactic_state%20after%20failure%3F/near/135090200):
try?

#### [Scott Morrison (Oct 03 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/discard%20tactic_state%20after%20failure%3F/near/135090235):
(I've run into a problem where failed tactics are having unwanted side effects, e.g. unifying metavariables.)

#### [Simon Hudon (Oct 03 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/discard%20tactic_state%20after%20failure%3F/near/135091267):
So you write `try tac`, `tac` unifies variables and then fails and the unification persists?

#### [Mario Carneiro (Oct 03 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/discard%20tactic_state%20after%20failure%3F/near/135091455):
`try` definitely restores the original tactic state after failure, so it's possible you've stumbled upon one of lean's less functional sides

#### [Scott Morrison (Oct 03 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/discard%20tactic_state%20after%20failure%3F/near/135091563):
Hmm, it seems I was wrong, as sticking such a tactic into the place I thought would fix things, hasn't fixed things. Maybe more later, sorry for the noise!

