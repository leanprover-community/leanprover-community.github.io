---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48677combiningclasses.html
---

## [general](index.html)
### [combining classes](48677combiningclasses.html)

#### [Reid Barton (Dec 13 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151584488):
If I have `class C t extends A t, B t.` I guess it doesn't mean that anything which is an instance of `A` and `B` is automatically an instance of `C`? Does it make sense to write an instance for `C` to make that true?

#### [Reid Barton (Dec 13 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151584538):
hmm, it seems not to be a good idea.

#### [Mario Carneiro (Dec 13 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151585886):
no, it means that a `C t` is an `A t` and a `B t`

#### [Mario Carneiro (Dec 13 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151585889):
so that instance would be a loop

#### [Reid Barton (Dec 13 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151586018):
So is it a bad idea to define this class `C` in the first place then?

#### [Mario Carneiro (Dec 13 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151586529):
It has the same concerns as any other class introduction

#### [Reid Barton (Dec 13 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151586740):
I can't use C as a shorthand for A + B though

#### [Reid Barton (Dec 13 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151586752):
because I don't see any way to arrange that there is an instance of C whenever there is one of both A and B

#### [Reid Barton (Dec 13 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151586801):
In GHC, this works because GHC doesn't have these weird backwards instances "try to get A from C"

#### [Reid Barton (Dec 13 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151586810):
In particular, I'm looking at https://github.com/leanprover/mathlib/blob/master/category_theory/fully_faithful.lean#L52

#### [Johan Commelin (Dec 13 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151587244):
Right, so I've only been proving that things are `fully_faithful` but I never put it as an assumption. It's a bit awkard.

#### [Reid Barton (Dec 13 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151587292):
I guess that works, to an extent

#### [Johan Commelin (Dec 13 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151588362):
@**Reid Barton** But you would also want the type class system to try to deduce that `F` is `full` by searching for an instance that `F` is `fully_faithful` (which you say GHC wouldn't do). So the search *must* go both ways. We really need a smarter system, that wouldn't run into these *trivial* loops.

#### [Mario Carneiro (Dec 13 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151588420):
GHC would require that you prove `F` is `full` before proving it is `fully_faithful`, so it doesn't have to do the search

#### [Andrew Ashworth (Dec 13 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590559):
The smarter you make type class search, the more memory it will use... I'm sure you could use high power search techniques like contraction hierarchies, along with keeping visited nodes in memory so you could detect loops... I suspect/speculate it hasn't been done because 90% of CS users would riot over the unnecessary resource usage in large projects that do not need these features. Maybe I'm completely off-base.

#### [Andrew Ashworth (Dec 13 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590617):
It would definitely be interesting to benchmark different algorithms over a large code-base though - those would be interesting results.

#### [Johan Commelin (Dec 13 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590726):
I understand.

#### [Kevin Buzzard (Dec 13 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590731):
Mathematicians seem to me to be a class of users who are constantly running into these issues with the type class system though.

#### [Johan Commelin (Dec 13 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590737):
Lean 4 will give us the possibility to swap out the type class search algorithm...

#### [Johan Commelin (Dec 13 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590739):
So then everyone can be happy.

#### [Kevin Buzzard (Dec 13 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590801):
You made `group` a class and we thought "Oh I get it, a locally analytic topological vector space must be a class" and then it turns out that it's harder than that

#### [Kevin Buzzard (Dec 13 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590860):
@**Reid Barton** in a given use case you could try adding the loopy instance with priority 0, and then hope that this discouragement is enough in practice. It feels like any code you ship should come with a warning though.

#### [Kevin Buzzard (Dec 13 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590875):
The system would be likely to loop rather than fail so for buggy code where it should error with a failure you'll instead perhaps get a more obscure error

#### [Kevin Buzzard (Dec 13 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151590987):
Johan I guess I made one explicit example of where we weren't happy very clear to Sebastian the other day -- type class inference failing to unify two terms of a subsingleton type -- so he knows we want more here. Loops are another issue. We definitely want them. "Defeq loops" should be fine but even they can cause problems because the system doesn't abort. "Oh look we've been here before -- let's press on"

#### [Gabriel Ebner (Dec 13 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151594433):
Haskell has this nice [constraint kinds extension](https://downloads.haskell.org/~ghc/latest/docs/html/users_guide/glasgow_exts.html#the-constraint-kind), which allows you to define aliases for combinations of type classes:
```haskell
type Stringy a = (Read a, Show a) -- Read and Show are type classes
type C t = (A t, B t) -- Reid's example
```
In principle, there is no fundamental reason why we couldn't do something like this in Lean as well.  @**Johan Commelin** I wouldn't count on customizing type class inference.

#### [Johan Commelin (Dec 13 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/combining%20classes/near/151594520):
Ooh, too bad. I thought I heard at some point that it would be possible...

