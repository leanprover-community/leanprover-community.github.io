---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04902simplemma.html
---

## [general](index.html)
### [simp lemma](04902simplemma.html)

#### [Kenny Lau (Sep 07 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma/near/133500344):
Should these two be simp lemmas?
```lean
theorem subset_union_left {s₁ s₂ : finset α} : s₁ ⊆ s₁ ∪ s₂ := λ x, mem_union_left _

theorem subset_union_right {s₁ s₂ : finset α} : s₂ ⊆ s₁ ∪ s₂ := λ x, mem_union_right _
```

