---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/85433toadditivemultiplicative.html
---

## [maths](index.html)
### [to_additive multiplicative](85433toadditivemultiplicative.html)

#### [Patrick Massot (Oct 09 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/to_additive multiplicative/near/135470227):
This is again a question about the machinery allowing to transfer stuff from multiplicative monoids/groups to additive. I'm trying to get a version of https://github.com/leanprover/mathlib/blob/master/group_theory/submonoid.lean#L112-L142 for groups. I tried:
```lean
import group_theory.subgroup

namespace group
variables {α : Type*} [group α]
theorem exists_list_of_mem_closure {s : set α} {a : α} (h : a ∈ closure s) :
  (∃l:list α, (∀x∈l, x ∈ s ∨ x⁻¹ ∈ s) ∧ l.prod = a) :=
begin
  induction h,
  case in_closure.basic : a ha { existsi ([a]), simp [ha] },
  case in_closure.one { existsi ([]), simp },
  case in_closure.mul : a b _ _ ha hb {
    rcases ha with ⟨la, ha, eqa⟩,
    rcases hb with ⟨lb, hb, eqb⟩,
    existsi (la ++ lb),
    simp [eqa.symm, eqb.symm, or_imp_distrib],
    exact assume a, ⟨ha a, hb a⟩
  },
  case in_closure.inv : a a_in_clo hlist {
    rcases hlist with ⟨la, ha, eqa⟩,
    existsi (la.reverse.map (λ x, x⁻¹)),
    split,
    { intros x x_in, 
      rw list.mem_map at x_in,
      rcases x_in with ⟨b, b_in, hb⟩,
      rw list.mem_reverse at b_in,
      specialize ha b b_in,
      have hb' : b = x⁻¹, by rw ←hb ; simp,
      rw [hb, hb'] at ha, 
      cc },
    { rw [←eqa, inv_prod la] } }
end
end group

namespace add_group
variables {α : Type*} [add_group α]

theorem exists_list_of_mem_closure {s : set α} {a : α} (h : a ∈ closure s) :
  (∃l:list α, (∀x∈l, x ∈ s ∨ -x ∈ s) ∧ l.sum = a) :=
@group.exists_list_of_mem_closure (multiplicative α) _ _ _ _

end add_group
```

#### [Patrick Massot (Oct 09 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/to_additive multiplicative/near/135470239):
But Lean doesn't accept the second statement

