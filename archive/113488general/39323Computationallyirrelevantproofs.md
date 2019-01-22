---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39323Computationallyirrelevantproofs.html
---

## [general](index.html)
### [Computationally irrelevant proofs](39323Computationallyirrelevantproofs.html)

#### [AHan (Jan 04 2019 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154428282):
Is there any tactics for handling program containing computationally irrelevant proof?
Sometimes it's annoying that the non-trivial proof been replace by `_`...

#### [Johan Commelin (Jan 04 2019 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154428517):
All proofs are irrelevant.

#### [Johan Commelin (Jan 04 2019 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154428527):
That's a design choice.

#### [Johan Commelin (Jan 04 2019 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154428543):
You shouldn't ever have to care about them again.

#### [Kenny Lau (Jan 04 2019 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154428601):
`set_option pp.proofs true`

#### [AHan (Jan 04 2019 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154429152):
@**Johan Commelin**  Why shouldn't I have to care about them again ? 
I mean what if I can proof my goal with just unfold definitions of some functions, but they're hided by `_`?

#### [AHan (Jan 04 2019 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154429205):
@**Kenny Lau**  Thanks this is exactly what i'm looking for !

#### [Mario Carneiro (Jan 04 2019 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154429544):
The reason they are hidden is because it doesn't matter what is there; all proofs are definitionally equal (so if you unify with a term which has a different proof in that slot it doesn't matter), and proofs are computationally irrelevant (they do not affect control flow in any way) and they are literally thrown away by the VM.

#### [Mario Carneiro (Jan 04 2019 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154429587):
if you can prove your goal only by unfolding definitions, then probably `rfl` or similar will finish the job

#### [AHan (Jan 04 2019 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154430687):
Thanks for the explanation!

#### [petercommand (Jan 05 2019 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154464288):
is there any rw tactic to deal with programs containing computationally irrelevant proofs? like, sometimes I want to rewrite a subterm in a goal, but  the type  of the computationally irrelevant proof depends on that subterm

#### [petercommand (Jan 05 2019 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154464297):
and that makes it really annoying to manually rewrite that particular subterm

#### [petercommand (Jan 05 2019 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154464343):
I would very much want a tactic to deal with this :3

#### [petercommand (Jan 05 2019 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154464356):
like, a tactic that can rewrite the type of the proof simutaneously

#### [petercommand (Jan 05 2019 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154464407):
(and the type of the terms of the type of the proof etc)

#### [Chris Hughes (Jan 05 2019 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154465158):
There is `subst`, but that isn't too powerful at the moment.

#### [Mario Carneiro (Jan 05 2019 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154465872):
`simp` will do this, but probably not in the full generality you expect

#### [Mario Carneiro (Jan 05 2019 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154465873):
the full problem is actually quite hard

#### [Mario Carneiro (Jan 05 2019 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154465880):
but it is because of things like this that I try to avoid partial functions

#### [Mario Carneiro (Jan 05 2019 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154465883):
there are a variety of tricks for totalizing functions so that there is no proof argument in the way

#### [Kenny Lau (Jan 05 2019 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154466144):
@**Mario Carneiro** does that include using `epsilon` instead of `some`?

#### [Mario Carneiro (Jan 05 2019 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154466359):
I usually just pair `some` with an if statement

#### [Mario Carneiro (Jan 05 2019 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154466537):
 There are other options too, you aren't necessarily removing the proof argument. You could push the proof into the domain, making it a subtype domain like `finset`, or you could push it into the codomain producing an `roption` function

#### [Kevin Buzzard (Jan 05 2019 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154470598):
This conversation is too abstract for me. Can someone post some examples of what people are saying should be avoided?

#### [Chris Hughes (Jan 05 2019 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154470962):
Stuff like `log : Π z : ℂ, z ≠ 0 → ℂ ` because then if I have `log x hx` in my goal and `x = y` it's hard to rewrite.

#### [Patrick Massot (Jan 05 2019 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154471014):
Teaser: my talk in Amsterdam will feature this discussion on some example

#### [Kevin Buzzard (Jan 05 2019 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154471076):
Oh yes, you can't rewrite because hx isn't a proof of the right thing. Thanks.

#### [Kevin Buzzard (Jan 05 2019 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154471078):
The CS guys should just fix this

#### [Kevin Buzzard (Jan 05 2019 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154471130):
It's a problem with their system. They shouldn't be working around it. We should be making maths the way mathematicians do it, not moaning about things like this. Why can't it be fixed? Can it be fixed in Lean 4?

#### [Patrick Massot (Jan 05 2019 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154471182):
It seems the general case is hard for good reasons. But I agree Lean should have tactics that try heuristic or special cases

#### [Chris Hughes (Jan 05 2019 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154471192):
I get the sense that it might be much easier to make something that works 95% of the time, and the last 5% is super hard.

#### [Scott Morrison (Jan 06 2019 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154499678):
"Perfect is the enemy of good" has never been more appropriate!

#### [Kenny Lau (Jan 06 2019 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154509503):
maybe write a tactic to do it

#### [Kevin Buzzard (Jan 06 2019 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154520838):
I don't understand what's difficult here, but I'm sure there is something difficult because I'm aware that this issue comes up now and again

#### [Kevin Buzzard (Jan 06 2019 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154520840):
It feels the same as the "replace this ring with this isomorphic ring" issue

#### [petercommand (Jan 07 2019 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154551482):
```quote
It feels the same as the "replace this ring with this isomorphic ring" issue
```
 I would think that "replace this ring with this isomorphic ring" would be even harder than substituting propositionally equal term

#### [petercommand (Jan 07 2019 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154551494):
since two isomorphic rings are not necessarily propositionally equal

#### [Kevin Buzzard (Jan 07 2019 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154552001):
Right! Mathematicians have a code of honour where we only do things to rings which would work if you replaced the ring with an isomorphic one

#### [Kenny Lau (Jan 07 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154554248):
so you mean functors

#### [Joe Hendrix (Jan 11 2019 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154941811):
To resurrect this a bit, has there been a tactic that just introduces casts as needed?   In the log example, with `log : Π z : ℂ, z ≠ 0 → ℂ`, if you have the term `log x h` and equality`e: x = y`, the tactic could rewrite `log x h` to `log y (eq.rec h e)`.    I've tried this on an ad-hoc basis and sometimes run into problems later dealing with terms like `(eq.rec h e)`, but perhaps a tactic could systematically rewrite through rec.

#### [Chris Hughes (Jan 11 2019 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154942122):
`subst` already does this but only for local constants. Apparently the problem is very hard in general.

#### [Mario Carneiro (Jan 11 2019 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally irrelevant proofs/near/154948114):
You can often get `simp` to do this, or `conv`, because they use congruence lemmas for rewriting

