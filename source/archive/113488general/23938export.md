---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23938export.html
---

## [general](index.html)
### [export?](23938export.html)

#### [Kevin Buzzard (Jun 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995777):
From lean core:

#### [Kevin Buzzard (Jun 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995779):
```lean
class has_pow (α : Type u) (β : Type v) :=
(pow : α → β → α)

export has_andthen (andthen)
export has_pow (pow)
```

#### [Kevin Buzzard (Jun 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995786):
What does `export` do? The line reminds me of those old batman TV shows.

#### [Kenny Lau (Jun 13 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995829):
like `open`

#### [Kevin Buzzard (Jun 13 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995833):
oh I just remembered `#help`

#### [Kevin Buzzard (Jun 13 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995835):
`export: create aliases for declarations`

#### [Kevin Buzzard (Jun 13 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995846):
At the end of the day, does this just mean that `pow` can be used instead of `has_pow.pow`?

#### [Kevin Buzzard (Jun 13 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995886):
Aah -- does it mean that this is true globally?

#### [Kevin Buzzard (Jun 13 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995890):
I see -- `#check pow` seems to work fine in a new file

#### [Kevin Buzzard (Jun 13 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995894):
so it's open on steroids

#### [Kevin Buzzard (Jun 13 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995899):
"open and never close"?

#### [Johan Commelin (Jun 13 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995954):
No, I guess that is an artifact of the fact that it is in core.

#### [Johan Commelin (Jun 13 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995963):
Hmm, no... that is not what I meant.

#### [Sebastian Ullrich (Jun 13 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127995966):
> "open and never close"?

Yes, basically. You can locally "close" it with `hide`.

#### [Kevin Buzzard (Jun 13 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127996018):
Thanks Sebastian.

#### [Kevin Buzzard (Jun 13 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127996073):
The reason I asked was that I noticed that if I import `tactic.ring` then I can do `a ^ 2` for a in a `comm_ring`, but I can't do this otherwise. I was just trying to figure out where that instance was defined, but I don't know how to do this, short of looking at what `tactic.ring` imports and importing all of those things instead, until I finally find the import which actually makes it work.

#### [Kevin Buzzard (Jun 13 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127996075):
That's one approach -- and searching for has_pow.pow is another, but actually I should just search for `pow` perhaps

#### [Kevin Buzzard (Jun 13 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127996085):
Got it -- obviously to get powers in a ring the key import is `group_power.lean` ;-)

#### [Kevin Buzzard (Jun 13 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/export%3F/near/127996088):
[mumble mumble monoid]

