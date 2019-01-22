---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/75464brewinstalllean.html
---

## [general](index.html)
### [brew install lean](75464brewinstalllean.html)

#### [Sean Leather (Sep 04 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/brew%20install%20lean/near/133326846):
Has anybody tried `brew install lean` on macOS lately? I thought it had stagnated, but the [formula](https://formulae.brew.sh/formula/lean) is actually up to date with v3.4.1. I just installed it and `lean --version` worked just fine. Haven't done anything else, yet.

#### [Simon Hudon (Sep 04 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/brew%20install%20lean/near/133326900):
Does it install `elan`?

#### [Sean Leather (Sep 04 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/brew%20install%20lean/near/133326911):
No.

#### [Simon Hudon (Sep 04 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/brew%20install%20lean/near/133326941):
I feel like that's the only thing it should install.

#### [Sean Leather (Sep 04 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/brew%20install%20lean/near/133327042):
Well, there was discussion recently about installing `lean` from GitHub and not having `gmp` (https://github.com/leanprover/lean/issues/1971), so I think it's important for some people to know that `brew install lean` might work just fine.

