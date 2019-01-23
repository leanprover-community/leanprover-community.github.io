---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/50492Leantalkformathematicians.html
---

## Stream: [general](index.html)
### Topic: [Lean talk for mathematicians](50492Leantalkformathematicians.html)

---

#### [Johan Commelin (Sep 03 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133249947):
I've been asked to talk about Lean in our colloquium. Still freaking out... what should I put in such a talk? How do I manage expectations, so that they become realistic (instead of "Blah, unusable crap" or "They'll use AI to prove millenium problems. They're stealing our jobs.")

#### [Johan Commelin (Sep 03 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133249950):
Over lunch I only ever hear these extremes.

#### [Johan Commelin (Sep 03 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133249953):
Any tips or tricks are very welcome.

#### [Patrick Massot (Sep 03 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250093):
When will you give this talk?

#### [Patrick Massot (Sep 03 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250096):
I will also probably try that

#### [Patrick Massot (Sep 03 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250099):
I hope the perfectoid project will be completed before

#### [Johan Commelin (Sep 03 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250141):
I can still choose the date, but it could be as early as mid-October.

#### [Johan Commelin (Sep 03 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250159):
This is another reason why we should have easy installers and/or code browsers...

#### [Johan Commelin (Sep 03 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250175):
In some sense freshmen students will have a lot more patience and persistence then tenured staff. If it doesn't work out of the box, we've lost them for a couple of years again.

#### [Johan Commelin (Sep 03 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250221):
Still, the fact that I was asked to give a talk shows that there is some interest among them. And I want to capitalize on that.

#### [Patrick Massot (Sep 03 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250390):
If you want to attract mathematicians, I think the best you can do is to work on perfectoid spaces. Look at how we hooked people. If I understand correctly,  Bryan,  Soham and you came here because you heard about either schemes or perfectoid spaces in Lean. It would be interesting to compare with what happened in Coq. @**Assia Mahboubi** how many mathematicians or advanced maths students showed up in Coq forums or mailing lists when the odd order theorem proof was announced?

#### [Patrick Massot (Sep 03 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250408):
If we manage to complete the definition, you'll be able to show nice dependency graphs displaying how much maths goes into this definition.

#### [Johan Commelin (Sep 03 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250623):
Right! We want dependency graphs and such! We want boatloads of visualisation tools.

#### [Johan Commelin (Sep 03 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250628):
Scott had really cool visualisations! We need more of those (-;

#### [Patrick Massot (Sep 03 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250630):
Recall we already have that

#### [Johan Commelin (Sep 03 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250635):
Yes... but not enough

#### [Johan Commelin (Sep 03 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250676):
The code browser is also a form of visualisation (in my eyes)

#### [Patrick Massot (Sep 03 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250687):
during your talk you can use VScode

#### [Johan Commelin (Sep 03 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250699):
Sure, I was planning to do that.

#### [Kevin Buzzard (Sep 03 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250931):
I wanted to concentrate on preparing my course in September but lots of things are happening. I just need to work harder. I don't think mid-October is an unreasonable target for perfectoid spaces. Sometimes when I look at the definition I think "this is easy, there's nothing left apart from a bunch of standard stuff which should be easy", and at other times I remember that I watched Mario take three hours to prove the math-trivial fact that the two standard definitions of Noetherian module are equivalent and then the realisation hits me. Another concern I have is that people are appearing out of the woodwork, either here or in my inbox, saying "can I help?" and currently I just seem to be saying "Sure! Just join in!". I meant to spend some time yesterday getting on top of the perfectoid project (like I did with the scheme project in Paris -- getting it to compile again!) but all I managed to do was remove some of the errors we get when compiling.

#### [Kevin Buzzard (Sep 03 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250976):
Most of my summer students have finished now though, so I will hopefully be far more active in Sept in the project than I have been in July and Aug (I've spent a *lot* of time talking to undergraduates about UG level maths in Lean recently).

#### [Patrick Massot (Sep 03 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250979):
Right now I'm working on getting the project to compile

#### [Patrick Massot (Sep 03 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250983):
But it's lunch time

#### [Patrick Massot (Sep 03 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133250997):
Can you give me two hours, and then I'll hopefully PR some progress?

#### [Johan Commelin (Sep 03 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133251074):
Kevin, I think pointing people to Zulip is a very good idea.

#### [Johan Commelin (Sep 03 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133251110):
We'll usually be able to get people started.

#### [Johan Commelin (Sep 03 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133251129):
Also, like I said, I haven't fixed a date for my talk yet. So it could also be 3 weeks later.

#### [Kevin Buzzard (Sep 03 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133251442):
It's nice to have deadlines though.

#### [Kevin Buzzard (Sep 03 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133251451):
If there's flexibility, why not ask for November? :-)

#### [Johan Commelin (Sep 03 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133251462):
Because I don't have as many deadlines as you (-;

#### [Johan Commelin (Sep 03 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133251468):
I don't want to pressure you. But I'dd certainly wait till November if that means that the perfectoid project will likely be ready.

#### [Kevin Buzzard (Sep 03 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133251643):
I am being funded to run a Lean course which starts on Oct 1st, with 250 students, and out of the 100 formalised maths questions and solutions which I need to prepare to run this course, I have so far finished 1. On the other hand my kids go back to school on Wednesday and life gets a bit saner after that. I think what I currently need is a clearer view of the route to the finish line. Occasionally I look at the point in Wedhorn's paper that we're up to, and it's the line "let V_pre denote the category of topological spaces endowed with a presheaf of topological rings having some properties" and I always think "I wonder if Scott's library can help me here?". @**Scott Morrison** I can easily make this category "by hand" -- if I want perfectoid spaces done by mid-Oct should I do so?

#### [Kevin Buzzard (Sep 03 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133251707):
https://www2.math.uni-paderborn.de/fileadmin/Mathematik/People/wedhorn/Lehre/AdicSpaces.pdf bottom of p76

#### [Kevin Buzzard (Sep 03 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133251779):
```quote
Right now I'm working on getting the project to compile
```
Compile modulo sorries, of course.

#### [Johan Commelin (Sep 03 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133251952):
Scott is working on sheaves with values in arbitrary types. So I think we can soon have a reasonable clean definition of this category. @**Scott Morrison** I don't want to put words in your mouth. Did I say that right?

#### [Kevin Buzzard (Sep 03 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133252032):
Right, but the question is whether in practice "soon" means "by January" or "by next week".

#### [Kevin Buzzard (Sep 03 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133252081):
I keep looking at the definition and thinking "he's taking a directed limit to construct the stalk -- I did all that by hand in the schemes repo, I wonder whether I should just sit and wait this time". But actually I guess all I need is a direct limit of rings anyway *shrug* -- the topology plays no role.

#### [Scott Morrison (Sep 03 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133252370):
@**Kevin Buzzard**, I think I can have "the category of sheaves of rings on a topological space" in pretty short order.

#### [Scott Morrison (Sep 03 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133252387):
In order to be able to talk about the stalk, we'd need to add least get the definition of tensor product of commutative rings into mathlib.

#### [Scott Morrison (Sep 03 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133252390):
This should be easy now that Kenny has pushed tensor products of modules?

#### [Kevin Buzzard (Sep 03 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133252432):
To get the stalk of the structure sheaf we only need direct limits I guess

#### [Scott Morrison (Sep 03 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133252434):
In order to be able to *usefully* talk about stalks, we'd need to have filtered colimits of rings.

#### [Scott Morrison (Sep 03 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133252446):
(The difference between direct and filtered is pretty small, I think; filtered should be barely harder.)

#### [Scott Morrison (Sep 03 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133252455):
This is definitely doable, in the sense that I started writing it, and didn't see any obvious obstructions besides me being slow.

#### [Johan Commelin (Sep 03 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133252511):
Please don't say that you are slow... I already reserved that word for my tempo...

#### [Scott Morrison (Sep 03 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133252540):
It would be nice to write direct/filtered colimits in a way that makes it easy to see how to generalise. Reid was talking about eventually writing some machinery (possibly having to involve some tactics, I'm not sure) that would construct limits and filtered colimits just from knowing properties of the forgetful functor.

#### [Scott Morrison (Sep 03 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133252541):
But I don't think we need to wait on that. :-)

#### [Scott Morrison (Sep 03 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133252587):
A general question: where do people think particular categories should go?

#### [Scott Morrison (Sep 03 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133252590):
i.e. should I make a `category_theory/examples/` folder, and put `Ring` and `Top` etc there?

#### [Scott Morrison (Sep 03 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133252595):
Or do that categories go all spread out through the repository, close to their natural homes?

#### [Scott Morrison (Sep 03 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133252624):
And if they go all spread out, should I just put them in as soon as they are definable, requiring `category_theory/` as a dependency, or just have one extra file per theory that imports `category_theory` and does the assembly work there, and people who need it can import that?

#### [Kenny Lau (Sep 03 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133252910):
while you're busy characterising direct limit... I'm building direct limit :P

#### [Soham Chowdhury (Sep 03 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133269173):
```quote
If you want to attract mathematicians, I think the best you can do is to work on perfectoid spaces. Look at how we hooked people. If I understand correctly,  Bryan,  Soham and you came here because you heard about either schemes or perfectoid spaces in Lean. 
```
This is true; I write a good amount of Haskell and so I've been aware of, e.g. work in Coq/Agda/Idris (and Liquid Haskell) on proving data-structures or algorithms correct, or space/time-complexity bounds, and so on, but was never motivated to jump into that sort of thing. 

Before I became aware of the work on formalising mathematics I know/am learning/care about, I had resigned myself to waiting until I understood enough homotopy theory to take a stab at HoTT.

#### [Soham Chowdhury (Sep 03 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/133269199):
btw, @**Patrick Massot** thanks for pointing me the right way, I worked through some of the tutorial today

#### [Patrick Massot (Sep 26 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134668740):
```quote
I've been asked to talk about Lean in our colloquium. Still freaking out... what should I put in such a talk? How do I manage expectations, so that they become realistic (instead of "Blah, unusable crap" or "They'll use AI to prove millenium problems. They're stealing our jobs.")
```
Johan, did you give that talk already? I also took up the challenge. Actually I was asked to give a colloquium about any topic, and I proposed the title "Can mathematicians use proof verification software?". Somewhat surprisingly, this was accepted. We now have a new deadline for the perfectoid project: October 18th...

#### [Kevin Buzzard (Sep 26 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134670182):
or October 17th if you count my colloquium in Sheffield in front of Neil Strickland...

#### [Scott Morrison (Sep 26 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134670528):
Haha, I'm on October 5, for a colloquium at Adelaide. :-)

#### [Patrick Massot (Sep 26 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134670740):
Nice, let's finish it before October 5th! My colloquim will (presumably) be in front of Sébastien and Assia. It sounds a bit ridiculous but the point is exactly to discuss how much is doable by a normal clueless mathematician

#### [Patrick Massot (Sep 26 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134670809):
Of course I'm cheating since I'm currently waiting for Johannes to unlock my completion stuff...

#### [Kevin Buzzard (Sep 26 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134670923):
...and Hilbert Basis is on hold too. Who knows if I will have time to look at this stuff before October. The annual pile of reference letter requests has begun to appear...

#### [Patrick Massot (Sep 26 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134670962):
Reference letters are easy to write those days: "Dr. XXX claims nice result, but I haven't seen a formalized proof, so who knows what he/she is talking about?"

#### [Johan Commelin (Sep 26 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134678425):
Ok, I don't have a date yet. But I think I will be last in row.

#### [Sebastien Gouezel (Sep 26 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134685715):
As a further data point in the question of usability of proof assistants in real-life (well, mathematical real-life), you can have a look at http://www.math.sciences.univ-nantes.fr/~gouezel/articles/morse_lemma.pdf (preliminary version).

Some time ago, I mentioned that I found a gap in a published paper while formalizing it in Isabelle. This gap is now corrected, and the new proof is completely formalized. The above paper explains the corrected proof, for mathematicians, but it also mentions the formalized proof. By the way, it raises interesting questions on the way to write a math papers when you have a formalized proof (when we need a lemma that is related, but not exactly the same, to results already in the literature, should we give the proof or just point the reader to the formalized proof?) We have tried to find some middle ground here, but I guess our way to write papers will have to change. Comments welcome!

#### [Patrick Massot (Sep 26 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134693460):
Amazing! Do you intend to submit this to a traditional math journal? I'd be very interested to see what happens.

#### [Sebastien Gouezel (Sep 26 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134694710):
Yes, probably as a corrigendum to the journal where the initial paper was published (Journal of Functional Analysis, an excellent journal but published by Elsevier, which is a bit of a problem for ethical reasons but traditionally a paper and a corrigendum are in the same journal. We will see)

#### [Patrick Massot (Sep 26 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134694868):
It seems pretty clear to me that "our way to write papers will have to change" when we have formalized proofs. Writing technical details in TeX is pointless of you have a formal proof. You should rather spend the energy on explaining what's going on

#### [Reid Barton (Sep 26 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134694893):
This is very cool!

#### [Reid Barton (Sep 26 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134694976):
Is there something like a "Journal of Formalized Mathematics", but not particular to any one theorem proving system?

#### [Mario Carneiro (Sep 26 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134695063):
CPP is something like that

#### [Patrick Massot (Sep 26 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134695180):
I'm impressed by the Isabelle snippets: it seems Isabelle allows the user to use lambda as a  constant real number

#### [Johannes Hölzl (Sep 26 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134695328):
huh where do you see this? I just see the names `lambda` and `delta`?

#### [Patrick Massot (Sep 26 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134695385):
```hausdorff_distance (f`{a..b}) G ≤ 92 * lambda^2 * (C + deltaG(TYPE('a)))```

#### [Sebastien Gouezel (Sep 26 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134695397):
lambda as a sequence of letters, yes. But probably not λ, this is reserved for function definitions.

#### [Patrick Massot (Sep 26 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134695414):
ah...

#### [Patrick Massot (Sep 26 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134695421):
I'll stick to Lean then

#### [Patrick Massot (Sep 26 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134695443):
Reading the introduction doesn't allow me to understand why optimizing the constant is worth the trouble

#### [Mario Carneiro (Sep 26 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134695493):
I think bold lambda gets used somewhere...

#### [Johannes Hölzl (Sep 26 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134695611):
@**Reid Barton**  w.r.t "Journal of Formalized Mathematics" there is also the Journal of Automated Reasoning (https://link.springer.com/journal/10817), the "Journal of Formalized Reasoning" https://jfr.unibo.it/, and the ITP the conference on interactive theorem proving.

#### [Patrick Massot (Sep 26 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134695643):
Sébastien, I think you should explain a bit more how to read Isabelle code. It's not easy to map the traditional statement to Isabelle statement

#### [Reid Barton (Sep 26 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134695820):
Is a $$(\lambda, C)$$-quasi-isometry the same as a $$(\lambda, C)$$-quasi-geodesic? Is a geodesic the same as a $$(1, 0)$$-quasi-geodesic?

#### [Sebastien Gouezel (Sep 26 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134696310):
a  (λ,C)-quasi-geodesic is a (λ,C)-quasi-isometry defined on an interval. A geodesic is a (1,0)-quasi-geodesic, yes. All these terms are supposed to be standard in the domain. As for the explanations of Isabelle code, since the math statement is given just before the Isabelle statement, I was hoping that the correspondance would be easy to make for people interested in the formalization, but maybe I am too optimistic. If you have a hard time reading the statement, I should definitely add some details (or maybe this is because you are too used to Lean syntax...)

#### [Patrick Massot (Sep 26 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134696680):
I guess it would be much easier if notation matched. Thinking about the main statement, I guess that `'a = X` and `f = Q` but I don't understand why the notation changes.

#### [Reid Barton (Sep 26 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134696787):
Oh I'm sure that they are standard--but the article is also nearly readable for someone like me who has almost no relevant knowledge beyond the definition of a metric space.

#### [Patrick Massot (Sep 26 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134696822):
I wonder if you should include more background for people who read this paper because of the formalization

#### [Askar Safin (Sep 26 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134696942):
hi. is lean based on pts?

#### [Mario Carneiro (Sep 26 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134698276):
@**Askar Safin** I don't think it fits into the definition of a PTS; it is dependently typed but most PTSs I have seen are simply typed

#### [Sebastien Gouezel (Sep 26 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134699158):
```quote
I guess it would be much easier if notation matched. Thinking about the main statement, I guess that `'a = X` and `f = Q` but I don't understand why the notation changes.
```
`'a` is the Isabelle name for a type (in the same way that, in Lean, your `X` would be called alpha). `Q` is the quasi-geodesic and `f` is its parametrization. Thanks for the comments, I will try to make it more self-contained.

#### [Patrick Massot (Sep 26 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134699438):
In Lean, you can actually call a group G if you insist enough. See Johannes recent commits in https://github.com/leanprover-community/mathlib/tree/completions He cleaned a lot of things, but didn't write alpha everywhere :smile:

#### [Chris Hughes (Sep 26 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134699653):
There's even a group called G in master, in `group_theory/quotient_group`

#### [Kenny Lau (Sep 26 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134700579):
we have reclaimed our land!

#### [Sebastien Gouezel (Sep 26 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134700614):
In Isabelle, as far as I know, it has to be `'a`.

#### [Patrick Massot (Sep 26 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134700632):
Sébastien, you should really switch to Lean now that this project is done

#### [Patrick Massot (Sep 26 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134700686):
And then your metric spaces will be `X` again

#### [Sebastien Gouezel (Sep 26 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134701650):
Of course I should switch to Lean, the future is there. But a rough estimate for me is that proving in Isabelle is probably 20 times faster than in Lean.
Look at these lines:
```
  also have "... = lambda^2 * (11/2 * C + (3200*exp(-459/50*ln 2)/ln 2 + 83) * delta)"
    unfolding Kmult_def K_def L_def alpha_def D_def using ‹delta > 0› ‹lambda ≥ 1› by (simp add: algebra_simps divide_simps power2_eq_square mult_exp_exp)
  also have "... ≤ lambda^2 * (11/2 * C + 91 * delta)"
    apply (intro mono_intros, simp add: divide_simps, approximation 14)
    using ‹delta > 0› by auto
```
Is there an automatic way in Lean to prove that `3200*exp(-459/50*ln 2)/ln 2 + 83` is bounded by `91`?

#### [Sebastien Gouezel (Sep 26 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134701901):
(This is a rhetorical question, I know that `exp`just made it into Lean). And the true value is `90.959`, so the estimates can not be too rough...

#### [Sebastien Gouezel (Sep 26 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134702195):
More seriously, I would really be interested by the feeling of someone who is proficient both in Lean and in Isabelle, for instance Johannes, as to how quickly he proves things in both systems.

#### [Chris Hughes (Sep 26 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134702470):
What are the drawbacks to Lean? Is it just that the libraries aren't big enough yet?

#### [Johannes Hölzl (Sep 26 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134702586):
Hm, I still miss some things from Isabelle, like most simp procs are just not available.  But this is something I'm sure we get with Lean 4 (or we implement it ourselves). A prover for simple logical statements like `auto` is missing. Type (class) inference in Isabelle is more predictable.
But my general feeling  is that I'm now faster in Lean than in Isabelle. Lean also feels more responsive.

#### [David Michael Roberts (Sep 27 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/134730031):
@**Scott Morrison|110524** 

Oh, nice! I have a student from Comp Sci who was interested in working on something over summer and I casually mentioned Lean. If he's free around the time you're here I could get him to come by

#### [Scott Morrison (Oct 02 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135024554):
Hi all .... I need help selecting an example. I want to actually prove something during my talk. I just recorded myself proving there are infinitely many primes, and even going too fast it took 20+ minutes.

#### [Scott Morrison (Oct 02 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135024570):
I have at most 10... What should I do?

#### [Patrick Massot (Oct 02 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135024595):
`by obviously`!

#### [Scott Morrison (Oct 02 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135024702):
I'll talk a little about automation at the very end. I want something much more basic for this.

#### [Patrick Massot (Oct 02 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135024891):
I'm called for lunch, but I'll tell you more later

#### [Johan Commelin (Oct 02 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135024901):
Hmmm... I'm on the fence about this. If you do something too basic you risk that mathematicians will think this stuff is stupid, and only usable for 1st stuff.

#### [Kevin Buzzard (Oct 02 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135024902):
If you were allowed an import which did the boring bits behind the scenes, then I reckon irrationality of sqrt(2) would fit into 10 minutes, if you formalised it as the assertion that there were no positive nats a and b with a^2=2b^2, or something close to that. But why not go with infinitely many primes? Just hide the tedious work behind an import which you wrote earlier.

#### [Scott Morrison (Oct 02 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135024933):
Hmm, okay, it hadn't occurred to me to cheat.

#### [Scott Morrison (Oct 02 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135024937):
I like that a lot. :-)

#### [Kevin Buzzard (Oct 02 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135024951):
I am absolutely cheating with my 1st year maths example sheets, because they are much too hard otherwise.

#### [Kevin Buzzard (Oct 02 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135025028):
For a 1st year undergrad, $$x^2-3x+2=0\iff x=1\lor x=2$$ is "trivial by the formula for a quadratic"

#### [Scott Morrison (Oct 02 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135025052):
The other things I was considering was doing something basic with `nat` (but this requires way too much talking about inductive types for what I'm trying to do), or proving something completely elementary about groups or group homomorphisms (but this is lame and unexciting).

#### [Kevin Buzzard (Oct 02 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135025054):
And they need this on sheet 1, but the proof uses the fact that the reals are an integral domain and blah blah blah. So I prove it in the import file and just offer them that theorem and tell them to `rw` with it.

#### [Kevin Buzzard (Oct 02 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135025168):
If you want to not cheat, then you could prove something like "A binary relation is an equivalence relation if and only if it is reflexive and Euclidean".

#### [Kevin Buzzard (Oct 02 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135025193):
I would strongly recommend *not* proving that if a function is surjective then it has a one-sided inverse, because the axiom of choice is not pretty :-)

#### [Scott Morrison (Oct 02 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135025450):
It occurs to me that my recent PR to `solve_by_elim` lets me cheat outrageously in the proof of infinitude of primes. I can just tag a few lemmas with attributes and have `solve_by_elim` do large chunks.

#### [Scott Morrison (Oct 02 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135025468):
I'm a little dubious about showing people a proof that only works in a private branch of mathlib. :-)

#### [Kevin Buzzard (Oct 02 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135026497):
I just think that you should tell them that this is actual work in progress and this is what can be done now, and later on it will work in proper mathlib. Or actually just not bore them at all with technical details like this, if time is tight. Who is the actual audience? Does mathlib have something like translation invariance of Lebesgue measure on the reals? What do these people want to see? Existence of complicated things, or proofs of simple things?

#### [Scott Morrison (Oct 02 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135026674):
This is a (maths) colloquium audience at a random Australian university. I really don't know what is worth doing as an example. I definitely want to give some realistic flavour of "writing code", but given everything else that needs to be said in a talk it really can't take more than 10 minutes.

#### [Scott Morrison (Oct 02 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135026727):
I've just written a much shorter proof using a slightly fictional `backwards_reasoning`, and I'll time it later to see if it's viable.

#### [Kevin Buzzard (Oct 02 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135027743):
Colloquium talk -- I don't think I'd care at all about whether it worked in core mathlib or not. Anyone who wants to try and join in will have 100 simpler things to worry about before they're able to prove that there are infinitely many primes. A lot of them might not get past installing the software.

#### [Patrick Massot (Oct 02 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135027757):
Last week I spend some time showing Lean to a collaborator, using https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/demo.lean that I wrote a while ago for that kind of explanation. It shows basic reasoning, as well as crushing things using automation, using axiom of choice, a calc proof, and a proof by induction. Nothing exciting but he was really surprised by how natural it felt

#### [Patrick Massot (Oct 02 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135027806):
I think it's important to show that we have no trouble with axiom of choice, since many mathematicians heard false rumors of proof assistant being limited to constructive math

#### [Patrick Massot (Oct 02 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135027815):
Of course I use my https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/choice.lean

#### [Patrick Massot (Oct 02 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135027819):
I should really PR that into mathlib

#### [Scott Morrison (Oct 02 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135028162):
Thanks, Patrick, that's a nice demo file.

#### [Patrick Massot (Oct 02 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135028184):
It makes me think: is anyone working on https://mathoverflow.net/a/311159/58618?

#### [Kevin Buzzard (Oct 02 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135029001):
" If anyone wants to send me Lean code then I would be grateful." says Neil. He's the guy who invited me to speak in Sheffield in 2 weeks' time.

#### [Scott Morrison (Oct 02 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135029060):
Neil was at the Dagstuhl meeting

#### [Scott Morrison (Oct 02 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135029066):
He gave a talk about his library of "semi-formalised" mathematics.

#### [Scott Morrison (Oct 02 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135029071):
and had someone from every theorem prover sit down and show him the basics.

#### [Patrick Massot (Oct 02 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135029571):
What about using the kbb repository to collaborate on Leaning this wishlist?

#### [Johan Commelin (Oct 02 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135030961):
I think it would be really good if we could answer Neil's question quickly on MO.

#### [Johan Commelin (Oct 02 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135031015):
It would make a good impression if we can actually show the community: look we took this issue seriously, and Lean became a bit more usable.

#### [Johan Commelin (Oct 02 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135031034):
With all the other answers, I think it is also a good idea that we don't forget about them, but mark them as done when we get there.

#### [Johan Commelin (Oct 02 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135031041):
People will be scrolling through that list about 4 years from now, and they should see that everything got done.

#### [Johan Commelin (Oct 02 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135031698):
We could reuse `kbb`, but we could also setup a new project. Alternatively, we create a `tutorial` branch on the community fork.

#### [Johan Commelin (Oct 02 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135031762):
We could put Neil's ideas into the tutorial branch. And also Patrick's demo, translating it to English and annotating it with some comments.

#### [Johan Commelin (Oct 02 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135031785):
I really like your demo file, @**Patrick Massot**. Thanks!

#### [Reid Barton (Oct 02 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135032196):
I like the idea of putting the tutorial in mathlib itself, as an ordinary `.lean` file--then we will have to keep it working with current mathlib.

#### [Johan Commelin (Oct 02 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135032589):
Agreed

#### [Johan Commelin (Oct 02 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135032593):
bitrot is too easy

#### [Johan Commelin (Oct 02 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135032607):
@**Johannes Hölzl** @**Mario Carneiro** What do you think of a `tutorial/` folder in mathlib?

#### [Johan Commelin (Oct 02 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135032616):
Or possible `docs/tutorial`?

#### [Patrick Massot (Oct 02 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135032940):
I like the `docs/tutorial` idea, although it may lead to disappointment for people expecting a fully fledged tutorial. I also PR'ed my `choice` tactic.

#### [Johan Commelin (Oct 02 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135033474):
Ok, how about `docs/demo/`

#### [Johan Commelin (Oct 02 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135033524):
And then a bunch of files called `demo_1.lean` etc...

#### [Kevin Buzzard (Oct 02 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135033576):
+1 from me. Three times now people have asked here "how do quotients work in Lean?" and amongst the answers has been me saying "I wrote this random bit of code which is dumped somewhere on github probably in the xena repo -- maybe it helps?"

#### [Kevin Buzzard (Oct 02 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135033635):
I am writing stuff like this http://wwwf.imperial.ac.uk/~buzzard/xena/html/source/ch1_and_or_props/prop_exercises.html by the way. By the end of term there will definitely be a whole lot more of that stuff.

#### [Scott Morrison (Oct 02 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135066515):
I'm certainly in favour of `docs/demo/` and `docs/tutorials/` (plural tutorials might lessen the blow when people realise it isn't a top-to-bottom tutorial encompassing everything!)

#### [Scott Morrison (Oct 02 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135066566):
I was thinking to record a screen capture of doing the infinitude of primes proof, which may contribute towards answering Neil.

#### [Scott Morrison (Oct 05 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135256674):
https://www.youtube.com/watch?v=3O032b3ujWU&feature=youtu.be

#### [Johan Commelin (Oct 05 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135258077):
Your `Presheaf` misses an `op` (-;

#### [Johan Commelin (Oct 05 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135258109):
By the way, I really like the typography of the slides!

#### [Johan Commelin (Oct 05 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135259581):
@**Scott Morrison|110087** Thanks for sharing this talk! It's a wonderful resource for the rest of us will be giving similar talks in the next few weeks.

#### [Bryan Gin-ge Chen (Oct 05 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135259794):
Fun talk so far! I keep thinking your mouse cursor on the slides is mine though...

#### [Patrick Massot (Oct 05 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135280131):
@**Scott Morrison|110087**  I'd be curious to know whether you had any reactions to your talk. I would have never dared to start explaining Types vs Sets without first showing how it works in the software

#### [Scott Morrison (Oct 05 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135283141):
No one directly complained about the types vs. sets things. I did talk to a quite a few people afterwards (drinks in the department, then drinks at the faculty bar...). From those discussions, I realised the thing I should have been clearer about was the distinction between automatic and interactive theorem proving.

#### [Scott Morrison (Oct 05 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135283165):
It seemed a number of people were aware of the idea of automatic theorem proving, but hadn't realised what you could do interactively.

#### [Scott Morrison (Oct 05 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135283274):
On a side note, I would love to make a fake screen capture sometime, of an interaction with emacs, writing a proof in LaTeX, and occasionally hitting C-:hammer: and having emacs fill in a few sentences for you.

#### [Scott Morrison (Oct 05 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135283278):
Just to demonstrate what we're aspiring to. :-)

#### [Scott Morrison (Oct 10 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135521401):
I gave another talk today, this time in the local "logic" seminar at ANU, which has quite a few participants who use/develop interactive theorem provers. (Notably Michael Norrish, who was involved, I think, in Sledgehammer.)

#### [Scott Morrison (Oct 10 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135521409):
I recorded it, but unfortunately the screen capture part didn't work, so the video is just me getting in the way of an unreadable projector screen.

#### [David Michael Roberts (Oct 10 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135521452):
No slides at https://tqft.net/web/talks yet :-P

#### [Scott Morrison (Oct 10 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135521457):
The notes are at https://tqft.net/web/notes/load.php?name=talks/20181010-experiments-in-Lean, and the video, if you're _really_ keen, is at https://youtu.be/Ldhw4WfXELQ

#### [Scott Morrison (Oct 10 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135521458):
Hit reload, David. :-)

#### [David Michael Roberts (Oct 10 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135521464):
I was too fast...

#### [Kevin Buzzard (Oct 10 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135521722):
So Scott -- you just recorded yourself when you gave the Adelaide colloquium? I am giving a colloquium in Sheffield a week today and I conjecture that these are not recorded in general. You got louder and quieter as you moved nearer and further from your laptop but I was quite happy to live with this minor issue because the advantages of seeing your talk far outweighed it.

#### [Scott Morrison (Oct 10 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135521731):
Yeah, I just plonked my laptop on the table, and used "Camtasia 2", which is a very usable video recording/editing program.

#### [Scott Morrison (Oct 10 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135521734):
It can capture the screen and camera simultaneously, and then arrange them as you like later.

#### [Scott Morrison (Oct 10 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135521740):
It's the same software I used to make the installation videos.

#### [Scott Morrison (Oct 10 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135521807):
If you decide to use it, let me know and I can tell you a few tricks.

#### [Patrick Massot (Oct 10 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135528966):
It's nice to get these recordings but I guess they explain why Lean is always slower than you expect during your talk (in addition to the standard fact that computer misbehave when anyone is doing a demo)

#### [Scott Morrison (Oct 10 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135529028):
Ugh, it was worse than that today. Some serious bug has crept into `rewrite_search` in the last few weeks...

#### [Johannes Hölzl (Oct 10 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135556866):
Michael Norrish wasn't involved in Sledgehammer (AFAIK) but he is the maintainer of HOL4.

#### [Patrick Massot (Oct 11 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135611931):
```quote
As a further data point in the question of usability of proof assistants in real-life (well, mathematical real-life), you can have a look at http://www.math.sciences.univ-nantes.fr/~gouezel/articles/morse_lemma.pdf (preliminary version).
```
See https://arxiv.org/abs/1810.04579. I post this link primarily to point out that everyone can now use this example which has been publicly released.

#### [Patrick Massot (Oct 14 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135773538):
I need to start actually preparing my Thursday talk. Mario, do you think there is any hope we could get modules by, say, Tuesday? Or should I completely give up the hope to talk about how the perfectoid project is doing?

#### [Sebastien Gouezel (Oct 14 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135773936):
At what time are you planning to arrive in Nantes?

#### [Mario Carneiro (Oct 14 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135774051):
I've got a paper deadline by thursday, so I doubt it

#### [Patrick Massot (Oct 14 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135774052):
Around lunch time

#### [Patrick Massot (Oct 14 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135774104):
What are you writing about?

#### [Mario Carneiro (Oct 14 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135774107):
primitive recursion

#### [Mario Carneiro (Oct 14 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135774124):
you know, all that useless stuff in `computability`

#### [Mario Carneiro (Oct 14 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135775265):
don't give me that frowny face, it's my day job that supports all this mathlib stuff

#### [Kevin Buzzard (Oct 14 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135776801):
Patrick: who cares when modules are done. Perfectoids are not going to be done for a while yet, however all of us know that perfectoids *can* be done (which is the main claim) and will be done soon, although the actual path to nirvana involves Mario, Johannes, you, Johan, Me and Scott, *at least*, and we all have other things to do, so sometimes progress is slow.

#### [Patrick Massot (Oct 14 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135776833):
My dream was to have a connected perfectoid project (with sorry) for my talk

#### [Patrick Massot (Oct 14 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135776835):
not a completed project

#### [Kevin Buzzard (Oct 14 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135776877):
https://mathoverflow.net/a/312661/1384 by the way

#### [Patrick Massot (Oct 14 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135776878):
(well, completed was my initial dream, but I understood a long time ago that it was hopeless)

#### [Kevin Buzzard (Oct 14 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135776977):
I think I take a more pragmatic view. I'll talk about perfectoids in my talk on Wednesday but I don't expect anyone to be racing to download and install Lean and then immediately cloning our project to see how it all works. Any newcomers face a mountain before they can even understand the complex current status of the perfectoid project properly, and anyone who doesn't download Lean (i.e. 99% of my audience) can just know that it's "work in progress with light very much at the end of the tunnel".

#### [Patrick Massot (Oct 16 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135920700):
I tried my Thursday talk on a mostly innocent colleague today. @**Sebastien Gouezel** I need urgent confirmation that Nantes' colloquium last at least three hours...

#### [Johan Commelin (Oct 16 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135920801):
O.oo... did the innocent colleague feel abused?

#### [Patrick Massot (Oct 16 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135920947):
He seemed ok

#### [Patrick Massot (Oct 16 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135920970):
I tried to demonstrate too much, and I had no reference point about how fast you can live code during a talk

#### [Johan Commelin (Oct 16 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135920997):
Ok, well. Then it's good that you practiced!

#### [Patrick Massot (Oct 16 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135921018):
Yes. Of course I usually don't practice my talks, but this time I new it was necessary

#### [Sebastien Gouezel (Oct 16 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135927843):
```quote
I tried my Thursday talk on a mostly innocent colleague today. @**Sebastien Gouezel** I need urgent confirmation that Nantes' colloquium last at least three hours...
```
Yes, three hours from 17h15 to 18h15.

#### [Patrick Massot (Oct 16 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135927936):
Thanks.

#### [Patrick Massot (Oct 16 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135927945):
I'll be able to sleep then

#### [Sebastien Gouezel (Oct 16 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135927947):
Once, we had a one hour colloquium by Laurent Lafforgue, that lasted almost two hours. And the chairman didn't dare to interrupt him. Maybe you can try this.

#### [Patrick Massot (Oct 16 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135928019):
Please hold on, let me grab a Fields medal first...

#### [Patrick Massot (Oct 16 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135928128):
However I guess I'll give a similar flavor talk: let me tell you about what could be a revolution in mathematics, but is currently completely useless...

#### [Kevin Buzzard (Oct 16 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135928797):
My talk on Wed has changed quite a bit. I would say I learnt quite a lot in the last few weeks about what is going on here. Computer scientists and mathematicians have two different definitions of pure mathematics. They meet at the bottom with proofs that sqrt(2) is irrational etc, but after some point the sociological aspects of mathematics start influencing our tribe, and not theirs, and this makes some things quite different. Our experts proclaim what is proved and what is not proved; we try to choose the appropriate experts for each theorem, and our experts do not always get it right. However we have things that the CS world view does not have, like a very fluid understanding of techniques, and guiding principles such as the global Langlands reciprocity "principle", which is not even a well-defined statement but which seems to have well-defined consequences (for example functoriality, which can certainly be made into a formal statement (in more than one way, depending on how optimistic you want to be)). We also have very different opinions on what comprises beautiful mathematics. Both communities have a lot to offer each other in the future, I believe, and the main issue stopping this from happening is that there are very few experts in one area who know any more than epsilon about the modern tools available in the other area. That's what we have to change.

#### [Sebastien Gouezel (Oct 16 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135929670):
```quote
However I guess I'll give a similar flavor talk: let me tell you about what could be a revolution in mathematics, but is currently completely useless...
```
I think I will be more convinced by your talk than his...

#### [Kevin Buzzard (Oct 16 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135929771):
You [Sebastien] are a piece of evidence in my talk :-)

#### [Patrick Massot (Oct 17 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135954880):
Yes, I thought about saying "proof assistants are nice and easy, anyone can use them, look at what Sébastien did!". But that works only with people who never heard of Sébastien, and I fear there won't be many of them in the audience tomorrow.

#### [Kevin Buzzard (Oct 17 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135955273):
My talk is today. I'm going to say just that there are two different ways of doing pure mathematics and over the last year I have realised how little the two groups of people doing them are communicating with one another, and that both have a lot to offer the other side.

#### [Kevin Buzzard (Oct 17 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135955339):
I don't think I'm going to make any claims about how using these tools is easy. In fact saying "I took a year of doing number theory research and learnt mathematics from scratch starting with undergraduate level, then graduate, then research" is not a particularly good advert for how easy they are. But this can be fixed. All we need is a good book.

#### [Patrick Massot (Oct 17 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135980228):
Tomorrow at that time I'll be talking about Lean, and I may quickly show this website. Everybody, please refrain from emphasizing pain and bugs at that time :wink:

#### [Johan Commelin (Oct 17 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135984455):
@**Kevin Buzzard** We are all desperately longing to hear your experience!

#### [Kevin Buzzard (Oct 17 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135984726):
It went fine. About 100 people (including @**Neil Strickland** ), but I spent most of my talk talking about the "mess" that mathematics was in, and just the last 15 minutes suggesting that mathematicians and computer scientists should talk more. I met a computer scientist who said "I use Isabelle and the fact that there are no dependent types is problematic for mathematicians", which was not what Paulson said, but I need to figure out who is right.

#### [Patrick Massot (Oct 17 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135985622):
Makes me think: @**Kevin Buzzard**  and @**David Michael Roberts**, do you have news from the abc war?

#### [Kevin Buzzard (Oct 17 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/135986172):
Nothing from me. I don't think it's a war. The community have decided it's not a proof and everything else is now probably noise unless M actually decides to attempt to engage with the criticism.

#### [Scott Morrison (Oct 17 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136002706):
You didn't record, did you?

#### [Kevin Buzzard (Oct 17 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136002854):
I didn't.

#### [Kevin Buzzard (Oct 18 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136005731):
I spent over half the talk giving what I thought was a fairly level-headed summary of things like the current status of the classification of finite simple groups and Arthur's work on the trace formula -- parts of maths where there are holes in the literature. I then talked a little bit about errors in the literature and also in the first half spent a bit of time philosophising about the nature of mathematics as done by humans and talking about various sociological issues which interfere with a formalist's viewpoint of what mathematics should be (I've been reading books by Bruno Latour). I then showed them Lean and some code that @**Chris Hughes** wrote, stressing that he had no computing experience when he arrived at Imperial 1 year ago (I did no live coding, for tedious technical reasons -- a minor system failure there) and showed off some of my summer students' work, and finished with a plea that mathematicians and computer scientists should work together more closely in the future on a common vision for pure mathematics, because we both have things to offer the other "tribe".

Neil Strickland was a very engaging host, he knows a lot about other proof assistants and I trusted him to provide a perhaps more unbiased view than that which I might find here (that's not an accusation -- I think people here are very level-headed in general, but many of us know more about Lean than any other system). But I definitely came away from that conversation feeling that I had not made a mistake in choosing Lean. Tom Bridgeland is another mathematician that I have a lot of respect for, and was very pleased he came to lunch with us; he also had interesting questions and comments. He pointed out that Carlos Simpson had formalised localising categories in Coq a decade ago, which I didn't know (I think of Simpson as a mathematician, and I know that most mathematicians wouldn't be able to formalise anything). In some sense the funniest thing Bridgeland said was that he didn't care less about the foundations of his subject, he just got on with it, which I thought was interesting for someone who used categories so much. I met the person who taught the introduction to proof course and told them to send me some of their problem sheets and I'd see what I could do with them.

#### [Kevin Buzzard (Oct 18 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136006600):
PS I'm speaking to 20 bright high school kids next week

#### [Adam Kurkiewicz (Oct 18 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136012105):
@**Scott Morrison** great talk, it's a real shame that audio gets a lot worse halfway through the talk. Loved the joke about old mathematicians dying out :D (you guys do get a lot of freedom in what you can say at work!). I think what could have been valuable (maybe you said it and I missed it) was that regardless of how the proof is written, it gets compiled down to a simplified form checked by a trusted kernel. Otherwise using the backwards reasoning tactic seems a bit like a cheat!

#### [David Michael Roberts (Oct 18 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136015915):
I emailed Mochizuki and he clarified a couple of things in response to some direct questions about his Report. I will continue to probe as I get time. For example: he discusses "gluing two [char 0] fields along their common subfield Q" in the Report. I imagined this to be some kind of formal colimit, or the pushout of rings or similar, and so asked what it really was: he said he meant the pushout of sets. I suspect there's a lot of these details that are in fact quite crucial to the category-theoretic constructions that are not very explicit.

#### [Reid Barton (Oct 18 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136018291):
```quote
PS I'm speaking to 20 bright high school kids next week
```
What's your plan for this talk? I imagine it's easier to get a bright high school student to try out Lean than the average mathematician.

#### [Kevin Buzzard (Oct 18 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136021117):
Plan for high school kids talk: definition of nat and addition; proof that addition is commutative on nat.

#### [Johan Commelin (Oct 19 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136093607):
@**Patrick Massot** How did it go?

#### [Patrick Massot (Oct 19 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136094876):
I think it was ok. Of course I rushed at the end and live coding doesn't work so well when you are already 5 minutes over time. But I think people were happy. I'll know more today because I'll spend the day in the department. There should be a video recording available at some point (but the talk was in French)

#### [Johan Commelin (Oct 19 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136134133):
So, what kind of feedback did you get? @**Patrick Massot**

#### [Patrick Massot (Oct 19 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136136553):
I got excellent feed-back. Several people thanked me for this talk today (but of course people who don't like talks rarely say it)

#### [David Michael Roberts (Oct 20 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136145249):
Well, I have one small further insight: for Mochizuki, a diagram in a category is a **subcategory**, not a functor from a diagram shape. This probably stems from his desire to only ever use isomorphism classes of functors. I will write up a blog post when I can get all I sensibly can.

#### [Johan Commelin (Oct 25 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136453479):
@**Scott Morrison|110087** Do you have a quick list of lemmas that you added to `back` to enable the nice proof of infinitude of primes that you demoed in your talk?

#### [Floris van Doorn (Oct 25 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136454981):
<deleted, I posted in wrong topic>

#### [Scott Morrison (Oct 25 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136456152):
If you look at the `back` pull request, you’ll find that proof as the test case.

#### [Kevin Buzzard (Oct 25 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136456438):
So I gave a school talk yesterday (to bright 17 year olds who had elected to go on a maths camp -- it's "half term" here so kids have a week off). It went better than my last school talk, it has probably got as far as "OK" but I am still not at "brilliant". One thing I have learnt is that even these bright schoolkids *do not know what induction is* which is a real problem when trying to do anything. However they *do* know what the complex numbers are! Here was what I did, and I think it went OK:

1) Observation that $$1+2+3=6$$ but they did make a choice about which addition to do first, because with $$9-2-1$$ it really matters which subtraction you do first. [NB this part of the talk is irrelevant because of what happened later]

2) Observation that $$a+b=b+a$$ is intuitively obvious if we think about addition as "getting more stuff" or "moving further in one direction", but that $$0.999999999...<1$$ is also kind of intuitively obvious, as is $$0.999999999...=1$$ (and we can't just argue about which one is right -- we need rules and definitions -- "pictures are not enough"). 

3) 
```lean
inductive thing
| stop : thing
| tick : thing -> think
```

and a long time talking about what this meant, culminating in a general understanding that every `thing` looked like `tick (tick (tick ...(tick (stop)))...`

4) `thing` -> `nats`, `stop` -> `zero`, `tick` -> `succ` (there were giggles about the "suck" word, maybe there are better words). `one := succ zero`, `two := succ (succ zero)`, `two' := succ (one)`

5) Proof that `two = two'` by `rfl`

6) Definition of induction as "proof by knocking over the first domino and watching the rest fall over" (note: kids these days have never seen a domino).

7) Definition of addition on `nats` *and no attempt to prove anything like associativity* because I realised it would simply be too hard. [rendering (1) obsolete]. Basically I bailed on associativity. I think that internalising the "two rules for addition" (the equation lemmas) and then using them to prove what is quite a complex thing (it's a good few lines) is too hard for schoolkids.

8) Proof that `one + one = two` from the axioms. This *worked*. Students could attempt to unravel what `one + one = two` means and see that the proof was `rfl`.

9) Now questions. I tell them that we prove `a+b=b+a` next, and ask what happens after that. "Definition of multiplication" says one. Eventually I get them to come up with the following plan: define `+` and `*` on nat, define int (because someone says "define subtraction!" and I say "We can't! How do we do 2 - 3?"), define `+-*` on int, define rat (because we can't do division until we do), define `+-*/` on rat, define `real`, define `+-*/` on real. Then define `complex`.

10) Show them the definition of `complex` as a pair of reals, invent stupid notation `[x,y]` for complexes because I tell them `x+yi` is not allowed because we didn't define `+` or `i` yet, then challenge them to define addition and multiplication, challenge them to prove on paper that multiplication is commutative.

So essentially no induction at all, and I get to show them random bits of Lean, and I *think* that this is just about a level which works. Still needs work, but a much more positive experience than last time when I was telling people that induction on false was `false -> P`.

#### [Mario Carneiro (Oct 25 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136456944):
Re: "suck" giggles, I find that you can avoid some of that by pronouncing it "sook"

#### [Mario Carneiro (Oct 25 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136456948):
at least you didn't have to talk about coq

#### [Kevin Buzzard (Oct 25 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136457040):
I might just give up and call it `nextone` or something. Coq uses `S` I think, which is probably not good for a school talk either.

#### [Andrew Ashworth (Oct 25 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136459392):
is pronouncing it in full as "successor" not an option :)?

#### [Johan Commelin (Oct 25 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136459525):
It becomes tedious when you want to say `4 = succ (succ (succ (succ zero)))`, I guess...

#### [Chris Hughes (Oct 25 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136460253):
How about a CS flavour with "increment". I think thinking about definitions of functions as computer programs is easier than talking about axioms, particularly because the distinction between axioms and definitions made in Lean is not made everywhere else. I certainly didn't have a clear idea about what an axiom was a year ago.

#### [Kevin Buzzard (Oct 25 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136461201):
```quote
How about a CS flavour with "increment". I think thinking about definitions of functions as computer programs is easier than talking about axioms, particularly because the distinction between axioms and definitions made in Lean is not made everywhere else. I certainly didn't have a clear idea about what an axiom was a year ago.
```
I like `inc`! It's sort of obvious what it means, `inc (inc zero)` means increment zero twice.

#### [David Michael Roberts (Oct 26 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136522124):
OR even `add_one`

#### [Adam Kurkiewicz (Oct 28 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136651427):
Kevin, how much time did it take you? When I did my workshop on commutativity of addition, I didn't get any giggles on succ, but it could be because by the time we got there, it was already 2 hours (with a single short break), and I had to give up on interactivity and fall back from workshop-style to lecture-style. I was still getting quite a lot of questions, and they at least *saw* me do the proofs, but some were getting really tired towards the end.

#### [Adam Kurkiewicz (Oct 28 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136651434):
Did your kids also have access to computers, or was it just one computer?

#### [Kevin Buzzard (Oct 31 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136842650):
```quote
As a further data point in the question of usability of proof assistants in real-life (well, mathematical real-life), you can have a look at http://www.math.sciences.univ-nantes.fr/~gouezel/articles/morse_lemma.pdf (preliminary version).

Some time ago, I mentioned that I found a gap in a published paper while formalizing it in Isabelle. This gap is now corrected, and the new proof is completely formalized. The above paper explains the corrected proof, for mathematicians, but it also mentions the formalized proof. By the way, it raises interesting questions on the way to write a math papers when you have a formalized proof (when we need a lemma that is related, but not exactly the same, to results already in the literature, should we give the proof or just point the reader to the formalized proof?) We have tried to find some middle ground here, but I guess our way to write papers will have to change. Comments welcome!
```
https://mathoverflow.net/a/312661/1384 @**Sebastien Gouezel**

#### [Johan Commelin (Oct 31 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136842838):
It's really cool that this is now the accepted answer!

#### [Kevin Buzzard (Oct 31 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20talk%20for%20mathematicians/near/136850283):
Indeed -- that's what prompted me to post here.

