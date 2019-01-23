---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37878somethingistaking1second.html
---

## Stream: [general](index.html)
### Topic: [something is taking 1 second](37878somethingistaking1second.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 23 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/something%20is%20taking%201%20second/near/130147638):
```lean
import linear_algebra.multivariate_polynomial

universes u

namespace mv_polynomial

variables {σ : Type*} [decidable_eq σ] {α : Type*} [decidable_eq α] [comm_ring α]

instance : comm_ring (mv_polynomial σ α) := finsupp.to_comm_ring

instance C_is_ring_hom : is_ring_hom (C : α → mv_polynomial σ α) :=
{ map_one := C_1,
  map_add := λ x y, finsupp.single_add,
  map_mul := λ x y, eq.symm $ C_mul_monomial }

end mv_polynomial
open mv_polynomial

noncomputable theory
local attribute [instance] classical.prop_decidable

-- def ℤpinv := {x ∈ ℚ | ∃ n : ℕ, ∃ y : ℤ, x * (p:ℚ)^n = y}
set_option profiler true
lemma functorial_C_X {R : Type u} [comm_ring R] : functorial (C : R → mv_polynomial ℕ R) (X 0) = X 0 :=
begin
  simp [functorial,X]
end

#check 2
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 23 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/something%20is%20taking%201%20second/near/130147646):
```
elaboration of functorial_C_X took 975ms
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 23 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/something%20is%20taking%201%20second/near/130147865):
Over here it isn't even a proof...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 23 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/something%20is%20taking%201%20second/near/130147908):
that's just the first step

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 23 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/something%20is%20taking%201%20second/near/130147911):
Ok


{% endraw %}
