---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17594Supvssup.html
---

## [general](index.html)
### [Sup vs sup](17594Supvssup.html)

#### [Johan Commelin (Dec 06 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sup vs sup/near/150984986):
Is there something in mathlib expressing compatibility between `Sup` and `sup` for complete lattices?
I would expect something like
```lean
lemma Sup_eq_sup (a b : X) : Sup {x | x = a \or x = b} = a \sqcup b := sorry
```

#### [Mario Carneiro (Dec 06 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sup vs sup/near/150985082):
that's `Sup {a, b}` on the left, did you look for that?

#### [Mario Carneiro (Dec 06 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sup vs sup/near/150985130):
also it might be expressed in terms of `Sup (insert a s)`

#### [Johan Commelin (Dec 06 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sup vs sup/near/150985153):
Aah, there is a `Sup_insert`. And that can be chained with `Sup_singleton`

