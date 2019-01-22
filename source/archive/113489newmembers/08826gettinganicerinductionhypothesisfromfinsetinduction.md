---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/08826gettinganicerinductionhypothesisfromfinsetinduction.html
---

## [new members](index.html)
### [getting a nicer induction hypothesis from finset.induction](08826gettinganicerinductionhypothesisfromfinsetinduction.html)

#### [Bryan Gin-ge Chen (Sep 24 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/getting%20a%20nicer%20induction%20hypothesis%20from%20finset.induction/near/134558327):
I'm working on formalizing a proof where the idea is to induct on the size of $$Y \setminus X$$ for two finsets $$X, Y$$. I've currently set up something like the following:
```lean
import data.finset

open finset
variables {α : Type*} [decidable_eq α] {E : finset α}

def r {X : finset α} (hX : X ⊆ E) : ℕ := sorry

theorem foo {X Y : finset α} (hX : X ⊆ E) (hY : Y ⊆ E) :
  r (union_subset hX hY) = r hX := 
begin
  induction h : (Y \ X) using finset.induction with a S ha ih,
  /-
  case h₁
  α : Type u_1,
  _inst_1 : decidable_eq α,
  E X Y : finset α,
  hX : X ⊆ E,
  hY : Y ⊆ E,
  h : Y \ X = ∅
  ⊢ r _ = r hX
  -/
  -- I have handled the empty case
  sorry,
  /- 
  case h₂
  α : Type u_1,
  _inst_1 : decidable_eq α,
  E X Y : finset α,
  hX : X ⊆ E,
  hY : Y ⊆ E,
  a : α,
  S : finset α,
  ha : a ∉ S,
  ih : Y \ X = S → r _ = r hX, -- How do I use this?
  h : Y \ X = insert a S
  ⊢ r _ = r hX
  -/
  sorry
end
```
The current `ih`, which in full form reads `ih : Y \ X = S → r (union_subset hX hY) = r hX`, seems impossible to for me to apply since it requires `Y \ X = S`, but we have `h : Y \ X = insert a S`. I suspect I'm abusing the tactic here, since the target doesn't contain `Y \ X` in it directly. I would be happy and the theorem would be proved if I had instead `ih : r (union_subset hX hS) = r hX` where `hS : S  ⊆ E` (and the rest of the tactic state the same).  Is there some way to set that up?

#### [Bryan Gin-ge Chen (Sep 25 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/getting%20a%20nicer%20induction%20hypothesis%20from%20finset.induction/near/134565383):
I managed to massage the goal so that now `ih : Y \ X = S → r hXuY' = r hX` where `hXuY' : X ∪ Y \ X ⊆ E`. This seems closer though I'm still not sure if my current approach is going anywhere or not. Not that I could apply this here yet, but is there any way to take a term of type `a = b → P a`and produce `P b`?

#### [Mario Carneiro (Sep 25 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/getting%20a%20nicer%20induction%20hypothesis%20from%20finset.induction/near/134565694):
You need to generalize `Y` and `X` in the induction

#### [Mario Carneiro (Sep 25 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/getting%20a%20nicer%20induction%20hypothesis%20from%20finset.induction/near/134565749):
Why are you working on subsets of a finset `E` instead of just restricting the type?

#### [Mario Carneiro (Sep 25 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/getting%20a%20nicer%20induction%20hypothesis%20from%20finset.induction/near/134565754):
You could just assume `fintype α`

#### [Bryan Gin-ge Chen (Sep 25 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/getting%20a%20nicer%20induction%20hypothesis%20from%20finset.induction/near/134566466):
Ah, so that's what `generalizing` does! I wasn't able to make sense of that part of the docstring. As for fintype, I can see that will make things much easier. I just kind of rushed ahead without looking beyond `finset` when I started this. Thanks!

