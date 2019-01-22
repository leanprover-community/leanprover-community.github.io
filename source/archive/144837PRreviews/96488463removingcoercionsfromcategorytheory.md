---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/96488463removingcoercionsfromcategorytheory.html
---

## [PR reviews](index.html)
### [#463 removing coercions from category_theory/](96488463removingcoercionsfromcategorytheory.html)

#### [Scott Morrison (Nov 07 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146929906):
For your consideration, @**Mario Carneiro**, @**Johannes Hölzl**, @**Johan Commelin**, @**Reid Barton**, @**Michael Jendrusch**.

I propose removing all the coercions. It only took about 20 minutes to take them out, and I think overall it already simplifies the mathlib code, and will simplify lots of other things going forward.

#### [Scott Morrison (Nov 07 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146929916):
The cost is having to write `F.obj X` instead of `F X`, and having to write `t.app X` instead of `t X`.

#### [Scott Morrison (Nov 07 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146929959):
The benefit is not having to work out why `F X` doesn't work some fraction of the time.

#### [Scott Morrison (Nov 07 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146929965):
and not having to jump through hoops with extra variations of structure fields, to introduce coercions.

#### [Scott Morrison (Nov 07 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146929970):
and ... various other things as discussed in recent threads.

#### [Scott Morrison (Nov 07 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146929985):
https://github.com/leanprover/mathlib/pull/463/files

#### [Scott Morrison (Nov 07 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146929990):
Notice that overall it reduces the codebase: +247 −317

#### [Kevin Buzzard (Nov 07 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146930066):
I don't really see this as a cost. It's sort-of how I think of functors anyway :-)

#### [Kenny Lau (Nov 07 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146930864):
@**Mario Carneiro** do you think this will also benefit modules?

#### [Johan Commelin (Nov 07 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146931051):
@**Scott Morrison|110087** I think this is totally fine. In the sheaf stuff I've already avoided coercions; it wasn't too painful.

#### [Mario Carneiro (Nov 07 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146931064):
you know, I'm not sure how to take the lines reduction when you are reformatting at the same time :P

#### [Mario Carneiro (Nov 07 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146931112):
https://github.com/leanprover/mathlib/pull/463/files#diff-d821da3f10c3bc4b40e7718069576210R81

#### [Mario Carneiro (Nov 07 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146931252):
there are also almost no actual proofs involved. Is it all just definitions?

#### [Kevin Buzzard (Nov 07 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146931583):
This night be a silly question because I don't know the previous setup -- could you just have the coercion on objects and only explicitly have to write F.app for the morphisms?

#### [Kevin Buzzard (Nov 07 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146931654):
Oh I see, this is exactly what was causing problems

#### [Kevin Buzzard (Nov 07 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146931665):
I now realise t is not a functor but probably a natural transformation

#### [Scott Morrison (Nov 07 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146932793):
> there are also almost no actual proofs involved. Is it all just definitions?

Yeah, nothing in `category_theory/` so far counts as a "theorem" except perhaps yoneda.

#### [Kevin Buzzard (Nov 07 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146933605):
I am reminded of https://mathoverflow.net/a/10899/1384

#### [Scott Morrison (Nov 07 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/146933680):
Hmm... Does sounds like Lang. :-)

#### [Scott Morrison (Nov 08 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147273670):
Hi @Mario, I'd be interested to hear your thoughts on this. I'm hesitant to continue working on later parts of the category theory development, because in several spots my current issues are connected to coercions. If I know whether or not it's likely this will be merged, I can decide whether or not to continue fighting those issues. :-)

#### [Mario Carneiro (Nov 08 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147273876):
I want to hear what @**Johannes Hölzl** has to say. You've been fighting these demons more than me, so I'll go with it if you think it helps, but I think it is a stylistic loss

#### [Johan Commelin (Nov 08 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147276465):
I would be happy with merging this. I think @**Reid Barton** expressed a similar opinion.

#### [Johannes Hölzl (Nov 08 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147285804):
I agree that it is a stylisitic loss, but its not too bad. Also we get rid of a lot of boilerplate code.
So I'm okay with removing the coercions

#### [Scott Morrison (Nov 08 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147285900):
Whee... :-) After :four_leaf_clover:, I will see if we can do better.

#### [Scott Morrison (Nov 08 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147285913):
Would it be better with a symbol in between, instead of just field notation?

#### [Johan Commelin (Nov 08 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147285958):
Naahh, I would find it less readable with a symbol

#### [Mario Carneiro (Nov 08 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147285959):
I'm a bit worried that you can't do the same thing with notations

#### [Mario Carneiro (Nov 08 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147285967):
in particular that example with monoidal functor application

#### [Scott Morrison (Nov 08 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147285994):
@**Mario Carneiro**, could you clarify that? I'm not sure what you mean yet.

#### [Mario Carneiro (Nov 08 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147286041):
if `F` is a monoidal functor, then `F.app X` is magically parsed to `F.to_functor.app X`

#### [Mario Carneiro (Nov 08 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147286048):
You don't get the same magic if you write `F +> X` or whatever

#### [Johannes Hölzl (Nov 08 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147286639):
is it ready to be merged?

#### [Mario Carneiro (Nov 08 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147286899):
go for launch

#### [Johannes Hölzl (Nov 08 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23463%20removing%20coercions%20from%20category_theory//near/147287069):
merged

