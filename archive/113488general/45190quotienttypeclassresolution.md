---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45190quotienttypeclassresolution.html
---

## Stream: [general](index.html)
### Topic: [quotient typeclass resolution](45190quotienttypeclassresolution.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125182192):
here is a working example:
```lean
import group_theory.coset

universes u v

variables (G : Type u) [group G] (X S : Type v)

class group_action : Type (max u v) :=
(fn : G → X → X)
(one : ∀ x, fn 1 x = x)
(mul : ∀ g h x, fn (g * h) x = fn g (fn h x))

variable [group_action G X]
variables (g h : G) (x y : X)

infixr ` ● `:100 := group_action.fn -- \ci

variables {G X g h x y}

@[simp] lemma one_act : (1:G) ● x = x :=
group_action.one G x

lemma mul_act : (g * h) ● x = g ● h ● x :=
group_action.mul g h x

lemma act_act : g ● h ● x = (g * h) ● x :=
eq.symm $ group_action.mul g h x

lemma inv_act (H : g ● x = y) : g⁻¹ ● y = x :=
by rw ← H; simp [act_act]

variables (G X g h x y)

def stab : set G :=
{ g | g ● x = x }

@[simp] lemma mem_stab_iff : g ∈ stab G X x ↔ g ● x = x := iff.rfl

instance stab.is_subgroup : is_subgroup (stab G X x) :=
{ mul_mem := λ g1 g2 hg1 hg2, by simp at hg1 hg2; simp [mul_act, hg1, hg2],
  one_mem := by simp,
  inv_mem := λ g hg, inv_act hg }

example (L : left_cosets (stab G X x)) : false :=
quotient.induction_on L _
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125182195):
working but not minimalized

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125182198):
the error is on the last line

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125182199):
I cannot use `quotient.induction_on` because apparently Lean doesn't know that `left_cosets (stab G X x)` is a quotient

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125182246):
error message:
```
[class_instances]  class-instance resolution trace
[class_instances] (0) ?x_0 : setoid G := @left_rel ?x_1 ?x_2 ?x_3 ?x_4
[class_instances] (1) ?x_2 : group G := _inst_1
[class_instances] (1) ?x_4 : @is_subgroup G _inst_1 _inst_1 ?x_3 := @stab.is_subgroup ?x_5 ?x_6 ?x_7 ?x_8 ?x_9
[class_instances] (2) ?x_6 : group G := _inst_1
[class_instances] (2) ?x_8 : @group_action G _inst_1 ?x_7 := _inst_2
[class_instances] trying next solution, current solution has metavars
@left_rel G _inst_1 (@stab G _inst_1 X _inst_2 ?x_9) _
[...]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125182252):
what is this supposed to mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125182316):
I think the `x` messed up everything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125182318):
How do i solve this problem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient%20typeclass%20resolution/near/125183528):
`left_rel` is a bad instance, because it depends on `s` which is not in the output. I made it a `def` and used `local instance` for the proofs in that file. With this modification, you have to write
```
example (L : left_cosets (stab G X x)) : false :=
by letI := left_rel (stab G X x); exact
quotient.induction_on L _
```
but then it works

