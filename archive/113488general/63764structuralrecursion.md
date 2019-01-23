---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63764structuralrecursion.html
---

## Stream: [general](index.html)
### Topic: [structural recursion](63764structuralrecursion.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 29 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structural%20recursion/near/132971116):
I have the following code for which Lean cannot prove termination because it's trying to use well-founded recursion:

```lean
import data.equiv.basic

universes u v

inductive get_m : Type u → Type (u+1)
| fail {α} : get_m α
| pure {α} : α → get_m α
| read {α} : (unsigned → get_m α) → get_m α
| loop {α β γ : Type u} : β → (β → unsigned → get_m (α ⊕ β)) → (α → get_m γ) → get_m γ

open ulift

def sum_ulift (α β : Type u) : (α ⊕ β) ≃ (ulift.{v} α ⊕ ulift.{v} β) :=
(equiv.sum_congr equiv.ulift.symm equiv.ulift.symm)

def get_m.up : Π {α : Type u} {β : Type.{max u v}} (Heq : α ≃ β), get_m α → get_m β
| _ _ Heq (get_m.pure x) := get_m.pure $ Heq x
| _ _ Heq (get_m.fail) := get_m.fail
| _ _ Heq (get_m.read f) := get_m.read (λ w, get_m.up Heq (f w))
| _ β' Heq (@get_m.loop α β γ x f g) :=
  get_m.loop (up.{v} x)
    (λ a b, get_m.up (sum_ulift α β) (f (down.{v} a) b))
    (λ w, get_m.up Heq (g $ down w))
```

How can I fix that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 29 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structural%20recursion/near/132974185):
Here's my fix:

```lean
def get_m.up' : Π {α : Type u} {β : Type.{max u v}} (Heq : α → β), get_m α → get_m β :=
λ α β f x, (@get_m.rec_on (λ α _, Π β, (α → β) → get_m β) α x 
(λ α β f, get_m.fail) 
(λ α x β f, get_m.pure $ f x)  
(λ α next get_m_up β f, get_m.read $ λ w, get_m_up w _ f) 
(λ α β γ x₀ body rest get_m_up₀ get_m_up₁ β' f, 
  get_m.loop (up x₀) 
    (λ a b, get_m_up₀ (down a) b (ulift.{v} α ⊕ ulift.{v} β) 
                      (sum_ulift α β)) 
    (λ r, get_m_up₁ (down r) _ f) )) β f
```

I really don't like it but it type checks.

