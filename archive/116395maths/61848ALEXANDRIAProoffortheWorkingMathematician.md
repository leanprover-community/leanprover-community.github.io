---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/61848ALEXANDRIAProoffortheWorkingMathematician.html
---

## Stream: [maths](index.html)
### Topic: [ALEXANDRIA: Proof for the Working Mathematician](61848ALEXANDRIAProoffortheWorkingMathematician.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (May 15 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588456):
**[ALEXANDRIA: Large-Scale Formal Proof for the Working Mathematician](https://www.cl.cam.ac.uk/~lp15/Grants/Alexandria/)**

*L. C. Paulson, Computer Laboratory, University of Cambridge*

> Mathematical proofs have always been prone to error. Today, proofs can be hundreds of pages long and combine results from many specialisms, making them almost impossible to check. One solution is to deploy modern verification technology. Interactive theorem provers have demonstrated their potential as vehicles for formalising mathematics through achievements such as the verification of the Kepler Conjecture. Proofs done using such tools reach a high standard of correctness.

> However, existing theorem provers are unsuitable for mathematics. Their formal proofs are unreadable. They struggle to do simple tasks, such as evaluating limits. They lack much basic mathematics, and the material they do have is difficult to locate and apply.

> ALEXANDRIA will create a proof development environment attractive to working mathematicians, utilising the best technology available across computer science. Its focus will be the management and use of large-scale mathematical knowledge, both theorems and algorithms. The project will employ mathematicians to investigate the formalisation of mathematics in practice. Our already substantial formalised libraries will serve as the starting point. They will be extended and annotated to support sophisticated searches. Techniques will be borrowed from machine learning, information retrieval and natural language processing. Algorithms will be treated similarly: ALEXANDRIA will help users find and invoke the proof methods and algorithms appropriate for the task.

> ALEXANDRIA will provide (1) comprehensive formal mathematical libraries; (2) search within libraries, and the mining of libraries for proof patterns; (3) automated support for the construction of large formal proofs; (4) sound and practical computer algebra tools.

> ALEXANDRIA will be based on legible structured proofs. Formal proofs should be not mere code, but a machine-checkable form of communication between mathematicians.

> The project will run for 60 months starting 1 September 2017.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 15 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588533):
Wow, those are big claims (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588843):
Yeah exactly. So I emailed him saying "you're just up the road from me, how come you're not reaching out to mathematicians like me so we can talk about this sort of stuff?" and he said "yeah I'm just sitting in my office like usual really" so I said "OK so you can reach out to me by me coming to visit on Tuesday and you telling me what it's all about" and he said "OK"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588848):
I mean, I guess he didn't say _exactly_ that...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588856):
but he did remark that someone called Peter Koepke would also be there on Tuesday giving a talk...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 15 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588906):
At the risk of sounding maybe a bit unimpressed, but I think that this proposal is not overly ambitious.  It's basically a continuation of current work in Isabelle.  The goals are pretty much 1) formalize some undergrad math, 2) improve the search function a bit, 3) add more refactoring tools, and 4) integrate and polish some computer algebra tactics.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588909):
```quote
Wow, those are big claims (-;
```
It's also big money, right? Multi-million pound ERC grant. One of the last the UK will ever get, due to Brexit.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588921):
Such a shame to do this in Isabelle

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588922):
He should have come here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588923):
Thanks for this Gabriel. In mathematics it seems to be extremely difficult to get these big ERC grants, in the sense that the people I know who have got them recently have put in some very high-powered proposals.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588925):
My impression is that he is really into the idea of formal proofs being readable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588927):
As far as I can see there is no obstruction to having readable proofs in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588964):
I mean, human-readable source code

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588970):
It's only Mario and Johannes don't like them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588975):
The sledgehammer thing is much more serious issue of course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588990):
I sometimes write "low-level" proofs, and I find them very enjoyable (my instincts just tell me to press on instead of trying tactics), but I do feel at the end of it all that they are no more readable than any other Lean code, they are just intro, apply, intro, refine, intro, exact, cases, cases, rwa, done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588991):
`intros a Ha`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126588992):
Maybe I should be writing `intros a proof_that_a_is_in_X`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589037):
I often try to do that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589093):
https://github.com/kbuzzard/lean-stacks-project/blob/d2f64a23d8e6347bde488de0b0a93be1b72f18d6/src/tag00E8.lean#L145

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589099):
"I follow my nose, cases, rw, apply, cases, exact, intro, split, cases, apply, exact"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589106):
and voila, Spec(R) is compact

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589115):
I don't think it would be hard to make it easier to read

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589118):
You already have a couple of explicit ``have``

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589121):
I agree

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589159):
it was certainly easy to write :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589162):
but my point is that I didn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589163):
make it easy to read

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589164):
You could add a few more, maybe with some `suffices`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589241):
Why "quasi-compact" if you prove compactness?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589308):
I thought that this was the French's fault?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589354):
In the UK, compact := every cover has a finite subcover. In France it's Hausdorff + ...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589357):
but alg geom is a French subject

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589365):
because schemes are typically not Hausdorff, it's quasi-compact

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589425):
PS @**Gabriel Ebner** when writing grant proposals, you write what you think will get funded (so you get a promotion or pay rise when you get the grant), and then you just keep on doing what you were doing beforehand anyway (at least that's what happens in maths).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589440):
One might also ask why computer scientists have been sitting on things like Coq / Isabelle for decades, and these are perfectly capable of formalising all of undergraduate pure mathematics, but nobody has done it yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589585):
Oh, I understand: you mean mathlib's definition of compactness is the broken one (without Haussdorff)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589588):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589589):
it's only broken because of your cultural upbringing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589591):
One could instead regard it as a translation issue

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589594):
English "compact" := French quasi-compact

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589639):
Like UK N := France N^0 or N^* or whatever you call the thing without a zero.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589643):
Anyway, I don't understand how proving quasi-compactness can be anything but trivial in algebraic geometry: any open set covers almost everything!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589646):
well I did point out that my proof was just 50 lines of intro, apply, exact ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 15 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126589804):
To be honest I have no idea where this difference comes from. All spaces I work with are obviously Haussdorff, so I never say or write quasi-compact

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 15 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126590092):
But then, you forget saying Haussdorff half the time!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 15 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126591097):
He's using type class inference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126964435):
```
Did you get any insights with the ALEXANDRIA / Peter Koepke lecture person today?
```
yesterday

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126964438):
That was an interesting day

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126964446):
I'll talk about it later, I need to go and do family stuff for 30 minutes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966431):
So Koepke gave a nice talk about some system that they got going which checks ZFC proofs and whose parser parses statements which look like natural language

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966437):
I personally don't know how much importance to attach to the concept that a computer-checked proof should be human-readable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966438):
And after that there was a long discussion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966481):
for over 2 hours

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966483):
where we just talked about life and where all this was going

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966497):
Koepke had taken someone else's Haskell code written in 2008 and got an MSc student to understand it and rewrite it better

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966500):
Their system is called SAD

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966508):
and they are producing "miniatures", i.e. relatively short proofs which rely on a lot of assumptions which are axioms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966551):
e.g. they proved something about successor cardinals being regular but assuming things like kappa x kappa = kappa etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966554):
what his point was, was that the proof script is genuinely human-readable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966556):
and everyone dreamt about having all 1st and 2nd year UG maths in their system

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966564):
but I think that only I have a coherent strategy for making this happen

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966567):
i.e. getting 1st and 2nd year UGs to put it into the system themselves

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966571):
and we all moaned about how the Cauchy Integral Formula was hard

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966616):
and Paulson even had an anecdote about it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966621):
having translated Harrison's proof from (something) into (something)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966622):
maybe from HOL light into Isabelle?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966630):
and there was some subtlety about whether the curve you were integrating around was differentiable or continuously differentiable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966632):
that sort of thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966640):
And Paulson wants to know what to do with this pot of euro money that he's sitting on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966698):
but we didn't talk much about that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966755):
but one of his post-docs, Angeliki Koutsoukou-Argyraki, is speaking at Imperial College London in a few weeks' time so perhaps I should have a think about this and talk to her

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966761):
My impression is that Paulson wants to reach out to mathematicians but doesn't actually want to go and meet any, he has plenty of more important things to do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966764):
but he has people who can go and meet them for him

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966804):
but he is very open to ideas of how to give money to mathematicians

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966808):
and turn them to his way of thinking

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966811):
and I can definitely work with that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 23 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966866):
This Haskell code producing human-readable proofs... was that from Tim Gowers?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 23 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966873):
He had such a project, but I think it was more like 2012 or something...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966875):
I'm pretty sure the best you could do now would be to document your journey towards that scheme milestone, then get Mario or Johannes to help you redoing it right, and document that second journey.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966884):
To me it seems way more useful than adding some more undergrad maths to some new proofs assistant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966918):
By the way, who is coming to Europe this summer in the end? I guess we all saw someone decided that ITP is not about maths (and it's not for lack of submissions). But maybe people still want to come?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966965):
There is also this http://www.uc.pt/en/congressos/thedu/thedu18 which is intriguing but there is no program yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 23 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126966985):
I am going to Dagstuhl but not ITP this summer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967028):
Is the Dagstuhl the thing Assia is organising?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967029):
What is Dagstuhl?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 23 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967030):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967032):
Is that quite soon?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967035):
Last time I thought about that it seemed hopeless for me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 23 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967039):
no, it's in August I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967046):
Nooo, why August?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967049):
August doesn't exist

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967050):
The dreaded month

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967051):
if you're French

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967054):
les vacances

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 23 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967056):
this https://www.dagstuhl.de/en/program/calendar/semhp/?semnr=18341

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967058):
Indeed, it's les vacances

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 23 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967102):
what's all this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967109):
In France attending a conference in mid-August pretty much automatically implies divorce

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (May 23 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967165):
Huh, so August in the Netherlands is not quite as bad as it sounds like [August in France](https://www.frenchtoday.com/blog/french-vocabulary/french-vacation-vocabulary-expressions-les-vacances) is, but I was always surprised how quiet it got.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 23 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967182):
Yes, August is the only month where we have decent weather... so we all leave the country (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967226):
I'm also pretty surprised this Dagstuhl thing was not advertised here before

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967343):
Do you think this will be all about Coq and Isabelle, or there could be some room for Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 23 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967406):
Well, I'll be there...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 23 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967417):
You should have seen when I went to represent metamath at a conference where no one's ever heard of it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967462):
I hope the case of Lean is different (metamath looks purely masochistic)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 23 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967471):
It's really not as bad as it looks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 23 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967480):
I would not have been so successful with it if it were not so ergonomic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967525):
@**Sebastien Gouezel** Did you discuss this conference with Assia?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967529):
Do you know more about it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967631):
What about trying to gather either in London or Paris the week after Dagstuhl?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126967641):
That week has much more existence

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (May 23 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126968938):
```quote
Do you know more about it?
```
You mean the conference in August? I already had to negotiate with my wife to go to ICM, another conference this summer is completely impossible. So no, I have not discussed it with Assia.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126968954):
I can believe that ICM is already too much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126969019):
But Assia not advertising this conference to the only mathematician at her university interested in formal proof probably means this conference is not intended at all for mathematicians

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (May 23 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126969050):
Yes, ICM is long, and far away. We considered going there with the family, but Rio is not the safest city in the world for a woman alone and three children...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (May 23 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126974146):
I will be in Dagstuhl and at ITP in Oxford. Going to Paris or London would be easy for me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 23 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126974155):
Ah! Do you like schemes or manifolds?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 23 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/126977983):
A related question -- what about going to Paris _and_ London :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (May 29 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ALEXANDRIA%3A%20Proof%20for%20the%20Working%20Mathematician/near/127247353):
Hi, indeed I am (co)organizing this Dagstuhl [stuff](https://www.dagstuhl.de/en/program/calendar/semhp/?semnr=18341), with 3 colleagues: [Andrej Bauer](http://www.andrej.com/research.html), [Peter Lumsdaine](http://peterlefanulumsdaine.com/research.html) and  and [Martin Escardo](http://www.cs.bham.ac.uk/~mhe/).  Dagsthul is the CS's Oberwolfach so it is invitation only and  the application (including the list of invitees) has been crafted a long time ago. Before I was even aware that you guys could be interested in this kind of event...

