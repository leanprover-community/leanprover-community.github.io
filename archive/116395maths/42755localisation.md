---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/42755localisation.html
---

## Stream: [maths](index.html)
### Topic: [localisation](42755localisation.html)

---

#### [Johan Commelin (Nov 23 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/localisation/near/148248534):
@**Kenny Lau** Did you have a proof somewhere that if you localise a ring at `S`, then `S` maps to `units` of the localisation?

#### [Johan Commelin (Nov 23 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/localisation/near/148248540):
Or something similar to that?

#### [Kenny Lau (Nov 23 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/localisation/near/148248548):
yes...

#### [Johan Commelin (Nov 23 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/localisation/near/148248579):
I don't think that is in mathlib.

#### [Kenny Lau (Nov 23 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/localisation/near/148248583):
it's in limbo...

#### [Johan Commelin (Nov 23 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/localisation/near/148248588):
/me searches for https://github.com/kckennylau/limbo

#### [Kenny Lau (Nov 23 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/localisation/near/148248601):
https://github.com/leanprover/mathlib/pull/481/files#diff-8b1b305bf224a13c5239cddad4405491R131

#### [Kevin Buzzard (Nov 23 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/localisation/near/148248663):
```quote
it's in limbo...
```
 Just to comment that the `@kbuzzard` in that PR had no visible effect (in the sense that I didn't notice anything). I've only just seen this PR now.

#### [Johan Commelin (Nov 23 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/localisation/near/148248724):
Shouldn't that give you something in your GitHub notification area (or send you an email)?

#### [Kevin Buzzard (Nov 23 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/localisation/near/148248726):
Yeah but now I switched GH notifications on I always have 100 notifications.

#### [Kevin Buzzard (Nov 23 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/localisation/near/148248727):
So now I just don't read them.

#### [Johan Commelin (Nov 23 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/localisation/near/148248852):
Hmmm, maybe you should be more careful in which repositories you watch...

#### [Johan Commelin (Nov 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/localisation/near/148248895):
Anyway, @**Kenny Lau** it's cool that this is coming to mathlib in some near future

#### [Kenny Lau (Nov 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/localisation/near/148248897):
...right

#### [Patrick Massot (Nov 23 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/localisation/near/148249206):
:open_mouth: I also missed that PR!

#### [Patrick Massot (Nov 23 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/localisation/near/148249209):
I vote for reviewing that PR! And also the #where PR

