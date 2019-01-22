---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/21890Therealnumbers.html
---

## [maths](index.html)
### [The real numbers](21890Therealnumbers.html)

#### [Kevin Buzzard (May 31 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127331937):
How are our real numbers getting along? Do we have the definition of a differentiable function yet, and of its derivative?

#### [Kenny Lau (May 31 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127331992):
one thing about analysis is that there are a lot of promises made

#### [Kenny Lau (May 31 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127331996):
when we say the derivative of a function, we don't just mean the derivative of a function

#### [Kenny Lau (May 31 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127331999):
we mean that it exists

#### [Kevin Buzzard (May 31 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332157):
Do we have that the reals are the unique Dedekind-complete ordered field up to unique isomorphism?

#### [Kenny Lau (May 31 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332202):
is R[ε] Dedekind-complete?

#### [Kevin Buzzard (May 31 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332210):
I was writing a chapter in my book on reals and I was trying to figure out the interface that a mathematician needed.

#### [Kevin Buzzard (May 31 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332219):
I figure we need the uniqueness statement above, and the intermediate value theorem and the mean value theorem

#### [Kevin Buzzard (May 31 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332221):
and I reckon we have then got a huge chunk of 1st year Imperial analysis

#### [Andrew Ashworth (May 31 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332225):
analysis is tricky, I took a long look at awhile back since I was interested in probability

#### [Kevin Buzzard (May 31 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332231):
I could get students working on this over the summer but I don't have a clue about the current state of things and just thought it was easiest to ask

#### [Kenny Lau (May 31 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332232):
I already proved the IVT ^^

#### [Kevin Buzzard (May 31 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332274):
Where Kenny?

#### [Kenny Lau (May 31 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332279):
in my own construction of the real numbers

#### [Kenny Lau (May 31 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332294):
https://github.com/kckennylau/Lean/blob/master/cauchy_real.lean#L1508

#### [Andrew Ashworth (May 31 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332316):
my plan for attacking it (which I eventually gave up on when I realized is was quite some work) was to follow the isabelle analysis theorems (many of them were written by johannes and jeremy avigad!)

#### [Andrew Ashworth (May 31 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332393):
well, you could just ask @**Johannes Hölzl**  for his advice on what analysis developments to work on :)

#### [Kevin Buzzard (May 31 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332436):
Kenny did you prove that your real numbers were the unique complete ordered field up to unique isomorphism?

#### [Kenny Lau (May 31 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332438):
no

#### [Kevin Buzzard (May 31 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332442):
Is it in mathlib?

#### [Kenny Lau (May 31 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332444):
no idea

#### [Andrew Ashworth (May 31 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332530):
out of curiosity is there a good reference on filters around? I only know about the Cauchy sequence construction, but it seems I must know more to use the reals in mathlib...

#### [Johannes Hölzl (May 31 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332539):
@**Andrew Ashworth**  most of Isabelle's analysis developed over some time. Starting from Fleuriot, over porting stuff from HOL Light by Amine Chaieb, and then generalizing it to type classes by Brian Huffman, Fabian Immler and me.

#### [Johannes Hölzl (May 31 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332541):
and a lot of other people

#### [Johannes Hölzl (May 31 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332591):
@**Kevin Buzzard** I don't think there is a uniqueness proof in mathlib

#### [Kevin Buzzard (May 31 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332645):
@**Andrew Ashworth** Given a point in a space, you get a "filter" of sets on the space, namely the sets containing the point.

#### [Kevin Buzzard (May 31 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332652):
So a filter is kind-of a generalization of a point

#### [Kevin Buzzard (May 31 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332655):
it's a really cool way of saying "tends to +infinity" for example

#### [Kevin Buzzard (May 31 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332658):
because even though infinity isn't a real number

#### [Johannes Hölzl (May 31 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332659):
@**Andrew Ashworth** do you know our filter paper http://home.in.tum.de/~hoelzl/documents/hoelzl2013typeclasses.pdf ? at least it explains how filters are used in Isabelle.

#### [Kevin Buzzard (May 31 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332663):
the sets of reals that contain an open interval (r,infinity) is a filter

#### [Johannes Hölzl (May 31 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332686):
* the sets of sets (r, infinite) over all r

#### [Johannes Hölzl (May 31 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332740):
the sets of all neighbourhoods around x forms a filter, all left neighbourhoods (and right neibourhoods) etc

#### [Johannes Hölzl (May 31 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332826):
but currently you need to do a lot of operations directly with filters, there is a lot of *porcelian* missing. Porcelain the sense that a lot the nice lemmas to show continuity of a function and using it are just not there yet. Many should be proved in a couple of lines but need to be written down.

#### [Kevin Buzzard (May 31 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332892):
Am I right in thinking that @**Mario Carneiro** @**Johannes Hölzl** and @**Kenny Lau** -- that all of you wrote distinct definitions of real numbers recently?

#### [Kevin Buzzard (May 31 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332893):
Each one of you should prove the fundamental theorem of real numbers

#### [Kevin Buzzard (May 31 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332904):
that you are a Dedekind complete ordered field

#### [Kevin Buzzard (May 31 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332913):
and the moment you do that you can access all the theorems proved about the other real numbers

#### [Kevin Buzzard (May 31 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332921):
Did you all do that?

#### [Mario Carneiro (May 31 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332965):
Uniqueness is overrated

#### [Kevin Buzzard (May 31 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332967):
rofl

#### [Kevin Buzzard (May 31 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332969):
you people

#### [Kevin Buzzard (May 31 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332971):
you don't understand equality

#### [Mario Carneiro (May 31 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332974):
It's really not needed for anything practical though

#### [Mario Carneiro (May 31 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332978):
in a sense it tells you you "got it right" but that's it

#### [Kevin Buzzard (May 31 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332979):
it's needed for clear thinking

#### [Kevin Buzzard (May 31 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332984):
and so we have to teach it to computers

#### [Kevin Buzzard (May 31 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332990):
it makes the world a simpler place

#### [Mario Carneiro (May 31 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332993):
when you want to apply theorems about reals, you need to have theorems on (your) reals

#### [Mario Carneiro (May 31 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127332995):
a uniqueness statement doesn't help here

#### [Kevin Buzzard (May 31 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333062):
I just mean you can port theorems with the uniqueness statement

#### [Mario Carneiro (May 31 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333067):
yeah, that's a bad idea, avoid if you can help it

#### [Kevin Buzzard (May 31 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333079):
I want to do more than port theorems

#### [Kevin Buzzard (May 31 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333083):
I want to identify them as one

#### [Mario Carneiro (May 31 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333125):
Better to have a single definition and prove equivalent "views" of it

#### [Kenny Lau (May 31 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333128):
uniqueness theorem is a part of interface, because sometimes you would have more than one instance, because it's describing a class of objects (e.g. algebra homomorphism)

#### [Kenny Lau (May 31 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333130):
but in this case there is only one object that we call the real numbers

#### [Kevin Buzzard (May 31 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333131):
I have so much to learn about the way you guys think about things.

#### [Kenny Lau (May 31 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333133):
we won't be constructing other real numbers

#### [Kenny Lau (May 31 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333135):
so I don't see why uniqueness is important

#### [Kevin Buzzard (May 31 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333149):
What is the point of having three copies of the real numbers?

#### [Kevin Buzzard (May 31 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333154):
Is one of them "the best one" or do they all have their merits or what?

#### [Kenny Lau (May 31 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333158):
i just did it for myself

#### [Mario Carneiro (May 31 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333161):
There's only one I'm aware of, unless Kenny did something

#### [Kenny Lau (May 31 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333164):
i did it privately

#### [Mario Carneiro (May 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333204):
There was an old construction by Johannes and I replaced it with my own

#### [Kevin Buzzard (May 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333207):
I thought we had a filter one and a cauchy sequence one in mathlib at different times

#### [Kevin Buzzard (May 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333208):
right

#### [Kevin Buzzard (May 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333210):
and then Kenny's

#### [Mario Carneiro (May 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333213):
The filter construction is gone, although the theorems aren't

#### [Kenny Lau (May 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333219):
rip filter construction 2017-2018

#### [Kevin Buzzard (May 31 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333229):
OK so Mario, let's say that in Johannes' construction of real numbers with filters, he proved that the real numbers were a Dedekind complete totally ordered field (he almost certainly did prove this, I believe I remember checking once).

#### [Kevin Buzzard (May 31 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333231):
Then isn't that all you will ever need from the real numbers?

#### [Mario Carneiro (May 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333284):
Yes, and that theorem is still there

#### [Kenny Lau (May 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333287):
no, you need a way to construct real numbers

#### [Kenny Lau (May 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333288):
like sqrt(2)

#### [Kenny Lau (May 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333291):
and filters are hard to work with

#### [Kevin Buzzard (May 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333292):
but if Johannes had made it to that pinnacle

#### [Kevin Buzzard (May 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333294):
you would never need to think about filters any more

#### [Kenny Lau (May 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333299):
how would you make sqrt(2)?

#### [Kevin Buzzard (May 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333310):
take the sup of the set of real whose square was less than 2

#### [Mario Carneiro (May 31 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333329):
My construction just slots in where the old one was, all the theorems still work after porting (with filters and everything)

#### [Kevin Buzzard (May 31 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333333):
and then say that you're a complete field

#### [Mario Carneiro (May 31 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333347):
The abstract theorems like that exist, but that's still a far cry from the "algebraic" theory with say transcendental functions

#### [Kevin Buzzard (May 31 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333392):
Chris did exp and sin and cos

#### [Kevin Buzzard (May 31 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333395):
did that ever make it into mathlib?

#### [Kevin Buzzard (May 31 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333398):
I need that for October!

#### [Kenny Lau (May 31 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333399):
it's still in PR i think

#### [Kevin Buzzard (May 31 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333406):
If it needs work, let me know, that would be a great thing for students to work on

#### [Kevin Buzzard (May 31 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333414):
I need e^(i theta) = cos(theta) + i sin(theta)

#### [Kenny Lau (May 31 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333422):
you're on the wrong thread then

#### [Kevin Buzzard (May 31 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333432):
you mentioned R[e] earlier, this is R[i]

#### [Kevin Buzzard (May 31 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333708):
https://math.stackexchange.com/questions/269353/isomorphism-of-dedekind-complete-ordered-fields

#### [Kevin Buzzard (May 31 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333715):
The quote from Spivak

#### [Kevin Buzzard (May 31 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333718):
[not the question itself]

#### [Kevin Buzzard (May 31 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333726):
Is that proof, that any two complete ordered fields are isomorphic, in mathlib?

#### [Kenny Lau (May 31 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333767):
(removed)

#### [Kevin Buzzard (May 31 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333774):
up to unique isomorphism

#### [Kevin Buzzard (May 31 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333780):
they are _the same_

#### [Kevin Buzzard (May 31 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333784):
they are equal

#### [Kevin Buzzard (May 31 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333813):
they are `maths-equivalent`

#### [Mario Carneiro (May 31 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127333950):
Having that theorem will just make you more frustrated when it isn't as powerful as you want

#### [Reid Barton (May 31 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334011):
Incidentally, in my limited experience, it's better not to work with any particular model of the reals directly, but just axiomatize the features that you need using type classes

#### [Kevin Buzzard (May 31 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334024):
Don't prove a single theorem about the reals

#### [Kevin Buzzard (May 31 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334027):
just prove a theorem about complete totally ordered fields?

#### [Reid Barton (May 31 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334032):
I got frustrated when Lean would keep running out of memory when trying to check stuff like `rfl : 2 * 1 = 1 + 1`

#### [Reid Barton (May 31 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334077):
but then when I switched to working over a general totally ordered discrete topological whatever field, my compile times went way down

#### [Kenny Lau (May 31 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334078):
that one is mul_one :P

#### [Kevin Buzzard (May 31 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334081):
norm_num ftw

#### [Reid Barton (May 31 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334089):
I know, but it's hard to stop Lean from trying to reduce

#### [Kenny Lau (May 31 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334090):
2 is defined to be bit0 1, which is defined to be 1+1

#### [Reid Barton (May 31 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334100):
It means every time you use `simp` or something, you might fall into a memory leak

#### [Mario Carneiro (May 31 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334102):
but you still have to reduce (1+1)*1 = 1+1 there

#### [Reid Barton (May 31 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334103):
and then you have to back up and carefully walk around it

#### [Reid Barton (May 31 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334115):
Sure, and then `norm_num` can do that for you

#### [Kenny Lau (May 31 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334117):
so I said it's `mul_one`

#### [Andrew Ashworth (May 31 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334125):
I have wondered whether the reals should be a typeclass too, in case somebody wants to have a really efficient computable version at some point in the future

#### [Kevin Buzzard (May 31 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334135):
but Kenny what about `2/3*4/5=8/30*2`

#### [Kenny Lau (May 31 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334137):
but there is no computable version

#### [Mario Carneiro (May 31 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334179):
well, the current version is as computable as it gets

#### [Kevin Buzzard (May 31 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334186):
I see, so the issue is of course not about proving theorems, it is about doing calculations

#### [Kevin Buzzard (May 31 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334188):
computations

#### [Mario Carneiro (May 31 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334189):
i.e. stuff like `2 * 3 = 6` computes

#### [Kenny Lau (May 31 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334194):
everything is about computation

#### [Kevin Buzzard (May 31 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334196):
which are of course important when you want to prove theorems

#### [Kevin Buzzard (May 31 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334200):
you want your reals to be "as computable as possible"?

#### [Mario Carneiro (May 31 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334206):
well yes

#### [Kevin Buzzard (May 31 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334213):
Don't you take one look at a question involving rationals and instantly descend to the rationals?

#### [Kenny Lau (May 31 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334216):
then make `inv` into a function that takes a proof that it is not zero

#### [Mario Carneiro (May 31 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334217):
I did

#### [Andrew Ashworth (May 31 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334218):
Kenny, there is such a thing as constructive, computable reals. You can treat it as arbitrary-precision floating point

#### [Mario Carneiro (May 31 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334256):
It's called `divp`

#### [Kevin Buzzard (May 31 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334263):
and does it work on an arbitrary complete totally ordered field?

#### [Mario Carneiro (May 31 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334265):
It works on any *ring*

#### [Kenny Lau (May 31 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334268):
you won't want to formalize computable reals

#### [Andrew Ashworth (May 31 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334284):
you won't want to, but yet it'll be super useful

#### [Kenny Lau (May 31 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334345):
are you going to set up turing machines now

#### [Mario Carneiro (May 31 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334354):
lol I'm actually typing out turing machines right now

#### [Mario Carneiro (May 31 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127334361):
Actually I'm going via Wang B-machines

#### [Kevin Buzzard (May 31 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127336402):
Lean challenge : $$(\surd2+\surd3)^2=5+2\surd6$$

#### [Kenny Lau (May 31 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127336620):
```lean
import data.real.basic tactic.norm_num

prefix `√`:90 := real.sqrt

example : (√2 + √3)^2 = 5 + 2*√6 :=
by rw [pow_two, add_mul_self_eq, mul_assoc,
  ← real.sqrt_mul, ← real.sqrt_mul, ← real.sqrt_mul,
  real.sqrt_mul_self, real.sqrt_mul_self]; norm_num;
  rw [← add_assoc]; refl
```

#### [Kenny Lau (May 31 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127336744):
```lean
import data.real.basic tactic.norm_num

prefix `√`:90 := real.sqrt

example : (√2 + √3)^2 = 5 + 2*√6 :=
by rw [pow_two, add_mul_self_eq, mul_assoc,
  ← real.sqrt_mul, ← real.sqrt_mul, ← real.sqrt_mul,
  real.sqrt_mul_self, real.sqrt_mul_self, add_right_comm];
  norm_num
```

#### [Kevin Buzzard (May 31 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127341099):
Thanks Kenny.

#### [Kevin Buzzard (May 31 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127341111):
In `data/real/basic.lean` there is an import of `algebra.big_operators ` which doesn't seem to me to be used. Is this sort of PR welcome?

#### [Kevin Buzzard (May 31 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342055):
https://github.com/leanprover/mathlib/blob/bdd54acda358f535b42951b784757135213dcf52/data/real/basic.lean#L16

#### [Kevin Buzzard (May 31 2018 at 05:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342065):
At that line, `#check mk` gives that `mk` is `rat.mk`. And then on the next line it feels like it was redefined. Why is mk not overloaded now?

#### [Kevin Buzzard (May 31 2018 at 05:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342067):
Is there some priority trick?

#### [Mario Carneiro (May 31 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342234):
`mk` is overloaded at that point. But when one of the theorems with that name is in the current namespace (i.e. inside a `namespace` block), it takes precedence over other `open` namespaces.

#### [Kevin Buzzard (May 31 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342250):
I see. Thanks.

#### [Kevin Buzzard (May 31 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342253):
```lean
instance : has_add ℝ :=
⟨λ x y, quotient.lift_on₂ x y (λ f g, mk (f + g)) $
  λ f₁ g₁ f₂ g₂ hf hg, quotient.sound $
  by simpa [(≈), setoid.r] using add_lim_zero hf hg⟩
```

#### [Kevin Buzzard (May 31 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342254):
and then

#### [Kevin Buzzard (May 31 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342255):
```lean
instance : has_neg ℝ :=
⟨λ x, quotient.lift_on x (λ f, mk (-f)) $
  λ f₁ f₂ hf, quotient.sound $
  by simpa [(≈), setoid.r] using neg_lim_zero hf⟩

```

#### [Kevin Buzzard (May 31 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342257):
That's the same code again!

#### [Mario Carneiro (May 31 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342305):
sure is, less than 30 seconds copy paste work

#### [Kevin Buzzard (May 31 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342307):
That should be `by math_trivial [add_lim_zero]`

#### [Kevin Buzzard (May 31 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342311):
and then `by math_trivial [neg_lim_zero]`

#### [Mario Carneiro (May 31 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342315):
like I said, ~20 times repetition before I even consider making a tactic

#### [Mario Carneiro (May 31 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342321):
6 or 7 times is not enough

#### [Kevin Buzzard (May 31 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342329):
but if someone just came along and made that tactic and offered it to mathlib, do you think it would be useful?

#### [Kevin Buzzard (May 31 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342330):
I am seeing this ... idiom or whatever you call it over and over again

#### [Kevin Buzzard (May 31 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342332):
"we laboriously transport structure"

#### [Mario Carneiro (May 31 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342334):
in particular, it is often the case that all the axioms of concrete structure X are similar to each other, but not similar to structure Y

#### [Mario Carneiro (May 31 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342382):
having a tactic that proves axioms of X is not that helpful since there are only O(1) of them, and the tactic won't help with Y

#### [Kevin Buzzard (May 31 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342387):
Transport of structure is a central idea of mathematics as we see in the work of Grothendieck and Deligne

#### [Mario Carneiro (May 31 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342390):
Would this `math_trivial` tactic apply equally to `real` and `pnat`?

#### [Kevin Buzzard (May 31 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342392):
This is just the sort of thing I want to find out

#### [Kevin Buzzard (May 31 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342395):
I found myself when doing schemes

#### [Kevin Buzzard (May 31 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342397):
wanting a tactic like this

#### [Kevin Buzzard (May 31 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342398):
and I know that when I start perfectoids

#### [Kevin Buzzard (May 31 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342401):
I'll find it again

#### [Mario Carneiro (May 31 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342444):
My point is that there are not that many similarities between the proof that `pnat` has an add and `real` does

#### [Kevin Buzzard (May 31 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342447):
yeah isn't that interesting

#### [Kenny Lau (May 31 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342450):
lol

#### [Kenny Lau (May 31 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342451):
Kevin

#### [Kenny Lau (May 31 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342452):
the sky is blue

#### [Kevin Buzzard (May 31 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342462):
These guys need to make a proper mathematician

#### [Kevin Buzzard (May 31 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342464):
with the right kind of equals

#### [Kenny Lau (May 31 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342506):
it's foggy

#### [Kenny Lau (May 31 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342511):
relative humidity 98%

#### [Kevin Buzzard (May 31 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342570):
```lean

/- Extra instances to short-circuit type class resolution -/
instance : semigroup ℝ      := by apply_instance
instance : monoid ℝ         := by apply_instance
instance : comm_semigroup ℝ := by apply_instance
instance : comm_monoid ℝ    := by apply_instance
instance : add_monoid ℝ     := by apply_instance
instance : add_group ℝ      := by apply_instance
instance : add_comm_group ℝ := by apply_instance
instance : ring ℝ           := by apply_instance
```

#### [Kevin Buzzard (May 31 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342571):
Why do they make life better?

#### [Kevin Buzzard (May 31 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342572):
This is all in data/real/basic.lean

#### [Kenny Lau (May 31 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342573):
because beneath you is an uncomputable instance

#### [Kevin Buzzard (May 31 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342575):
those are the best kind IMO

#### [Kenny Lau (May 31 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342576):
if you don't do this, the uncomputable instance will be used

#### [Kenny Lau (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342614):
so your definitions would have to be noncomputable

#### [Kenny Lau (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342619):
and it is used because it is declared the latest

#### [Kevin Buzzard (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342620):
none of this makes any sense to me

#### [Mario Carneiro (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342621):
no, that's not related

#### [Mario Carneiro (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342623):
those instances
> short-circuit type class resolution

#### [Kevin Buzzard (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342626):
so they are creating new paths in the system

#### [Kenny Lau (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342627):
well in my construction, if I don't do that, my things become uncomputable

#### [Kevin Buzzard (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342629):
which are defeq to longer paths

#### [Mario Carneiro (May 31 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342630):
yes

#### [Kevin Buzzard (May 31 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342635):
and this is perhaps making the system better for some reason

#### [Kevin Buzzard (May 31 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342640):
why doesn't the system run all those commands every time anyone makes anything a comm_ring?

#### [Mario Carneiro (May 31 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342641):
it means less time traversing the instance graph

#### [Kevin Buzzard (May 31 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342642):
then it would be much less time

#### [Mario Carneiro (May 31 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342645):
because that wouldn't save any time, it would just create lots of space

#### [Kevin Buzzard (May 31 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342685):
```lean
instance : has_lt ℝ :=
⟨λ x y, quotient.lift_on₂ x y (<) $
  λ f₁ g₁ f₂ g₂ hf hg, propext $
  ⟨λ h, lt_of_eq_of_lt (setoid.symm hf) (lt_of_lt_of_eq h hg),
   λ h, lt_of_eq_of_lt hf (lt_of_lt_of_eq h (setoid.symm hg))⟩⟩
```

#### [Kevin Buzzard (May 31 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342687):
They're getting quite tricky for my tactic now

#### [Mario Carneiro (May 31 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342689):
If you do it in *every* case, there is no advantage over just searching the graph, since you have just precalculated all paths

#### [Kevin Buzzard (May 31 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342692):
ha ha

#### [Mario Carneiro (May 31 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342699):
the point is that I know that `real` is important and people want to use it lots

#### [Mario Carneiro (May 31 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342702):
so I set up the system to make that easier

#### [Kevin Buzzard (May 31 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342742):
What else can you control within the type class inference system?

#### [Mario Carneiro (May 31 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342743):
so that when weirdos state `ring` theorems over the reals for some reason, it's not horribly slow

#### [Kevin Buzzard (May 31 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342748):
I liked @**Reid Barton** 's comment about typeclasses.

#### [Kevin Buzzard (May 31 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342763):
```lean
--def real := quotient (@cau_seq.equiv ℚ _ _ _ abs _) -- orig
def real := quotient (cau_seq.equiv : setoid (cau_seq ℚ abs)) -- clearer for me
```

#### [Kevin Buzzard (May 31 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342764):
You prefer yours?

#### [Kevin Buzzard (May 31 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342767):
`@` and `_` are a bit ugly maybe

#### [Kevin Buzzard (May 31 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342806):
but yours is shorter

#### [Mario Carneiro (May 31 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127342867):
```
def real := @quotient (cau_seq ℚ abs) cau_seq.equiv
```

#### [Kevin Buzzard (May 31 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343308):
What is your preference? The mathlib one?

#### [Mario Carneiro (May 31 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343310):
I don't have a strong preference

#### [Kevin Buzzard (May 31 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343312):
In terms of Lean they're all presumably defeq

#### [Kevin Buzzard (May 31 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343321):
but in terms of readability some have more worth than others

#### [Mario Carneiro (May 31 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343351):
they are all syntactically equal

#### [Kevin Buzzard (May 31 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343365):
My favourite is the last one `@quotient (cau_seq ℚ abs) cau_seq.equiv` because it's the most readable to mathematicians

#### [Kevin Buzzard (May 31 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343406):
`instance : has_le ℝ := ⟨λ x y, x < y ∨ x = y⟩`

#### [Kevin Buzzard (May 31 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343408):
You've gone the wrong way

#### [Kevin Buzzard (May 31 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343411):
you can do `has_le` first and get `has_lt` for free!

#### [Mario Carneiro (May 31 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343412):
I know

#### [Kevin Buzzard (May 31 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343413):
You did it this way for a reason, presumably?

#### [Mario Carneiro (May 31 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343418):
the constructively natural one is lt

#### [Kevin Buzzard (May 31 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343419):
I see

#### [Kevin Buzzard (May 31 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343420):
it's all about computing

#### [Mario Carneiro (May 31 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343421):
it states that there is some epsilon separating them

#### [Mario Carneiro (May 31 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127343422):
for le, it's either the negation of that or the disjunction with equals

#### [Patrick Massot (May 31 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127349002):
```quote
that you are a Dedekind complete ordered field
```
Note: as a mathematician, I use real numbers every day, and I have no idea what is a "Dedekind complete ordered field"

#### [Patrick Massot (May 31 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127349061):
```quote
How are our real numbers getting along? Do we have the definition of a differentiable function yet, and of its derivative?
```
I have a definition of a function from a real normed vector space to another one which is differentiable at a point. But I don't have a normed space structure on ℝ^n because I'm swamped in type class resolution issues (https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tc.20loop.20again). Life is really hard here.

#### [Kevin Buzzard (Jun 01 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388365):
*boggle* I am typing up my exam into Lean and I need the fact that the decimal expansion of the real number 0.71 contains no 8's :-)

#### [Kevin Buzzard (Jun 01 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388372):
does Lean have decimal expansions??

#### [Kevin Buzzard (Jun 01 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388432):
maybe a function from the non-negative reals to (functions from nat to nat)

#### [Kevin Buzzard (Jun 01 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388438):
with f(succ n)<=9

#### [Kenny Lau (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388441):
you can write that yourself

#### [Kenny Lau (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388444):
it's quite explicit using floor

#### [Kevin Buzzard (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388446):
you are right!

#### [Kenny Lau (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388450):
given a real number r

#### [Kevin Buzzard (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388452):
But I was just asking if someone had already written it

#### [Kevin Buzzard (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388454):
Kenny I can do it :-)

#### [Kevin Buzzard (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388456):
I even lecture it in M1F some years

#### [Kevin Buzzard (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388459):
Darn it

#### [Kevin Buzzard (Jun 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127388463):
if I'd lectured it this year then @**Chris Hughes**  would have done it :-)

#### [Kevin Buzzard (Jun 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389782):
```lean
import analysis.real -- should come with a warning

noncomputable definition real.floor (x : ℝ) : ℤ := 
  classical.some (real.exists_floor x)

noncomputable definition expansion (r : ℝ) (H : r ≥ 0) : ℕ → ℕ
| 0 := real.floor r
| (n + 1) := 7

```

#### [Kevin Buzzard (Jun 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389786):
I made a slip: real.floor r on the last but one line is an int not a nat

#### [Kenny Lau (Jun 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389791):
Kevin

#### [Kenny Lau (Jun 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389792):
the fllor is there already

#### [Kevin Buzzard (Jun 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389794):
but when using reals, sllips like this bring the system to its knees. 100% CPU usage, orange bars

#### [Kenny Lau (Jun 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389797):
it's in archimedean

#### [Kevin Buzzard (Jun 01 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389804):
Thanks

#### [Kevin Buzzard (Jun 01 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389809):
but why does my code make Lean have a deterministic timeout?

#### [Kevin Buzzard (Jun 01 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389811):
Mario has answered this before

#### [Kevin Buzzard (Jun 01 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389853):
but this behaviour ("use the imported definitions wisely or there will be timeouts") is not the norm

#### [Kenny Lau (Jun 01 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389864):
it's just a typeclass fallout

#### [Kevin Buzzard (Jun 01 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389866):
right

#### [Kevin Buzzard (Jun 01 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389870):
but is this a design problem with Lean or something which can be fixed in mathlib or what?

#### [Kenny Lau (Jun 01 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389877):
no idea

#### [Kevin Buzzard (Jun 01 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127389940):
hey that floor_ring stuff is a really cool way of doing it :-)

#### [Kevin Buzzard (Jun 01 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390072):
`⌊10 / 3⌋ : ℤ`

#### [Kevin Buzzard (Jun 01 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390088):
`#reduce ⌊(real.sqrt 2 : ℝ)⌋`

#### [Kevin Buzzard (Jun 01 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390092):
100% CPU usage!

#### [Mario Carneiro (Jun 01 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390094):
For some reason, coercing an int to a nat causes a typeclass overflow

#### [Kevin Buzzard (Jun 01 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390096):
segv :-)

#### [Mario Carneiro (Jun 01 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390133):
I've seen this many times before

#### [Kevin Buzzard (Jun 01 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390141):
but it's only with reals

#### [Kevin Buzzard (Jun 01 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390143):
Lean is really good with most structures

#### [Kevin Buzzard (Jun 01 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390151):
Oh indpt of reals?

#### [Mario Carneiro (Jun 01 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390169):
you defined an int function and applied it to get a  nat

#### [Kevin Buzzard (Jun 01 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390186):
I know

#### [Kevin Buzzard (Jun 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390193):
I assumed the problem was because reals always time out

#### [Kevin Buzzard (Jun 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390237):
but maybe you fixed that

#### [Kevin Buzzard (Jun 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390253):
and this is an independent timeout

#### [Mario Carneiro (Jun 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390254):
The major source of that was fixed a while ago

#### [Mario Carneiro (Jun 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390260):
this is just Z -> N timeout

#### [Kevin Buzzard (Jun 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390266):
What do you get with

#### [Kevin Buzzard (Jun 01 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390267):
`#reduce ⌊(real.sqrt 2 : ℝ)⌋` ?

#### [Mario Carneiro (Jun 01 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390276):
something horrible, don't do that

#### [Mario Carneiro (Jun 01 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390279):
What part of `noncomputable` don't you understand?

#### [Kevin Buzzard (Jun 01 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390283):
:-)

#### [Kevin Buzzard (Jun 01 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390286):
I thought there was no harm trying

#### [Mario Carneiro (Jun 01 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390288):
it will be some huge stuck term depending on `classical.choice`

#### [Kevin Buzzard (Jun 01 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390289):
after all, schoolkid can do it

#### [Kevin Buzzard (Jun 01 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390326):
it's 1 Mario

#### [Mario Carneiro (Jun 01 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390330):
You can do it, but not like this

#### [Mario Carneiro (Jun 01 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390334):
In order for `reduce` to work it has to be true generally

#### [Kevin Buzzard (Jun 01 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390335):
this is going to be tough to explain to the mathematicians

#### [Kevin Buzzard (Jun 01 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390340):
I'm just being daft, I know about eval

#### [Mario Carneiro (Jun 01 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390344):
and there are messy terms you can give where it's impossible to decide

#### [Mario Carneiro (Jun 01 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390347):
`#eval` won't do any better

#### [Kevin Buzzard (Jun 01 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390354):
no but it could

#### [Mario Carneiro (Jun 01 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390356):
actually it will just complain up front

#### [Mario Carneiro (Jun 01 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390362):
no it can't, `real.floor` is *necessarily* noncomputable

#### [Kevin Buzzard (Jun 01 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390371):
the reduce gives me a segv (twice now)

#### [Mario Carneiro (Jun 01 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390414):
What *can* do better is `norm_num` style tactics that prove specific instances of this in some subset of the full language of lean

#### [Kevin Buzzard (Jun 01 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390415):
but the floor of the square root of 2 isn't noncomputable

#### [Mario Carneiro (Jun 01 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390426):
That statement doesn't make sense

#### [Mario Carneiro (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390431):
noncomputability is a property of a term, not its denotation

#### [Kenny Lau (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390432):
@**Kevin Buzzard** local computability does not patch to give global computability

#### [Kenny Lau (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390442):
it ain't no sheaf

#### [Kevin Buzzard (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390443):
is the obstruction finite?

#### [Mario Carneiro (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390444):
?

#### [Kenny Lau (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390446):
floor is computable iff halting problem can be solved

#### [Kenny Lau (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390448):
you have an obstructio in each integer, so no it ain't finite

#### [Kevin Buzzard (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390449):
I know but you can do it on sqrt(2)

#### [Kevin Buzzard (Jun 01 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390450):
I can prove that 1 is floor of sqrt(2)

#### [Mario Carneiro (Jun 01 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390491):
So do that

#### [Kenny Lau (Jun 01 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390493):
that doesn't mean you can compute floor(sqrt(2))

#### [Kevin Buzzard (Jun 01 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390495):
so it can be computed in this case

#### [Kevin Buzzard (Jun 01 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390497):
Kenny -- doesn't it?

#### [Mario Carneiro (Jun 01 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390500):
`floor (sqrt 2)` is a computable number, yes

#### [Mario Carneiro (Jun 01 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390502):
but `floor` is not a computable function

#### [Mario Carneiro (Jun 01 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390509):
so you can't just plug `sqrt 2` into `floor` and expect an answer

#### [Kenny Lau (Jun 01 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390516):
you need uniform computability without creativeness

#### [Kenny Lau (Jun 01 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390519):
informally

#### [Kenny Lau (Jun 01 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390520):
you need a canonical function

#### [Kevin Buzzard (Jun 01 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390521):
We could get transcendental numbers into Lean if we could get Chris' sin and cos stuff

#### [Kenny Lau (Jun 01 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390523):
that works across everything

#### [Kevin Buzzard (Jun 01 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390566):
floor is daft. Give me exp any day

#### [Kevin Buzzard (Jun 01 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390572):
Is that computable?

#### [Mario Carneiro (Jun 01 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390574):
By the way, floor is computable on algebraic numbers

#### [Kevin Buzzard (Jun 01 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390575):
I reckon I can prove the sequence is Cauchy

#### [Kenny Lau (Jun 01 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390579):
everything is computable on algebraic numbers

#### [Mario Carneiro (Jun 01 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390581):
so you can write `floor (sqrt 2)` and compute to `1`

#### [Kenny Lau (Jun 01 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390584):
surprise

#### [Mario Carneiro (Jun 01 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390586):
`exp` is computable

#### [Kevin Buzzard (Jun 01 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390589):
Kenny I'm sure there are non-recursive or whatever subsets of the natural numbers

#### [Kenny Lau (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390640):
I was uttering hyperbole

#### [Kevin Buzzard (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390641):
and so of the algebraic numbers

#### [Mario Carneiro (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390643):
I think real numbers are overrated in math

#### [Kenny Lau (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390644):
agree

#### [Kevin Buzzard (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390645):
They're just some random completion

#### [Kenny Lau (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390646):
I was about to say, let's study other local fields

#### [Kevin Buzzard (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390647):
that sometimes helps in physics

#### [Kevin Buzzard (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390649):
exactly

#### [Mario Carneiro (Jun 01 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390651):
you don't need *full* completion in 99.9% of cases

#### [Kenny Lau (Jun 01 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390657):
but there's a problem @**Mario Carneiro**

#### [Kevin Buzzard (Jun 01 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390658):
in number theory we need the product of all the completions :-)

#### [Mario Carneiro (Jun 01 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390659):
something like complete under computable sequences is more than enough

#### [Kevin Buzzard (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390699):
Mario do you think Langlands' work on cyclic base change would work with this smaller subset of the reals?

#### [Mario Carneiro (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390700):
or maybe "complete under all the operations I'm talking about today"

#### [Kevin Buzzard (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390705):
I'm sure it uses AC everywhere

#### [Kenny Lau (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390706):
I can't recall the name of the theroem

#### [Mario Carneiro (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390707):
it's not so different to doing categories in ZFC

#### [Kenny Lau (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390709):
but essentially, if you include exp, then your field is noncomputable

#### [Kenny Lau (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390710):
algebraic numbers and exp

#### [Kenny Lau (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390711):
maybe some other things

#### [Kenny Lau (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390712):
maybe you'll know the name

#### [Mario Carneiro (Jun 01 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390713):
you just want enough stuff for your theorem, but you assume too much for simplicity

#### [Mario Carneiro (Jun 01 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390779):
@**Kenny Lau** I guess it would be too easy to just compute to find out if e + pi is irrational

#### [Kenny Lau (Jun 01 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390782):
that's irrelevant

#### [Kenny Lau (Jun 01 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390784):
for every rational r, if you spent enough time, you can prove that e+pi is not r

#### [Kenny Lau (Jun 01 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390825):
you just can't prove that, for every rational r, e+pi is not r

#### [Kenny Lau (Jun 01 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390829):
decidable equality doesn't mean decidable pi equality

#### [Kenny Lau (Jun 01 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390831):
pi equality meaning forall equality

#### [Kenny Lau (Jun 01 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390832):
not 3.14159

#### [Mario Carneiro (Jun 01 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390834):
I know, but rationality is decidable on algebraic numbers

#### [Kenny Lau (Jun 01 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390835):
oh is it

#### [Kenny Lau (Jun 01 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390837):
how do you define algebraic numbers?

#### [Mario Carneiro (Jun 01 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390838):
yes, just compute the minimal polynomial and see if it has degree 1

#### [Kenny Lau (Jun 01 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390845):
do you store the minimal polynomial?

#### [Mario Carneiro (Jun 01 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390846):
yes

#### [Kenny Lau (Jun 01 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390847):
I see

#### [Mario Carneiro (Jun 01 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390900):
I think the most impressive thing about the algebraic numbers is that irreducibility and factoring of Q[x] polynomials is decidable

#### [Kenny Lau (Jun 01 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127390904):
agree

#### [Kevin Buzzard (Jun 01 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391365):
come on norm-num

#### [Kevin Buzzard (Jun 01 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391366):
`↑⌊0⌋ * 10 = 0`

#### [Kevin Buzzard (Jun 01 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391367):
you can do it

#### [Kevin Buzzard (Jun 01 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391369):
gaargh

#### [Kevin Buzzard (Jun 01 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391374):
stupid floor function

#### [Kevin Buzzard (Jun 01 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391420):
oh there is a lemma

#### [Kevin Buzzard (Jun 01 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391422):
I remember now

#### [Kevin Buzzard (Jun 01 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391429):
`floor_coe`

#### [Mario Carneiro (Jun 01 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391439):
I guess floor_zero and floor_one should be simp lemmas

#### [Mario Carneiro (Jun 01 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391442):
and theorems

#### [Kevin Buzzard (Jun 01 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391511):
oh you're right, that's not (0 : Z)

#### [Kevin Buzzard (Jun 01 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391514):
that one of your other zeros

#### [Mario Carneiro (Jun 01 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391560):
it's defeq though, you can just apply `floor_coe`

#### [Kevin Buzzard (Jun 01 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391939):
not in a rewrite :-/

#### [Mario Carneiro (Jun 01 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391953):
here, use as you like:
```
@[simp] theorem floor_zero : ⌊(0:α)⌋ = 0 := floor_coe 0

@[simp] theorem floor_one : ⌊(1:α)⌋ = 1 :=
by rw [← int.cast_one, floor_coe]
```

#### [Kenny Lau (Jun 01 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127391956):
```quote
that one of your other zeros
```
lol

#### [Mario Carneiro (Jun 01 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392017):
unfortunately this doesn't help with say `⌊2⌋ = 2`, that gets tricky in general

#### [Mario Carneiro (Jun 01 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392018):
because the two `2`'s are represented differently

#### [Kevin Buzzard (Jun 01 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392030):
I've got interested in what needs names

#### [Kevin Buzzard (Jun 01 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392031):
I would vote for floor_zero

#### [Kevin Buzzard (Jun 01 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392080):
rofl I just tried it in my code and it didn't work

#### [Kevin Buzzard (Jun 01 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392085):
and then I remembered that someone writing some code on the internet doesn't mean my computer runs it

#### [Kevin Buzzard (Jun 01 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392087):
and you have to copy paste

#### [Mario Carneiro (Jun 01 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392101):
Those lines were written in `archimedean.lean`, they might not work out of context

#### [Kevin Buzzard (Jun 01 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392176):
I know archimedean.lean so I could fix it up

#### [Kevin Buzzard (Jun 01 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392179):
I've been reading some of the real code recently

#### [Kevin Buzzard (Jun 01 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392181):
and I'd missed archimedean so I read it the moment Kenny pointed it out to me

#### [Mario Carneiro (Jun 01 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392183):
I already have added those lines to my local copy, they will be out with the next batch

#### [Kevin Buzzard (Jun 01 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392224):
I was just thinking I should do the same

#### [Kevin Buzzard (Jun 01 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392225):
but for me it's much harder

#### [Kevin Buzzard (Jun 01 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392232):
I'm doing undergrad stuff in my xena project at the minute (e.g. decimal expansions) but the library imports your mathlib

#### [Kevin Buzzard (Jun 01 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127392249):
so I can't edit my fork of your mathlib and then run it easily in my project, unless I actually start importing my mathlib

#### [Kevin Buzzard (Jun 01 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393083):
ha ha, to finish Q2 of my exam all I now need to do is to prove that if `s : ℝ := 71/100` then `⌊s⌋ = 7`

#### [Kevin Buzzard (Jun 01 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393085):
the students didn't spend too much time on this bit

#### [Kenny Lau (Jun 01 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393100):
does that mean you finished Q1?

#### [Mario Carneiro (Jun 01 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393146):
I guess this isn't stated as a theorem explicitly, but the way to prove `⌊x⌋ = n` is to prove `n <= x < n+1`, and norm_num will usually take care of that

#### [Kevin Buzzard (Jun 01 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393148):
no

#### [Kevin Buzzard (Jun 01 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393149):
I liked Q2 better

#### [Kevin Buzzard (Jun 01 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393151):
right

#### [Mario Carneiro (Jun 01 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393153):
also, the theorem you stated is false

#### [Mario Carneiro (Jun 01 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393159):
the floor of s is zero

#### [Kevin Buzzard (Jun 01 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393160):
:-)

#### [Kevin Buzzard (Jun 01 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393161):
oh too many 10s

#### [Kevin Buzzard (Jun 01 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393162):
sorry

#### [Kevin Buzzard (Jun 01 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393167):
I have to work out the full decimal expansion

#### [Kevin Buzzard (Jun 01 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393169):
so i need a fair few floors

#### [Mario Carneiro (Jun 01 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393211):
You really want to do this on rat

#### [Mario Carneiro (Jun 01 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393212):
then you can just compute

#### [Mario Carneiro (Jun 01 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393216):
just take your real number and map it to rat

#### [Kevin Buzzard (Jun 01 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393271):
I didn't know to what extent that mattered

#### [Kevin Buzzard (Jun 01 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393275):
now I need some theorem that says that the floors agree

#### [Kevin Buzzard (Jun 01 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393282):
`noncomputable definition s : ℝ := 71/100
lemma bound1 : 0 ≤ s := by norm_num -- fails` :-(

#### [Mario Carneiro (Jun 01 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393284):
I am already on it

#### [Kenny Lau (Jun 01 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393285):
`by unfold s; norm_num`

#### [Kevin Buzzard (Jun 01 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127393286):
thanks

#### [Mario Carneiro (Jun 01 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394102):
this should work for you:
```
@[simp] theorem rat.cast_floor
  {α} [linear_ordered_field α] [archimedean α] (x : ℚ) :
  by haveI := archimedean.floor_ring α; exact ⌊(x:α)⌋ = ⌊x⌋ :=
begin
  haveI := archimedean.floor_ring α,
  apply le_antisymm,
  { rw [le_floor, ← @rat.cast_le α, rat.cast_coe_int],
    apply floor_le },
  { rw [le_floor, ← rat.cast_coe_int, rat.cast_le],
    apply floor_le }
end
```

#### [Kevin Buzzard (Jun 01 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394219):
you have to use `haveI` in the statement to make it typecheck

#### [Mario Carneiro (Jun 01 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394222):
I did...

#### [Kevin Buzzard (Jun 01 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394224):
and then again in the proof

#### [Kevin Buzzard (Jun 01 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394227):
The devs don't come here, this is the maths chat

#### [Kevin Buzzard (Jun 01 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394230):
what do you think about all this haveI stuff?

#### [Kevin Buzzard (Jun 01 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394269):
Aren't things worse than they used to be?

#### [Kevin Buzzard (Jun 01 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394272):
Or did other stuff get fixed when that change was made?

#### [Mario Carneiro (Jun 01 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394273):
I think I got Leo angry about it, so I'm not going to try again

#### [Mario Carneiro (Jun 01 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394275):
haveI is the compromise position

#### [Mario Carneiro (Jun 01 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394281):
...but it's not unreasonable here

#### [Mario Carneiro (Jun 01 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394290):
I'm injecting an instance which is not an instance normally

#### [Kevin Buzzard (Jun 01 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394371):
Thanks.

#### [Kevin Buzzard (Jun 01 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394670):
I feel like I want to apply `int.succ_le_of_lt` out of decency

#### [Kevin Buzzard (Jun 01 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394677):
`lemma int.succ_le_of_lt (a b : ℤ) : a < b → int.succ a ≤ b :=`

#### [Kevin Buzzard (Jun 01 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394680):
but proof is id

#### [Mario Carneiro (Jun 01 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394683):
It's up to you

#### [Kevin Buzzard (Jun 01 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394721):
it looks like bad style to just know it's id

#### [Kenny Lau (Jun 01 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394724):
who the .... cares

#### [Kevin Buzzard (Jun 01 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394727):
it's the interface Kenny

#### [Kenny Lau (Jun 01 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394734):
proofs are irrelevant

#### [Kevin Buzzard (Jun 01 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394735):
id sometimes deserves a name :-)

#### [Kevin Buzzard (Jun 01 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394740):
proofs are irrelevant but names are important

#### [Mario Carneiro (Jun 01 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394744):
You are absolutely right, using defeq like this breaks the interface

#### [Mario Carneiro (Jun 01 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394750):
but it's not a hill I want to die on

#### [Mario Carneiro (Jun 01 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127394759):
I would say "use in moderation"

#### [Kevin Buzzard (Jun 01 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395229):
```lean
lemma floor_of_bounds (r : α) (z : ℤ) :
  ↑z ≤ r ∧ r < (z + 1) ↔ ⌊ r ⌋ = z :=
begin
  split,swap, -- easy one
  { intro H,rw ←H,
    split,exact floor_le r,
    suffices : r < ↑⌊r⌋ + (1 : ℤ),
      simpa using this,
    have H' := lt_succ_floor r,
    rw ←int.cast_add,
    exact H',
  },
  have H := λ d, @le_floor α _ d r,
  
  intro J,cases J with floor_le' lt_succ_floor',
  cases (le_or_gt ⌊r⌋ z) with HT HF,
  swap, exfalso, -- false one
  { have XXX := (H (z+1)).1 (int.succ_le_of_lt _ _ HF),
    rw int.cast_add at XXX,
    clear HF,
    have H2 := lt_of_le_of_lt XXX lt_succ_floor',
    revert H2,simp, 
  }, 
  cases lt_or_eq_of_le HT with HF HT',swap,exact HT',
  exfalso,
  have XXX := (H z).2 floor_le',
  apply lt_irrefl z,
  exact lt_of_le_of_lt XXX HF,
end
```

#### [Kevin Buzzard (Jun 01 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395230):
Rubbish lean code but it's a proof

#### [Kevin Buzzard (Jun 01 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395235):
What tricks am I missing?

#### [Kenny Lau (Jun 01 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395291):
`le_floor`?

#### [Kenny Lau (Jun 01 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395337):
given `z <= r`, use `le_floor` to deduce `z <= floor(r)`

#### [Kevin Buzzard (Jun 01 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395346):
here's the reals back to their old tricks

#### [Kenny Lau (Jun 01 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395388):
given `r < z+1`, `floor_lt` tells you `floor(r) < z + 1`

#### [Kenny Lau (Jun 01 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395391):
then deduce `floor(r) <= z` (everything is an integer now)

#### [Kenny Lau (Jun 01 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395393):
and then `le_antisymm`

#### [Kevin Buzzard (Jun 01 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395400):
```lean
noncomputable definition s : ℝ := 71/100

example : floor s = 0 := 
begin
show floor ((71/100:ℚ):ℝ) = 0,
admit
end 
```

#### [Kevin Buzzard (Jun 01 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395401):
deterministic timeout

#### [Kenny Lau (Jun 01 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395406):
because 71:R / 100:R is not defeq to 71:Q / 100:Q

#### [Kevin Buzzard (Jun 01 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395446):
I did it by contradiction :-)

#### [Kevin Buzzard (Jun 01 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395450):
you always want to do things constructively

#### [Kenny Lau (Jun 01 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395451):
?

#### [Kenny Lau (Jun 01 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395454):
I see

#### [Kenny Lau (Jun 01 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395455):
to each their own

#### [Kenny Lau (Jun 01 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395457):
I have no time

#### [Kenny Lau (Jun 01 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395458):
I need to learn what the Weil group is

#### [Kevin Buzzard (Jun 01 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395459):
oh the coercion to R is done before the division

#### [Mario Carneiro (Jun 01 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395466):
The magic of biconditional theorems...
```
lemma floor_of_bounds (r : α) (z : ℤ) :
  ↑z ≤ r ∧ r < (z + 1) ↔ ⌊ r ⌋ = z :=
by rw [← le_floor, ← int.cast_one, ← int.cast_add, ← floor_lt,
  int.lt_add_one_iff, le_antisymm_iff, and.comm]
```

#### [Kenny Lau (Jun 01 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395470):
lol

#### [Kenny Lau (Jun 01 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395472):
two lines vs 100 lines

#### [Kevin Buzzard (Jun 01 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395473):
very nice

#### [Kevin Buzzard (Jun 01 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395475):
but I never got stuck

#### [Kevin Buzzard (Jun 01 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395477):
I just proved it and enjoyed it

#### [Kevin Buzzard (Jun 01 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395478):
walking around the gardens of mathematics

#### [Mario Carneiro (Jun 01 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395526):
oh you proved by contradiction

#### [Mario Carneiro (Jun 01 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395527):
that's a bit roundabout

#### [Kevin Buzzard (Jun 01 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395571):
it's inbuilt

#### [Kevin Buzzard (Jun 01 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395575):
I asked 250 students to prove sup(S) + sup(T) = sup(S+T)

#### [Mario Carneiro (Jun 01 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395576):
you have so many cases in this proof...

#### [Kevin Buzzard (Jun 01 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395577):
and about 80 did it

#### [Kenny Lau (Jun 01 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395578):
really

#### [Kevin Buzzard (Jun 01 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395579):
and 79 did it by contradiction

#### [Kenny Lau (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395581):
such a simple theorem

#### [Kenny Lau (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395584):
only 80 out of 250

#### [Kevin Buzzard (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395588):
it's about that

#### [Kevin Buzzard (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395590):
I didn't count carefully and it's all gone back to the exams office now

#### [Kenny Lau (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395591):
@**Mario Carneiro** and the 1 is me lol

#### [Kevin Buzzard (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395592):
maybe more

#### [Mario Carneiro (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395594):
I recall this story

#### [Kenny Lau (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395595):
like seriously

#### [Kenny Lau (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395598):
the UMPs of sup is all you need

#### [Kevin Buzzard (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395599):
contradiction is the most powerful method of proof

#### [Kevin Buzzard (Jun 01 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395600):
you get to assume the most stuff

#### [Kenny Lau (Jun 01 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395640):
but 0% of the people know about UMP and UMP of sup

#### [Kenny Lau (Jun 01 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395644):
rounded down to the nearest percent

#### [Mario Carneiro (Jun 01 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395645):
I'm not even against it on intuitionistic grounds

#### [Kevin Buzzard (Jun 01 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395647):
if you've never had your brain polluted by constructivism it's a very natural first step

#### [Kenny Lau (Jun 01 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395652):
cleansed

#### [Mario Carneiro (Jun 01 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395654):
it has a way of making thinking easier and proof more complicated

#### [Kevin Buzzard (Jun 01 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395656):
right

#### [Kevin Buzzard (Jun 01 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395658):
I even saw, on several occasions, and this is certainly not the first time,

#### [Kevin Buzzard (Jun 01 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395659):
people writing

#### [Kenny Lau (Jun 01 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395666):
it's not even about constructivism anymore, I'm just chaining UMPs all around

#### [Kenny Lau (Jun 01 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395669):
it's not about constructivism when people use UMP in category theory

#### [Kenny Lau (Jun 01 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395670):
because it's what it is

#### [Kenny Lau (Jun 01 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395671):
it's the UMP

#### [Kevin Buzzard (Jun 01 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395672):
"We want to prove X. Let's prove it by contradiction. So assume X is false. Now consider the following perfectly good proof of X. But X is false! Contradiction!

#### [Kevin Buzzard (Jun 01 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395674):
"

#### [Kenny Lau (Jun 01 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395713):
if you are a lazy person who only knows proof by contradiction it's a very natural first step

#### [Mario Carneiro (Jun 01 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395720):
For things like timed tests it's a good strategy

#### [Kenny Lau (Jun 01 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395723):
I find UMPs easier

#### [Mario Carneiro (Jun 01 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395726):
where you just write and write until you get the answer

#### [Kenny Lau (Jun 01 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395732):
I just use 100 UMPs until I get the answer

#### [Kenny Lau (Jun 01 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395733):
and I always get it

#### [Kenny Lau (Jun 01 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395734):
because it's universal

#### [Mario Carneiro (Jun 01 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395736):
Also resolution theorem proving is based on this idea

#### [Kenny Lau (Jun 01 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395745):
solve_by_elim ain't

#### [Mario Carneiro (Jun 01 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395748):
where you whittle down a counterexample until it is impossible

#### [Mario Carneiro (Jun 01 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395790):
but the resulting proof looks ugly I think

#### [Kenny Lau (Jun 01 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395800):
(whatever)

#### [Mario Carneiro (Jun 01 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395801):
when you want that "polished" look it's best to avoid proof by contradiction

#### [Kevin Buzzard (Jun 01 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395980):
My goal is `has_le.le (coe 0) (has_div.div 71 100)`

#### [Kevin Buzzard (Jun 01 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127395983):
and if I try and unfold either `has_le.le` or `coe` I get a deterministic timeout

#### [Kenny Lau (Jun 01 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396024):
so don't unfold them?

#### [Kevin Buzzard (Jun 01 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396038):
norm_num times out too

#### [Kenny Lau (Jun 01 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396081):
did you use `div` lemmas?

#### [Kenny Lau (Jun 01 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396082):
`div_nonneg`

#### [Kevin Buzzard (Jun 01 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396084):
oh I need to feed those in

#### [Kenny Lau (Jun 01 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396085):
you just need that one

#### [Kenny Lau (Jun 01 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396087):
the rest should be `norm_num`

#### [Kevin Buzzard (Jun 01 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396088):
do I put it in the context?

#### [Kenny Lau (Jun 01 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396096):
no, you apply it

#### [Kevin Buzzard (Jun 01 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396146):
you want me to actually prove it by hand??

#### [Kevin Buzzard (Jun 01 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396149):
what is this -- the 1980s?

#### [Kevin Buzzard (Jun 01 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396152):
we have norm_num!

#### [Kenny Lau (Jun 01 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396163):
my math teacher at high school would tell the story of people using calculators to verify that 5 x 0 = 0

#### [Kevin Buzzard (Jun 01 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396207):
`refine div_nonneg _ _,` times out

#### [Kevin Buzzard (Jun 01 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396209):
everything times out

#### [Kevin Buzzard (Jun 01 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396211):
my goal is corrupted

#### [Kenny Lau (Jun 01 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396215):
code

#### [Kevin Buzzard (Jun 01 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396229):
```lean

noncomputable definition s : ℝ := 71/100

theorem sQ : s = ((71/100:ℚ):ℝ) := by unfold s;norm_num 

--set_option pp.all true
example : floor s = 0 := 
begin
rw [sQ,rat.cast_floor],
apply (floor_of_bounds _ _).1,
split,
{ have H : (100 : ℚ)> 0 := by norm_num,
  refine div_nonneg _ _,
  --unfold has_le.le,
--show 0 ≤ 71 / 100,
  
    sorry},
{sorry}
end 
```

#### [Kevin Buzzard (Jun 01 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396231):
all this fuss about `0.71`

#### [Kevin Buzzard (Jun 01 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396232):
I should have been in bed hours ago

#### [Kevin Buzzard (Jun 01 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396276):
I'm glad none of my students spent 2 hours on this bit

#### [Kevin Buzzard (Jun 01 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396283):
it was only a 2 hour exam

#### [Kenny Lau (Jun 01 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396337):
```lean
example : floor s = 0 :=
begin
  rw ← floor_of_bounds,
  split,
  { unfold s, apply div_nonneg; norm_num },
  { unfold s, rw div_lt_iff; norm_num }
end
```

#### [Mario Carneiro (Jun 01 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396449):
```
example : floor s = 0 := by rw [← floor_of_bounds, s, int.cast_zero]; norm_num
```

#### [Kevin Buzzard (Jun 01 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396503):
So using rat.cast_floor was a bad idea

#### [Kevin Buzzard (Jun 01 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396509):
Even though my instinct is to get out of R ASAP

#### [Kenny Lau (Jun 01 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396510):
there's a box

#### [Mario Carneiro (Jun 01 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396511):
I meant to use that if you were planning on kernel computation

#### [Kenny Lau (Jun 01 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396512):
think out of it

#### [Kenny Lau (Jun 01 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396513):
@**Mario Carneiro** i couldn't get the kernel to compute it

#### [Mario Carneiro (Jun 01 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396517):
Actually `71` might be too big for the kernel...

#### [Kenny Lau (Jun 01 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396521):
lol

#### [Kenny Lau (Jun 01 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396524):
71 is too big for the kernel

#### [Kenny Lau (Jun 01 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396526):
https://tio.run/##K6gsycjPM/7/v6AoM69Ew9xQS8vcUPP/fwA

#### [Mario Carneiro (Jun 01 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396531):
that's VM computation though

#### [Mario Carneiro (Jun 01 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396534):
or would be if it were lean

#### [Mario Carneiro (Jun 01 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396578):
python doesn't have to bother proving it is correct

#### [Mario Carneiro (Jun 01 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127396582):
and it also doesn't use a braindead representation

#### [Kevin Buzzard (Jun 01 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127397530):
Kenny I did it:

#### [Kevin Buzzard (Jun 01 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127397531):
`theorem no_eights (n : ℕ) : decimal.expansion s (by unfold s;norm_num) n ≠ 8 := ...`

#### [Kevin Buzzard (Jun 01 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127397532):
`0.71` has no 8's in its decimal expansion

#### [Johan Commelin (Jun 01 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127402805):
```quote
Actually `71` might be too big for the kernel...
```
Would it help if we compute in base $$r$$ (with $$r = 10$$ or $$16$$)? Then we could have a lookup-table of simp-lemmas. And we could implement stuff like https://en.wikipedia.org/wiki/Multiplication_algorithm#Karatsuba_multiplication

#### [Johan Commelin (Jun 01 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127402818):
And for specific computations, of course a specific base could be used, with pre-computed lookup-tables.

#### [Johan Commelin (Jun 01 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127402890):
Ok, to be clear: I am not suggesting that we change the implementation of `nat`. But I am suggesting that we have a parallel implementation specifically for computations in base `r`. And an isomorphism between the implementations.

#### [Johan Commelin (Jun 01 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127402899):
But maybe this means that we also need a parallel implementation of `int` and `rat`. And then I'm not sure if I would want to go down that rabbit-hole

#### [Mario Carneiro (Jun 01 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403216):
Yes, it would help to work in base r. The really important part is that r should be greater than 1

#### [Mario Carneiro (Jun 01 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403221):
The `num` type is used to address these issues, by implementing binary natural numbers instead of the default `nat` which is unary

#### [Mario Carneiro (Jun 01 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403272):
`znum` is the parallel implementation of `int`; there is no qnum type (yet)

#### [Johan Commelin (Jun 01 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403365):
Hmm, ok. So then you would need a `qnum` and afterwards an `rnum` and a `cnum`...

#### [Mario Carneiro (Jun 01 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403409):
well, those last two don't matter anyway

#### [Mario Carneiro (Jun 01 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403415):
or at least, they would be significantly different from the `real` type you know and love

#### [Mario Carneiro (Jun 01 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403421):
because computable reals are not like regular reals

#### [Johan Commelin (Jun 01 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403424):
I am not suggesting that `rnum` be computable

#### [Johan Commelin (Jun 01 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403431):
But maybe then it isn't useful either (-;

#### [Mario Carneiro (Jun 01 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403438):
That's the whole point

#### [Mario Carneiro (Jun 01 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403446):
The idea is to have a "programming numbers" type which is proven isomorphic to the abstract version

#### [Johan Commelin (Jun 01 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403450):
Right

#### [Johan Commelin (Jun 01 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403501):
But for a speed-up of Kevin's question, you would like to convert to `num` at some point. Is that correct?

#### [Mario Carneiro (Jun 01 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403502):
Unfortunately, you currently have to make a decision between VM-optimized and kernel-optimized data types

#### [Mario Carneiro (Jun 01 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403511):
so there are valid reasons to keep both around

#### [Mario Carneiro (Jun 01 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403555):
`nat` is actually the faster one in the VM, because lean replaces it with GMP bignums or C ints if small enough

#### [Mario Carneiro (Jun 01 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403558):
while `num` is just a regular inductive type so it's implemented as a linked list of digits

#### [Mario Carneiro (Jun 01 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403607):
If you want to prove theorems by `rfl` or `dec_trivial`, you need to use kernel-efficient data types or else keep the numbers very small

#### [Johan Commelin (Jun 01 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403619):
Yes, I understand. So, are things like Karatsuba or Tom-Cook implemented for `num`?

#### [Mario Carneiro (Jun 01 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403621):
If you are using `norm_num` or `simp`, you want VM-efficient data types

#### [Mario Carneiro (Jun 01 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403622):
No, the numbers have not got that big (yet)

#### [Mario Carneiro (Jun 01 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403662):
That requires significant size before it pays off

#### [Johan Commelin (Jun 01 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403665):
I guess another problem is that for big numbers the conversion between `nat` and `num` will become the bottle-neck. Right?

#### [Mario Carneiro (Jun 01 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403666):
You can't do anything that even mentions `nat` in the kernel with big numbers

#### [Mario Carneiro (Jun 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403686):
you can't even accept nat input and convert to num because the parser produces some `bit0 (bit0 ... 1)` term to pass to your function, and the kernel evaluates it before getting to your function

#### [Johan Commelin (Jun 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403713):
O.o (-;

#### [Mario Carneiro (Jun 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403716):
So this means that any conversion from `nat` has to be done in the VM. The good news is that this can be done efficiently and still be verified

#### [Johan Commelin (Jun 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403722):
Ok, I don't follow this anymore... but I think it means that I can relax (-;

#### [Mario Carneiro (Jun 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403724):
You just have theorems saying `bit0 \u x = \u bit0 x` where `\u : nat -> num`

#### [Johan Commelin (Jun 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403725):
I thought that the VM cheated... and you would lose verification

#### [Mario Carneiro (Jun 01 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403754):
and you have a tactic (running in the VM) that selectively chooses to apply this theorem

#### [Mario Carneiro (Jun 01 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403766):
by looking at the *term* in the goal

#### [Mario Carneiro (Jun 01 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403771):
with regular lean functions you can only look at the value that is given, but tactics can decompose the expr that represents the value

#### [Mario Carneiro (Jun 01 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403779):
so something like `bit0 (bit0 ... 1)` has reasonable size as a term but not as a value

#### [Mario Carneiro (Jun 01 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403816):
and you can apply log(n) `bit0 \u x = \u bit0 x` theorems to get it down to a theorem just about `num`

#### [Mario Carneiro (Jun 01 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403820):
and then you prove by `rfl` or whatever

#### [Mario Carneiro (Jun 01 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403821):
and the kernel never has to evaluate big nats

#### [Johan Commelin (Jun 01 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403881):
Ok, I see the strategy.

#### [Johan Commelin (Jun 01 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403891):
I think Kevin is going to like that if at some point he wants to do some modular form stuff...

#### [Johan Commelin (Jun 01 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403897):
Because their coefficients explode

#### [Mario Carneiro (Jun 01 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403938):
So `norm_num` is also working in binary, I guess

#### [Mario Carneiro (Jun 01 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403940):
it produces a theorem that is longer for larger numbers though

#### [Mario Carneiro (Jun 01 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403944):
while a kernel proof is always just `rfl`

#### [Mario Carneiro (Jun 01 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127403990):
For the most part, kernel computation is discouraged because it's not particularly optimized for that

#### [Mario Carneiro (Jun 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404013):
But I think it's amusing that in dependent type theory you can write down a very short proof of almost anything

#### [Johan Commelin (Jun 01 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404066):
What do you mean with that last statement?

#### [Mario Carneiro (Jun 01 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404068):
for example, I can write a program that enumerates proofs in ZFC or whatever, and then if there is a proof of RH with fewer than 2^2^2^2^2^2^2^2^2^2^2 symbols, then I can prove it by `rfl`

#### [Johan Commelin (Jun 01 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404077):
Right, but that proof will require a lot of prerequisite work

#### [Johan Commelin (Jun 01 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404078):
(Which I consider part of the proof.)

#### [Mario Carneiro (Jun 01 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404123):
The only work that needs to be done is the setup, stating the problem

#### [Mario Carneiro (Jun 01 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404127):
the "hard part" is completely absent from the accounting, except in the length bound

#### [Mario Carneiro (Jun 01 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404134):
but I can write functions that grow ridiculously fast in DTT so that's not saying much

#### [Johan Commelin (Jun 01 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404140):
Ok, so we can prove that RH doesn't have a short proof.

#### [Johan Commelin (Jun 01 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404141):
And neither has Fermat's Last Theorem

#### [Mario Carneiro (Jun 01 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404183):
Okay, fermat is a good example, since we know that one is true

#### [Johan Commelin (Jun 01 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404184):
For otherwise they would already have been in mathlib with a `rfl` proof.

#### [Mario Carneiro (Jun 01 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404190):
I can prove Fermat's last theorem by `rfl`

#### [Johan Commelin (Jun 01 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404193):
I would love to see that done.

#### [Johan Commelin (Jun 01 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404195):
The statement is already there

#### [Johan Commelin (Jun 01 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404196):
And that is all the setup you need.

#### [Mario Carneiro (Jun 01 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404211):
I just write a `bool` function that checks the first bazillion proofs and returns `tt` if one works, and assert by `rfl` that it is `tt`

#### [Johan Commelin (Jun 01 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404258):
Right. And of course Lean will never finish running.

#### [Mario Carneiro (Jun 01 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404270):
that proof checks if and only if there is a short enough proof of FLT, and since we know there is, that means I have a short proof

#### [Mario Carneiro (Jun 01 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404282):
Of course the problem with this kind of analysis is that lean will run (almost) forever on such a proof

#### [Mario Carneiro (Jun 01 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404288):
But it seems to be some kind of deficiency in DTT, that the length of a proof is no longer a suitable measure of the hardness of the proof

#### [Johan Commelin (Jun 01 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404323):
Yes, and that's why we still dont have FLT in mathlib (-;

#### [Johan Commelin (Jun 01 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404333):
No, but compile-time is still a good measure

#### [Mario Carneiro (Jun 01 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404340):
Yes. Or number of proof steps including definitional reductions

#### [Mario Carneiro (Jun 01 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404351):
This doesn't come up in ZFC since there's no definitional reduction, what you see is what you get

#### [Mario Carneiro (Jun 01 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404418):
anyway, this "feature" of DTT should be thought of as abuse of lean, so don't be surprised if it starts to sweat

#### [Mario Carneiro (Jun 01 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404428):
when you try to `#reduce 71 / 100`

#### [Johan Commelin (Jun 01 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404477):
Sure, and in fact, we don't even know what the value of "bazillion" is for your `bool` function. We only have a very clear suggestion that it is finite.

#### [Mario Carneiro (Jun 01 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404491):
I think there are some pretty reasonable upper bounds based on physical considerations

#### [Mario Carneiro (Jun 01 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404496):
i.e. the proof appears to fit in the universe, so it's shorter than Graham's number

#### [Johan Commelin (Jun 01 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127404502):
ok, fair enough

#### [Johan Commelin (Jun 01 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127411378):
It seems that `real` is not an instance of `has_pow`. Should I add it, or is there some computability reason for not doing that?

#### [Kevin Buzzard (Jun 01 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414076):
I think the definition of `has_pow` is post-real so it might just be that nobody used them seriously enough since. As you can see, I've come back to the reals recently, and I am always interested in making them "undergraduate-friendly" so I would have run into this sooner or later.

#### [Kevin Buzzard (Jun 01 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414077):
@**Mario Carneiro** -- where do these definitions go? Mathlib? My own Xena library? (I'm writing a library for stuff my UG mathematicians might want or need and which is not in mathlib -- can you envisage there being good reasons for such a library?)

```lean
definition is_upper_bound (x : ℝ) (S : set ℝ) := ∀ s ∈ S, s ≤ x 
definition is_bounded_above (S : set ℝ) := ∃ x, is_upper_bound x S   
definition is_LUB (x : ℝ) (S : set ℝ) := is_upper_bound x S ∧ ∀ y : ℝ, is_upper_bound y S → x ≤ y 

definition has_LUB (S : set ℝ) := ∃ x, is_LUB x S 
```

#### [Johan Commelin (Jun 01 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414310):
Hmm, I guess to do has_pow properly, we should define `x^r` for `x r : real`. And then all of a sudden you have to work.

#### [Johan Commelin (Jun 01 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414359):
Or can we have multiple instances, depending on whether `r` has type `nat` or `int` or `rat` or `real`.

#### [Kevin Buzzard (Jun 01 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414447):
this is exactly the problem with pow

#### [Johan Commelin (Jun 01 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414459):
@**Kevin Buzzard** Isn't `Sup` already on line 316 of data.real.basic?

#### [Kevin Buzzard (Jun 01 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414460):
Chris Hughes wrote exp : C -> C but it's still not in mathlib

#### [Kevin Buzzard (Jun 01 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414712):
That's CS sup

#### [Kevin Buzzard (Jun 01 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414713):
sup(S)+sup(T) = sup(S+T) is not true for that sup

#### [Kevin Buzzard (Jun 01 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414714):
let S have one element and let T be empty

#### [Kevin Buzzard (Jun 01 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414715):
(deleted)

#### [Kevin Buzzard (Jun 01 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414716):
it returns 37 if the set has no sup

#### [Kevin Buzzard (Jun 01 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414717):
This is philosophy not mathematics

#### [Kevin Buzzard (Jun 01 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414723):
but if you're going to define sup globally

#### [Kevin Buzzard (Jun 01 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414776):
then it should be taking values in -infty + R + infty

#### [Kevin Buzzard (Jun 01 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414781):
not just spewing out 37s when it's stuck

#### [Kevin Buzzard (Jun 01 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414795):
You see how my predicate solves this problem?

#### [Kevin Buzzard (Jun 01 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414799):
I can say "if a is the sup of S and b is the sup of T then a + b is the sup of S + T

#### [Johan Commelin (Jun 01 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414804):
Ok, so I read too quickly (-;

#### [Kevin Buzzard (Jun 01 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414807):
My question is how to formalize that statement in mathlib

#### [Kevin Buzzard (Jun 01 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414813):
and my predicates make it look nice and easy

#### [Kevin Buzzard (Jun 01 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414815):
whereas I can't quite do it with what we have

#### [Kevin Buzzard (Jun 01 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414856):
however I am unclear about whether "what I want as someone who wants to formulate elementary lemmas about sup"

#### [Kevin Buzzard (Jun 01 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414862):
has anything to do with "what should be in mathlib"

#### [Kevin Buzzard (Jun 01 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414863):
I am very unclear about what the boundaries of mathlib are

#### [Kevin Buzzard (Jun 01 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414865):
Look, watch this:

#### [Kevin Buzzard (Jun 01 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414867):
@**Mario Carneiro** -- should I put schemes in mathlib? Let me know. I don't care either way but you never answer

#### [Kevin Buzzard (Jun 01 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414871):
he never answers

#### [Kevin Buzzard (Jun 01 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414878):
I think he reads the question, thinks "hmm, I don't know offhand, I should look at the repo, oh look it's 7000 lines of sometimes poorly-written code"

#### [Kevin Buzzard (Jun 01 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414879):
"this will need some thought"

#### [Kevin Buzzard (Jun 01 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414886):
I'll try another approach

#### [Kevin Buzzard (Jun 01 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414954):
@**Mario Carneiro** I think definitions of high-level mathematical objects and statements of extremely technical theorems are extremely important things to have in Lean and I will be making quite a few of these in the future. Do you want them in mathlib or do you feel that they are beyond mathlib's remit? I hope I have conveyed in the past how I feel about this matter (namely that I think that there are many people whose interest would be sparked by a small database of complex objects built in Lean)

#### [Kevin Buzzard (Jun 01 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127414996):
I believe @**Scott Morrison** thinks they should be in mathlib

#### [Johannes Hölzl (Jun 01 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127416299):
least upper bounds etc as predicates are already there: https://github.com/leanprover/mathlib/blob/master/order/bounds.lean

#### [Sebastien Gouezel (Jun 01 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127417740):
You can also have a look at https://github.com/leanprover/mathlib/blob/master/order/conditionally_complete_lattice.lean

#### [Mario Carneiro (Jun 01 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127422500):
>  -- should I put schemes in mathlib? Let me know. I don't care either way but you never answer

RIght now? No. As Patrick has mentioned before, the scheme code is huge and requires major refactoring to go into mathlib, much like some other planned additions, e.g. Scott's category theory stuff (and he's made some progress on this last I checked). As it currently exists, it is written as a "race to the finish" which gets the job done without worrying about looking good while doing it, whereas I need "polished" code to go into mathlib. It's like the difference between research notes and a journal article or textbook. This process of bringing schemes in will take a lot of both of our time and right now I think you have bigger plans, so I would hold off on attempting this for the present.

#### [Mario Carneiro (Jun 01 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127422552):
>  I think definitions of high-level mathematical objects and statements of extremely technical theorems are extremely important things to have in Lean and I will be making quite a few of these in the future. Do you want them in mathlib or do you feel that they are beyond mathlib's remit?

The "level" of the definition is not a problem, it can be as advanced as you like. But it must also be good lean code, that's my main concern.

#### [Mario Carneiro (Jun 01 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127422727):
@**Johan Commelin** There is a definition of has_pow on real, because it is a field. You can use `a^n` where `n : nat` and `a : real`

#### [Mario Carneiro (Jun 01 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127422826):
Actually `a^n` where `n : int` is not quite there, since the instance that exists is for `group`s and `real` isn't a (multiplicative) group. Maybe there should be another definition for `division_ring`s that sets `0^-n = 0`?

#### [Mario Carneiro (Jun 01 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127422964):
You could use the (tiny) library of proper division in mathlib though: `units.mk0 a h` where `a : real` and `h : a != 0` is an element of `units real`, which is a group, so you can raise it to an integer power and coerce back to real

#### [Johan Commelin (Jun 01 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127425169):
Ok, thanks. I will take a look at those functions.

#### [Johan Commelin (Jun 01 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127425350):
Is it now easy to have the integers \cup infty? How about `int \cup -\infty` ? Including the order and addition on them. (Otherwise I could just take `option int`.

#### [Mario Carneiro (Jun 01 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127425837):
Yes, `with_top int` has an addition operation and an order, and is defeq to `option int`

#### [Johan Commelin (Jun 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426287):
Hmm, but there is no `with_bot` for semigroups. I want to define a function `f : nat \to (with_top int)`, and then another function `nat \to real := \lam n, b^(- f(n))`, where `b` is some fixed real number.

#### [Johan Commelin (Jun 01 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426324):
So then I need to extend `-` to `- : with_top int \to with_bot int`. And I need to explain to `has_pow real` that `b^(-infty) = 0`.

#### [Mario Carneiro (Jun 01 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426376):
eww

#### [Mario Carneiro (Jun 01 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426384):
that's a bit specialized

#### [Johan Commelin (Jun 01 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426404):
Ok, `f(n) = infty \iff n = 0`.

#### [Mario Carneiro (Jun 01 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426420):
You can define `-` as `option.map (\lam x, -x)`, and `b^o` where `o : with_bot int` by cases

#### [Johan Commelin (Jun 01 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426421):
The other option is that I just use if-then-else everywhere... but I don't really like that either...

#### [Mario Carneiro (Jun 01 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426432):
no if-then

#### [Mario Carneiro (Jun 01 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426437):
it's an option, use cases

#### [Johan Commelin (Jun 01 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426457):
Right. (I meant avoiding `option` and just do `dite (n = 0)` in all the definitions.

#### [Johan Commelin (Jun 01 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426525):
(This stuff shows up everywhere in nonarchimedean valuations.)

#### [Mario Carneiro (Jun 01 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426532):
what `n = 0` are you talking about?

#### [Mario Carneiro (Jun 01 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426548):
you said `f` returns an option

#### [Mario Carneiro (Jun 01 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426554):
well, a `with_top`

#### [Johan Commelin (Jun 01 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426559):
Yes, but I could also define `f` on `pnat`, and `g` with a `dite`.

#### [Johan Commelin (Jun 01 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426561):
Right?

#### [Mario Carneiro (Jun 01 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426610):
Oh, I misunderstood your iff statement

#### [Johan Commelin (Jun 01 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426662):
But I like your approach. I'll try to implement it when I'm back at Lean. (And should I just clone and dualise the `with_top` stuff to `with_bot` for semigroups?

#### [Mario Carneiro (Jun 01 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426664):
It's already there

#### [Johan Commelin (Jun 01 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426731):
Hmm, for `with_bot` I only see instances for partial orders and lattices. Not for semigroups.

#### [Mario Carneiro (Jun 01 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426754):
There is `with_zero` also, there are lots of ways to construe the added element in all the structures

#### [Mario Carneiro (Jun 01 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426835):
Oh, I see, `with_top` and `with_bot` are actually the same as add_semigroups

#### [Johan Commelin (Jun 01 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426845):
Ok, so maybe you can also give a hint on how to define `f`. It is the p-adic valuation (where p is a prime). So `f(n)` is the maximal `e : nat` such that `p^e` divides `n`.

#### [Johan Commelin (Jun 01 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426852):
```quote
Oh, I see, `with_top` and `with_bot` are actually the same as add_semigroups
```
Yes, but not as ordered add_semigroups.

#### [Mario Carneiro (Jun 01 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426863):
Yeah, I'll work on that

#### [Reid Barton (Jun 01 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426978):
@**Johan Commelin** see https://gist.github.com/rwbarton/599327954b01b2e840894189981172ea

#### [Mario Carneiro (Jun 01 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127426979):
First, I would want a "prime count" function that takes a nat and finds the appropriate power of p. It is defined arbitrarily at zero, but for concreteness that means `f 0 = 0`

#### [Reid Barton (Jun 01 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127427030):
I gave that to Kevin earlier and I think he has improved it some in the Fibonacci project

#### [Johan Commelin (Jun 01 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127427033):
Yes, or f 0 = infty. And then you would be done.

#### [Johan Commelin (Jun 01 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127427047):
Reid, thanks. I'll take a look.

#### [Mario Carneiro (Jun 01 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127427048):
Then the valuation function is defined by cases on `n`

#### [Mario Carneiro (Jun 01 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127427138):
actually, I just checked what I did in metamath for this and I used with_top as well. So past me seems to think that's a better idea

#### [Mario Carneiro (Jun 01 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127427163):
I'm a bit worried about having to coerce all the time though

#### [Kevin Buzzard (Jun 01 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428342):
I don't think I ever got the code completely working in the Fibonacci project, there was perhaps one sorry I never got rid of

#### [Kevin Buzzard (Jun 01 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428438):
```quote
As it currently exists, it is written as a "race to the finish" which gets the job done without worrying about looking good while doing it, whereas I need "polished" code to go into mathlib. It's like the difference between research notes and a journal article or textbook. This process of bringing schemes in will take a lot of both of our time and right now I think you have bigger plans, so I would hold off on attempting this for the present.
```

Yes, this is exactly how I wrote it, and I put very little thought into how to make structures because I didn't really know how to make structures at the time. Here are my more long-term thoughts on these matters:

#### [Kevin Buzzard (Jun 01 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428457):
I'm going to do perfectoid spaces because I think it would be funny to do them

#### [Kevin Buzzard (Jun 01 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428470):
Some scheme stuff we will need e.g. sheaves

#### [Kevin Buzzard (Jun 01 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428479):
but I was thinking about re-doing it

#### [Kevin Buzzard (Jun 01 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428485):
doing it all for a second time in a perfectoid spaces directory

#### [Kevin Buzzard (Jun 01 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428548):
and this time doing it better and checking with people like Mario along the way as to whether the structures looked sensible

#### [Kevin Buzzard (Jun 01 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428559):
I understand now much better what I can do well and what I do badly

#### [Kevin Buzzard (Jun 01 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428567):
and especially what I do so badly that it will take a lot of time to fix

#### [Kevin Buzzard (Jun 01 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428580):
I make no apologies for the race to the finish with schemes -- this was simply a test to see if it could be done, and it could be done

#### [Mario Carneiro (Jun 01 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428624):
I thnk that's a good plan

#### [Kevin Buzzard (Jun 01 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428673):
In the long term with schemes, I propose doing perfectoid spaces, seeing the parts which are common to both theories, using this commonality as an argument for inclusion in mathlib, and then spending some time writing these parts of the code properly

#### [Kevin Buzzard (Jun 01 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428688):
so for example we will need sheaves of types at some point

#### [Kevin Buzzard (Jun 01 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428693):
and when we need them in the perfectoid theory I will revisit what I did for schemes

#### [Mario Carneiro (Jun 01 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428694):
The second time around you will have a *much* better appreciation for the subtleties and design questions and can do it right

#### [Kevin Buzzard (Jun 01 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428705):
(in fact we did these already and I even have a suggested definition from Mario somewhere in my starred messages)

#### [Kevin Buzzard (Jun 01 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428708):
yes -- second time round much better

#### [Mario Carneiro (Jun 01 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428729):
Not to mention you are a better lean programmer now than last month (and the month before that etc)

#### [Kevin Buzzard (Jun 01 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428731):
so second time round I think "this is important, I knocked up a definition in 10 minutes when I was doing schemes, here are the problems I had with it, let's fix those problems now and aim for mathlib"

#### [Kevin Buzzard (Jun 01 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428737):
"and write a proper interface while we're here"

#### [Kevin Buzzard (Jun 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428749):
so it's partly some random repo with random bits of people's papers formalised

#### [Kevin Buzzard (Jun 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428789):
and then some directory called "mathlib_someday"

#### [Mario Carneiro (Jun 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428799):
When I look at `dioph.lean` I am ashamed of myself, I would write that so much better now and it's been only a year

#### [Kevin Buzzard (Jun 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428805):
where we put files where someone has actually made an effort to make the file mathlib-worthy

#### [Kevin Buzzard (Jun 01 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127428825):
You're absolutely right that I get better every month. When I started schemes I had no idea how to use type class inference so never used it -- I would just supply all the missing proofs myself.

#### [Scott Morrison (Jun 02 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127440781):
This all sounds like a great plan --- schemes absolutely deserve to be in mathlib (what would be the point of mathlib if we weren't aiming for it to cover the basic essentials?), and at the same time we should try to make sure code going into mathlib is good (not perfect, though).

#### [Scott Morrison (Jun 02 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127440829):
My categories code (getting there! :-) is still abysmal, probably, and I appreciate it's going to be lots of work to get it into mathlib. :-)

#### [Kevin Buzzard (Jun 03 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482657):
```lean
import algebra.archimedean

#check @abs_nonneg
-- abs_nonneg : ∀ {α : Type u_1} 
--   [_inst_1 : decidable_linear_ordered_comm_group α] (a : α),
--   abs a ≥ 0

theorem abs_nonneg' (α : Type) [floor_ring α] [decidable_linear_ordered_comm_group α] 
(r : α) : abs r ≥ 0 := abs_nonneg r -- fails
```

#### [Kevin Buzzard (Jun 03 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482660):
My understanding of something Reid said a few days ago about the reals

#### [Kenny Lau (Jun 03 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482661):
diamond of death?

#### [Kevin Buzzard (Jun 03 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482664):
was that I shouldn't be proving things about the reals

#### [Kevin Buzzard (Jun 03 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482670):
I should just demand I'm a complete totally ordered field and deduce everything from that

#### [Mario Carneiro (Jun 03 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482671):
yeah, this is a diamond problem

#### [Kevin Buzzard (Jun 03 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482672):
but the real problem was decidability I think

#### [Mario Carneiro (Jun 03 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482674):
you have two conflicting group structures on A

#### [Kenny Lau (Jun 03 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482675):
and order structure?

#### [Kevin Buzzard (Jun 03 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482676):
I want to use this abs >= 0 lemma

#### [Kevin Buzzard (Jun 03 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482721):
a floor_ring has an order

#### [Mario Carneiro (Jun 03 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482723):
Why do you have two typeclasses here? that's the question

#### [Reid Barton (Jun 03 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482728):
In this case I think you don't need `decidable_linear_ordered_comm_group`

#### [Mario Carneiro (Jun 03 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482730):
you do, to state `abs`

#### [Mario Carneiro (Jun 03 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482731):
but you don't need the floor_ring

#### [Kevin Buzzard (Jun 03 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482878):
```lean
definition abs_expansion (r : α) [decidable_linear_ordered_comm_group α]: ℕ → ℕ :=
  expansion (abs r) (abs_nonneg r)
```

#### [Kevin Buzzard (Jun 03 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482879):
that's what the problem becomes if I remove the floor_ring

#### [Mario Carneiro (Jun 03 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482884):
what's `expansion`

#### [Kevin Buzzard (Jun 03 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482885):
```
type mismatch at application
  expansion (abs r) _
term
  abs_nonneg r
has type
  @ge α
    (@preorder.to_has_le α
       (@partial_order.to_preorder α
          (@ordered_comm_group.to_partial_order α
             (@decidable_linear_ordered_comm_group.to_ordered_comm_group α _inst_3))))
    (@abs α _inst_3 r)
    0
but is expected to have type
  @ge α
    (@preorder.to_has_le α
       (@partial_order.to_preorder α
          (@ordered_comm_monoid.to_partial_order α
             (@ordered_cancel_comm_monoid.to_ordered_comm_monoid α
                (@ordered_semiring.to_ordered_cancel_comm_monoid α
                   (@ordered_ring.to_ordered_semiring α
                      (@linear_ordered_ring.to_ordered_ring α (@floor_ring.to_linear_ordered_ring α _inst_2))))))))
    (@abs α _inst_3 r)
    0
```

#### [Mario Carneiro (Jun 03 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482887):
Again, conflicting typeclasses

#### [Kevin Buzzard (Jun 03 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482890):
```lean
definition expansion (r : α) (H : r ≥ 0) : ℕ → ℕ
| 0 := int.to_nat (floor r)
| (n + 1) := int.to_nat (floor (chomp r n))
```

#### [Mario Carneiro (Jun 03 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482892):
`inst_3` in one, `inst_2` in the other

#### [Kevin Buzzard (Jun 03 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482895):
But it's just a decidability issue

#### [Mario Carneiro (Jun 03 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482933):
no it's a conflicting typeclasses issue

#### [Kevin Buzzard (Jun 03 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482936):
I just want to "switch decidability on"

#### [Mario Carneiro (Jun 03 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482938):
I assume you don't care about classical?

#### [Kevin Buzzard (Jun 03 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482940):
right

#### [Mario Carneiro (Jun 03 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482941):
just `local instance decidable_prop`

#### [Kevin Buzzard (Jun 03 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127482942):
This is stuff for mathematicians

#### [Mario Carneiro (Jun 03 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483004):
Maybe you should just do this over `\R` instead of `A`

#### [Mario Carneiro (Jun 03 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483006):
or else use the noncomputable floor instance for archimedean `A`

#### [Kevin Buzzard (Jun 03 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483010):
```lean
example (α : Type) [floor_ring α] : add_comm_group α := by apply_instance
example (α : Type) [floor_ring α] : linear_order α := by apply_instance
```

#### [Kevin Buzzard (Jun 03 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483116):
I am a complete idiot

#### [Kevin Buzzard (Jun 03 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483117):
I should just be proving a junk theorem

#### [Kevin Buzzard (Jun 03 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483158):
I was defining decimal expansions of real numbers

#### [Kevin Buzzard (Jun 03 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483159):
and being fussy about issues with negative numbers

#### [Kevin Buzzard (Jun 03 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483168):
I should just let the function return some random result if the input is negative and then stop fussing

#### [Kenny Lau (Jun 03 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483214):
57

#### [Kevin Buzzard (Jun 03 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483216):
I can't believe I'm going to prove a junk theorem

#### [Kevin Buzzard (Jun 03 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483218):
I feel dirty

#### [Kevin Buzzard (Jun 03 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483233):
This is the problem

#### [Kevin Buzzard (Jun 03 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483234):
```lean
definition expansion (r : α) (H : r ≥ 0) : ℕ → ℕ
| 0 := int.to_nat (floor r)
| (n + 1) := int.to_nat (floor (chomp r n))
```

#### [Kevin Buzzard (Jun 03 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483237):
I just have to drop `H`

#### [Mario Carneiro (Jun 03 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483279):
It's not even used

#### [Kevin Buzzard (Jun 03 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483280):
and coerce a negative integer into nat

#### [Kevin Buzzard (Jun 03 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483283):
that's not the point Mario

#### [Kevin Buzzard (Jun 03 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483285):
it's all part of the mathematician's promise

#### [Mario Carneiro (Jun 03 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483288):
That goes in theorems, not definitions

#### [Kevin Buzzard (Jun 03 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483289):
we don't quite model things in the same way

#### [Mario Carneiro (Jun 03 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483298):
I have never seen a mathematician write a function that has an additional proof argument

#### [Mario Carneiro (Jun 03 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483303):
I think they would have a hard time even understanding what that means

#### [Kevin Buzzard (Jun 03 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483304):
```quote
It's not even used
```
it should be there on moral grounds

#### [Kevin Buzzard (Jun 03 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483346):
there should be some tactic bringing it along

#### [Kevin Buzzard (Jun 03 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483349):
"mathematicians promise that they will not run this programme on negative numbers"

#### [Kenny Lau (Jun 03 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483354):
@kevin just treat it like how you treat `nat.sub`

#### [Mario Carneiro (Jun 03 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483355):
You could use `roption` for partial functions too

#### [Kenny Lau (Jun 03 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483356):
"subtraction with a star"

#### [Mario Carneiro (Jun 03 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483399):
alternatively, you could actually make sense of expansions of negative numbers

#### [Mario Carneiro (Jun 03 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483402):
which of course makes perfect sense and generates p-adic numbers

#### [Mario Carneiro (Jun 03 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483404):
or two's complement for the CS folks

#### [Kevin Buzzard (Jun 03 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483414):
```quote
It's not even used
```
It's used in `int.to_nat`

#### [Mario Carneiro (Jun 03 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483464):
Yet more alternatively, don't define it as a function, have an existence theorem

#### [Mario Carneiro (Jun 03 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483466):
the inverse to this is a lot easier to state

#### [Mario Carneiro (Jun 03 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483624):
```
def expansion (r : α) (n : ℕ) : ℕ :=
⌊r * (10 ^ n : ℕ)⌋.nat_mod 10
```

#### [Mario Carneiro (Jun 03 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127483636):
I'm not sure why `n` is a nat here, there are both negative and positive exponent terms in the expansion

#### [Kevin Buzzard (Jun 03 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127484618):
```quote
least upper bounds etc as predicates are already there: https://github.com/leanprover/mathlib/blob/master/order/bounds.lean
```
I see that I did mine a different way around to you. I defined `is_LUB x S` and you `is_lub S x`. Is there a preference for yours over mine? I chose "x S" because I would say x before S ("x is a least upper bound for S")

#### [Mario Carneiro (Jun 03 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127484680):
yes, this allows you to view `is_lub S` as a predicate by currying

#### [Mario Carneiro (Jun 03 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127484692):
generally speaking, more "parameter" like things should come first

#### [Kevin Buzzard (Jun 03 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127484745):
I'm far more likely to be fixing S and trying various x's than I am to be fixing an x and seeing if it bounds any S's, this seems far more unlikely to occur in practice

#### [Mario Carneiro (Jun 03 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127484944):
that's why I said that

#### [Mario Carneiro (Jun 03 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127484947):
`S` is the parameter, `x` is the variable

#### [Mario Carneiro (Jun 03 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127484948):
so `S` comes first

#### [Kevin Buzzard (Jun 03 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127503868):
```quote
that's why I said that
```
I know, I was just translating you into maths

#### [Kevin Buzzard (Jun 04 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518169):
Hey @**Kenny Lau**

#### [Kevin Buzzard (Jun 04 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518175):
I was playing with sups

#### [Kevin Buzzard (Jun 04 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518193):
what do you think this is:

#### [Kevin Buzzard (Jun 04 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518220):
```lean
⟨λ u Hu, let ⟨s,Hs,t,Ht,Hu⟩ := Hu in by rw Hu;exact add_le_add (HSb.1 s Hs) (HTc.1 t Ht),
 λ d Hd,add_le_of_le_sub_right $ HSb.2 (d - c) (λ s Hs,le_sub.1 ((λ s₁ Hs₁,HTc.2 _ (λ t Ht,le_sub_left_of_add_le $ Hd _ ⟨s₁,Hs₁,t,Ht,rfl -- the proof
   ⟩)) s Hs))⟩
```

#### [Kenny Lau (Jun 04 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518224):
my constructive proof?

#### [Kevin Buzzard (Jun 04 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518226):
right

#### [Kenny Lau (Jun 04 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518228):
yay

#### [Kevin Buzzard (Jun 04 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518236):
here's an even better version

#### [Kevin Buzzard (Jun 04 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518237):
I wrote it twice

#### [Kevin Buzzard (Jun 04 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518238):
second time looked like this

#### [Kevin Buzzard (Jun 04 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518240):
```lean
theorem lub_add'' (S T : set ℝ) (b c : ℝ) (HSb : is_lub S b) (HTc : is_lub T c) : is_lub (S + T) (b + c) :=
⟨λ u Hu, let ⟨s,Hs,t,Ht,Hu⟩ := Hu in by rw Hu;exact add_le_add (HSb.1 s Hs) (HTc.1 t Ht),
λ d Hd,add_le_of_le_sub_right $ HSb.2 _ $ λ s Hs,le_sub.1 $ HTc.2 _ $ λ t Ht,le_sub_left_of_add_le $ Hd _ ⟨s,Hs,t,Ht,rfl⟩
⟩
```

#### [Kenny Lau (Jun 04 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518244):
more dollar signs?

#### [Kevin Buzzard (Jun 04 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518245):
`instance : has_add (set ℝ) := ⟨λ S T,{u | ∃ (s ∈ S) (t ∈ T), u = s + t}⟩`

#### [Kevin Buzzard (Jun 04 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518291):
`import order.bounds `

#### [Kevin Buzzard (Jun 04 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518294):
and `analysis.real`

#### [Kevin Buzzard (Jun 04 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518295):
and it will run

#### [Kevin Buzzard (Jun 04 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518298):
I couldn't get that stupid triangle thing to work on the first line of the proof

#### [Kevin Buzzard (Jun 04 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518300):
the \t triangle that Patrick and I both dread

#### [Kevin Buzzard (Jun 04 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518302):
so I have to use rw;exact :-)

#### [Kevin Buzzard (Jun 04 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518309):
so that can be golfed a bit more

#### [Kevin Buzzard (Jun 04 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518311):
but the proof the other way I was extremely pleased with :-)

#### [Kevin Buzzard (Jun 04 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518315):
I formulated the theorem

#### [Kevin Buzzard (Jun 04 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518316):
I proved it in tactic mode

#### [Kevin Buzzard (Jun 04 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518318):
I then translated my tactic mode proof into term mode

#### [Kenny Lau (Jun 04 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518357):
nice!

#### [Kevin Buzzard (Jun 04 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518358):
and then I started again and proved it in term mode

#### [Kevin Buzzard (Jun 04 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518365):
from scratch

#### [Kevin Buzzard (Jun 04 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518370):
looking at my old term mode proof for hints about which arithmetic functions to use :-)

#### [Kevin Buzzard (Jun 04 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518441):
in that last proof line, Lean was somehow always "on the last term" -- I never had to fill in a hole with a non-zero number of characters to the right of it (other than the close bracket)

#### [Kevin Buzzard (Jun 04 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518446):
Kenny if you had given me that answer I would have had a hard time marking it.

#### [Kevin Buzzard (Jun 04 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518485):
I mean the lambda

#### [Kevin Buzzard (Jun 04 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518486):
it's become unreadable, right?

#### [Kenny Lau (Jun 04 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518487):
lol

#### [Kenny Lau (Jun 04 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518488):
but you can verify it

#### [Kevin Buzzard (Jun 04 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/The%20real%20numbers/near/127518498):
that is a very different thing from understanding it

