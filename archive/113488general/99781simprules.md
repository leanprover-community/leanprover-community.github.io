---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99781simprules.html
---

## Stream: [general](index.html)
### Topic: [simp rules](99781simprules.html)

---

#### [Sebastien Gouezel (Dec 04 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877417):
I see there are many things that I would like to add as simp rules. For instance `le_refl`. And all de Morgan's rules that take a `not` and push it inside logical connectives, to get to some kind of a normal form, like `theorem not_or_distrib : ¬ (a ∨ b) ↔ ¬ a ∧ ¬ b`. Are there good reasons not to do it?

#### [Mario Carneiro (Dec 04 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877616):
I think a normal form for propositions is not a good idea unless it is a component in a full proof a la `tauto`

#### [Mario Carneiro (Dec 04 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877625):
most of the time this just mucks things up for manual proof

#### [Mario Carneiro (Dec 04 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877720):
I don't see a problem with `le_refl` as a simp rule; what other things are in scope here?

#### [Sebastien Gouezel (Dec 04 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877737):
What do you mean?

#### [Scott Morrison (Dec 04 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877881):
I definitely wouldn't want `not_or_distrib` as a simp lemma. The right hand side is only obviously simpler after you've made a particular choice about what your normal form is.

#### [Sebastien Gouezel (Dec 04 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877902):
My question about normal forms is because I ended up in a proof with several expressions of the form `¬(¬ a ∨ b)`, or things like that. I can definitely add the right rule to expand stuff, but I am under the impression that most of the time it is the right thing to do.

#### [Scott Morrison (Dec 04 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877933):
simp lemmas should have right hand sides that are "unambiguously" simpler.

#### [Mario Carneiro (Dec 04 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877935):
if I'm trying to prove `A -> B` and `simp` decides to "helpfully" replace it with `not A or B` I will be annoyed

#### [Scott Morrison (Dec 04 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150877979):
If a normal form exists for some class of objects, we want a tactic that rewrites into that normal form, but if not everyone wants to use that normal form all the time, that tactic shouldn't be `simp`.

#### [Sebastien Gouezel (Dec 04 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150878008):
Of course, `A -> B` should not be simplified like you say. I only want to add in the ones that push `¬` as far inside as possible, which looks simpler to me as `¬` is more basic than and or or. But if you all agree that it is a bad idea, let's forget about it.

#### [Mario Carneiro (Dec 04 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150878142):
I think that propositional structure in lean quite often reflects a certain structure of proof, according to its intuitionistic reading

#### [Mario Carneiro (Dec 04 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20rules/near/150878221):
even if we are being classical, lean is still easier to use when you "go with the flow" of the logic, and other stuff requires applying theorems explicitly

