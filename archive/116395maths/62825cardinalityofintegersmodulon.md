---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/62825cardinalityofintegersmodulon.html
---

## Stream: [maths](index.html)
### Topic: [cardinality of integers modulo n](62825cardinalityofintegersmodulon.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey van Langen (Jan 14 2019 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155093729):
I am trying to prove the following result
```lean
example (n : ℕ) (h : n ≠ 0) : ideal.quotient (ideal.span {(n : ℤ)}) ≃ fin n := sorry
```
This seems a simple result in math, but I am having a lot of trouble making a simple proof in lean. Anyone got any suggestions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155093930):
I don't think you want that `fintype` there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155093986):
`fintype` means as much as "Hey Lean, this type is finite".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey van Langen (Jan 14 2019 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155094056):
That is right, I first wanted to split proving finite and the exact cardinality separately, but realized I could combine the two

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155094142):
If you want to construct a map from `ideal.quotient ...` to the right, look for things called `lift` in the file of ideal quotients.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155094197):
Maybe the easiest way would be to compute the kernel of the `cast : int → zmod n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155094207):
And then use the isomorphism theorem (that we probably don't have :rolling_on_the_floor_laughing:)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey van Langen (Jan 14 2019 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155094270):
We don't have an isomorphism theorem. At least not for rings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey van Langen (Jan 14 2019 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155094320):
```zmod``` may also be ```fin``` since I am not necessarily interested in the ring structure of it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 14 2019 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155094395):
There is already a construction of `zmod n` in `data.zmod.basic`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey van Langen (Jan 14 2019 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155094448):
But there it is not constructed using the integers. The thing on the left naturally arises from a problem I have and I want to relate the two

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey van Langen (Jan 14 2019 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155094468):
Or at least get the necessary result about cardinality of the quotient on the left

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155094806):
I agree that the lemma you state should be proven at some point. So we might as well do it now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey van Langen (Jan 14 2019 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155094821):
This is what I have thus far:
```lean
let nℤ := @span ℤ _ {(n : ℤ)} in
let ℤmodnℤ := ideal.quotient nℤ in
have g : fin n → ℤmodnℤ, from λ m : fin n, ideal.quotient.mk nℤ $ of_nat $ m.val,
have f : ℤ → fin n, from λ x : ℤ,
  { val := nat_abs (x % n),
    is_lt := sorry},
have f' : ℤmodnℤ → fin n, from sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155094902):
I think it is better to prove the isomorphism theorem. Because you will need that time and again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155094956):
@**Chris Hughes** @**Kenny Lau**  Do you have anything in that direction?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 14 2019 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155094967):
I'm not sure on your application, but I think the best way to do quotient rings in Lean is to not prove things about the `quotient` construction, but prove lemmas about quotient rings for any quotient, even if it isn't constructed using the `quot` constant. For example, `ideal.lift`, should have been defined with a type like this.
```lean
def lift {γ : Type*} [comm_ring γ] (f : α → β) [is_ring_hom f] (q : α → γ) [is_ring_hom q] (hq : surjective q) 
  (H : ∀ (a : α), q a = 0 → f a = 0) : γ → β :=
```

Would refactoring the library like this help?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 14 2019 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155095011):
For the cardinality, all you need is the isomorphism theorem on groups, which is already there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155095086):
Aah, if we have it for groups, then proving it for rings shouldn't be too hard. But I agree that we don't need it for the cardinality result.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey van Langen (Jan 14 2019 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155095132):
So working with the predefined group structure on ```zmod n``` should do the trick

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey van Langen (Jan 14 2019 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155095145):
I will try to make that work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155095283):
@**Chris Hughes** Don't you need your `q` to be a ring hom as well?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155095362):
I mean, you can probably define this... But then you can't really prove things about it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155095375):
... without extra assumptions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 14 2019 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155095395):
Yes, I missed that out.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey van Langen (Jan 14 2019 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155095676):
```quote
Would refactoring the library like this help?
```
 I think the current version of lift is fine, as you most often want maps from a quotient

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 14 2019 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155095796):
Why do you need to construct `ℤmodnℤ` using `quotient` instead of using `zmod n`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey van Langen (Jan 14 2019 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155095933):
For finite fields, to show that they are field extensions of some field with p elements, I make use of the natural map from $$\mathbb{Z}$$ to the field which factors over a quotient of that form.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 14 2019 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155096132):
So if you had `lift` with the type I suggested, you could show the field homomorphism directly from `zmodp p hp` instead of mentioning `ideal.quotient` right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey van Langen (Jan 14 2019 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155096375):
I would need to prove that the map to ```zmod p hp``` is surjective, which is I think the difficult part of the proof I want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey van Langen (Jan 14 2019 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155096447):
A priori you do not know that there is a map from ```zmod p hp``` to the field

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 14 2019 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155096521):
There's a proof somewhere that `fin.val` is a one-sided inverse of `int.cast` or perhaps only `nat.cast`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Neil Strickland (Jan 14 2019 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155097440):
I vote in favour of @**Chris Hughes** 's suggestion for refactoring.  I have thought about the technicalities of formalizing a number of arguments, both for arbitrary commutative rings and for rings arising in algebraic topology, and it is clear that the more flexible form of the lift construction will be much more convenient in many places.  The same applies for localisations: instead of a theorem about homomorphisms $A[S^{-1}]\to B$ , there should be an `is_localization` predicate for maps $A\to A'$ and a theorem about maps $A'\to B$ when that predicate is satisfied.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 14 2019 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155100374):
I don't quite understand this yet, but I'd like to [NB `$$ A\to A'$$`for maths mode on Zulip]. Currently given a commutative ring `A` and a submonoid `S` of `A` we have some localisation type `loc A S`plus a proof it's a ring, and the universal property theorems. 

This approach gave me trouble. I was a Lean amateur at the time. I wanted to prove things like $$A[1/f][1/g]=A[1/fg]$$ (that's the mathematician's "=" there -- "canonical isomorphism" if you'd rather) from the universal property and if I remember correctly there was a lot of kerfuffle. See https://github.com/kbuzzard/lean-stacks-project/blob/ad816148cd9292f9205efd2674e180418d2680ec/src/localization_UMP.lean#L230 for example.  In fact https://github.com/kbuzzard/lean-stacks-project/blob/ad816148cd9292f9205efd2674e180418d2680ec/src/localization_UMP.lean#L288 was even worse -- I briefly explain what I was trying to do in the comments above. I was hoping @**Ramon Fernandez Mir** would refactor all this, this month.

Is the idea instead that if $$f:A\to B$$ and $$S\subseteq A$$ then we have a predicate which mathematically means that the induced $$A$$-algebra structure on $$B$$ is isomorphic to $$A[1/S]$$?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 14 2019 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155110131):
Compare with https://github.com/leanprover/mathlib/blob/19e7b1f574d813b9b305b41f8c0820c01bf99c84/analysis/topology/continuity.lean#L379-L382 and how it appears in different statements, including https://github.com/leanprover/mathlib/blob/19e7b1f574d813b9b305b41f8c0820c01bf99c84/analysis/topology/continuity.lean#L934  but not only

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 14 2019 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155121156):
```lean
import ring_theory.ideals

example (n : ℕ) (h : n ≠ 0) : ideal.quotient (ideal.span ({n} : set ℤ)) ≃ fin n :=
{ to_fun := λ x, quotient.lift_on' x (λ i, (⟨int.nat_abs (i%n),
      int.coe_nat_lt.1 $ by rw [int.nat_abs_of_nonneg (int.mod_nonneg _ (int.coe_nat_ne_zero.2 h))]; exact
      int.mod_lt_of_pos _ (int.coe_nat_pos.2 $ nat.pos_of_ne_zero h)⟩ : fin n))
    (λ i j hij, let ⟨k, hk⟩ := ideal.mem_span_singleton.1 hij in fin.eq_of_veq $ show int.nat_abs _ = int.nat_abs _,
      by rw [eq_add_of_sub_eq hk, add_comm, int.add_mul_mod_self_left]),
  inv_fun := λ k, ideal.quotient.mk _ k,
  left_inv := λ x, quotient.induction_on' x $ λ i, quotient.sound' $ ideal.mem_span_singleton'.2 ⟨_,
    show _ = ↑(int.nat_abs (i%n)) - i, by rw [int.nat_abs_of_nonneg (int.mod_nonneg _ (int.coe_nat_ne_zero.2 h)),
      int.mod_def, sub_sub, add_comm, sub_add_eq_sub_sub, sub_self, zero_sub, neg_mul_eq_mul_neg, mul_comm]⟩,
  right_inv := λ k, fin.eq_of_veq $ show int.nat_abs (k.1%n) = _, by rw [← int.coe_nat_mod, int.nat_abs_of_nat, nat.mod_eq_of_lt k.2] }

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155132489):
@**Kevin Buzzard** Yes, this is the idea. Something just like it came up during the mathlib maintenance discussion at lean together, where we had an equality theorem `quotient (separation_setoid A) = (\bot : ideal A).quotient`, IIRC. If we could say that something is a quotient rather than having a quotient construction, then this typal equality could be avoided

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155132583):
Topology already has the notion of a "quotient map" that is already performing this exact thing, we just need to extend it to quotient maps of rings, groups, etc, as well as localization maps and maps for other kinds of constructions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155132712):
Of course we still want the construction - it's no good having theorems about quotient maps if we can't prove they exist - but being able to quantify over things isomorphic to a particular construction is actually a really powerful way to avoid DTT hell

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155132787):
I think we've also talked about having a `euclidean_space A` typeclass that basically means "isomorphic to R^n" which seems silly but is useful for exactly this kind of thing - you don't want to build in a dependence on the precise way a type is constructed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155152420):
Yes, this is exactly why I posted the cryptic link in my previous message in this thread.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155152528):
And I wanted to mention this `quotient (separation_setoid A) = (\bot : ideal A).quotient` (which is [here](https://github.com/leanprover/mathlib/blob/19e7b1f574d813b9b305b41f8c0820c01bf99c84/analysis/topology/quotient_topological_structures.lean#L189)) in my Amsterdam talk but I didn't have time. Note that I did find a workaround in the mean time, but we should still do something more systematic.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155152826):
One big difference between localisations and Euclidean space is that if the $$A$$-algebra $$B$$ is isomorphic to $$A[1/S]$$ as an $$A$$-algebra then it's uniquely isomorphic to $$A[1/S]$$ as an $$A$$-algebra. However if a space is isomorphic to $$\mathbb{R}^n$$ as an $$\mathbb{R}$$-vector space, then there is in general more than one isomorphism, and you may or may not want to keep track of an isomorphism I guess, depending on what you're doing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155155008):
```quote
Is the idea instead that if $$f:A\to B$$ and $$S\subseteq A$$ then we have a predicate which mathematically means that the induced $$A$$-algebra structure on $$B$$ is isomorphic to $$A[1/S]$$?
```
Aah! The penny has just dropped. Instead of the definition of the predicate being "B is isomorphic to the A[1/S] we constructed", it says "B satisfies the universal property we want". Is that the idea? We have predicates for universal properties?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 15 2019 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155155081):
Are all isomorphisms isomorphic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 15 2019 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155155095):
but universal property is not a property... it is a function and has data right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155155118):
Given f:A->B and S in A, the universal property just says that for all A -> C sending S to units, there's a unique B -> C making the diagram commute. Does this have data?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155155163):
Universal property is more than isomorphism, it's unique isomorphism.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 15 2019 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155155170):
of course this has data

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155155174):
?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 15 2019 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155155178):
But modulo `choice` it doesn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155155929):
The data is the unique B -> C that fits

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155155952):
Right, it's constructively data but classically a property, because we also assert that it is unique

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 15 2019 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155155996):
I think we really need a typeclass that is nonempty + subsingleton

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 15 2019 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155156002):
and another that is inhabited+subsingleton

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155156144):
You can't make the map constructively unless you have an explicit inverse for your units. I am unclear about whether as a mathematician I should even care about this discussion. For sure I want something that works if I just know abstractly that something is a unit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155156216):
Generalising Kenny's argument one should have two definitions of unit as well -- existence of an inverse, and the inverse

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 15 2019 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155156249):
```quote
Generalising Kenny's argument one should have two definitions of unit as well -- existence of an inverse, and the inverse
```
 We do... there is `units` and `is_unit`, if I'm not mistaken.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155156625):
Good point about needing to have an actual inverse in order to construct the induced map constructively.
The good news is that any constructively reasonable definition will also be at least usable classically, because you can always conjure up the witness you need using `choice`. The question is what is most convenient.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155156657):
`is_unit a` is defined as `∃u:units α, a = u`, the other version would be with a sigma instead of an exists

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155156939):
```quote
```quote
Is the idea instead that if $f:A\to B$ and $S\subseteq A$ then we have a predicate which mathematically means that the induced $A$-algebra structure on $B$ is isomorphic to $A[1/S]$?
```
Aah! The penny has just dropped. Instead of the definition of the predicate being "B is isomorphic to the A[1/S] we constructed", it says "B satisfies the universal property we want". Is that the idea? We have predicates for universal properties?
```
 In general this is the idea but in some cases you can also give an equivalent but more hands-on description of the predicate, e.g., R -> S being a quotient map of rings can be defined either in terms of a universal property or just as a surjective map.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155157804):
Another way of looking at this is that a map being of the form R -> R/I is something that is either true by definition or not, while a map being a quotient map is a theorem you can *prove* using any methods at your disposal.
The tradeoff is that it's not quite as convenient to use the quotient map hypothesis because you need to pass it to the place it is used, while Lean "just knows" when a ring is defined as a quotient ring.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155159954):
The analogue of `is_surjective` in the localisation situation is not something I think I can write down without simply saying something like "image of $$S$$ lands in the units, and induced map from concrete localisation is a bijection". Is such a predicate useful?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162195):
You can't directly use the universal property as the definition, because of universe issues (it can't quantify over all universes), so you have to find an "internal" characterization roughly equivalent to the construction itself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162213):
*boggle*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162265):
How about "is isomorphic to Kenny's explicit construction" then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 15 2019 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162268):
The `is_quotient ` class could include a truncated inverse to the quotient map.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162293):
I don't even want to use universes. How about I make everything in Type?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162297):
I think for localization it is something like "there is a surjective map from A x S and some additional about it"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162301):
It's much worse than that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162351):
It's "it's what Kenny wrote when he defined localisation"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162361):
you don't need the proofs though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162376):
but you probably need to spell out the equivalence relation again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162385):
you may need the equivalence relation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162392):
but there may also be a way to characterize it via ideals or something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162393):
Kenny's definition of $$A[1/S]$$ is a quotient of $$A\times S$$ by an equivalence relation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162394):
so that it looks more like a universal property

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162441):
So the predicate we need is "it satisfies the universal property that the quotient by an equivalence relation satisfies"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162453):
that is `is_quotient` the way we are going

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162454):
Here $$A\times S$$ is little more than a monoid

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162485):
you might also be able to get away with just maps from A -> loc and S -> loc since it's a ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162542):
or just what you said - a ring hom A -> loc and an assertion that the image of S are units

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155162773):
oh but you still have to say surjective using a map from A x S

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155163051):
If you have that situation, and `(s₁ * r₂ - s₂ * r₁) * t = 0` where `t \in S`, then mapping across `f : A -> loc`, you have `(f s₁ * f r₂ - f s₂ * f r₁) * f t = 0` and `f t` is invertible so `f s₁ * f r₂ = f s₂ * f r₁`, and `f s₁` and `f s₂` are invertible so `f r₁ / f s₁ = f r₂ / f s₂`. So this direction is already provable. The other direction can be asserted: if `f r₁ / f s₁ = f r₂ / f s₂` then there exists `t \in S` such that `(s₁ * r₂ - s₂ * r₁) * t = 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Neil Strickland (Jan 15 2019 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155179691):
I have put some stuff about localization at 
https://github.com/NeilStrickland/lean_comm_alg/blob/master/src/localization.lean
It is not finished, but I would be interested in comments on the general architecture.
The idea is to set things up so that you can make computable maps out of a localisation 
if you have enough data, and you can make non-computable maps if you only have
existence statements, and as much stuff as possible is shared between the two cases.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155182495):
So in your definition of `is_localization` you do *not* write "it satisfies the universal property", you instead write down some explicit ring-theoretic criterion following Mario's suggestion that such a criterion should exist.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155182632):
Whilst I am no Lean expert, I am slightly worried about lines 102-120 because you are defining data in tactic mode, and I think that data constructed in this way usually turns out to be very unwieldy because tactic mode was not really designed for this. Possibly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155182775):
This is totally fake tactic mode, it could be rewritten as a term without any effort.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155182791):
I think it also means that writing it as Neil did should be harmless

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155182932):
I totally agree that it's fake tactic mode. I was less sure than you about whether writing it as Neil did would be harmless.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155182978):
I checked the maths and it seems to me that this does indeed characterise rings isomorphic to the localisation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155183026):
I am still a bit unclear as to why one can't just write "it satisfies the universal property", but I've seen this sort of thing be problematic before.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155183133):
```lean
def submonoid_ann (S : set A) [is_submonoid S] : ideal A := 
{ carrier := λ a, ∃ as : ann_aux S, as.1.1 = a,
  zero := ⟨ann_aux.zero S,rfl⟩,
  add := λ _ _ ⟨⟨⟨a,s⟩,ea0⟩,rfl⟩ ⟨⟨⟨b,t⟩,eb0⟩,rfl⟩, ⟨ann_aux.add S ⟨⟨a,s⟩,ea0⟩ ⟨⟨b,t⟩,eb0⟩,rfl⟩,
  smul := λ a _ ⟨⟨⟨b,t⟩,eb0⟩,rfl⟩, ⟨ann_aux.smul S a ⟨⟨b,t⟩,eb0⟩,begin rw ann_aux.smul,refl,end⟩
}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155183311):
Oh, everything other than `carrier` is a prop anyway, so i'm really fussing about nothing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155183871):
By the way, regarding getting this `is_localization` information around, it can easily be a typeclass (with a not so interesting search problem) and so get this data to where it needs to be

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155184036):
Note that `has_denom_data` is a bit problematic because it is not a subsingleton

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155184467):
```lean
def is_localization_initial 
 (hf : is_localization_data S f) (g : A → C) [is_ring_hom g] (hg : inverts_data S g) 
 : B → C := 
begin
 intro b,
 rcases (hf.has_denom b) with ⟨⟨s,a⟩,e⟩,
 rcases (hg s) with ⟨gsi,e3⟩,
 exact (g a) * gsi,
end
```
Here's another place (the only other place?) where Neil uses tactics to define data.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155184701):
This is even more fake tactic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Neil Strickland (Jan 15 2019 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155184944):
I hadn't heard this kind of deprecation of tactics-for-data before.  It seems to me to be a very natural translation of how I would write definitions in ordinary mathematics.  Is there something that I am missing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155185025):
tactics tend to produce ugly proof terms, which is fine for proofs (well not really, but that's another discussion) and causes problems for defs, because defs are later unfolded and their definitions matter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155185094):
Some tactics are fine and produce exactly what you expect, like `exact` and `intro`, while things like `rw` and `simp` are hell to work with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155185103):
```lean
def is_localization_initial' 
 (hf : is_localization_data S f) (g : A → C) [is_ring_hom g] (hg : inverts_data S g) 
 : B → C := λ b, g (hf.has_denom b).1.2 * (hg (hf.has_denom b).1.1).1
```
This is what I would have written. But I don't understand things well enough to know whether it makes a difference.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155185125):
Because Neil only used `intro`, `rcases` and `exact` maybe it doesn't matter.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155185196):
`rcases` and `cases` will use the corresponding `cases_on` recursor, which is sometimes what you want and sometimes not. We often prefer to use projections when applicable, as in Kevin's version

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155185251):
Neil -- the bottom line is that the sorries you have at the end of the file -- if they are easier to fill in using my suggestion then this is why my suggestion is better, and if they aren't then I'm talking nonsense :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155185363):
You could also use `let ⟨⟨s,a⟩,e⟩ := hf.has_denom b in ...` in place of the `rcases` application, which is more or less the same but produces an auxiliary definition that you can unfold on command. Sometimes this is good, sometimes not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155185377):
```lean
def is_localization_initial 
 (hf : is_localization_data S f) (g : A → C) [is_ring_hom g] (hg : inverts_data S g) 
 : B → C := 
λ b, let ⟨⟨s,a⟩,e⟩ := (hf.has_denom b),
         ⟨gsi,e3⟩ := hg s in (g a) * gsi
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155185387):
Arg, Mario was faster

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155185412):
`set_option eqn_compiler.zeta true`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155185527):
You can also put underscores instead of creating names you won't use

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155185627):
My definition unfolds to ` g (((hf.has_denom b).val).snd) * (hg (((hf.has_denom b).val).fst)).val`, Neil's to
```
subtype.cases_on (hf.has_denom b)
    (λ (val : ↥S × A) (e : f ↑(val.fst) * b = f (val.snd)),
       prod.cases_on val
         (λ (s : ↥S) (a : A) (e : f ↑((s, a).fst) * b = f ((s, a).snd)),
            subtype.cases_on (hg s) (λ (gsi : C) (e3 : g ↑s * gsi = 1), g a * gsi))
         e)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155185828):
Patrick's becomes 
```lean
 is_localization_initial._match_2 S f g hg b (hf.has_denom b)
```
and `is_localization_initial._match_2` becomes 
```
 subtype.cases_on _a
    (λ (val : ↥S × A) (property : f ↑(val.fst) * b = f (val.snd)),
       prod.cases_on val
         (λ (val_fst : ↥S) (val_snd : A) (property : f ↑((val_fst, val_snd).fst) * b = f ((val_fst, val_snd).snd)),
            id_rhs C (is_localization_initial''._match_1 S g val_fst val_snd (hg val_fst)))
         property)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155186036):
What about the defeq equivalence classes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155186066):
Patrick's and Neil's definitions should be defeq, but Kevin's is different

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Neil Strickland (Jan 15 2019 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155186115):
So I have some visible instances of `cases_on` and you don't.  My guess is that the framework for structures effectively defines  `fst` and `snd` in terms of `cases_on`.  But perhaps that's wrong.  And even if it's right, perhaps it is somehow better to bury the call to `cases_on` deeper down.  I don't feel that I understand the issues very well here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155186134):
Me neither, that's why I brought it up here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155186162):
Technically the projections are defined in terms of cases_on, but they are buried really deep and lean has special support for them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155186224):
The `rcases` tactic is getting from `<b,c>` to `b` and `c` using `cases_on`, whereas my direct approach is going from `a:=<b,c>` to `b` using `a.1`. But you're saying that `a.1` is defined using `cases_on` anyway?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155186273):
But it is useful to do the cases late rather than at the beginning because then you can prove things about the shape of the expression even when it's not a pair or whatever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155186357):
To take a simpler example, we've discussed the difference between the definitions 
```
prod.map (f : A -> C) (g : B -> D) : A x B -> C x D | <a, b> := <f a, g b>
```
and
```
prod.map (f : A -> C) (g : B -> D) : A x B -> C x D := \lam p : A x B, <f p.1, g p.2>
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155186509):
The advantage of the second definition is that `prod.map f g p` already unfolds to a pair, while the first definition does not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155186541):
In both cases `prod.map f g <a, b> = <f a, g b>` is definitional

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155186643):
So as an application `(prod.map f g p).1 = f p.1` is definitional only with the second definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155188586):
```lean
instance (hf : is_localization_data S f) (g : A → C) [is_ring_hom g] (hg : inverts_data S g) :
 is_ring_hom (is_localization_initial S f hf g hg) := 
{ map_one := begin 
    unfold is_localization_initial,
    rcases (hf.has_denom 1) with ⟨⟨s,a⟩,h⟩,
    show g a * (hg s).val = 1,
    change f s * 1 = f a at h,
    rw mul_one at h,
    have h2 := (hg s).property,
    have h3 : a - s ∈ ker f,
      show f (a - s) = 0,
      rw is_ring_hom.map_sub f,
      rw h,
      rw sub_self,
    suffices : g a = g s,
      rw this; exact h2,
    have h4 := hf.ker_eq,
    rw h4 at h3,
    cases h3 with t Ht,
    rcases t with ⟨⟨b,t⟩,h5⟩,
    change b = a - s at Ht,
    change b * t = 0 at h5,
    rw Ht at h5,
    rw sub_mul at h5,
    rw sub_eq_zero at h5,
    have h6 : g (a * t) = g (s * t),
      rw h5,
    rw is_ring_hom.map_mul g at h6,
    rw is_ring_hom.map_mul g at h6,
    rcases hg t with ⟨u,hu⟩,
    calc g a = g a * 1 : by rw mul_one
    ...      = g a * (g t * u) : by rw hu
    ...      = (g a * g t) * u : by rw mul_assoc
    ...      = (g s * g t) * u : by rw h6
    ...      = g s * (g t * u) : by rw mul_assoc
    ... = g s : by rw [hu,mul_one]
  end,
...
```
@**Kenny Lau** can you do any better?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155188663):
My bet: yes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155188685):
I wondered whether he would just answer "yes" and leave it at that :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 15 2019 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155188753):
```quote
Technically the projections are defined in terms of cases_on, but they are buried really deep and lean has special support for them
```
 Why doesn't this work?
```lean
example {α β : Type} (x : α × β) : x.fst = prod.rec (λ a b, a) x := rfl -- doesn't work
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155188758):
The question boils down to proving that if $$f(a)=f(s)$$ then $$g(a)=g(s)$$, which looks suspicious until you realise that we know something about the kernel of $$f$$, namely that $$t(a-s)=0$$ for some $$t\in S$$; the fact that $$g(t)$$ is also a unit is what gets us home.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155188921):
Actually I think Kenny would far rather refactor my proof than write his own.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jan 15 2019 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155190260):
@**Chris Hughes** Lean has two type checkers: the kernel and the type context.  The kernel is the small low-level one, and the type context is the high-level one used for tactics, etc., which also supports unification, type class inference, etc.  The kernel only does the final check when you add a theorem to the environment.  Now, the kernel knows that prod.fst is defined in terms of rec, but the type context pretends projections are opaque definitions that only reduce when applied to the `mk` constructor.  With a bit of creativity (i.e., circumventing the type context), you can still prove your example using just rfl:
```lean
run_cmd tactic.add_decl $ declaration.thm `prod.fst_def []
    `(∀ α β : Type, ∀ x : α × β, x.fst = prod.rec (λ a b, a) x)
    (pure `(λ α β : Type, λ x : α × β, eq.refl x.fst))
attribute [_refl_lemma] prod.fst_def

#print prod.fst_def
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 15 2019 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155190559):
@**Kevin Buzzard** mwe?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155190610):
Ramon and me just isolated a lemma, and we now know how to prove `is_ring_hom (is_localization_initial S f hf g hg)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155191027):
The lemma is that if `is_localization_data S f` and `inverts_data S g` then $$f(a)=f(b)\implies g(a)=g(b)$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155191153):
and the proof is that $$a-b$$ is in the kernel of $$f$$ so by `ker_eq` on $$f$$ we know $$s(a-b)=0$$ for some $$s\in S$$; hence $$g(sa)=g(sb)$$, but we can cancel $$g(s)$$ because of `inverts_data S`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155191167):
Everything now follows after some algebra

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155194135):
```quote
@**Kevin Buzzard** mwe?
```
 https://gist.github.com/kbuzzard/b40f8501b311ada3e42b1314f2c0426c

@**Kenny Lau**  -- what is going on here is that Neil has defined a predicate `is_localisation f S` where `f:A -> B` and `S : set A`; the predicate is true iff B is isomorphic to A[1/S]. I just wanted to write the universal property (for all C, if I have h:A -> C such that h(s) is invertible for all s then there's a unique B -> C making the diagram commute) but Mario seems to think that there are universe issues with this approach. Neil has taken a completely different approach, noting that given f : A -> B and the hypothesis that f(s) is a unit for all s in S implies that there's a map A x S - >B sending (a,s) to f(a)/f(s). The claim is that B = A[1/S] in the maths sense iff this map A x S -> B is surjective and the kernel of f : A -> B is the a such that there's s with a*s=0. This is not proved in the file but looks OK to me -- the hypothesis gives a map A[1/S] -> B, the surjectivity claim implies it's surjective, and the kernel claim implies that it's injective.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155194402):
I think @**Ramon Fernandez Mir** might fill in the proofs. I guess we also need that `A -> loc A S` satisfies the predicate -- this might be something which would be easier for you to do.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 15 2019 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155194489):
The universal property is actually more like (forall u: universe, forall C : Type u, ...), but this predicate isn't definable in Lean, so you have to find an equivalent things that doesn't quantify over universes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155194523):
Right -- so I just want to quantify over the universe that A and S are in.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155194567):
Because that's what I do in real live maths in ZFC with no universes -- this "stick to one universe" approach doesn't usually cause me problems.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155195578):
Surely we can prove that the universal property for one universe (if chosen correctly) implies it for all universes, which is a statement we can write down because it only involves prefix quantification of universes, and we can apply it wherever needed when applying the universal property.
(The proof can be that we already constructed the localization within the original universe, so another candidate which has the universal property within that universe must be isomorphic to it, and we know the localization we constructed actually has the universal property for all universes.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155196737):
I just came here to say the same thing. What is wrong with this strategy? Somehow Neil's version seems cleaner though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155197181):
The test case would be to prove that a composition of `is_localization` maps is `is_localization`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155197249):
which should be easy with the universal property

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Neil Strickland (Jan 15 2019 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155197619):
Here are some basic test cases:
1. Can we identity $$A[a^{-1}][b^{-1}]$$ with $$A[(ab)^{-1}]$$?
1. If $$e^2=e$$, can we identify $$A[e^{-1}]$$ with $$A/(1-e)$$?
1. If we define $$\mathbb{Z}_{(p)}$$ as a subring of $$\mathbb{Q}$$, can we produce the ring map $$\mathbb{Z}_{(p)}\to\mathbb{Z}/p$$?
I think that all of the maps implicit in these examples should be computable under very mild assumptions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155198610):
there is nothing wrong with Reid's strategy, it's just less direct and possibly leads to worse defeqs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155198991):
Neil's test 1 came up a lot in the schemes repo.

I guess the idea that everything should be proved constructively and then we just deduce the classical stuff from it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155198995):
Yeah, if you want the constructive version then it's not as nice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155199105):
Do we care about being constructive here? At the very least I would want any constructive version to be a subsingleton like `fintype`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155199157):
also, why the sudden focus on localization? I think the quotient case is far more prevalent and pressing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155199480):
I think the constructive version should use an indexed family rather than a set S

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155199591):
That is, `S` should be the image of a monoid hom rather than a submonoid

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155199598):
because we're refactoring the schemes repo and we had just been trying to make sense of the stuff I wrote about universal properties of localisation, that's why I jumped on this. I had arranged to meet Ramon at 4pm today and Neil's post arrived shortly beforehand so I thought it was a really good time to understand this alternative approach. I think it's beautiful!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155199631):
I think that S should be an arbitrary set, and we should localise at the monoid generated by S.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155199727):
I mean that for constructive purposes you want S to be enumerated by a concrete structure (the domain of the monoid hom). Predicates have no data

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155199740):
Neil was already doing this with $$A[1/ab]$$ etc. When I was doing schemes I had `loc A S` and then `loc A (powers f)` came up so much that Kenny made a bunch of lemmas for it. I am now beginning to wonder whether we should be working in this generality in general.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155199766):
Of course for `powers f` the indexing monoid is just N

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155199803):
I think that demanding that S is a monoid is a pain, because Neil wants me to check that f(s) is invertible for all s in S, and in the case S=<x> I only want to check that f(x) is invertible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155199821):
Sorry for over-use of f there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155199903):
If S = <x> then the analogous monoid hom is `\lam n, add_monoid.smul n x` (which we know is a monoid hom, I think)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155199988):
It also occurred to me that we could just set everything up with monoids, and then write different functions for arbitrary subsets. Mario is suggesting a different generalisation though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155200767):
I think if we actually want to do this we should forget about computation for now, or until we have an actual application

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155201534):
By the way, what happens in the noncommutative case? Is there anything to write down simpler than "the map from the localization is an isomorphism"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155203076):
The real test case for localization is decimal numbers. Can mathlib handle schoolkid maths?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155203475):
noncommutative fields of fractions are really complicated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155203525):
see https://en.wikipedia.org/wiki/Ore_condition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 15 2019 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155206004):
Eew yeah. We number theorists had to learn this stuff about a decade ago when non-commutative Iwasawa theory became a thing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 16 2019 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155231190):
@**Kevin Buzzard** https://github.com/kckennylau/Lean/blob/master/localization_alt.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 16 2019 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155241502):
Neil, your file has been Kennied™.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Neil Strickland (Jan 16 2019 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155242270):
That's great, thanks to @**Kenny Lau** .  I am also working on a slightly different framework which I will report on later.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 16 2019 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/cardinality%20of%20integers%20modulo%20n/near/155245575):
Many thanks @**Kenny Lau** ! Neil, you might either find it instructive to see how Kenny rewired your code, or intimidating, depending on how much you can make sense of it I guess. Kenny will have liked your approach because he is at heart a constructivist.

