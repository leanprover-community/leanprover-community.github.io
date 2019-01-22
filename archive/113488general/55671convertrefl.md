---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55671convertrefl.html
---

## [general](index.html)
### [convert, refl](55671convertrefl.html)

#### [Reid Barton (Nov 27 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert%2C%20refl/near/148646168):
This is a new one for me--`convert` left a goal which I could close with `refl`

#### [Patrick Massot (Nov 27 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert%2C%20refl/near/148646555):
You can easily play with `convert` and, especially `congr'` code, they are easy to understand, as long as you don't try to understand what `congr_core` is doing, which I suspect you won't need to try

#### [Reid Barton (Nov 27 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert%2C%20refl/near/148646599):
Maybe `refl` closed some later goal, fixing a metavariable, and that caused an earlier goal to also be closable by `refl`

#### [Reid Barton (Nov 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert%2C%20refl/near/148646658):
I do have a `_` in the argument to `convert`

