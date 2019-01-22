---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/05206Introductions.html
---

## [new members](index.html)
### [Introductions](05206Introductions.html)

#### [Xita Meyers (Sep 06 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133439634):
Hello, I have never asked a public question on Zulip before, and in order for me to get used to doing so, I have been ordered by @**Kenny Lau**  to state the following in order to introduce myself: 

"I am a proud student of Kevin Buzzard."

I look forward to learning much more about Lean through Zulip. 

Thanks.

#### [Kenny Lau (Sep 06 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133439648):
Welcome!

#### [Xita Meyers (Sep 06 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133439666):
Thanks for welcoming me! This is my first time navigating Zulip, nice to meet you!

#### [Johan Commelin (Sep 06 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133439730):
Welcome Xita! Nice to meet you.

#### [Johan Commelin (Sep 06 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133439735):
What kind of stuff have you been looking at lately? Were you involved in UROP?

#### [Xita Meyers (Sep 06 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133439876):
I've been involved in the UROP, but didn't learn very much by reading Theorem Proving in Lean; It was hard to understand to some extent. Currently I'm trying to prove a lemma in number theory that if p is a prime of form 4K + 3, then it cannot divide an integer of form x^2 + 1.

#### [Johan Commelin (Sep 06 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133440201):
Ok, nice. Whenever you have questions, just ask! That's how we are all learning. (Most of us don't find the documentation sufficient, but we lack the time, energy, or courage to improve it.)

#### [Kenny Lau (Sep 06 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133440214):
or motivation

#### [Kevin Buzzard (Sep 06 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133440757):
Hey Su. Here would be a cheap way of doing this. If x^2=-1 mod p (p=4K+3) then x^{4K+2}=-1 mod p as well, contradicting Fermat's Little Theorem.

#### [Xita Meyers (Sep 06 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133450178):
Yeah, that's how I've been trying to do it. It's taking longer than I expected.

#### [Harald Schilly (Sep 06 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133450780):
Hi, I'm Harald, and I'm one of the devs behind CoCalc ... I've just worked on improving its syntax highlighter and well, I should also learn one or another detail about lean itself :-)

#### [Patrick Massot (Sep 06 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133451632):
Welcome Harald!

#### [Kevin Buzzard (Sep 06 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133455563):
@**Harald Schilly** here would be a good place to get information about where Lean is looking for files to import. At the minute I couldn't get mathlib imports working in CoCalc. This and the current inability to see the goal in tactic mode are in my mind the last two problems which need to be solved before lean is really usable. In particular, you guys are nearly there. I am hoping Gabriel Ebner gave you some hints about the latter goal, and the former goal can't be hard. I can't believe I'm saying this but actually just dumping the mathlib files into the lean core directory would probably work, although it's a horrible idea.

#### [Harald Schilly (Sep 06 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133457088):
So, I know there is an env variable `LEAN_PATH` and we could set it to something. There is also a precompiled (but months old) mathlib in `/ext/lean/lean/mathlib/`. I bet it just depends on setting that lean path correctly to make it work. Should we discuss this in #**general** ?

#### [Johan Commelin (Sep 06 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133457128):
Sure, I think we could move this discussion to the CoCalc thread.

#### [Johan Commelin (Sep 06 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133457191):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc

#### [Mario Carneiro (Sep 06 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133457207):
@**Harald Schilly** Don't use `LEAN_PATH`, it is deprecated since the `leanpkg` tool

#### [Kevin Buzzard (Sep 06 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133457458):
There's something I don't understand about the set-up. At some point Lean will have to be told "look at `leanpkg.path`, that's where you should import stuff". How does that bit work? Aah, presumably this depends on the IDE. And because Harald is involved with writing a new IDE...maybe he needs to be told to look at `leanpkg.path`.

#### [Tobias Grosser (Sep 07 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133490898):
Hey guys, just wanted to introduce myself as it seems to be a common habit here. Some of you may already have seen that I started to ask some smaller questions and also organize a theorem proving sozial at ETH.

#### [Tobias Grosser (Sep 07 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133490940):
My background is mostly compilation, static analysis, loop transformations, often using Presburger arithmetic to get where I want to be.

#### [Tobias Grosser (Sep 07 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133490942):
Since a year I look into theorem proving, and recently started to use lean.

#### [Tobias Grosser (Sep 07 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133490957):
I work since maybe 10 years on LLVM and developed there the Polly loop optimizer

#### [Tobias Grosser (Sep 07 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133491006):
I am interested in using lean eventually for teaching and for some of my day-to-day work.

#### [Simon Hudon (Sep 07 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133491016):
Welcome to the Lean community! I hope it lives up to your expectations :)

#### [Tobias Grosser (Sep 07 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133491062):
Thanks. Until now everybody is very helpful. Looking forward to meet the first members in person next week.

#### [Simon Hudon (Sep 07 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133491140):
I wish I could attend. I'm no longer in Zurich but I'm sending a representative

#### [Simon Hudon (Sep 07 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133491150):
My friend Malte is a lecturer at ETH and I think he wants to attend

#### [Tobias Grosser (Sep 07 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133491315):
That's great.

#### [Tobias Grosser (Sep 07 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133491317):
Let me know when you are back in Zurich

#### [Simon Hudon (Sep 07 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133491337):
I haven't been back in years but I think I'm due for a visit soon :)

#### [Corey Richardson (Sep 08 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/133555206):
hi :) I'm coming back around to using Lean. previously I was an intern working on the seL4 verification, and a student doing research for cryptographic protocol analysis ATPs. good to see such a community has sprung up around lean!

#### [Ryan Smith (Sep 21 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134356472):
Hi, I'm completely new to Lean. I come from an algebra and number theory background, and don't have much experience with formal logic beyond a course taken in undergrad a lot of years ago.

#### [Johan Commelin (Sep 21 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134356476):
Cool, welcome! Where are you based?

#### [Johan Commelin (Sep 21 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134356480):
I'm a postdoc in Freiburg, working in algebraic geometry.

#### [Tobias Grosser (Sep 21 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134358790):
Welcome Ryan.

#### [Tobias Grosser (Sep 21 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134358793):
Researcher at ETH Zurich here!

#### [Patrick Massot (Sep 21 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134361010):
Hi Ryan! I'm a French mathematician working in Orsay. Would you care to tell us how you heard about Lean?

#### [Sebastian Graf (Sep 21 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134365477):
Hi, I'm a PhD student in Karlsruhe with strong interest in functional programming. Although I'm mostly into GHC middle-end stuff, I really like type systems and would spend more time (well, if I had more time to spend) formalizing things, preferrably in Lean :)

#### [Johan Commelin (Sep 21 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134365877):
Welcome! Karlsruhe is not too far from Freiburg (-; Have you seen https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/LUG.20Freiburg.202018 ?

#### [Sebastian Graf (Sep 21 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134374044):
Sounds interesting! I'm afraid I won't be able to make it due to the usual busy stuff during semester.

#### [Agnishom Chattopadhyay (Sep 21 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134380063):
Hi;

I am Agnishom. I am an undergraduate student of Mathematics and Computer Science. I am interested in Logic in general.

Can somebody help me figure out how to install lean and configure emacs on my system?

#### [Alistair Tucker (Sep 21 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134380466):
I suggest homebrew if you are on a mac

#### [Agnishom Chattopadhyay (Sep 21 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134380797):
I am on linux mint

#### [Kevin Buzzard (Sep 21 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134392224):
https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/

#### [Kevin Buzzard (Sep 21 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134392286):
Does that help? Are there some instructions somewhere on github? I forget.

#### [Robert Kornacki (Sep 21 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134396506):
Hi there, I've just started going through Theorem Proving In Lean and I've got to say I've really been enjoying using it. I come from a functional programming background, and when I tried out Idris earlier this year I really got a pull into the dependent type world. Lean has been a joy to use thus far in comparison to Idris for the very small reason that it's impeccably fast for displaying goals & holes making the whole process feel really smooth rather than a little clunky (though I do enjoy Idris' ability to name holes). Out of curiosity, does anyone know of any performance comparisons of Lean vs Idris, would be neat to know.

#### [Andrew Ashworth (Sep 21 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134400827):
Seeing as how Idris allows for code extraction to C, and is a language very much more focused on programming, I can't imagine the comparison being very favorable. When Lean 4 rolls around, that'll be a more interesting comparison since there will be easy interop with C++

#### [Reid Barton (Sep 21 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134403093):
And ordinary lean programs will be compiled/JITted, as I understand it, rather than run in a VM like today

#### [Simon Winwood (Sep 25 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134559792):
Hi All, I am a research engineer at Galois.  I am mainly used to Isabelle, and less-so Coq.  I am mainly interested in program verification, but also am keen on theorem proving in general.

#### [Simon Hudon (Sep 25 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134566178):
Hi Simon! Welcome to Lean! I was an intern at Galois last year and that's actually where I first started using Lean. I got hooked.

#### [Simon Winwood (Sep 25 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134572150):
Ah, I thought I recognised your name,

#### [David Michael Roberts (Sep 27 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134737991):
Hello all. I've been following UF/HoTT/proof assistants as a lurker since the special year at the IAS. I'm in category theory/differential geometry/topos theory. I have some non-commutative algebra constructions (groupoid/category algebras) that I'd like to have a crack at formalising, as I warm up to learning about serious C*-algebra stuff (don't think I'd formalise that, but who knows...)

#### [Kevin Buzzard (Sep 27 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134739330):
By far the best way to learn how to use the software is to just decide that you're going to try formalising X (rather than X and Y and Z and W) and then ask on the forum with a precise reference of what you're aiming at, and you'll get comments either of the form "this is done" or "this is feasible, start like this" or "this is way too hard, you'll first need to do X' so if you're still interested in then start there".

#### [David Michael Roberts (Sep 27 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134740913):
OK, thanks. :-)

#### [Kevin Buzzard (Sep 27 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134754218):
...although probably reading Theorem Proving In Lean might help too. I was planning on writing docs for mathematicians over the summer, but my mathematicians didn't really seem to need docs, they asked each other questions (or me) and got stuck on things which wouldn't necessarily be covered in the docs I was planning on writing, so I didn't write them. I might have to write them next month when I have far more students than I can talk to individually.

#### [Kevin Buzzard (Sep 27 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134754259):
I guess even if you don't plan on formalising something, you could still state more precisely what you might be interested in formalising and the community might offer comments.

#### [Scott Morrison (Sep 27 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134776123):
Welcome, David! It's fun here. :-)

#### [David Michael Roberts (Sep 28 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134778506):
Well, given a small groupoid and a field, I want to construct the convolution algebra on the vector space with basis the arrows of that groupoid, and also construct the multiplier algebra of such a beast. I guess I would need:

fields
vector spaces
algebras
small groupoids
modules and their maps

I'll have to have a dig through mathlib to see what's there already, but I imagine a bunch of those (if not small groupoids) have been done.

#### [Mario Carneiro (Sep 28 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134778666):
We have all of those except algebras and groupoids, although we have categories so it's not hard to state what a groupoid is.

#### [Reid Barton (Sep 28 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134778683):
I have (small) groupoids in another project already which I could PR

#### [Reid Barton (Sep 28 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134778701):
It's the most basic possible thing, but should get you started

#### [Mario Carneiro (Sep 28 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134778720):
what is the convolution algebra?

#### [Mario Carneiro (Sep 28 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134778791):
I guess the elements of the algebra are linear combinations of arrows of the groupoid, and multiplication involves the composition of arrows somehow?

#### [Kevin Buzzard (Sep 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134808586):
what is an `algebra` in this context? The word is used in so many ways. In commutative ring theory "A is a B-algebra" is simply a long-winded say of saying `f : B -> A`

#### [David Michael Roberts (Sep 28 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809225):
Mario: Correct. Multiplication is the bilinear extension of f*g = f\circ g (if composable), 0 (if not)

#### [David Michael Roberts (Sep 28 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809282):
Kevin:  a vector space with an associative bilinear multiplication—and I'm not going to assume unital.

#### [Kevin Buzzard (Sep 28 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809370):
Well making this definition is trivial, but Lean doesn't quite work like that; one also has to make a basic API for the definition, which means proving 20 trivial lemmas about it

#### [Kevin Buzzard (Sep 28 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809379):
and giving them names which computer scientists find acceptable

#### [Kevin Buzzard (Sep 28 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809429):
(something which I was initially skeptical about but now have very much come around to)

#### [Sean Leather (Sep 28 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809430):
~~computer scientists~~ Mario and Johannes

#### [Kevin Buzzard (Sep 28 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809443):
Apologies for bad-mouthing the CS community in general :-)

#### [Johan Commelin (Sep 28 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809452):
Here a question that I don't know how to answer: are Lie algebras algebras?

#### [Johan Commelin (Sep 28 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809460):
Bourbaki says: yes

#### [Kevin Buzzard (Sep 28 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809461):
not in general I guess

#### [Johan Commelin (Sep 28 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809465):
But I think Lean will run into trouble with notation...

#### [Kevin Buzzard (Sep 28 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809466):
But it's completely consistent that Bourbaki have a different definition of algebra

#### [Johan Commelin (Sep 28 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809544):
I think if we want to use `has_mul` then the multiplication must be associative.

#### [Kevin Buzzard (Sep 28 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809550):
the word is used in so many ways. I think I once checked explicitly that the Lie bracket was not associative in general, even though there's a meta-proof of the form "if it were associative in general then someone would have pointed this out by now".

#### [Johan Commelin (Sep 28 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809559):
Otherwise brains will explode

#### [Kevin Buzzard (Sep 28 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809563):
`has_mul` is just notation, it doesn't have to be associative by definition

#### [Johan Commelin (Sep 28 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809568):
associative Lie brackets are trivial, right? So you get abelian Lie algebras

#### [Kevin Buzzard (Sep 28 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809613):
Notation is a minefield and it's now my opinion that this is to a large extent the fault of mathematics.

#### [Johan Commelin (Sep 28 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809619):
Sure, but non-associative `has_mul` might even create more problems then your `int` vs `nat` woes

#### [Kevin Buzzard (Sep 28 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809628):
We invented notation over the last few hundred years and some of it is awful. Quadratic Reciprocity is a statement about fractions in brackets.

#### [Johan Commelin (Sep 28 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809704):
Somehow even Lean depends on notation. When I first understood that the simplifier relied on notation I was really disturbed.

#### [Johan Commelin (Sep 28 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809707):
But notation seems to be more than just syntactic sugar

#### [Kevin Buzzard (Sep 28 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809815):
Unfolding is an art, this is my understanding of it. If you unfold everything then you have a complete mess which you cannot work with. But *notation*? Doesn't that just get unfolded by the parser right at square 1 so `simp` can't even notice it is there?

#### [Mario Carneiro (Sep 28 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809871):
there might be a terminological clash here - `has_mul` and such are often called "notation typeclasses" since they have a notation associated to them, but obviously `simp` knows about `has_mul`, even if it doesn't know that `*` is used to draw it

#### [Johan Commelin (Sep 28 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809884):
Aaah, so we can drop the associativity condition

#### [Johan Commelin (Sep 28 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809890):
And make `[X,Y]` notation for `Lie_algebra.mul X Y`

#### [Johan Commelin (Sep 28 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134809940):
It's really sad that we can't bind notation to namespaces...

#### [Johan Commelin (Sep 28 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810105):
@**Mario Carneiro** Do you think this is a viable strategy? To have `algebra` and then `is_unital`, `is_assoc`, `is_comm`, etc...

#### [Johan Commelin (Sep 28 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810107):
Where `algebra` just means bilinear multiplication on a module.

#### [Mario Carneiro (Sep 28 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810151):
ironically, there is already `is_comm`, `is_assoc` etc in `@[algebra]`

#### [Mario Carneiro (Sep 28 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810156):
but I think that means something different

#### [Johan Commelin (Sep 28 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810158):
What do they mean?

#### [Mario Carneiro (Sep 28 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810160):
it is not bound to a notation

#### [Johan Commelin (Sep 28 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810162):
Ok, but we could have `has_mul.is_assoc` etc, right?

#### [Mario Carneiro (Sep 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810169):
what's the use case?

#### [Johan Commelin (Sep 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810175):
Well, there are entire fields of mathematics that work with associative algebras

#### [Johan Commelin (Sep 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810181):
But there are also entire books about non-associative algebras

#### [Mario Carneiro (Sep 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810182):
but you don't want to use `*` for them, right?

#### [Johan Commelin (Sep 28 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810191):
Sometimes the associative algebras are unital, and/or commutative

#### [Johan Commelin (Sep 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810194):
Why not use `*`?

#### [Mario Carneiro (Sep 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810195):
that's whatever

#### [Johan Commelin (Sep 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810239):
My proposal is to use `has_mul` for all of them

#### [Mario Carneiro (Sep 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810240):
If you want to use `*`, go ahead and define your typeclass based on `has_mul`

#### [Johan Commelin (Sep 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810250):
And then only for Lie algebras introduce a second notation, namely `[X,Y]` instead of `X * Y`

#### [Mario Carneiro (Sep 28 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810251):
the danger is if you need a conventional mul and also a lie bracket thing at the same time

#### [Johan Commelin (Sep 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810256):
I have never heard of that before

#### [Johan Commelin (Sep 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810260):
Ah, I do

#### [Johan Commelin (Sep 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810263):
Hmmm... that's nasty

#### [Johan Commelin (Sep 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810271):
Every ring gives a Lie algebra, via the commutator bracket

#### [Mario Carneiro (Sep 28 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810278):
yeah you probably don't want to confuse those

#### [Johan Commelin (Sep 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810340):
Hmmm... so we have `algebra` without notation. Just the `op`. And then `assoc_algebra` gets `has_mul`, and `Lie_algebra` gets `has_bracket`. Could that work?

#### [Johan Commelin (Sep 28 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810358):
Hmm... but then there would still be two instances of `algebra` on every `ring`.

#### [Johan Commelin (Sep 28 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810363):
And they aren't even equal.

#### [Mario Carneiro (Sep 28 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810370):
What about a translation wrapper like `multiplicative`?

#### [Johan Commelin (Sep 28 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810414):
What would that do?

#### [Mario Carneiro (Sep 28 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810431):
change the notation

#### [Mario Carneiro (Sep 28 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810447):
so you could develop the theory on `has_mul`, and then transfer any results to the `has_bracket` version

#### [Johan Commelin (Sep 28 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134810512):
Ok, but then, suppose we have `[ring R]`, this would give `[algebra R]`. And then? Something like `[Lie_algebra (commutator R)]`?

#### [Chris Hughes (Sep 28 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134811201):
Isn't semigroup has_mul.assoc?

#### [Kevin Buzzard (Sep 28 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134811280):
Yeah but the Lie algebra associated to a ring is a second "multiplication", defined as `[a,b] = a*b-b*a`. This is not associative.

#### [Kevin Buzzard (Sep 28 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134811302):
It's not even a multiplication really, this conversation was started by the observation that Bourbaki apparently claims that Lie algebras are "algebras", whatever that word means.

#### [Mario Carneiro (Sep 28 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134812486):
I think this is the wrong thread

#### [Ryan Smith (Oct 01 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Introductions/near/134948015):
Sorry for the slow response, went on vacation right after learning about Lean :). I read about the verification of Feit-Thompson and I was really impressed that compute checked proofs have come so far that such a thing was possible. That lead to doing a survey of proof checkers, and it seemed that Lean was a much more dynamic community than Coq and some of the others. If I needed any more proof that Lean is legit, seeing Kevin Buzzard here is a pretty strong endorsement.

I actually left academia a couple years ago for industry, and I've been thinking about find project that would allow me to be more involved with math and work on something that would useful to the community.

