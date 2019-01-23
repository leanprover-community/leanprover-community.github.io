---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/20828HalesreviewofLean.html
---

## Stream: [general](index.html)
### Topic: [Hales' review of Lean](20828HalesreviewofLean.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134182451):
Johan mentioned this but I thought it deserved its own stream. I would like to hear the community's response to the negative points.

https://jiggerwit.wordpress.com/2018/09/18/a-review-of-the-lean-theorem-prover/

I am not too bothered about the steep learning curve (point 3). This will change over time as more documentation becomes available. There are sporadic counterexamples to Tom's claim, e.g. @**Edward Ayers** and others seem to have managed well just by asking questions (and indeed I guess technically I am not in any of the categories Hales mentions either, although it did take me a year of my life and I'm still not very good at it).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134182648):
As for 9 (diamonds), I know that Chris was finding these extremely frustrating and he was just goofing around with finite sets.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 18 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134182959):
I think the story with diamonds is: there are workarounds, but they aren't particularly natural and you almost certainly won't get it right on your first attempt.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183534):
Does anyone know what libraries are alluded to in Point 2: "Lean 3 broke the Lean 2 libraries, and old libraries still haven’t been ported to Lean 3. "?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183676):
Chris' struggles were particularly vacuous -- my understanding was that he would end up with two instances of a subsingleton which were not defeq and it would break type class inference.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Sep 18 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183691):
I read over his negative points, but I don't see how they could be (1) fixed, or (2) fixed in a way that doesn't make another set of tradeoffs somewhere else down the line

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183751):
Well of course this is a perfectly valid point. One can take any thing, however wonderful, and list all the ways it could be even more wonderful, including problems which are basically known to be impossible to fix.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183800):
I think Simon and Sean are working on point 4 (software engineering library)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183854):
I sympathise with Hales' point 10 -- I did find it a bore during my brief dalliance with topological rings, that I had to write `ring` and `topological space` and `topological ring` everywhere. And it's absolutely true that one wants to take completed tensor products of topological modules when doing adic spaces.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183890):
Is (8) fixed by these `additive` and `multiplicative` tricks, to a large extent?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183893):
I think "It seems to me that a system designed for doing mathematics should do more than just declare them illegal." is Tom misunderstanding Lean's main goal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183971):
Is point 7 (Ugly projection chains are required.) a problem in real situations?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134183998):
Of course 9, 10 and 11 are real problems, but I have no idea how to fix that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134184650):
About point 10, why can't we define `topological ring` in a single line using class and extends?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 18 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134185611):
I think it would be useful to separate the pain points from the points of annoyance.  Point 10 seems to me to be a point of annoyance. In mathematics, you can underspecify your constructions. You can parameterize your constructions and say "the reader knows what I mean here". In formal language everything needs to be completely specified which is bound to cause annoying verbosity. Coq chooses to parameterize constructions using functors and modules which can make modules simple but their use complicated. Lean's adoption of type classes can make the specification of your mathematical concepts a bit more verbose but using them is extremely unintrusive.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134185782):
It's comments like this from the CS side which I was really hoping to elicit. Thanks Simon (and Mario!)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 18 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134185871):
You're welcome! I'm glad this is welcome. I sometimes have a hard time stopping myself for ranting and wouldn't want to annoy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 18 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134186077):
I'm really tempted to shrug off all those down sides to be honest. 

His point 1. about being bloated doesn't make sense to me. Bloated compared to what? HOL-light? Isabelle? The logic aren't the same so it's hard to meaningfully compare. Compared to Coq? Absolutely not. Lean exorcised features like termination checking, coinductive types and pattern matching from the kernel to great benefit.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 18 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134186310):
I also wondered how many of these cons were disadvantages of Lean compared to other theorem proving systems, versus just "formal methods are hard".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 18 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134186744):
Actually point 10 about bundling and unbundling is the item on this list which has caused me the most grief

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 18 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134186891):
```quote
Actually point 10 about bundling and unbundling is the item on this list which has caused me the most grief
```
Do you know if other provers address the problem better?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 18 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134187062):
Nope, and I don't really have any idea what a better solution would look like.
I guess a general method for unbundling is "a [type-with-structure] whose underlying type is equal to [T]", so I guess better support for handling equalities would ease the pain. (For example, I saw some slides about some theorem proving system whose name I forget in which if you had a proof of `p = q` in scope, then the types `p` and `q` would unify. I guess GHC works a bit like this as well. It has its own complications.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 18 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134187064):
```quote
I also wondered how many of these cons were disadvantages of Lean compared to other theorem proving systems, versus just "formal methods are hard".
```
Good question. And I think the comparison can be broken down into two parts: 

1. for someone who's about to start a short term project, is Lean a good choice?
2. if you're willing to contribute libraries or other infrastructure, is Lean a good prover to invest in?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 18 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134187072):
I think it should be noted that Tom Hales is someone who has years and years of experience both as a user of theorem provers and as a "regular" research mathematician. This is not just someone listing a couple of annoyances. There probably is quite a lot of thought and experience behind this critique.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 18 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134187984):
That's actually the angle that I'm trying to take and I think that's the reason why we should look closely at the list. Individually, we may miss nuggets of insight but I'm hoping a discussion like this can dig them out.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 18 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188213):
> Does anyone know what libraries are alluded to in Point 2: "Lean 3 broke the Lean 2 libraries, and old libraries still haven’t been ported to Lean 3. "?

I think Tom is wrong on this point. While it's true that we never actually ported the lean 2 libraries, they have been "morally" ported, and the reasons for not porting directly have more to do with the change in management and design decisions than backwards incompatibility on the part of lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188283):
When Lean 4 hits, if it has no simplifier, am I right in thinking that porting mathlib will simply wait until it does?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 18 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188292):
more or less

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 18 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188308):
mathlib will live wherever it is most well supported

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188311):
Do you know why mathlib takes so long to compile?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188322):
or more precisely why it takes so long for some people?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188329):
For me it's fine but i have a relatively new machine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 18 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188412):
There are a lot of culprits to point at. Extensive use of tactics and slow elaboration are probably the main factors, if we're talking about compilation from scratch

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188432):
Can we fix slow elaboration with cunning instance definitions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 18 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188453):
Not really, at least not without sacrificing something far more important

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 18 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188496):
that's something that needs to be tackled on the core side

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 18 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188501):
and I don't even know if it can be improved

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188512):
https://github.com/kbuzzard/lean-perfectoid-spaces/blob/f9e9bf90003f6a2b82196e60da0b14cc57c90c44/src/valuation_spectrum.lean#L17

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 18 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188526):
but we've all seen examples of simple `exact` proofs that inexplicably take several seconds

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188531):
Why did Patrick have to `set_option class.instance_max_depth 41`?
`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 18 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188548):
that's a good question to ask Patrick

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188564):
Is that related? Is thjs "exact proofs take several seconds" phenomenon understood?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 18 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188576):
not by me, not really

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188622):
There was one that came up the other day, maybe Kenny had something which took 4 seconds and changing the elaboration strategy fixed it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188674):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/why.20is.20this.20slow.3F

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 18 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188678):
yes, that's the sort of thing I'm talking about

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 18 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188693):
I'm pretty sure that there are several borderline proofs in mathlib that are just taking a long time to elaborate

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 18 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134188757):
when you multiply that by thousands it starts to contribute to global warming

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Sep 18 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134189015):
out of curiosity if I wanted to write a tactic could I write it in C++ (like Coq does with OCaml?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Sep 18 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134189041):
maybe a better question is: can I compile it into a library and dynamically link to it at runtime?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134189046):
I think you have to write it in Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134189098):
but only because I've never heard anyone else talking about or doing this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 18 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134189940):
I also wondered whether Lean has some kind of FFI.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 18 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134190001):
I think there is such a thing as a "Lean extension" but I don't know anything more about that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 18 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134190057):
I don't see any reason why Lean couldn't adopt a Haskell-style FFI to C

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 18 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134190085):
I wonder what sort of existing libraries Tom Hales wants to use (or uses, in HOL light)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 18 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134190267):
I think a proper FFI is planned for Lean 4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 18 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134190785):
If you want to write a tactic which uses a linear programming solver as an oracle, then a simple FFI is enough. If you want to write "simp, but different" in C++ (for performance or familiarity) then you need direct access to Lean internals.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Sep 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134218109):
About a year ago when I first saw Lean (at the big proof conf) I had similar reservations.

I agree that the language is difficult to learn. There is just a lot of syntax and it is hard to tell if a piece of syntax is fundamental or just sugar. Some of the attributes do magic syntax things that aren't documented.  But the syntax is _way_ easier than Isabelle's.

I think that Lean has a chance of taking off because it is relatively simple and there is a strong focus on tooling support and because it is a fresh start that doesn't have to be backwards compatible.
Eg the Isabelle source code is an intimidating sprawl of different projects and languages. 

Complaining about a lack of library support is an inevitable complaint. Libraries for a new computer language always have to start somewhere. I also believe that the ultimate goal of interactive theorem proving should be that writing up a new mathematical theory in a formal system should (in the future)  take about the same amount of time as writing rigorous, informal notes. Formalising a theory for oneself, even a simple undergraduate one, is an extremely powerful way of learning about that theory. So I believe that mathlib should be more of a book of examples and standardisations that you can use to code up your own formalisations, rather than a monorepo of truth.

With the typeclass complaints (7 to 11), I have just come to accept that this is always a total nightmare no matter what system you use. Humans are very good at looking at (their own, internal) typeclasses and rapidly bundling, unbundling, identifying obvious coercions, diamonding, finding isomorphisms and so on. Computers need these spelled out to them, so libraries get cluttered with typeclass-plumbing lemmas. Oh well.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134218516):
```quote
 So I believe that mathlib should be more of a book of examples and standardisations that you can use to code up your own formalisations, rather than a monorepo of truth.
```

I need to have my monorepo of truth because the sooner we can start saying "Look! We have a complete definition of perfectoid spaces! Look! We have a complete formulation of Langlands functoriality! Look! Here are the 6 Clay Problems which are actually mathematics!" the sooner mathematicians will sit up and take notice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134218564):
I regard this as extremely high priority.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134218579):
I also, this time just for personal reasons, want to be able to say "Look! Our students are demanding problem sheets are set in Lean and you can't do that for them because you don't know it" to my colleagues, but I have a longer time frame for that goal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134218654):
I think the book of standardisations and formalisations is something else. What would you imagine it looked like? No way are we going to get mathlib to define a compact space as "every open cover has a finite subcover" because they have their reasons for using filters etc. However we are equally unlikely to get the 2nd year metric spaces and topology person to switch to using filters, because most mathematicians never need them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134218666):
@**Edward Ayers** tell me more about what you want. I have a bunch of undergraduates who are currently writing code which has nowhere to go.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Sep 19 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219095):
The main thing that I want (and am working on) is automation that is good enough that one doesn't need to clutter ones theory file with lots of lemmas that you wouldn't put in a maths textbook.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Sep 19 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219289):
I think it is critical to get formal documents to have the same terseness and readability as informal mathematics.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219315):
Let's just say that in 5 years' time you get funded for some proposal to write an undergraduate mathematics textbook in Lean, and you have to prove that a compact metric space is complete.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219331):
You look at mathlib and discover that there is already a proof in there, probably in the generality of pseudo-compact semi-metric spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219376):
and the proof is unreadable, and intended to be unreadable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219411):
Is the idea that you prove it again, using the standard filter-free proof presented to undergraduate mathematicians, and underlying it all is a really good interface which people have written so that it now reads like the maths proofs which I present to undergraduate mathematicians in lectures?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219477):
If you did that, it would teach mathematicians how to use Lean I guess. But the proof will still be in mathlib and terse and incomprehensible, and devs would rather use the mathlib proof than the proof in the book.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219483):
I'm just trying to understand how all this fits into the scheme of things.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Sep 19 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219485):
Yes the result in the library isn't good enough because it is over-generalised. It doesn't have to be in Latex and be all fancy, and the argumentation doesn't have to be exactly the same as how it is done in lectures. But it has to possible to follow the argument without unpacking lots of more general theories.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219490):
So your goal is a *readable proof*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Sep 19 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219546):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219550):
I must be honest, I do not really understand enough about library maintenance to know why mathlib prefers what one might call "obfuscated proofs".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219560):
But I have no doubt that they have good reasons.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Sep 19 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219564):
It has to be a proof where you can read it and be able to see how to make similar arguments yourself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219576):
And I want to conclude from this that your readable proofs will not actually be useful in terms of library-building, for some reason that I don't understand but am arguing must exist

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219628):
On the other hand it seems to me that your readable proofs will be essential for teaching mathematicians how to use formal proof verification systems.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Sep 19 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219636):
If you use the obfuscated approach I think you can save time because you only have to prove the super-general case.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219661):
```quote
It has to be a proof where you can read it and be able to see how to make similar arguments yourself.
```
I specifically tried to write the definition of a perfectoid space in such a way that a mathematician who knows 0 about theorem provers and look at the code and think "oh yeah, I can see that this might well be a definition of a perfectoid space"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Sep 19 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219666):
It depends on what you want the library to do I guess.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219678):
but I made no attempt to do so for some of the earlier files because I have dreams of getting at least some of this stuff into mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219682):
```lean
/-- A perfectoid ring, following Fontaine Sem Bourb-/
class perfectoid_ring (R : Type*) extends Tate_ring R :=
(complete : is_complete R)
(uniform  : is_uniform R)
(ramified : ∃ ϖ : units R, (is_pseudo_uniformizer ϖ) ∧ ((ϖ^p : R) ∣ p))
(Frob     : ∀ a : Rᵒ, ∃ b : Rᵒ, (p : Rᵒ) ∣ (b^p - a))

class perfectoid_space (X : Type*) extends adic_space X :=
(perfectoid_cover : ∀ x : X, ∃ (U : opens X) (A : Huber_pair) [perfectoid_ring A.R],
(x ∈ U) ∧ is_preadic_space_equiv U (Spa A))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219742):
Mathematicians who know this area know that a perfectoid ring is a complete uniform ring satisfying some axioms, and that's what they see here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219756):
But if they look at the definition of complete, they see filter hell

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219775):
So you see, I am trying to conform to mathlib's aims in some places and your aims in others.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134219948):
But in general I am very unclear about why Larry is so keen on human-readable code and given that mathlib is run by people who seem to know what they are doing, and who are intentionally accepting highly minimised code which is not at all optimised for readability, there are presumably arguments for both styles. Can I deduce from what you're saying that there should be a place for both?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134220322):
```quote
But if they look at the definition of complete, they see filter hell
```
That's actually a bad example. Uniform spaces are needed for topological rings (we can't assume the topology is metrizable here)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134220635):
```quote
Why did Patrick have to `set_option class.instance_max_depth 41`?
```
Because it won't compile with depth 40. Of course it almost certainly doesn't mean that one successful search has depth 41. Most likely it means Lean needs depth 41 before giving up on a bad idea and starting to backtrack. So what seems needed is a way to block stupid ideas in type class search. But this is clearly something for Leo and Sebastian to think about, we can't do anything about that (the same thing applies to the thread discussing proof cache yesterday, it's a bit ridiculous to discuss this as if Leo never thought about its...)  In the mean time we could try to carefully craft type class shortcuts in this specific case.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134220691):
complete rings: Yes that is true. But in general I guess one could do a "case study". Ed gets hold of some second year metric spaces and topology lecture course, and tries to write down the course *exactly as the lecturer wrote it* and see how much of it he could get Lean to swallow, filling in all the auxiliary boring stuff with the `by undergraduate_mathematician` tactic.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134220693):
@**Kevin Buzzard** Why Larry is so keen on human-readable proof, and why we don't have them in mathlib:
Isabelle's language (called Isar) was always intended to produce human readable proofs. A lot of document generation around it allows to produce TeX-documents. The automation is geard towards it. And type inference is much easier in the simple typed setting of Isabelle.

One important part in readable formal proofs is to repeat the statements you want to prove. But in DTT this is much harder, as type inference often fails, and the user needs to provide more information (or needs to add type class information `letI` and co). In Isabelle this is often not necessary. There, it is much easier just to copy your statement and it just works, without adding additional typing informations. Of course, this is all at the cost of a much simpler type system.

At least this is for me a reason, why I don't use `have` etc as much as I did in Isabelle. Also Isabelle has more automation like `auto` and `sledgehammer`, where it makes sense just to say what you want to prove, without stating how it is proved.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134221026):
```quote
I think it should be noted that Tom Hales is someone who has years and years of experience both as a user of theorem provers and as a "regular" research mathematician. This is not just someone listing a couple of annoyances. There probably is quite a lot of thought and experience behind this critique.
```

Yes, we need to be careful not to become a fanboy community. Everybody here love Lean, but it doesn't mean it can't be criticized. I've seen this with the Blender3D community, and I think it's pretty dangerous. And we can actually act on some of these bad points, especially the learning curve and libraries part. Of course many things are beyond our control, but I'm sure Leo will read it at some point, and although he probably knows all this, he may still get something out of it (but I'm afraid many things are very difficult to "fix" without breaking something else).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134221352):
Ed's comments make me think that he might be better off using Isabelle

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134221353):
on the other hand it would be wonderful to do this sort of project in Lean for teaching purposes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Sep 19 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134224649):
Don't make me go back to Isabelle!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 19 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134224759):
:-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Sep 19 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134225432):
More seriously,
I don't quite agree with @**Johannes Hölzl**  about readability.
Firstly, most of the time you can avoid the 'dependent' part of DTT and write out proofs in the same way as Isar without too many problems.
There is no reason why Lean can't have automation like sledgehammer and auto, it is just that Isabelle has been around longer.

Readability for me doesn't mean that it pretty prints to Latex and has plain english keywords. It means that what is written maps cleanly to an explanation at a level that a human would give.

Perhaps a good example is

``` lean
protected lemma add_comm : ∀ n m : ℕ, n + m = m + n
| n 0     := eq.symm (nat.zero_add n)
| n (m+1) :=
  suffices succ (n + m) = succ (m + n), from
    eq.symm (succ_add m n) ▸ this,
  congr_arg succ (add_comm n m)
```
This would not look good in a maths textbook, but once you take time to understand the syntax, it matches what a human would write:

> Induct on `n`. In the zero case we have `n+0=0+n` which we proved in `nat.zero_add`.
> In the `m+1` case, it suffices to prove `succ (n + m) = succ (m + n)` since we have
> ` ∀ (n m : ℕ), succ n + m = succ (n + m)`. But then we are done since `(n+m)=(m+n)` by the induction premiss.

The proofs are totally different syntactically but they both share the same skeleton and go in to (roughly) the same level of detail. That's what I mean by readability.

So my complaint with mathlib is that often the lemmas and definitions will sometimes deviate from the level of explanation that a mathematician is after.
Either spelling out simple lemmas that a mathemematician would not bother with, or appealing to some mysterious general lemma. 

I think a good example of this is defining the lattice structure on filters using galois connections in mathlib (in `filter.lean`). Here, we take advantage of a general theory to define a lattice structure. But then if you read the code, after this we have to use `original_complete_lattice.copy` because we want non-general definitions of join and meet. So using the general theory introduced a lot of plumbing that makes it hard to follow.  (apologies to the authors of that file, I am not trying to be a  jerk and I don't have a better way of solving this)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Sep 19 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134225517):
Perhaps that's not a good example, I don't know how the lattice structure on a filter would be introduced in a maths textbook.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Sep 19 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134225948):
Isar syntax doesn't meet this definition of readability because you will often have to write out vastly more steps than a textbook proof would need, even with the help of Isabelle's powerful automation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134226390):
With readable I don't mean that it resembles readable English text. What I mean is that it is readable without looking at the tactic output. This is not only a technicality: When we have control how the proof is represented why have more control how to guide a user through the proof. Maybe we can call this **explicit** proofs?!

Your example of `add_comm` is an exception in mathlib. Often one wouldn't write the `suffices`. so the (second) central part to understand the proof is missing. The main part, the induction, is luckily easy to see.

Another difference is that Isar doesn't have a very powerful tactic mode (at least nothing comparable to Lean's). So people are much more eager to write down `have` with repeating a similar statements. This again helps a reader going through a proof and reading it. 

I also hope that Lean will have in the non to distant future tactics similar to auto (tidy is a good candidate) and sledgehammer. But we will see if people start writing more explicit proofs.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hales%27%20review%20of%20Lean/near/134226465):
I think currently it is not possible to find a theorem prover were you don't need to write vastly more steps than a textbook proof would need. Hopefully somewhere in the future this is possible. But we are far from this.

