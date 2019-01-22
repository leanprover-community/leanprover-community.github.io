---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48438leftovertrace.html
---

## [general](index.html)
### [leftover trace?](48438leftovertrace.html)

#### [Patrick Massot (Sep 29 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leftover%20trace%3F/near/134895750):
When I build mathlib, I see:

#### [Patrick Massot (Sep 29 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leftover%20trace%3F/near/134895751):
```
@[class, priority 100, to_additive name.mk_string "add_group" name.anonymous]
structure group : Type u → Type u
fields:
group.mul : Π {α : Type u} [c : group α], α → α → α
group.mul_assoc : ∀ {α : Type u} [c : group α] (a b c_1 : α), a * b * c_1 = a * (b * c_1)
group.one : Π (α : Type u) [c : group α], α
group.one_mul : ∀ {α : Type u} [c : group α] (a : α), 1 * a = a
group.mul_one : ∀ {α : Type u} [c : group α] (a : α), a * 1 = a
group.inv : Π {α : Type u} [c : group α], α → α
group.mul_left_inv : ∀ {α : Type u} [c : group α] (a : α), a⁻¹ * a = 1
```

#### [Patrick Massot (Sep 29 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leftover%20trace%3F/near/134895753):
Is there a debug trace left somewhere?

#### [Simon Hudon (Sep 30 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leftover%20trace%3F/near/134899203):
You can use `grep` on the mathlib directory. It's probably one of the flavors of `#print`

