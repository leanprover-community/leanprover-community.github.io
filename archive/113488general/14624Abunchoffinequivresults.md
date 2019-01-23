---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/14624Abunchoffinequivresults.html
---

## Stream: [general](index.html)
### Topic: [A bunch of fin equiv results](14624Abunchoffinequivresults.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 22 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125521488):
```lean
import data.equiv data.fin

variables (m n : ℕ)

def fin_zero_elim {C : Sort*} : fin 0 → C :=
λ x, false.elim $ nat.not_lt_zero x.1 x.2

def fin_sum  : (fin m ⊕ fin n) ≃ fin (m + n) :=
{ to_fun := λ x, sum.rec_on x
    (λ y, ⟨y.1, nat.lt_of_lt_of_le y.2 $ nat.le_add_right m n⟩)
    (λ y, ⟨m + y.1, nat.add_lt_add_left y.2 m⟩),
  inv_fun := λ x, if H : x.1 < m
    then sum.inl ⟨x.1, H⟩
    else sum.inr ⟨x.1 - m, nat.lt_of_add_lt_add_left $
      show m + (x.1 - m) < m + n,
      from (nat.add_sub_of_le $ le_of_not_gt H).symm ▸ x.2⟩,
  left_inv := λ x, sum.cases_on x
    (λ y, by simp [y.2]; from fin.eq_of_veq rfl)
    (λ y, have H : ¬m + y.val < m, by simp [nat.zero_le],
       by simp [H, nat.add_sub_cancel_left];
       from fin.eq_of_veq rfl),
  right_inv := λ x, begin
    by_cases H : x.1 < m,
    { dsimp; rw [dif_pos H]; simp,
      exact fin.eq_of_veq rfl },
    { dsimp; rw [dif_neg H]; simp,
      apply fin.eq_of_veq; simp,
      rw [nat.add_sub_of_le (le_of_not_gt H)] }
  end }

def fin_prod : (fin m × fin n) ≃ fin (m * n) :=
{ to_fun := λ x, ⟨x.2.1 + n * x.1.1, calc
          x.2.1 + n * x.1.1 + 1
        = x.1.1 * n + x.2.1 + 1 : by ac_refl
    ... ≤ x.1.1 * n + n : nat.add_le_add_left x.2.2 _
    ... = (x.1.1 + 1) * n : eq.symm $ nat.succ_mul _ _
    ... ≤ m * n : nat.mul_le_mul_right _ x.1.2⟩,
  inv_fun := λ x, have H : n > 0,
      from nat.pos_of_ne_zero $ λ H,
        nat.not_lt_zero x.1 $ by subst H; from x.2,
    (⟨x.1 / n, (nat.div_lt_iff_lt_mul _ _ H).2 x.2⟩,
     ⟨x.1 % n, nat.mod_lt _ H⟩),
  left_inv := λ ⟨x, y⟩, have H : n > 0,
      from nat.pos_of_ne_zero $ λ H,
        nat.not_lt_zero y.1 $ H ▸ y.2,
    prod.ext.2
    ⟨fin.eq_of_veq $ calc
            (y.1 + n * x.1) / n
          = y.1 / n + x.1 : nat.add_mul_div_left _ _ H
      ... = 0 + x.1 : by rw nat.div_eq_of_lt y.2
      ... = x.1 : nat.zero_add x.1,
     fin.eq_of_veq $ calc
            (y.1 + n * x.1) % n
          = y.1 % n : nat.add_mul_mod_self_left _ _ _
      ... = y.1 : nat.mod_eq_of_lt y.2⟩,
    right_inv := λ x, fin.eq_of_veq $ nat.mod_add_div _ _ }

def fin_zero_pi : (fin 0 → fin m) ≃ fin (m ^ 0) :=
{ to_fun := λ _, ⟨0, dec_trivial⟩,
  inv_fun := λ _ x, false.elim $ nat.not_lt_zero x.1 x.2,
  left_inv := λ _, funext $ λ x, fin_zero_elim x,
  right_inv := λ ⟨x, hx⟩, fin.eq_of_veq $ eq.symm $
    nat.eq_zero_of_le_zero $ nat.le_of_lt_succ hx }

def fin_succ_pi : (fin (n + 1) → fin m) ≃ ((fin n → fin m) × fin m) :=
{ to_fun := λ f, (f ∘ raise_fin, f ⟨n, nat.lt_succ_self n⟩),
  inv_fun := λ f x, if H : x.1 < n then f.1 ⟨x.1, H⟩ else f.2,
  left_inv := λ f, funext $ λ x, if H : x.1 < n
    then by dsimp [raise_fin]; rw [dif_pos H];
      from congr_arg f (fin.eq_of_veq rfl)
    else by dsimp; rw [dif_neg H];
      from congr_arg f (fin.eq_of_veq $ nat.le_antisymm
        (le_of_not_gt H) (nat.le_of_lt_succ x.2)),
  right_inv := λ ⟨f, x⟩, prod.ext.2
    ⟨funext $ λ y, by dsimp [raise_fin]; rw [dif_pos y.2];
       from congr_arg f (fin.eq_of_veq rfl),
     by simp⟩ }

def fin_pi : (fin n → fin m) ≃ fin (m ^ n) :=
nat.rec_on n (fin_zero_pi m) $ λ n ih, calc
      (fin (n + 1) → fin m)
    ≃ ((fin n → fin m) × fin m) : fin_succ_pi _ _
... ≃ ((fin (m ^ n)) × fin m) : equiv.prod_congr ih $ equiv.refl _
... ≃ fin (m ^ (n + 1)) : fin_prod _ _
```

Are these already in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 22 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125521581):
I just built myself a digit converter accidentally
```lean
#eval (fin_pi 5 6).symm ⟨300, dec_trivial⟩ 0 --0
#eval (fin_pi 5 6).symm ⟨300, dec_trivial⟩ 1 --0
#eval (fin_pi 5 6).symm ⟨300, dec_trivial⟩ 2 --2
#eval (fin_pi 5 6).symm ⟨300, dec_trivial⟩ 3 --2
#eval (fin_pi 5 6).symm ⟨300, dec_trivial⟩ 4 --0
#eval (fin_pi 5 6).symm ⟨300, dec_trivial⟩ 5 --0
#eval nat.to_digits 5 300 --[0,0,2,2]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 22 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125521582):
Not exactly, but `fintype.card_sum` seems really similar, and not nearly as complicated of a proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 22 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125521927):
```quote
Not exactly, but `fintype.card_sum` seems really similar, and not nearly as complicated of a proof
```
well, that depends on a lot of lemmas (and I still can't trace where the main proof is), whereas this one builds everything from "scratch"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 22 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125521931):
(ignoring lemmas about natural numbers)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 22 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125521988):
that's what I mean by not nearly as complicated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 22 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125521989):
them giants have shoulders, use them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 22 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125522030):
hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 22 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125522077):
It's possible that a refactoring is necessary, but this is clearly repeating work that already exists and I would want there to be only one proof from which both facts follow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 22 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125522078):
Also there are some similar statements in `cardinal`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 22 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125522084):
right but that's cardinals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 22 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125522086):
I'm pretty sure `nat_cast_pow` unfolds to exactly `fin_pi`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 22 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125522126):
it's talking about cardinality of finite sets in terms of `fin`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 22 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125522134):
interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 22 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125522135):
and relating it to the cardinal power which is the function space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 22 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125522136):
I wonder how my digit extraction will work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 22 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125522137):
```lean
#eval (fin_pi 5 6).symm ⟨300, dec_trivial⟩ 0 --0
#eval (fin_pi 5 6).symm ⟨300, dec_trivial⟩ 1 --0
#eval (fin_pi 5 6).symm ⟨300, dec_trivial⟩ 2 --2
#eval (fin_pi 5 6).symm ⟨300, dec_trivial⟩ 3 --2
#eval (fin_pi 5 6).symm ⟨300, dec_trivial⟩ 4 --0
#eval (fin_pi 5 6).symm ⟨300, dec_trivial⟩ 5 --0
#eval nat.to_digits 5 300 --[0,0,2,2]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 22 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125522138):
will this code run?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 22 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125522188):
Neither the cardinal version nor the finset version gives you this explicitly, since the finset is unordered and the cardinal is nonconstructive (the proof is probably constructive but it's buried in a nonconstructive statement)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 22 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125522189):
exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 22 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/A%20bunch%20of%20fin%20equiv%20results/near/125522190):
but `multiset.pi` should be generalized to `list.pi` and that is your digit calculator

