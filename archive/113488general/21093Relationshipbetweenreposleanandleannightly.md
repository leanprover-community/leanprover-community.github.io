---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21093Relationshipbetweenreposleanandleannightly.html
---

## [general](index.html)
### [Relationship between repos lean and lean-nightly](21093Relationshipbetweenreposleanandleannightly.html)

#### [Ching-Tsun Chou (Mar 11 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Relationship between repos lean and lean-nightly/near/123582525):
I am confused about the relationship between the following two repos:

https://github.com/leanprover/lean

https://github.com/leanprover/lean-nightly

I thought the latter contains snapshots of the former which also appear as nightly builds.  But the latest nightly in:

https://github.com/leanprover/lean-nightly/releases
commit: 5f38fd46d102e81ea798b97d18825ca583150aca

does not appear to exist in the lean repo.  Was my understanding wrong?

Thanks!

#### [Simon Hudon (Mar 11 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Relationship between repos lean and lean-nightly/near/123582599):
I believe that hash is a commit to the `lean-nightly` project which is not a fork of `lean` it is used more like some server space. When travis is done building `lean`, it pushes a release `lean-nightly` which is not a commit in `lean-nightly`

#### [Sebastian Ullrich (Mar 11 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Relationship between repos lean and lean-nightly/near/123583589):
These are still test releases. I will remove them once the change is live.

#### [Ching-Tsun Chou (Mar 11 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Relationship between repos lean and lean-nightly/near/123583642):
What about the nightlies here?

https://leanprover.github.io/download/

How are they related to the ones in lean-nightly?

Thanks!

#### [Sebastian Ullrich (Mar 11 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Relationship between repos lean and lean-nightly/near/123584437):
The download page will link to the releases page when the change is done

