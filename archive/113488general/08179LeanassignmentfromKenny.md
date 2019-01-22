---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08179LeanassignmentfromKenny.html
---

## [general](index.html)
### [Lean assignment from Kenny](08179LeanassignmentfromKenny.html)

#### [Kenny Lau (Jul 30 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130567187):
(optional) assignment for the people here who are too bored:
Consider this inductive type:
```lean
inductive nested : Type
| nest : list nested → nested
```
Level 1: Write a definition `nested.cases_on'` and prove its equational lemmas.
Level 2: Prove that this type has decidable equality (no, `@[derive decidable_eq]` won't work).
Level 3: Write a definition `mem` such that `mem x (nest L)` iff `list.mem x L` and prove that `mem` is well-founded.
Level 4: Prove that this type is `denumerable` (i.e. constructively countable).

#### [Kenny Lau (Jul 30 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130567191):
(I've done levels 1-3 and will upload the code later)

#### [Kevin Buzzard (Jul 30 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130567208):
Should this be a structure?

#### [Kenny Lau (Jul 30 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130567259):
can you make it a structure?

#### [Kevin Buzzard (Jul 30 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130567272):
I don't know. I only mention it because I am dimly aware that if you make something a structure then it does some of the work for you. And it only has one constructor...

#### [Kenny Lau (Jul 30 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130567285):
I'm not sure whether `inductive` or `structure` comes with more tools, but I don't think you can make this a structure

#### [Kevin Buzzard (Jul 30 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130567296):
I remember the days when I was bored. I have far too much to do nowadays to even contemplate being bored!

#### [Kenny Lau (Jul 30 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130569524):
Answers: https://github.com/kckennylau/Lean/blob/master/nested.lean

#### [Kenny Lau (Jul 30 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130586341):
here's a choice function:

#### [Kenny Lau (Jul 30 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130586343):
```lean
def choice : Π x : nested, x ≠ nest [] → { z // z ∈ x }
| (nest [])       H := absurd rfl H
| (nest (hd::tl)) H := ⟨hd, (mem_def _ _).2 $ or.inl rfl⟩
```

#### [Kevin Buzzard (Jul 31 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130626524):
Somebody should collect up these puzzles which appear here occasionally and make a little challenge page somewhere.

#### [Kenny Lau (Jul 31 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130626588):
such as in your blog?

#### [Kenny Lau (Jul 31 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130627160):
someone pointed out to me that my type is the type of all finite trees

#### [Kevin Buzzard (Jul 31 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130627630):
Do you want to write a guest post about this problem? I look at it and I think "I'd like to work on that, but I am too busy trying to deal with the questions my UROP students are asking me".

#### [Kenny Lau (Jul 31 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130627637):
I'm busy reading ANT and AM and all that :-)

#### [Kevin Buzzard (Jul 31 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130627647):
I saw Mario explicitly pointing out in a conference talk that there was not enough number theory in mathlib. I say that we begin to concentrate on fixing this.

#### [Kenny Lau (Jul 31 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130627696):
I'd say that among all things, the theory of fin.dim. vector spaces is a prerequisite

#### [Kevin Buzzard (Jul 31 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130627699):
What exactly do you need? I have several people working on this.

#### [Kenny Lau (Jul 31 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130627702):
determinant and trace, right

#### [Kevin Buzzard (Jul 31 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130627709):
I have several people working on det too

#### [Kenny Lau (Jul 31 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130627712):
Cayley-Hamilton would be great

#### [Kenny Lau (Jul 31 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130627713):
I mean, you know much more ANT than me

#### [Kevin Buzzard (Jul 31 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130627715):
right, indeed, that's precisely what I'm a world expert in :-)

#### [Kenny Lau (Jul 31 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130627719):
then why are you asking me lol

#### [Kevin Buzzard (Jul 31 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean assignment from Kenny/near/130627720):
I'm asking you to implement it ;-)

