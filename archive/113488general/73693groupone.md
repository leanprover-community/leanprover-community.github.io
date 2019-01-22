---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73693groupone.html
---

## [general](index.html)
### [group.one?](73693groupone.html)

#### [Kenny Lau (Sep 02 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group.one?/near/133204605):
This is the definition of `group`:
```lean
class group (α : Type u) extends monoid α, has_inv α :=
(mul_left_inv : ∀ a : α, a⁻¹ * a = 1)
```
then how does this produce `group.one`?

#### [Reid Barton (Sep 02 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group.one?/near/133205871):
Probably `monoid` extends `has_one`?

#### [Simon Hudon (Sep 02 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group.one?/near/133205875):
Yes it does and `group` is an `old_structure`

