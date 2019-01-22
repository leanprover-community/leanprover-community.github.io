---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23087boundedexistsdecidable.html
---

## [general](index.html)
### [bounded exists decidable](23087boundedexistsdecidable.html)

#### [Kenny Lau (Apr 23 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20exists%20decidable/near/125567139):
```lean
instance nat.decidable_bexists_lt (n : nat) (P : Π k < n, Prop) :
  ∀ [H : ∀ n h, decidable (P n h)], decidable (∃ n h, P n h) :=
begin
  induction n with n IH; intro; resetI,
  { exact is_false (λ ⟨_, h, _⟩, nat.not_lt_zero _ h) },
  cases IH (λ k h, P k (nat.lt_succ_of_lt h)) with h,
  { by_cases p : P n (nat.lt_succ_self n),
    { exact is_true ⟨n, nat.lt_succ_self n, p⟩ },
    { apply is_false,
      intro hk,
      rcases hk with ⟨k, hk1, hk2⟩,
      cases nat.lt_succ_iff_lt_or_eq.1 hk1 with hk hk,
      { exact h ⟨k, hk, hk2⟩ },
      { subst hk, exact p hk2 } } },
  apply is_true,
  rcases h with ⟨k, hk1, hk2⟩,
  exact ⟨k, nat.lt_succ_of_lt hk1, hk2⟩
end

instance nat.decidable_exists_fin {n : ℕ} (P : fin n → Prop)
  [H : decidable_pred P] : decidable (∃ i, P i) :=
decidable_of_iff (∃ k h, P ⟨k, h⟩)
⟨λ ⟨k, hk1, hk2⟩, ⟨⟨k, hk1⟩, hk2⟩, λ ⟨⟨k, hk1⟩, hk2⟩, ⟨k, hk1, hk2⟩⟩
```

#### [Kenny Lau (Apr 23 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20exists%20decidable/near/125567143):
@**Mario Carneiro** nao penso que isso e em mathlib agora

#### [Kenny Lau (Apr 23 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20exists%20decidable/near/125567144):
would you include them inside?

#### [Chris Hughes (Apr 23 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20exists%20decidable/near/125569210):
Not sure, but I think they might be there for generic fintypes.

