---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89043coinductivetypes.html
---

## [general](index.html)
### [coinductive types](89043coinductivetypes.html)

#### [Kevin Buzzard (Feb 28 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123081684):
Can someone (@**Simon Hudon** ?) explain what a coinductive type is and, more specifically, whether a mathematician would ever need them?

#### [Kevin Buzzard (Feb 28 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123081788):
As to the comments about them made here and linked to here, this might be another of those "perfect is the enemy of good" situations where we could either have Simon's "does the job to a certain extent", or the observation that one could do this much better if only we could find a Lean C++ hacker that just sat down and wrote a bunch of complicated working code, I would vote for Simon any day of the week.

#### [Mario Carneiro (Feb 28 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123081900):
We don't need a C++ hacker for this one. I hope to implement the next version of (co)inductive types in lean

#### [Sean Leather (Feb 28 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123081904):
@**Kevin Buzzard**: [Non-wellfounded Set Theory](https://plato.stanford.edu/entries/nonwellfounded-set-theory/) might help.

#### [Mario Carneiro (Feb 28 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123081913):
Mathematically, the theory of coinductive types is very elegantly dual to the theory of inductive types. A simple example of a coinductive type is the type of "possibly infinite lists", which is defined with the same clauses as `list`

#### [Mario Carneiro (Feb 28 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123081955):
This is a type that contains the empty list, finite lists, as well as all infinite lists (a.k.a "streams")

#### [Mario Carneiro (Feb 28 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123082040):
(These are often called `llist` or "lazy lists" for reasons to come.) The type `llist` has a `cases_on`, i.e. you can ask for any `llist` whether it is nil or a cons of an element and a `llist`, but there is no `rec`, because a `llist` is not well founded

#### [Simon Hudon (Feb 28 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123102878):
There's also:
@**Tim Carstens** 
> terminal co-algebra of an endofunctor, instead of initial algebra of an endofunctor

if you want to look at them in terms of category theory

#### [Simon Hudon (Feb 28 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123103022):
`llist` are easy enough without `coinductive` types but I imagine if you care about (possibly) infinite objects such as trees, it will be hard to study them without coinductive types.

I personally care about them mostly for modelling programs that do not terminate such as operating systems, controllers for pacemakers or any internet protocol

#### [Tim Carstens (Feb 28 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123103123):
maybe bass-serre theory, aka doing group theory by way of group actions on (infinite) trees

#### [Tim Carstens (Feb 28 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123103136):
i'm struggling to think up examples from pure math where coinductives would be handy

#### [Tim Carstens (Feb 28 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coinductive%20types/near/123103143):
it's a big world out there though

