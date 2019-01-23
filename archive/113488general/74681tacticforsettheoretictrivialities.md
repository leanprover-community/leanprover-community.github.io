---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74681tacticforsettheoretictrivialities.html
---

## Stream: [general](index.html)
### Topic: [tactic for set-theoretic trivialities](74681tacticforsettheoretictrivialities.html)

---

#### [Kevin Buzzard (May 21 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866089):
I am beginning to tire of goals of the form `Ua ∩ Ub ∩ Uc ⊆ Ua ∩ Ub ∩ (Ua ∩ Uc)`

#### [Kevin Buzzard (May 21 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866091):
Is there a tactic which solves them?

#### [Kevin Buzzard (May 21 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866093):
[these are sets]

#### [Kevin Buzzard (May 21 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866107):
[let me stress that I can solve them, it's just the novelty is wearing off]

#### [Andrew Ashworth (May 21 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866109):
`by finish`?

#### [Kevin Buzzard (May 21 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866116):
didn't work for me for this one

#### [Kevin Buzzard (May 21 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866165):
cc and simp don't work either

#### [Kevin Buzzard (May 21 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866176):
[Prediction : in about 8 hours Scott wakes up and remarks that one of his secret tactics does the job immediately]

#### [Kenny Lau (May 21 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866279):
`solve_by_elim`?

#### [Kevin Buzzard (May 21 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866331):
Note that any such tactic will have to deal with the fact that `exact ⟨Ha,Hb,⟨Ha,Hc⟩⟩` is not a proof of `y ∈ Ua ∩ Ub ∩ (Ua ∩ Uc)` because of stupid left associativity of \cap

#### [Kevin Buzzard (May 21 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866342):
`solve_by_elim` doesn't work

#### [Mario Carneiro (May 21 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866351):
I think `finish` was intended to work on those goals

#### [Mario Carneiro (May 21 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866401):
but you may need to use its options

#### [Mario Carneiro (May 21 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866429):
```
example {α} (Ua Ub Uc : set α) : Ua ∩ Ub ∩ Uc ⊆ Ua ∩ Ub ∩ (Ua ∩ Uc) :=
by simp [set.subset_def] {contextual := tt}
```

#### [Andrew Ashworth (May 21 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866528):
it reminds me I don't know what `finish` solves. Does it work on any boolean algebra?

#### [Patrick Massot (May 21 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866532):
`by finish[set.subset_def]` also works

#### [Mario Carneiro (May 21 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866533):
it works on the boolean algebra of propositions...

#### [Mario Carneiro (May 21 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866539):
that's why `subset_def` is needed here

#### [Kenny Lau (May 21 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866767):
people just bloody abusing `finish`

#### [Kevin Buzzard (May 21 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866773):
We're too classical for you

#### [Kevin Buzzard (May 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866779):
Do you think it's true in constructive maths?

#### [Kevin Buzzard (May 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866780):
I would have no idea :-)

#### [Kenny Lau (May 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866782):
of course it is

#### [Kevin Buzzard (May 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866783):
:-)

#### [Kenny Lau (May 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866784):
they're literally the same set

#### [Kevin Buzzard (May 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866786):
yeah but you never know with this constructive maths thing

#### [Patrick Massot (May 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866787):
Using `finish` does not only finishes the goal. It also conveys the meaning that the goal is now something we don't want to discuss at all

#### [Kevin Buzzard (May 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866789):
I mean not not P is literally the same as P, right?

#### [Kenny Lau (May 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866830):
*t r i g g e r e d*

#### [Kevin Buzzard (May 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866833):
Shouldn't you be revising for mechanics?

#### [Kenny Lau (May 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866836):
I see that you're proving mul_add

#### [Kenny Lau (May 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866838):
can't you prove that the two sets are equal instead?

#### [Patrick Massot (May 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866839):
Shouldn't you be marking?

#### [Kenny Lau (May 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866840):
I think equality is eaiser to prove

#### [Kenny Lau (May 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866842):
```quote
Shouldn't you be marking?
```
oooooooh

#### [Kevin Buzzard (May 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866843):
I've just proved something is a ring!

#### [Kevin Buzzard (May 21 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866848):
I'm sitting on the tube platform at South Ken, completely elated

#### [Kevin Buzzard (May 21 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866853):
[:= v happy]

#### [Kevin Buzzard (May 21 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866855):
Now if only someone had proved that a product of rings was a ring

#### [Kevin Buzzard (May 21 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866886):
oh wait

#### [Kevin Buzzard (May 21 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866904):
I think O_X(U) is a ring!

#### [Kevin Buzzard (May 21 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866905):
I still have to prove restriction is a ring homomorphism though

#### [Kevin Buzzard (May 21 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866906):
I will save that for after some marking

#### [Kevin Buzzard (May 21 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866918):
What I am actually pleased about is that I seriously engaged with quotient types for the first time in my life, and I have come out alive

#### [Kevin Buzzard (May 21 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866962):
Why is quot.lift called that?

#### [Kevin Buzzard (May 21 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866964):
It's the opposite of a lift, the way things are set up in my brain

#### [Kevin Buzzard (May 21 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866965):
It's a descent

#### [Patrick Massot (May 21 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866966):
I remember being puzzled by this terminology while reading TPIL

#### [Kevin Buzzard (May 21 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866973):
I think that this observation was genuinely something which added to my confusion when looking at quotient type stuff

#### [Kevin Buzzard (May 21 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866975):
This name was not at all intuitive for me

#### [Patrick Massot (May 21 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866976):
Obviously

#### [Kevin Buzzard (May 21 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866983):
Is this a CS thing Patrick?

#### [Patrick Massot (May 21 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866984):
No idea

#### [Patrick Massot (May 21 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866985):
Just crazyness if you ask me

#### [Kevin Buzzard (May 21 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126867031):
Anyway, we live and learn, and I've certainly learnt something over the last couple of days. Thanks to everyone that helped. I genuinely feel like a better Leaner.

#### [Sean Leather (May 21 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126867301):
~~Leaner~~Lea(r)ner

