---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01137sumiteoverfin.html
---

## Stream: [general](index.html)
### Topic: [sum ite over fin](01137sumiteoverfin.html)

---


{% raw %}
#### [ Johan Commelin (Sep 07 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum%20ite%20over%20fin/near/133512435):
How do I kill off this one?
```lean
lemma MWE (R : Type v) [ring R] (n : ℕ) :
finset.univ.sum (λ (k : fin (n + 2)), (-1) ^ k.val * ite (0 = k) (1 : R) (0 : R)) = 1 := sorry
```

#### [ Chris Hughes (Sep 07 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum%20ite%20over%20fin/near/133512763):
`finset.sum_eq_single`

#### [ Kenny Lau (Sep 07 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum%20ite%20over%20fin/near/133512793):
not found

#### [ Kenny Lau (Sep 07 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum%20ite%20over%20fin/near/133512872):
```lean
import data.fintype

universe v

lemma MWE (R : Type v) [ring R] (n : ℕ) :
finset.univ.sum (λ (k : fin (n + 2)), (-1) ^ k.val * ite (0 = k) (1 : R) (0 : R)) = 1 :=
begin
  transitivity finset.sum (finset.singleton 0 : finset (fin (n+2))) _,
  { symmetry,
    apply finset.sum_subset,
    { intros i H, simp },
    { intros, simp at a, simp [ne.symm a] } },
  simp, refl
end
```

#### [ Chris Hughes (Sep 07 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum%20ite%20over%20fin/near/133512883):
It's actually `sum_eq_single` due to a naming error.

#### [ Kenny Lau (Sep 07 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum%20ite%20over%20fin/near/133512895):
that's the same thing, and still not found

#### [ Johan Commelin (Sep 07 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum%20ite%20over%20fin/near/133512898):
@**Chris Hughes** My Lean still doesn't find it.

#### [ Chris Hughes (Sep 07 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/sum%20ite%20over%20fin/near/133513251):
I think it might be new.


{% endraw %}
