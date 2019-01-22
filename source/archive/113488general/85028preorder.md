---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85028preorder.html
---

## [general](index.html)
### [preorder](85028preorder.html)

#### [Kevin Buzzard (Sep 03 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder/near/133250860):
```lean
class preorder (α : Type u) extends has_le α, has_lt α :=
(le_refl : ∀ a : α, a ≤ a)
(le_trans : ∀ a b c : α, a ≤ b → b ≤ c → a ≤ c)
(lt := λ a b, a ≤ b ∧ ¬ b ≤ a)
(lt_iff_le_not_le : ∀ a b : α, a < b ↔ (a ≤ b ∧ ¬ b ≤ a) . order_laws_tac)
```

I just want to check I've got this right. The `lt` field does not even seem to document its type, but given that we have an example of how to fill it in, we can infer the type. The `lt_iff_le_not_le` field demands that `lt a b` is logically equivalent to `(a ≤ b ∧ ¬ b ≤ a)`, so from a mathematician's point of view it may as well be defined to be `λ a b, a ≤ b ∧ ¬ b ≤ a`. However from a computer scientist's point of view they might want some other algorithm for computing `<` and then a theorem saying it's equivalent. The `order_laws_tac` thing -- this is some tactic, which presumably is a beefed-up version of `exact iff.refl`. Mathematicians could hence simply completely ignore the last two fields when getting a feel as to what a preorder is (I am more used to partial orders). A preorder is just a category whose objects are terms of alpha and for which there is at most one morphism between any two objects; it's weaker than a partial order because there can be objects which are isomorphic but not equal. A Galois connection is no more and no less than a pair of adjoint functors between two such categories. Have I got all this straight?

#### [Kevin Buzzard (Sep 03 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder/near/133252175):
Why are the maps called `l` and `u` in the Galois connection stuff? `l` and `r` I would understand...

#### [Kevin Buzzard (Sep 03 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder/near/133252362):
What does `notation `⨆` binders `, ` r:(scoped f, supr f) := r` mean?

#### [Johan Commelin (Sep 03 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder/near/133252436):
I think it was `l`ower and `u`pper?

#### [Johan Commelin (Sep 03 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder/near/133252453):
But also `l`eft and `u`nderlying...

#### [Johannes Hölzl (Sep 03 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder/near/133252862):
Yes `l` for lower, and `u` for upper. But left and underlying is also nice
I don't understand the `notation`-syntax myself. This specific case sets up `⨆` to behave like a lambda, and put a `supr` around it.
I.e. `(⨆a, f a) := supr (λa, f a)`

#### [Johannes Hölzl (Sep 03 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder/near/133252917):
That we want to overwrite `<` is not necessary due to more efficient computation, but sometimes also easier proofs. For example for nat it is defined to be `a < b := nat.succ a <= b`

#### [Reid Barton (Sep 03 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/preorder/near/133254462):
Kevin what you say is right. Also worth noting is that every preorder has a canonical equivalence (in the category theory sense) to a poset, so there's not much harm in treating posets and preorders as the same thing.

