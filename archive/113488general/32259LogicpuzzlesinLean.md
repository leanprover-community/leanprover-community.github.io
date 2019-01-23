---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32259LogicpuzzlesinLean.html
---

## Stream: [general](index.html)
### Topic: [Logic puzzles in Lean](32259LogicpuzzlesinLean.html)

---

#### [Patrick Massot (Jan 22 2019 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20puzzles%20in%20Lean/near/156635984):
I'm considering include a couple of small logic puzzles in my Lean exercises. But I realize I don't know how to do that. Probably I should have paid more attention to some of Kevin's messages. Say I want to formalize the solution to the first question in http://www.johnpratt.com/items/puzzles/logic_puzzles.html Say I define `inductive people : Type | Brown | Jones | Smith`. I'd like to do case disjunctions according to whether some term of type people is Brown, Jones or Smith. But `cases` is very disappointing. It replaces only in the current goal. What is the workflow here?

#### [Kevin Buzzard (Jan 22 2019 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20puzzles%20in%20Lean/near/156638799):
Answer to second one: https://xkcd.com/1134/ . For the first one, Chris would prove it using `dec_trivial` somehow.

#### [Kenny Lau (Jan 22 2019 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20puzzles%20in%20Lean/near/156638953):
@**Patrick Massot** you should `derive decidable_eq` (can we derive fintype?) and then just `dec_trivial` everything

#### [Patrick Massot (Jan 22 2019 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20puzzles%20in%20Lean/near/156640009):
I don't want a nice hi-tech proof. The question is whether I could do a logic exercise using those questions, not a `dec_trivial` exercise.

#### [Rob Lewis (Jan 22 2019 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20puzzles%20in%20Lean/near/156641666):
I'm not sure exactly what you're trying to do, could you post some code where `cases` doesn't do quite what you want?

#### [Patrick Massot (Jan 22 2019 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20puzzles%20in%20Lean/near/156644035):
Rob, say I start with:
```lean
attribute [instance] classical.prop_decidable

inductive people : Type | Brown | Jones | Smith

variables (only_child : people → Prop) (salary : people → ℕ)

inductive job : Type | doctor | lawyer | teacher
variable (P : job → people)
variable (J : people → job)
variable (PJ : ∀ x, P (J x) = x)
variable (JP : ∀ x, J (P x) = x)
include PJ JP

open people job

example (h₁ : only_child (P teacher)) 
 (h₂ : salary (P teacher) < salary (P lawyer))
 (h₃ : salary (P teacher) < salary (P doctor))
 (h₄ : ¬ only_child Brown)
 (h₅ : salary Smith > salary (P lawyer))
: J Smith = doctor ∧ J Brown = lawyer ∧ J Jones = teacher:=
begin
   sorry
end
```
I'd like to say: let's examine in turn all three possibilities for `J Smith`, derive contradictions in two cases, deduce the value of `J Smith` and move on. But `cases J Smith` does not do that. It does spawn 3 cases, but with no extra assumption, simply replacing `J Smith` in the goal.

#### [Patrick Massot (Jan 22 2019 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20puzzles%20in%20Lean/near/156644203):
Of course I can use `by_cases H : J Smith = doctor,` but this gives me two goals, not three, and only the first goal has the shape I'd like to see

#### [Rob Lewis (Jan 22 2019 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20puzzles%20in%20Lean/near/156644220):
`cases h : J Smith`?

#### [Rob Lewis (Jan 22 2019 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20puzzles%20in%20Lean/near/156644278):
That will give you the three goals, each with an additional hypothesis `h : J Smith = ...`

#### [Patrick Massot (Jan 22 2019 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20puzzles%20in%20Lean/near/156644299):
Thanks!

#### [Kenny Lau (Jan 22 2019 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20puzzles%20in%20Lean/near/156644327):
btw
```lean
@[derive decidable_eq]
inductive people : Type | Brown | Jones | Smith

@[derive decidable_eq]
inductive job : Type | doctor | lawyer | teacher
```

