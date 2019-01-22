---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/64802provingsizeatleast3.html
---

## [maths](index.html)
### [proving size at least 3](64802provingsizeatleast3.html)

#### [Kevin Buzzard (Aug 13 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132037729):
I would be interested in a relatively slick proof of either of the below examples:

```lean
import data.fintype
import set_theory.cardinal

-- fintype
open fintype
example (α : Type) [fintype α] (a b c : α) (Hab : a ≠ b) (Hbc : b ≠ c) (Hac : a ≠ c) :
card α ≥ 3 := sorry

-- general
example (α : Type) (a b c : α) (Hab : a ≠ b) (Hbc : b ≠ c) (Hac : a ≠ c) :
cardinal.mk α ≥ 3 := sorry
```
This is for pedagogical purposes and I don't really mind if we stick to fintypes or not.

As a side issue, is `cardinal.mk` really the way to talk about the cardinality of a type? Is there not some interface function?

#### [Mario Carneiro (Aug 13 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132037883):
`cardinal.mk` is the interface function

#### [Kenny Lau (Aug 13 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132038796):
```lean
import data.fintype
import set_theory.cardinal

@[derive decidable_eq]
inductive three : Type
| A : three
| B : three
| C : three

open three

instance : fintype three :=
{ elems := {A, B, C},
  complete := λ x, by cases x; simp }

theorem three.cardinal : cardinal.mk three = 3 :=
(cardinal.fintype_card three).trans $
show ((3 : nat) : cardinal) = 3, by simp

-- fintype
open fintype
example (α : Type) [fintype α] (a b c : α) (Hab : a ≠ b) (Hbc : b ≠ c) (Hac : a ≠ c) :
  card α ≥ 3 :=
show card three ≤ card α, from
card_le_of_injective (λ n, three.rec_on n a b c) $
λ x y h, by cases x; cases y; dsimp at h; cc

-- general
example (α : Type) (a b c : α) (Hab : a ≠ b) (Hbc : b ≠ c) (Hac : a ≠ c) :
cardinal.mk α ≥ 3 :=
three.cardinal ▸ nonempty.intro ⟨λ n, three.rec_on n a b c,
λ x y h, by cases x; cases y; dsimp at h; cc⟩
```

#### [Mario Carneiro (Aug 13 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132038797):
hm, I needed some additional library functions for this, attached. The main proof is not so hard:
```lean
@[simp] lemma fintype.card_coe (s : finset α) :
  fintype.card (↑s : set α) = s.card := card_attach

theorem card_le_of_finset {α} (s : finset α) :
  (s.card : cardinal) ≤ cardinal.mk α :=
begin
  rw (_ : (s.card : cardinal) = cardinal.mk (↑s : set α)),
  { exact ⟨function.embedding.subtype _⟩ },
  rw [cardinal.fintype_card, fintype.card_coe]
end

-- fintype
open fintype
example (α : Type) [fintype α] (a b c : α) (Hab : a ≠ b) (Hbc : b ≠ c) (Hac : a ≠ c) :
  card α ≥ 3 :=
finset.card_le_of_subset (finset.subset_univ ⟨a::b::c::0, by simp *⟩)

-- general
example (α : Type) (a b c : α) (Hab : a ≠ b) (Hbc : b ≠ c) (Hac : a ≠ c) :
  cardinal.mk α ≥ 3 :=
begin
  suffices : ((3:ℕ) : cardinal) ≤ cardinal.mk α, {simpa},
  exact card_le_of_finset ⟨a::b::c::0, by simp *⟩
end
```

#### [Kenny Lau (Aug 13 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132038801):
just 3 seconds apart!

#### [Kevin Buzzard (Aug 13 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132063967):
Thanks to both of you! [I've only just seen these].

#### [Kevin Buzzard (Aug 14 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132075090):
This is one of those "easy in maths, hard in Lean" moments :-/ I am going to need stuff like "card X = 3 iff there exists a,b,c all distinct and every element of X must be a, b or c" [but I've gotta scoot]. I think I can take it from here but this is all a bit ugly. Mathematicians are so good at 3 :-/

#### [Mario Carneiro (Aug 14 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132084120):
that latter fact is essentially exactly the definition of a fintype instance where the underlying multiset has three elements

#### [Kevin Buzzard (Aug 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132131438):
Here's a proof for the cardinal case:

```lean
import set_theory.cardinal

lemma three (α : Type) (Hthree : cardinal.mk α = 3) :
  ∃ a b c : α, a ≠ b ∧ b ≠ c ∧ c ≠ a ∧ ∀ d : α, d = a ∨ d = b ∨ d = c :=
begin
  rw ←(show cardinal.mk (fin 3) = 3, by simp) at Hthree,
  cases (quotient.exact Hthree) with Hequiv,
  let a := Hequiv.symm 0,let b := Hequiv.symm 1,let c := Hequiv.symm 2,
  have H12 : a ≠ b := by simp [Hequiv];exact dec_trivial,
  have H23 : b ≠ c := by simp [Hequiv];exact dec_trivial,
  have H31 : c ≠ a := by simp [Hequiv];exact dec_trivial,
  existsi a,existsi b,existsi c,
  refine ⟨H12,H23,H31,λ d,_⟩,
  cases H : (Hequiv d) with n Hn,
  cases n with e He,
    left,show d = Hequiv.symm ⟨0,Hn⟩,rw ←H,simp,
  cases e with e He,
    right,left,show d = Hequiv.symm ⟨1,Hn⟩,rw ←H,simp,
  cases e with e He,
    right,right,show d = Hequiv.symm ⟨2,Hn⟩,rw ←H,simp,
  exfalso,apply not_le_of_gt Hn,exact dec_trivial,
end
```

Now I need to do `four` :cry: (but that's the last one)

#### [Mario Carneiro (Aug 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132131694):
noo... my heart, it hurts

#### [Mario Carneiro (Aug 14 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132131735):
`n` is easier than `3`

#### [Kevin Buzzard (Aug 14 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132131957):
So 4 is easier than 3? :-)

#### [Mario Carneiro (Aug 14 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132131963):
3 is easier than 3

#### [Kevin Buzzard (Aug 14 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132132062):
I did think about doing the general case but at the end of the day I want to extract exactly those things in the conclusion, and I wasn't entirely sure how easy it would be if I had a list of size n or whatever, so I decided to bite the bullet now rather than later.

#### [Mario Carneiro (Aug 14 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132132086):
trust me, it's way easier to conclude from the general statement, even if the final goal is exactly the statement you wrote

#### [Mario Carneiro (Aug 14 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132132147):
hint: if you have a list of length 3, then you can `match` it against `[a, b, c]`

#### [Kevin Buzzard (Aug 14 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132132148):
I was a bit surprised to see `simp` leave me with a goal `not 0 = 1` in the H12 proof.

#### [Mario Carneiro (Aug 14 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132132170):
and `d \in [a, b, c]` and `list.nodup [a, b, c]` will simplify to the disjunctions you wrote

#### [Kevin Buzzard (Aug 14 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132132192):
This is the stupid cardinal version, because Richard Thomas complained that I was assuming unnecessary finiteness hypotheses.

#### [Mario Carneiro (Aug 14 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132132241):
there are theorems showing equivalence to the finite versions in `cardinal`

#### [Kevin Buzzard (Aug 14 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132132253):
Oh OK, maybe I'll take it from here. Thanks!

#### [Kevin Buzzard (Aug 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132132278):
It's just my lack of experience which made me do the 3 case explicitly. I could see I could try for the n case, but I figured that doing the 3 case directly would be less painful. I guess your instincts immediately told you otherwise.

#### [Mario Carneiro (Aug 14 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving size at least 3/near/132132331):
even 2 is sometimes tricky, but certainly `2 < n < 3`

