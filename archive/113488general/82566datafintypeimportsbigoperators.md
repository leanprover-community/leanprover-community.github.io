---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/82566datafintypeimportsbigoperators.html
---

## Stream: [general](index.html)
### Topic: [data.fintype imports big_operators](82566datafintypeimportsbigoperators.html)

---

#### [Johan Commelin (Oct 02 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data.fintype%20imports%20big_operators/near/135034142):
Is this good? I would assume that `data/fintype.lean` is pretty basic. Is it ok that this imports `algebra.big_operators`?

#### [Johannes Hölzl (Oct 02 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data.fintype%20imports%20big_operators/near/135036126):
I think we should move the content of `big_operators` to `finset` anyway. The big operators on lists are in `data/list/...` and the one for `multiset` are in `data/multiset.lean`

