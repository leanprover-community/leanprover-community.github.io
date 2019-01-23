---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01899ccisunexpectedlyfast.html
---

## Stream: [general](index.html)
### Topic: [cc is unexpectedly fast](01899ccisunexpectedlyfast.html)

---

#### [Kenny Lau (Aug 17 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20unexpectedly%20fast/near/132284614):
[2018-08-17-1.png](/user_uploads/3121/H2XKxrFTq7Uuh78QYpIZg00o/2018-08-17-1.png)

#### [Kenny Lau (Aug 17 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20unexpectedly%20fast/near/132284629):
oh... it's cheating :P

#### [Kenny Lau (Aug 17 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20unexpectedly%20fast/near/132284630):
```lean
theorem test : 1001 = 2000 → false :=
λ (H : 1001 = 2000), false.elim (false_of_true_eq_false (absurd H (nat.bit1_ne_bit0 500 1000)))
```

#### [Johan Commelin (Aug 17 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20is%20unexpectedly%20fast/near/132284942):
That's not cheating. That's being smart (-;

