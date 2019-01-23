---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/23186additivegroupgame.html
---

## Stream: [maths](index.html)
### Topic: [additive group game](23186additivegroupgame.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 28 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802827):
The additive group `add_group` in Lean is defined in core Lean, which means it's hard to change. The definition is this:

#### [ Kevin Buzzard (Apr 28 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802831):
```lean
@[class, priority 100]
structure add_group : Type u → Type u
fields:
add_group.add : Π {α : Type u} [c : add_group α], α → α → α
add_group.add_assoc : ∀ {α : Type u} [c : add_group α] (a b c_1 : α), a + b + c_1 = a + (b + c_1)
add_group.zero : Π (α : Type u) [c : add_group α], α
add_group.zero_add : ∀ {α : Type u} [c : add_group α] (a : α), 0 + a = a
add_group.add_zero : ∀ {α : Type u} [c : add_group α] (a : α), a + 0 = a
add_group.neg : Π {α : Type u} [c : add_group α], α → α
add_group.add_left_neg : ∀ {α : Type u} [c : add_group α] (a : α), -a + a = 0
```

#### [ Kevin Buzzard (Apr 28 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802834):
It's a class, with a bunch of axioms.

#### [ Kevin Buzzard (Apr 28 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802837):
And I think one of them follows from the others

#### [ Kevin Buzzard (Apr 28 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802840):
which means that `add_group` can be made to go faster, I think.

#### [ Kevin Buzzard (Apr 28 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802841):
Is that right?

#### [ Kevin Buzzard (Apr 28 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802842):
I wanted to prove this myself:

#### [ Kevin Buzzard (Apr 28 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802843):
```lean
variables {α : Type}
theorem add_group.add_zero
(add : α → α → α)
(add_assoc : ∀ a b c : α, a + b + c = a + (b + c))
(zero : α)
(zero_add : ∀ a : α, 0 + a = a)
(neg : α → α)
(add_left_neg : ∀ a : α, -a + a = 0)
: ∀ a : α, a + 0 = a := sorry
```

#### [ Kevin Buzzard (Apr 28 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802882):
I just faffed around and cut and pasted that from Lean output, it was pretty painful, it would have been much easier to do in emacs.

#### [ Kevin Buzzard (Apr 28 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802883):
And at the end of it all, it didn't work anyway

#### [ Kevin Buzzard (Apr 28 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802886):
because it doesn't know what `+` means yet

#### [ Kevin Buzzard (Apr 28 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802894):
I just wanted to make myself a toy abelian group

#### [ Kevin Buzzard (Apr 28 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802896):
but then start taking away the axioms by editing the definition

#### [ Kevin Buzzard (Apr 28 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802998):
All I want to do is to create an additive group but with one axiom missing.

#### [ Kevin Buzzard (Apr 28 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125802999):
Is there a trick?

#### [ Kevin Buzzard (Apr 28 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20game/near/125803007):
Can I create one with type class inference and then write over the axiom with a sorry?


{% endraw %}
