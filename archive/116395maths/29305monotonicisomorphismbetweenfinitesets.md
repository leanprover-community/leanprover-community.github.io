---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/29305monotonicisomorphismbetweenfinitesets.html
---

## Stream: [maths](index.html)
### Topic: [monotonic isomorphism between finite sets](29305monotonicisomorphismbetweenfinitesets.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 18 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132370926):
I'm looking for a lexicographic total order on `fin a × fin b` and a proof that's it's isomorphic to the lexicographic total order on `fin b × fin a`. Is this easy in lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 18 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132372379):
No longer needed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 21 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132508918):
Turns out I do need it after all. I need a linear order isomorphism between any two totally ordered types of the same size. Is that anywhere in lean? Seems like the sort of thing that might have come up doing ordinals.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 21 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132509200):
I have no idea whether this is in Lean. Also, I'm not a master of finsets, like you are. But my initial attempt would be to prove this by induction. Construct a map to `fin n`. If the cardinality is `0`, then it's easy. If it is `k+1` construct a map to `fin k+1` by sending the largest element to `k`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 21 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132509490):
Do you in fact also want to prove that the linear order isom is unique?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 21 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132509662):
I don't care if it's unique I don't think.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 21 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132512403):
> I need a linear order isomorphism between any two totally ordered types of the same size

This isn't true for all types, e.g. nat and int are not order isomorphic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 21 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132512417):
This fact for finite linear orders is a special case of the uniqueness of well orders in the finite case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 21 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132512622):
He's only interested in finite types surely

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 21 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132512913):
I do mean finite

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 21 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132513119):
So the question is "is existence and uniqueness (up to permutation) of a total order on a finite type in Lean"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 21 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132513204):
`ord n` essentially imposes a well order on any set (or the well order theorem directly), which gives you the existence part

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 21 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132513255):
The uniqueness is what I care about.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 21 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132513564):
A linear order of a finite set is a well order, so you get an embedding of each order into `ordinal`; the cardinals for these orders is equal so you have uniqueness by `ord_nat` and hence an order isomorphism

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 21 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132513571):
(this is probably an excessively high powered proof)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 21 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132514251):
I'm still struggling with something like
```lean
noncomputable def something : @order_iso (α) (fin $ fintype.card α) (<) (<) :=
classical.choice $ ordinal.type_eq.1 $ (ordinal.fintype_card (<)).trans (ordinal.lift_type_fin $ fintype.card α).symm
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 21 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132514255):
(I hadn't read the messages by Mario)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 21 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132514599):
oh and my incomplete code (posting here because I don't want to work with it now):

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 21 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monotonic%20isomorphism%20between%20finite%20sets/near/132514602):
```lean
import set_theory.ordinal

universes u v w

variables (α : Type u) [fintype α] [linear_order α]
variables (β : Type v) [has_lt β] [is_well_order β (<)]
variables (γ : Type w)

instance is_well_order_of_fintype : is_well_order α (<) :=
{ wf := sorry }

@[simp] lemma ulift_up_eq (x y : γ) : ulift.up x = ulift.up y ↔ x = y :=
⟨ulift.up.inj, congr_arg _⟩

instance ulift.is_well_order : is_well_order (ulift.{u v} β) (equiv.ulift.to_fun ⁻¹'o has_lt.lt) :=
{ trans := λ ⟨x⟩ ⟨y⟩ ⟨z⟩ Hxy Hyz, @is_trans.trans β (<) _ x y z Hxy Hyz,
  irrefl := λ ⟨x⟩ H, is_irrefl.irrefl (<) x H,
  trichotomous := λ ⟨x⟩ ⟨y⟩, by simpa using is_trichotomous.trichotomous (<) x y,
  wf := inv_image.wf _ $ is_well_order.wf _ }

noncomputable def something : @order_iso (α) (fin $ fintype.card α) (<) (<) :=
classical.choice $ ordinal.type_eq.1 $ (ordinal.fintype_card (<)).trans (ordinal.lift_type_fin $ fintype.card α).symm
#check cardinal.ord_nat
#check something
```


{% endraw %}
