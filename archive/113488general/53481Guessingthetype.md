---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53481Guessingthetype.html
---

## Stream: [general](index.html)
### Topic: [Guessing the type](53481Guessingthetype.html)

---

#### [Alexandru-Andrei Bosinta (Nov 21 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Guessing%20the%20type/near/148130635):
```
import data.rat
open classical

structure Dedekind_real :=
(carrier : set ℚ)
(nonemp : ∃ a, a ∈ carrier)
(nonrat : ∃ a, a ∉ carrier)
(down : ∀ p ∈ carrier, ∀ q, q ≤ p → q ∈ carrier)
(nomax : ∀ p ∈ carrier, ∃ q, q ∈ carrier ∧ p ≤ q ∧ p ≠ q)

notation `ℝ` := Dedekind_real

instance : has_coe ℝ (set ℚ) := ⟨λ r, r.carrier⟩

namespace Dedekind_real

protected def le (α β : ℝ) : Prop := (α : set ℚ) ⊆ β
instance : has_le ℝ := ⟨Dedekind_real.le⟩

end Dedekind_real

open Dedekind_real

lemma le_total_r : ∀ a b : ℝ, a ≤ b ∨ b ≤ a := λ a b, (em (∃ x, x ∈ a.carrier ∧ x ∉ b.carrier)).elim 
sorry (λ h, or.inl (λ x hxa, classical.not_not.1 (not_and.1 ( (@not_exists ℚ _).1 h x) hxa) ) )  

/-
lemma le_total_r' : ∀ a b : ℝ, a ≤ b ∨ b ≤ a := λ a b, (em (∃ x, x ∈ a.carrier ∧ x ∉ b.carrier)).elim 
sorry (λ h, or.inl (λ x hxa, classical.not_not.1 (not_and.1 ( not_exists.1 h x) hxa) ) )  
-/
```
I am really confused about why the first proof works (for `le_total_r`), but the second one (commented) doesn't. The second proof gives 2 weird errors, one of which states that Lean is guessing the first thing `_` in `( (@not_exists _ _).1 h x)` to be a `Prop`, and then it wants `x` to be a `Prop`, but shouldn't it infer the first thing to be `ℚ` because the type of the provided `x` is `ℚ`?

#### [Simon Hudon (Nov 21 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Guessing%20the%20type/near/148134227):
I'm not sure why there's a difference but interestingly enough, if you write `iff.mp not_exists h x` instead `not_exists.1 h x`, the proof works. It suggests that the type inference issue might be related to the `.` notation.

#### [Kevin Buzzard (Nov 22 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Guessing%20the%20type/near/148142652):
So this is not the usual "higher order unification is hard blah blah blah" story?

#### [Simon Hudon (Nov 22 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Guessing%20the%20type/near/148145849):
I wouldn't think so but maybe @**Gabriel Ebner** can enlighten us

#### [Gabriel Ebner (Nov 22 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Guessing%20the%20type/near/148165703):
Some other variations work: e.g. if you write `(not_exists.1 h x : _)` to suppress propagation of the expected type, or if you avoid field notation with `iff.mp not_exists h x`.  A good way to debug these kinds of issues is to 1) minimize the problem a bit and 2) turn various trace options on and stare at the output:
```lean
set_option trace.type_context.is_def_eq true
set_option trace.elaborator_detail true
set_option trace.elaborator true
lemma foo (a b : ℝ) (h : ¬∃ (x : ℚ), x ∈ a.carrier ∧ x ∉ b.carrier) (x : ℚ) (hxa : x ∈ a.carrier) :
    ¬(x ∈ a.carrier ∧ x ∉ b.carrier) :=
-- (@not_exists ℚ _).1 h x
-- (not_exists.1 h _ : _)
-- (not_exists.mp h _ : _)
-- (iff.mp not_exists h x)
(not_exists.mp h x)
```
The offending unfication is here:
```
[type_context.is_def_eq] (¬∃ (x : ?m_1), ?m_2 x) ↔ ∀ (x : ?m_1), ¬?m_2 x =?= ?m_3 ↔ ?m_4 ... success  (approximate mode)
[type_context.is_def_eq] ¬(x ∈ a.carrier ∧ x ∉ b.carrier) =?= ¬?m_1 ?m_2 ... success  (approximate mode)
```

#### [Gabriel Ebner (Nov 22 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Guessing%20the%20type/near/148165924):
The problem here is that we unify the return type of the field notation application with the expected type before checking the arguments.  (In general it's a good idea to first unify the return type with the expected type---this propagates type information from the expected type to the argument types.  Consider e.g. `id ⟨a,b⟩`: in order to elaborate `⟨a,b⟩`, we need the type, but we only get that type if we propagate the expected type of `id ⟨a,b⟩` to the argument.)  The resulting second-order unification problem then does not get the solution we want.

#### [Gabriel Ebner (Nov 22 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Guessing%20the%20type/near/148166020):
The reason this only happens for the field notation case is that field notations are elaborated in two steps.  Essentially `not_exists.mp h x` is elaborated as `(iff.mp not_exists : _) h x` (which also fails).
If you write e.g. `iff.mp not_exists h x` then the return type of `iff.mp` is `?m_1 ↔ ?m_2` which does not induce a problematic second-order unification problem.

