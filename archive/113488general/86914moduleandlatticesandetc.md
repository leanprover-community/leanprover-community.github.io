---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86914moduleandlatticesandetc.html
---

## Stream: [general](index.html)
### Topic: [module and lattices and etc](86914moduleandlatticesandetc.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 06 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20and%20lattices%20and%20etc/near/146859692):
```lean
def module_of_module_of_ring_hom {R : Type u} [ring R]
  {S : Type v} [ring S] (f : R → S) [is_ring_hom f]
  {M : Type w} [add_comm_group M] [module S M] : module R M :=
module.of_core {
  smul := λ r m, f r • m,
  smul_add := λ r, smul_add _,
  add_smul := λ r s x, show f (r + s) • x = _,
    by rw [is_ring_hom.map_add f, add_smul],
  mul_smul := λ r s x, show f (r * s) • x = _,
    by rw [is_ring_hom.map_mul f, mul_smul],
  one_smul := λ x, show f 1 • x = _,
    by rw [is_ring_hom.map_one f, one_smul],
}
```
@**Mario Carneiro** how should we call this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 06 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20and%20lattices%20and%20etc/near/146892841):
@**Mario Carneiro**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 06 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module%20and%20lattices%20and%20etc/near/146894746):
module.of_ring_hom maybe?


{% endraw %}
