---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/73938bicategories.html
---

## Stream: [maths](index.html)
### Topic: [bicategories](73938bicategories.html)

---

#### [Reid Barton (Oct 10 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502092):
@**Scott Morrison|110087** have you by any chance done or thought about formalizing bicategories?

#### [Reid Barton (Oct 10 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502151):
I know you have monoidal categories somewhere which is in approximately the same direction

#### [Scott Morrison (Oct 10 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502652):
Yes, I'd like to, but have done nothing.

#### [Scott Morrison (Oct 10 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502667):
I've been meaning to rewrite the work on monoidal categories for a while now, as it's an excellent playground for my student Keeley Hoek's "rewrite_search" algorithms.

#### [Scott Morrison (Oct 10 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502740):
I think the lesson I eventually learnt there is that defining a monoidal category as a category `C` equipped with a functor `C x C to C` is actually a bad idea, mostly for syntactic reasons! I think it will work much better if you have have operations tensor_obj and tensor_hom, and laws for them, etc, then have a theorem that packages these as a functor when needed.

#### [Scott Morrison (Oct 10 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502772):
The basic problem is just that if you think of tensor as a functor out of C x C, then its argument is a pair, and you'd really really prefer the curried version of these for parsing, pattern matching, etc. Dealing with the pairs causes lots of pain.

#### [Reid Barton (Oct 10 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502818):
Hmm, makes sense...

#### [Scott Morrison (Oct 10 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502824):
It is a bit sad though that this is a significant consideration.

#### [Reid Barton (Oct 10 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502843):
https://ncatlab.org/nlab/show/bicategory#detailedDefn

#### [Scott Morrison (Oct 10 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502904):
> The point is not that one would want to write out the definition in such elementary terms (although apparently I just did anyway) but rather that one can.

#### [Scott Morrison (Oct 10 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135502923):
In a different direction, I would love to do (have someone do?) quasi-strict categories (according to Vicary), as a foundation for hooking up Lean and Globular.

#### [Reid Barton (Oct 10 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135503213):
Right, I think we talked about this briefly in Orsay

#### [Reid Barton (Oct 10 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135507318):
I suppose a possible alternative to `C x C -> C` is a curried functor `C => (C => C)`, though I don't have a clear sense of the issues here yet

#### [Scott Morrison (Oct 10 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135508059):
I suspect, although haven't actually checked, that this is just as bad. Because `F X` is handled via a coercion, rather than merely notation, I suspect we could never get `T X Y` to work for a curried functor.

#### [Mario Carneiro (Oct 10 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135510023):
I think the curried functor should work fine

#### [David Michael Roberts (Oct 10 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135520001):
Why not use the dependently-typed definition of bicategory a la an enriched category?

#### [David Michael Roberts (Oct 10 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135520083):
As in, something like `obj1:Obj obj2:Obj |- Hom_obj1_obj2 : Cat` and then apply whatever solution makes the monoidal case work, modulo adapting to multiple objects?

#### [Reid Barton (Oct 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bicategories/near/135530891):
I think the issue is that we don't have a nice solution for monoidal categories, that doesn't require a structure with ~30 fields

