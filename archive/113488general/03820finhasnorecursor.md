---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03820finhasnorecursor.html
---

## [general](index.html)
### [fin has no recursor](03820finhasnorecursor.html)

#### [Kenny Lau (Mar 30 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fin has no recursor/near/124402350):
fin doesn’t have the morally correct recursor. we should prove it maybe.

#### [Mario Carneiro (Mar 30 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fin has no recursor/near/124402455):
There are two obvious approaches: using `fz` and `fs` like in `fin2`, or by peeling off the right end instead, with `raise_fin` and `last` or whatever you want to call them

#### [Mario Carneiro (Mar 30 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fin has no recursor/near/124402457):
there should be more consistent naming here...

#### [Mario Carneiro (Mar 30 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fin has no recursor/near/124402660):
```
@[elab_as_eliminator] def fin.succ_rec
  {C : ∀ n, fin n → Sort*}
  (H0 : ∀ n, C (succ n) 0)
  (Hs : ∀ n i, C n i → C (succ n) i.succ) : ∀ {n : ℕ} (i : fin n), C n i
| 0 i := i.elim0
| (succ n) ⟨0, _⟩ := H0 _
| (succ n) ⟨succ i, h⟩ := Hs _ _ (fin.succ_rec ⟨i, lt_of_succ_lt_succ h⟩)

@[elab_as_eliminator] def fin.succ_rec_on {n : ℕ} (i : fin n)
  {C : ∀ n, fin n → Sort*}
  (H0 : ∀ n, C (succ n) 0)
  (Hs : ∀ n i, C n i → C (succ n) i.succ) : C n i :=
i.succ_rec H0 Hs
```

