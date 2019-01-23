---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99005typeclassproblems.html
---

## Stream: [general](index.html)
### Topic: [typeclass problems](99005typeclassproblems.html)

---

#### [Kenny Lau (Jun 16 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128143681):
This loop is breaking everything
```lean
[class_instances] (25) ?x_99 : out_param (field ?x_97) := @field_extension.to_field ?x_101 ?x_102 ?x_103 ?x_104
[class_instances] (26) ?x_104 : @field_extension ?x_101 ?x_102 ?x_103 := @algebraic_field_extension.to_field_extension ?x_105 ?x_106 ?x_107 ?x_108
[class_instances] (27) ?x_108 : @algebraic_field_extension ?x_105 ?x_106 ?x_107 := @algebraic_closure.to_algebraic_field_extension ?x_109 ?x_110 ?x_111 ?x_112
```

#### [Kenny Lau (Jun 16 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128143694):
```lean
class alg_closed_field (α : Type*) extends field α :=
(alg_closed : ∀ f : polynomial α, f.deg > 1 → ∃ x, f.eval α α x = 0)

class field_extension (α : out_param $ Type*) (β : Type*)
  [out_param $ field α] extends field β :=
(f : α → β) [hom : is_ring_hom f]

instance field_extension.to_is_ring_hom (α : Type*) (β : Type*)
  [field α] [field_extension α β] : is_ring_hom (field_extension.f β) :=
field_extension.hom β

instance field_extension.to_algebra (α : Type*) (β : Type*)
  [field α] [field_extension α β] : algebra α β :=
{ f := field_extension.f β }

class algebraic_field_extension (α : out_param $ Type*) (β : Type*)
  [out_param $ field α] extends field_extension α β :=
(algebraic : ∀ x : β, ∃ f : polynomial α, f.eval α β x = 0)

set_option old_structure_cmd true

class algebraic_closure (α : out_param $ Type*) (β : Type*)
  [out_param $ field α] extends alg_closed_field β, algebraic_field_extension α β

set_option old_structure_cmd false
```

#### [Kenny Lau (Jun 16 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128143821):
I'm not very good at dealing with typeclasses

#### [Kenny Lau (Jun 16 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128144488):
somehow the same setting with `ring` instead of `field` doesn't cause this problem:
```lean
class algebra (R : out_param Type*) (A : Type*)
  [out_param $ comm_ring R] extends comm_ring A :=
(f : R → A) [hom : is_ring_hom f]
```
This doesn't cause any loops

#### [Kenny Lau (Jun 16 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128144728):
solution:
```lean
class is_alg_closed_field (α : Type*) [field α] : Prop :=
(alg_closed : ∀ f : polynomial α, f.deg > 1 → ∃ x, f.eval α α x = 0)

class field_extension (α : out_param $ Type*) (β : Type*)
  [out_param $ field α] extends field β :=
(f : α → β) [hom : is_ring_hom f]

instance field_extension.to_is_ring_hom (α : Type*) (β : Type*)
  [field α] [field_extension α β] : is_ring_hom (field_extension.f β) :=
field_extension.hom β

instance field_extension.to_algebra (α : Type*) (β : Type*)
  [field α] [field_extension α β] : algebra α β :=
{ f := field_extension.f β }

class is_algebraic_field_extension (α : out_param $ Type*) (β : Type*)
  [out_param $ field α] [field_extension α β] : Prop :=
(algebraic : ∀ x : β, ∃ f : polynomial α, f.eval α β x = 0)

class is_algebraic_closure (α : out_param $ Type*) (β : Type*)
  [field α] [field_extension α β]
  extends is_alg_closed_field β, is_algebraic_field_extension α β : Prop
```

#### [Kenny Lau (Jun 16 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128144742):
TLDR: change `algebraic_field_extension` (not `Prop`) to `is_algebraic_field_extension` (`Prop`) etc

#### [Kenny Lau (Jun 16 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128144825):
update: it is not true that the `algebra` causes no problem

#### [Mario Carneiro (Jun 16 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128144857):
> `out_param (field ?x_97)`

not the first time I've seen this today

#### [Kenny Lau (Jun 16 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128144919):
but `module` seems to be doing fine

#### [Mario Carneiro (Jun 16 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128144929):
What caused this typeclass search? You never want to find arbitrary fields

#### [Kenny Lau (Jun 16 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128144937):
what stops `ring.to_module` and `class module ... [ring _]` from forming a loop?

#### [Kenny Lau (Jun 16 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145013):
```quote
What caused this typeclass search? You never want to find arbitrary fields
```
I have something involving rings and no fields at all. The searcher wants to know that it has addition. Somehow it got to fields, and then it started the loop

#### [Mario Carneiro (Jun 16 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145033):
I don't mean just `field ?`, but also `ring ?` and other such things

#### [Mario Carneiro (Jun 16 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145047):
the bad sign is a class on a metavar

#### [Kenny Lau (Jun 16 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145075):
```lean
[class_instances]  class-instance resolution trace
[class_instances] (0) ?x_0 : has_zero α := @pi.has_zero ?x_1 ?x_2 ?x_3
failed is_def_eq
[class_instances] (0) ?x_0 : has_zero α := cardinal.has_zero
failed is_def_eq
[class_instances] (0) ?x_0 : has_zero α := @finsupp.has_zero ?x_4 ?x_5 ?x_6
failed is_def_eq
[class_instances] (0) ?x_0 : has_zero α := @multiset.has_zero ?x_7
failed is_def_eq
[class_instances] (0) ?x_0 : has_zero α := unsigned.has_zero
failed is_def_eq
[class_instances] (0) ?x_0 : has_zero α := @fin.has_zero ?x_8
failed is_def_eq
[class_instances] (0) ?x_0 : has_zero α := int.has_zero
failed is_def_eq
[class_instances] (0) ?x_0 : has_zero α := nat.has_zero
failed is_def_eq
[class_instances] (0) ?x_0 : has_zero α := @no_zero_divisors.to_has_zero ?x_9 ?x_10
[class_instances] (1) ?x_10 : no_zero_divisors α := @domain.to_no_zero_divisors ?x_11 ?x_12
[class_instances] (2) ?x_12 : domain α := @linear_nonneg_ring.to_domain ?x_13 ?x_14
[class_instances] (2) ?x_12 : domain α := @to_domain ?x_13 ?x_14
[class_instances] (3) ?x_14 : linear_ordered_ring α := @linear_nonneg_ring.to_linear_ordered_ring ?x_15 ?x_16
[class_instances] (3) ?x_14 : linear_ordered_ring α := @linear_ordered_field.to_linear_ordered_ring ?x_15 ?x_16
[class_instances] (4) ?x_16 : linear_ordered_field α := @discrete_linear_ordered_field.to_linear_ordered_field ?x_17 ?x_18
[class_instances] (3) ?x_14 : linear_ordered_ring α := @linear_ordered_comm_ring.to_linear_ordered_ring ?x_15 ?x_16
[class_instances] (4) ?x_16 : linear_ordered_comm_ring α := @decidable_linear_ordered_comm_ring.to_linear_ordered_comm_ring ?x_17 ?x_18
[class_instances] (5) ?x_18 : decidable_linear_ordered_comm_ring α := @linear_nonneg_ring.to_decidable_linear_ordered_comm_ring ?x_19 ?x_20 ?x_21 ?x_22
[class_instances] (5) ?x_18 : decidable_linear_ordered_comm_ring α := int.decidable_linear_ordered_comm_ring
failed is_def_eq
[class_instances] (5) ?x_18 : decidable_linear_ordered_comm_ring α := @discrete_linear_ordered_field.to_decidable_linear_ordered_comm_ring ?x_19 ?x_20
[class_instances] (2) ?x_12 : domain α := @division_ring.to_domain ?x_13 ?x_14
[class_instances] (3) ?x_14 : division_ring α := @field.to_division_ring ?x_15 ?x_16
[class_instances] (4) ?x_16 : field α := @field_extension.to_field ?x_17 ?x_18 ?x_19 ?x_20
[class_instances] (5) ?x_20 : @field_extension ?x_17 α ?x_19 := @algebraic_field_extension.to_field_extension ?x_21 ?x_22 ?x_23 ?x_24
[class_instances] (6) ?x_24 : @algebraic_field_extension ?x_21 α ?x_23 := @algebraic_closure.to_algebraic_field_extension ?x_25 ?x_26 ?x_27 ?x_28
[class_instances] (7) ?x_27 : field ?x_25 := @field_extension.to_field ?x_29 ?x_30 ?x_31 ?x_32
[class_instances] (8) ?x_32 : @field_extension ?x_29 ?x_30 ?x_31 := @algebraic_field_extension.to_field_extension ?x_33 ?x_34 ?x_35 ?x_36
[class_instances] (9) ?x_36 : @algebraic_field_extension ?x_33 ?x_34 ?x_35 := @algebraic_closure.to_algebraic_field_extension ?x_37 ?x_38 ?x_39 ?x_40
[class_instances] (10) ?x_39 : field ?x_37 := @field_extension.to_field ?x_41 ?x_42 ?x_43 ?x_44
```

#### [Kenny Lau (Jun 16 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145120):
loop the last 3 lines

#### [Mario Carneiro (Jun 16 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145133):
`field_extension.to_field`

#### [Mario Carneiro (Jun 16 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145134):
kill it

#### [Kenny Lau (Jun 16 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145145):
```lean
class field_extension (α : out_param $ Type*) (β : Type*)
  [out_param $ field α] extends field β :=
(f : α → β) [hom : is_ring_hom f]
```

#### [Kenny Lau (Jun 16 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145161):
```lean
class algebra (R : out_param Type*) (A : Type*)
  [out_param $ comm_ring R] extends comm_ring A :=
(f : R → A) [hom : is_ring_hom f]
```

#### [Kenny Lau (Jun 16 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145162):
```lean
class module (α : out_param $ Type u) (β : Type v) [out_param $ ring α]
  extends has_scalar α β, add_comm_group β :=
(smul_add : ∀r (x y : β), r • (x + y) = r • x + r • y)
(add_smul : ∀r s (x : β), (r + s) • x = r • x + s • x)
(mul_smul : ∀r s (x : β), (r * s) • x = r • s • x)
(one_smul : ∀x : β, (1 : α) • x = x)
```

#### [Kenny Lau (Jun 16 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145165):
(not that `algebra` is not causing problem)

#### [Kenny Lau (Jun 16 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145204):
why does `module` have no problem

#### [Kenny Lau (Jun 16 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145313):
@**Mario Carneiro** what should I replace it with?

#### [Kenny Lau (Jun 16 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128145315):
I see

#### [Kenny Lau (Jun 16 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128147101):
```lean
class subring (α : Type*) [comm_ring α] (S : set α) : Prop :=
(add_mem : ∀ {x y}, x ∈ S → y ∈ S → x + y ∈ S)
(neg_mem : ∀ {x}, x ∈ S → -x ∈ S)
(mul_mem : ∀ {x y}, x ∈ S → y ∈ S → x * y ∈ S)
(one_mem : (1:α) ∈ S)

open subring

instance subring.to_comm_ring (α : Type*) [comm_ring α] (S : set α) [subring α S] : comm_ring S :=
{ add            := λ ⟨x, hx⟩ ⟨y, hy⟩, ⟨x + y, add_mem hx hy⟩,
  add_assoc      := λ ⟨x, hx⟩ ⟨y, hy⟩ ⟨z, hz⟩, subtype.eq $ add_assoc x y z,
  zero           := ⟨0, eq.subst (add_neg_self (1:α)) $ add_mem (one_mem S) $ neg_mem $ one_mem S⟩,
  zero_add       := λ ⟨x, hx⟩, subtype.eq $ zero_add x,
  add_zero       := λ ⟨x, hx⟩, subtype.eq $ add_zero x,
  neg            := λ ⟨x, hx⟩, ⟨-x, neg_mem hx⟩,
  add_left_neg   := λ ⟨x, hx⟩, subtype.eq $ add_left_neg x,
  add_comm       := λ ⟨x, hx⟩ ⟨y, hy⟩, subtype.eq $ add_comm x y,
  mul            := λ ⟨x, hx⟩ ⟨y, hy⟩, ⟨x * y, mul_mem hx hy⟩,
  mul_assoc      := λ ⟨x, hx⟩ ⟨y, hy⟩ ⟨z, hz⟩, subtype.eq $ mul_assoc x y z,
  one            := ⟨1, one_mem S⟩,
  one_mul        := λ ⟨x, hx⟩, subtype.eq $ one_mul x,
  mul_one        := λ ⟨x, hx⟩, subtype.eq $ mul_one x,
  left_distrib   := λ ⟨x, hx⟩ ⟨y, hy⟩ ⟨z, hz⟩, subtype.eq $ left_distrib x y z,
  right_distrib  := λ ⟨x, hx⟩ ⟨y, hy⟩ ⟨z, hz⟩, subtype.eq $ right_distrib x y z,
  mul_comm       := λ ⟨x, hx⟩ ⟨y, hy⟩, subtype.eq $ mul_comm x y }
```

#### [Kenny Lau (Jun 16 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128147109):
will this `instance` cause problems?

#### [Kenny Lau (Jun 16 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128147157):
if so, what should I replace it with?

#### [Kenny Lau (Jun 16 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128150369):
adding `by letI := subring.to_comm_ring _ S` to every definition and theorem is not very feasible

#### [Kenny Lau (Jun 16 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128150378):
and is wasting me a lot of time

#### [Kenny Lau (Jun 16 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128150382):
but as soon as I make it an instance, everything crashes

#### [Kenny Lau (Jun 16 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128162502):
what is this

#### [Kenny Lau (Jun 16 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128162503):
```lean
def Hausdorff_abelianization (G : Type*) [t : topological_group G] : Type* :=
@left_cosets (abelianization G) _ (closure {1})
  (by apply_instance)
```

#### [Kenny Lau (Jun 16 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128162544):
```lean
[class_instances] (0) ?x_60 : topological_group G := t
failed is_def_eq
```

#### [Kenny Lau (Jun 16 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128162755):
Lean, they *are* the same

#### [Kenny Lau (Jun 16 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128165992):
if `subring.to_comm_ring` causes problems then why doesn't `subtype.group` cause problems?

#### [Kenny Lau (Jun 16 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128168992):
```quote
@**Patrick Massot** @**Sebastian Ullrich** @**Mario Carneiro** it can be avoided by using universes instead of `Type*`
```
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/unfolding.20notation.20in.20theorem.20vs.20def.2Finstance/near/128167978

#### [Kenny Lau (Jun 16 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128168993):
oh and of ***course*** the same trick applies to this case

#### [Kenny Lau (Jun 16 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128168994):
there's no loop any more

#### [Kenny Lau (Jun 16 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128168995):
once I use `Type u` instead of `Type*`

#### [Kenny Lau (Jun 16 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128169044):
```quote
Lean, they *are* the same
```
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/typeclass.20problems/near/128162755

#### [Kenny Lau (Jun 16 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128169046):
ditto

#### [Kenny Lau (Jun 16 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174540):
Is this a good instance?
```lean
def Hausdorff_abelianization.setoid (G : Type u)
  [topological_group G] : setoid G :=
left_rel (closure (commutator_subgroup G set.univ))
```

#### [Mario Carneiro (Jun 16 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174678):
A local instance maybe

#### [Mario Carneiro (Jun 16 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174679):
it looks a bit domain specific

#### [Kenny Lau (Jun 16 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174680):
domain specific?

#### [Mario Carneiro (Jun 16 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174681):
is there a reason that should be the canonical equivalence on any top group?

#### [Kenny Lau (Jun 16 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174686):
it's the functor from TopGrp to AbelianHasudorffTopGrp

#### [Johan Commelin (Jun 16 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174688):
Kenny, for every topological group G, there should be at most 1 instance of `setoid G`.

#### [Kenny Lau (Jun 16 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174689):
I see

#### [Kenny Lau (Jun 16 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174690):
ok this isn't canonical then

#### [Johan Commelin (Jun 16 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174737):
So you should probably not make this an instance. But possibly define AbHausTopGrp, and make it an instance of that...

#### [Kenny Lau (Jun 16 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174743):
I'm glad I didn't switch the first two words of the name of the category... :D

#### [Johan Commelin (Jun 16 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174782):
I don't get what would be wrong with that? ... Am I overly naive, and missing a joke?

#### [Kenny Lau (Jun 16 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174789):
it sounds similar to a rude word in german

#### [Johan Commelin (Jun 16 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174830):
Ach so, ich muss noch viel Deutsch üben. Und ich kenn kein unhöfliche Worten.

#### [Kenny Lau (Jun 16 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174838):
"Hau ab" means "piss off"

#### [Johan Commelin (Jun 16 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128174879):
Wunderbar

#### [Kenny Lau (Jun 18 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128218541):
[2018-06-17-2.png](/user_uploads/3121/THVijpQP7DblIbSyWC9G2hGx/2018-06-17-2.png)

#### [Kenny Lau (Jun 18 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128218546):
when I turn `trace.class_instances` on, there's nothing peculiar, except the `has_sizeof` thing getting pretty long

#### [Kenny Lau (Jun 18 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128218550):
that option is not really helpful in my experience

#### [Kenny Lau (Jun 18 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128218552):
@**Mario Carneiro**

#### [Kenny Lau (Jun 18 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219542):
oh and the depth of the class instance search never went to 6

#### [Kenny Lau (Jun 18 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219604):
and I don't think `cogroup.base_change_left` is the problem, after looking at the trace

#### [Kenny Lau (Jun 18 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219700):
it's here: https://github.com/kckennylau/local-langlands-abelian/blob/master/src/torus.lean#L136

#### [Simon Hudon (Jun 18 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219741):
Why does it need an instance of `has_sizeof`?

#### [Kenny Lau (Jun 18 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219742):
no idea

#### [Kenny Lau (Jun 18 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219743):
to build a structure, I think?

#### [Kenny Lau (Jun 18 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219748):
Please help me, my deadline is in like 12 hours

#### [Simon Hudon (Jun 18 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219751):
Your screenshot is not telling me much. If you comment one field declaration at a time, when does it stop failing?

#### [Kenny Lau (Jun 18 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219752):
as soon as I remove the last field

#### [Kenny Lau (Jun 18 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219907):
@**Simon Hudon** is there other information I can provide?

#### [Simon Hudon (Jun 18 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219909):
I think your project needs mathlib

#### [Simon Hudon (Jun 18 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219910):
I'm building it on my machine to have a closer look

#### [Kenny Lau (Jun 18 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219911):
thank you very much

#### [Kenny Lau (Jun 18 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219912):
yes, it does require mathlib

#### [Simon Hudon (Jun 18 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219951):
Is it possible you did not commit the latest version of `leanpkg.toml`? (I don't need it, I can fix it but in general, that makes things smoother for people trying your project)

#### [Kenny Lau (Jun 18 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219960):
oh I didn't really set it up

#### [Simon Hudon (Jun 18 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219961):
Ah ok. Just to be sure, do you use Lean 3.4.1 and the latest mathlib?

#### [Kenny Lau (Jun 18 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128219999):
yes

#### [Kenny Lau (Jun 18 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128220051):
ok not exactly the latest

#### [Kenny Lau (Jun 18 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128220052):
i'm on mathlib commit fe590ca272a41bb321a13be505964e78cad1e731

#### [Kenny Lau (Jun 18 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128220055):
third from latest

#### [Simon Hudon (Jun 18 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128220966):
In this expression `(tensor_a F split.S T)` you get into trouble because `split.S` is a set but a type is expected. If you replace it with `subtype split.S`, type is required to have a `comm_ring` instance which you only have for `T`

#### [Kenny Lau (Jun 18 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128220967):
:o

#### [Kenny Lau (Jun 18 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128220968):
thanks

#### [Kenny Lau (Jun 18 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128220970):
do you have a fix?

#### [Simon Hudon (Jun 18 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221062):
No, it really depends on what you're trying to do. If you actually want `subtype split.S`, you'd need to add `[comm_ring (subtype split.S)]` to the local instances which would get hairy because `split` is a field. Maybe replacing `split.S` with `T` would suit your purpose, in which case, the fit is perfect because you already have a `comm_ring T` instance

#### [Kenny Lau (Jun 18 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221064):
I can't just change my deifnition like that?

#### [Simon Hudon (Jun 18 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221065):
Which one?

#### [Kenny Lau (Jun 18 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221070):
replacing `split.S` with `T`?

#### [Simon Hudon (Jun 18 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221072):
That might work. I haven't tried it but that would fix that particular problem

#### [Kenny Lau (Jun 18 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221074):
I mean, it would be a wrong definition

#### [Simon Hudon (Jun 18 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221116):
What would be the right definition?

#### [Kenny Lau (Jun 18 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221117):
`split.S` as it is

#### [Simon Hudon (Jun 18 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221121):
That would be nonsense: that's not type correct.

#### [Simon Hudon (Jun 18 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221129):
Unless your `tensor_a` definition is wrong and it should take a set there, not a type

#### [Kenny Lau (Jun 18 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221130):
I'm coercing a set to a type

#### [Kenny Lau (Jun 18 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221134):
it's done automatically

#### [Kenny Lau (Jun 18 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221135):
I do it every time

#### [Simon Hudon (Jun 18 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221186):
Right but that type is then expected to be a commutative ring. I'm not sure how that can be proved automatically

#### [Kenny Lau (Jun 18 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221190):
I have a working version above it, one can trace class instance

#### [Kenny Lau (Jun 18 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221228):
I think it will go through subfield -> field -> comm_ring

#### [Simon Hudon (Jun 18 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221235):
How do you prove that it's a subfield?

#### [Kenny Lau (Jun 18 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221237):
```lean
instance finite_Galois_intermediate_extension.to_subfield
```

#### [Kenny Lau (Jun 18 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221239):
L132 of field_extensions.lean

#### [Kenny Lau (Jun 18 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221248):
right, I just realized, there should be no problem, because there's a working version right above it!

#### [Simon Hudon (Jun 18 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221291):
Which line?

#### [Kenny Lau (Jun 18 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221292):
The `#check` one

#### [Kenny Lau (Jun 18 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221293):
L139

#### [Kenny Lau (Jun 18 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221301):
oops

#### [Kenny Lau (Jun 18 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221302):
L123

#### [Kenny Lau (Jun 18 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221303):
https://github.com/kckennylau/local-langlands-abelian/blob/master/src/torus.lean#L123

#### [Kenny Lau (Jun 18 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221304):
```lean
#check λ (F : Type u) [field F]
  (AC : Type v) [field AC] [is_alg_closed_field AC]
  [field_extension F AC] [is_algebraic_closure F AC]
  (T : Type w) [comm_ring T] [algebra F T] [cogroup F T]
(split : finite_Galois_intermediate_extension F AC)
(rank : ℕ),
@cogroup_iso split.S _ (tensor_a F split.S T)
  (tensor_a.comm_ring _ _ _)
  (base_change_left F split.S T)
  (GL₁ⁿ split.S rank) _ _
  (cogroup.base_change_left F split.S T)
  (GL₁ⁿ.cogroup _ _)
```

#### [Simon Hudon (Jun 18 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221344):
If I change that `check` into a `def`:

```lean
def foo := λ (F : Type u) [field F]
  (AC : Type v) [field AC] [is_alg_closed_field AC]
  [field_extension F AC] [is_algebraic_closure F AC]
  (T : Type w) [comm_ring T] [algebra F T] [cogroup F T]
(split : finite_Galois_intermediate_extension F AC)
(rank : ℕ),
@cogroup_iso split.S _ (tensor_a F split.S T)
  (tensor_a.comm_ring _ _ _)
  (base_change_left F split.S T)
  (GL₁ⁿ split.S rank) _ _
  (cogroup.base_change_left F split.S T)
  (GL₁ⁿ.cogroup _ _)
```

#### [Simon Hudon (Jun 18 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221345):
I get I lot of errors

#### [Kenny Lau (Jun 18 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221352):
curious

#### [Simon Hudon (Jun 18 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221354):
[Screen-Shot-2018-06-17-at-7.57.01-PM.png](/user_uploads/3121/K4n0zheF40urE2YaifViOPKA/Screen-Shot-2018-06-17-at-7.57.01-PM.png)

#### [Simon Hudon (Jun 18 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221356):
I think you're asking a lot of type class inference

#### [Kenny Lau (Jun 18 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221395):
heh...

#### [Kenny Lau (Jun 18 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221397):
how about I move them before the colon

#### [Kenny Lau (Jun 18 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221398):
```lean
def foo (F : Type u) [field F]
  (AC : Type v) [field AC] [is_alg_closed_field AC]
  [field_extension F AC] [is_algebraic_closure F AC]
  (T : Type w) [comm_ring T] [algebra F T] [cogroup F T]
(split : finite_Galois_intermediate_extension F AC)
(rank : ℕ) :=
@cogroup_iso split.S _ (tensor_a F split.S T)
  (tensor_a.comm_ring _ _ _)
  (base_change_left F split.S T)
  (GL₁ⁿ split.S rank) _ _
  (cogroup.base_change_left F split.S T)
  (GL₁ⁿ.cogroup _ _)
```

#### [Kenny Lau (Jun 18 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221399):
no errors!

#### [Kenny Lau (Jun 18 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221404):
also I looked at the trace as I said before

#### [Simon Hudon (Jun 18 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221407):
You're right, I didn't do it well

#### [Kenny Lau (Jun 18 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221408):
there is no issue with the typeclass inferences

#### [Kenny Lau (Jun 18 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221409):
and the max depth is 5

#### [Kenny Lau (Jun 18 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221412):
there should not be any error

#### [Simon Hudon (Jun 18 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221463):
Try:

```lean
structure torus (F : Type u) [field F]
  (AC : Type v) [field AC] [is_alg_closed_field AC]
  [field_extension F AC] [is_algebraic_closure F AC]
  (T : Type w) [comm_ring T] [algebra F T] [cogroup F T] :=
(split : finite_Galois_intermediate_extension F AC)
(rank : ℕ)
(splits : foo F AC T split rank)
```

#### [Kenny Lau (Jun 18 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221471):
what the actual

#### [Kenny Lau (Jun 18 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221475):
@**Mario Carneiro** you need to see this

#### [Kenny Lau (Jun 18 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221518):
@**Simon Hudon** what do you think

#### [Simon Hudon (Jun 18 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221525):
I'm not actually sure why the other one wouldn't work. In general, there's nothing wrong with breaking down your definitions into smaller pieces though

#### [Kenny Lau (Jun 18 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221567):
I see

#### [Kenny Lau (Jun 18 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221763):
@**Simon Hudon** how should I break this loop?

#### [Kenny Lau (Jun 18 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221764):
```lean
[class_instances] (5) ?x_31 : field AC := _inst_6
failed is_def_eq
[class_instances] (5) ?x_31 : field AC := @subfield.to_field ?x_34 ?x_35 ?x_36 ?x_37
failed is_def_eq
[class_instances] (5) ?x_31 : field AC := @topological_field.to_field ?x_38 ?x_39
[class_instances] (5) ?x_31 : field AC := @linear_ordered_field.to_field ?x_34 ?x_35
[class_instances] (6) ?x_35 : linear_ordered_field AC := @discrete_linear_ordered_field.to_linear_ordered_field ?x_36 ?x_37
[class_instances] (7) ?x_37 : discrete_linear_ordered_field AC := rat.discrete_linear_ordered_field
failed is_def_eq
[class_instances] (5) ?x_31 : field AC := @discrete_field.to_field ?x_34 ?x_35
[class_instances] (6) ?x_35 : discrete_field AC := rat.field_rat
failed is_def_eq
[class_instances] (6) ?x_35 : discrete_field AC := @discrete_linear_ordered_field.to_discrete_field ?x_36 ?x_37
[class_instances] (7) ?x_37 : discrete_linear_ordered_field AC := rat.discrete_linear_ordered_field
failed is_def_eq
[class_instances] (5) ?x_30 : field ?x_28 := @subfield.to_field ?x_34 ?x_35 ?x_36 ?x_37
[class_instances] (6) ?x_35 : field ?x_34 := _inst_7
[class_instances] (6) ?x_37 : @subfield AC _inst_7 ?x_36 := @finite_Galois_intermediate_extension.to_subfield ?x_38 ?x_39 ?x_40 ?x_41 ?x_42 ?x_43 ?x_44 ?x_45
[class_instances] (7) ?x_39 : field ?x_38 := _inst_7
[class_instances] (7) ?x_41 : field AC := _inst_7
[class_instances] (7) ?x_42 : @is_alg_closed_field AC _inst_7 := _inst_8
[class_instances] (7) ?x_43 : @field_extension AC AC _inst_7 _inst_7 := _inst_9
failed is_def_eq
[class_instances] (7) ?x_43 : @field_extension AC AC _inst_7 _inst_7 := @is_intermediate_field.to_field_extension' ?x_46 ?x_47 ?x_48 ?x_49 ?x_50 ?x_51 ?x_52
failed is_def_eq
[class_instances] (7) ?x_43 : @field_extension AC AC _inst_7 _inst_7 := @is_intermediate_field.to_field_extension ?x_53 ?x_54 ?x_55 ?x_56 ?x_57 ?x_58 ?x_59
failed is_def_eq
[class_instances] (7) ?x_42 : @is_alg_closed_field AC _inst_7 := @is_algebraic_closure.to_is_alg_closed_field ?x_46 ?x_47 ?x_48 ?x_49 ?x_50 ?x_51
[class_instances] (8) ?x_48 : field ?x_46 := _inst_7
[class_instances] (8) ?x_49 : field AC := _inst_7
[class_instances] (8) ?x_50 : @field_extension AC AC _inst_7 _inst_7 := _inst_9
failed is_def_eq
[class_instances] (8) ?x_50 : @field_extension AC AC _inst_7 _inst_7 := @is_intermediate_field.to_field_extension' ?x_52 ?x_53 ?x_54 ?x_55 ?x_56 ?x_57 ?x_58
failed is_def_eq
[class_instances] (8) ?x_50 : @field_extension AC AC _inst_7 _inst_7 := @is_intermediate_field.to_field_extension ?x_59 ?x_60 ?x_61 ?x_62 ?x_63 ?x_64 ?x_65
failed is_def_eq
```

#### [Simon Hudon (Jun 18 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221823):
There seems to be a circular dependency between your instances. You should try to guarantee that something decreases (syntactically) whenever you apply an instance. For example, `instance [decidable_eq a] : decidable_eq (list a) := ... ` is such an instance. It is about `list a` and all the instances it relies on involve simpler expressions.

#### [Kenny Lau (Jun 18 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221863):
sorry but could you explain what you mean by decreasing?

#### [Simon Hudon (Jun 18 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221918):
If you compare `a` and `list a` (one is a type in an assumed instance, the other, in the head of the instance) `list a` is a more complex expression than `a`. That means that if I look for an instance of `decidable_eq (list a)` and I apply the above instance, I'm decreasing the size of my problem so I'm getting closer to a solution. If every instance decreases the size of the problem, you can't search forever. (just like with structural recursion)

#### [Kenny Lau (Jun 18 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221973):
hmm... but there are times at which I would need to infer simpler instances from complex instances?

#### [Simon Hudon (Jun 18 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221980):
like `field` from `discrete_linear_ordered_field`?

#### [Kenny Lau (Jun 18 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221981):
sure

#### [Kenny Lau (Jun 18 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221982):
or sometimes I need to infer a single instance from like 10 instances

#### [Kenny Lau (Jun 18 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128221984):
do you have general workarounds?

#### [Simon Hudon (Jun 18 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222030):
A single instance from 10 instances is not a problem as long as each instance is smaller than the initial one

#### [Kenny Lau (Jun 18 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222031):
hmm I still don't know how to judge whether two instances are smaller

#### [Simon Hudon (Jun 18 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222032):
In the case of `discrete_linear_ordered_field`, does it not `extend` `field`?

#### [Kenny Lau (Jun 18 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222034):
I mean, your examples are quite obvious

#### [Kenny Lau (Jun 18 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222036):
yes it does

#### [Kenny Lau (Jun 18 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222077):
I think

#### [Simon Hudon (Jun 18 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222081):
That should be enough, no? You don't need an instance on top of that

#### [Kenny Lau (Jun 18 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222082):
this is a bad instance then?
```lean
instance subring.to_comm_ring (α : Type u) [comm_ring α] (S : set α) [subring α S] : comm_ring S :=
```

#### [Simon Hudon (Jun 18 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222085):
You can compare by counting the number of symbols and operators in each types.

#### [Kenny Lau (Jun 18 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222096):
that instance doesn't seem to be causing much problem though

#### [Kenny Lau (Jun 18 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222098):
I guess it's because it requires `subring`

#### [Kenny Lau (Jun 18 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222143):
This seems to be the problem:
```lean
instance finite_Galois_intermediate_extension.to_subfield
  (F : Type u) [field F]
  (AC : Type v) [field AC] [is_alg_closed_field AC]
  [field_extension F AC] [is_algebraic_closure F AC]
  (E : finite_Galois_intermediate_extension F AC) :
  subfield _ E.S :=
by apply_instance
```

#### [Simon Hudon (Jun 18 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222144):
`subring` is actually what I find problematic in it

#### [Kenny Lau (Jun 18 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222148):
because I have an instance from subfield to field

#### [Kenny Lau (Jun 18 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222151):
```quote
`subring` is actually what I find problematic in it
```
how so?

#### [Simon Hudon (Jun 18 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222192):
there are invisible operators: `comm_ring S` is actually `comm_ring (subtype S)` which is more complex than `comm_ring a`. However `subring a (subtype S)` is more complex than `comm_ring (subtype S)`

#### [Kenny Lau (Jun 18 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222193):
nah it's `subring a S`

#### [Kenny Lau (Jun 18 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222194):
there is no coercion there

#### [Simon Hudon (Jun 18 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222199):
It might actually fly then

#### [Simon Hudon (Jun 18 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222201):
Lean is actually more tolerant than what I'm used to and I'm not sure if that's a good thing or if it's just handing you enough rope to hang yourself with

#### [Kenny Lau (Jun 18 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222258):
this should be the problem

#### [Kenny Lau (Jun 18 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222259):
```lean
[class_instances] (5) ?x_30 : field ?x_28 := @subfield.to_field ?x_34 ?x_35 ?x_36 ?x_37
[class_instances] (6) ?x_35 : field ?x_34 := _inst_7
[class_instances] (6) ?x_37 : @subfield AC _inst_7 ?x_36 := @finite_Galois_intermediate_extension.to_subfield ?x_38 ?x_39 ?x_40 ?x_41 ?x_42 ?x_43 ?x_44 ?x_45
[class_instances] (7) ?x_39 : field ?x_38 := _inst_7
[class_instances] (7) ?x_41 : field AC := _inst_7
[class_instances] (7) ?x_42 : @is_alg_closed_field AC _inst_7 := _inst_8

```

#### [Kenny Lau (Jun 18 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222298):
right, subfield.to_field is the problem

#### [Simon Hudon (Jun 18 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222299):
You can try commenting one instance at a time until the problem disappears

#### [Simon Hudon (Jun 18 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222302):
cool

#### [Kenny Lau (Jun 18 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222303):
that isn't how it works

#### [Kenny Lau (Jun 18 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222306):
if I comment one instance out, a million lines of code will break

#### [Kenny Lau (Jun 18 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222355):
@**Simon Hudon** a million things depend on `subfield.to_field` though...

#### [Kenny Lau (Jun 18 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222357):
this is a huge abyss

#### [Simon Hudon (Jun 18 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222358):
does `subfield` extend `field`?

#### [Kenny Lau (Jun 18 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222360):
no

#### [Simon Hudon (Jun 18 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222361):
Why not?

#### [Kenny Lau (Jun 18 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222364):
just as `is_subgroup` does not extend `group`

#### [Kenny Lau (Jun 18 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222368):
and as I say this sentence

#### [Kenny Lau (Jun 18 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222370):
why doesn't that cause problems?

#### [Simon Hudon (Jun 18 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222373):
I'm not intimate enough with the algebraic hierarchy to know

#### [Kenny Lau (Jun 18 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222415):
```lean
#check @subtype.group
/-
subtype.group : Π {α : Type u_1} [_inst_1 : group α] {s : set α} [_inst_2 : is_subgroup s], group ↥s
-/
```

#### [Simon Hudon (Jun 18 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222425):
Actually, because there's no coercion, that's not that big of a deal. A different instance must be worse

#### [Kenny Lau (Jun 18 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222427):
hmm

#### [Kenny Lau (Jun 18 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222428):
this is a huge mess

#### [Simon Hudon (Jun 18 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222472):
Yeah, that's a problem with this way of doing type classes. You can't understand each instance in isolation

#### [Kenny Lau (Jun 18 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128222566):
I think depth first search is not very good

#### [Kevin Buzzard (Jun 18 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass%20problems/near/128234704):
Kenny remember as a last resort you can just override the type class system and give it the instances yourself. I used to do this all the time when I got stuck on (much easier) stuff.

