---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51326orderofinputstofunction.html
---

## Stream: [general](index.html)
### Topic: [order of inputs to function](51326orderofinputstofunction.html)

---

#### [Kevin Buzzard (Nov 14 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20of%20inputs%20to%20function/near/147668376):
Sorry if this is already covered somewhere. What should the order of the inputs be in a definition such as

```lean

lemma nth_root_pow_left {x : ℝ} {m n : ℕ} (Hm : 0 < m) (Hx : 0 < x) :
(nth_root x m) ^ (m * n) = x ^ n :=
```
? I'm writing a little library about n'th roots and I've realised that I'm just putting the reals and nats and positivity facts in random and inconsistent orders.

#### [Kenny Lau (Nov 14 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20of%20inputs%20to%20function/near/147668608):
`x` before `m`, so `x` before `m`

