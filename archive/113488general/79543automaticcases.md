---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79543automaticcases.html
---

## [general](index.html)
### [automatic cases](79543automaticcases.html)

#### [Kenny Lau (Jul 28 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20cases/near/130457556):
Can we have a tactic that does `cases` on the argument of `XX.rec` or `XX.rec_on`?

#### [Kevin Buzzard (Jul 28 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20cases/near/130457669):
That sounds like a really nice basic tactic for a tactic-learner to write!

#### [Kenny Lau (Jul 28 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20cases/near/130457886):
good! are you a tactic-learner?

#### [Kevin Buzzard (Jul 28 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20cases/near/130458769):
Maybe @**Chris Hughes** is? I think he got a bit disheartened when he realised he had 100 questions and couldn't face asking Mario and Simon all of them though...

#### [Kevin Buzzard (Jul 28 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20cases/near/130458770):
(and of course I was no help)

#### [Kevin Buzzard (Jul 28 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20cases/near/130458776):
Maybe there should be a basic tactic-writing thread. The workflow I see is: start Zulip thread, spam it with basic questions which are not covered in PIL, experts occasionally make insightful comments, someone writes some notes and sticks them up in the mathlib docs project, we all learn something.

#### [Kevin Buzzard (Jul 28 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20cases/near/130458988):
From Programming In Lean:

```lean
open tactic

meta def destruct_conjunctions : tactic unit :=
repeat (do
l ← local_context,
first $ l.map (λ h, do
ht ← infer_type h >>= whnf,
match ht with
| `(and %%a %%b) := do
n ← get_unused_name `h none,
mk_mapp ``and.left [none, none, some h] >>= assertv n a,
n ← get_unused_name `h none,
mk_mapp ``and.right [none, none, some h] >>= assertv n b,
clear h
| _ := failed
end))

example (P Q : Prop) (HPQ : P ∧ Q) : false :=
begin
  destruct_conjunctions,
  exact false.intro
end
```

That's how to break up an `and` in the hypotheses. You just want to break up a `rec` in the conclusion. How hard can it be? ;-)

#### [Johan Commelin (Jul 28 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/automatic%20cases/near/130459043):
```quote
Maybe there should be a basic tactic-writing thread. The workflow I see is: start Zulip thread, spam it with basic questions which are not covered in PIL, experts occasionally make insightful comments, someone writes some notes and sticks them up in the mathlib docs project, we all learn something.
```
Or a "tactics" stream? We've got a "maths" stream after all. This seems like a general enough topic (in the non-Zulip sense) to turn it into a stream.

