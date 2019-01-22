---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/78247categories.html
---

## [new members](index.html)
### [categories](78247categories.html)

#### [Edward Ayers (Aug 08 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131073671):
I made a silly .lean file for mathematical category theory.
https://gist.github.com/EdAyers/87fa2de6ddfc13ab273af52c21d48681
Two questions; 
- what is the best way to solve the lemmas with `sorry` in them?
- doesn't the definition of `Cat` break the type universe hierarchy? And if so why doesn't lean care?

#### [Edward Ayers (Aug 08 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131074009):
Also any comments on style / readability would be appreciated

#### [Kevin Buzzard (Aug 08 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131074344):
Just to comment that fresh this week we've had a huge category theory PR accepted into mathlib: https://github.com/leanprover/mathlib/commit/9b1be732e122d371100b0df479ca000c2a3f73b0

#### [Edward Ayers (Aug 08 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131074686):
ok thanks I can compare it to my code

#### [Scott Morrison (Aug 08 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131079511):
Hi @**Kevin Buzzard**, sorry to disappoint, but that PR that was merged was only the first epsilon of the actual category theory library (just 3 files!) It's still a long way to go anything useful to you is there. :-)

#### [Scott Morrison (Aug 08 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131079519):
There's a second PR waiting, if anyone feels like giving some comments.<https://github.com/leanprover/mathlib/pull/239>.

#### [Patrick Massot (Aug 09 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131165293):
```quote
I made a silly .lean file for mathematical category theory.
https://gist.github.com/EdAyers/87fa2de6ddfc13ab273af52c21d48681
```
Who keeps the record of all beginners who had category theory as their first idea of something to formalize?

#### [Kevin Buzzard (Aug 09 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131165597):
If you want to add to the list of "stuff which it looks like a good idea to be the first thing to formalise" then you seem to be able to add basic number theory to that list. My students ended up in coercion hell going from nat to int to zmod n

#### [Reid Barton (Aug 09 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131169156):
Heh, the first two things I tried to formalize were fibrations of categories (that went poorly) and FLT for n=4

#### [Kevin Buzzard (Aug 09 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131169279):
At least FLT for n=4 is a statement about nat.

#### [Kevin Buzzard (Aug 09 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131169292):
The proof might not stray too far from nat either

#### [Kevin Buzzard (Aug 09 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131169296):
oh actually maybe it strays into int a fair bit...

#### [Reid Barton (Aug 09 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131169410):
I managed to nearly avoid using int, I think, but it might have been better to use it more. Lots of annoying inequality side conditions to check when doing algebraic manipulations over nat

#### [Edward Ayers (Aug 09 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131170956):
I chose cats because that's the area of maths I'm strongest at and because it forces me to use lots of dependent-type features

#### [Mario Carneiro (Aug 09 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131171043):
I don't disagree that it's a logical choice when starting to play with a DTT prover, but it really is so common it's almost a joke

#### [Mario Carneiro (Aug 09 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131171049):
I'm sure I've seen this happen at least 8 times

#### [Edward Ayers (Aug 09 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131171320):
Another fun one is making `vec n` and matrices and so on.

#### [Mario Carneiro (Aug 09 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/131171614):
Those might be in TPIL though

#### [David Michael Roberts (Oct 10 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/135524085):
So I would like to say that I have some category, and say that it has some object. It's not obvious how to even declare a variable of type `category`. What I would like to do is to define the type of terminal objects of a given category. In type theory I guess I would do something like the dependent type

C:category |- terminalObj(C): C.obj

where C.obj is the type of objects of C.

#### [David Michael Roberts (Oct 10 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/135524246):
(I should say I'm using `category_theory` in mathlib)

Then terminalObj(C) := Σ t: C.Obj Π_{x:C.Obj} Π_{f,g:Hom(x,t)} f = g

#### [Mario Carneiro (Oct 10 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/135524331):
In lean, we have `category A` as the type of categories where `A` is the type of objects. (That is, they are "partially unbundled" with the type of objects exposed.) Then you can define a structure `is_terminal (X : A) : Type` with fields for the unique map in, and the statement of uniqueness

#### [David Michael Roberts (Oct 10 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/135527489):
Ah, that makes sense. Particularly as Cat is fibred over Class by sending a category to its class of objects, so that it makes sense to talk of the dependent type A:Type |- category(A): Type.

#### [Mario Carneiro (Oct 10 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/135527835):
Yes, what you call fibration is what we call unbundling

#### [Scott Morrison (Oct 10 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/135528430):
Terminal objects (along with every other shape of (co)limit) are on the horizon. If you want to peek, and don't mind peeking at often-broken code, see the `working` branch of https://github.com/semorrison/lean-category-theory/tree/working/src/category_theory/limits.

#### [Scott Morrison (Oct 10 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/135528440):
("working" here is as-in "I'm working on it", not "it is working"...)

#### [Mario Carneiro (Oct 10 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/135528454):
I think `wip` is less susceptible to misinterpretation

#### [Scott Morrison (Oct 10 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/135528498):
ok, I'll use that in future! thanks.

#### [David Michael Roberts (Oct 10 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/categories/near/135529320):
@**Scott Morrison|110087** thanks, I'll check it out

