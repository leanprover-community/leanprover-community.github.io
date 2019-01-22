---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/36508multivariateanalysis.html
---

## [maths](index.html)
### [multivariate analysis](36508multivariateanalysis.html)

#### [Jeremy Avigad (Oct 10 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135568640):
Friends,

I apologize in advance for this long post. For various projects, I am going to need a good library for multivariate analysis. At minimum, I want to be able to reason about systems of differential equations and dynamical systems on R^n, optimization problems in R^n, etc. The general idea is to look for ways to make Lean and ITP useful for working on problems in applied mathematics. (In the long run, it would be great to have complex analysis, measure theory, optimization on function spaces, stochastic calculus, differential geometry, etc., etc. But the plan is to start small and try to find some compelling prototype applications rather than focus exclusively on building general theory.)

Two examples of the sort of thing it would be good to have are these:

(1) Some of Fabian Immler's very nice work on the dynamical systems background to the numeric calculations related to the Lorenz attractor. (The first paper on his web page is an excellent survey: http://home.in.tum.de/~immler/)

(2) Damien Rouhling's very nice formalization of a solution to the inverted pendulum problem (https://hal.inria.fr/hal-01639819) based on the mathcomp library and prior work with Cyril Cohen (https://hal.inria.fr/hal-01612293). 

So I can use the Isabelle and mathcomp libraries as a model.

https://www.isa-afp.org/browser_info/current/AFP/Ordinary_Differential_Equations/index.html
https://github.com/math-comp/analysis
https://github.com/drouhling/LaSalle

Lots of things in that are already in the Lean library will be helpful: topological, limits, polynomials, matrices, the transcendental functions, normed spaces, and Johannes' work on integration. As far as I can tell, these are the things I should work on:

- The Frechet derivative, defined in general for functions between normed vector spaces
- The spaces R^n as instances, connections between linear maps and matrices, polynomials and their derivatives, etc.
- ODE's and the Picard-Lindelöf theorem.

I am planning to work on this on a fork in my repository but push to a branch of leanprover-community/mathlib often, whenever things look decent.

As usual, lots of little questions and design decisions will arise, such as:

- how much to bundle (e.g. (f : real -> real) [bounded f] [continous f] or (f : bounded_continuous_function R R))
- how much to use type classes for
- how to restrict to subdomains (continuous_on f s) or (continuous (restrict f s))
- how to handle partial functions

I will experiment and raise specific questions here as they come up.

Here is the reason for this long post:

(1) If any of you have advice, suggestions, requests, etc. please let me know.

(2) If any of you are working on related things, or plan to work on related things, please let me know so that we can coordinate and avoid duplication.

In particular, @**Patrick Massot** , Mario pointed me your differential topology repo. Are you still working on it? Can I steal the chain rule? Is there anything you want me to do or to avoid?

#### [Kevin Buzzard (Oct 10 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135568777):
You're going to embark upon this in Lean 3?

#### [Patrick Massot (Oct 10 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135568947):
Of course you can steal anything from my differential topology repo, but I don't think you'll want to. I think everything that was decent has been incorporated into mathlib (the last piece was https://github.com/leanprover/mathlib/blob/master/analysis/bounded_linear_maps.lean). The chain rule proof works but is horribly painful

#### [Patrick Massot (Oct 10 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135569057):
I'm not currently working on this. I'm very slow with Lean, and all my Lean effort is currently driven by the perfectoid project (it happens in the branch https://github.com/leanprover-community/mathlib/tree/completions). My initial hope was to investigate whether it would be possible to do differential topology in Lean because most mathematicians would be very surprised. But clearly I couldn't do that alone, so I preferred to join another project with more mathematicians involved (but we still can't do anything without Johannes and Mario)

#### [Patrick Massot (Oct 10 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135569153):
I really think we should finish the perfectoid project before starting another ambitious project, but if we ever finish perfectoid spaces then I'd be delighted to work on differentiable manifolds with you.

#### [Patrick Massot (Oct 10 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135569166):
Note also https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Material/banach_contraction.lean that is still waiting for cleanup, but very relevant to your goals

#### [Kevin Buzzard (Oct 10 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135569374):
```quote
I really think we should finish the perfectoid project before starting another ambitious project, but if we ever finish perfectoid spaces then I'd be delighted to work on differentiable manifolds with you.
```
I see no obstructions to finishing perfectoid spaces other than the fact that most of the people involved are extremely busy.

#### [Kevin Buzzard (Oct 10 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135569504):
Every issue we have come up against has been solved or will be solved soon.

#### [Jeremy Avigad (Oct 10 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135570753):
@Kevin, yes, of course, in Lean 3. Where else? 
@Patrick, thanks! There is no rush and of course I'd be happy to work together if/when you have time. I just want to make sure I am not stepping on anyone's toes in the meanwhile. The Banach fpt will indeed be helpful.

#### [Jeremy Avigad (Oct 15 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135800981):
Here's a little report on some things I learned about limits, filters, and set-valued functions this weekend.

Suppose we want to formalize the notion of a limit, and say `f x` approaches something as `x` approaches something. The problem is that there are lots of variations on the "somethings" -- `x` can approach a value or infinity or negative infinity, or it can approach a value from the left or the right, etc. 

The solution (described here http://home.informatik.tu-muenchen.de/~hoelzl/html-data/documents/hoelzl2013typeclasses.pdf and implemented by Johannes in `order/filter.lean`) is to write down a general relation `tendsto f l1 l2`, where `l1` and `l2` are filters. The relation `tendsto f l1 l2` asserts that the preimage of any set in `l2` under `f` is an element of `l1`. Instantiating `l1`, for example, with the filter of neighborhoods of a point `a`, we have convergence as `x` approaches `a`.

One issue that comes up when doing ordinary calculus is that often we want to restrict attention to a subset of the domain. Think of all the theorems about a function `f` that is continuous or differentiable on a closed interval `[a, b]`. When assessing continuity at `a`, we want to ignore anything outside the interval. The filter technology gives a means of doing this; replacing `l1` by `inf l1 (principal s)` restricts the domain to `s`. The Isabelle library proves all the basic theorems with such restrictions. Replacing `s` by `univ` results in the unqualified version.

Mario pointed out to me that sometimes, when working with an interval `[a, b]`, it is more natural to work with a partial function `f` on that domain, rather than a total function taking arbitrary values. He has defined `data/pfun.lean` for that purpose. Working with it is rather pleasant; you write `y ∈ f x` to say that `f` is defined at `x` and equal to `y`.

The relation `tendsto` generalizes to a relation `ptendsto` for partial functions, and if we define `res f s` to be the restriction of a total function `f` to a partial function with domain `s`, we have
```
tendsto f (l₁ ⊓ principal s) l₂ ↔ ptendsto (pfun.res f s) l₁ l₂
```
Here both sides say that `f` tends to `l₂` along `l₁` when the domain is restricted to `s`, but they say it is different ways: the lhs restricts the filter, and the rhs restricts the function. We recover the usual notion of convergence when `s` is `univ`, so in a sense working with partial functions is more general, and it avoids the need to mention `s` explicitly everywhere.

There is a catch, however. When generalizing the `tendsto` relation, one has to generalize the notion of a `preimage` to partial functions. Here there are two choices for the preimage of `f` on `s`: we can define it as `{x | ∃ a ∈ f x, a ∈ s}` or `{x | ∀ a ∈ f x, a ∈ s}`. The first one may seem more natural, but it is the second one, which basically adds all the values outside the domain of `f` to the first, which gives the equivalence above.

The plot thickens. In set-valued analysis, one further generalizes partial functions to "set-valued functions," which map a value `x` to a set of values -- possibly the empty set, possibly a singleton, and possibly lots of values. A set-valued function from `α` to `β` is really just a relation, but thinking of it as a multi-valued function suggests natural and useful generalizations of definitions and theorems in ordinary analysis, as described in this classic book: https://www.springer.com/la/book/9780817648473.

Here is the kicker: both versions of `preimage` suggested above generalize to relations, and both are considered in set-valued analysis:
```
def rel (α : Type*) (β : Type*):= α → β → Prop

namespace rel

variable (r : rel α β)

def preimage (s : set β) := {x | ∃ y ∈ s, r x y}

def core (s : set β) := {x | ∀ y, r x y → y ∈ s}

end rel
```
They give rise to two different notations of convergence. When talking about sequences of sets, the two notions are called "liminf" and "limsup". When used to define continuity of set-valued functions, we get "lower semicontinuity" and "upper continuity". 

I implemented the general notions of convergence as `rtendsto` and `rtendsto'` in this file: https://github.com/avigad/mathlib/blob/multivariate/analysis/multivariate/limit.lean. (Here the "r" is for relation.) At the very end, both versions are easily shown to be equivalent to `tendsto` in the function case, but in general, the two notions are different. In the case of a partial function, the definition is easily shown to be equivalent to `ptendsto` as defined above.

The bottom line: it seems to me that the fundamental notions of convergence we use should the be relational (set-valued) versions. They strictly generalize the cases of functions and partial functions, but it seems they are no harder to work with. I am inclined to stick with the general versions until there is good reason to specialize, and then to stick with partial functions unless/until there is good reason to restrict to functions.

@**Johannes Hölzl** , @**Mario Carneiro** , what do you think?

#### [Floris van Doorn (Oct 15 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135806766):
Could you explain briefly why we want to generalize to set-valued functions?

#### [Kevin Buzzard (Oct 15 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135812012):
I haven't even got more than a few lines into this post and already I've learnt a ton of stuff; I'm currently looking at the "Type classes and filters..." papers by Johannes et al linked to at the top.

1) @**Mario Carneiro** you and me and others were talking about why the ordering on filters was the opposite of the naive inclusion ordering recently; a very clear and coherent answer is at the top of p7 of the pdf Jeremy links to.

2) @**Patrick Massot** remember when we were discussing how one was supposed to pronounce `tendsto`, this fundamental relationship between filters in Lean, and I asked you what the notation was for it in Bourbaki and what terminology they used, and I think neither of us knew and we agreed to go and look it up and then neither of us did? It is described on p8 of this pdf (as `LIM` or `filterlime`). But see p2: "While filters have long been used to express limits in topology, our generic limit operator parameterized by two filters is novel (see Section 4.2)." :O Maybe it's not actually in Bourbaki! It seemed like such a natural notion that I assumed it was as old as the hills! Is this due to Johannes et al? Did you know this already? I've only just realised.

I think I'd seen this paper before, but now I have a much better understanding of a filter I got a lot more from it.

#### [Mario Carneiro (Oct 15 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135812795):
No, I didn't know that about the two filters thing. But as a student it's hard to get *any* exposure to filters; for some reason mathematics teachers everywhere believe that filters are too complicated for anything before grad school, and think that 30 variations on L'Hopital's rule is easier...?

#### [Mario Carneiro (Oct 15 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135812874):
(Needless to say I heartily disagree. I put filters at the same level of abstraction as topological spaces, and I think they should be taught together.)

#### [Kevin Buzzard (Oct 15 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813295):
Some notes  for mathematicians on Jeremy's post; in `data/pfun.lean` there is a variant of `option` defined, called `roption`, which is noncomputably equivalent to `option`. One way of thinking about `option A` in classical maths is that it's the set of subsets of `A` of size at most 1 (so it's `A` plus one extra element, here modelled as the empty set). A partial function $$A\to B$$ is just a function `A -> option B` (they use `roption` but I am too blinded by 30 years of classical mathematics to understand the difference properly) and the interpretation of `option B` as subsets of size at most 1 explains the observation Jeremy refers to as pleasant (and indeed it is pleasant). The "catch" Jeremy is talking about comes from the fact that with subsingletons (sets of size at most 1) the difference between exists and forall is that the empty set works with forall but not exists. 

This subtlety that Jeremy has uncovered (choosing exists or forall when defining preimage) leads to there being two natural ways to do some things at this hugely abstract level, and he's observing that these two choices give rise to things like liminf and limsup. If you had asked me about this stuff last year I would have said "oh I'm sure it's all in Bourbaki somewhere" but I am genuinely now wondering if this is actually new mathematics. Can anyone here come up with some dusty old book from the 70s where it's all done like this to show these computer science people that they're re-inventing the wheel?  Or are they actually inventing the wheel?

#### [Mario Carneiro (Oct 15 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813542):
Well, the problem with the exists definition of preimage is that it doesn't define a filter

#### [Mario Carneiro (Oct 15 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813549):
because the preimage of univ under a partial function is not univ

#### [Kevin Buzzard (Oct 15 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813561):
you can look at the filter generated by this?

#### [Mario Carneiro (Oct 15 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813606):
Classically that's the same as this other preimage

#### [Kevin Buzzard (Oct 15 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813611):
I thought you were going to say that

#### [Mario Carneiro (Oct 15 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813633):
I don't know if this will help, but I think that A -> roption B is actually the "real" partial function the way mathematicians think of it

#### [Mario Carneiro (Oct 15 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813686):
Originally I defined a partial function as a subset of the domain and a function on that subset, but it's equivalent to A -> roption B

#### [Mario Carneiro (Oct 15 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813691):
It is A -> option B that is the weird one

#### [Mario Carneiro (Oct 15 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813703):
When was the last time you totalized your partial functions by adding a new value outside the original domain as a "null" value?

#### [Kevin Buzzard (Oct 15 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813718):
```quote
(Needless to say I heartily disagree. I put filters at the same level of abstraction as topological spaces, and I think they should be taught together.)
```
I have already suggested that filters would be a great second year project topic in our department.

#### [Kevin Buzzard (Oct 15 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135813838):
They've already taught me what it means for a map between topological spaces to be continuous at a point. I was talking to a lecturer at another UK university last month and they explicitly raised this issue -- they were covering for the topology guy in a lecture, and were given his notes to read out, and the notes explicitly said that there was no notion of being continuous at a point for a map between topological spaces.

#### [Patrick Massot (Oct 15 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135816439):
That paper by Johannes has been cited countless times here on Zulip (and previously on gitter). I think it's the first Lean-related paper I ever printed.

#### [Patrick Massot (Oct 15 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135816497):
And indeed I wasn't able to find the general `tendsto` definition in Bourbaki

#### [Kevin Buzzard (Oct 15 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135831590):
Yes I've certainly seen it before. But this is the first time I looked at it since I learnt about some of that filter stuff.

#### [Kevin Buzzard (Oct 15 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135831637):
I actually understand the point of it now!

#### [Kevin Buzzard (Oct 15 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135832009):
You computer scientists attach value to a completely different set of data to us. For you the theory of filters on a type is some beautiful tool which can help you to make other stuff. I don't think we attach much value to that theory at all. I think it's cool but if you ask me if it's in Bourbaki I would just say I don't know and don't really care, I'm sure it all works great and let's get on with the good stuff. I attach value to the Riemann Hypothesis, some random statement about the zeros of some completely randomly-defined function which is a pain to formalise because it involves analytic continuation but which at the end of the day is no different to any other function really, and the main point seems to be just that humans are worse at finding the zeros for that Riemann function than for some other functions like the identity function.

#### [Jeremy Avigad (Oct 16 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135865554):
@**Floris van Doorn** @**Kevin Buzzard**  I haven't spent much time with it yet, but the book I linked to is a very nice introduction, and the opening chapter makes a good case for the generalization. CMU's library has an electronic copy, and I'd be glad to share it with you.
@**Floris van Doorn** If you Google around a bit, you'll see that the notion of a set-valued function gets used quite a lot in various branches of applied mathematics. For example, it is used to generalize differential questions to cases where instead of having a unique trajectory you only have some bounds on the possible evolutions of the system (https://en.wikipedia.org/wiki/Differential_inclusion, https://bookstore.ams.org/gsm-41). It is used in optimization problems, where a given parameterized problem can have multiple optimum values (https://www.springer.com/us/book/9783642542640). It is used in nonsmooth convex analysis to generalize the derivative to the case where there can be multiple "tangent lines" beneath a curve (https://en.wikipedia.org/wiki/Subderivative, https://www.degruyter.com/view/product/467711). 
By the way, I think branches of applied mathematics like these are good targets for interactive theorem proving: not only is there a lot of symbolic and numeric computation, but the models tend to be complicated and unruly, and one can imagine that a interactive system can help people reason about them rigorously.
That said, my goal isn't to do any of that right away, only develop the notions of limit in as great a generality as conveniently possible while heading toordinary (function-based) analysis.
@**Kevin Buzzard**  I wrote down the notion of a preimage that would make the theorem go through, and I was delighted to find essentially that notion in the book, at least in the particular setting they treat there. I don't think it is radically new or deep mathematics, but it is a nice was of organizing and unifying concepts. This happens a lot with formalization, and I am glad that you find it an interesting and valuable aspect of the whole business.

#### [Jeremy Avigad (Oct 16 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135865604):
By the way, I seem to be incapable of writing a short Zulip post. Sorry about that.

#### [Scott Morrison (Oct 16 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135870229):
(We had to train Kevin to remember to hit enter. :-)

#### [Mario Carneiro (Oct 16 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/135870388):
but not too much

#### [Jeremy Avigad (Nov 08 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147272989):
Here is a progress report on a library for multivariate analysis. I wrote down the definition of the Frechet derivative, but before doing anything with that, I decided to expand the library for limits. It has taken more time than I thought it would. Currently everything is in one file in a branch on `leanprover_community`, https://github.com/leanprover-community/mathlib/blob/multivariate/analysis/multivariate/limit.lean.
It includes:
* operations like `dom`, `codom`, `image`, `preimage`, and `core` for relations and partial functions, and relationships to the notions for functions.
* generalizations of `tendsto` to relations (`rtendsto` and `rtendsto'`) and partial functions (`ptendsto`) and relationships between them.
* a filter for convergence at a point: `tendsto f (at_within a s) l` means that `f x` approaches `l` as `x` approaches `a` within the set `s`. We define `at_pt a := at_within a univ`. Note that we need to use "punctured" neighborhoods of `a`. For example, if `f x := if x = 0 then 1 else 0` we want `tendsto f (at_pt 0) (nhds 0)`.
* Characterizations of `at_within a s` in terms of subtypes. For example, given `a` in a set `s`, we have `tendsto f (at_within a s) l ↔ tendsto (f ∘ (@subtype.val _ s)) (at_pt ⟨a, h⟩) l`. Roughly, `f` converges to `l` as `x` approaches `a` within `s` if and only `f` restricted to `subtype s` converges to `l` as `x` approach `a` on that subtype.
* Unwrapping the definition of convergence at a point `a` within a set `s` in a metric space.
I plan to develop properties of pointwise continuity along these lines (restricted to sets, on subtypes, with partial functions, etc., etc.) and then put these things in appropriate places and issue a pull request. And THEN I'll move on to derivatives.
Comments and suggestions are welcome.

#### [Mario Carneiro (Nov 08 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147274679):
The move toward a `rel` type is unexpected, but I can see that we don't have as much as might be expected. As far as integrating it with mathlib, I would want to have a proof that `rel A B` is a complete lattice, and maybe we could use it for uniformities (once my work on generalizing filters to other lattices lands)

#### [Mario Carneiro (Nov 08 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147275134):
Also I've mentioned this to you personally, but I would like to minimize the use of `at_pt` and `at_within` in our main developments where possible. I think that "punctured neighborhoods" make some undesirable hidden assumptions about separation properties of the underlying topological space, and overall they lead to additional complications. Of course they are necessary in some cases, particularly in functions that divide by zero at the limit point, but in particular they aren't needed for saying that a function is continuous at a point.

#### [Sebastien Gouezel (Nov 08 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147283724):
```quote
* generalizations of `tendsto` to relations (`rtendsto` and `rtendsto'`) and partial functions (`ptendsto`) and relationships between them.
* a filter for convergence at a point: `tendsto f (at_within a s) l` means that `f x` approaches `l` as `x` approaches `a` within the set `s`. We define `at_pt a := at_within a univ`. Note that we need to use "punctured" neighborhoods of `a`. For example, if `f x := if x = 0 then 1 else 0` we want `tendsto f (at_pt 0) (nhds)`
```
I would like to argue strongly against the use of punctured neighborhoods. For instance, in your last example, I definitely wouldn't want that `f` tends to `0` at `0`, because, well, it does not, for the commonly accepted definition of limit :)

I don't recall any instance in research mathematics where I have seen punctured neighborhoods: they are mainly used in undergraduate courses to define the derivative as `lim (f (x+h) - f(x))/h`when `h` tends to 0 and is different from `0`. However, when you do Frechet derivatives you can also write this as `f(x+h) = f(x) + Df(x) h + o(h)` (where by `o(h)` I mean the norm of `h` multiplied by a function which tends to 0 at 0). And then you don' need to divide by 0 any more.

On the other hand, plain neighborhoods are used all the time. That created a lot of issues for me in Isabelle when working with the analysis library, designed using punctured neighborhoods: I had to argue separately about the value at the point and the value in the punctured neighborhoods many many times. I would have been much more happy with some unpunctured `nhds_within a s`. 

Any thoughts?

#### [Patrick Massot (Nov 08 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147285332):
I also vote for keeping unpunctured neighborhoods as the default. The general filter machinery can then allow to use punctured neighborhoods in the rare cases where this is useful.

#### [Mario Carneiro (Nov 08 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147285403):
It's interesting to hear that @**Sebastien Gouezel** , I had a conversation about this with Jeremy and he used Isabelle as a model for a lot of this, based on his previous experiences with the Isabelle analysis library

#### [Johannes Hölzl (Nov 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147286545):
I think using `nhds` is much easier. The main reason for me is that composition is easier: `tendsto f (nhds x) (nhds y)` `tendsto g (nhds y) (nhds z)` composes nicely using just `tendsto.comp` while the `at` statements are `tendsto f (at x) (nhds y)` and then one needs a special composition rule. This doesn't happen only for `tendsto` but at other occasions too.

#### [Sebastien Gouezel (Nov 08 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147286728):
I want to emphasize that Isabelle multivariate analysis is absolutely wonderful. Extremely well designed and handy to use. The only point that made me pester is the use of punctured neighborhoods. So, using Isabelle's library as a model looks like an excellent idea. And if you could remove the overuse of punctured neighborhoods to make it even better, I would be all the more happy.

#### [Mario Carneiro (Nov 08 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287093):
well, if we aren't using punctured neighborhoods then we should discuss the alternative. The main application, I believe, is for derivatives of various kinds, where you have to divide by zero

#### [Mario Carneiro (Nov 08 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287172):
In metamath I got around this by saying "the function `g(h) = if h = 0 then c else (f(x+h) - f(x))/h` is continuous at zero", which uses only regular neighborhoods

#### [Mario Carneiro (Nov 08 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287224):
(here `c` is the claimed derivative of f at x)

#### [Sebastien Gouezel (Nov 08 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287780):
A linear map `L` is a derivative of `f`at the point `x` along the set `s` if `(f(y)-f(x)-L (y-x))/norm(y-x)` tends to `0` when `y` tends to `x` along `s`. This works since `0/0 = 0`.

#### [Patrick Massot (Nov 08 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287876):
And why dividing? Why not using the little-o definition?

#### [Mario Carneiro (Nov 08 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287882):
I remember you wrote something like that in your definition patrick

#### [Mario Carneiro (Nov 08 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287887):
but I think the little o function is basically unique

#### [Patrick Massot (Nov 08 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287892):
https://github.com/math-comp/analysis/blob/master/derive.v#L48

#### [Mario Carneiro (Nov 08 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287899):
and you have to write it with division anyway

#### [Patrick Massot (Nov 08 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287909):
why?

#### [Mario Carneiro (Nov 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287956):
how else are you going to prove that this function exists in a concrete situation?

#### [Patrick Massot (Nov 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287964):
And what do you mean "I wrote something like this"? I wrote https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean#L18

#### [Mario Carneiro (Nov 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287975):
right, that

#### [Patrick Massot (Nov 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287976):
And I wrote this because I didn't have a little-o library

#### [Mario Carneiro (Nov 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287980):
that epsilon function is unique

#### [Sebastien Gouezel (Nov 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287981):
I prefer the definition with little o, I am only afraid it requires more work to set up. But it avoids division, which is definitely a big plus.

#### [Mario Carneiro (Nov 08 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287983):
and it's a division

#### [Mario Carneiro (Nov 08 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287990):
so you may as well eliminate it

#### [Patrick Massot (Nov 08 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147287998):
Sébastien, have you seen https://hal.inria.fr/hal-01719918?

#### [Mario Carneiro (Nov 08 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288004):
I am on board if you can find a way to actually avoid division, but I don't think this achieves that

#### [Patrick Massot (Nov 08 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288049):
Of course it requires more setup but we need little-o and big-O anyway.

#### [Mario Carneiro (Nov 08 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288063):
this part -> `∃ ε : E → F, (∀ h, f (a + h) = f a + L h + ∥h∥ • ε h)` can only be satisfied for one function epsilon

#### [Mario Carneiro (Nov 08 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288071):
it's too strict

#### [Patrick Massot (Nov 08 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288078):
Of course, but why would you care?

#### [Patrick Massot (Nov 08 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288084):
And anyway I want little-o instead

#### [Patrick Massot (Nov 08 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288090):
I want this proof: https://github.com/math-comp/analysis/blob/master/derive.v#L687

#### [Mario Carneiro (Nov 08 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288091):
because then it isn't really avoiding division, it's just hiding it

#### [Mario Carneiro (Nov 08 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288098):
and it comes back whenever you actually want to apply the definition

#### [Sebastien Gouezel (Nov 08 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288101):
```quote
Sébastien, have you seen https://hal.inria.fr/hal-01719918?
```
This has been available for a long time in Isabelle :) And Isabelle will also compute limits automatically for you, i.e., it has tactics to compute the limit, say, of `(sin x + cos x - e^x)/x^2` at `0`. Or at infinity. Or whatever.

#### [Patrick Massot (Nov 08 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288265):
They claim to do better little-o/big-O than Isabelle. Have you read it in detail?

#### [Patrick Massot (Nov 08 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288273):
Mario, the discussion about what I wrote in my calculus file is a bit pointless, this will soon be replaced by using little-o

#### [Sebastien Gouezel (Nov 08 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288274):
No, I have not read the details (yet). And the limits tactics for Isabelle is very recent, to be honest.

#### [Patrick Massot (Nov 08 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288373):
There is very preliminary work on porting this to Lean in https://github.com/leanprover-community/mathlib/blob/landau/analysis/landau.lean (but it's currently a mess so don't look at it too closely)

#### [Mario Carneiro (Nov 08 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288449):
I don't think being little o or not matters, it's the same definition with a different name

#### [Mario Carneiro (Nov 08 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288648):
What about a definition like: for all `ε > 0`, for all `h` near `nhds 0`, `|f (a + h) - f a - L h| <= ε |h|`

#### [Patrick Massot (Nov 08 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288651):
Then I don't see how you would need to divide whenever you want to apply the definition. Let's try to prove that the identity on R is differentiable at 0, with derivative id. Then the definition asks you check that 0 is o(x). This is done in https://github.com/leanprover-community/mathlib/blob/landau/analysis/landau.lean#L26. Where do you see a division by x?

#### [Patrick Massot (Nov 08 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288703):
Mario, what you wrote is exactly the little-o definition!

#### [Patrick Massot (Nov 08 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288721):
Maybe the confusion comes from the fact we don't share the same definition of little-o

#### [Mario Carneiro (Nov 08 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288726):
yes, I see that this matches your little o definition

#### [Mario Carneiro (Nov 08 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288783):
However I'm not yet convinced of the `mklittleo` thing

#### [Mario Carneiro (Nov 08 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288787):
I think it is best to just use the definition

#### [Patrick Massot (Nov 08 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288810):
I'm tempted to first try to trust Cyril and its collaborators

#### [Mario Carneiro (Nov 08 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288849):
was this file Cyril's work in Freiburg?

#### [Patrick Massot (Nov 08 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288856):
He helped me write it, but all the ugly parts are solely my mistake

#### [Patrick Massot (Nov 08 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288861):
He also helped me with big op and worked on parametricity

#### [Mario Carneiro (Nov 08 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288871):
specifically, I don't think lean's notations will let us do the same trickery that coq does

#### [Patrick Massot (Nov 08 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147288882):
Some stuff work better with Lean parser, some work better in Coq

#### [Jeremy Avigad (Nov 08 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147301608):
Serves me right for posting a message before going to sleep -- I missed all the fun discussion.

Regarding `rel`, there are two motivations for introducing it. First, when you are working with relations, it is a lot more pleasant to write `rel α β` than to write `α → β → Prop` repeatedly, and it is pleasant to be able to write `r.image`, `r.preimage`, `r.dom`, `r.codom`, etc. (So much so that I started withing that Lean had the convention that function types were implictly associated to the `function` namespace, so we could write `f.image`, `f.preimage`, etc. I have decided that I don't really like the `f '' s` and `f ⁻¹' s` notation, and I will start favoring `s.image` or `set.image f s` unless someone talks me out of it.) 

I don't feel strongly that the library needs a calculus for relations, and I wouldn't mind keeping it in reserve until a compelling need arises. But if we do have one, I think `rel` is the way to go. So, if there are no objections, I'll follow Mario's suggestion and make it a lattice instance and prepare it for the library.

#### [Jeremy Avigad (Nov 08 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147302883):
Setting aside the puncturing issue for a moment, I'll remind readers that `at_within a s` is basically just `nds a ⊓ principal s`. The point is that we want to say "f is differentiable on [a, b]" where "differentiable at a" is independent of what f does outside the interval. As far as I can tell, there are three options:

* Use "at_within" to restrict the domain of interest.
* Lift f to a subtype, and make the statement about the subtype.
* Restrict f to [a,b] to get a partial function, and make the statement about the partial function.

I am most hopeful about the first approach. In my experience with Isabelle, it was easy, intuitive, and natural to relativize statements to sets. But my plan is to support all three in the library and prove equivalences, so we can try all the different approaches and go with whatever works best. 

As far as subtypes, packing and unpacking information can be a royal pain in the neck, and for many purposes, like taking intersections or translating sets, we really want [a, b] to be a subset rather than a subtype. Also, as Mario pointed out to me, for some purposes it doesn't work: to define the derivative, we need a subtraction on the domain, and you don't get that if you restrict to a subtype.

Mario seems to think that the third approach will prove the most useful. I am not yet convinced, but I added all the pfun stuff to support it. To see what I am concerned about, take a look at the definition of the Frechet derivative, and now imagine what has to change if f is a partial function. All the operations on the codomain -- addition, substraction, scalar multiplication, the norm -- have to be lifted to partial functions as well. I am not convinced that it will be possible to do all the calculations in a reasonable way, even with some monad trickery, and that it will be worth it.

Anyhow, as I said, my plan is to develop the infrastructure and give it a try as long as it does not make progress too painful.

#### [Jeremy Avigad (Nov 08 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147303319):
Finally, regarding the "puncturing" issue, I have no strong opinions here. As Johannes points out, it is often easier without it. If we take `at_within a s` with the definition above, we can have the punctured version with `at_within a (s \ {a})` if and when we need it.

I don't have my copy of Munkres handy, but I thought the punctured definition was mathematically standard. Googling around supports that:
https://math.stackexchange.com/questions/1019388/why-are-punctured-neighborhoods-in-the-definition-of-the-limit-of-a-function/1019418
https://en.wikipedia.org/wiki/Limit_(mathematics)#Limit_of_a_function
But if nobody will stand up for it, I'll give "at_within" the simpler definition and work with that.

#### [Jeremy Avigad (Nov 08 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147303439):
Oh, I'll also change the name "at_within" to "nhds_within". It is a better description of the new definition.

#### [Kevin Buzzard (Nov 08 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147304121):
Just my two cents about punctured neighbourhoods -- I am not an analyst, but my impression is that one sees this punctured neighbourhood stuff precisely at the very beginning when one is formalising limits, and then it very quickly drops off the radar, not least because in practice 99% of functions which 99% of mathematicians deal with are continuous/differentiable/whatever so the issue doesn't *seem* to come up, at least on the informal level where mathematicians usually work. I am pretty sure that the only time we saw this punctured neighbourhood definition in my mathematical upbringing was in the very first course I took on limits.

#### [Jeremy Avigad (Nov 08 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147304208):
That speaks in favor of making the simpler `nhds_within` fundamental, and puncturing explicitly only when we really need to.

#### [Jeremy Avigad (Nov 08 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147305049):
BTW, @**Johannes Hölzl**, I have a new appreciation for `filter.comap`. It is quite natural for reasoning about induced topologies and subspace topologies:
```
theorem nhds_induced [T : topological_space α] (f : β → α) (a : β) : 
  @nhds β (topological_space.induced f T) a = comap f (nhds (f a)) := ...

theorem nhds_subtype (s : set α) (a : {x // x ∈ s}) :
  nhds a = comap subtype.val (nhds a.val) :=
by rw nhds_induced
```

#### [Johannes Hölzl (Nov 08 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147309063):
@**Jeremy Avigad** 
```quote
I have a new appreciation for `filter.comap`.
```
Heh, yes I had the same revelation. I originally introduced it for a special case in uniform spaces. Only later I realized that it is a quiet nice way to express many operations (especially `tendsto` and `prod`). I think Manuel Eberl had a similar experience.

#### [Johannes Hölzl (Nov 08 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147309411):
+1 for `nhds_within`, I also like `rel A B`. There are already complete lattice instances for `Prop` and for `->`, so its just about unfolding the definition and using `apply_instance` to get the complete lattice instance

#### [Cyril Cohen (Nov 08 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147315179):
@**Jeremy Avigad** In my experience, keeping total functions, not using subtyping, and passing the domain around as a predicate (i.e. your solution 1) is the most usable presentation, at least in mathcomp...

#### [Jeremy Avigad (Nov 08 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147317356):
That's helpful to hear. I'll try to keep an open mind, but it is good to know that there is at least one workable approach.

#### [Patrick Massot (Nov 08 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147321129):
Jeremy, I don't know uses of calculus for relations, but if you want to develop stuff about relation, you should have a look at the beginning of https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean to see what can be reused or refactored

#### [Patrick Massot (Nov 08 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147321463):
`filter.comap` is indeed essential when working with subspaces and quotients. It's used all over https://github.com/leanprover/mathlib/blob/master/analysis/topology/completion.lean. It also plays a central role for topological group (the uniform structure is defined using comap, see https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_groups.lean#L27)

#### [Jeremy Avigad (Nov 08 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147322250):
Interesting. This raises the question as to whether `rel A B` should be `A x B -> Prop` (definitionally the same as `set (A x B)`) or `A -> B -> Prop`. I find the second to be a lot more convenient, but the uniform_spaces library uses the first. I suppose I can see what happens if I replace `set (A x B)` by my `rel A B` in the uniform spaces library, but rewriting that whole library and everything that depends on it doesn't sounds like fun. 

@**Johannes Hölzl**, what do you think? Maybe that should be a project for a rainy day?

#### [Patrick Massot (Nov 08 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147322408):
```quote
I have decided that I don't really like the `f '' s` and `f ⁻¹' s` notation, and I will start favoring `s.image` or `set.image f s` unless someone talks me out of it.) 
```
I'd like to try to talk you out of using `s.image f` instead of `f '' s` (and `s.preimage f` instead of `f ⁻¹' s`). I don't like these notations, but the alternative really seems attached to the wrong object. It's really a functor attached to `f` and applied on `s`, not the other way around. I think there is no good functoriality property of `s.image`.

#### [Patrick Massot (Nov 08 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147322498):
Same with filters actually. If `F` is a filter on `a` and `f : a -> b` then `map f F` is really the functor `f_*` applied to `F`.

#### [Patrick Massot (Nov 08 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147322513):
The notation `F.map f` feels really weird

#### [Jeremy Avigad (Nov 08 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147323162):
I know, I really wish I could write `f.image s`. O.k., maybe I'll just give up and use the notations.

#### [Reid Barton (Nov 08 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147324231):
`image f s` is also fine, I would say

#### [Reid Barton (Nov 08 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147324315):
Can Lean disambiguate that from other things called `image` based on the type of `s`?

#### [Reid Barton (Nov 08 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147324342):
(I assume you would have the `set` namespace open, but perhaps not?)

#### [Jeremy Avigad (Nov 08 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147325931):
I usually don't open any more namespaces than I have to, but I can open it, or use `open set (image)`, or just write `set.image f s`.

#### [Patrick Massot (Nov 09 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147358107):
I should also point out that, although I don't see a need for calculus for relations right now, I do see a big need for differentiation of partially defined functions. The (traditional) definition of differentiable manifolds is full of partially defined functions and restrictions of partially defined functions, see https://en.wikipedia.org/wiki/Differentiable_manifold#Atlases

#### [Mario Carneiro (Nov 09 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147358421):
Right, this is the real application

#### [Mario Carneiro (Nov 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147358433):
The thing is that the derivative of a function or partial function is a relation, not a function

#### [Mario Carneiro (Nov 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147358434):
so if you want something that you can iterate you end up in relations

#### [Mario Carneiro (Nov 09 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multivariate%20analysis/near/147358485):
It's not even a functional relation in some edge cases

