---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/01478easyproofofsurjectiveiffinjective.html
---

## Stream: [maths](index.html)
### Topic: [easy proof of surjective_iff_injective](01478easyproofofsurjectiveiffinjective.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 06 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124726537):
Is there an easy proof of 
```lean
lemma  injective_iff_surjective [fintype α] {f : α → β} (e : α ≃ β) : injective f ↔  surjective f
```
 It took me 40 lines, but with stuff like this, there's often some one or two line proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124726662):
I have no idea whether this maths idea is easily leanified, but using e you can build a map alpha -> alpha (f then e to get you back to alpha), and if the collection of all such maps alpha -> alpha is known to be a fintype then you know there must exist nats `a<b` with f^a = f^b (f^n = f composed with itself n times).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124726668):
Now under either the injectivity or the surjectivity assumption you can deduce f^{b-a} = id

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124726669):
and then f^{b-a-1} is the inverse

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 06 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124727085):
Sounds very doable. I'm not sure there's a power function on functions yet though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 06 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124733354):
Longer, but cooler
```lean
instance fun.monoid {α : Type*} : monoid (α → α) :=
{ mul := (∘),
  mul_assoc := λ _ _ _, rfl,
  one := id,
  one_mul := λ _, rfl,
  mul_one := λ _, rfl }

lemma eq_of_left_inv_of_right_inv [monoid α] {a b c : α} 
    (h₁ : a * b = 1) (h₂ : c * a = 1) : b = c := 
have h₃ : c  * a * b = c * 1 := by rw [← h₁, mul_assoc],
by rwa [h₂, one_mul, mul_one] at h₃

lemma pow_mul_pow_eq_one [monoid α] {a b : α} : ∀ n, a * b = 1 → a^n * b^n = 1
| 0     := λ h, one_mul _
| (n+1) := λ h, 
  by rw [pow_succ', _root_.pow_succ, mul_assoc, ← mul_assoc a, h, one_mul];
  exact pow_mul_pow_eq_one n h

lemma mul_eq_one_of_mul_eq_one [fintype α] [monoid α] 
    (a b : α) (h : a * b = 1) : b * a = 1 := 
have hmn : ∃ m n, m ≠ n ∧ a^n = a^m :=
by_contradiction $ λ h, set.not_injective_nat_fintype 
(show injective (monoid.pow a), from
λ m n h₁, by_contradiction $ λ h₂, h ⟨m, n, h₂, h₁.symm⟩),
let ⟨m, n, hmn₁, hmn₂⟩ := hmn in
begin
  clear _let_match,
  wlog hn : n ≤ m using n m,
  have : 0 < m - n := nat.sub_pos_of_lt (lt_of_le_of_ne hn hmn₁.symm),
  have h₁ : a^n * b^n = a^(m - n) * a^n * b^n :=
    by rw [← _root_.pow_add, nat.sub_add_cancel hn, hmn₂],
  rw [mul_assoc, pow_mul_pow_eq_one _ h, mul_one, ← succ_pred_eq_of_pos
      this, pow_succ'] at h₁,
  rw [eq_of_left_inv_of_right_inv h h₁.symm, h₁],
end

lemma surjective_iff_injective [fintype α] {f : α → α} : injective f ↔ surjective f :=
or.cases_on (classical.em (nonempty α)) 
  (λ ⟨a⟩, ⟨λ hinj, surjective_of_has_right_inverse $ 
    let ⟨g, hg⟩ := @injective.has_left_inverse _ ⟨a⟩ _ _ hinj in
    ⟨g, λ x, show (f * g) x = x, by rw mul_eq_one_of_mul_eq_one 
        g f (id_of_left_inverse hg); refl⟩, 
  λ hsurj, injective_of_has_left_inverse $ 
    let ⟨g, hg⟩ := surjective.has_right_inverse hsurj in
    ⟨g, λ x, show (g * f) x = x, by rw mul_eq_one_of_mul_eq_one 
        f g (id_of_right_inverse hg); refl⟩⟩) 
(λ h, ⟨λ _ a, false.elim (h ⟨a⟩), λ _ a, false.elim (h ⟨a⟩)⟩)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 06 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124733504):
Some of the monoid stuff is there already actually.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124734102):
I agree it's cooler, in the sense that you seem here to be proving what look like fundamental facts about monoids. Dumb question:  is there some infinite monoid for which an element can have a left inverse which is not a right inverse?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124734144):
That's the sort of question asked by someone who does not have a good enough collection of monoids in their brain

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 06 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124734460):
Yes. `pred` and `succ` are a perfect example of this: `pred (succ n) = n` but `succ (pred n) != n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124736849):
Aah, endomorphisms of an arbitrary set are a monoid.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124736923):
I see. In fact a category with one object is the same thing as a monoid, and an example of a category with one object is take your favourite algebraic structure and consider structure-preserving endomorphisms of an object with that structure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124736932):
Here we have the simple case of a set, i.e. no algebraic structure at all.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124736947):
well, maybe "the empty algebraic structure" is a better way of saying it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124737052):
so this (succ and pred) is a proof that the naturals are not a fintype.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124737895):
actually, that's circular, because Chris (and me!) uses the fact that they're infinite in the proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124737952):
Oh, +1 for use of wlog ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 06 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124737978):
Was `wlog` hard to use?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124738032):
No, it's just such a natural maths thing to use and it wasn't there a few weeks ago :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124738034):
So just the opposite really.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 06 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124738150):
Glad to hear it :)


{% endraw %}
