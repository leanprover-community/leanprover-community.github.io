---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/17253orderisowoes.html
---

## Stream: [new members](index.html)
### Topic: [order_iso woes](17253orderisowoes.html)

---

#### [Bryan Gin-ge Chen (Oct 10 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135512696):
I'm trying to generalize [this function](https://github.com/leanprover-community/mathlib/blob/tutorials/order/partitions.lean#L366) (there's a typo, that should be a def not a lemma; nonetheless it works...). I want to prove that an `order_iso`gives rise to a `galois_insertion` but I'm stuck on what seems to me to be simple:
```lean
import order.galois_connection order.order_iso

namespace order_iso
variables {β : Type*} {γ : Type*} [preorder β] [preorder γ] 
{r : β → β → Prop} {s : γ → γ → Prop} (oi : order_iso r s)

set_option pp.implicit true

theorem to_galois_connection :
  galois_connection (oi.to_fun) (oi.inv_fun) :=
by unfold galois_connection;
exact λ {b g}, calc (oi.to_fun b) ≤ g ↔ 
  (oi.to_fun b) ≤ (oi.to_fun (oi.inv_fun g)) : by rw oi.right_inv
... ↔ b ≤ (oi.inv_fun g) : by { -- rw oi.ord 
  have : r b (oi.inv_fun g) ↔
    s (oi.to_fun b) (oi.to_fun (oi.inv_fun g)) := (@order_iso.ord β γ r s oi b (oi.inv_fun g)),
  change oi.to_fun b ≤ oi.to_fun (oi.inv_fun g) ↔ b ≤ oi.inv_fun g,
  sorry }

protected def to_galois_insertion [preorder β] [preorder γ] : @galois_insertion β γ _ _
  (oi.to_fun) (oi.inv_fun) :=
{ choice := λ b h, oi.to_fun b,
  gc := to_galois_connection oi,
  le_l_u := λ g, le_of_eq (oi.right_inv g).symm,
  choice_eq := λ b h, rfl }

end order_iso
```
In the tactic state near where I gave up, the only difference I see between the goal and `this` is that the goal uses ≤ and `this` uses `r` and `s`.

#### [Kevin Buzzard (Oct 10 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135521752):
This is a job for @**Kenny Lau**

#### [Mario Carneiro (Oct 10 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135521873):
You should be able to use function coercion instead of `to_fun` and `inv_fun` everywhere

#### [Kenny Lau (Oct 10 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525340):
This is ridiculous.

#### [Kenny Lau (Oct 10 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525381):
```lean
variables {β : Type*} {γ : Type*} [preorder β] [preorder γ]
{r : β → β → Prop} {s : γ → γ → Prop} (oi : order_iso r s)
```

#### [Kenny Lau (Oct 10 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525382):
game: spot the error

#### [Mario Carneiro (Oct 10 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525444):
no error?

#### [Kenny Lau (Oct 10 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525621):
even Mario missed it

#### [Kenny Lau (Oct 10 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525626):
the correct declaration should be
```lean
variables {β : Type*} {γ : Type*} [preorder β] [preorder γ]
(oi : @order_iso β γ (≤) (≤))
```

#### [Johan Commelin (Oct 10 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525779):
In particular, this means that `order_iso` is not what we want it to be.

#### [Kenny Lau (Oct 10 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525786):
```lean
import order.galois_connection order.order_iso

namespace order_iso
variables {β : Type*} {γ : Type*} [preorder β] [preorder γ]
(oi : @order_iso β γ (≤) (≤))

theorem to_galois_connection : galois_connection oi oi.symm :=
λ b g, by rw [ord' oi, apply_inverse_apply]

protected def to_galois_insertion :
  @galois_insertion β γ _ _ oi oi.symm :=
{ choice := λ b h, oi b,
  gc := to_galois_connection oi,
  le_l_u := λ g, le_of_eq (oi.right_inv g).symm,
  choice_eq := λ b h, rfl }

end order_iso
```

#### [Kenny Lau (Oct 10 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525822):
@**Mario Carneiro** how many of this error do you think are in mathlib?

#### [Mario Carneiro (Oct 10 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525870):
Oh, I missed the context

#### [Mario Carneiro (Oct 10 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525877):
I thought you meant those variables don't typecheck

#### [Mario Carneiro (Oct 10 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525899):
are you saying that this is in mathlib?

#### [Mario Carneiro (Oct 10 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525974):
I guess there is a tension here between `order_iso`, which works with explicit relations, and `galois_connection`, which works with types with a `preorder` instance

#### [Kenny Lau (Oct 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135525988):
I'm saying that there are errors like this in mathlib

#### [Mario Carneiro (Oct 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135526005):
I'm sure there are, but someone has to notice them first

#### [Mario Carneiro (Oct 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135526012):
if no one notices them then they aren't doing anyone harm

#### [Johan Commelin (Oct 10 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135526075):
```quote
if no one notices them then they aren't doing anyone harm
```
Except that you might think you have formalised something, but it turns out to be something else.

#### [Mario Carneiro (Oct 10 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135526085):
that's where the fun is

#### [Johan Commelin (Oct 10 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135526089):
Isn't this exactly related to https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/stacks.20project.20.2F.20schemes/near/123090992

#### [Kevin Buzzard (Oct 10 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135529045):
@**Kenny Lau** , now all the people who bothered to click and investigate are in on the joke, can you paste one line of explanation for those of us that are so busy preparing 1st year lectures that we don't even understand the issue at hand here and would hence prefer it if your comments were less cryptic?

#### [Kenny Lau (Oct 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135531256):
@**Kevin Buzzard** basically there are two orders on each type when there should only be one order

#### [Bryan Gin-ge Chen (Oct 10 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/order_iso%20woes/near/135541695):
Thanks Kenny! I'm glad it turned out to be something simple.

