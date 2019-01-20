---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: LeanTogether2019/analysissession.html
---

## [Lean Together 2019](index.html)
### [analysis session](analysissession.html)

#### Mario Carneiro (Jan 15 2019 at 15:56):
in short, taking a quotient will not mask *all* information; you are left with `trunc`

#### Mario Carneiro (Jan 15 2019 at 15:56):
this procedure of using sets of functions extending a partial function to represent partial functions

#### Patrick Massot (Jan 15 2019 at 15:57):
ok

#### Mario Carneiro (Jan 15 2019 at 15:58):
the type that does mask all information when the predicate is false is `roption`, and corresponds to the `data.pfun` implementation of partial functions

#### Joseph Corneli (Jan 15 2019 at 16:03):
@**Mario Carneiro** an interesting example is tangent, which is defined, after all, as a quotient in the function sense.  It also "tiles" so looks like a quotient in a geometric sense.  I realise many other cases won't have the same feel or origin story but it seems like the partiality in this case emerges from a *process*.

#### Mario Carneiro (Jan 15 2019 at 16:04):
I don't follow. The tangent function is not a partial function, unless you are talking about behavior at the poles

#### Joseph Corneli (Jan 15 2019 at 16:04):
Yes, that's what I'm talking about.

#### Mario Carneiro (Jan 15 2019 at 16:05):
I don't see how saying "`tan (pi/2)` is a real number but we don't know which" is a satisfying solution

#### Joseph Corneli (Jan 15 2019 at 16:06):
Well, it's not a real number but what is it?

#### Johan Commelin (Jan 15 2019 at 16:07):
It is `37`, or `0`, depending on whom you are asking.

#### Mario Carneiro (Jan 15 2019 at 16:07):
Again I think that `roption` really is capturing the right idea. It's isomorphic to the class of subsets of R with at most one element

#### Mario Carneiro (Jan 15 2019 at 16:07):
and this allows you to actually say "tan (pi/2) is not a real number"

#### Mario Carneiro (Jan 15 2019 at 16:08):
it induces a relation "r is the tan of x" which is satisfied for no r at pi/2

#### Joseph Corneli (Jan 15 2019 at 16:09):
All this does seem good but I feel I'd want to see this emerging as a "limit" of some kind.

#### Mario Carneiro (Jan 15 2019 at 16:10):
the limit comes in the fact that to define an roption you need a predicate, and this predicate describes the good behavior of the object, be it a limit, or multiplying to something reasonable, etc. If no such element exists then the value is undefined

#### Mario Carneiro (Jan 15 2019 at 16:13):
In general, I don't think we want to give any additional structure to generic partial functions; just like how functions are arbitrary maps not continuous maps or other things, partial functions can have any domain, not just open domains, and the mapping may not be computable or anything else like that

#### Mario Carneiro (Jan 15 2019 at 16:17):
By the way there is actually a data type in mathlib for underdetermined elements, called `semiquot`. It is a value that lives in a set, but we don't know which element of the set it is

#### Joseph Corneli (Jan 15 2019 at 16:23):
Thanks for the responses -- I'm glad I didn't hesitate (too much) to post.  I do still feel that there's a story to tell on the reals, and I'm only just learning the vocabulary now.  Maybe I'll come back with a further iteration of the question/idea another time!

#### Jeremy Avigad (Jan 16 2019 at 03:59):
I am hoping to experiment soon and come up with a workable way of dealing with partial functions in the analysis library. There are multiple ways we can model the space `α →. β` of partial functions. We can use `option β` or `roption β`, but, as Mario points out, there are other possibilities. For example, we can use sets with at most one element. Classically, these are all isomorphic, so I don't know whether it makes much of a difference.

Nobody seems to like the name `roption`. Assuming we stick with that type, I have a proposal: rename `roption β` to `partial  β`. Think of an element of this type as a "partial value," that is, a value that may or may not really exist. In that case, a partial function `f :  α →. β` from `α` to `β` is, by definition, a function from `α` to `partial β`.

Cute, isn't it?

#### Johan Commelin (Jan 16 2019 at 07:53):
I think I like that name! :thumbs_up:

