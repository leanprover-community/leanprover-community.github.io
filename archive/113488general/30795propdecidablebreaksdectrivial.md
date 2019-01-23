---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30795propdecidablebreaksdectrivial.html
---

## Stream: [general](index.html)
### Topic: [prop_decidable breaks dec_trivial?](30795propdecidablebreaksdectrivial.html)

---

#### [Kevin Buzzard (Jul 26 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prop_decidable%20breaks%20dec_trivial%3F/near/130351758):
```lean
local attribute [instance] classical.prop_decidable
example : (-1:ℤ) ≠ (0:ℤ) := dec_trivial -- fails
/-
exact tactic failed, type mismatch, given expression has type
  true
but is expected to have type
  as_true (-1 ≠ 0)
state:
⊢ as_true (-1 ≠ 0)
-/
```

In practice this is in the middle of a big file which needs decidable props but occasionally also needs simple calculations like this. Is this expected behaviour?

#### [Patrick Massot (Jul 26 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prop_decidable%20breaks%20dec_trivial%3F/near/130352293):
Did you try `local attribute [instance, priority 0] classical.prop_decidable`?

#### [Kevin Buzzard (Jul 26 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prop_decidable%20breaks%20dec_trivial%3F/near/130352343):
Works! Thanks!

#### [Kevin Buzzard (Jul 26 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prop_decidable%20breaks%20dec_trivial%3F/near/130352372):
What's happening here? Oh -- we have two instances

#### [Patrick Massot (Jul 26 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prop_decidable%20breaks%20dec_trivial%3F/near/130352384):
We really need that `tips_and_tricks.md` in  mathlib docs

#### [Kevin Buzzard (Jul 26 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prop_decidable%20breaks%20dec_trivial%3F/near/130352766):
I sometimes wonder why we can't solve diamond issues using priorities. "now we have two instances of topological_space (X x Y) and they're equal but not defeq so we have rw problems" -- "well just make the one you want a higher priority"

#### [Patrick Massot (Jul 26 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prop_decidable%20breaks%20dec_trivial%3F/near/130353004):
Good question!

