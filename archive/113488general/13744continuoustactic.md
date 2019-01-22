---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/13744continuoustactic.html
---

## [general](index.html)
### [continuous tactic](13744continuoustactic.html)

#### [Kenny Lau (Nov 01 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/continuous tactic/near/136888333):
Can we have a tactic that solves continuity goals, matching e.g. `continuous (f o g)` and splitting it into two goals?

#### [Kevin Buzzard (Nov 01 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/continuous tactic/near/136888372):
``meta def continuity_goals := `[apply continuous.comp]`` or something?

#### [Reid Barton (Nov 01 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/continuous tactic/near/136891384):
I have this but it is based on `backwards_reasoning` and it seemed better to wait for that to land in mathlib first.

#### [Kenny Lau (Nov 01 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/continuous tactic/near/136891435):
nice

#### [Scott Morrison (Nov 01 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/continuous tactic/near/136903346):
Sorry, I haven’t given the backwards reasoning PR much attention recently. I’ll try to get back to it!

