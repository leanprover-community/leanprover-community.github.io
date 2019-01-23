---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/41867bugwithtypeclasses.html
---

## Stream: [general](index.html)
### Topic: [bug with typeclasses](41867bugwithtypeclasses.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 07 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20typeclasses/near/123411400):
Forgive me for not minimizing:

```
instance structure_presheaf_value_has_zero {R : Type*} [comm_ring R] (U : set (X R)) (HU : is_open U) :
  has_zero (structure_presheaf_value U HU) :=
⟨⟨λ P HP, 0, sorry⟩⟩
#check λ {R : Type*} [comm_ring R] (U : set (X R)) (HU : is_open U), (by apply_instance : has_zero (structure_presheaf_value U HU))
```

Here the `#check` succeeds with this trace:
```
[class_instances]  class-instance resolution trace
[class_instances] (0) ?x_0 : has_zero (@structure_presheaf_value R _inst_1 U HU) := @structure_presheaf_value_has_zero ?x_1 ?x_2 ?x_3 ?x_4
[class_instances] (1) ?x_2 : comm_ring R := _inst_1
```

---

```
instance structure_presheaf_value_has_zero {R : Type*} [comm_ring R] (U : set (X R)) (HU : is_open U) :
  has_zero (structure_presheaf_value U HU) :=
⟨⟨λ P HP, 0, λ u hu,
let ⟨V, ⟨f, hf⟩, huV, hVU⟩ := (D_f_form_basis R).2 U HU u hu in
⟨f, hf ▸ huV, hf ▸ hVU, 0, λ Q hQ h2, eq.symm $ is_ring_hom.map_zero _⟩⟩⟩
#check λ {R : Type*} [comm_ring R] (U : set (X R)) (HU : is_open U), (by apply_instance : has_zero (structure_presheaf_value U HU))
```

Here the `#check` fails with the following trace:
```
[class_instances]  class-instance resolution trace
[class_instances] (0) ?x_0 : has_zero (@structure_presheaf_value R _inst_1 U HU) := @structure_presheaf_value_has_zero ?x_1 ?x_2 ?x_3 ?x_4
failed is_def_eq
[class_instances] (0) ?x_0 : has_zero (@structure_presheaf_value R _inst_1 U HU) := rat.has_zero
failed is_def_eq
[... more shenanigans ...]
```

---

But if I change the last line to:
```
#check λ {R : Type*} [comm_ring R] (U : set (X R)) (HU : is_open U), (structure_presheaf_value_has_zero U HU : has_zero (structure_presheaf_value U HU))
```

Then it succeeds with the following trace:
```
[class_instances]  class-instance resolution trace
[class_instances] (0) ?x_0 : comm_ring R := _inst_1
```

---

any idea why?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 07 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20typeclasses/near/123412417):
Can you show the definition of `structure_resheaf_value` along with any attributes it may have?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 07 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20typeclasses/near/123412616):
```
definition structure_presheaf_value {R : Type*} [comm_ring R] (U : set (X R)) (HU : is_open U) :=
(structure_presheaf_of_types_on_affine_scheme R).F U HU
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 07 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20typeclasses/near/123412661):
and then `instance structure_presheaf_value_has_add {R : Type*} [comm_ring R] (U : set (X R)) (HU : is_open U) :
  has_add (structure_presheaf_value U HU) :=...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 07 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20typeclasses/near/123412667):
and `instance structure_presheaf_value_has_neg`, mul , zero and one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 07 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20typeclasses/near/123413523):
Structures drive me nuts.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 07 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20typeclasses/near/123413566):
I see different behaviour if I set `mul := [long definition]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 07 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20typeclasses/near/123413577):
to if I make the long definition outside and let mul be that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 07 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20typeclasses/near/123413682):
https://github.com/kbuzzard/lean-stacks-project/blob/708d11f6afbcffb0fd552cd7087100a1400fe40d/src/scheme.lean
most of the things are here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 07 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20typeclasses/near/123414031):
OK so we have a workaround

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 07 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20typeclasses/near/123414072):
```
  mul_assoc := λ _ _ _,subtype.eq (funext (λ _,funext (λ _,mul_assoc _ _ _))),
  add_assoc := λ _ _ _,subtype.eq (funext (λ _,funext (λ _,add_assoc _ _ _))),
  zero_add := λ _,subtype.eq (funext (λ _,funext (λ _,zero_add _))),
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 07 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20typeclasses/near/123414073):
and so on and so on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 08 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20typeclasses/near/123458500):
@**Mario Carneiro** could you have a look?


{% endraw %}
