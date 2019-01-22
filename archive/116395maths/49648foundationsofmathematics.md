---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/49648foundationsofmathematics.html
---

## [maths](index.html)
### [foundations of mathematics](49648foundationsofmathematics.html)

#### [Kevin Buzzard (Apr 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875861):
I spent some time over the last couple of days learning about Voevodsky's work in type theory. I found this paper https://arxiv.org/abs/1711.01477 by Dan Grayson quite illuminating.

#### [Kenny Lau (Apr 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875865):
quite high

#### [Kevin Buzzard (Apr 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875869):
It seems to me that univalent foundations is similar to, but not the same as, DTT

#### [Kevin Buzzard (Apr 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875870):
`a = b` is not a Prop in univalent foundations

#### [Kevin Buzzard (Apr 10 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875877):
In fact there seems to me to be no impredicative Prop universe in univalent foundations

#### [Patrick Massot (Apr 10 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875879):
What happened to your project of documenting what's in mathlib?

#### [Kevin Buzzard (Apr 10 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875882):
there are just some universes, and a Prop is basically defined to be a subsingleton

#### [Kevin Buzzard (Apr 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875923):
But the claim is the same as in Lean -- "we can use this set-up as a way of doing all of maths"

#### [Andrew Ashworth (Apr 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875924):
kenny would love hott

#### [Kenny Lau (Apr 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875926):
```quote
kenny would love hott
```
nope

#### [Kevin Buzzard (Apr 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875928):
One major weakness (possibly only temporary) is that the model you're supposed to carry around is that a type can be thought of as a topological space

#### [Kevin Buzzard (Apr 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875932):
but apparently they can't construct the n-sphere from the axioms

#### [Kevin Buzzard (Apr 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875935):
so they add n-spheres as new inductive types

#### [Kevin Buzzard (Apr 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875936):
and then they can't prove the theory is consistent

#### [Kevin Buzzard (Apr 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875937):
This does not bode well, as far as I can see.

#### [Andrew Ashworth (Apr 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875938):
```quote
```quote
kenny would love hott
```
nope
```
are you a fair-weather constructivist

#### [Kevin Buzzard (Apr 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875941):
I also re-watched Voevodsky's Newton Institute talk from last yeat

#### [Kevin Buzzard (Apr 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875944):
year

#### [Kenny Lau (Apr 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875945):
abuse of topology

#### [Kevin Buzzard (Apr 10 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875984):
and his discussion about how he tried to persuade Suslin to re-prove some theorem of his constructively

#### [Kevin Buzzard (Apr 10 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875985):
because Voevodsky wanted to prove an old theorem of Voevodsky constructively in this univalent foundations way

#### [Kevin Buzzard (Apr 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875994):
but my impression was that Suslin had no interest in the question (perhaps unsurprisingly, as I know essentially 0 mathematicians who care about constructive maths)

#### [Kenny Lau (Apr 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875995):
1

#### [Kevin Buzzard (Apr 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875996):
and it seemed that Voevodsky was losing interest in the whole project of checking the proof anyway (or perhaps he was stuck)

#### [Kenny Lau (Apr 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875997):
Alessio Corto

#### [Kevin Buzzard (Apr 10 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124875998):
Alessio Corti

#### [Kenny Lau (Apr 10 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876037):
sure

#### [Patrick Massot (Apr 10 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876039):
To me it settles the question: HoTT is constructive ⇒ I don't care

#### [Kevin Buzzard (Apr 10 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876042):
I think Voevodsky is something else

#### [Kevin Buzzard (Apr 10 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876045):
I think HoTT might be a third thing

#### [Kevin Buzzard (Apr 10 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876046):
I'm not sure though

#### [Kevin Buzzard (Apr 10 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876049):
Is Univalent Foundations = HoTT? I'm not so sure

#### [Patrick Massot (Apr 10 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876060):
More precisely: it's constructive ⇒ I think it's irrelevant to most mathematics

#### [Kevin Buzzard (Apr 10 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876062):
I completely agree.

#### [Kevin Buzzard (Apr 10 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876064):
So here are some questions.

#### [Kevin Buzzard (Apr 10 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876103):
We know that Lean will allow classical logic, and to be quite frank if it didn't allow it then I definitely would not be here.

#### [Kevin Buzzard (Apr 10 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876104):
I should say Lean 3, because at some point one has to talk about what Lean 2 was

#### [Kevin Buzzard (Apr 10 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876106):
Univalent Foundations seems to have been implemented in Coq, but there are lots of rules about commands in Coq which you are _not allowed to use_ in Univalent Foundations

#### [Kevin Buzzard (Apr 10 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876112):
e.g. you are not allowed to make new inductive types

#### [Kevin Buzzard (Apr 10 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876116):
you have to stick to the ones they made in the core files

#### [Kevin Buzzard (Apr 10 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876118):
But I should get to the point.

#### [Kevin Buzzard (Apr 10 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876119):
If I am interested in mathematics, done in classical logic

#### [Kevin Buzzard (Apr 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876159):
then what are my options for doing this in type theory?

#### [Kevin Buzzard (Apr 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876163):
DTT I know, because Lean 3

#### [Kevin Buzzard (Apr 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876164):
HoTT?

#### [Kevin Buzzard (Apr 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876165):
Univalent Foundations?

#### [Kenny Lau (Apr 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876167):
Voevodsky is high

#### [Kevin Buzzard (Apr 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876169):
And if there is more than one option, why should I choose Lean 3?

#### [Kenny Lau (Apr 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876170):
that settles it

#### [Kevin Buzzard (Apr 10 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876171):
Voevodsky is dead :-(

#### [Kenny Lau (Apr 10 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876177):
oh rip

#### [Andrew Ashworth (Apr 10 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876186):
there are very few popular dtt languages; you've already listed two, coq and lean, and there is also agda and idris

#### [Andrew Ashworth (Apr 10 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876227):
i think ats might also be based on dtt

#### [Andrew Ashworth (Apr 10 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876229):
basically the only other contender is not based on dtt at all, which is isabelle

#### [Kenny Lau (Apr 10 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876230):
how is she doing

#### [Moses Schönfinkel (Apr 10 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876287):
It is worth noting that both Agda and Idris are primarily programming languages. Unlike Lean and Coq.

#### [Andrew Ashworth (Apr 10 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876298):
isabelle is quite popular amongst mathematicians

#### [Kenny Lau (Apr 10 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876300):
because it ain't constructive?

#### [Moses Schönfinkel (Apr 10 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876302):
because they press Sledgehammer butan'

#### [Kevin Buzzard (Apr 10 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876303):
What are Isabelle's foundations?

#### [Moses Schönfinkel (Apr 10 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876308):
Isabelle is a metalanguage, you can instantiate it with whatever you feel like. Isabelle/HOL is the most popular.

#### [Andrew Ashworth (Apr 10 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876351):
i know little of isabelle. but my impression is most people work in set theory

#### [Kevin Buzzard (Apr 10 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876352):
This is what Hales used for Kepler, right?

#### [Kenny Lau (Apr 10 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876358):
one should make a proof-assistant based on ZFC

#### [Moses Schönfinkel (Apr 10 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876360):
As in ZF(C)? Mmm, I've always thought it's mostly just HOL.

#### [Andrew Ashworth (Apr 10 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876361):
that's already been done 30 years ago

#### [Kenny Lau (Apr 10 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876366):
who?

#### [Kevin Buzzard (Apr 10 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876369):
Apparently proof assistants based on ZFC are hard to use

#### [Kevin Buzzard (Apr 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876405):
I think Mario told me this

#### [Andrew Ashworth (Apr 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876407):
the original big one was called mizar

#### [Kenny Lau (Apr 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876410):
```quote
Apparently proof assistants based on ZFC are hard to use
```
another reason why ZFC is BS

#### [Moses Schönfinkel (Apr 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876411):
I believe Isabelle/ZFC is also a thing.

#### [Andrew Ashworth (Apr 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876412):
i recall sebastian gouzel was also slightly annoyed with isabelle

#### [Andrew Ashworth (Apr 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876414):
something about it being impossible to define the adeles

#### [Andrew Ashworth (Apr 10 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876416):
(whatever they may be)(

#### [Kevin Buzzard (Apr 10 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876419):
What do you mean by impossible?

#### [Kevin Buzzard (Apr 10 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876425):
Kenny is supposed to be defining the adeles in Lean

#### [Kevin Buzzard (Apr 10 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876426):
once he's finished revising his mechanics

#### [Andrew Ashworth (Apr 10 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876427):
discussion of the adeles is beyond my pay grade

#### [Sean Leather (Apr 10 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876430):
@**Andrew Ashworth**:
```quote
i think ats might also be based on dtt
```
[Not quite](https://groups.google.com/d/msg/ats-lang-users/k-6NMsZYllo/mePvbC3tCwAJ)

#### [Kevin Buzzard (Apr 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876477):
There is certainly no obstruction to defining the adeles in Lean

#### [Moses Schönfinkel (Apr 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876478):
There is once you don't have dependent types (a'la Isabelle).

#### [Andrew Ashworth (Apr 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876479):
yes, iirc he said that was a major draw for him to work in dtt

#### [Kenny Lau (Apr 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876482):
```quote
discussion of the adeles is beyond my pay grade
```
it isn't quite hard to understand if you start simple, i.e. start with Q

#### [Patrick Massot (Apr 10 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876483):
https://gitter.im/leanprover_public/Lobby?at=5a2daedfffa3e379191e9195

#### [Kevin Buzzard (Apr 10 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876484):
Kenny, the adeles of a general number field K are just (adeles of Q) tensor_Q K

#### [Kevin Buzzard (Apr 10 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876491):
and because you did tensor product

#### [Kevin Buzzard (Apr 10 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876493):
you can do adeles for a general number field

#### [Kenny Lau (Apr 10 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876496):
wonderful

#### [Kevin Buzzard (Apr 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876537):
The adeles are an easy exercise given what we have

#### [Andrew Ashworth (Apr 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876538):
isabelle and coq currently have ::quite:: an advantage in library size

#### [Kenny Lau (Apr 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876539):
***quite***

#### [Andrew Ashworth (Apr 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876540):
leaving aside isabelle, why would you use lean over coq? mostly for nicer unicode syntax

#### [Kevin Buzzard (Apr 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876541):
But we seem to have a proof that isabelle is not suitable for all of mathematics?

#### [Kevin Buzzard (Apr 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876543):
Lean > Coq -- because tactics

#### [Andrew Ashworth (Apr 10 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876552):
however if you wanted to jump straight into doing research mathematics, you can't in lean because mathlib is far smaller than its coq competitors

#### [Kenny Lau (Apr 10 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876556):
far smaller than it is coq competitors

#### [Kevin Buzzard (Apr 10 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876560):
and I think that nicer unicode syntax, whilst this might just be superficial for CS people, will I think be important to undergraduate mathematicians

#### [Moses Schönfinkel (Apr 10 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876563):
Coq > Lean because of existing tactics. Lean > Coq because of the way you write tactics.

#### [Kevin Buzzard (Apr 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876602):
But I am playing the long game

#### [Kevin Buzzard (Apr 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876604):
So I choose Lean. However this thread was basically my attempt to review this choice.

#### [Moses Schönfinkel (Apr 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876607):
If you're playing the very long game, it might still be the case Coq > Lean, Ltac2 is coming.

#### [Kevin Buzzard (Apr 10 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876611):
If I can understand the claim that "Isabelle can't do the adeles" then we can cross Isabelle off the list

#### [Kevin Buzzard (Apr 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876618):
But what about HoTT?

#### [Kevin Buzzard (Apr 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876622):
And what about UniMath?

#### [Andrew Ashworth (Apr 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876623):
hott is not ready for anything, it is a subject of research

#### [Kevin Buzzard (Apr 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876624):
And this does not apply to DTT

#### [Kevin Buzzard (Apr 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876625):
because Coq

#### [Kenny Lau (Apr 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876627):
let's do things over NBG

#### [Kenny Lau (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876667):
or just second order peano arithmetic

#### [Moses Schönfinkel (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876669):
The original univalence axiom is not constructive. There's cubical type theory extension thereof tho: https://arxiv.org/abs/1611.02108

#### [Andrew Ashworth (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876670):
dtt without any funny additions has been proven sound

#### [Kenny Lau (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876672):
sound!

#### [Kenny Lau (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876673):
sound in what?

#### [Andrew Ashworth (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876674):
as in you can do useful things with it and not summon false from anywhere

#### [Kenny Lau (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876675):
how do you even define sound

#### [Kevin Buzzard (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876676):
by "proven sound" you mean "relative to ZFC + existence of infinitely many inaccessible cardinals" right?

#### [Moses Schönfinkel (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876679):
@**Kenny Lau** Funny you should say that. My table currently contains "Subsystems of second order arithmetic".

#### [Kevin Buzzard (Apr 10 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876680):
You can't prove that anything is sound, in some sense

#### [Kenny Lau (Apr 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876688):
exactly

#### [Kevin Buzzard (Apr 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876693):
without assuming consistency of some less-likely-to-be-sound system

#### [Kenny Lau (Apr 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876742):
forget about the reals

#### [Kenny Lau (Apr 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876744):
just do peano arithmetic

#### [Kenny Lau (Apr 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876746):
and then embed ZFC within

#### [Moses Schönfinkel (Apr 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876747):
and then Goedel encode everything.

#### [Kenny Lau (Apr 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876748):
and then you can do the reals

#### [Andrew Ashworth (Apr 10 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876761):
i think for undergraduates who are not trying to do research mathematics, lean is nicer for reading and writing tactics (though i doubt they will get around to writing tactics)

#### [Moses Schönfinkel (Apr 10 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876769):
Actually, Coq has much nicer tactic-description syntax still.

#### [Andrew Ashworth (Apr 10 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876772):
coq is the winner if you're trying to make something that will be around for years

#### [Andrew Ashworth (Apr 10 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876814):
it has been around for decades

#### [Kenny Lau (Apr 10 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876823):
feit thompson e.g.

#### [Moses Schönfinkel (Apr 10 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876825):
You can pattern match on goals themselves for example. There's no obscure monad with arbitrary `pexpr` transforming functions.

#### [Andrew Ashworth (Apr 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876835):
i think writing tactics is beyond most mathematician's interest

#### [Andrew Ashworth (Apr 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876837):
realistically speaking

#### [Moses Schönfinkel (Apr 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876842):
Realistically speaking, using Lean is beyond most mathematician's interest :P.

#### [Andrew Ashworth (Apr 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876845):
also true

#### [Moses Schönfinkel (Apr 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876848):
i think this has a sadder part though

#### [Moses Schönfinkel (Apr 10 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876851):
using Lean is beyond most CS peoeple interest as well

#### [Andrew Ashworth (Apr 10 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876901):
well, most cs majors would rather have a tooth pulled than work with something that reminds them of their undergraduate discrete math course

#### [Moses Schönfinkel (Apr 10 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876956):
most people studying CS want to be "programmers", there's no clear distinction between CS and software engineering in academia, for worse or worse

#### [Kevin Buzzard (Apr 10 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876958):
I agree about tactics. For now.

#### [Kevin Buzzard (Apr 10 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876961):
But I am going to make mathematicians interested in Lean.

#### [Andrew Ashworth (Apr 10 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876964):
if you split the two cleanly then academic CS may as well be in the math department along with the statisticians

#### [Andrew Ashworth (Apr 10 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876970):
and logicians

#### [Patrick Massot (Apr 10 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124876974):
```quote
But I am going to make mathematicians interested in Lean.
```
Then we need more documentation, for instance your old project of describing mathlib

#### [Kevin Buzzard (Apr 10 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877016):
oh yeah sorry Patrick I didn't respond to your earlier question

#### [Kevin Buzzard (Apr 10 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877019):
I am still trying to figure out all the finite stuff

#### [Kevin Buzzard (Apr 10 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877022):
but multiset.lean is so long

#### [Kevin Buzzard (Apr 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877033):
My blog post about induction was just some consequence of me trying to understand finite stuff

#### [Kevin Buzzard (Apr 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877035):
For mathematicians, finite sets are so important and foundational

#### [Kevin Buzzard (Apr 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877036):
and I found them very hard to do in DTT

#### [Kevin Buzzard (Apr 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877038):
but I am slowly getting on top of them

#### [Moses Schönfinkel (Apr 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877039):
@**Andrew Ashworth** well we then need to communicate better what to expect in a CS course at least... it is as you said, tooth extraction wins over discrete math for many students I teach...

#### [Kevin Buzzard (Apr 10 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877078):
My middle child is a budding CS student and he was moaning about discrete maths only 2 days ago

#### [Andrew Ashworth (Apr 10 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877082):
surely he knows better than to moan about maths to you, haha

#### [Kevin Buzzard (Apr 10 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877084):
:-)

#### [Patrick Massot (Apr 10 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877085):
I know I'm always writing the same thing, but did you read that Coq bigoperator paper?

#### [Kevin Buzzard (Apr 10 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877091):
I was reading it yesterday

#### [Kevin Buzzard (Apr 10 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877093):
I learnt some stuff

#### [Kevin Buzzard (Apr 10 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877095):
For example I didn't really know how to prove that sum from 0 to n of f(i) equalled sum from 0 to n of f(n-i)

#### [Kevin Buzzard (Apr 10 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877099):
but I can now see a nice way of doing it using bigoperators

#### [Sean Leather (Apr 10 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877102):
Discrete math was one of my favorite undergrad courses.

#### [Moses Schönfinkel (Apr 10 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877154):
I teach Java to students that had compulsory discrete math one semester prior. They think I'm evil when I want them to, and I quote, "remember what properties equivalence relations have"... :-\

#### [Kevin Buzzard (Apr 10 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877208):
In summary then, apparently HoTT isn't ready, UniMath I am still unsure about, Isabelle has problems with adeles, Mizar didn't catch on for some reason, so there's only DTT left?

#### [Kevin Buzzard (Apr 10 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877248):
And if it turns out that Coq > Lean then I just switch to Coq

#### [Andrew Ashworth (Apr 10 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877250):
that is a bonus. if lean ever dies everything you've learnt moves easily over to coq

#### [Kevin Buzzard (Apr 10 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877260):
Can I write a regular expression which turns all my Lean proofs into Coq proofs?

#### [Andrew Ashworth (Apr 10 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877265):
that's a little ambitious :)

#### [Kevin Buzzard (Apr 10 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877266):
Oh Ok

#### [Kevin Buzzard (Apr 10 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877267):
I don't know what you CS guys can do

#### [Moses Schönfinkel (Apr 10 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877310):
I don't think it's a completely ridiculous idea.

#### [Andrew Ashworth (Apr 10 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877318):
i mean, it's theoretically possible to write a transpiler. but who would do the work?

#### [Patrick Massot (Apr 10 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877329):
Lean advantages over Coq are not only about unicode. You also get better overall ergonomics. And, most of all, less constructive stuff.

#### [Patrick Massot (Apr 10 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877335):
And *much* better documentation

#### [Moses Schönfinkel (Apr 10 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877336):
How is less constructive stuff a good thing?!

#### [Patrick Massot (Apr 10 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877340):
It's a good thing for mathematics, not for everything

#### [Andrew Ashworth (Apr 10 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877341):
well.. lean, instead of having less constructive stuff, just has _less_ stuff :)

#### [Patrick Massot (Apr 10 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877382):
From what I understand, in Coq you need to spend more energy fighting constructivism

#### [Kevin Buzzard (Apr 10 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877385):
In Dan Grayson's article he argues that constructive maths is better than normal maths because constructive maths is a generalisation of normal maths

#### [Kevin Buzzard (Apr 10 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877386):
I was like "..."

#### [Kevin Buzzard (Apr 10 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877390):
I should tell all the group theorists I know to move into monoid theory

#### [Patrick Massot (Apr 10 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877393):
Exactly what I was about to write

#### [Patrick Massot (Apr 10 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877395):
let's all do monoids!

#### [Kevin Buzzard (Apr 10 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877396):
actually let's just do set theory

#### [Kevin Buzzard (Apr 10 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877398):
who cares about structure

#### [Kevin Buzzard (Apr 10 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877399):
we have the classification theorem already

#### [Kevin Buzzard (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877446):
each one bijects with a unique cardinal

#### [Kevin Buzzard (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877447):
so off we go

#### [Moses Schönfinkel (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877448):
this is surprisingly reminiscent of static vs dynamic typing discussion

#### [Andrew Ashworth (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877449):
also, unimath is basically hott

#### [Andrew Ashworth (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877450):
unimath is dtt + univalence

#### [Kevin Buzzard (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877451):
What is this documentation comment Patrick?

#### [Andrew Ashworth (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877452):
and then a bunch of mathematics

#### [Kevin Buzzard (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877454):
I thought Coq had some big chunky tomes

#### [Andrew Ashworth (Apr 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877455):
like, actual math, like i recall seeing a construction of the reals using dedekind cuts

#### [Andrew Ashworth (Apr 10 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877463):
so unimath is basically mathlib + univalence

#### [Kevin Buzzard (Apr 10 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877464):
equality is not a prop in unimath

#### [Kevin Buzzard (Apr 10 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877465):
apparently

#### [Kevin Buzzard (Apr 10 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877466):
equality in unimath seems more like \equiv in Lean

#### [Andrew Ashworth (Apr 10 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877508):
if i knew more homotopy theory i'd feel more eager to say things about hott :)

#### [Patrick Massot (Apr 10 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877561):
```quote
What is this documentation comment Patrick?
```
Coq has *no* documentation targeting mathematicians. TPIL is written for us, and beats anything I've seen about Coq by a very wide margin.

#### [Andrew Ashworth (Apr 10 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124877956):
yes, the big three textbooks for coq are: [software foundations](https://softwarefoundations.cis.upenn.edu), [certified programming with dependent types](http://adam.chlipala.net/cpdt/), and [coq'art](https://www.labri.fr/perso/casteran/CoqArt/coqartF.pdf). ssreflect also has a good manual [here](https://math-comp.github.io/mcb/book.pdf). notice all but the last is focused towards programmers...

#### [Patrick Massot (Apr 10 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124878169):
SSReflect manual is clearly going in the right direction compared to the other three, but it's still much harder to read that TPIL (I tried reading it before switching to Lean).

#### [Kevin Buzzard (Apr 10 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124879260):
I thought that Coq also had some useful introductory tutorials. But I agree with Patrick that TPIL is a very good read for mathematicians.

#### [Kevin Buzzard (Apr 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124879285):
Patrick -- I was going to write something else for mathematicians, where I enter tactic mode on page 1 and basically never leave, and also on page 1 I do mathematics rather than goofing around with logic, doing basic mathematical proofs of familiar statements like stuff involving congruences right from square 1. I show them the tactics they need and we go from there.

#### [Kevin Buzzard (Apr 10 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124879333):
I still think that term mode is too hard for mathematicians. You clearly have a programming background. I am guessing that you were happy with lambda notation for functions before you started reading these docs.

#### [Kevin Buzzard (Apr 10 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124879336):
I would like to suppress lambda notation for as long as possible.

#### [Patrick Massot (Apr 10 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124879345):
I agree wholeheartedly with all those goals

#### [Kevin Buzzard (Apr 10 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124879460):
OK! Thanks for your opinion, I genuinely value it.

#### [Kevin Buzzard (Apr 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124879481):
We are both in the same sort of boat, trying to read books written for computer scientists with in some sense an "amateur" background (with me rather more amateurish than you when it comes to computing) but I really want to appeal to people who know no CS at all.

#### [Kevin Buzzard (Apr 10 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124879699):
Back to the point -- does anyone here know if one can do classical mathematics in UniMath?

#### [Andrew Ashworth (Apr 10 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124879899):
I think so. https://github.com/HoTT/HoTT/issues/299

#### [Andrew Ashworth (Apr 10 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124880270):
speaking of, i linked this a long time ago, but here you can see a comparison of the most popular proof languages

#### [Andrew Ashworth (Apr 10 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124880271):
http://www.cs.ru.nl/~freek/100/

#### [Simon Hudon (Apr 10 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124891320):
```quote
yes, the big three textbooks for coq are: [software foundations](https://softwarefoundations.cis.upenn.edu), [certified programming with dependent types](http://adam.chlipala.net/cpdt/), and [coq'art](https://www.labri.fr/perso/casteran/CoqArt/coqartF.pdf). ssreflect also has a good manual [here](https://math-comp.github.io/mcb/book.pdf). notice all but the last is focused towards programmers...
```

I think that suggests @**Patrick Massot** has the right idea: if you want documentation for mathematicians, we need actual mathematicians to do it.

#### [Patrick Massot (Apr 10 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124891477):
I don't if you count Avigad as mathematician but TPIL comes very close to what we want. You only to unemphasize term mode and put more math examples.

#### [Simon Hudon (Apr 10 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124891705):
Right. What I meant is that building a theorem prover is something done by programmers so it kind of colors what they'll use the prover for in the documentation.

#### [Simon Hudon (Apr 10 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124891869):
That's the curious difference between a prover and an accounting software. In accounting software, you do it for / with accountants / people who want to do accounting. With a prover, I have a feeling you start one when you need a prover that does stuff that the other provers don't do. You're kind of the first user of the prover so you assume the other users will want the prover for the same reason. Not that I built a prover with more than 1.5 users but ...

#### [Andrew Ashworth (Apr 10 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892093):
```quote
I don't if you count Avigad as mathematician but TPIL comes very close to what we want. You only to unemphasize term mode and put more math examples.
```
term mode is not the enemy! i feel like if one wants to get anything done, you'll end up needing to know both modes 
personally my favorite code style for math is the isabelle style, as seen https://github.com/sgouezel/mathlib/blob/d4836822a625677b9f292e26fcafb4870bbf9f91/order/conditionally_complete_lattice.lean

#### [Kevin Buzzard (Apr 10 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892290):
Term mode is not the enemy. But for a mathematician there are many things which you have to learn in order to work this sort of language, and term mode is somehow one of the more obscure things. Let's give them time to wrestle with how to steer this thing whilst they're proving that the square root of 2 is irrational, or whatever, in tactic mode, before telling them that lambda is no longer supposed to mean a real number.

#### [Andrew Ashworth (Apr 10 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892502):
if logic and proof (jeremy's other textbook) was fully worked out in lean 3, is that something you'd be looking for?

#### [Kevin Buzzard (Apr 10 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892633):
That's less Lean and less tactic mode!

#### [Patrick Massot (Apr 10 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892634):
I didn't write "completely remove term mode" but "unemphasize" (I don't know if this word exists but I hope what I mean is clear)

#### [Andrew Ashworth (Apr 10 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892687):
ah, true. only 50% of logic and proof is lean

#### [Kevin Buzzard (Apr 10 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892690):
I know exactly what I want, and I'm going to write it myself using Jeremy's cool org mode solution for generating books

#### [Patrick Massot (Apr 10 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892694):
I'd be happy to help in any way

#### [Andrew Ashworth (Apr 10 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892704):
very awesome, i think everyone here would love to peek at it as you write it

#### [Andrew Ashworth (Apr 10 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892705):
at least i would, i read all your blog posts, hah

#### [Simon Hudon (Apr 10 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892755):
@**Kevin Buzzard** I think he moved from org-mode to Restructured Text, didn't he?

#### [Kevin Buzzard (Apr 10 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892773):
In some sense the main question I have for Patrick is how to write a book which has maths like $$R[1/f]$$ and `lean stuff like this` all coloured in correctly.

#### [Kevin Buzzard (Apr 10 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892777):
Simon I was basing my org claim on this

#### [Kevin Buzzard (Apr 10 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892778):
https://github.com/leanprover/mkleanbook

#### [Kevin Buzzard (Apr 10 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892816):
and the fact that the files were called `blah.org`

#### [Patrick Massot (Apr 10 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892832):
This is not how TPIL is currently produced

#### [Kevin Buzzard (Apr 10 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892838):
You must be right

#### [Kevin Buzzard (Apr 10 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892840):
do you know how it's currently done?

#### [Patrick Massot (Apr 10 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892848):
Sphinx

#### [Patrick Massot (Apr 10 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892854):
https://github.com/leanprover/theorem_proving_in_lean

#### [Patrick Massot (Apr 10 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892861):
scroll down to README

#### [Andrew Ashworth (Apr 10 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892862):
that said, there is nothing wrong with mkleanbook, the issue was other people didn't want to use emacs

#### [Kevin Buzzard (Apr 10 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892869):
what about getting things $$in maths mode$$?

#### [Kevin Buzzard (Apr 10 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124892913):
(although perhaps not regular sentences, they can stay in non maths mode)

#### [Simon Hudon (Apr 10 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124894266):
Do you mean that you would format Lean code in math mode? I'd really like to see that

#### [Kevin Buzzard (Apr 10 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124895411):
I mean I want to write maths and Lean code (at different times)

#### [Kevin Buzzard (Apr 10 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124895465):
Ideally the maths I write would look as good as LaTeX and the Lean would be coloured in correctly

#### [Simon Hudon (Apr 10 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124895486):
Ah ok! I think the setup they have for Lean documents should allow that

#### [Simon Hudon (Apr 10 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124895597):
I'm soon going to give Pandoc a try. I heard good things about it and it looks easier to set up than Sphinx

#### [Simon Hudon (Apr 10 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124895678):
Ideally, I'd like to get to a point where I don't have to switch between writing and checking Lean and writing and checking documentation.

#### [Mario Carneiro (Apr 10 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124900412):
> One major weakness (possibly only temporary) is that the model you're supposed to carry around is that a type can be thought of as a topological space
> but apparently they can't construct the n-sphere from the axioms
> so they add n-spheres as new inductive types
> and then they can't prove the theory is consistent
> This does not bode well, as far as I can see.

As far as I am aware, HoTT + all the HITs people care about, including S^n and quotients and things, is known consistent because of the existence of simplicial set models and such. The unknown consistency claim here may be particular to Univalent Foundations, I'm not sure.

#### [Mario Carneiro (Apr 10 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124900578):
> Is Univalent Foundations = HoTT? I'm not so sure

I think Univalent Foundations = HoTT + Propositional resizing, which means that everything you can prove is a proposition lives in the lowest universe. This is similar to Lean's `Prop` universe, but in Lean you can't prove that something lives in `Prop`, it either is or isn't by virtue of the form of the expression. Regular HoTT does not have this resizing rule, so there are "more propositions" in higher universes, which talk about correspondingly large objects.

#### [Mario Carneiro (Apr 10 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124900659):
> If I am interested in mathematics, done in classical logic
> then what are my options for doing this in type theory?

I think this is the wrong question. You can do mathematics in just about any system above a certain minimum threshold of complexity, which is somewhere around second order PA. It just gets less convenient as you remove features

#### [Mario Carneiro (Apr 10 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124900935):
> I believe Isabelle/ZFC is also a thing.

Pretty much all Isabelle work is done in Isabelle/HOL. Metamath is similar in that it is a general framework which allows you to define DTT, HOL, ZFC, PA or anything else, but 99% of the actual theorem proving work has gone into the ZFC database.

> Apparently proof assistants based on ZFC are hard to use
> I think Mario told me this

I'm not 100% clear on this, because I hear conflicting messages, but this is the usual line:
* ZFC based stuff is hard to use in proof automation because there isn't much information on what is what, which helps in relevance filtering and eliminating proof steps that are not well typed
* Type theory based stuff is hard for proof automation because keeping track of all the types is hard, and all the major tools are built in FOL with one big FOL universe, i.e. ZFC (or smaller FOL systems like first order equational theories, PA, etc.)

#### [Mario Carneiro (Apr 10 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124901093):
> If you're playing the very long game, it might still be the case Coq > Lean, Ltac2 is coming.

If you are playing a sufficiently long game, the best bet doesn't exist yet

> dtt without any funny additions has been proven sound

DTT with inductive types, quotients and proof irrelevance is also sound, courtesy of yours truly

#### [Mario Carneiro (Apr 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124901174):
> I am still trying to figure out all the finite stuff
> but multiset.lean is so long

You don't need to read multiset.lean that carefully. The easy version is: it's lists up to permutation, with all the list functions lifted to multiset. All the lemmas are exactly what you would expect, given the definitions.

#### [Mario Carneiro (Apr 10 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124901284):
> i mean, it's theoretically possible to write a transpiler. but who would do the work?

I would, if I understood Coq's metatheory as well as I do Lean's. Since they were not nearly so careful with their kernel as Lean has been, I don't know if I will find the acceptable Gallina terms written up anywhere that isn't an approximation or out of date

#### [Mario Carneiro (Apr 10 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124901543):
> equality in unimath seems more like \equiv in Lean

This is exactly the right idea. However, there is something you really need to pay attention to which I think you have missed and are using to get a "free lunch" in your conception of HoTT: equality (the type constructor) is *not* the same as definitional equality. In Lean this isn't that big a deal because of proof irrelevance, but you absolutely cannot hold the view that one thing is as good as an equal thing when doing HoTT. In particular, it will not save you from your "up to equivalence" problems in the other thread, but I will discuss this more there.

#### [Mario Carneiro (Apr 10 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124902506):
> I still think that term mode is too hard for mathematicians. You clearly have a programming background. I am guessing that you were happy with lambda notation for functions before you started reading these docs.
> I would like to suppress lambda notation for as long as possible.

I don't think this is a good idea. The idea of a lambda itself, a function giving a result, is quite integral to mathematics and it's a surprise they haven't picked up the notation already (or something isomorphic, like `x \in A |-> b(x)`).

If you want to write a tactic-centric lean tutorial, I would suggest to begin with a brief overview of the terms of the language, i.e. lambda, application, constants and variables, make sure they understand what a bound variable is, then move on with some statement along the lines "writing these terms directly is cumbersome, so here's a language for quickly constructing terms that is designed more for ease of use". You don't need to mention the Isar-inspired terms like `match` and `have` and `show` until later if you want, but the core type theory should be at least briefly described.

#### [Scott Morrison (Apr 11 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/foundations of mathematics/near/124907734):
It is a good point that mathematicians know perfectly well about lambdas, they just write them $x \mapsto f(x)$.

