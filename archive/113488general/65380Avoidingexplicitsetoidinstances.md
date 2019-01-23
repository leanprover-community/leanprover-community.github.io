---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/65380Avoidingexplicitsetoidinstances.html
---

## Stream: [general](index.html)
### Topic: [Avoiding explicit setoid instances](65380Avoidingexplicitsetoidinstances.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 04 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Avoiding%20explicit%20setoid%20instances/near/127558107):
Below is my proof that quotient by a normal subgroup is a group. I can't do it without giving explicit setoid instances everywhere. Using `haveI` at the beginning of the proof just gives me the error that inferred and synthesized instances are not definitionally equal. Also, in my `begin` `end` tactics blocks, I have to use `assume` within tactics blocks, otherwise my goal is just a metavariable. Is there a way of doing this nicely?
```lean
import group_theory.coset
variables {G : Type*} [group G]

instance (H : set G) [normal_subgroup H] : group (left_cosets H) :=
{ one := @quotient.mk _ (left_rel H) (1 : G),
  mul := λ a b, @quotient.lift_on₂ _ _ _ (left_rel H) (left_rel H) a b 
  (λ a b : G, @quotient.mk _ (left_rel H) (a * b)) 
  (λ a₁ a₂ b₁ b₂ (hab₁ : a₁⁻¹ * b₁ ∈ H) (hab₂ : a₂⁻¹ * b₂ ∈ H), 
    @quotient.sound _ (left_rel H) _ _ 
    ((is_subgroup.mul_mem_cancel_left H (is_subgroup.inv_mem hab₂)).1
        (by rw [mul_inv_rev, mul_inv_rev, ← mul_assoc (a₂⁻¹ * a₁⁻¹),
          mul_assoc _ b₂, ← mul_assoc b₂, mul_inv_self, one_mul, mul_assoc (a₂⁻¹)];
          exact normal_subgroup.normal _ hab₁ _))),
  mul_assoc := λ a b c, @quotient.induction_on₃ _ _ _ (left_rel H) (left_rel H) (left_rel H) 
    _ a b c 
    begin
      assume a b c,
      show @quotient.mk _ (left_rel H) (a * b * c) = @quotient.mk _ (left_rel H) (a * (b * c)),
      rw mul_assoc
    end,
  one_mul := λ a, @quotient.induction_on _ (left_rel H) _ a
    begin
      assume a,
      show @quotient.mk _ (left_rel H) (1 * a) = _,
      rw one_mul
    end,
  mul_one := λ a, @quotient.induction_on _ (left_rel H) _ a
    begin
      assume a,
      show @quotient.mk _ (left_rel H) (a * 1) = _,
      rw mul_one
    end,
  inv := λ a, @quotient.lift_on _ _ (left_rel H) a (λ a, @quotient.mk _ (left_rel H) (a⁻¹))
    begin
      assume a b hab,
      refine @quotient.sound _ (left_rel H) _ _ _,
      show a⁻¹⁻¹ * b⁻¹ ∈ H,
      rw ← mul_inv_rev,
      exact is_subgroup.inv_mem (is_subgroup.mem_norm_comm hab)
    end,
  mul_left_inv := λ a, @quotient.induction_on _ (left_rel H) _ a
    begin
      assume a,
      show @quotient.mk _ (left_rel H) (a⁻¹ * a) = @quotient.mk _ (left_rel H) 1,
      rw inv_mul_self
    end }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 04 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Avoiding%20explicit%20setoid%20instances/near/127558202):
```lean
local attribute [instance] left_rel
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 04 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Avoiding%20explicit%20setoid%20instances/near/127558269):
Chris, did you check how they did quotient modules? It is probably hard to make it nicer than that...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 04 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Avoiding%20explicit%20setoid%20instances/near/127558431):
```quote
```lean
local attribute [instance] left_rel
```
```
I did try that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 04 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Avoiding%20explicit%20setoid%20instances/near/127558723):
All fixed. adding this line solved everything `
instance normal_to_subgroup (H : set G) [normal_subgroup H] : is_subgroup H := by apply_instance`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 04 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Avoiding%20explicit%20setoid%20instances/near/127559187):
Much nicer proof below. Weirdly, marking `normal_subgroup.to_is_subgroup` as an instance solved the problem, even though it already is an instance. Not sure why this would happen.

```lean
import group_theory.coset
variables {G : Type*} [group G] (H : set G) [normal_subgroup H]

local attribute [instance] left_rel normal_subgroup.to_is_subgroup

instance: group (left_cosets H) :=
{ one := ⟦1⟧,
  mul := λ a b, quotient.lift_on₂ a b 
  (λ a b : G, ⟦a * b⟧) 
  (λ a₁ a₂ b₁ b₂ (hab₁ : a₁⁻¹ * b₁ ∈ H) (hab₂ : a₂⁻¹ * b₂ ∈ H), 
    quotient.sound 
    ((is_subgroup.mul_mem_cancel_left H (is_subgroup.inv_mem hab₂)).1
        (by rw [mul_inv_rev, mul_inv_rev, ← mul_assoc (a₂⁻¹ * a₁⁻¹),
          mul_assoc _ b₂, ← mul_assoc b₂, mul_inv_self, one_mul, mul_assoc (a₂⁻¹)];
          exact normal_subgroup.normal _ hab₁ _))),
  mul_assoc := λ a b c, quotient.induction_on₃ 
    a b c (λ a b c, show ⟦_⟧ = ⟦_⟧, by rw mul_assoc),
  one_mul := λ a, quotient.induction_on a
    (λ a, show ⟦_⟧ = ⟦_⟧, by rw one_mul),
  mul_one := λ a, quotient.induction_on a
    (λ a, show ⟦_⟧ = ⟦_⟧, by rw mul_one),
  inv := λ a, quotient.lift_on a (λ a, ⟦a⁻¹⟧)
    (λ a b hab, quotient.sound begin 
      show a⁻¹⁻¹ * b⁻¹ ∈ H,
      rw ← mul_inv_rev,
      exact is_subgroup.inv_mem (is_subgroup.mem_norm_comm hab)
    end),
  mul_left_inv := λ a, quotient.induction_on a
    (λ a, show ⟦_⟧ = ⟦_⟧, by rw inv_mul_self) }
```

