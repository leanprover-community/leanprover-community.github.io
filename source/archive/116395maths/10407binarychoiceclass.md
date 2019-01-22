---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/10407binarychoiceclass.html
---

## [maths](index.html)
### [binary choice class](10407binarychoiceclass.html)

#### [Sean Leather (May 23 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binary%20choice%20class/near/126968229):
Any thoughts (e.g. name and possible location in mathlib) on this class and instances? It's useful for the `finset` `max`/`min` stuff.

```lean
class has_choice {α : Sort*} (f : α → α → α) : Prop :=
(choice : ∀ a b, f a b = a ∨ f a b = b)

def choice {α : Sort*} (f : α → α → α) [has_choice f] : ∀ (a b : α), f a b = a ∨ f a b = b :=
has_choice.choice f

instance if_choice {α : Sort*} (c : Prop) [d : decidable c] : has_choice (@ite c d α) :=
⟨λ a b, by by_cases h : c; simp [h]⟩

instance min_choice {α : Sort*} [d : decidable_linear_order α] : has_choice (@min α d) :=
⟨λ a b, by simp [min, (if_choice (a ≤ b)).choice]⟩

instance max_choice {α : Sort*} [d : decidable_linear_order α] : has_choice (@max α d) :=
⟨λ a b, if h : a ≤ b then or.inr (max_eq_right h) else or.inl (max_eq_left_of_lt (lt_of_not_ge h))⟩
```

