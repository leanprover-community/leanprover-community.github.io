---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/62254atactictoforgetthedefinition.html
---

## [general](index.html)
### [a tactic to forget the definition](62254atactictoforgetthedefinition.html)

#### [Kenny Lau (Nov 07 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20tactic%20to%20forget%20the%20definition/near/147254137):
Can we make a tactic to forget the definition of something in the local context while keeping everything else unchanged?

#### [Kenny Lau (Nov 07 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20tactic%20to%20forget%20the%20definition/near/147254192):
so it would make `h : R := 1+1` into `h : R`

#### [Chris Hughes (Nov 07 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20tactic%20to%20forget%20the%20definition/near/147259811):
Use `generalize` instead of let to define h in the first place. Is this something to do with trying to get `subst ` to work?

#### [Kenny Lau (Nov 07 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20tactic%20to%20forget%20the%20definition/near/147260386):
it isn't

#### [Mario Carneiro (Nov 08 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20tactic%20to%20forget%20the%20definition/near/147266720):
you could `replace h := h` I think

