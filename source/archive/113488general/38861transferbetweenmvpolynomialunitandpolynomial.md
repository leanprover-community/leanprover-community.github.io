---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/38861transferbetweenmvpolynomialunitandpolynomial.html
---

## [general](index.html)
### [transfer between mv_polynomial unit and polynomial](38861transferbetweenmvpolynomialunitandpolynomial.html)

#### [Johan Commelin (Sep 03 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transfer%20between%20mv_polynomial%20unit%20and%20polynomial/near/133275790):
Suppose I want to build a slick machine to move back and forth between `mv_polynomial unit` and `polynomial`. Does it make sense to start with
```lean
def rel_unit {X : Type u} : (unit → X) → X → Prop :=
λ f x, f unit.star = x
```
More generally, what goes into building a "transfer API"?

#### [Chris Hughes (Sep 03 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transfer%20between%20mv_polynomial%20unit%20and%20polynomial/near/133277005):
I thought about this a bit, and I think the function should take an element of an indexing type as an argument. I think this makes it easier if I want to multiply two univariate polynomials together to get a MV poly in two variables.

#### [Chris Hughes (Sep 03 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transfer%20between%20mv_polynomial%20unit%20and%20polynomial/near/133277077):
I think the transfer API just has all the lemmas about preserving evaluation, degree, multiplication etc.

