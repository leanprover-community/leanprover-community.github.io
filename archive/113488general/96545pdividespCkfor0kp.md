---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96545pdividespCkfor0kp.html
---

## Stream: [general](index.html)
### Topic: [p divides pCk for 0<k<p](96545pdividespCkfor0kp.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/p%20divides%20pCk%20for%200%3Ck%3Cp/near/135785763):
Do we have this already?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 14 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/p%20divides%20pCk%20for%200%3Ck%3Cp/near/135785907):
I don't know, but we have p-adic valuations and all the lemmas that go with them, and the easiest proof nowadays might be to compute the p-adic valuation of all the factorials. Another proof is to give a free action of Z/pZ on the set of subsets of Z/pZ of size k (addition) but no doubt this would be much more painful in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 14 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/p%20divides%20pCk%20for%200%3Ck%3Cp/near/135787440):
```lean
import data.nat.choose data.nat.prime
open nat

lemma dvd_fact_of_le : ∀ {k n : ℕ} (hk : 0 < k) (hkn : k ≤ n), k ∣ fact n
| k 0     hk0 hkn := absurd hk0 (not_lt_of_le hkn)
| k (n+1) hk0 hkn := (lt_or_eq_of_le hkn).elim 
  (λ hkn, dvd.trans (dvd_fact_of_le hk0 (le_of_lt_succ hkn)) ⟨n + 1, mul_comm _ _⟩) 
  (λ hkn, hkn.symm ▸ ⟨n.fact, rfl⟩)
  
lemma prime_dvd_fact_iff : ∀ {n p : ℕ} (hp : prime p), p ∣ n.fact ↔ p ≤ n
| 0 p hp := by simp [nat.pos_iff_ne_zero.1 hp.pos, ne.symm (ne_of_lt hp.gt_one)]
| (n+1) p hp := begin
  rw [fact_succ, hp.dvd_mul, prime_dvd_fact_iff hp],
  exact ⟨λ h, h.elim (le_of_dvd (succ_pos _)) le_succ_of_le,
    λ h, (lt_or_eq_of_le h).elim (or.inr ∘ le_of_lt_succ) (λ h, by simp [h])⟩
end

example {p k : ℕ} (hk : 0 < k) (hkp : k < p) (hp : prime p) : p ∣ choose p k :=
(hp.dvd_mul.1 (show p ∣ choose p k * (fact k * fact (p - k)),
  by rw [← mul_assoc, choose_mul_fact_mul_fact (le_of_lt hkp)]; 
    exact dvd_fact_of_le hp.pos (le_refl _))).resolve_right
      (by rw [hp.dvd_mul, prime_dvd_fact_iff hp,
          prime_dvd_fact_iff hp, not_or_distrib, not_le, not_le];
        exact ⟨hkp, nat.sub_lt_self hp.pos hk⟩)

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 14 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/p%20divides%20pCk%20for%200%3Ck%3Cp/near/135787707):
The annoying thing about this proof, is that nothing in mathlib imports `data.nat.choose` and `data.nat.prime` at the moment.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 14 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/p%20divides%20pCk%20for%200%3Ck%3Cp/near/135787893):
thank you @**Chris Hughes**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 14 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/p%20divides%20pCk%20for%200%3Ck%3Cp/near/135788049):
PRed

