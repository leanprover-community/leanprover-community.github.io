---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72117deconstructsigmatypes.html
---

## Stream: [general](index.html)
### Topic: [deconstruct sigma types](72117deconstructsigmatypes.html)

---

#### [Kevin Buzzard (Nov 30 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871250):
```lean
-- works fine
example (α : Type) (f : α → Type) :
(Σ (a : α), f a) → α :=
λ (x : (Σ (a : α), f a)), x.1

-- doesn't work
example (α : Type) (f : α → Type) :
(Σ (a : α), f a) → α :=
λ (⟨s,t⟩ : (Σ (a : α), f a)), s
-- invalid binder, identifier expected
-- and other errors
```

Can't I take a sigma type apart like this? Isn't a sigma type just a structure? I suspect I'm missing a trick?

#### [Kenny Lau (Nov 30 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871337):
nooooo

#### [Kenny Lau (Nov 30 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871343):
don’t deconstruct things in definitions

#### [Kevin Buzzard (Nov 30 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871461):
```lean
-- works
example (α : Type) (f : α → Type) :
(Σ (a : α), f a) → α :=
λ (x : (Σ (a : α), f a)), let ⟨s,t⟩ := x in s
```

#### [Kevin Buzzard (Nov 30 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871469):
Is this better Kenny?

#### [Kevin Buzzard (Nov 30 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871480):
Or still bad?

#### [Mario Carneiro (Nov 30 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871492):
drop the type ascription

#### [Kevin Buzzard (Nov 30 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871506):
Heh, why would this help?

#### [Mario Carneiro (Nov 30 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871515):
the syntax for lambda match is `λ ⟨s,t⟩, ...` with no type ascriptions permitted

#### [Kevin Buzzard (Nov 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871569):
Oh!

#### [Mario Carneiro (Nov 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871573):
the `⟨s,t⟩` is not actually a pair even though it looks like one

#### [Mario Carneiro (Nov 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871577):
it's just syntax

#### [Kevin Buzzard (Nov 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871593):
Kenny says it's a bad idea -- is the `let` thing OK or is it a bad idea for the same reason?

#### [Mario Carneiro (Nov 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871607):
it's the same

#### [Kevin Buzzard (Nov 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871621):
```lean
-- works
example (α : Type) (f : α → Type) :
(Σ (a : α), f a) → α :=
λ ⟨s,t⟩, s
```

#### [Mario Carneiro (Nov 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871638):
The simpler way is just to pattern match right from the start

#### [Mario Carneiro (Nov 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871648):
```lean
example (α : Type) (f : α → Type) :
(Σ (a : α), f a) → α
| ⟨s,t⟩ := s
```

#### [Mario Carneiro (Nov 30 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871724):
I think the reason Kenny doesn't like those definitions is because it creates an auxiliary, and it doesn't unfold unless it's an explicit pair

#### [Mario Carneiro (Nov 30 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148871743):
as opposed to
```lean
example (α : Type) (f : α → Type) :
(Σ (a : α), f a) → α :=
λ p, p.1
```

#### [Johan Commelin (Nov 30 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148872806):
It would be nice if what Kevin wants would just be syntactic sugar for the `p, p.1` version...

#### [Johan Commelin (Nov 30 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148872834):
But I guess syntactic sugar will only take you so far...

#### [Mario Carneiro (Nov 30 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148873306):
this is a thing: they are called lazy pattern matches in haskell, and they've been discussed on this chat before

#### [Patrick Massot (Nov 30 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148873412):
Yeah, this is a very common fantasy on this chat

#### [Kevin Buzzard (Nov 30 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148874206):
Reality: `set.image (λ x, let (⟨⟨⟨j,k⟩,f⟩,r⟩ : (Σ y : (Σ x : J × J, (R x.1) → (R x.2)), R y.1.1)) := x in
      (X ⟨j,r⟩ - X ⟨k,f r⟩)) {x | x.1 ∈ F})`

#### [Kevin Buzzard (Nov 30 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148874226):
well, that's actually just a small piece of the reality

#### [Kevin Buzzard (Nov 30 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148874243):
We're making colimits in the category of commutative rings!

#### [Kevin Buzzard (Nov 30 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/deconstruct%20sigma%20types/near/148874306):
Without it, it will be `x.1.1.1` everywhere

