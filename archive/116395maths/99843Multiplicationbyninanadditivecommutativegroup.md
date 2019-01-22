---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/99843Multiplicationbyninanadditivecommutativegroup.html
---

## [maths](index.html)
### [Multiplication by n in an additive commutative group](99843Multiplicationbyninanadditivecommutativegroup.html)

#### [Johan Commelin (May 14 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Multiplication%20by%20n%20in%20an%20additive%20commutative%20group/near/126531796):
Is this somewhere in mathlib?
```lean
definition mul_n {G : Type*} [add_comm_group G] (n : ℤ) (g : G) : G := n • g -- sorry
```

#### [Johannes Hölzl (May 14 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Multiplication%20by%20n%20in%20an%20additive%20commutative%20group/near/126533667):
Its `gsmul` (generalized(?) scalar multiplication) in `algebra.group_power`

#### [Johan Commelin (May 14 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Multiplication%20by%20n%20in%20an%20additive%20commutative%20group/near/126534062):
Thanks!

#### [Mario Carneiro (May 14 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Multiplication%20by%20n%20in%20an%20additive%20commutative%20group/near/126550514):
the "g" stands for "group" in gsmul and gpow.

