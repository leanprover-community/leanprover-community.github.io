---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/75628importrenaming.html
---

## Stream: [general](index.html)
### Topic: [import renaming?](75628importrenaming.html)

---

#### [Scott Morrison (Aug 09 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20renaming%3F/near/131161156):
can someone point me to the syntax for import renaming? I can't find it. :-(

#### [Mario Carneiro (Aug 09 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20renaming%3F/near/131161170):
I don't think there is such a thing

#### [Mario Carneiro (Aug 09 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20renaming%3F/near/131161216):
I think it was proposed for lean 4, but AFAIK it can't be done in lean 3

#### [Patrick Massot (Aug 09 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20renaming%3F/near/131161219):
People often talk about it here, but only to wish it exists

#### [Scott Morrison (Aug 09 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20renaming%3F/near/131161224):
oh, wow, maybe I dreamt it. I have a really strong memory of yesterday learning that you could hide and rename individual declarations when you made an import!

#### [Mario Carneiro (Aug 09 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20renaming%3F/near/131161259):
There is `open` and `hide`, which have a syntax for opening individual declarations and renaming

#### [Johan Commelin (Aug 09 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20renaming%3F/near/131161343):
I don't think you learnt that here...

#### [Sebastian Ullrich (Aug 09 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20renaming%3F/near/131184956):
Declarations in a Lean environment aren't grouped by modules, so I don't see how this would be implemented without fundamentally changing the architecture. Which we don't plan to do, afaik.

