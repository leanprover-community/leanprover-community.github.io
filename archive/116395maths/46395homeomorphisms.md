---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/46395homeomorphisms.html
---

## [maths](index.html)
### [homeomorphisms](46395homeomorphisms.html)

#### [Reid Barton (Jun 01 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127431536):
@**Patrick Massot**, did you have a definition of homeomorphisms somewhere?

#### [Patrick Massot (Jun 01 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127431596):
https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/homeos.lean

#### [Reid Barton (Jun 01 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127432191):
thanks! I like this `extends equiv` idea

#### [Patrick Massot (Jun 01 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127435414):
This was Mario's idea. At that time I had no idea `equiv` existed

#### [Kenny Lau (Jun 01 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127435457):
just do it in a category man

#### [Kevin Buzzard (Jun 01 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437006):
won't there be universe issues?

#### [Kenny Lau (Jun 01 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437010):
just build a category theory without universe issue, man

#### [Kevin Buzzard (Jun 01 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437112):
I think Russell had something to say about that

#### [Kenny Lau (Jun 01 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437168):
the category itself as an object has universe issues

#### [Kenny Lau (Jun 01 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437170):
if you use the things within, you should be fine

#### [Kevin Buzzard (Jun 01 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437171):
I never really understood the issues that Scott had with universes but my impression is that things are harder than you might think

#### [Kenny Lau (Jun 01 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437173):
(there's a different category for each universe)

#### [Kenny Lau (Jun 01 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437175):
(but it doesn't matter)

#### [Kevin Buzzard (Jun 01 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437712):
my understanding is that sometimes it does matter

#### [Kevin Buzzard (Jun 01 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127437718):
because maybe you end up with the right object but in the wrong universe

#### [Scott Morrison (Jun 02 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127440872):
The problem with universes (which is the sole reason I didn't have a PR ready months ago) is that there are genuinely two different sorts of categories one needs in mathematics: "small categories", in which objects and morphisms live in the same fixed universe, and "large categories", in which objects get to live in one higher universe than the morphisms.

#### [Scott Morrison (Jun 02 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127440923):
For a very long time in my pre-Lean mathematical career, I thought this wasn't such a big deal, but I've learnt better. :-)

#### [Scott Morrison (Jun 02 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127441044):
(Briefly: we need large categories because all the basic algebra examples like `Types`, `Groups`, `PL`, etc are large. We need small categories because if you try thinking about any of the basic machinery in category theory, particularly taking limits, when you index over objects in a large category you find yourself having to move up the universe hierarchy over and over again, while when you index over objects in a small category you can stay at one level. Happily, one can get away with doing most of mathematics only having to index over a small category --- but not quite all, so eventually you need to admit that the universe parameter can vary across a development.)

#### [Scott Morrison (Jun 02 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127441103):
So, how to implement this? We don't want to have parallel developments of small and large categories, because then we'd have at least 3 different types of functors (small to small, small to large, large to large -- large to small is just silly, of course :-), and lifts between these, and then more mess at the level of transformations, and it will all end badly.

#### [Scott Morrison (Jun 02 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127441107):
The two options I considered were:

#### [Scott Morrison (Jun 02 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127441133):
1) "categories" by default have objects in `Type (u+1)` and morphisms in `Type u`, and a small category is a category along with the additional evidence that the objects are equivalent in something in `Type u` after all.

#### [Scott Morrison (Jun 02 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127441186):
2) We define "categories" to have two universe parameters, so objects live in `Type u` and morphisms in `Type v`, and define "small_category" and "large_category" as subclasses (with `u=v` and `u=v+1` respectively).

#### [Scott Morrison (Jun 02 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127441203):
In the end, it seems that 1) just doesn't work; I found that I was having to implement multiple sorts of functors and natural transformations anyway.

#### [Scott Morrison (Jun 02 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeomorphisms/near/127441301):
2) mostly works. You develop as much as you need at the level of "independent universe" categories, but then when it makes sense restrict to either `small_category` or `large_category`. Working entirely with independent universe categories becomes problematic, because Lean usually can't infer the morphism universe level. Mostly you can get around this just by specifying that level explicitly, but it also starts to break typeclass inference and so eventually becomes a serious problem.

