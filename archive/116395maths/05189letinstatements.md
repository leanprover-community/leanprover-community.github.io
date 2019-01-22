---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/05189letinstatements.html
---

## [maths](index.html)
### [let in statements](05189letinstatements.html)

#### [Patrick Massot (Dec 19 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/let%20in%20statements/near/152207819):
How does mathlib like using `let` in order to unclutter a statement, as in:
```lean
lemma uniform_continuous₂_iff [uniform_space α] [uniform_space β] [uniform_space γ]
{f : α → β → γ}  :
let π_α : (α × β) × (α × β) → α × α := (λ p, (p.1.1, p.2.1)),
    π_β : (α × β) × (α × β) → β × β := (λ p, (p.1.2, p.2.2)),
    F   : (α × β) × (α × β) → γ × γ := (λ p, (f p.1.1 p.1.2, f p.2.1 p.2.2)) in
uniform_continuous₂ f ↔ map F (comap π_α uniformity ⊓ comap π_β uniformity) ≤ uniformity :=
by simp [uniform_continuous,uniformity_prod, tendsto]
```

#### [Patrick Massot (Dec 19 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/let%20in%20statements/near/152207833):
Of course this is done in a file having `set_option eqn_compiler.zeta true`

#### [Patrick Massot (Dec 19 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/let%20in%20statements/near/152207931):
Note that the above snippet also use full type ascriptions in lets in order to clarify what are those functions without reading their obscure definition

#### [Scott Morrison (Dec 19 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/let%20in%20statements/near/152212620):
Seems like a good idea.

