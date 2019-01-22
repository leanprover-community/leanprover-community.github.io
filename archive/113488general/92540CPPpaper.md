---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/92540CPPpaper.html
---

## [general](index.html)
### [CPP paper](92540CPPpaper.html)

#### [Rob Lewis (Oct 16 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135887180):
I'm submitting a paper about the p-adics and Hensel's lemma to CPP. If anyone is interested in taking a look, the paper is here: http://robertylewis.com/padics/padics.pdf I'm happy to hear any comments before or after the submission deadline on Thursday!

#### [Rob Lewis (Oct 16 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135887286):
By the way, CPP (https://popl19.sigplan.org/track/CPP-2019#) is one of the main venues for publishing about formalizations. ITP (http://itp19.cecs.pdx.edu/) is another.

#### [Kevin Buzzard (Oct 16 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135887709):
I am really interested in this idea and in the CS culture in general. Mathematicially you have done something which is 100 years old so the new ideas are not there. In computer science I would *imagine* that you are not the first person to formalise Hensel's Lemma. Am I wrong about this? And even if someone else had done it in Mizar in 2009 or whatever -- would this matter? I am trying to work out which notions of "value" a potential referee would attach to a paper such as this.

#### [Kevin Buzzard (Oct 16 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135887744):
Obviously I ask because if I get the schemes repo and/or the perfectoid repo into shape then I will be thinking about the same sort of thing, but I have no idea how it works.

#### [Kevin Buzzard (Oct 16 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135887824):
I see -- in section 6 you are perhaps claiming that as far as you know, Hensel's Lemma for the p-adics has not ever been done before.

#### [Johan Commelin (Oct 16 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135887905):
@**Rob Lewis** Typo in section 6. You write "Metmath"

#### [Johan Commelin (Oct 16 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135887919):
Also, congrats with the draft :wink:

#### [Kevin Buzzard (Oct 16 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135887927):
If I were supervising a Masters student who wanted to do something involving Hensel's Lemma I would have told them to prove it for an arbitrary complete DVR and then prove that the p-adic numbers are a complete DVR. The fact that this machinery is not in Lean somehow makes this less convenient. Yes, let me also congratulate you on the draft :-)

#### [Kevin Buzzard (Oct 16 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135888115):
The philosophy here is that proving Hensel's Lemma for the p-adics is a way of putting the library through its paces. How did you get the status of Hensel's Lemma in all the gazillion other proof assistants? Presumably I'll have to do this with schemes one day.

#### [Johan Commelin (Oct 16 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135888233):
```quote
Presumably I'll have to do this with schemes one day.
```
I think that is a lot easier. I'm pretty sure nobody has done that before. (Although I've seen slides by Coquand on constructive algebraic geometry. But that didn't do any sheaves. It just defined `Spec A` as a locale [~~ `open_set`].)

#### [Rob Lewis (Oct 16 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135888258):
The expectation for this kind of paper is that the subject hasn't been formalized before, or that you've formalized it in a novel and interesting way, and typically that it's part of some broader project. It isn't novel math, but it's a novel formalization, that shows off features of Lean and mathlib, that's a building block for work we plan to do in the future. And of course there's no guarantee that it gets accepted!

#### [Rob Lewis (Oct 16 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135888317):
@**Johan Commelin** Thanks, fixed :slight_smile:

#### [Rob Lewis (Oct 16 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135888347):
There aren't really a gazillion other proof assistants to check. It's easy enough to see what's in the Isabelle AFP, Mizar MML, and HOL Light library, they're all pretty self-contained.

#### [Rob Lewis (Oct 16 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135888401):
Coq is trickier since it's a bit more fragmented, but Google "p-adic numbers coq" or "hensel's lemma coq" turns up what exists.

#### [Kevin Buzzard (Oct 16 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135895307):
```quote
There aren't really a gazillion other proof assistants to check. It's easy enough to see what's in the Isabelle AFP, Mizar MML, and HOL Light library, they're all pretty self-contained.
```
Maybe for you -- it sounds a bit scary to me! I can't even read mathlib, and that's in a language that I kind-of know! Have schemes or perfectoid spaces been done before?

But your message answers my question very well -- thanks. I saw that someone had a paper or some sort of a write-up at least on formalising localisation of a ring in some other theorem prover and my first thought was "Kenny did that in Lean when he was a first year undergrad". If you want to explain another reason why it's part of a broader project, you can say that it's part of the 4th year undergrad curriculum at Imperial College London (p-adic numbers and Hensel's Lemma are part of the elliptic curves course, which I designed about 15 years ago) so they're an essential part of my plan to digitise the entire pure maths curriculum! And anyway, this universe is so real-number-centred and I've never understood why, the p-adic numbers are just another completion of the rationals, I don't know why we don't teach them to schoolkids.

#### [Rob Lewis (Oct 16 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135895805):
```quote
Have schemes or perfectoid spaces been done before?
```
I strongly suspect that they haven't. A quick look at Google doesn't turn up anything relevant for perfectoid spaces. This is a new and deep concept, if it's been formalized it won't have been done silently. Schemes are harder to search for because the word is used another way in logic, but I don't see anything at a glance.

#### [Rob Lewis (Oct 16 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135895866):
http://fm.mizar.org/fm.bib is a quick way to search through the Mizar library. https://www.isa-afp.org/topics.html to see significant developments in Isabelle, although not everything done in Isabelle is there.

#### [Rob Lewis (Oct 16 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135896017):
https://github.com/math-comp/math-comp is maybe the most likely place to find these sorts of things in Coq, and you can use the normal GitHub search there. But there are other unconnected Coq libraries.

#### [Kevin Buzzard (Oct 16 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135896096):
Thanks so much for the algorithm Rob!

#### [Rob Lewis (Oct 16 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135896164):
Just remember it isn't a decision procedure!

#### [Tobias Grosser (Oct 16 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135909496):
Very nice!

#### [Tobias Grosser (Oct 16 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135909524):
Does it make sense to reference the git hash of mathlib/lean version u are using in the paper?

#### [Tobias Grosser (Oct 16 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135909795):
Also, I spend some time reading about math yesterday to learn about p-adic numbers. So your paper comes at a very convenient point.

#### [Tobias Grosser (Oct 16 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135909805):
Put it already on my reading list.

#### [Tobias Grosser (Oct 16 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135909833):
I already have one question: "AFAIU 2's complement representation used to represent numbers in computers is a special case of p-adic number, right?"

#### [Tobias Grosser (Oct 16 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135909907):
Does your representation require p to be prime?

#### [Tobias Grosser (Oct 16 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135909967):
I wonder if existing decision procedures for Presburger arithmetic could apply directly to p-adic numbers or if instead one would need to explicitly model the "wrapping" using existentially quantified variables over a domain ```\mathbb{Z}```.

#### [Kenny Lau (Oct 16 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135910024):
nothing uncountable can be decidable

#### [Tobias Grosser (Oct 16 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135910072):
OK, I need to understand this in more detail.

#### [Tobias Grosser (Oct 16 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135910141):
Likely p-adic numbers in full generality may be undecidable, but the special case of 2's complement representation used on computers is certainly decidable.

#### [Tobias Grosser (Oct 16 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135910171):
I am not sure what the delta is in between.

#### [Tobias Grosser (Oct 16 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135910585):
http://www.numericana.com/answer/p-adic.htm

#### [Tobias Grosser (Oct 16 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135910590):
Explains how two's complements in computers related to p-adic numbers.

#### [Kevin Buzzard (Oct 16 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135910715):
The problem is that a 2-adic number is an infinite string of 0s and 1s

#### [Kevin Buzzard (Oct 16 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135910764):
so just like the reals there's no way to decide if two 2-adic numbers are equal because you don't know whether they're going to be different at the term after you got tired checking

#### [Tobias Grosser (Oct 16 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135910916):
Right. So in computers we always have finite lenght integers, such that after bit 32 all outer bits are dropped, aka assumed to have the same value than bit 32.

#### [Kevin Buzzard (Oct 16 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135910935):
that would be like doing real numbers to 32 significant figures

#### [Tobias Grosser (Oct 16 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135910979):
Right.

#### [Tobias Grosser (Oct 16 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135910997):
That should then be trivially decidable, afaiu.

#### [Kevin Buzzard (Oct 16 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911019):
so your system sounds more like $$\mathbb{Z}/2^n\mathbb{Z}$$ where $$n$$ is the number of bits you want to spend storing your numbers

#### [Kevin Buzzard (Oct 16 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911056):
but the 2-adic integers are the limit of these things -- the projective limit, if you're a mathematician -- as $$n$$ goes to infinity.

#### [Tobias Grosser (Oct 16 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911117):
I see.

#### [Tobias Grosser (Oct 16 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911160):
AFAIU Z/2^n Z gives just positive numbers

#### [Tobias Grosser (Oct 16 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911193):
2's complement representation allows to reason about positive and negative numbers with one bit indicating the sign and n-1 bits indicating the value.

#### [Kevin Buzzard (Oct 16 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911244):
but that bit which indicates the sign is just disappearing off to infinity in the limit, and disappears completely by the time you got there

#### [Kevin Buzzard (Oct 16 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911277):
The CS model isn't a very good one for understanding the 2-adic integers. You could think of it as an infinite string of bits, and at some point you're hoping that you'll be told what the sign is, but actually you never get to that information.

#### [Tobias Grosser (Oct 16 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911368):
Is the reason that towards infinity the digits might switch from 0 to 1 and vice versa?

#### [Tobias Grosser (Oct 16 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911387):
So only if you know that all what is left is an infinite sequence of '0' and '1' you know the sign, right?

#### [Johan Commelin (Oct 16 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911421):
No, there is no notion of positivity for `p`-adics. This is one of the main "problems" in arithmetic.

#### [Kenny Lau (Oct 16 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911489):
so we can represent each 2-adic integer as a sequence (A, BA, CBA, DCBA, EDCBA, ...) where each letter is 0 or 1.
-5 would correspond to (1, 11, 011, 1011, 11011, 111011, 1111011, ...)

#### [Kenny Lau (Oct 16 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911509):
5 would correspond to (1, 01, 101, 0101, 00101, 000101, 0000101, ...)

#### [Kenny Lau (Oct 16 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911543):
and you can write them more compactly as ....1111111011 and .....000000101

#### [Kevin Buzzard (Oct 16 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911546):
The problem with saying "we can define the sign if it's all 1's from here" is that you've only defined the sign on 0% of the 2-adic numbers.

#### [Kevin Buzzard (Oct 16 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911560):
For a general 2-adic number there is no good notion of sign

#### [Kenny Lau (Oct 16 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911565):
but a dense set :P

#### [Tobias Grosser (Oct 16 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911576):
In CS, we are only interested in this finite subset of the p-adic numbers, I feel.

#### [Kevin Buzzard (Oct 16 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911615):
(i.e. not one which is continuous, or which has basic algebraic properties etc)

#### [Tobias Grosser (Oct 16 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911630):
Probably the concept is way too general for what I would like to use it for.

#### [Kevin Buzzard (Oct 16 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911652):
Modelling an abstract mathematical object like the reals by a concrete CS type such as a `float` means that you lose information (as far as we are concerned). In applications this might not be an issue, but in maths it is.

#### [Tobias Grosser (Oct 16 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911674):
Sure, I don't want to squeeze all 2-adic numbers in fixed-size integers.

#### [Tobias Grosser (Oct 16 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911679):
This is hopeless.

#### [Mario Carneiro (Oct 16 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911733):
The two's complement representation of an integer coincides with its 2-adic expansion as $$\mathbb Z$$ embedded in $$\mathbb Z_2$$

#### [Tobias Grosser (Oct 16 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911756):
I see.

#### [Tobias Grosser (Oct 16 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911761):
Thanks @**Mario Carneiro** for explaining this.

#### [Kevin Buzzard (Oct 16 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911764):
Just like you can't squeeze all real numbers into 32 bits. But here is a consequence -- it means that you have trouble distinguishing rational from irrational numbers in `float` because you've lost information which from a "am I far from the right answer" position is small, but from a "have I lost any arithmetic information" is big

#### [Tobias Grosser (Oct 16 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911784):
Would it make sense to e.g. define Cooper over this domain?

#### [Kevin Buzzard (Oct 16 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911797):
There's no inequalities either, if you need inequalities

#### [Mario Carneiro (Oct 16 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911800):
sure, I mean it's still the integers, but it's not easier

#### [Mario Carneiro (Oct 16 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911886):
> nothing uncountable can be decidable

This is an interesting statement. I wonder how you would prove this

#### [Kenny Lau (Oct 16 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911887):
however given two *explicit* terms of type `p_adic_integer -> nat`, you can decide if they are equal. (This is a meta-theorem, not a theorem)

#### [Kenny Lau (Oct 16 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911893):
```quote
> nothing uncountable can be decidable

This is an interesting statement. I wonder how you would prove this
```
that's a meta-theorem as well

#### [Mario Carneiro (Oct 16 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911894):
false

#### [Kenny Lau (Oct 16 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911906):
hmm?

#### [Mario Carneiro (Oct 16 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911912):
You can do the same tricks as in R to construct numbers whose equality is equivalent to the halting problem

#### [Kenny Lau (Oct 16 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911972):
right, but I mean terms that are constructed explicitly and constructively

#### [Mario Carneiro (Oct 16 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911977):
even so

#### [Kenny Lau (Oct 16 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911980):
i.e. computable functions

#### [Tobias Grosser (Oct 16 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911982):
@**Kevin Buzzard**, I need to read more of this but this is a paper I want to read regarding this issue: https://arxiv.org/pdf/1602.07209.pdf

#### [Mario Carneiro (Oct 16 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135911992):
computable number equality is not decidable

#### [Mario Carneiro (Oct 16 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912004):
even though it is a countable set

#### [Mario Carneiro (Oct 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912007):
so the converse of your statement is false

#### [Kenny Lau (Oct 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912009):
i.e. you can't say "the n-th bit is 1 if this program terminates at the n-th step"

#### [Kenny Lau (Oct 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912025):
that won't be a computable function

#### [Mario Carneiro (Oct 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912027):
that's a computable function

#### [Kenny Lau (Oct 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912039):
ah wait

#### [Mario Carneiro (Oct 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912041):
termination in n steps is decidable

#### [Kenny Lau (Oct 16 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912113):
wait no

#### [Kenny Lau (Oct 16 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912116):
that isn't what I said

#### [Kenny Lau (Oct 16 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912118):
```quote
however given two *explicit* terms of type `p_adic_integer -> nat`, you can decide if they are equal. (This is a meta-theorem, not a theorem)
```
here

#### [Kenny Lau (Oct 16 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912128):
you gave me two terms of type `p_adic_integer`

#### [Mario Carneiro (Oct 16 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912138):
what is an explicit term of `p_adic_integer`? It is a lambda, which is a computable function

#### [Kenny Lau (Oct 16 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912221):
right

#### [Kenny Lau (Oct 16 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912230):
but I'm talking about terms which have type `p_adic_integer -> nat`

#### [Mario Carneiro (Oct 16 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912239):
oh you are using Andrej Bauer's trick

#### [Kenny Lau (Oct 16 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912241):
right

#### [Kenny Lau (Oct 16 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912244):
someone should make that a tactic :P

#### [Mario Carneiro (Oct 16 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912264):
well, it's still false because `choice` is an explicit term

#### [Kenny Lau (Oct 16 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135912270):
constructive

#### [Tobias Grosser (Oct 16 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135913075):
Here the interesting part:
> Obviously  there  is  no  direct translation of concepts like linear inequalities and Barycentric Division to non-ordered fields, such as the p-adic ones. Nevertheless we want our p-adic polytopes and simplexes to be defined by conditions which are as simple as possible, to obtain a notion of faces satisfying all the above properties, and most of all to develop a flexible and powerful division tool. This is achieved here by first introducing and studying certain subsets of Γm called “largely continuous precells modN”, for a fixed m-tuple N of positive integers.  These sets will be defined by a very special triangular system of linear inequalities  and  congruence  relations  modN.   In  particular  they  are  defined simply by linear inequalities in the special case where N= (1,...,1) ...

#### [Tobias Grosser (Oct 16 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135913192):
and
> We extend the binary congruence relations of Z to Γ with the convention that a≡+∞[N] for every a∈Γ and everyN∈N.  A subset A of FI(Γm) is a basic Presburger set if it is the set of solutions of finitely many linear inequalities and congruence relations.  Although we will not use it, it is worth mentioning that, by the quantifier elimination of the theory of Z in the language LP res, the definable subsets of Z d, and more generally of Γm, are exactly the finite unions of basic Presburger sets.

#### [Tobias Grosser (Oct 16 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135913312):
Need to allocate a weekend to go through the paper carefully before i can have an in-depth discussion here.

#### [Tobias Grosser (Oct 16 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135913315):
Thanks for the comments.

#### [Mario Carneiro (Oct 16 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135915767):
@**Kenny Lau**  Here's a stab at your first statement: suppose P Is a program that decides equality for terms of type T. Given inputs (x, y), P will make some number of decisions (like if statements) before announcing true or false, which maps (x, y) in $$\mathbb{Z}\subseteq\mathbb{Z}_2$$ where the ones and zeros correspond to the choices, and the termination is because P always halts. This is a mapping $$F : T \times T \to \mathbb{Z}$$, and there is some set $$S\subseteq \mathbb{Z}$$ of "accepting states" where the program announces equality; correctness of P implies $$F(x,y)\in S\iff x=y$$.

If P has access to mysterious operations that measure x and y jointly, then it is possible that x=y is just a single instruction in the machine and so the theorem won't hold. Instead, we assume that each branching operation measures some property of either x or y but not both at the same time. (Stuff like comparing the first bit of x against the first bit of y can be split into two branches to measure first x then y.)

Now if $$F(x,x) = F(y,y)$$, meaning that the same sequence of operations that lead to the decision $$x=x$$ or $$y=y$$, then we also have $$F(x,x)=F(x,y)$$ because both execution paths make the same decisions regardless of whether they are examining $$x$$ or $$y$$. Thus $$x=y$$, so $$F$$ is injective on the diagonal and hence $$T$$ is countable.

#### [Rob Lewis (Oct 16 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135921571):
Looks like I missed an interesting conversation, but just to answer the easy questions at the beginning! @**Tobias Grosser** indeed, referencing a git hash would be ugly but more stable. I'll try it out. The construction does require `p` to be prime. I don't even have a picture of what Presburger arithmetic over Z_p would look like since there's no ordering. Maybe there's an answer in the polytope paper you linked, that looks super interesting.

#### [Tobias Grosser (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135921698):
Thanks @**Rob Lewis** for the answer. I would really like to discuss some of these topics in Freiburg.

#### [Tobias Grosser (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135921722):
Need to do more reading to be able to have at least a somehow sensible conversation.

#### [Tobias Grosser (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135921728):
Getting your opinion on this topic would be very useful.

#### [Rob Lewis (Oct 16 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135921807):
For sure!

#### [Tobias Grosser (Oct 16 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135921893):
Regarding the lack of ordering, in our compiler we associate to comparisions the information if a comparision should be interpreted as signed or unsigned.

#### [Tobias Grosser (Oct 16 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135921947):
In this sense, hence there are two "order" relations.

#### [Tobias Grosser (Oct 16 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135921957):
When when interpreting the values as signed integers, the other when interpreting them as unsigned.

#### [Tobias Grosser (Oct 16 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135921960):
They are to my understanding not compatible.

#### [Tobias Grosser (Oct 16 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135921996):
And maybe don't work  for generic p-adic numbers, but just the finite bitwidth numbers we are interested in.

#### [Reid Barton (Oct 16 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135922000):
They're also both not compatible with other structure like addition. For example if $$a \ge b$$ (in either sense), then it does not follow that $$a + c \ge b + c$$, unless you know that the additions do not overflow somehow

#### [Tobias Grosser (Oct 16 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135922052):
Right.

#### [Reid Barton (Oct 16 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135922101):
If you tried to define inequalities similarly for the 2-adics, then you should "start from the left-most bit"--but there is no left-most bit of a 2-adic number

#### [Tobias Grosser (Oct 16 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135922149):
Right. Many things don't fully checkout here.

#### [Reid Barton (Oct 16 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135922197):
I took a quick look at that paper and it was a bit hard to understand what their goal was, in part because the paper seemed to be setting up some background theory for a subsequent paper. But as far as I can tell, it talks about Presburger arithmetic not on Z_p or Q_p directly but on N or Z via the p-adic valuation.

#### [Reid Barton (Oct 16 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135922360):
You could also say that Presburger arithmetic on N is really just the first order theory of addition (and zero) because an inequality $$a \le b$$ can be represented by $$\exists c, a + c = b$$. So then you could ask about the first order theory of addition for Z_p. I think it would just reduce to making statements about the p-adic valuations.

#### [Tobias Grosser (Oct 16 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/135922570):
Interesting.

#### [Siddharth Bhat (Oct 21 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/136224451):
@**Reid Barton**  what does it mean to perform presburger arithmetic on the p-adic valuation?

#### [Reid Barton (Oct 21 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/136224600):
Well the p-adic valuation of a p-adic integer is a natural number, and Presburger arithmetic is the theory of natural numbers under zero and addition. So we're talking about formulas like "$$v_p(x) = v_p(y) + v_p(y) + 1$$".

#### [Siddharth Bhat (Oct 21 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/136224767):
Ah, hm.

#### [Siddharth Bhat (Oct 21 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP paper/near/136225013):
@**Reid Barton** Do you know, how much of the geometry of presburger sets is left over when you move to p-adics?

