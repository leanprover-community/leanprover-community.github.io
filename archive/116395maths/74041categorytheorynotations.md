---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/74041categorytheorynotations.html
---

## Stream: [maths](index.html)
### Topic: [category theory notations](74041categorytheorynotations.html)

---

#### [Scott Morrison (Apr 28 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125808846):
I am very-nearly-just-about ready with my category theory PR. I would like some help with notations, however.

#### [Scott Morrison (Apr 28 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125808889):
Perhaps I will write up a short document explaining my current choices, and hopefully some of the mathematicians (/computer scientists who like category theory) here can complain about them. :-)

#### [Kenny Lau (Apr 28 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125808941):
@**Scott Morrison** fancy incorporating my examples?

#### [Scott Morrison (Apr 28 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809059):
@**Kenny Lau** which examples?

#### [Scott Morrison (Apr 28 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809060):
I'll look, but it may just be best to do a later PR.

#### [Scott Morrison (Apr 28 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809097):
My first category theory PR is going to be a tiny subset of the whole existing library.

#### [Kenny Lau (Apr 28 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809100):
```quote
@**Kenny Lau** which examples?
```
I have many examples in my repo :P

#### [Kenny Lau (Apr 28 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809101):
https://github.com/kckennylau/category-theory

#### [Scott Morrison (Apr 28 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809359):
okay --- let's wait until we have the basics in mathlib, and then we can start importing!

#### [Reid Barton (Apr 28 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809663):
@**Scott Morrison**, I should have mentioned this earlier, but I noticed that your `Complete C` class doesn't quite correspond to the usual notion of completeness, since one ordinarily only requires the indexing category `J` for a limit to be small (w.r.t. the same universe in which the hom sets of `C` are small), but your definition further requires the hom sets of `J` to belong to an even smaller universe.

#### [Reid Barton (Apr 28 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809669):
More concretely, in a complete category one may always form the equalizer of all the morphisms between a given pair of objects, but that's not possible with the `Complete` class.

#### [Reid Barton (Apr 28 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125809788):
And generally speaking it is useful to have a notion of "small category" where the objects and morphisms are sets that live in the same universe. I mention this because one possible way to address this (though maybe not the best way) would be to add a second universe parameter to the `category` class, which would probably involve many other changes.

#### [Reid Barton (Apr 28 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125810026):
Another option might be to define a small category as a category with object type of the form `ulift.{i (i+1)} a`

#### [Scott Morrison (Apr 28 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125810972):
(deleted)

#### [Scott Morrison (Apr 28 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125810978):
(deleted)

#### [Kevin Buzzard (Apr 28 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817480):
It seems to me that doing category theory in Lean brings up some extremely delicate issues.

#### [Kevin Buzzard (Apr 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817520):
I am an end user and I do not care about universes or these subtleties, at least when I have my algebraic geometry hat on

#### [Kevin Buzzard (Apr 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817523):
I just want to write down a functor from "the" category of open sets on a topological space to "the" category of groups, without caring at all about which universe all these things live in.

#### [Kevin Buzzard (Apr 28 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817572):
On the other hand, I have seen intelligent people occasionally pausing to say "by the way, when I say category of _all_ schemes, it might be best if you interpret this as the category of all schemes which show up at some level in a set-theoretical hierarchy, and here is a calculation indicating that certain basic operations will never take us out of that category"

#### [Kevin Buzzard (Apr 28 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817619):
Here, for example, is Johan de Jong being very careful about what he means by the category of schemes, as formalised within ZFC.

#### [Kevin Buzzard (Apr 28 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817620):
https://stacks.math.columbia.edu/tag/000H

#### [Kevin Buzzard (Apr 28 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817627):
It seems to me that when you are doing calculations such as these, you are making a *promise* to your reader.

#### [Kevin Buzzard (Apr 28 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817674):
You are saying "isn't maths great, look at all the things we can do. Here is one thing we can do which is quite sensible -- we can sometimes take certain limits of schemes. And look, if my schemes are all "small" and the diagram is "small" then the limit of the diagram is "small" too."

#### [Kevin Buzzard (Apr 28 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817677):
And now you make the promise that throughout the 6000 pages which are about to follow

#### [Kevin Buzzard (Apr 28 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817680):
you promise you don't do anything pathological

#### [Kevin Buzzard (Apr 28 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817681):
which forces a universe change

#### [Kevin Buzzard (Apr 28 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817682):
Now that is a really big promise.

#### [Kevin Buzzard (Apr 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817714):
But some mathematicians are absolutely alive to that promise.

#### [Kevin Buzzard (Apr 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817728):
and it's those kinds of mathematicians, like Brian Conrad, who, when you mention the fpqc topology on a scheme, points out that in that situation you have not kept your promise.

#### [Kevin Buzzard (Apr 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817730):
because an arbitrary map between fields is quasi-compact

#### [Kevin Buzzard (Apr 28 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817736):
and there are a lot of fields

#### [Kevin Buzzard (Apr 28 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817743):
What I am pretty convinced about is that one day in the future when we have formalised schemes, and their etale cohomology, their fppf cohomology and their fpqc cohomology

#### [Kevin Buzzard (Apr 28 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817792):
then at some point there will be an issue with fpqc

#### [Kevin Buzzard (Apr 28 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817797):
which will manifest itself in some constructions having to be worked out slightly differently

#### [Kevin Buzzard (Apr 28 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817798):
because of universe issues

#### [Kevin Buzzard (Apr 28 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817799):
I believe that mathematicians hide that thought away

#### [Kevin Buzzard (Apr 28 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817805):
because it hopefully doesn't affect anything they do

#### [Kevin Buzzard (Apr 28 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817843):
Scott -- if you could just give me some working definition of a category and a site and a topos

#### [Kevin Buzzard (Apr 28 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817846):
then there is nothing stopping people from formalising definitions of these fancy cohomology theories in Lean

#### [Kevin Buzzard (Apr 28 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817847):
Proving anything non-trivial about these fancy cohomology theories would almost certainly be extemely difficult

#### [Kevin Buzzard (Apr 28 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817848):
however _defining_ them is another kettle of fish

#### [Kevin Buzzard (Apr 28 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817855):
I defined schemes over a month ago and am still yet to produce a single example because I have been caught up in notions of canonical isomorphism

#### [Kevin Buzzard (Apr 28 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817856):
but the definition is there

#### [Kevin Buzzard (Apr 28 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817861):
So let me know when you want to define some fancy cohomology theories on the category of schemes

#### [Kevin Buzzard (Apr 28 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817863):
and not prove anything about them

#### [Kevin Buzzard (Apr 28 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817903):
because this would be an extremely good stress test for your category theory library

#### [Kevin Buzzard (Apr 28 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20notations/near/125817905):
and I believe it is within reach

