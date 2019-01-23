---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/05825ordersonproducts.html
---

## Stream: [new members](index.html)
### Topic: [orders on products](05825ordersonproducts.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 08 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151190056):
I want definitions like
```lean
instance prod_has_le {α β : Type} [has_le α] [has_le β] : has_le (prod α β) :=
{ le            := λ a b, a.1 ≤ b.1 ∧ a.2 ≤ b.2 }

instance prod_preorder {α β : Type} [preorder α] [preorder β] : preorder (prod α β) :=
{ le_refl       := λ a, ⟨le_refl a.1, le_refl a.2⟩,
  le_trans      := λ a b c h₁ h₂, ⟨le_trans h₁.1 h₂.1, le_trans h₁.2 h₂.2⟩,
  .. prod_has_le }

instance prod_partial_order {α β : Type} [partial_order α] [partial_order β] : partial_order (prod α β) :=
{ le_antisymm   := λ a b h₁ h₂, prod.ext (le_antisymm h₁.1 h₂.1) (le_antisymm h₁.2 h₂.2),
  .. prod_preorder }
```
(At the moment just for ℕ × ℕ, Cauchy sequences and contraction mapping theorem, but probably for more later on.)

These don't seem already to be in mathlib, so should I assume there is some good reason to exclude them? And if so, can I use some namespace trick to define them 'locally'?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 08 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151190145):
I think `attribute local instance` works for something which is already defined.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 08 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151190211):
For example this is from TPIL:
```lean
open classical
local attribute [instance] prop_decidable
```
(after `prop_decidable` has been defined)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 08 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151190359):
"However, such commands can often be prefixed with the local modifier, which indicates that they only have effect until the current section or namespace is closed, or until the end of the current file."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 08 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151190458):
Thanks, I'll do that then.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 08 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151190659):
It would not surprise me if there were a trick to do it all in one go. Does `local instance...` not work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 08 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151190672):
Oh! Do you need to import `pi_instances` or something? Maybe they're there?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Alistair Tucker (Dec 08 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151194606):
Hmm possibly. I didn't know about pi_instances.
```lean
import algebra.pi_instances

def a : bool → ℕ := λ i, if i then 1 else 2
def b : bool → ℕ := λ i, if i then 3 else 4

#check a ≤ b
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 08 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151194675):
```lean
import algebra.pi_instances

example {α β : Type} [partial_order α] [partial_order β] :
partial_order (α × β) := by apply_instance -- fails
```
I thought it might work out of the box. But no.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 08 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151194686):
Maybe the reason it's not an instance is that some people might want to use lex order in some cases

