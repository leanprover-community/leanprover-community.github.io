---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/34322Whydoesmygoalchange.html
---

## [new members](index.html)
### [Why does my goal change?](34322Whydoesmygoalchange.html)

#### [Ali Sever (Aug 04 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20does%20my%20goal%20change%3F/near/130885232):
After using `constructor` my goal was `?m_1 ∉ A`. Then I used `cases h with p hp`, and my goal became `?m_1[_] ∉ A`. What does that mean, and why does it even happen?

#### [Kenny Lau (Aug 04 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20does%20my%20goal%20change%3F/near/130885281):
MWE

#### [Mario Carneiro (Aug 04 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20does%20my%20goal%20change%3F/near/130886032):
That is a representation of a delayed abstraction. It means that the metavariable `?m_1` has been partially instantiated, although it still hasn't figured out what it should be yet

#### [Kevin Buzzard (Aug 04 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20does%20my%20goal%20change%3F/near/130888106):
Ali I think it's an unwise idea in general to have metavariables in your goals. Presumably you have more than one goal at this point, and another goal is probably asking you what the metavariable is. You might want to fill in some earlier hole.

