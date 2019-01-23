---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/40095finsetsubsetunion.html
---

## Stream: [new members](index.html)
### Topic: [finset.subset_union_*](40095finsetsubsetunion.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 16 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset.subset_union_%2A/near/134038959):
Is there a reason why `finset.subset_union_left` and `finset.subset_union_right`have implicit arguments `{s₁ s₂ : finset α}` and the corresponding `set.` theorems have explicit arguments `(s t : set α)`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset.subset_union_%2A/near/134045419):
These questions seem a bit subtle to me. The answer might be because this is one of those functions where you sometimes want the arguments to be implicit and sometimes explicit, depending on the exact context. In those cases what is the best choice?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 16 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset.subset_union_%2A/near/134045517):
Given that `mem_union_left` exists, I think they should be explicit.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 16 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset.subset_union_%2A/near/134053191):
That's what I thought too. [PR here](https://github.com/leanprover/mathlib/pull/353).

