---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/84032Provinglemmawithoutdoingpatternmatching.html
---

## Stream: [general](index.html)
### Topic: [Proving lemma without doing pattern matching](84032Provinglemmawithoutdoingpatternmatching.html)

---

#### [petercommand (Jan 14 2019 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20lemma%20without%20doing%20pattern%20matching/near/155091905):
```
lemma eq.subst' {α : Sort u} {a b : α} {P : Π (m: α), (m = a) ∨ (m = b) → Prop} 
    (h₁ : a = b) (h₂ : P a (or.inl rfl)) : P b (or.inr rfl) := by cases h₁; assumption
```
Is it possible to prove this lemma with eliminators without doing pattern matching?

#### [petercommand (Jan 14 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20lemma%20without%20doing%20pattern%20matching/near/155091997):
In this example, I am trying to prove a variant of the traditional Leibniz equality (subst)

#### [Patrick Massot (Jan 14 2019 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20lemma%20without%20doing%20pattern%20matching/near/155092468):
Of course it's possible, this is what Lean does in the end. You can `#print eq.subst'`. Or am I missing something?

#### [petercommand (Jan 14 2019 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20lemma%20without%20doing%20pattern%20matching/near/155094669):
You are right, it's just that I need to ```set_option pp.implicit true``` before ```#print eq.subst'```

#### [petercommand (Jan 14 2019 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20lemma%20without%20doing%20pattern%20matching/near/155094961):
I thought the generated program doesn't typecheck

#### [Patrick Massot (Jan 16 2019 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20lemma%20without%20doing%20pattern%20matching/near/155271925):
(deleted)

