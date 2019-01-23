---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02007namingissues.html
---

## Stream: [general](index.html)
### Topic: [naming issues](02007namingissues.html)

---

#### [Kenny Lau (May 02 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125982093):
```lean
#check sub_pos_of_lt
-- sub_pos_of_lt : ?M_4 < ?M_3 → 0 < ?M_3 - ?M_4
#check sub_neg_of_lt
-- sub_neg_of_lt : ?M_3 < ?M_4 → ?M_3 - ?M_4 < 0
#check sub_nonpos_of_le
-- sub_nonpos_of_le : ?M_3 ≤ ?M_4 → ?M_3 - ?M_4 ≤ 0
#check sub_nonneg_of_le
-- sub_nonneg_of_le : ?M_4 ≤ ?M_3 → 0 ≤ ?M_3 - ?M_4
```

#### [Kenny Lau (May 02 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125982096):
but I know the answer already: this is in core so we can't do nothing about it

#### [Mario Carneiro (May 02 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125984462):
what's the issue?

#### [Kenny Lau (May 02 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125985953):
```quote
what's the issue?
```
shouldn't one be `lt` and the other be `gt`?

#### [Mario Carneiro (May 02 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986033):
no? there is no usage of `gt` in those lemmas

#### [Kenny Lau (May 02 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986036):
I mean, how can both be lt

#### [Kenny Lau (May 02 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986038):
so does lt imply sub_pos or sub_neg?

#### [Mario Carneiro (May 02 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986043):
both...

#### [Mario Carneiro (May 02 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986084):
it's just a matter of where the variables go

#### [Mario Carneiro (May 02 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986096):
in mathlib the analogous theorem is just called `sub_pos`

#### [Kenny Lau (May 02 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986101):
aha

#### [Johan Commelin (May 02 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986144):
Lol, we need Lean to generate the names for us, given the type. Then we can have *provably correct names*

#### [Mario Carneiro (May 02 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125986147):
although the usage of `pos` and `neg` as names for >0 and <0 is problematic since it overlaps `neg` meaning `-x`

#### [Simon Hudon (May 02 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming%20issues/near/125991698):
maybe `-x` should be called `minus` instead of `neg`?

