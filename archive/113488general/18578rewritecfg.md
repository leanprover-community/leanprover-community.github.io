---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/18578rewritecfg.html
---

## Stream: [general](index.html)
### Topic: [rewrite_cfg](18578rewritecfg.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 21 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134366830):
Recently Johannes wrote `rwa [htop] {occs := occurrences.pos [2]}` and I suddenly became aware of the rewrite tactic configuration options. Is it only me who missed this? I don't see anything about this in TPIL or the reference manual. I searched a bit and found: https://github.com/leanprover/lean/blob/master/library/init/meta/rewrite_tactic.lean#L11 and https://github.com/leanprover/lean/blob/master/library/init/meta/occurrences.lean. So in case some terms appear several times, you can tell `rw` where you want to rewrite: everywhere (this is the default), only at a list of positions, everywhere except at a list of positions. There are two other parameters. `symm` presumably has to do with backward rewriting. Does it mean everything backward? Or try backward if forward doesn't work? We can experiment if nobody knows. And the last parameter is `md` which seem related to reducibility stuff.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 21 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134366841):
Previously I was using `conv` whenever I should have been using the `occs` parameter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Geoffrey Yeung (Sep 21 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134372914):
I'm still learning basic lean atm, and I've come across this recently: https://leanprover.github.io/tutorial/tutorial.pdf
This is an outdated Theorem Proving in Lean pdf for lean 2. However, there is an appendix in this version, which doesn't exist in the newer version.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Geoffrey Yeung (Sep 21 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134373418):
Even though quite a lot of the tactics have been renamed, changed, or removed, it's still pretty useful as a quick reference, especially for new learners like me. Should someone who's more familiar and knowledgeable about lean tactics update the appendix?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 21 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134375895):
Good question! @**Jeremy Avigad** what happened to this appendix?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 21 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134377970):
Tactics in Lean 2 worked completely different from Lean 3 tactics. Also the syntax very much changes. So I guess the appendix needed to be scrapped :(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 21 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134378895):
I think the closest thing is the reference manual. https://leanprover.github.io/reference/lean_reference.pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 21 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134378904):
This may not be completely up to date, and doesn't cover the mathlib-specific tactics.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 21 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134378921):
But it's certainly more accurate than the Lean 2 tutorial.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 21 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134379488):
It's also worth mentioning the more informal docs on e.g. `simp` and `cc` at https://github.com/leanprover/mathlib/tree/master/docs/extras

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jeremy Avigad (Sep 21 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134382321):
Yes, documentation for tactics in the core lib is in the reference manual, which should match the docstrings closely. The documentation for the mathlib tactics is also really helpful: https://github.com/leanprover/mathlib/blob/master/docs/tactics.md

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 22 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_cfg/near/134413575):
The `occs` parameter for `rewrite` is a bit unreliable (or at least its behaviour is somewhat unintuitive).

