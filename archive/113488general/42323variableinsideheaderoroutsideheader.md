---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42323variableinsideheaderoroutsideheader.html
---

## Stream: [general](index.html)
### Topic: [variable inside header or outside header](42323variableinsideheaderoroutsideheader.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 25 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/variable%20inside%20header%20or%20outside%20header/near/130250391):
```lean
import algebra.module
universes u v w u₁

namespace hidden1

variables {R : Type u} [comm_ring R]
include R

structure is_bilinear_map {M N P}
  [module R M] [module R N] [module R P]
  (f : M → N → P) : Prop :=
(add_pair : ∀ x y z, f (x + y) z = f x z + f y z)
(pair_add : ∀ x y z, f x (y + z) = f x y + f x z)
(smul_pair : ∀ r x y, f (r • x) y = r • f x y)
(pair_smul : ∀ r x y, f x (r • y) = r • f x y)

#check @is_bilinear_map
/-
is_bilinear_map :
  Π {R : Type u_1} [_inst_1 : comm_ring R] {M : Type u_2} {N : Type u_3} {P : Type u_4} [_inst_2 : module R M]
  [_inst_3 : module R N] [_inst_4 : module R P], (M → N → P) → Prop
-/

variables (M : Type v) (N : Type w) (P : Type u₁)
variables [module R M] [module R N] [module R P]

variables {f : M → N → P} (hf : is_bilinear_map f) --works

end hidden1

namespace hidden2

variables {R : Type u} [comm_ring R]
include R
variables (M : Type v) (N : Type w) (P : Type u₁)
variables [module R M] [module R N] [module R P]
variables {M N P}

structure is_bilinear_map (f : M → N → P) : Prop :=
(add_pair : ∀ x y z, f (x + y) z = f x z + f y z)
(pair_add : ∀ x y z, f x (y + z) = f x y + f x z)
(smul_pair : ∀ r x y, f (r • x) y = r • f x y)
(pair_smul : ∀ r x y, f x (r • y) = r • f x y)

#check @is_bilinear_map
/-
is_bilinear_map :
  Π {R : Type u_1} [_inst_1 : comm_ring R] {M : Type u_2} {N : Type u_3} {P : Type u_4}
  [_inst_2 : module R M (comm_ring.to_ring R)] [_inst_3 : module R N (comm_ring.to_ring R)]
  [_inst_4 : module R P (comm_ring.to_ring R)], (M → N → P) → Prop
-/

variables {f : M → N → P} (hf : is_bilinear_map f) -- fails

end hidden2
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 25 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/variable%20inside%20header%20or%20outside%20header/near/130250398):
why does it make a difference whether the variables are inside or outside the header (the space between the name of the definition and the colon)?

