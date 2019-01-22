---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/73892maximalfinsetinfinsetoffinsets.html
---

## [new members](index.html)
### [maximal finset in finset of finsets](73892maximalfinsetinfinsetoffinsets.html)

#### [Bryan Gin-ge Chen (Sep 13 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133904539):
Excuse the weird title. I'm trying to prove that a finset of subsets of a finset must contain an element of largest size, without relying on classical choice:
```lean
lemma not_empty_has_max_size {E : finset α} {F : finset (finset α)} :
F ⊆ powerset E → F ≠ ∅ → ∃ x ∈ F, ∀ g ∈ F, card g ≤ card x := sorry
```
Here's my attempt so far, which seems to have taken me down a strange path:
```lean
import data.finset

variable α:Type*
variable [decidable_eq α]

open finset

lemma finset.card_one_eq {E : finset α} : card E = 1 ↔ ∃ a, E = finset.singleton a :=
begin
  have h : _ := @multiset.card_eq_one α E.val,
  unfold card,
  rw [iff_congr h, exists_congr],
  intro a,
  rw [←singleton_val, val_inj],
  refl
end

lemma powerset_empty : powerset (∅ : finset α) = finset.singleton ∅ := rfl

lemma subset_singleton {F : finset (finset α)} :
F ⊆ finset.singleton (∅:finset α) ↔
F = ∅ ∨ F = finset.singleton ∅ :=
begin
  split,
  intro h,
  by_cases h1 : F = ∅,
  exact or.inl h1,
  have : F = finset.singleton ∅ := begin
    sorry
  end,
  sorry,
  intro h,
  exact or.elim h (begin
    intro h1,
    rw h1,
    simp
  end) (begin
    intro h1,
    rw h1,
    simp
  end)
end

lemma not_empty_has_max_size {E : finset α} {F : finset (finset α)} :
F ⊆ powerset E → F ≠ ∅ → ∃ x ∈ F, ∀ g ∈ F, card g ≤ card x :=
begin
  intros FPE Fne,
  induction E using finset.induction with a E ha hE,
  rw [powerset_empty, subset_singleton] at FPE,
  exact or.elim FPE (by contradiction) begin
    intro h,
    exact exists.intro ∅ begin
      rw h,
      exact exists.intro (mem_singleton_self ∅) (begin
        intros g hg,
        rw mem_singleton at hg,
        rw hg
      end)
    end
  end,
  by_cases hh1 : F ⊆ powerset E,
  exact hE hh1,
  sorry
end
```
I'm hoping someone can point me in a smarter direction. Thanks as always!

#### [Reid Barton (Sep 13 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133904686):
Doesn't every finset of finsets contain an element of largest size, regardless of `E` and the associated condition?

#### [Bryan Gin-ge Chen (Sep 13 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133904800):
Maybe, I got worried that without having some kind of bound on the size of the finsets I wouldn't be able to prove it without choice.

#### [Kevin Buzzard (Sep 13 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905022):
just use finset.map (I'm assuming this exists!) on finset.card to get a finset of nats and then take the max and work your way back?

#### [Reid Barton (Sep 13 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905060):
A finset is basically a list, and you could write a program that takes a list of lists and returns one of the maximum length, so there should be no trouble proving it constructively.

#### [Reid Barton (Sep 13 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905178):
Yeah, I was looking for a function on finset which is max after applying a function, but I guess since nat has decidable equality you can use `finset.map` in this case.

#### [Reid Barton (Sep 13 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905214):
Sorry, not `finset.map` but `finset.image`.

#### [Chris Hughes (Sep 13 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905271):
```lean
lemma not_empty_has_max_size {E : finset α} {F : finset (finset α)} :
F ⊆ powerset E → F ≠ ∅ → ∃ x ∈ F, ∀ g ∈ F, card g ≤ card x := 
λ _ h, let ⟨n, hn⟩ := (max_of_ne_empty (mt image_eq_empty.1 h) : ∃ a, a ∈ finset.max (F.image card)) in
let ⟨x, hx₁, hx₂⟩ := mem_image.1 (mem_of_max hn) in 
⟨x, hx₁, hx₂.symm ▸ λ g hg, le_max_of_mem (mem_image.2 ⟨g, hg, rfl⟩) hn⟩
```

#### [Bryan Gin-ge Chen (Sep 13 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905289):
Wow, thanks!

#### [Mario Carneiro (Sep 13 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905350):
That uses decidable_eq, doesn't it?

#### [Kevin Buzzard (Sep 13 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905394):
rofl

#### [Mario Carneiro (Sep 13 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905407):
My suggestion:
```
import data.finset

section
variables {α : Type*} (r : α → α → Prop) [is_preorder α r]
local infix ` ≼ `:50 := r

theorem list_zorn : ∀ l : list α, l ≠ [] → ∃ a ∈ l, ∀ b, a ≼ b → b ≼ a := sorry
theorem finset_zorn : ∀ s : finset α, s ≠ ∅ → ∃ a ∈ s, ∀ b, a ≼ b → b ≼ a := sorry

end
```

#### [Bryan Gin-ge Chen (Sep 13 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905415):
I would have never thought of using finset.image. And yes, decidable_eq is allowed.

#### [Mario Carneiro (Sep 13 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905436):
here the relation is `card s <= card t` on finsets

#### [Kenny Lau (Sep 13 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905447):
```quote
```lean
lemma not_empty_has_max_size {E : finset α} {F : finset (finset α)} :
F ⊆ powerset E → F ≠ ∅ → ∃ x ∈ F, ∀ g ∈ F, card g ≤ card x := 
λ _ h, let ⟨n, hn⟩ := (max_of_ne_empty (mt image_eq_empty.1 h) : ∃ a, a ∈ finset.max (F.image card)) in
let ⟨x, hx₁, hx₂⟩ := mem_image.1 (mem_of_max hn) in 
⟨x, hx₁, hx₂.symm ▸ λ g hg, le_max_of_mem (mem_image.2 ⟨g, hg, rfl⟩) hn⟩
```
```
what is the role of E in your theorem?

#### [Kevin Buzzard (Sep 13 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905450):
you can just prove this using the zorn in mathlib

#### [Mario Carneiro (Sep 13 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905467):
of course, but this (1) doesn't use nonconstructive axioms and (2) doesn't need the chain condition

#### [Bryan Gin-ge Chen (Sep 13 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905518):
If E is unnecessary here all the better. In the "application", it's the ground set of a matroid.

#### [Reid Barton (Sep 13 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905536):
`decidable_eq nat` doesn't use axioms either

#### [Mario Carneiro (Sep 13 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905569):
yes, but the theorem can be proven constructively without that assumption

#### [Reid Barton (Sep 13 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905579):
Yeah, the max/min stuff should be on multisets.

#### [Mario Carneiro (Sep 13 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905596):
Unfortunately, here max/min don't work directly since it's not a poset

#### [Kenny Lau (Sep 13 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905633):
{% raw %}
you can have zorn on a set (i.e. type) S as long as you have a choice function on P(P(S))\{{}}, right{% endraw %}

#### [Mario Carneiro (Sep 13 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905662):
yes, but we don't have that here and I claim it's still provable

#### [Kenny Lau (Sep 13 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905694):
sure

#### [Reid Barton (Sep 13 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905726):
I mean we should just define `max` for a set in the same style as `prod`, in terms of `max` on multiset, and nat is already a decidable linear whatever so there would be no problem there.
```lean
protected def prod [comm_monoid β] (s : finset α) (f : α → β) : β := (s.1.map f).prod
```

#### [Mario Carneiro (Sep 13 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905781):
what is this about `nat`? I don't see it in the question

#### [Reid Barton (Sep 13 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905798):
`nat` is the codomain of `finset.card` (I assume)

#### [Mario Carneiro (Sep 13 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905829):
sure but that doesn't really matter; we are doing the choosing on `finset A` which is not decidable (unless you assume so)

#### [Mario Carneiro (Sep 13 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905887):
all that decidability of nat gives you is decidability of the relation `≼` given by `s ≼ t ↔ card s ≤ card t`

#### [Kenny Lau (Sep 13 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905902):
I guess Kevin ran away from all this decidable nonsense :P

#### [Reid Barton (Sep 13 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905936):
I'm a bit confused.
All I am saying is that the original thing should be a direct conclusion of some lemma about `max` of a `multiset nat`, applied to `F.1.map finset.card`.

#### [Reid Barton (Sep 13 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906034):
That lemma being the analogue for multisets of `finset.max_of_ne_empty` and `finset.le_max_of_mem`

#### [Reid Barton (Sep 13 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906232):
But I guess maybe `decidable_linear_order` is stronger than `decidable_eq` anyways, so it doesn't really matter.

#### [Mario Carneiro (Sep 13 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906443):
the point is this isn't a question about decidable linear orders, but decidable preorders. Lack of uniqueness of the maximum makes it hard to define a function like `max` directly

#### [Reid Barton (Sep 13 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906534):
You mean something like a "pre-total order"?

#### [Mario Carneiro (Sep 13 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906805):
`is_total_preorder` exists in core btw

#### [Mario Carneiro (Sep 13 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906808):
but totality is not needed

#### [Reid Barton (Sep 13 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906861):
Finding the maximum value of a function on a finite set is a pretty standard thing to do. Of course there might not be a unique element of the set which maximizes the function, but the maximum value of the function is still well-defined. And often you only need some statement about the existence of a maximizing element.
It's not very obvious how you're supposed to get this from only the ability to take the maximum element of a finite set (in a totally ordered type).

#### [Mario Carneiro (Sep 13 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906917):
like kenny and chris have shown, you can take the image of the finset and get the maximum

#### [Mario Carneiro (Sep 13 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906965):
unless you care about  constructivity and then you have to prove it from scratch

#### [Mario Carneiro (Sep 13 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906991):
that works in any total preorder

#### [Mario Carneiro (Sep 13 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133907005):
in a partial order, I don't see any easy way to get it except zorn's lemma

#### [Kenny Lau (Sep 13 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133907255):
```quote
like kenny and chris have shown, you can take the image of the finset and get the maximum
```
I don't think I did anything

#### [Bryan Gin-ge Chen (Sep 13 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133907303):
I care a little bit about constructivity, but maybe I'll see how far I can get with Chris's solution first.

#### [Mario Carneiro (Sep 13 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133909339):
oops, I didn't see that you just quoted chris's solution

