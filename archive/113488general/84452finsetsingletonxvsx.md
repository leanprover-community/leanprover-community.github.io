---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/84452finsetsingletonxvsx.html
---

## [general](index.html)
### ["finset.singleton x" vs "{x}"](84452finsetsingletonxvsx.html)

#### [Kenny Lau (Sep 28 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/"finset.singleton x" vs "{x}"/near/134833971):
there are two ways to write the same finset. there's a simp lemma converting the latter to the former. however there are also many lemmas written using the latter instead of the former. so what is the standard?

#### [Kenny Lau (Sep 28 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/"finset.singleton x" vs "{x}"/near/134834042):
I don't even know if it's a good idea to inherit the multiset singleton as `finset.singleton` to begin with. That means I don't see why there needs to be two traditions at all and we should just stick to {x}

#### [Kenny Lau (Sep 28 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/"finset.singleton x" vs "{x}"/near/134834160):
also when there are two things that represent the same thing, don't we usually write two lemmas each time?

#### [Mario Carneiro (Sep 28 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/"finset.singleton x" vs "{x}"/near/134838973):
finset.singleton doesn't require decidable_eq

#### [Chris Hughes (Sep 28 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/"finset.singleton x" vs "{x}"/near/134839003):
Is that the only reason?

#### [Mario Carneiro (Sep 28 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/"finset.singleton x" vs "{x}"/near/134839093):
I think so... unfortunately root.singleton is a definition rather than a typeclass

#### [Mario Carneiro (Sep 28 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/"finset.singleton x" vs "{x}"/near/134839212):
it is also marginally faster to execute

