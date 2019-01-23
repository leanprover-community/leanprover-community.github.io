---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/141825kbb/77718splittingfields.html
---

## Stream: [kbb](index.html)
### Topic: [splitting fields](77718splittingfields.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/133967305):
It would be great if we could push the splitting fields branch to the point where we can define the Galois group of a splitting field.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/133967354):
So far we can adjoint the root of an irreducible polynomial. There is a `sorry`d statement of the universal property of adjoining a root.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/133967371):
Ooh, the branch I'm talking about is not in this repo, but in the community mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/133967448):
If we combine this with the stuff on Hecke operators, then we'll have the formal abstract of Kevin's paper (modulo one fact that requires a Mjölnir to prove).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134084535):
Little hole in the quotient ring api. I'll leave it to others to :golf: 
```lean
def quotient_ring.lift {α : Type u} {β : Type v} [comm_ring α] [comm_ring β]
(S : set α) [is_ideal S] (f : α → β) [is_ring_hom f] (H : ∀ {a}, a ∈ S → f a = 0) :
quotient_ring.quotient S → β :=
begin
  refine @quotient.lift _ _ (quotient_ring.quotient_rel S) f _,
  intros a b h,
  apply eq_of_sub_eq_zero,
  rw is_submodule.quotient_rel_eq at h,
  simpa only [is_ring_hom.map_sub f] using H h,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085269):
Here is `adjoin_root.lift`:
```lean
def lift {L} [discrete_field L] (i : K → L) [is_field_hom i]
  (x : L) (h : f.eval₂ i x = 0) : (adjoin_root f) → L :=
begin
  refine @quotient_ring.lift _ _ _ _
    (@span _ _ _ ring.to_module ({f} : set (polynomial K))) (is_ideal.span _)
    (eval₂ i x) _ _,
  intros g H,
  simp [span_singleton] at H,
  cases H with y H,
  dsimp at H,
  rw [← H, eval₂_mul],
  simp [h],
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085272):
Which can undoubtly be golfed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085351):
@**Mario Carneiro** I think the next step was some really crazy inductive proof, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085364):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085383):
the next step is the splitting field for one polynomial

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085455):
Do we know that every polynomial over a field has an irreducible factor?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085540):
I think so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085543):
We know that `polynomial K` is a PID

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085545):
and every PID is a UFD

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085546):
I think that latter fact is now also in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085548):
we have UFDs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085554):
Hmm, I guess there is a standard lemma on `lift_mk` or something?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085592):
We'll also need that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085596):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085598):
Yes, Johannes added UFD's after Orsay

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085606):
So we need this `lift_mk` for quotient rings, and then for adjoin root.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085609):
the fact you want about `lift` is composition with the coercion from `K`, and value at the root

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085677):
is the proof constructive? (i.e. is there a function from a polynomial to its smallest irreducible factor or something)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085678):
Not only stuff from `K`, right? Also `K[X]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085688):
Hmm, factoring is hard.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085689):
that isn't needed, it follows by homness

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085693):
???

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085700):
but I guess the quotient map is equal to the eval map, we want to know that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085747):
oh, you didn't prove `lift` is a field hom

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085751):
we definitely need that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085864):
I didn't even prove it is a ring hom

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085866):
Working on that now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134085909):
I think those are the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086046):
@**Mario Carneiro** I need some help to get the right statements for these API things: this is in the `quotient_ring` namespace:
```lean
def lift (S : set α) [is_ideal S] (f : α → β) [is_ring_hom f] (H : ∀ (a : α), a ∈ S → f a = 0) :
quotient_ring.quotient S → β :=
begin
  refine @quotient.lift _ _ (quotient_ring.quotient_rel S) f _,
  intros a b h,
  apply eq_of_sub_eq_zero,
  rw is_submodule.quotient_rel_eq at h,
  simpa only [is_ring_hom.map_sub f] using H _ h,
end

lemma lift_mk {S : set α} [is_ideal S] {f : α → β} [is_ring_hom f] {H : ∀ (a : α), a ∈ S → f a = 0} {a : α} :
lift S f H ⟦a⟧ = f a :=
begin

end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086049):
Should the latter be a simp-lemma?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086054):
At the moment the `⟦a⟧` notation is broken.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086097):
This is my first time working with quotients in Lean...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086098):
I forget the details but I don't think `⟦⟧` is part of the interface

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086108):
The only "public" functions are the map from `K`, and the root element

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086163):
No, I'm working on quotient rings at the moment.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086165):
Splitting field will come later.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086167):
We don't even have `lift` for quotient rings at the moment.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086182):
I guess we want that notation for general quotient rings, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086190):
ah okay

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086193):
you want to redefine `mk` for that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086200):
that way you can give it the right type and find it with typeclass inference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086240):
when you prove it is a ring hom

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086263):
Aah, `local attribute [instance] quotient_rel` fixes it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086321):
that won't help outside the section

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086330):
you still want a public `mk` function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086494):
Right. Quotient rings already had that. But they didn't have `lift`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 17 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134086539):
in that case you should use it in the statement of `lift_mk`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134087318):
Ok, this is what I now have
```lean
namespace quotient_ring -- move this to the right file
open is_submodule
variables {α : Type u} [comm_ring α] {β : Type v} [comm_ring β]

local attribute [instance] quotient_rel

def lift (S : set α) [is_ideal S] (f : α → β) [is_ring_hom f] (H : ∀ (a : α), a ∈ S → f a = 0) :
quotient S → β :=
begin
  refine @quotient.lift _ _ (quotient_rel S) f _,
  intros a b h,
  apply eq_of_sub_eq_zero,
  rw quotient_rel_eq at h,
  simpa only [is_ring_hom.map_sub f] using H _ h,
end

@[simp] lemma lift_mk {S : set α} [is_ideal S] {f : α → β} [is_ring_hom f] {H : ∀ (a : α), a ∈ S → f a = 0} {a : α} :
lift S f H ⟦a⟧ = f a := rfl

#print quotient_ring.is_ring_hom_mk

instance {S : set α} [is_ideal S] {f : α → β} [is_ring_hom f] {H : ∀ (a : α), a ∈ S → f a = 0} :
is_ring_hom (lift S f H) :=
{ map_one := by show lift S f H ⟦1⟧ = 1; simp [is_ring_hom.map_one f],
  map_add := λ a₁ a₂, quotient.induction_on₂ a₁ a₂ $ λ a₁ a₂, begin
    show lift S f H (mk a₁ + mk a₂) = lift S f H ⟦a₁⟧ + lift S f H ⟦a₂⟧,
    have := quotient_ring.is_ring_hom_mk S,
    rw ← this.map_add,
    show lift S f H (⟦a₁ + a₂⟧) = lift S f H ⟦a₁⟧ + lift S f H ⟦a₂⟧,
    simp only [lift_mk, is_ring_hom.map_add f],
  end,
  map_mul := λ a₁ a₂, quotient.induction_on₂ a₁ a₂ $ λ a₁ a₂, begin
    show lift S f H (mk a₁ * mk a₂) = lift S f H ⟦a₁⟧ * lift S f H ⟦a₂⟧,
    have := quotient_ring.is_ring_hom_mk S,
    rw ← this.map_mul,
    show lift S f H (⟦a₁ * a₂⟧) = lift S f H ⟦a₁⟧ * lift S f H ⟦a₂⟧,
    simp only [lift_mk, is_ring_hom.map_mul f],
  end }

end quotient_ring
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 17 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134087827):
You should be able to use `quotient.lift'` instead of `@quotient.lift ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134087890):
Yes, I've been golfing them a bit. I didn't use the `lift'` version though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134088444):
Ok, I pushed a bunch of changes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134088461):
@**Mario Carneiro** I think I might want to try the induction proof now...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089038):
Hmm, so we have UFD's but we don't know that `K[X]` is an example of a UFD

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089066):
What we need to know is that if we have a polynomial `f` with a root `x`, then we can factor `f` as `(X - x) * g`, and the degree of `g` is lower than `degree f`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089116):
@**Chris Hughes** Did you have stuff like that in your QR project?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 17 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089125):
This is Euclidean division

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 17 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089129):
I think we have that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 17 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089131):
It's in polynomial.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089132):
Great

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 17 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089135):
dvd_iff_is_root or something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 17 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089258):
Can't find it. We have similar stuff. `p %ₘ (X - C a) = C (p.eval a)` and `dvd_iff_mod_by_monic_eq_zero`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089262):
@**Johannes Hölzl** Have you thought about PID → UFD in Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 17 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089321):
Euclidean_domain -> UFD might be easier, and that all that's needed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089398):
I didn't think about it yet, but I surely want it. I guess that's my project for today  :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089401):
Awesome!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089414):
Your version of UFD is not a Prop. Do we also want a version where it is a prop?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 17 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089423):
Johan, what's your plan? Are you still working towards a specific goal before the birthday?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 17 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089464):
when is the b-day again?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089469):
Friday

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089474):
I'm not competent enough to work on `pi`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089476):
Maybe I shouldn't distract the experts, and let them work on that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 17 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134089490):
I think what is really needed is Mario and Johannes telling us whether they think anything from the kbb repository could be PR'ed on Friday

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134096940):
How would you even show that `K[X]` is an example of a UFD, with the current definition of UFD? You have to give an algorithm that factors polynomials, right? I'm not sure if those even exist for arbitrary `K`...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134096959):
Or should we just use choice, somehow?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134096976):
@**Johannes Hölzl** did you have a particular plan here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 17 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134096996):
Yes, in the worst case I will use `choice`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134097036):
Ok, I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134098587):
Here is a little hole in the `polynomial` api:
```lean
namespace polynomial

variables {R : Type u} [comm_semiring R] [decidable_eq R]

@[simp] lemma map_id (f : polynomial R) : map id f = f := sorry

end polynomial
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134098592):
How would I unsorry that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 17 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134098676):
@**Johan Commelin** By the way, `kbb` doesn't build for me: `SL2Z_M.finitely_many_orbits` is missing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 17 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134098925):
@**Johan Commelin** `eval₂` is defined using the `finsupp.sum` operator. The combination of `single_eq_C_mul_X` and `finsupp.sum_single` should be enough. With `sum_single` you can proof that the polynomial `f` has a sum representation over `single` and with `single_eq_C_mul_X` you change the representation to `C (id a) * X^n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134099100):
```quote
@**Johan Commelin** By the way, `kbb` doesn't build for me: `SL2Z_M.finitely_many_orbits` is missing
```
Aaah, Kenny changed this. It is now
```lean
def finiteness (hm : m ≠ 0) : fintype (quotient $ action_rel $ SL2Z_M_ m) :=
@fintype.of_equiv _ _ (reps.fintype m hm) (reps_equiv m hm).symm
```
on lines 344-345 of `SL2Z_generators.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134099131):
I think that error was in the Hecke operator file? I'm afraid that file won't really see any improvements. I don't have the time, and probably it is not realistic to work on it before Friday anyway.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134099330):
```lean
@[simp] lemma map_id (f : polynomial R) : map id f = f :=
by dsimp [map,eval₂]; conv { to_lhs, congr, skip, funext, rw ← single_eq_C_mul_X }; simp
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134099343):
@**Johannes Hölzl** Thanks, done :lol:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134114645):
I think that progress on splitting fields will require a bit of an api for `k[x]` as UFD. Things like units of `R[x]` is units of `R`. Every polynomial in `k[x]` of degree (not `nat_degree`!) equal to 0 is a unit, and vice versa. All polynomials of degree 1 are irreducible. Etc...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134114670):
I have not started on any of this. But I also found myself mentally blocked on writing down the definition of a splitting field.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134114674):
I suspect those issues are related.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134259146):
I don't know if this is still needed, but PID -> UFD is finished now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134259321):
Nice! I think the hope was to make progress on splitting field, which will probably not happen very soon. But this is good to know anyway.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134260767):
@**Johannes Hölzl** Cool. Thanks a lot! I think this should help with the splitting fields branch. The next steps there are probably proving that non-zero constants are exactly the units and linear polynomials are irreducible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/splitting%20fields/near/134260795):
Once that is know, I think we can start some sort of construction of splitting fields that inducts on the degree of the polynomial.

