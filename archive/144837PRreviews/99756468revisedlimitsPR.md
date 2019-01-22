---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/99756468revisedlimitsPR.html
---

## [PR reviews](index.html)
### [#468 revised limits PR](99756468revisedlimitsPR.html)

#### [Scott Morrison (Nov 09 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#468 revised limits PR/near/147348952):
Is this the biggest PR so far? Adds +3,634 lines.

#### [Scott Morrison (Nov 09 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#468 revised limits PR/near/147349003):
Of course, because writing an all-singing all-dancing `dualize` tactic still feels hard, you get to divide that number by exactly two, since everything gets said exactly twice ...

#### [Kenny Lau (Nov 09 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#468 revised limits PR/near/147357101):
Is `dualize` harder than `to_additive`?

#### [Scott Morrison (Nov 10 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#468 revised limits PR/near/147411779):
Yes. At the very least, there needs to be a mechanism to tell it which category needs to be "opposited" --- lots of the theorems we have in the limits PR talk about several categories at once, and it's the categories we take limits in that need to be switched, while the diagram categories don't.

#### [Scott Morrison (Nov 10 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#468 revised limits PR/near/147411782):
If someone wants to prove me wrong, and start writing a `dualize` tactic, that would be awesome. :-)

#### [Scott Morrison (Nov 15 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#468 revised limits PR/near/147769590):
I've just removed `examples/CommRing/equalizers.lean`, that still deserved more work, and so the `limits` branch is ready for further review and/or merging.

