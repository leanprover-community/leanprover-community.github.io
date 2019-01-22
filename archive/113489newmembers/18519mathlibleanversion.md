---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/18519mathlibleanversion.html
---

## [new members](index.html)
### [mathlib/lean version](18519mathlibleanversion.html)

#### [Scott Olson (Sep 25 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/mathlib/lean version/near/134602285):
The mathlib instructions at https://github.com/leanprover/mathlib/blob/master/docs/elan.md#scenario-1-start-a-new-package suggest using the version in the mathlib leanpkg.toml, expecting it to be a nightly, but it's actually the stable 3.4.1 now, which means leanpkg downloads the lean-3.4.1 branch instead of master.

What's the right way to use mathlib master?

#### [Scott Olson (Sep 25 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/mathlib/lean version/near/134603971):
For now I've just specified the latest nightly, but I'm not sure if I'm supposed to be tracking along with mathlib as suggested by those docs somehow

#### [Scott Morrison (Sep 25 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/mathlib/lean version/near/134629753):
Ugh, we really need to fix this issue! There was some discussion a few days ago.

