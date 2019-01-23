---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/81772RichStandardLibrary.html
---

## Stream: [general](index.html)
### Topic: [Rich Standard Library?](81772RichStandardLibrary.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Speee (Jul 14 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129671263):
I see that Jeremy Avigad boasts of a rich standard library in Lean here (pdf): https://leanprover.github.io/talks/stanford2017.pdf

For comparison, he notes a bunch of other theorem provers (like Coq and Isabelle) that have, among others, "elementary number theory, real and analysis, point-set topology, measure-theoretic probability, algebra, Galois theory" as part of their standard library.

I assume this is the case for Lean, but I couldn't find anything relevant using the search terms 'topology' and 'lean theorem prover'. I looked through lean/library on github, but it seemed to me very basic.

So is a more sophisticated library non-existent or just hard to find?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 14 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129671841):
https://github.com/leanprover/mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 14 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129671844):
The library's a bit smaller than Coq and Isabelle's libraries at the moment.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 14 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129673133):
To give an indication of a few things that are in Lean that might be harder to find in other theorem provers, Lean currently has localisation of commutative rings at multiplicative sets (definitions and universal properties), affine schemes (and also general schemes, although essentially nothing is proved about them), and I'm working on formalising the definition of a perfectoid space at the minute with some others here. On the other hand there are certainly still gaps in Lean's maths library. I think Coq has some basic representation theory and as far as I know we have none of that in Lean. I hope we're not too far from some basic Galois theory but it's not there yet. I am running a summer project with a bunch of undergraduates from Imperial College London where we're formalising random parts of our undergraduate syllabus. It's completely directionless in the sense that the students can just choose to formalise what they like, and many are doing problem sheets from basic courses but some are putting new definitions into Lean. Some students are working on basic homotopy theory for example. I'm hoping we'll do some group cohomology at some point over the summer, and I think we'll get the fundamental group within the next couple of weeks. Is there anything particular you're looking for? Lean is only a couple of years old but it seems to me that the maths library is growing much faster and in more interesting directions than the other provers you mention. I could be wrong though -- I know far less about what is going on in the other provers than what is happening in Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 14 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129673136):
Coq has the whole proof of Feit-Thompson

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 14 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129674924):
Sure! That's why it has some representation theory; my understanding is that the motivation to develop the representation theory that's there was for Feit-Thompson. But a lot of that huge Feit-Thompson proof can't really be used to do other things, at least that's my understanding of it -- it's just lots of technical lemmas about group actions and maximal subgroups etc which are used only to prove F-T. Of course one might use F-T to prove other things.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 14 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129674972):
Lean might have a statement of the local Langlands conjectures for tori. @**Kenny Lau**  -- does it have a sorry-free statement nowadays?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675103):
not really

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 14 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675370):
What needs doing? How hard is the absolute Galois group? We have existence of maximal ideal of a non-zero ring -- is constructing alg closure still a lot harder?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 14 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675384):
I just feel like there's a huge barrier although I can't tell you what it is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 14 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675436):
should we develop enough machinery so that we can prove that K1 is already algebraically closed?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 14 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675444):
structure theorem for inseparable polynomials: every polynomial f(x) is of the form h(x^(p^n)) where h(x) is a separable polynomial and p is the characteristic of the field, under the convention char Q = 1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675485):
8 definitions of a perfect field

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675488):
What's the point?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 14 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675494):
At the end of the day I am interested in a definition of the algebraic closure, not a tricky theorem about how it can be written in a different way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 14 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675498):
you wouldn't teach someone LCFT if that someone doesn't know what a separable polynomial is, that's the point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 14 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675500):
I am not so sure about that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 14 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675502):
there are plenty of people who only care about applications to number fields so assume char 0 everywhere

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 14 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675539):
"separable polynomial" was an example for more basic knowledge

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 14 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675542):
Oh I see.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 14 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675615):
Are you still working on the perfectoid project?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 14 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675659):
I've not even thought about it for the past two weeks -- I've been very busy with undergraduate level maths. I'd really like to get back to it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 14 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675664):
Today I had two hours to kill so I spent some time on my book. I just have more Lean projects to do than there are hours in the day at the minute.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 14 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675667):
[2018-07-15.png](/user_uploads/3121/WdfDkyjA-qgtr9SE-ysIitcY/2018-07-15.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 14 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675668):
I understand you've been busy. I'm only asking if you still want to pursue this or prioritize other projects

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 14 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675669):
and as for me, I'm now half way through

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 14 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675671):
(never mind, I can't maths)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 14 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675710):
I'm *almost* half way through

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 14 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675714):
half way  through what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 14 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675715):
My last hold-up was that I needed to prove several definitions of valuation were equivalent, and then discovered that we didn't even have quotient rings and that R/P was an integral domain if P was prime.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 14 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675716):
Atiyah-Macdonald

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 14 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675718):
I definitely want to pursue it and I saw your work on completions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 14 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675721):
Reading or formalizing Atiyah-Mcdonald?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 14 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675722):
reading

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 14 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675724):
unfortunately

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 14 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129675774):
Ok. Hopefully I'll work more on completions. It should be doable and not too long

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 15 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129709863):
the point is that we have two definitions of a separable extension:
1. the usual one
2. the one involving tensor products
and one of them is more useful than the other, but one of them is quicker to define

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 15 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129709866):
the point is that you don't want to just define a bunch of stuff and rush the goal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Speee (Jul 17 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129837392):
Thanks! So given the relative poverty of the library, what are some reasons to choose lean for my formalizing needs anyway?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 17 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129837461):
That would depend very much on your formalizing needs I guess. I use it because it's fast, it has a cool community here, and the unicode looks good so mathematicians find it less scary

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 17 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129837707):
In what sense relative poverty? Are you coming from a particular theorem proving community?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 17 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129837712):
Yeah, we're the only guys with schemes :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 17 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129837739):
I'm concerned that Speee is referring to the core lib which is quite impoverished but is far from all there is in lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Speee (Jul 18 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129838324):
I do prefer readability most of all (and Lean shines here), but I could use a mature library to compare my own attempts against. It's nice to see an active community though, as that can provide the kind of feedback I'm looking for!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Rich%20Standard%20Library%3F/near/129838358):
I don't know how mathlib rates on maturity, but there is certainly more than enough for comparing your own work against

