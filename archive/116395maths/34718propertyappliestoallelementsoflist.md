---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/34718propertyappliestoallelementsoflist.html
---

## Stream: [maths](index.html)
### Topic: [property applies to all elements of list](34718propertyappliestoallelementsoflist.html)

---


{% raw %}
#### [ Sean Leather (Apr 30 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/property%20applies%20to%20all%20elements%20of%20list/near/125884050):
Is there another, convenient way one might specify this given what exists in mathlib?

```lean
inductive allp (p : α → Prop) : list α → Prop
| nil {} : allp []
| cons : Π {a : α} {l : list α}, p a → allp l → allp (a :: l)
```

Or, alternatively:

```lean
def allp (p : α → Prop) : list α → Prop :=
list.foldr (λ a h, p a ∧ h) true
```

#### [ Mario Carneiro (Apr 30 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/property%20applies%20to%20all%20elements%20of%20list/near/125884097):
The standard way to write `allp` is `\forall x \in l, p x`

#### [ Sean Leather (Apr 30 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/property%20applies%20to%20all%20elements%20of%20list/near/125884291):
I see. That uses the recursive of `list.mem` to accomplish the recursion of `allp`.

Are there existing equivalent theorems to these?

```lean
theorem allp_singleton (pa : p a) : allp p [a]
theorem allp_append : allp p l₁ → allp p l₂ → allp p (l₁ ++ l₂)
theorem allp_nil : allp p [] ↔ true
theorem allp_cons : allp p (a :: l) ↔ p a ∧ allp p l
```

#### [ Sean Leather (Apr 30 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/property%20applies%20to%20all%20elements%20of%20list/near/125884299):
In the core library?

```lean
lemma ball_nil (p : α → Prop) : ∀ x ∈ @nil α, p x
lemma ball_cons (p : α → Prop) (a : α) (l : list α) : (∀ x ∈ (a :: l), p x) ↔ (p a ∧ ∀ x ∈ l, p x)
```

#### [ Mario Carneiro (Apr 30 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/property%20applies%20to%20all%20elements%20of%20list/near/125884401):
There are `forall_mem_nil` and `forall_mem_cons`, but the append theorem is not there. You can probably get the singleton theorem by simp


{% endraw %}
