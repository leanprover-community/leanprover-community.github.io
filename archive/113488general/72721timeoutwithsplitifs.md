---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72721timeoutwithsplitifs.html
---

## Stream: [general](index.html)
### Topic: [timeout with split_ifs](72721timeoutwithsplitifs.html)

---

#### [Kenny Lau (Jul 28 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130454443):
```lean
import data.fin

variable {n : ℕ}

def fin.fall : Π i : fin (n+1), i.1 < n → fin n :=
λ i h, ⟨i.1, h⟩

def fin.descend (pivot : fin (n+1)) : Π i : fin (n+1), i ≠ pivot → fin n :=
λ i H, if h : i.1 < pivot.1
  then i.fall (lt_of_lt_of_le h $ nat.le_of_lt_succ pivot.2)
  else i.pred (λ H1, H $ by subst H1;
    replace h := nat.eq_zero_of_le_zero (le_of_not_gt h);
    from fin.eq_of_veq h.symm)

def fin.ascend (pivot : fin (n+1)) : Π i : fin n, fin (n+1) :=
λ i, if i.1 < pivot.1 then i.raise else i.succ

@[simp] lemma fin.descend_ascend (pivot : fin (n+1))
  (i : fin n) (H : pivot.ascend i ≠ pivot) :
  pivot.descend (pivot.ascend i) H = i :=
begin
  unfold fin.descend fin.ascend,
  split_ifs -- (deterministic) timeout
end
```

#### [Kenny Lau (Jul 28 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130454446):
I've used `split_ifs` quite a lot but it just happens to timeout here

#### [Kevin Buzzard (Jul 28 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130455338):
```lean
begin
  unfold fin.descend fin.ascend,
  have P := (ite (i.val < pivot.val) (fin.raise i) (fin.succ i)).val < pivot.val,
  let dP : decidable P := by apply_instance, -- fails
```

Is `P` decidable? It looks decidable to me.

#### [Kenny Lau (Jul 28 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130455339):
it should be decidable

#### [Kenny Lau (Jul 28 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130455342):
but Lean is not very intelligent

#### [Kevin Buzzard (Jul 28 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130455351):
Is there some missing instance `decidable.dite`?

#### [Kevin Buzzard (Jul 28 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130455871):
```quote
Is there some missing instance `decidable.dite`?
```
 `P` is just the statement that some nat is less than some other nat, right? But `example (a b : ℕ) : decidable (a < b) := by apply_instance ` works fine

#### [Kevin Buzzard (Jul 28 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130456027):
Oh I'm being an idiot. I've used `have` instead of `let` again.

#### [Gabriel Ebner (Jul 28 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130456430):
https://github.com/leanprover/mathlib/pull/224

#### [Kevin Buzzard (Jul 28 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130456434):
Nice one Gabriel.

#### [Gabriel Ebner (Jul 28 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130456474):
Apparently `simp` cannot simplify the second ite.

#### [Kenny Lau (Jul 28 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout%20with%20split_ifs/near/130456480):
thanks

