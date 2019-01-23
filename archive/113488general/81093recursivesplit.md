---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/81093recursivesplit.html
---

## Stream: [general](index.html)
### Topic: [recursive split](81093recursivesplit.html)

---

#### [Patrick Massot (Jul 02 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128962808):
Do we have a recursive split tactic? My goal looks likes `a ∧ b ∧ c ∧ d` and I would like to write one word and get four non-nested goals.

#### [Sean Leather (Jul 02 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128962925):
There's only one “word” in `refine ⟨_, _, _, _⟩`. :wink:

#### [Patrick Massot (Jul 02 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128963057):
Obviously, this is not exactly as readable as I hoped for, but at least this indeed does the trick.

#### [Sebastian Ullrich (Jul 02 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128964010):
`repeat { any_goals { split } }` :)

#### [Sebastian Ullrich (Jul 02 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128964047):
...which at least is a bit more general and could be extracted into a new tactic

#### [Jakob von Raumer (Jul 02 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128964146):
Isn't ther also a `rcases` in mathlib that does this?

#### [Kenny Lau (Jul 02 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128964164):
that destructs hypotheses

#### [Sean Leather (Jul 02 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128964437):
```quote
`repeat { any_goals { split } }` :)
```
How efficient is that? For `g1 ∧ g2 ∧ g3 ∧ g4`, I'm guessing that's 4 applications of `any_goals`, but `any_goals` would also test all previously `split` goals each time, right? I suppose it could be improved by “remembering” that `split` failed for a visited goal.

#### [Sebastian Ullrich (Jul 02 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128964553):
How big are your conjunctions that you expect this to be a problem :frowning: ? `split` isn't exactly an expensive tactic.

#### [Patrick Massot (Jul 02 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128969257):
I like that this version seems easy to turn into a new tactic. But, in the case I'm looking at, this creates too many goals, with stupid meta-variables

#### [Simon Hudon (Jul 02 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128970861):
Do you have existential quantifications?

#### [Simon Hudon (Jul 02 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128971009):
You can also use `constructor_matching* _ ∧ _` to make sure it only splits conjunctions

#### [Patrick Massot (Jul 02 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128971022):
Yes, hidden in subset image. After much effort, I managed to minimize to:
```lean
example (α β : Type) (f : α → β) (s : set α) (s' : set β) (x : β) :  
  f '' s ⊆ s' ∧ x ∈ f '' s :=
begin
  -- refine ⟨_, _⟩,
  repeat { all_goals { split } },
end 
```

