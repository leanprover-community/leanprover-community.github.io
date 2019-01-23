---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/56118newisgrouphom.html
---

## Stream: [maths](index.html)
### Topic: [new is_group_hom](56118newisgrouphom.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 16 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152694):
Recently `is_group_hom` became a class. Previously we had 
```lean
def is_group_anti_hom (f : α → β) : Prop := ∀ a b : α, f (a * b) = f b * f a

namespace is_group_anti_hom
variables {f : α → β} (H : is_group_anti_hom f)
include H

theorem inv (a : α) : (f a)⁻¹ = f a⁻¹ := ...
```
and I could then write
```lean
variables {α : Type} [group α]
def conj (a b : α) := a*b*a⁻¹

lemma inv_conj : (conj b a)⁻¹ = conj b (a⁻¹) := 
conj_is_mph.inv a
```
Is there such a compact way to write the proof of inv_conj with the new `is_group_hom`? I'm not talking about the LHS/RHS switch. I'm talking about the ability to use projection notation instead of writing `(is_group_hom.inv (conj b) a).symm`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152701):
I already complained about this :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 16 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152704):
I'm not really complaining

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152712):
right, but the answer is still you can't use projection

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 16 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152719):
I slightly prefer the old way in this case but I'm open to learning about advantages of the new way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152841):
```quote
Now you do `is_group_hom.one f` I think
```
:point_up: https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/is_group_hom.2Emul/near/124970169

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 16 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152927):
You should be using `inv_conj` in your proofs anyways, so this is a one-time cost

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152943):
but what is `conj_is_mph`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 16 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152945):
Hm, I didn't realize it was almost exactly the same question (I was vaguely aware of Kenny asking something about this change but didn't check)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 16 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125152946):
also you should probably swap `inv_conj` for the same reason `is_group_hom.inv`  was swapped

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 16 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153006):
Indeed my only use of this lemma was a `rw [<-invconj]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 16 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153022):
I'm trying (once more...) to get back to old stuff because I hope I'll have time to resume

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 16 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153069):
I tried to work on the pi instance PR. But I failed in the preparatory work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 16 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153077):
I wanted to properly dispatch the content of Johannes' `prod_module.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 16 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153084):
But trying to move stuff always gets Lean to go crazy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 16 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153093):
everything gets frozen in VSCode and I only end up with a broken mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 16 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153141):
Maybe I should PR everything into the `prod_module` black-hole and then let you or Johannes decide when this becomes a problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153171):
```
import algebra.group

variables {α : Type} [group α] (a b : α)

def conj := a * b * a⁻¹

instance conj.is_group_hom : is_group_hom (conj a) :=
λ x y, by simp [conj, mul_assoc]

lemma inv_conj : conj a (b⁻¹) = (conj a b)⁻¹ :=
is_group_hom.inv (conj a) b

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153213):
@**Patrick Massot** c'est c'que tu veux?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 16 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153251):
I know how to do this (except I went with `by finish [is_group_hom, conj]` in the instance proof. I was only asking how to properly use the new interface

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/new%20is_group_hom/near/125153261):
right, which I demonstrated

