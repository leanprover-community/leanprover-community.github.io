---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25118intereqofselfofsubset.html
---

## [general](index.html)
### [inter_eq_of_self_of_subset](25118intereqofselfofsubset.html)

#### [Reid Barton (Dec 22 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inter_eq_of_self_of_subset/near/152376322):
Should these lemmas from `data.set.basic` be simp lemmas? I was surprised when `simp` didn't solve these statements automatically.
```lean
theorem inter_eq_self_of_subset_left {s t : set α} (h : s ⊆ t) : s ∩ t = s :=
by finish [subset_def, ext_iff, iff_def]

theorem inter_eq_self_of_subset_right {s t : set α} (h : t ⊆ s) : s ∩ t = t :=
by finish [subset_def, ext_iff, iff_def]
```

