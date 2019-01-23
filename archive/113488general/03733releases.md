---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03733releases.html
---

## Stream: [general](index.html)
### Topic: [releases](03733releases.html)

---

#### [Patrick Massot (Mar 05 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123313063):
Is there anything like a Lean release policy? It seems to me quite a bit happened since Lean 3.3.0 and I don't see any indication that some new release is coming.

#### [Sebastian Ullrich (Mar 06 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123342909):
short answer: no

#### [Patrick Massot (Mar 06 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123344199):
I suspected the short answer. Is there a longer answer?

#### [Sebastian Ullrich (Mar 06 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123344597):
The long answer is that we really haven't given much thought to a release policy yet. There are many refactorings going on right now, so maybe after that would be a good time for a release. Though that may also describe Lean's perpetual state.

#### [Patrick Massot (Mar 06 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123344647):
Do you mean after monad refactoring or after new parser/hygienic stuff?

#### [Mario Carneiro (Mar 06 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123344665):
```quote
Though that may also describe Lean's perpetual state.
```
this

#### [Mario Carneiro (Mar 06 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123344716):
I don't think lean will reach a "stopping point" in my lifetime...

#### [Mario Carneiro (Mar 06 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123344726):
If anything it will probably die someday (hopefully long) in the future in the middle of another refactoring

#### [Patrick Massot (Mar 06 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123344769):
I'm very happy that Lean is always improving. The reason why I ask for releases is because TPIL doesn't update between releases. And I fear that this wonderful resource will become useless (or even confusing hence harmful)

#### [Mario Carneiro (Mar 06 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123345794):
Of course it is not a bad thing that lean is always in an improvement cycle, but I point this out only to stress that there is no point waiting for development to stop or even finish a big project before making a release. I think releases should be done at any point once a decent amount of changes have accrued since the last release. By my estimate we have passed at least 3 minor versions' worth of material since 3.3.0

#### [Sebastian Ullrich (Mar 06 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123347274):
I will ask Leo about a release after the monad/type_context/name refactorings (yeah, I do think right now is a particularly bad time). On the other hand, for TPIL I think it would be great to have some kind of versioned docs a la https://robpol86.github.io/sphinxcontrib-versioning/

#### [Patrick Massot (Mar 06 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123347386):
I already suggested having two branches of TPIL on the relevant github issue board

#### [Sebastian Ullrich (Mar 06 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123347502):
Yes, and that plugin would allow us to show both branch contents on the same page. We should really do that for the reference too.

#### [Patrick Massot (Mar 06 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/releases/near/123350064):
That sounds nice, I'll try to push this idea. You can go back to think about smarter issues :smile:

