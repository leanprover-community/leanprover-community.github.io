---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66487TypevsType.html
---

## [general](index.html)
### [Type* vs Type _](66487TypevsType.html)

#### [Patrick Massot (Apr 26 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type* vs Type _/near/125719177):
What's the difference between `(a: Type*)` and `(a: Type _)`?

#### [Gabriel Ebner (Apr 26 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type* vs Type _/near/125719646):
They both mean the same as `(a: Sort (_+1))` and `(a: Type.{_})`.

#### [Patrick Massot (Apr 26 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type* vs Type _/near/125719765):
So, we have lots of ways to confuse new users...

#### [Kevin Buzzard (Apr 26 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type* vs Type _/near/125732578):
On the other hand I ran into an example recently where just calling things "Type u", "Type v", "Type w"... seemed to have a different effect to calling them all "Type *". I hope I starred that post because I thought it was worth following up and I didn't do it at the time...

#### [Kevin Buzzard (Apr 26 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type* vs Type _/near/125732658):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe.20issues

#### [Kevin Buzzard (Apr 26 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type* vs Type _/near/125732669):
Me being burned by `Type *`

#### [Patrick Massot (Apr 26 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type* vs Type _/near/125732683):
I can tell you another example: the group instance on `perm X`

#### [Patrick Massot (Apr 26 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type* vs Type _/near/125732729):
But this is orthogonal to my question

#### [Sean Leather (Apr 27 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type* vs Type _/near/125780058):
```quote
But this is orthogonal to my question
```
I would say it's more of a footnote (`*`) to your question.

