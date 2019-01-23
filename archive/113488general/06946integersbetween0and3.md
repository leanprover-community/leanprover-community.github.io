---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/06946integersbetween0and3.html
---

## Stream: [general](index.html)
### Topic: [integers between 0 and 3](06946integersbetween0and3.html)

---


{% raw %}
#### [ Kevin Buzzard (Oct 20 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136162002):
`example : ∀ (r : ℤ), r ≥ 0 → r < 3 → r = 0 ∨ r = 1 ∨ r = 2 := dec_trivial` doesn't work for me. Is there any easy way of getting from $$0\leq r<3$$ (with `r : int`) to the three cases?

#### [ Kevin Buzzard (Oct 20 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136162014):
(with `nat` it works fine so there's a slightly painful way)

#### [ Kenny Lau (Oct 20 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136162377):
```lean
example : ∀ (r : ℤ), r ≥ 0 → r < 3 → r = 0 ∨ r = 1 ∨ r = 2
| (int.of_nat 0) _ _ := dec_trivial
| (int.of_nat 1) _ _ := dec_trivial
| (int.of_nat 2) _ _ := dec_trivial
```

#### [ Kevin Buzzard (Oct 20 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136162649):
So what is the equation compiler doing that `dec_trivial` can't do? It knows things which aren't decidable?

#### [ Kevin Buzzard (Oct 20 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136162650):
PS thanks

#### [ Kevin Buzzard (Oct 20 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136162733):
eew how do I sent this into the middle of a tactic proof?

#### [ Kevin Buzzard (Oct 20 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136162829):
```lean
example (r : ℤ) (H0 : r ≥ 0) (H3 : r < 3) : r = 0 ∨ r = 1 ∨ r = 2 :=
begin
  exact match r, H0, H3 with
  | (int.of_nat 0), _, _ := dec_trivial
  | (int.of_nat 1), _, _ := dec_trivial
  | (int.of_nat 2), _, _ := dec_trivial
  end,
end
```

#### [ Kevin Buzzard (Oct 20 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136162916):
got it

#### [ Mario Carneiro (Oct 20 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136162917):
We need a decidable instance for bounded integer ranges

#### [ Kevin Buzzard (Oct 20 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136162930):
that too. I was just tripped over by commas by the way. They're sometimes there and sometimes not.

#### [ Mario Carneiro (Oct 20 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136162975):
they are there in `match`, not in `def` patterns

#### [ Mario Carneiro (Oct 20 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136162980):
I agree that this is an annoying inconsistency, but it also makes sense locally, if you change it then it doesn't fit something else

#### [ Kenny Lau (Oct 20 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136163123):
```lean
import data.finset

def int.range (m n : ℤ) : finset ℤ :=
(finset.range (int.to_nat (n-m))).map
  ⟨λ r, m+r, λ r s H, int.coe_nat_inj $ add_left_cancel H⟩

theorem int.mem_range_iff {m n r : ℤ} : r ∈ int.range m n ↔ m ≤ r ∧ r < n :=
⟨λ H, let ⟨s, h1, h2⟩ := finset.mem_map.1 H in h2 ▸
  ⟨le_add_of_nonneg_right trivial,
  add_lt_of_lt_sub_left $ match n-m, h1 with
    | (k:ℕ), h1 := by rwa [finset.mem_range, int.to_nat_coe_nat, ← int.coe_nat_lt] at h1
    end⟩,
λ ⟨h1, h2⟩, finset.mem_map.2 ⟨int.to_nat (r-m),
  finset.mem_range.2 $ by rw [← int.coe_nat_lt, int.to_nat_of_nonneg (sub_nonneg_of_le h1),
      int.to_nat_of_nonneg (sub_nonneg_of_le (le_of_lt (lt_of_le_of_lt h1 h2)))];
    exact sub_lt_sub_right h2 _,
  show m + _ = _, by rw [int.to_nat_of_nonneg (sub_nonneg_of_le h1), add_sub_cancel'_right]⟩⟩

instance int.decidable_bounded (P : int → Prop) [decidable_pred P] (m n : ℤ) : decidable (∀ r, m ≤ r → r < n → P r) :=
decidable_of_iff (∀ r ∈ int.range m n, P r) $ by simp only [int.mem_range_iff, and_imp]
```

#### [ Kevin Buzzard (Oct 20 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136164321):
Will this trigger if I have `1<= r <= 5`?

#### [ Kenny Lau (Oct 20 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136167268):
you're welcome to write 3 more instances

#### [ Kenny Lau (Oct 20 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136167269):
but the answer is no

#### [ Kevin Buzzard (Oct 20 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136167496):
You should PR all four

#### [ Kenny Lau (Oct 20 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136167500):
nah I'll wait till they accept my current PR

#### [ Kenny Lau (Oct 20 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136167501):
you can PR all four

#### [ Kenny Lau (Oct 20 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136168035):
```lean
import data.finset

def int.range (m n : ℤ) : finset ℤ :=
(finset.range (int.to_nat (n-m))).map
  ⟨λ r, m+r, λ r s H, int.coe_nat_inj $ add_left_cancel H⟩

theorem int.mem_range_iff {m n r : ℤ} : r ∈ int.range m n ↔ m ≤ r ∧ r < n :=
⟨λ H, let ⟨s, h1, h2⟩ := finset.mem_map.1 H in h2 ▸
  ⟨le_add_of_nonneg_right trivial,
  add_lt_of_lt_sub_left $ match n-m, h1 with
    | (k:ℕ), h1 := by rwa [finset.mem_range, int.to_nat_coe_nat, ← int.coe_nat_lt] at h1
    end⟩,
λ ⟨h1, h2⟩, finset.mem_map.2 ⟨int.to_nat (r-m),
  finset.mem_range.2 $ by rw [← int.coe_nat_lt, int.to_nat_of_nonneg (sub_nonneg_of_le h1),
      int.to_nat_of_nonneg (sub_nonneg_of_le (le_of_lt (lt_of_le_of_lt h1 h2)))];
    exact sub_lt_sub_right h2 _,
  show m + _ = _, by rw [int.to_nat_of_nonneg (sub_nonneg_of_le h1), add_sub_cancel'_right]⟩⟩

instance int.decidable_le_lt (P : int → Prop) [decidable_pred P] (m n : ℤ) : decidable (∀ r, m ≤ r → r < n → P r) :=
decidable_of_iff (∀ r ∈ int.range m n, P r) $ by simp only [int.mem_range_iff, and_imp]

instance int.decidable_le_le (P : int → Prop) [decidable_pred P] (m n : ℤ) : decidable (∀ r, m ≤ r → r ≤ n → P r) :=
decidable_of_iff (∀ r ∈ int.range m (n+1), P r) $ by simp only [int.mem_range_iff, and_imp, int.lt_add_one_iff]

instance int.decidable_lt_lt (P : int → Prop) [decidable_pred P] (m n : ℤ) : decidable (∀ r, m < r → r < n → P r) :=
int.decidable_le_lt P _ _

instance int.decidable_lt_le (P : int → Prop) [decidable_pred P] (m n : ℤ) : decidable (∀ r, m < r → r ≤ n → P r) :=
int.decidable_le_le P _ _
```

#### [ Kenny Lau (Oct 28 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136655155):
https://github.com/leanprover/mathlib/pull/445 @**Kevin Buzzard**

#### [ Kevin Buzzard (Oct 28 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136655417):
Thank you Kenny

#### [ Kenny Lau (Oct 30 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136795548):
Merged @**Kevin Buzzard**

#### [ Tobias Grosser (Oct 30 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/integers%20between%200%20and%203/near/136801131):
(deleted)


{% endraw %}
