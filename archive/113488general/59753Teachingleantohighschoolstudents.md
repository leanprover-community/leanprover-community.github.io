---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59753Teachingleantohighschoolstudents.html
---

## Stream: [general](index.html)
### Topic: [Teaching lean to high school students](59753Teachingleantohighschoolstudents.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Jul 12 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/129529806):
Hey guys, I'll be talking about lean to a bunch of smart high school kids (BMO/ BIO type of crowd, they can program in python and write down "normal" maths proofs at a high school level).

I was thinking about some motivating example that we could cover from scratch in about 2 hours of a workshop.

I'm thinking to show that a + b = b + a over a custom-built nat (without using tactics), but that obviously involves covering all the stuff up to inductive types, which is not something they might be ready for.

I think I've heard @KevinBuzzard talking about teaching lean to high school students. What's the general feel on this task choice?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/129529953):
I gave a talk of a similar length to a similar crowd (UK IMO squad) and I pitched it too high. I wanted to show them inductive types, and how induction on nat was induction, but induction on false was the proof that false -> X, and I think it was all too much.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/129530016):
I think your idea is better though. When I was getting a feeling as to what Imperial College 1st year students could handle, I wrote a blog post about xnat, and it was very popular: https://xenaproject.wordpress.com/2017/10/31/building-the-non-negative-integers-from-scratch/ . I feel like this was the first time I managed to get students to engage in writing Lean code by themselves.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/129530033):
Warning: this does get pretty heavy at the end; I suspect that even a bright schoolkid would really struggle with proving e.g. transitivity of `<`, because you have to induct on exactly the right statement.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/129530147):
On the other hand I think that commutativity of addition is a very manageable goal. The problems I had in practice with demonstrating this were that if you chose to be flashy and rolled your own nats (called, say, `xnat`) and then used `has_zero` and `has_one` etc, you might sometimes end up accidentally proving things about nat instead of xnat. So I defined `one`, `two`, `three` etc and I think `has_add` for `+` notation and then it was OK. Definitely don't open nat by the way ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/129530232):
To give you another data point, one of my sons is 16 and a BIO contender (and a strong python programmer for his age) and he worked through some of the basic exercises in Software Foundations and could manage them, so that would be another possibility, to construct some sort of a talk from that. But I think `xnat` is really good -- kids have an informal definition of addition for which commutativity is obvious, and I think it's a bit of an eye-opener to see that if you define it recursively then one of `a+0=a` and `0+a=a` is obvious and the other isn't.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Jul 12 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/129534379):
Thank you very much for this Kevin! I'll go ahead with `a + b = b + a`, warning not to open `nat` acknowledged! I'll read your blog post this week. A quick scan suggests this is something that's potentially re-usable, except of course I don't do tactics yet (and neither would the students!) so I'd probably want to rewrite everything using terms.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/129534576):
I think tactics are far far easier than terms! Especially for proofs by induction, which you'll be doing a lot of. In tactic mode your one goal becomes two and it's very clear what's going on. In term mode I think it gets a lot murkier with holes and stuff. This might of course reflect my background -- a mathematician with no computer science background. Two years ago I didn't know what a lambda was but I certainly knew what a function and a proof were.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Jul 12 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/129534659):
It's probably a backround thing indeed. I simply still haven't got round to learning tactics yet, as I figured I could do everything with terms. But I think I really should!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 12 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/129542534):
My blog post is an attempt to teach people tactics :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 07 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/131034789):
Thanks Kevin, I've worked through about half of the blog post. My high-level thought is that I must really learn tactics. No excuses. It's a better way to do things than terms (if slightly uncomfortable!).

If you'd like some low-level thoughts, I've taken some notes as I was going through your blog post. Feedback 2 and 5 I think might be particularly useful, you might want to ignore the rest:

```
-- 1. Feedback on the sentence: "Here’s the full code (together with some other stuff which you don’t need to worry about)."
-- I'd probably avoid using `open` for now. Every bit of new notation introduced is a new thing to learn and can distort the "bigger picture". Sure, typing xnat before everything is a pain, but they'll have plenty of time to learn all the shortcuts as they become more expert (i.e. after the first lesson).

-- 2. Feedback on the sentence: "Well no we can’t yet, because we haven’t defined add yet! Let’s add a definition of add. We’ll define it by induction! Well, more precisely, by recursion."
-- I'd like to see some verification/testing that my definition worked straight after the definition. For example something like this:
-- #reduce add (xnat.succ xnat.zero) (xnat.succ (xnat.succ xnat.zero))

-- 3. Feedback on the sentence "Well, more precisely, by recursion. The idea is that a+0 will just be a, and a+succ(b) will just be succ(a+b)."
-- I'm not sure how I feel about equation compiler. On one hand it makes everything look easy and is probably more beginner-friendly than recursors. On the other it is hiding quite a lot of seemingly important detail. It's a tought one!

-- 4. Feedback on the sentence "notation a + b := add a b"
-- same point applies as with `open`, but less strongly.

-- 5. Feedback on the sentence: "In fact there is an easier way — the tactic refl just unravels everything and then checks that you’re left with something of the"
-- Yes, the tactic works. Arguably an easier way to kill the goal would be without entering the tactic environment alltogether, `rfl` or `eq.refl _` or `eq.refl two`. But educationally what really matters is that all these proof strategies work because both `add (xnat.succ xnat.zero) (xnat.succ xnat.zero)` and `xnat.succ (xnat.succ xnat.zero)` reduce to the same term:
-- #reduce add (xnat.succ xnat.zero) (xnat.succ xnat.zero)
-- #reduce xnat.succ (xnat.succ xnat.zero)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/131036136):
Thanks Adam. I'll mull over your feedback!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 07 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/131045141):
```quote
-- I'm not sure how I feel about equation compiler. On one hand it makes everything look easy and is probably more beginner-friendly than recursors. On the other it is hiding quite a lot of seemingly important detail. It's a tought one!
```

That's an interesting point. I think there's a difference between something you should 
understand (or gain from understanding it) and something you need to understand. I think at first, you can think of definitions as nothing more than its definitions.

I just spent hours upon hours trying to reimplement the equation compiler for the definitions I generate. That's a lot of work. And not having those equations really makes your proofs ugly and cumbersome. 

I'm all for opening the hood of your car to look at the engine but you can learn to drive before doing that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/131045263):
In the lean summer school I tried to do both. In the mornings I would give lectures on the basics of dependent type theory and recursors and things and in the afternoon we would look at more practical lean features and more hands on stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 07 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/131045549):
That's an interesting choice. Did you find that one lesson informed the other?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/131045765):
Not too much, at least not in the short time I had available. It would take a good while before you would really be able to appreciate how the equation compiler works, but it is enough, I think, to dispel the aura of magic and disconnection between what lean does and the underlying theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/131045842):
Although I think that the basics of DTT come in pretty directly in the concrete syntax of proof terms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/131045858):
i.e. you have to have a decent grasp of lambda calculus to know how to write terms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 07 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/131045991):
That's true. Did you find the students had an easier time with tactic proofs than with writing their own proof terms?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/131046216):
I am not sure now that I come to think about it. Since we were working towards FAbstracts we didn't do too much proving, we focused more on typeclasses and structures

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 07 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/131047442):
>  have to have a decent grasp of lambda calculus to know how to write terms
I think I might be a counterexample to this statement. Or maybe I'm tricking myself into thinking I can write terms.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 13 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132045780):
So I've put together a workshop, which my students will be going through on Tuesday (tomorrow). I'd be very curious if anybody had any feedback!

http://projectgrasp.co.uk/lean-workshops/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 13 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132046276):
You said earlier that you assume your students have background in math and Python, right? Not necessarily functional programming?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 13 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132046309):
Correct.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 13 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132046346):
If that's the case, they'll be very confused at fist by lambdas, function types, and partial applications.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 13 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132046350):
None of them have done any functional programming.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Aug 13 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132046465):
Exercises 2.5 and 3.2 aren't showing up properly. I think you need empty lines after `.. code-block:: lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 13 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132046470):
Just the idea that you can write application `f a b` without parentheses feels strange at first to students in that position. I think you're going to have to go very slowly at the beginning.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 13 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132046472):
I was hoping they'll be able to get by with minimal understanding of any of these concepts

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 13 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132046495):
Thanks Rob, I'll have this in mind.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 13 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132046503):
Also, btw, "Lean" should be capitalized everywhere.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 13 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132046509):
OK, will fix.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 13 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132046541):
Capitalized but not CAPITALIZED :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 13 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132047043):
Thanks Bryan, that's now fixed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 13 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132047075):
Mario, is any of your summer school teaching material re-usable? Have the lectures been recorded?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 13 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132047202):
The lectures were recorded, but last I heard the institute had put the recordings on CDs and mailed them to Tom

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 13 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132048162):
Ah, OK. No hurry there, I'm trying to keep an eye on educational aspects of Lean. There's a module at Glasgow, 2nd year computing called "Algorithmic Foundations", and the course is mostly logic, some easy discrete maths, some graph theory, etc. And we've had some issues with student engagement in the past couple of years. I'm thinking of replacing some parts of this course with Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 13 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132048188):
Just to make it a bit more exciting.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 13 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132048200):
The high school kids are a kind of "test bed" for this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 14 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132112582):
```quote
Also, btw, "Lean" should be capitalized everywhere.
```
It makes me think of a question: where does the Lean name come from? Is this an acronym? Or is it only a short word that can be written using ∃ and ∀?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 14 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132113112):
I forget, but I'm pretty sure it's not an acronym, and the ∃∀ thing is post-hoc logo-making

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Aug 14 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132113273):
I think part of the story is that Lean is a suffix of Boolean; and Jeremy had previously worked on a theorem prover called Boole.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 14 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132113682):
```quote
I think part of the story is that Lean is a suffix of Boolean; and Jeremy had previously worked on a theorem prover called Boole.
```
Yep. Jeremy, Leo, and Cody Roux started working on a DTT-based system called Boole which, as I remember it, was supposed to be able to interface between various kinds of mathematical software. https://github.com/avigad/boole

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 14 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132113703):
When Lean started, it was going to be one of the components that could hook into Boole, or maybe the backend? I don't really know. In any case, Boole + Lean = Boolean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 14 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132113714):
Boole didn't go anywhere, Lean has stuck around, so we're left with the name.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Aug 14 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132114273):
so I should pronounce Lean as Le-an?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 14 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132114315):
Interesting story. Maybe I should pronounce it differently then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Aug 14 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132114679):
Nobody called it Le-an even when Boole was still a thing, so I think we're safe sticking with the normal pronunciation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 14 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132115659):
thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Leonardo de Moura (Aug 14 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132137220):
I chose the name "Lean" because I wanted it to be smaller and simpler than Z3.  Z3 has more than 500k lines of code, a lot of legacy code and is quite complex. The original goal was to build an automated reasoning library (Lean) for DTT. Then, use Lean in systems such as F-star, Coq and Isabelle. For example, F-star and Isabelle both use Z3, and we (incorrectly) assumed they would both benefit from a library of tactics and decision procedures for DTT. Isabelle/HOL does not support dependent types, but it would still benefit from better support for higher-order logic.
When Soonho and I started Lean, Cody Roux was developing Boole, and we suggested that Lean could *also* be used as a backend for Boole, and I pointed out that "Boole + Lean" is almost "Boolean", but the name was not chosen because it is a suffix of "Boole".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 14 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132137335):
Thank you very much for this explanation!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 14 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132137447):
If you have time I'd love to read more about the history of this project, what happened to the "incorrect assumption" about F and Isabelle, and when it became an autonomous project. But maybe this is already documented somewhere? It would be nice to have a little historical section on the home page.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Leonardo de Moura (Aug 14 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132138571):
@**Patrick Massot** The first issue is that there are many flavors of type theory. SMT solvers, like Z3, are based on first-order logic, and the semantics is very well defined. Since each system implements a different flavor of type theory, we encountered big mismatches between the logic implemented by the potential customers (F-star, Coq) and the one implemented in Lean. We tried to interface F-star and Lean twice using different approaches, and it was an encoding mess. F-star is based on extensional type theory, has subtypes,  etc. We also found mismatches between what is a valid inductive datatype in Lean and F-star. We didn't try to interface with Coq, but I imagine we would also have many problems: no universe cumulativity in Lean, Fix Coq expressions vs Lean recursors, lack of proof-irrelevance in Coq, etc.  Another issue is that it is much harder to build robust end-game automation for DTT.  Here "end-game" means, it proves the goal or fail.  Z3 is used as an end-game tactic in F-star and Isabelle. Moreover, the automation must be integrated with system specific features (e.g., type class resolution). Non end-game tactics are not very useful since we have the logic mismatch issue. For example, suppose we have a goal in F-star, convert it into Lean, apply Lean's `simp`, and try to convert the result back into F-star. The result goal will probably be unreadable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 14 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132138688):
Thank you very much!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 14 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132139278):
Coq doesn't have proof irrelevance?! How do they do anything?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 14 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132139370):
They have it as an axiom that you can include or not and you have to invoke it when you need it. In Lean, it is baked into the kernel so you don't need to do anything to use it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 15 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132141231):
@**Leonardo de Moura**: I met Yves Bertot a few weeks ago who expressed concern for the soundness of the Lean implementation because of how hard it has been for Coq team to avoid the many pitfalls of CIC. How do you address that kind of concern?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Leonardo de Moura (Aug 15 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132144904):
@**Simon Hudon** > How do you address that kind of concern?
We can tell him that
1) The Lean kernel is simpler (e.g., we don't have a termination checker).  One of the soundness bugs in Coq was in the termination checker.
2) We have 2 independent type checkers.
3) We have a notion of trust level in Lean. In trust level 0, we disable optimizations and extensions, and nobody managed to type check a proof of `false` in trust level 0 so far. 
4) We don't have coinductive datatypes in the kernel like Coq.
5) We don't have nested inductive datatypes in Lean 3. So, it is much easier to check the "positivity" constraint. One of the bugs in Coq was in this check. BTW, this is item is only true for Lean <= 3 since we will have nested inductives  in Lean 4.

We can also say that we had a few users (e.g., Cody Roux) that tried to reconstruct Coq bugs in Lean and failed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 15 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132145264):
Thanks for the explanation! I was also under the impression that the Coq kernel might need to change more frequently because more of its features are part of the kernel. Does that make sense?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Leonardo de Moura (Aug 15 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132146076):
@**Simon Hudon** It is hard to speculate. I think the main issue is that the Coq's kernel has evolved over time, and many features have been added much later. For example, universe polymorphism was only added a few years ago (< 5 years). It is also quite hard to maintain code that has been written by many different people. I don't want to speculate further, and I want to make clear that I have a tremendous respect by all Coq developers.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 15 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132146589):
```quote
I have a tremendous respect by all Coq developers.
```

And I can see why. I was at the DeepSpec summer school a few months ago. It's impressive how many allegedly impossible things were done in Coq.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 15 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132146710):
```quote
1) The Lean kernel is simpler (e.g., we don't have a termination checker). One of the soundness bugs in Coq was in the termination checker.
```

I've been wondering about that. Isn't the concern for termination shifted to the synthesis of the datatypes' recursors? And doesn't that make the recursor synthesis part of the trusted code base?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Leonardo de Moura (Aug 15 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132147054):
@**Simon Hudon** Recursors are well understood and have a well defined shape that guarantees their termination. We don't have to write any termination checker. We just have to make sure we produce the correct recursor. This is much easier than writing a termination checker that has to handle arbitrary definitions written by users.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 15 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132147427):
Lean really never ceases to amaze me. I can't wait to see what Lean 4 has in store.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 15 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132163624):
@**Adam Kurkiewicz** How was your workshop?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 15 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132164268):
Thank you for all this information Leo, I'm sure it's really interesting, just a little bit beyond me to make any useful comments.

So, about the kids, it went pretty well yesterday. The brightest have got as far as the end of chapter 3 of my tutorial (up to propositions as types + a little bit of playing around with equality, all with terms), pretty much by themselves, although of course with frequent hints from my side. This was after ~2 hours of workshop and they were pretty tired towards the end, so I walked them through chapter 4 (inductive types + recursors + commutativity of addition) on my own, lecture style. They've at least *seen it*, so if they decide to ever go back to this content, it will at least seem vaguely familiar.

I've made a couple of observations:

1. It came as a big shock to all of them that there were some technical concepts they couldn't grasp in a single sitting. That's understandable given that all of them are bright and all of them followed standard Scottish high school education (which is not exactly the world's most challenging).
2. Functional programming indeed proved to be a challenge, as predicted by @**Rob Lewis** and I didn't explain things as much as I should have. I received a standard array of question from pretty much every student, such as, what is a $\lambda$, why do I not have to type brackets, why is this not typechecking (when evaluating a function on a term of incorrect type), etc. I reverted to a series of half-truths and rules of thumb (you need one $\lambda$ per one arrow in your type signature, everything on the left of the colon is a value, everything to the right of the colon is the type, etc.)
3. Lean is great, because it gives me a topic I can talk with these kids, without the risk of complete cognitive disconnection, and I'm actually really enthusiastic about (as opposed to maths puzzles, or basic python programming, which I'm slightly less enthusiastic about).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 15 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132164276):
Thanks for asking @**Patrick Massot** :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 15 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132164358):
Oh and, of course, I think I've proven the point, at least to myself, that we could teach Lean to our 2nd year undergrads without the risk of spontaneous brain explosions :D. Now I just have to convince all the big fish in the department :).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joseph Corneli (Aug 15 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132175285):
@**Adam Kurkiewicz** are you planning to run the workshop again, or continue it?  I'm in Edinburgh, maybe I could come over to Glasgow and observe or help out?  Or perhaps we could figure out a way to run a similar workshop here?  Following the observations you listed: 1 (Technical concepts), 2 (Functional programming); 3 (Mutual interest), are you thinking to  revise the workshop materials?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 15 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132180027):
Hi Joseph, just to give you a little bit of background, this workshop was a part of a bigger initiative, called "project Grasp" that me, Dr William Petterson and Prof Quintin Cutts have run at University of Glasgow in collaboration with local high schools (Glasgow Gaelic School, Bearsden Academy, Glasgow Academy and Douglas Academy), and a local tech company, Skyscanner. This workshop was the only workshop to focus on lean, all the other classes looked at maths Olympiad problems, recreational mathematics, Python programming, and some software development (students built a slack chatbot, using mostly Amazon Web Services stuff: AWS Lex, AWS API gateway, AWS lambda (Python), etc.).

Happy to pass you some links to student presentations, workshops, etc. if you're interested.

2017/2018 classes are now finished (this workshop was the final class). We are currently discussing budgets and the class content for 2018/2019, talking to funders, etc. We're planning to restart the project late September/ early October next year.

Let's keep in touch about this, and I'm sure we can work something out. If you'd like to chat about this, I'm in Ediburgh for work this Friday, we could meet up at any point after lunch :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Adam Kurkiewicz (Aug 15 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132180224):
Yes, when we re-run the lean workshop next year, I'll fix it all up, but for now I'm happy to let it bitrot on github :). It's all Creative Commons though, so if you want it, just take it!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joseph Corneli (Aug 16 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Teaching%20lean%20to%20high%20school%20students/near/132229450):
Sounds like a great initiative!  I wonder if there's anything at all similar here in Edinburgh, or with my colleagues in Dundee.  I'll ask around.  Also will PM you about Friday afternoon!

