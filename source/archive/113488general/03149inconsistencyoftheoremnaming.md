---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03149inconsistencyoftheoremnaming.html
---

## [general](index.html)
### [inconsistency of theorem naming](03149inconsistencyoftheoremnaming.html)

#### [Kenny Lau (Jul 27 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inconsistency%20of%20theorem%20naming/near/130393117):
```lean
#check list.index_of_nth_le _
/-
list.nth_le ?M_4 (list.index_of ?M_3 ?M_4) ?M_5 = ?M_3
-/
#check list.nth_le_index_of _ _ _
/-
list.index_of (list.nth_le ?M_3 ?M_5 ?M_6) ?M_3 = ?M_5
-/
#check list.nth_le_of_fn _ _
/-
list.nth_le (list.of_fn ?M_3) (?M_4.val) _ = ?M_3 ?M_4
-/
```

#### [Kenny Lau (Jul 27 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inconsistency%20of%20theorem%20naming/near/130393127):
all three examples consist of a function followed by another function in the name

#### [Kenny Lau (Jul 27 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inconsistency%20of%20theorem%20naming/near/130393168):
in the last example, the actual order in the statement is the same as the order in the name, i.e. `nth_le` and then `of_fn`

#### [Kenny Lau (Jul 27 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inconsistency%20of%20theorem%20naming/near/130393173):
but in the first two examples, the order is swapped

