---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/179818LeanTogether2019/90889analysissession.html
---

## Stream: [Lean Together 2019](index.html)
### Topic: [analysis session](90889analysissession.html)

---

#### [Jeremy Avigad (Jan 09 2019 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/154724961):
Friends, 

I am planning to formalize derivatives, etc. in terms of Lean's partial function type. To that end, I have generalized limits to partial functions (and even partial multifunctions = relations). I told Rob and Johannes that I'd like to talk about that in the analysis session, because I can use some feedback. In response, they told me I could moderate the session and abuse my status as moderator to talk about whatever I want. That works for me.

It would also be helpful to me to hear about Cyril's experiences formalizing analysis in Coq. So here is what I am thinking about for the session:

(1) a quick overview of approaches to dealing with partial functions (me, <= 15 minutes)

(2) notions of limits for partial functions and relations (e.g. what lim_{x -> a} f(x) means when f is partial) (me, <= 15 minutes)

(3) an overview of analysis in Coq (Cyril, ~20 minutes)

My thought is that I can mostly defer questions in (1) and (2), and then after Cyril has a chance to talk to a while, we can turn the session into open discussion. Does anyone object to that plan?

#### [Joseph Corneli (Jan 15 2019 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155174171):
I know Jeremy said he didn't want to start a debate about which way of representing partial functions is "better" but maybe it's worth sharing an after-the-fact reflection about how very *different* two of the options are.

Let's start with the *indicator function*:

$$\chi_{[0,1]}\colon \mathbb{R}\rightarrow\mathbb{R}$$,
$$x\in[0,1]\Rightarrow\chi(x)=1$$, $$x\notin[0,1]\Rightarrow \chi(x)=0$$

If we were to talk about a function $$\psi\colon\mathbb{R}\rightarrow\mathbb{R}$$ with the property $$\psi\vert_{[0,1]}=\chi_{[0,1]}$$, it seems to me that, until we are given further information, the values of $$\psi$$ outside of $$[0,1]$$ are more comfortably thought of as *unknown*, or even *irrelevant*, but not wholly "undefined".  In particular, we know that these values are in  $$\mathbb{R}$$.

So in the spirit of the example, we could define a "partial function on $$\mathbb{R}$$ that is equal to $$1$$ on $$[0,1]$$" to be the *set* of all functions on $$\mathbb{R}$$ that are equal to $$1$$ on $$[0,1]$$.  Actually, this seems to just be the "relation" option that Jeremy described, indeed, equality-on-the-unit-interval looks to be an equivalence relation.  Well, I admit, I do have a bias, which is that this definition seems to capture something "geometric" that the definition using `undefined` doesn't (at least not so directly).

#### [Patrick Massot (Jan 15 2019 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155174477):
I still think this is a very bad example, since the indicator function is a total function, without any discussion. Its values outside $$[0, 1]$$ are not undefined in any sense

#### [Joseph Corneli (Jan 15 2019 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155174551):
But you could make an information-theoretic version of the indicator function that masks all information outside of the unit interval.

#### [Patrick Massot (Jan 15 2019 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155174636):
For instance, it is of utmost importance that, for every other (say continuous) function $$f$$ , $$\int_{[0, 1]} f = \int_\mathbb{R} f\chi_{[0, 1]}$$. There is no other value than zero that would make that true

#### [Mario Carneiro (Jan 15 2019 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155174644):
This assumes the codomain is inhabited, else that set might be empty

#### [Mario Carneiro (Jan 15 2019 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155174726):
in general it shares many of the downsides of things like continuous extensions - they may not exist, although it's nice when they do

#### [Patrick Massot (Jan 15 2019 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155174840):
Mario, what are "This" and "it" in your latest messages?

#### [Mario Carneiro (Jan 15 2019 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155174847):
in short, taking a quotient will not mask *all* information; you are left with `trunc`

#### [Mario Carneiro (Jan 15 2019 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155174897):
this procedure of using sets of functions extending a partial function to represent partial functions

#### [Patrick Massot (Jan 15 2019 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155174958):
ok

#### [Mario Carneiro (Jan 15 2019 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155175059):
the type that does mask all information when the predicate is false is `roption`, and corresponds to the `data.pfun` implementation of partial functions

#### [Joseph Corneli (Jan 15 2019 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155175549):
@**Mario Carneiro** an interesting example is tangent, which is defined, after all, as a quotient in the function sense.  It also "tiles" so looks like a quotient in a geometric sense.  I realise many other cases won't have the same feel or origin story but it seems like the partiality in this case emerges from a *process*.

#### [Mario Carneiro (Jan 15 2019 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155175655):
I don't follow. The tangent function is not a partial function, unless you are talking about behavior at the poles

#### [Joseph Corneli (Jan 15 2019 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155175667):
Yes, that's what I'm talking about.

#### [Mario Carneiro (Jan 15 2019 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155175739):
I don't see how saying "`tan (pi/2)` is a real number but we don't know which" is a satisfying solution

#### [Joseph Corneli (Jan 15 2019 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155175890):
Well, it's not a real number but what is it?

#### [Johan Commelin (Jan 15 2019 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155175922):
It is `37`, or `0`, depending on whom you are asking.

#### [Mario Carneiro (Jan 15 2019 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155175925):
Again I think that `roption` really is capturing the right idea. It's isomorphic to the class of subsets of R with at most one element

#### [Mario Carneiro (Jan 15 2019 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155175950):
and this allows you to actually say "tan (pi/2) is not a real number"

#### [Mario Carneiro (Jan 15 2019 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155176063):
it induces a relation "r is the tan of x" which is satisfied for no r at pi/2

#### [Joseph Corneli (Jan 15 2019 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155176107):
All this does seem good but I feel I'd want to see this emerging as a "limit" of some kind.

#### [Mario Carneiro (Jan 15 2019 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155176227):
the limit comes in the fact that to define an roption you need a predicate, and this predicate describes the good behavior of the object, be it a limit, or multiplying to something reasonable, etc. If no such element exists then the value is undefined

#### [Mario Carneiro (Jan 15 2019 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155176486):
In general, I don't think we want to give any additional structure to generic partial functions; just like how functions are arbitrary maps not continuous maps or other things, partial functions can have any domain, not just open domains, and the mapping may not be computable or anything else like that

#### [Mario Carneiro (Jan 15 2019 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155176789):
By the way there is actually a data type in mathlib for underdetermined elements, called `semiquot`. It is a value that lives in a set, but we don't know which element of the set it is

#### [Joseph Corneli (Jan 15 2019 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155177265):
Thanks for the responses -- I'm glad I didn't hesitate (too much) to post.  I do still feel that there's a story to tell on the reals, and I'm only just learning the vocabulary now.  Maybe I'll come back with a further iteration of the question/idea another time!

#### [Jeremy Avigad (Jan 16 2019 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155223544):
I am hoping to experiment soon and come up with a workable way of dealing with partial functions in the analysis library. There are multiple ways we can model the space `α →. β` of partial functions. We can use `option β` or `roption β`, but, as Mario points out, there are other possibilities. For example, we can use sets with at most one element. Classically, these are all isomorphic, so I don't know whether it makes much of a difference.

Nobody seems to like the name `roption`. Assuming we stick with that type, I have a proposal: rename `roption β` to `partial  β`. Think of an element of this type as a "partial value," that is, a value that may or may not really exist. In that case, a partial function `f :  α →. β` from `α` to `β` is, by definition, a function from `α` to `partial β`.

Cute, isn't it?

#### [Johan Commelin (Jan 16 2019 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean%20Together%202019/topic/analysis%20session/near/155232912):
I think I like that name! :thumbs_up:

