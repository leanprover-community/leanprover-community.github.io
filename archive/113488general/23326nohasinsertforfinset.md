---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23326nohasinsertforfinset.html
---

## Stream: [general](index.html)
### Topic: [no `has_insert` for `finset`](23326nohasinsertforfinset.html)

---

#### [Chris Hughes (Jul 04 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20%60has_insert%60%20for%20%60finset%60/near/129094565):
```lean
example {α : Type*} : has_insert α (finset α) := by apply_instance -- doesn't work
```
Shouldn't there be a `has_insert` instance on `finset`? Without it I can't use the notation `{0,1,2}`

#### [Mario Carneiro (Jul 04 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20%60has_insert%60%20for%20%60finset%60/near/129094776):
there is an insert operation, but it requires decidable_eq

