---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/50743autoparamininstance.html
---

## [general](index.html)
### [autoparam in instance](50743autoparamininstance.html)

#### [Patrick Massot (Dec 18 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam in instance/near/152102423):
Is it possible to use autoparam in instances? I have a `is_add_group_hom` instance that never triggers, probably because is it contains a continuity assumption. The following doesn't seem to help:
```lean
instance sep_quot.is_add_group_hom_lift [separated β]  (hf : continuous f . tactic.assumption) : is_add_group_hom (sep_quot.lift f) := ...
```

#### [Johan Commelin (Dec 18 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam in instance/near/152102640):
Isn't this evidence that `continuous` should be a class?

#### [Patrick Massot (Dec 18 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam in instance/near/152102647):
Of course this also came to my mind

#### [Patrick Massot (Dec 18 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam in instance/near/152102650):
Here it would clearly help

#### [Johan Commelin (Dec 18 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam in instance/near/152102776):
/me doesn't know why group homs should be a class and continuous maps not...

#### [Gabriel Ebner (Dec 18 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam in instance/near/152102875):
```quote
Is it possible to use autoparam in instances?
```
 No, auto_params are handled by the elaborator.  Type class instance synthesis does not know about auto_param (or optional parameters).

#### [Patrick Massot (Dec 18 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam in instance/near/152102895):
Thanks Gabriel

#### [Kenny Lau (Dec 18 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam in instance/near/152104969):
neither should be a class

#### [Kenny Lau (Dec 18 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam in instance/near/152104973):
not group homs. not continuous maps. not linear maps.

#### [Johan Commelin (Dec 18 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam in instance/near/152105038):
So... what *should* be a class?

#### [Kenny Lau (Dec 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam in instance/near/152105320):
groups and topological spaces and modules?

#### [Johan Commelin (Dec 18 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam in instance/near/152105378):
Why???

#### [Kenny Lau (Dec 18 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam in instance/near/152105431):
how is it done in your category theory?

#### [Kevin Buzzard (Dec 18 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam in instance/near/152106769):
Continuous maps not a class -- Johannes has explained this before on this forum, although I have never really internalised the issue.

