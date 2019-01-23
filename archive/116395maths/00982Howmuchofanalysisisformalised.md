---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/00982Howmuchofanalysisisformalised.html
---

## Stream: [maths](index.html)
### Topic: [How much of analysis is formalised?](00982Howmuchofanalysisisformalised.html)

---

#### [Abhimanyu Pallavi Sudhir (Oct 13 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135728233):
How much of analysis is formalised right now? I'm guessing basic calculus -- limits, single-variable stuff, Riemann integrals -- are formalised. What about multivariable, complex analysis (e.g. the complex-analytic proof of the fundamental theorem of algebra), fractional calculus, variational calculus, etc.?

#### [Chris Hughes (Oct 13 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135728461):
Integrals are there, but very new, only arrived this week, No derivatives at all as far as I know. Complex analysis is currently very limited, no FTA, look through `analysis/complex` and you'll get the idea.

#### [Abhimanyu Pallavi Sudhir (Oct 13 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135728573):
Just simple Riemann integrals or are Lesbegue, etc. also there?

#### [Abhimanyu Pallavi Sudhir (Oct 13 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135728621):
Oh, ok, Lesbegue seems to be there -- analysis/lesbegue_measure.lean

#### [Chris Hughes (Oct 13 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135728795):
I haven't looked through it too much, but there's something called `lintegral` which I'm guessing is lebesgue integral, and something called `integral` and I don't know what that is.

#### [Kevin Buzzard (Oct 13 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135729077):
What is the situation regarding differentiation @**Patrick Massot** ? I am somehow always confused about whether someone is going to set up a theory of calculus for real-valued functions of one real variable or whether this is somehow all going to be subsumed by some massive multivariable possibly infinite-dimensional normed spaces because this was the correct generality that the theory should be developed in so that's how it has to work.

#### [Johannes Hölzl (Oct 13 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135735421):
hm, I see this is a little bit confusing `lintegral` is actually the lower Lebesgue integral (there might be later a upper Lebesgue integral). It is not the Lebesgue integral into the reals, but it is necessary to define it. My intention is to use this integral to define norms on measurable functions and then define the Bochner integral (which is an integral for functions into a separable Banch space, while the Lebesgue integral is integrating functions into reals)

#### [Johannes Hölzl (Oct 13 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135735470):
AFAIK, @**Jeremy Avigad** wants now to start on multivariate analysis, so also derivative of functions etc.

#### [Jeremy Avigad (Oct 13 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135735875):
Yes, I have just gotten started. I'll push to `leanprover-community` as soon as there is anything worth seeing.

#### [Patrick Massot (Oct 13 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135742603):
```quote
What is the situation regarding differentiation Patrick Massot? I am somehow always confused about whether someone is going to set up a theory of calculus for real-valued functions of one real variable or whether this is somehow all going to be subsumed by some massive multivariable possibly infinite-dimensional normed spaces because this was the correct generality that the theory should be developed in so that's how it has to work.
```
My hope was to do the possibly infinite dimensional stuff and deduce the 1-dimensional case, but we'll see what Jeremy does

#### [Kevin Buzzard (Oct 14 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135777542):
@**Abhimanyu Pallavi Sudhir** I think it's worth pointing out the analogy here with the theory of polynomials. Johannes Hoelzl made a big library for polynomials in an arbitrary number of variables, and after that one could argue that "Lean had polynomials". However there were lots of basic facts about polynomials in _one_ variable which we did not have (many of which did not generalise to polynomials in an arbitrary number of variables) and eventually Chris decided to lead the development of a theory of polynomials in one variable https://github.com/leanprover/mathlib/blob/master/data/polynomial.lean which turned out to be useful for my personal work on perfectoid spaces and also indirectly started to guide Mario towards how the theory of modules over a ring should actually be implemented in Lean (which has been an interesting open question for months). 

In short -- don't let the fact that people are considering writing some huge library of multivariable calculus stop you developing the basic theory of calculus in one variable. Here are a bunch of things, many of which I believe we don't have, and which will be useful for doing M1M1 in Lean: definition of derivative of a function from $$\mathbb{R}$$ to $$\mathbb{R}$$ and proof that it is linear (i.e. $$(f+g)'=f'+g'$$ etc), chain rule, product rule, quotient rule, the derivative of $$e^x$$ is $$e^x$$ and the derivative of $$\sin(x)$$ is $$\cos(x)$$. These last few things are maybe not even going to be covered by this general grand plan by experts to develop a theory of multivariable everything, but we're back to the same point: what would a _mathematician_ think when we tell them that we cannot prove that the derivative of $$\sin(x)$$ is $$\cos(x)$$? @**Chris Hughes** am I right in thinking that we still cannot do this in Lean?

#### [Chris Hughes (Oct 14 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778093):
We can't state it in Lean.

#### [Kenny Lau (Oct 14 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778240):
`forall x, tendsto (fun h, (sin(x+h)-sin(x))/h) (nbhd 0) (nbhd (cos x))`

#### [Mario Carneiro (Oct 14 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778349):
the division should go over the subtraction

#### [Kenny Lau (Oct 14 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778352):
edited

#### [Mario Carneiro (Oct 14 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778353):
also it's not true, because that function has a jump discontinuity at 0

#### [Kenny Lau (Oct 14 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778354):
but it's true because 0/0=0

#### [Mario Carneiro (Oct 14 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778359):
right, 0 not cos x

#### [Kenny Lau (Oct 14 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778360):
ah

#### [Kenny Lau (Oct 14 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778362):
`forall x, tendsto (fun h, (sin(x+h)-sin(x)-h*cos(x))/h) (nbhd 0) (nbhd 0)`

#### [Mario Carneiro (Oct 14 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778363):
still 0

#### [Mario Carneiro (Oct 14 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778364):
oh wait

#### [Mario Carneiro (Oct 14 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778417):
okay that should work

#### [Mario Carneiro (Oct 14 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778419):
at least, it's a true fact, it looks quite different from $$\sin'(x) = \cos(x)$$

#### [Kenny Lau (Oct 14 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778459):
say that to Patrick Massot

#### [Patrick Massot (Oct 14 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778661):
What?

#### [Kenny Lau (Oct 14 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778668):
that's how you defined complex derivative right

#### [Patrick Massot (Oct 14 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778732):
I'm not sure what you are talking about, but the definition of complex derivatives in kbb comes from Tom Hales

#### [Patrick Massot (Oct 14 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778734):
not from me

#### [Patrick Massot (Oct 14 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778739):
But it looked ok. Is the discussion around what happens at h=0?

#### [Kenny Lau (Oct 14 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135778793):
the discussion is that it looks quite different from sin'(x) = cos(x)

#### [Kevin Buzzard (Oct 14 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135779619):
it's one unfold away from sin' = cos

#### [Kevin Buzzard (Oct 14 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135779665):
so we are back to Chris' point.

#### [Kenny Lau (Oct 14 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135779701):
it isn't because this isn't defining a function

#### [Kevin Buzzard (Oct 14 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135779776):
oh, fair point.

#### [Sebastien Gouezel (Oct 14 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135784063):
As far as I can see, there is no typeclass for compact spaces, right? (I have the impression that `compact` is only a predicate on subsets of topological spaces). Is there any problem with
```lean
class compact_space (α : Type u) [topological_space α] :=
(compact_univ : compact (univ : set α))
```
?

#### [Reid Barton (Oct 14 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135784684):
I think I suggested an identical definition on zulip a week or two ago. Haven't had much time for actual Lean recently though.

#### [Johannes Hölzl (Oct 14 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20much%20of%20analysis%20is%20formalised%3F/near/135792687):
`compact_space` is surely helpful

