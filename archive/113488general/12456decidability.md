---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/12456decidability.html
---

## [general](index.html)
### [decidability](12456decidability.html)

#### [Kenny Lau (Mar 30 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428848):
Are there things that are decidable but not yet proven?

#### [Kenny Lau (Mar 30 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428850):
@**Mario Carneiro**

#### [Mario Carneiro (Mar 30 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428860):
Not sure I understand the meta level of the question

#### [Kenny Lau (Mar 30 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428902):
that means, things that should be decidable, but nobody has proved it in Lean yet

#### [Mario Carneiro (Mar 30 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428905):
of course

#### [Kenny Lau (Mar 30 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428906):
could you list some

#### [Mario Carneiro (Mar 30 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428908):
that's like asking if there are any not yet proven theorems

#### [Kenny Lau (Mar 30 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428920):
well there are only finitely many predicates that have been created in Lean

#### [Mario Carneiro (Mar 30 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428942):
Hm, none comes to mind... I have a definition that I don't have on mathlib yet that is waiting for a proof of decidability

#### [Kenny Lau (Mar 30 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428945):
what is it

#### [Mario Carneiro (Mar 30 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428987):
namely that level (in)equality in lean is decidable

#### [Kenny Lau (Mar 30 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428992):
hmm...

#### [Mario Carneiro (Mar 30 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429012):
that is, for expressions made up of `max`, `imax` and variables, you can determine if for all values of the variables in `nat`, one is <= the other or not

#### [Mario Carneiro (Mar 30 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429027):
The proof uses case splitting on any `imax` expressions that come up

#### [Kenny Lau (Mar 30 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429032):
oh, I should build a decidable version of `finsupp`

#### [Mario Carneiro (Mar 30 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429086):
I think Johannes had a proposal for that on here, where you use a `fintype` instead of `finite`

#### [Kenny Lau (Mar 30 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429095):
oh wait, I don't work with finite things

#### [Kenny Lau (Mar 30 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429096):
lol

#### [Kenny Lau (Mar 30 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429371):
@**Mario Carneiro** no examples from `nat` and `int`?

#### [Kenny Lau (Mar 30 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429372):
i.e. everything about them that should be decidable have been proven to be decidable?

#### [Mario Carneiro (Mar 30 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429446):
yes, there aren't that many interesting predicate to start with

#### [Kenny Lau (Mar 30 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429495):
nice

#### [Andrew Ashworth (Mar 30 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124430652):
@**Kenny Lau** out of curiousity what's up with your commutative algebra pr on mathlib

#### [Kenny Lau (Mar 30 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124430671):
I just started reworking it a few minutes ago, what a coincidence

#### [Kevin Buzzard (Mar 31 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433277):
Kenny feel free to PR some of the comm alg stuff in stacks project. Did UMP get PR'd? That's a really important tool I see now.

#### [Kenny Lau (Mar 31 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433281):
I can't PR anything until mathlib builds

#### [Kevin Buzzard (Mar 31 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433282):
Oh I see.

#### [Kevin Buzzard (Mar 31 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433283):
Why don't you roll back?

#### [Kenny Lau (Mar 31 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433324):
I mean, the PR will have a cross

#### [Kevin Buzzard (Mar 31 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433326):
I know it's a bore. Whenever Lean head and mathlib head don't play well together you're suddenly having to look up commits.

#### [Kevin Buzzard (Mar 31 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433332):
I just never upgrade unless I have no red cross and also a thumbs up here

#### [Kevin Buzzard (Mar 31 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433342):
I think Sebastian is seriously looking at making this kind of thing easier with leanpkg.

#### [Kenny Lau (Mar 31 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433346):
I still don't know why the latest build fails

