---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/11831defsyntax.html
---

## Stream: [new members](index.html)
### Topic: [def syntax](11831defsyntax.html)

---

#### [Alexandru-Andrei Bosinta (Nov 21 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148134203):
Is there a way to make a definition with a condition that is not decidable? I need something like 
```
def my_def := if p then sorry
else sorry
```
but with `p` not decidable.

#### [Johannes Hölzl (Nov 21 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148135957):
the easiest option is to activate classical logic in your `section` or on the module level:
```lean
local attribute [instance] classical.prop_decidable
```
add this to the top of your file

#### [Kevin Buzzard (Nov 21 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148135962):
```lean
local attribute [instance, priority 0] classical.prop_decidable

noncomputable def my_def (p : Prop) : ℕ := if p then sorry
else sorry
```

#### [Johannes Hölzl (Nov 21 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148135985):
ah yes, `priority 0` is a good idea

#### [Alexandru-Andrei Bosinta (Nov 21 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148136595):
Thanks for the idea, but also how do I give my condition a name so I can use it in the definition?
```
protected noncomputable def neg (α : ℝ) : ℝ := if ∃ (p : ℚ), α = lt_rat_r p then sorry
else sorry
```
This is what I am trying to do, and I need to give a name to my condition so I can use it in the definition.

#### [Kevin Buzzard (Nov 21 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148136656):
Maybe you want `dite`? "dependent if/then/else"

#### [Rob Lewis (Nov 21 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148136673):
`if h : p then _ else _`

#### [Alexandru-Andrei Bosinta (Nov 21 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148137486):
```quote
`if h : p then _ else _`
```
 Oh, thanks. I was trying to do something like this but I was putting too many parenthesis and Lean was complaining. (I was trying to use `(h : p)`)

#### [Alexandru-Andrei Bosinta (Nov 21 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148137657):
```quote
Maybe you want `dite`? "dependent if/then/else"
```
 `dite` also works, but I think I will use @**Rob Lewis**'s version for this. Also thanks for this function, I didn't know about it. It seems it can be pretty useful.

#### [Rob Lewis (Nov 21 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148138067):
`if h : p then _ else _` is actually just nicer syntax for `dite`.

#### [Alexandru-Andrei Bosinta (Nov 21 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148140541):
Is there a way to make the conditional an `∃` and then extract the element? It seems like `exists.elim` will not work here because it expects a `Prop` at the end (so it only works for proving propositions).

#### [Patrick Massot (Nov 21 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148140724):
use `classical.some`

#### [Patrick Massot (Nov 21 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148140739):
but beware that you don't get much control over which element will be returned

#### [Patrick Massot (Nov 21 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148140835):
and of course your function won't be computable

#### [Patrick Massot (Nov 21 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148140845):
Maybe it would help, if you could tell us more about what you are actually trying to do

#### [Alexandru-Andrei Bosinta (Nov 21 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148140975):
Thanks! `classical.some` worked. I did notice the problem that you don't get much control over which element will be returned (so my first attempt to use it failed), but I managed to make it work.

#### [Patrick Massot (Nov 21 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148141013):
It's important to understand that proof irrelevance makes it impossible to prove existence using some witness and hope to get back this witness using `some`. But that wouldn't make much sense in real world math either

#### [Patrick Massot (Nov 21 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148141147):
I mean
```lean
import tactic.norm_num
open classical
def h : ∃ a : ℕ, a ≠ 0 := ⟨42, by norm_num⟩

example : some h = 42 := sorry -- no hope
```
is hopeless (and honestly it wouldn't make sense)

#### [Alexandru-Andrei Bosinta (Nov 21 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148141536):
I understand what you mean, but I don't need to prove an existence. I am only doing the law of the excluded middle over a proposition of the type ` ∃ (x : ℚ), p x` with `p : ℚ → Prop`. So I am only using `some` to get the witness and use it in the proof, but I don't care what is the witness, so I won't use `some` to get it back.

#### [Patrick Massot (Nov 21 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148141768):
Good. I still advise you to post your code when you'll be done. It's easy to do suboptimal things in this area, and you may learn useful stuff from reactions here.

#### [Alexandru-Andrei Bosinta (Nov 21 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148141840):
Ok, I will post it here when I am done.

#### [Alexandru-Andrei Bosinta (Nov 22 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148147423):
```
import data.rat data.set.basic order.bounds tactic.ring
open classical
local attribute [instance, priority 0] classical.prop_decidable

structure Dedekind_real :=
(carrier : set ℚ)
(nonemp : ∃ a, a ∈ carrier)
(nonrat : ∃ a, a ∉ carrier)
(down : ∀ (p : ℚ), p ∈ carrier → ∀ (q : ℚ), q ≤ p → q ∈ carrier)
(nomax : ∀ (p : ℚ), p ∈ carrier → ∃ (q : ℚ), q ∈ carrier ∧ p < q)

notation `ℝ` := Dedekind_real

instance : has_coe ℝ (set ℚ) := ⟨λ r, r.carrier⟩

namespace Dedekind_real

protected def le (α β : ℝ) : Prop := (α : set ℚ) ⊆ β

instance : has_le ℝ := ⟨Dedekind_real.le⟩

end Dedekind_real

open Dedekind_real

lemma bounded_by_non_elements (α : ℝ) (x : ℚ): x ∉ α.carrier ↔ (∀ (q : ℚ), q ∈ α.carrier → q < x) := sorry

lemma real_intro : ∀ {a b : ℝ}, a.carrier = b.carrier → a = b := sorry

theorem not_exists_not_c {α : Type} {p : α → Prop} : (¬∃ (x : α), ¬p x) ↔ ∀ (x : α), p x := sorry

namespace Dedekind_real

def lt_rat_r (p : ℚ) : ℝ := ⟨{q | q < p}, sorry, sorry, sorry, sorry ⟩

protected noncomputable def neg (α : ℝ) : ℝ := if h : ∃ (p : ℚ), α = lt_rat_r p then lt_rat_r (some h)
else ⟨{p : ℚ | ∀ (q : ℚ), q ∈ α.carrier → p + q < 0}, 
exists.elim α.nonrat (λ r hr, ⟨-r, (λ q hq, neg_add_lt_of_lt_add (trans_rel_left rat.has_lt.lt 
( (bounded_by_non_elements α r).mp hr q hq) (eq.symm (add_zero r) ) ) ) ⟩ ),    
(classical.by_contradiction (λ h, exists.elim α.nonemp (λ q0 hq0, (not_lt_of_lt (trans_rel_left rat.has_lt.lt
(lt_add_one 0) (zero_add 1) ) ) (trans_rel_right rat.has_lt.lt (eq.symm (sub_add_cancel 1 q0) ) 
(not_exists_not_c.mp h (1-q0) q0 hq0) ) ) ) ), 
(λ p hp q hqp r hrα, lt_of_le_of_lt ((add_le_add_iff_right r).mpr hqp) (hp r hrα) ),
(λ p hp, dite (∃ (ε : ℚ), (ε < 0 ∧ ∀ (q : ℚ), q ∈ α.carrier → p + q < ε) ) 
(λ hε, exists.elim hε (λ ε hε, ⟨p-ε/2, (λ q hq, sorry), sorry⟩))
(λ hε, false.elim (h ⟨-p, real_intro (set.ext (λ x, 
⟨(λ hx, by calc x = -p + (p + x) : by ring
... < -p + 0 : add_lt_add_left (hp x hx) (-p)
... = -p : by ring),
(λ hx, sorry)⟩ ) ) ⟩ ) ) ) ⟩

end Dedekind_real
```
I am not done yet (I skipped some tedious calculations: the three `sorry` in the definition of `neg`; I know how to do them, but it seems extremely tedious to do in Lean), but this is what I have. To remove clutter, I removed most of the things irrelevant to this particular definition and added `sorry` instead of my written proofs for other theorems which are required.

I am starting to think that I am doing something wrong because this is getting way too tedious.

#### [Kenny Lau (Nov 22 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/def%20syntax/near/148182360):
There is a way to make this computable.

