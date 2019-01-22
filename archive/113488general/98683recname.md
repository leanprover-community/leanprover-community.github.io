---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98683recname.html
---

## [general](index.html)
### [rec_name](98683recname.html)

#### [Jakob von Raumer (Mar 19 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_name/near/123916531):
After adding an inductive type to the environment using `add_inductive`, I can use the `induction` tactic, but it doesn't return any useful case names... Can I solve this by defining `rec_name`?

#### [Sebastian Ullrich (Mar 19 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_name/near/123916665):
Sounds like it: https://github.com/leanprover/lean/blob/master/library/init/meta/tactic.lean#L425-L426

#### [Sebastian Ullrich (Mar 19 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_name/near/123916666):
Good to know that `induction` works at all

#### [Jakob von Raumer (Mar 19 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_name/near/123917223):
Yes, that's indeed a good thing. I don't even have to add the `using` clause...

#### [Sebastian Ullrich (Mar 19 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_name/near/123917266):
Apparently you do, if you want nice case names :)

#### [Sebastian Ullrich (Mar 19 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_name/near/123917320):
The alternative is to set the case names on your own, using a wrapper around the `induction` tactic

#### [Jakob von Raumer (Mar 19 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rec_name/near/123917471):
I don't _really_ need the case names so far, but I'm kind of feeling that I don't have enough control over which case belongs to which constructor while the tactic is working on it...

