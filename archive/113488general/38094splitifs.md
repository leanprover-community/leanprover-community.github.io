---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/38094splitifs.html
---

## [general](index.html)
### [split_ifs](38094splitifs.html)

#### [Scott Morrison (Jun 04 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/split_ifs/near/127536409):
@**Gabriel Ebner**, could we have `split_ifs` fail if there are no ifs to split? It's a trivial change, as in https://github.com/leanprover/mathlib/compare/master...semorrison:split_ifs?expand=1.

#### [Gabriel Ebner (Jun 04 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/split_ifs/near/127536623):
In general I don't have a preference, as long as it is consistent.  So if we're changing all tactics to fail if they would do nothing, then that's ok.
But this change will make `split_ifs` always fail, since it recursively calls itself.

#### [Scott Morrison (Jun 04 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/split_ifs/near/127536647):
ugh, sorry. :-) I will actually test my next fix!

#### [Scott Morrison (Jun 04 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/split_ifs/near/127536703):
At the moment it is really inconsistent. Last year sometime we convinced Leo that `simp` and `dsimp` should fail if they made no progress, and I would love to have everything else gradually switch to this convention.

#### [Scott Morrison (Jun 04 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/split_ifs/near/127536958):
Okay, this one should actually work: https://github.com/leanprover/mathlib/compare/master...semorrison:split_ifs?expand=1

#### [Scott Morrison (Jun 04 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/split_ifs/near/127537017):
So far I am just sending PRs for tactics where I run into an inconvenience because they fail silently, and I have to test myself whether they worked. If it would be helpful, I could try to check that all the tactics in mathlib behave this way.

#### [Gabriel Ebner (Jun 04 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/split_ifs/near/127537138):
Looks good to me if mathlib still builds.

