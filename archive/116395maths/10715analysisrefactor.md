---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/10715analysisrefactor.html
---

## Stream: [maths](index.html)
### Topic: [analysis refactor](10715analysisrefactor.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 21 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132541838):
@**Johannes Hölzl** If you have some time, I'd be interested to know what is the big plan underlying your recent mathilb commits

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Aug 21 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132541914):
Cleanup ennreal, and enhance nnreal. Change metrics and norms to nnreal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Aug 21 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132541930):
Another idea is to use Galois connections as cheap categorical constructions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 21 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132541949):
Didn't @**Sebastien Gouezel** make a convincing point of not doing that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 21 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132541963):
Where do you want to add Galois connections?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Aug 21 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542035):
Galois connections are already there. I "lift" along the `generate` / `sets` Galois connection (`generate g` produces the smallest filter/topology/measurable sets containing `g`, `sets` is the forgetful functor).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Aug 21 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542085):
This allows me to lift the complete lattice structure on `set` to topologies, filters, and measurable spaces. They were there before, but now we have a nicer construction.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Aug 21 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542099):
For `nnreal` I need to look at Sebastians argument again.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 21 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542120):
I know Galois connections are already there, I used filters quite a lot. I as asking about new uses.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 21 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542201):
(and I think I like the answer)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Aug 21 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542485):
I need to look at Sebastians argument more concretely. `dist` and `norm` will always return nonnegative numbers. So the difference is only that we pack this proof into the result type.  Subtracting on `nnreal` and `ennreal` is very ugly, but I don't see how this appears in a concrete case.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 21 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542604):
From https://github.com/leanprover/mathlib/pull/208#issuecomment-406893134 it's not hard to see where Sébastien encountered that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 21 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542614):
https://devel.isa-afp.org/entries/Gromov_Hyperbolicity.html

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 21 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542880):
> `abs(dist e a - dist e b)`

But surely `nnreal` is a metric space too? Why not just write `dist (dist e a) (dist e b)`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 21 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542975):
More generally, faced with a problem of the form "I have to do X a lot", maybe it's better to write a small convenience function to do X rather than distorting the underlying theory to avoid needing to do X.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 21 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132543209):
Maybe "distorting the underlying theory" is a bit exaggerated here. But really I have no idea about what should be done. I can only see that Sébastien did quite a lot of Gromov hyperbolic spaces in Isabelle, so this is a really concrete and battle tested opinion.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 21 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132543288):
Fair enough. In this case, it's not uncommon to see $$d(x, y) \ge 0$$ stated as an axiom of a metric space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 22 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132544270):
It's also not uncommon to see $$d:X\times X\to[0,\infty)$$. Honestly I don't think mathematicians have a mental structure that allows them to even distinguish these approaches, so I don't consider this good evidence in either direction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 22 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132544931):
I wonder whether it would help to have `has_sub a b` with `sub : a -> a -> b` with instances like `nat int` and `nnreal real`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 22 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132544936):
Or an affine space / vector space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 22 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132544944):
You can always write `(a - b : int)` where `a b : nat`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 22 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132544950):
same for `nnreal` and `real`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 22 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132544960):
indeed this is what I recommend if you want proper subtraction on one of these partial subtraction domains

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Aug 22 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132564296):
The most basic object in hyperbolic spaces is the Gromov product of two points `x`and `y` with basepoint `e`, defined as `(d(e, x) + d(e, y) - d(x,y))/2`. And one keeps computing with such objects, adding, subtracting or comparing them. All these computations are really much more convenient in reals than nnreals, although I guess they could most of the time be done in nnreals, at the price of making the proofs much more painful (for instance, in the definition of the Gromov product, the triangular inequality shows that `d(x, y) ≤ d(e,x) + d(e,y)`, so that the definition in reals or nnreals gives the same result, at least if one parenthesises the expression correctly). 
In fact, at the beginning I defined the Gromov product to be in `nnreal`, but later on I had to refactor everything as it made things uselessly complicated.

For the general issue, making distances and norms take values in `nnreal` would mathematically be the right thing to do. But I am not convinced that the benefits outweigh the difficulties in applications. As a middle ground, one could have two functions `nndist` and `dist`. Another related question is to have distances even taking values in `ennreal`. I think this is important to have, for instance to define the graph distance on a non-connected graph, or the `L^2` norm of a function which is not square-integrable (these are two real-life problems that I met in Isabelle and where I was stuck with the current hierarchy). Maybe a class `emetric_space` with distances taking values in `ennreal` (this is enough to define for instance a uniform structure, a topology, and so on), and a subclass `metric_space` in which the distance only takes finite values?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 22 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132581506):
Thanks for the more detailed example. Having both `nndist` and `dist` is a good option, in which case it may not even matter which of `dist` or `nndist` is taken to be part of the defining structure of a metric space. The potential cost is wanting two versions of all the lemmas about `nndist`/`dist`, but this kind of problem I feel could be solvable in the long run with better tools.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 22 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132581576):
Also totally agree with your second paragraph. An even more basic example is the extended metric space of (not necessarily bounded) functions from a given set to a given metric space, with the sup/uniform metric.

