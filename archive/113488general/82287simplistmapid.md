---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/82287simplistmapid.html
---

## [general](index.html)
### [simp list.map id](82287simplistmapid.html)

#### [Sean Leather (Sep 28 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp list.map id/near/134810749):
Interesting that `simp` doesn't solve `list.map (λ t, t) l = l`.

#### [Sean Leather (Sep 28 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp list.map id/near/134810792):
I suppose I could add this to the `simp`:

```lean
 theorem map_id' {f : α → α} (h : ∀ x, f x = x) (l : list α) : map f l = l
```

#### [Sean Leather (Sep 28 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp list.map id/near/134810856):
Yep, `simp [list.map_id']` does the job.

