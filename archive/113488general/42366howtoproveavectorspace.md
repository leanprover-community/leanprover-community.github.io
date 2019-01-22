---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42366howtoproveavectorspace.html
---

## [general](index.html)
### [how to prove a vector space](42366howtoproveavectorspace.html)

#### [Blair Shi (Aug 13 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20prove%20a%20vector%20space/near/132037240):
I want to prove `vector_space F (has_space n F)`and I have proved `module F (has_space n F)`
```
definition has_space (R : Type) (n : nat) := (fin n) → R

class vector_space (α : out_param $ Type u) (β : Type v) [field α] extends module α β

-- I want to show this one :(
instance (F : Type) (n : ℕ) [field F]: vector_space F (has_space F n) := 
```

#### [Mario Carneiro (Aug 13 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20prove%20a%20vector%20space/near/132037364):
`{}`

#### [Blair Shi (Aug 13 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20prove%20a%20vector%20space/near/132037447):
fair. thank you!

#### [Patrick Massot (Aug 13 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20prove%20a%20vector%20space/near/132037905):
https://github.com/leanprover/mathlib/blob/7dc1f5d2dbda9dd412bb58636f4261bb259ad106/algebra/pi_instances.lean#L51

#### [Kevin Buzzard (Aug 13 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20prove%20a%20vector%20space/near/132038599):
`has_space F n` is the finite-dimensional vector space F^n. What is a better name for this function?

