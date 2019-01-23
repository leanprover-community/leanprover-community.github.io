---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74264minofnonemptysetofnats.html
---

## Stream: [general](index.html)
### Topic: [min of non-empty set of nats](74264minofnonemptysetofnats.html)

---

#### [Kevin Buzzard (Jul 30 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/min%20of%20non-empty%20set%20of%20nats/near/130570396):
Presumably this is easy?

```lean
example (p : ℕ → Prop) : (∃ n : ℕ, p n) → ∃! m : ℕ, (p m ∧ ∀ d, d < m → ¬ (p d)) :=
```

#### [Kenny Lau (Jul 30 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/min%20of%20non-empty%20set%20of%20nats/near/130570547):
```lean
example (p : ℕ → Prop) [decidable_pred p] :
  (∃ n : ℕ, p n) → ∃! m : ℕ, (p m ∧ ∀ d, d < m → ¬ (p d)) :=
λ H, ⟨nat.find H, ⟨nat.find_spec H, λ _, nat.find_min H⟩,
λ y hy, le_antisymm (le_of_not_gt $ λ H2, hy.2 (nat.find H) H2 $ nat.find_spec H) $
nat.find_min' H hy.1⟩
```

#### [Kevin Buzzard (Jul 30 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/min%20of%20non-empty%20set%20of%20nats/near/130570608):
Thanks Kenny.

