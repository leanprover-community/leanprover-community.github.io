---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/97444naminghelp.html
---

## Stream: [general](index.html)
### Topic: [naming help](97444naminghelp.html)

---


{% raw %}
#### [ Sean Leather (Jul 24 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20help/near/130194006):
What names would you give these definitions?

```lean
universes u v

def unknown₁ {α : Type u} (β : α → Type v) : Prop :=
∀ ⦃s t : sigma β⦄ (h : s.1 = t.1), (eq.rec_on h s.2 : β t.1) = t.2

def unknown₂ {α₁ α₂ : Type u} {β₁ : α₁ → Type v} {β₂ : α₂ → Type v} (f : sigma β₁ → sigma β₂) : Prop :=
∀ ⦃s t : sigma β₁⦄, (f s).1 = (f t).1 → s.1 = t.1
```

#### [ Sean Leather (Jul 24 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20help/near/130194079):
The first says a `sigma β` should be considered a function: equal arguments (`fst`s) produce equal results (`snd`s).

#### [ Sean Leather (Jul 24 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20help/near/130194091):
The second says that a function on `sigma`s preserves (injective) equality on the `fst`s.


{% endraw %}
