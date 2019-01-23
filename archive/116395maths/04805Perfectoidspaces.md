---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/04805Perfectoidspaces.html
---

## Stream: [maths](index.html)
### Topic: [Perfectoid spaces](04805Perfectoidspaces.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307288):
Ok so here is the perfectoid spaces thread. As many people here know, I've long been mulling over the idea of formalising the notion of a perfectoid space in Lean. To the CS people -- it's just some structure, like a group, just a few more axioms and things.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307303):
The problem is that I'm a mathematician and I'm not very good at building structures in Lean yet because I haven't practiced enough yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307309):
So here's the plan.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307320):
I'm going to make a public github repo called lean-perfectoid-spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307327):
and then we develop what we need in there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307333):
What are the main ingredients? I'll explain these things in an issue.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307375):
But in short, we need adic spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307379):
so we need presheaves and sheaves of topological rings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307384):
and we need affinoid adic spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307387):
so we need the notion of a valuation on a ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307407):
Now here's a dumb thing that everyone knew already but only dawned on me recently.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307465):
There are two ways to make a perfectoid space -- a "top down" way, where you define a perfectoid space to be an adic space with some property and define an adic space afterwards -- you sorry your way from the top and attempt to connect to the bottom.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307477):
Or there's a "bottom up" way, where you think "we'll definitely need adic spaces so we'll need affinoid adic spaces so we'll need valuations so we'll need a way of turning a totally ordered group into a totally ordered monoid by adding a bottom element and I think we have that, or we nearly have that anyway, so let's start with that and then build up"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307485):
With schemes I read the stacks project from front to back and I made the definition from the bottom up.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307495):
Are there advantages in working from the top down?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307556):
Next, who should be allowed to push? Is it sensible to start with just me and force other people to learn about PRs and so on?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307565):
As a git newbie I found it far easier to just give Kenny full access to the stacks project repo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307574):
but the result of this was that one day I realised there were a bunch of files in my project which I had no idea what they did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307578):
and then when Lean upgraded and they all broke and Kenny was revising for exams I was sort-of stuck.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307635):
Should I concentrate on making sure I understand every line of code in the project, or should this be something which I should be happy to delegate?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307644):
Those are my initial thoughts. I've been really busy recently with marking issues but now these things are over and I hope to find some time to put into this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (May 30 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127307979):
I think that you should be able to understand every line of code in the project, but it does not mean than you cannot delegate and grant push access to others. Just that you should be ready to revert commits, ask for freezing etc. This is how the Feit Thompson proof was written, with many people having commit rights (it was not even a git repo).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (May 30 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127308229):
I have never seen anything serious being done top down. I have been working for some time with some axiomatic algebraic numbers, waiting form the completion of the closure construction, and even for such a simple thing, one of the axioms was wrong (I don't remember the details) . So I find it scary because it is usually hard to get definitions right at the first stab. And the one you're aiming at is a truly complex one. But may be you could try to build the bridge simultaneously from the two ends, and hope for the best. One really useful thing is to write down the complete roadmap somewhere, as precise as possible. But this is what will go in your issue right? Are there components that can be done in parallel?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127309013):
I love this place.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127309018):
Assia -- *many* thanks for your very quick and extremely helpful response.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127309036):
I will begin, hopefully before the weekend, by creating a repo and writing an extended issue explaining as much as I know about what needs to be done.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127309046):
There should be several things which can be done in parallel.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127309097):
I remember now -- when I talked about making something else I wanted in mathlib, Mario suggested that I wrote as detailed an explanation as possible and made it an issue.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312071):
I'm at the London Number Theory Seminar and it's being given by Matthew Morrow, co-author of several papers with Scholze and perfectoid expert! I just asked him what the definition of a perfectoid space was and I'm glad I did -- he said that he definition has gone through several iterations but he was now happy with it, and gave me a precise reference -- Scholze's paper "etale cohomology of diamonds".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312094):
https://arxiv.org/abs/1709.07343

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312095):
That is the definition we will be formalizing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312134):
The paper is under 9 months old. To the CS people -- the reason that defining a random structure is interesting to mathematicians is that this is a cutting-edge structure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312247):
It is definition 3.19 on page 18 of (v1 of) the paper at the above link

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 30 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312333):
It's funny Scholze refers to Fontaine's Bourbaki talk about Scholze

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 30 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312343):
Maybe this theory is actually circular

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312587):
:-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312594):
Fontaine only defines perfectoid rings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312661):
Technical interlude: in Scholze's original paper he only defined a perfectoid space over a field; Fontaine was the first person to make the definition live independently without being bound to an underlying field

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312669):
OK so here's a theorem in maths:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312705):
$$\mathbb{Z}_p^{cycl}[[T^{1/p^\infty}]]\langle(p/T)^{1/p^\infty}\rangle[1/T]$$ is a perfectoid ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312730):
You show that to any number theorist in the area and they'll know what that notation means

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312736):
Can we use it in Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312782):
We refer to the pointy brackets as "langle/rangle"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 30 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312784):
Definitely looks like the kind of sequences of symbols that show up in talks about perfectoid stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312785):
because LaTeX

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312802):
Nobody is raising a prime number to the power infinity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312805):
this is a limit of rings where the infinity is replaced by n

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312811):
and then n goes to infinity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312830):
That's not the major concern. Of course all those things are schematic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312834):
If this stuff were written out in full the definition would double in length and would involve two and possibly more limits

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312835):
How many ring construction mechanisms are nested there?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312896):
I think three or four

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312901):
depending on whether it's a theorem that something commutes with something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312903):
I don't think these things commute

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312906):
I think maybe four

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312910):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312915):
maybe far more

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312917):
it depends on what you mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312928):
$$\mathbb{Z}_p^{cycl}$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312930):
is a ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312932):
In lean syntax with constants, no notation, what would it look like roughly?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312949):
So am I allowed to make the ring Z_p^cycl?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312951):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312954):
I mean I can call it X?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312955):
that's like `Z_cycl p` I guess

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312962):
no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127312963):
it's much worse

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313007):
maybe it's about as bad

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313010):
there is an issue with completions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313015):
everything has to be complete at every stage

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313026):
so `completion (Z_cycl p)`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313033):
Let me define, for A an abelian group, `P A` to be the projective limit of $$A/p^nA$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313036):
where's `p`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313042):
it's a constant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313046):
we fix a prime p on line 1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313052):
It never changes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313058):
yeah okay, parameters

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313059):
there is no relation between the different p-adic theories for different primes p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313115):
So $$\mathbf{Z}_p^{cycl}$$ is:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313123):
$$\mathbf{Z}_p$$ is the p-adic integers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313140):
$$\mathbf{Z}_p[\zeta_{p^n}]$$ is the extension of that ring obtained by adjoining a primitive $$p^n$$th root of unity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313156):
$$\mathbf{Z}_p[\zeta_{p^\infty}]$$ is the direct limit of those things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313159):
But `Z_cycl_p` is one thing after all that construction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313160):
and $$\mathbf{Z}_p^{cycl}$$ is `P` of that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313171):
As in, the notation is not decomposable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313173):
it depends only on p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313204):
it's not p of Z^cycl or ^cycl of Z_p, really

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313225):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313232):
We build from left to right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313243):
So with that in mind, how many decomposable parts are there in the ring you mentioned at the top?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313247):
If $$A$$ is a ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313272):
then $$A[[T^{1/p^n}]]$$ is formal power series in $$T^{1/p^n}$$ with coefficients in $$A$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313288):
and $$A[[T^{1/p^\infty}]]$$ is `P` of the direct limit of these things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313289):
So that's just A[[X]] with some quotient?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313294):
no quotient involved

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313302):
$$T$$ is a variable with no relations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313352):
Each ring is isomorphic to `A[[X]]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313360):
the mentioning of the powers of p is just to show how to take the union

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313366):
what makes $$T^{1/p^n}$$ different from X

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313371):
the maps between the various rings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313375):
$$T^{1/p^{n+1}}^p=T^{1/p^n}$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313396):
For fixed n all those rings are isomorphic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313397):
but if you want to call them all X

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313401):
So the notation here is `p_infty_completion A p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313402):
then the maps all send X to X^p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313408):
where there are only two arguments A and p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313418):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313462):
that's what A[[T^{1/p^infty}]] means

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313473):
depends only on A and p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313478):
This is my question

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313483):
Depends only on the ring A and the prime number p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313484):
for each of those notations, what are the dependencies and atomic bits

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313492):
OK so I will say less about what you're not interested in for the pointy brackets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313494):
I now understand the game we're playing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313507):
If A is a topological ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313515):
and p is a prime number

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313523):
then I can build $$A\langle(p/T)^{1/p^\infty}\rangle$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313568):
Remark: $$\mathbb{Z}_p^{cycl}$$ has a topology

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313581):
and we need this topology to build a topology on $$\mathbf{Z}_p^{cycl}[[T^{1/p^\infty}]]$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313591):
Finally [1/T] is a localization

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313602):
if A is a ring and T is in A then A[1/T] is a localization of A

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313604):
I assume that the big expression is meant to be suggestive of the interpretation of the maps in the limit, but are there other expressions that could go there?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313606):
It is "standard notation"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313615):
this is really interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313617):
like does $$A\langle(pT)^{p^\infty-2}\rangle$$ make any sense?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313619):
no!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313621):
Are you crazy?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313671):
what kind of nonsense is that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313685):
So what is the question? :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313693):
if there's only one thing that the expression can be, it seems like a waste of notation :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313709):
but sure, if you want that exact thing only then you can get a reasonable approximation in lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313717):
$$A[[X^{1/p^\infty}]]\langle (p^3/X)^{1/p^\infty}\rangle[p/X]$$ makes sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313759):
I assume changing `T` for `X` does nothing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313763):
you got me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313767):
I was just showing you how amazingly flexible our notation was

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313769):
T

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313770):
X

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313771):
any letter at all

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313773):
except most of them would be completely unsuitable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313776):
I would stick with T

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313779):
From a CS standpoint those letters are kind of silly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313784):
I can't quite work out who is laughing at who in this conversation :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313785):
it's like a bound variable, but it isn't binding anything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313788):
The ring contains an element called $$T$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313789):
that's the trick

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313797):
$$k[T]$$ and $$k[X]$$ for polynomial rings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313808):
they're defeq for you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313846):
but for us, one has a T in and the other has an X in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313859):
A simple idea that is surprisingly hard to formalize

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 30 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313862):
$$T \in k[T]$$ just like $$\Gamma, x \vdash x$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313869):
A man who speaks both languages

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313872):
In that case `x` is in the context though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313879):
`k[T]` isn't a context or a context like thing, it's a concrete ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313885):
(I guess `k` is in the context)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313896):
Oh here is a question

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313897):
Is this question about notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313902):
*completely independent* of the question of formalizing the definition?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313950):
i.e. the notation is something which can be thought about later

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313953):
not completely, but for the most part yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313954):
Those rings are not needed in the definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313957):
it affects what things get definitions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313959):
that ring I posted is a famous example of a perfectoid ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313961):
nowhere in the definition of perfectoid space does that definition show up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313962):
so for example since $${\bf Z}^{cycl}_p$$ is a notation you need a definition `Z_cycl p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127313970):
however proving that that ring is a perfectoid ring is a theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314046):
To answer your explicit question, yes you can (and probably should) defer all consideration of notation until late in the development

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314058):
It's basically easy to retrofit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 30 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314138):
Probably in lean you wouldn't be able to have this X/T magic stuff, it would be just one fixed letter as part of the notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314558):
p151  : "choose a quasi-pro-etale surjection q from a strictly totally disconnected perfectoid space that can be written as an inverse limit of quasicompact separated etale maps q_i as in Proposition 11.24"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314560):
This is going to be so much fun

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314565):
Lean is made for this sort of stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314572):
Mario, this is what real maths looks like

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314588):
super-complex structures

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314596):
at least it's what some kinds of real maths looks like

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314603):
it is a million miles from anything that has ever been formalized

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314607):
and it will be easy to formalize

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314615):
that's why it's important

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314657):
and easy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314675):
it's a huge gap in the market

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314699):
and I want to be part of a group which naturally fills this gap

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314704):
and has a great deal of fun and learns a bunch of stuff at the same time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314769):
and there are huge gaps everywhere

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314778):
I'm sure Patrick can just reel off one in his area

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314793):
some complicated definition which turns out to be super-important in the kind of geometry he does

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314812):
Doing all this is **one way** of doing Tom Hales' fabstracts

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314818):
another way is: "scheme := sorry, now let's keep going"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314825):
but this way is much more fun

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314834):
and you'll end up with types that typecheck

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314882):
Lean is a big puzzle game

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314888):
and we will be able to make some really cool levels for this game

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314891):
"construct a term of this type"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314897):
that's the game

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314901):
the type is the level, the term is the solution

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314915):
All the old levels are boring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314924):
"prove quadratic reciprocity"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314927):
"prove the prime number theorem"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314928):
kids want new levels

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314931):
they are bored with those old levels

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314936):
and the computer scientists keep solving them again and again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127314998):
all those websites

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315009):
"100 classic levels in the formal proof verification game"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315019):
we want better levels with funkier graphics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315022):
I mean objects

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315037):
it's like when I show my kids the old text-based adventure games which I used to love at their age

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315040):
they are like "...dad, it's just a bunch of text"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315045):
"where are the perfectoid spaces?"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315097):
I mean graphics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315106):
the cool objects

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315119):
things have moved on in maths

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315326):
Should one put pdfs of papers in a github repo?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315366):
"Here are some foundational papers containing important definitions"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315370):
"which we are formalising"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315375):
Choice 1: offer a link

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315377):
Choice 2: offer a pdf subdirectory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315385):
[Choice 3: both]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 30 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315476):
If arxiv version are up to date then a link is enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 30 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315487):
But it's much more important to write a roadmap

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (May 30 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127315496):
unless you want to formalize everything in those papers...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127317549):
This is very helpful.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127317553):
It will take me some time to write a good roadmap

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 30 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127317562):
by which I mean a couple of days

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 30 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127324192):
```quote
Probably in lean you wouldn't be able to have this X/T magic stuff, it would be just one fixed letter as part of the notation
```
In Sage it is possible to choose your own symbol for the polynomial variable. I don't know what magic Python has to do this. But it is really nice!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 31 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127349529):
Hmm, we probably also need some "almost mathematics". Or is that not needed for the definition, but only for using these guys? I don't remember...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 31 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127354214):
That's only needed for the tilting correspondence I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 31 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127354219):
although we will surely need some facts about perfectoid rings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446113):
What are the arguments for and against making `Tate_ring` into a typeclass?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446114):
https://arxiv.org/pdf/1709.07343.pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446115):
page 14 just before definition 3.1 for Tate ring. And then there is also the notion of `perfectoid_ring` in the definition itself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446128):
it's a condition on a pair consisting of a Tate ring and a prime number

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446174):
for example a certain subring of the ring (defined by the topology) has to be p-adically complete

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446182):
we will constantly be localizing Tate rings and getting other Tate rings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446190):
it's some sort of p-adic version of usual ring localization

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 02 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446306):
against: the pseudo-uniformiser is not canonical

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446310):
Kenny it's just the assertion that there exists pi with pi^p divides p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446312):
you don't have to give it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446313):
pi pseudouniformiser

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446319):
See Remark 3.2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446320):
all you need is that one exists

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446324):
any choices are equivalent in some strong way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446366):
I don't see why it wouldn't be a typeclass

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446368):
so no diamonds?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446372):
with what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446380):
I have no idea how these things work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446381):
where is `p` coming from though? Is it a component of any lower structures?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446383):
it's a prime number

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446384):
best described as a parameter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446387):
because you never change it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446427):
The problem with parameters is they don't last long

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446432):
then it's just an input which is a prime number

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446434):
and which goes everywhere

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446436):
once you exit the section, the parameter becomes explicit and you can't make it a parameter again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446453):
The question is: if lean is inferring `Tate_ring ?p R`, how can it infer `p`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446513):
I guess as long as all the theorems have `p` mentioned explicitly it may be solvable by unification, but I don't know how well this will work with notation and such that doesn't have a `p` explicitly in it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 02 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446518):
`Tate_ring.p`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446521):
that's also a possibility

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446586):
> Let p be a fixed prime throughout.  Recall that a topological ring R is Tate if it contains an open and bounded subring R0 ⊂ R and a topologically nilpotent unit omega∈R; such elements are called pseudo-uniformizers.

Where is p mentioned in that definition? Looks like Tate doesn't depend on p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446653):
Right, I was confused earlier. You don't need p for Tate

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446656):
but you do need it for perfectoid

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446665):
so Tate_ring is I think fine, it's just a top ring plus some axioms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446666):
and perfectoid_ring needs a Tate ring and a prime

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446713):
I suggest using a parameter (a two-argument typeclass) and see how it goes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446729):
So my options are: (1) just make it a structure on a type alpha -- (a) it's a Tate ring (b) there's a prime (c) axioms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446772):
or (2) demand both alpha and p as inputs and then it's a structure with (a) Tate ring and (b) axioms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446773):
this is me building perfectoid ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446774):
I am building perfectoid space from the top down

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446775):
it's a long way up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446776):
I'm taking tentative steps down

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127446787):
and Mario is suggesting (2)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127447844):
Eew prime numbers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127447847):
how am I supposed to input a prime number?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127447848):
there's a function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127447849):
prime : nat -> Prop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127447889):
so it could be carrying round `{p : nat} {p_prime : prime p}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 02 2018 at 03:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127447891):
just make a subtype

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127447892):
I have an issue with the subtype solution

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127447900):
then you have to spend your entire life writing p.1 instead of p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127447901):
and it is an absolutely fundamental part of the notation, it is on every line

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 02 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127447905):
```quote
then you have to spend your entire life writing p.1 instead of p
```
\u p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127447963):
and then you show it to people with the up-arrows off or something.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127447973):
like our dirty underwear

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127447987):
Is the subtype already there?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448066):
I can't see it explicitly defined. What is the subtype's name?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448069):
`prime` is taken by the predicate

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 02 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448203):
I don't think there is one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448254):
so I call it `prime'`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448505):
```lean
import data.nat.prime 
open nat
definition prime' := subtype prime
-- unit test
definition two' : prime' := ⟨2,prime_two⟩

instance prime'_is_nat : has_coe prime' ℕ := ⟨subtype.val⟩

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448508):
Anyone any comments on style or anything that's missing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 02 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448555):
make it an autoparam like pnat lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448559):
oh ha ha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448561):
that is a really cool idea

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448562):
wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448563):
how does this work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448569):
that open should be a namespace I think -- I'll edit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448612):
I'll post a gist

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Jun 02 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448613):
what about `a_prime`? as in, “I have a prime number `p : a_prime`” (just my own way of doing it, I don’t think it’s common)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448615):
https://gist.github.com/kbuzzard/327a9c466e3aaecf38fe93109ef8fde6

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448620):
I would like to maximise the chance that this stuff gets into mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Jun 02 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448621):
or rename the predicate to `is_prime`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448623):
so I'd like to get it right as soon as possible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448626):
It's very mathematical coding and the more I do it the better i'll get at it. I hope.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448667):
for all I know there are standard rules of thumb concerning whether a name like `prime` should be used for the subtype or the predicate

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 02 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448668):
this is probably a bad idea but
```lean
instance predicate.has_coe_to_sort : has_coe_to_sort (ℕ → Prop) := (by apply_instance : has_coe_to_sort (set ℕ))
variables {p : prime}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 02 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448675):
lmao

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 02 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448676):
folly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448678):
```lean
constant p
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 02 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448680):
ensues

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448682):
I think that's the best place to start

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448684):
```constant p : nat```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 02 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448723):
`axiom hp : prime p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448724):
I think that's consistent

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448726):
the guys doing $$L^p$$ spaces will hit the roof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 02 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448733):
chaos

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448828):
Can I branch the mathlib in my perfectoid space repo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448829):
and edit it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448830):
and create a PR?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448840):
and just make some note in a file: "this needs some stuff which isn't in mathlib yet -- when it's in mathlib then remove the `import mathlib-foo-branch` import"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448843):
Is that a sane workflow or does it lead to madness?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448883):
and get leanpkg to keep my branch up to date

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 02 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448887):
it is sane

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448888):
What I am not clear on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448892):
is whether I am supposed to say that my project has Mario's mathlib as a dependency

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127448899):
or whether I am supposed to say that my project has some fork of mathlib, perhaps on my github website, as a dependency

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449063):
If you have things you want to add to mathlib, I would have mathlib as its own project

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449064):
and you work on it in that folder

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449066):
editing `_target` is bad news

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449170):
I see. So you're saying that the perfectoid space repository could have as a dependency a perfectoid space mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449171):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449172):
which is some fork of mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449178):
and we maybe have some directory like `src/for_mathlib` subdirectory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449220):
and then when things are looking tidy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449223):
we can just edit our mathlib, submit a PR, and press on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449232):
Have I got all this straight?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449276):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449280):
_target is not for things you plan on editing or working on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449282):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449289):
you know what I sometimes creep in there in the middle of the night and run `leanpkg build`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449292):
because I know my project won't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449333):
Is `adic_space` a typeclass?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449335):
Is `scheme` a typeclass?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449336):
@**Reid Barton** what are your thoughts?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449337):
indeed package distribution in lean is a bit annoying right now since it's hard to distribute `.oleans`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449340):
I just rebuild whenever I upgrade

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449345):
worth the initial wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449347):
if mathlib really wants to contain all of mathematics, at some point people are not going to be able to run leanpkg build in a sane amount of time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449349):
unfortunately we are not quite near that point though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449353):
https://github.com/kbuzzard/lean-stacks-project/blob/6617de7dd5f11af46f0c7e0d2223ee065d71b9f3/src/scheme.lean#L366

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449399):
if you have a sensible project that builds, then I think you can just build your project and it will only build the bits of mathlib that it needs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449401):
this is one of my motivations for defining perfectoid spaces by the way -- to see performance.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449402):
It's all very well proving things about finite groups

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449410):
the proof of the odd order theorem is just John Thompson and his friends writing down everything they know about finite groups and noticing that it happens to be enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449412):
but to write down even one thing about perfectoid spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449413):
will force Lean to handle the notion of a perfectoid space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449414):
we also want oleans so we can search everything though (although there are ways to handle this differently)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449466):
Oh -- does e.g. hover or ctrl-space not work in VS Code without the olean files? What exactly do you need them for?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449469):
I have no idea what they are

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449470):
all I know is that if you type leanpkg build in _target/deps/mathlib then afterwards it goes quicker

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449563):
> unfortunately we are not quite near that point though

Did you see https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/travis.20caching/near/127367872 ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449603):
dammit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449604):
I want to get some headline definition of perfectoid space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449605):
```lean
structure perfectoid_space (α : Type) extends adic_space α :=
(perfectoid_cover : ∃ {γ : Type} (R : γ → Type) [∀ i : γ,  blah blah blah

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449610):
so I need `adic_space`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449611):
but

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 02 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449612):
Using `structure` for schemes and so on seems reasonable. I don't see any practical advantages to using a type class.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449613):
`structure adic_space (α : Type) : Type := sorry` doesn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449614):
I mean the sorry doesn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449615):
that's not an adequate structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449616):
you can write `structure adic_space (α : Type) : Type.`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449658):
or `def adic_space (α : Type) : Type := sorry`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449663):
the problem with the structure solution is that then it is far less obvious that something is missing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449664):
the problem with the def solution is that I can't then extend the structure to a perfectoid space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449665):
If you want to make sure to get the sorry warning with a structure you can do `structure adic_space (α : Type) : Type := (unfinished : sorry)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449666):
rofl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449710):
Why are rings typeclasses? Why are they any different to schemes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449712):
Product of schemes is a scheme etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449752):
[wrong thread @**Andrew Ashworth** ] -- you can edit the post and just change the thread by editing it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 02 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449857):
but the product of schemes isn't a "scheme structure" on the product of the underlying sets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 02 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449859):
because that is sort of a weird way of thinking about it, but more importantly because its set of points is different

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 02 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449866):
Somehow the relationship between a ring and its underlying set is much more important than the relationship between a scheme and its underlying set

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449911):
o_O so it depends on the underlying type?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449914):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 02 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449915):
Well, if you were going to write
```lean
class scheme (\a : Type) := ...
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449921):
what about if I just wrote `class scheme := ` and then asked the user to provide the type?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449924):
oh is that somehow the canonically bad thing to do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 02 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449925):
then nobody would know which scheme you were talking about

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449926):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 02 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449969):
Somehow, I feel that `class group (\a : Type) := ...` is related to the abuse of notation where we identify a group with its underlying set

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 02 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449970):
we feel that we can identify the group just by naming the set

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449976):
I do think it is rare that you find yourself putting two group structures on one set

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449978):
and even if it happened you could imagine that it was for some temporary calculation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127449980):
possibly which ultimately even proved they were equal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450019):
on the other hand I'd say just the same thing about schemes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 02 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450020):
but I guess, do you think of a scheme as a set equipped with "scheme structure"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450023):
Maybe it's a locally-ringed space with a scheme set-of-axioms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 02 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450032):
Yes, that seems much better

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450033):
oh god that would make it a dreaded subtype

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 02 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450041):
Anyways, you wouldn't be able to write `instance (scheme α) (scheme β) : scheme (α × β)` to get `α × β` notation for product schemes because the underlying set is wrong

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450081):
As a mathematician I find it extremely hard to distinguish whether I "think about a scheme as a set equipped with the structures of a topological space, a sheaf of rings on the space and an axiom about the rings"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450082):
or whether I "think about it as a locally ringed space equipped with an axiom"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450093):
By the way re: your prime question, there is the naming convention of capitalizing `p : Prime` for bundled structures

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450095):
oh great! Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 02 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450150):
Yeah, I think it's hard to pin anything down too precisely in this direction.
That's why I wrote "practical advantages" above :simple_smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450200):
current v

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450201):
https://gist.github.com/kbuzzard/327a9c466e3aaecf38fe93109ef8fde6

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450202):
of Prime

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450230):
```quote
Yes, that seems much better
```
So a scheme should extend a locally ringed space by adding one axiom?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450234):
Ha ha that would break my proof that affine schemes are schemes :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450235):
the dirty truth coming out :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450279):
I figured that I could define a scheme to be a topological space with a sheaf of rings which was locally an affine scheme

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450281):
because this would imply it was a locally ringed space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450282):
I was cutting corners :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 05:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450288):
and you wonder why I think it isn't ready for mathlib...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 02 2018 at 05:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450291):
Oh, I forgot "locally ringed" includes an extra condition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450748):
```quote
I do think it is rare that you find yourself putting two group structures on one set
```
I think the most famous example is Eckman-Hilton for homotopy groups.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450791):
And indeed, you prove that they are the same group structure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450807):
Personally I definitely would love to be able to write `X \times Y` for the product of schemes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450851):
The only way that I currently see to make this happen, is that we have some sort of `has_cat_prod` notation for categorical products. And then a proof that `Schemes` has products.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450863):
Pullbacks become a problem (notationwise) because we cannot but a subscript scheme under the `\times`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450968):
I've got two elements of a ring.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450969):
Oh I know the bloody answer to what I was going to ask

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450970):
Mathematicians are great

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450971):
"use a subtype"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450972):
"elements a and b in R, with a dividing b in the subring S"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450974):
Having p as a subtype is awful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450975):
`x ^ p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450978):
Lean : ?!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450983):
yeah this is going to be difficult

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450986):
x is in a ring and p has a coercion to nat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450988):
you can either coerce, or have a `has_pow A Prime` instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127450991):
rofl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451034):
I coerce with \u?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451036):
lean can't coerce and do typeclass inference at the same time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451038):
you would have to say it's a nat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451043):
`x ^ (p:nat)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451055):
```quote
lean can't coerce and do typeclass inference at the same time
```
Is this something that might change in Lean 4?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451056):
I think that a prime typeclass might work better for you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451058):
no, that's unlikely to change

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451060):
if you think about it that's a really large search space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451099):
it's too underdetermined

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451100):
Yes, I agree. Somehow humans are extremely good at navigating that search space.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451102):
wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451103):
`example (R : Type) [comm_ring R] : has_pow R ℕ := by apply_instance `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451104):
is that not a thing? Doesn't run for me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451109):
you have `algebra.group_power`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451114):
I have one lying around somewhere

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451214):
How about adding p as a constant and the fact that it's prime as an axiom?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451215):
Is that just a bridge too far?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451223):
so if the predicate is called `prime` and the subtype `Prime`, what is the typeclass called?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127451224):
`is_prime` I guess?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453513):
eew

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453514):
`definition complete (R : Type) [topological_space R] [ring R] [topological_ring R] : Prop := sorry `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453551):
is that going away in Lean 4?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453554):
Yes, we've decided that no one needs topology anymore

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453555):
you're going to use sites?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453564):
nothing but pointless topology for us

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453565):
No, infty-topoi.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453569):
```quote
nothing but pointless topology for us
```
```lean
definition complete (R : Type) [pointless_topological_space R] [ring R] [pointless_topological_ring R] : Prop := sorry 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453606):
much better

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453618):
Kevin, so the problem is that `topological_ring` should imply `ring` and `topological_space`, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453662):
I don't know why I had to say all three

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453664):
Maybe @**Johannes Hölzl** should field this one, I'm not sure why it's not a class extending those others

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453704):
I tried using type class inference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453705):
`class perfectoid_ring (R : Type) [Tate_ring R] (p : ℕ) [is_prime p] :=`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453710):
and then when I ask type class inference to prove the hypothesis that R is a perfectoid ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453711):
I mean I know why you had to write that, are you asking what is happening or why is it set up that way?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453755):
I have typeclass woes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453757):
I am writing my flagship definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453759):
so it has to look lovely

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453760):
and I write ` [∀ i, perfectoid_ring (R i) p]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453761):
and curse the `p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453763):
and it complains that it can't see why `R i` is a Tate ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453769):
because perfectoid ring depends on Tate ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453813):
The way you declared it, you always have to write `[Tate_ring R] [is_prime p] [perfectoid_ring R p]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453821):
since `perfectoid_ring ` takes the other two as parameters

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453882):
```lean

class perfectoid_ring (R : Type) [Tate_ring R] (p : ℕ) [is_prime p] :=
(is_complete : complete R)
(is_uniform  : uniform R)
(ramified    : ∃ ω : R ᵒ, 
                 (is_pseudo_uniformizer ω) ∧ (ω ^ p ∣ p))
 (Frob       : ∀ a : R ᵒ,
                 ∃ b c : R ᵒ, a = b ^ p + p * c)

structure foo (p : ℕ) [is_prime p] :=
(hello : ∃ (R : Type) [perfectoid_ring R p], 1 + 1 = 2) -- failed to synthesize Tate_ring
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453922):
`(hello : ∃ (R : Type) [Tate_ring R] [perfectoid_ring R p], 1 + 1 = 2) `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453923):
works but looks silly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453924):
of course it's a Tate ring -- it's a perfectoid ring!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453925):
It can't synthesize any of those classes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453931):
it's right of the colon, so no typeclass inference for you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453932):
So, you should extend Tate_ring?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453935):
use `by exactI` to workaround

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453936):
but I don't want by exactI everywhere

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453937):
it's an ugly hack

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453976):
Wait we're talking about different things again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453978):
to make Tate_ring inferrable from perfectoid_ring, just make it `extends` the other

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127453983):
instead of taking it as parameter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454080):
I changed for a reason

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454128):
Why did you write out the divisibility condition instead of using the existing definition?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454264):
I didn't know how to reduce mod p offhand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454265):
so just wrote something mathematically equivalent

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454271):
reducing mod p would be fine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454311):
I'd just need to look up how to make a principal ideal and then quotient out by an ideal, and then I would have had to verify that the p'th power map was well-defined on the  quotient

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454313):
or you could write `p | b ^ p - a`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454314):
try that with a subtype

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454322):
?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454324):
just noting that a lot of coercion would be happening if we used subtypes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454325):
for p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454367):
I don't recommend it. You need it more often as a nat than a prime

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454376):
```
type mismatch at application
  pow b
term
  b
has type
  :Rᵒ
but is expected to have type
  ℕ
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454415):
b has type some strange smiley

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454422):
`                 ∃ b : R ᵒ, (p : R ᵒ) ∣ (b ^ p - a))`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 02 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454425):
looks less cool

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454720):
Hmm, this doesn't score many readability points with me...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454727):
why? that seems plenty readable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454728):
you may also be able to get away with just `\u p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454771):
Well, we are optimising this definition for maximal readability, because it will be the first Lean a lot of mathematicians will read this summer.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454772):
And then `(p : R ᵒ)` will already scare them away.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454773):
Why is it even there?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454779):
because `p` is a nat but it is being mapped into the ring so it can be a divisor

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454781):
Can't we tell somewhere else that this division happens in `R ᵒ` ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 02 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454785):
yes, that's why I suggested `\u p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454833):
I think in the end, I would rather prefer something close to `∃ b : R ᵒ, a = b ^ p mod p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454835):
Even if it is just notation for what we had before.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 02 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127454876):
@**Kevin Buzzard** something like that should be possible. And then you don't need quotient rings.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jun 02 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127458263):
```quote
Maybe @**Johannes Hölzl** should field this one, I'm not sure why it's not a class extending those others
```
If `topological_ring` would contain the topology or the ring itself, then we would need to duplicate the algebraic and topological type class hierarchy.  So we would need a `topological_domain`, a `uniform_space_ring`, a `uniform_domain` etc. by keeping it a relation this type class hierarchy duplication is avoided. Also `topological_ring` is a `Prop` now, so we can add arbitrary instances proving that something is a `topological_ring` without worrying that they are definitional equal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127515805):
OK so a perfectoid space is an adic space with some properties, so we need to develop the theory of adic spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127515855):
and a basic constructor for adic spaces is the `Spa` function, which takes as input a so-called "Huber pair" and outputs an affinoid pre-adic space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127515865):
I am thinking about how to formalize that in Lean and I have a question regarding the input, that is, the Huber Pair.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127515909):
A Huber Pair is a topological ring $$R$$ satisfying some axioms, and a subring $$R^+$$ satisfying some more axioms related to both $$R^+$$ and how it sits in $$R$$.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127515917):
So I can envisage several ways of setting this up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127515966):
and what of course I would really like to know is which one is the "best" way, where by "best" I mean "one for which the interface will be easiest to write".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127515968):
so how do I analyse this further?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127515970):
I definitely want easy access to $$R$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127516022):
and most of the time, when creating new pairs from old, you build the new $$R$$ from the old $$R$$ and then let the new $$R^+$$ be "the same construction but with $$R^+$$"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127516024):
e.g. new $$R^+$$ could be the image of the old $$R^+$$ or whatever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127516027):
and occasionally $$R$$ stays the same but $$R^+$$ changes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127516032):
one could think of changing $$R^+$$ as "changing $$R$$ infinitesimally"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127516034):
"so mostly you don't notice"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127516038):
and everything will be a topological ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127516076):
and every map will be continuous

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127516084):
and we'll be building things like "polynomial ring over a Huber Pair", sending $$(R,R^+)$$ to $$(R[X],R^+[X])$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127516087):
or "completion of a Huber Pair", sending $$(R,R^+)$$ to $$(\hat{R},\hat{R}^+)$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127516134):
where $$\hat{R}$$ is a certain kind of completion of $$R$$ etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 03 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127516137):
and $$\hat{R}^+$$ is the topological closure of $$R^+$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127517460):
I'm going to make a structure containing $$R$$ and $$R^+$$, and rely on `has_coe_to_sort` to enable me to treat it as `R`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127517466):
Is there trouble ahead?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127517537):
There will be maps between different $$R$$s but in TPIL they sketch a method of how to use `has_coe_to_fun` which was designed for this purpose I guess.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127518088):
@**Kenny Lau** I am looking at the definition of f-adic ring in Wedhorn's notes (section 6.1) and he talks about a finitely-generated ideal of a ring. What's the best way of saying "there exists a finitely-generated ideal of R such that blah" in Lean, for a `comm_ring`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 04 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127518093):
we have all about that in `linear_algebra/something` I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 04 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127518097):
they proved that every vector space has a basis

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127518100):
http://www2.math.uni-paderborn.de/fileadmin/Mathematik/People/wedhorn/Lehre/AdicSpaces.pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127518113):
it's the finiteness I am interested in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127518114):
I just want a smooth way of formalizing that definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127518116):
p46 of the pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 04 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127518117):
finiteness is just either `fintype` or `set.finite`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127518159):
OK I'll write something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127518161):
and then you can laugh at me :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 04 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127518162):
```lean
/-- Linear span of a set of vectors -/
def span (s : set β) : set β := { x | ∃(v : lc α β), (∀x∉s, v x = 0) ∧ x = v.sum (λb a, a • b) }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 04 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127518164):
https://github.com/leanprover/mathlib/blob/master/linear_algebra/basic.lean#L122

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127518165):
Oh!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127518167):
I forgot -- see you on the R thread

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127519719):
Does this already have a name in mathlib:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127519721):
`definition is_cover {X γ : Type} (U : γ → set X) := ∀ x, ∃ i, x ∈ U i`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 04 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127519834):
```lean
lemma compact_elim_finite_subcover {s : set α} {c : set (set α)}
  (hs : compact s) (hc₁ : ∀t∈c, is_open t) (hc₂ : s ⊆ ⋃₀ c) : ∃c'⊆c, finite c' ∧ s ⊆ ⋃₀ c' :=
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 04 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127519835):
https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_space.lean#L475

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127519839):
```lean
structure Huber_Pair (R : Type) :=
[is_Hring : Huber_ring R]
(Rp : set R)
[intel : is_ring_of_integral_elements Rp]

structure Huber_Pair' (R : Type) [Huber_ring R] :=
(Rp : set R)
[intel : is_ring_of_integral_elements Rp]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127519890):
Is the first one just silly or does it ever have its uses?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127519897):
A Huber Pair is a Huber Ring plus a subring which is a ring of integral elements (i.e. satisfies a bunch of axioms)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127519913):
```quote
https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_space.lean#L475
```
`is_cover` is about as long as `s ⊆ ⋃₀ c`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 04 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127519915):
lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127519954):
it's all about the interface though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127519974):
`(R⁺ : set R)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520012):
what is this "unexpected token" error?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520018):
can I PR it in somehow?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520022):
hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520024):
can I use it in notation?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520077):
yes :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520414):
```quote
Is the first one just silly or does it ever have its uses?
```
aargh the second one doesn't compile :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520418):
because of type class inference woes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520461):
`definition is_ring_of_integral_elements {R : Type} [Huber_ring R] (Rplus : set R) : Prop := sorry`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520464):
needs huber ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520514):
*boggle* <goes back to type class woes thread>

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 04 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520522):
I don't understand why that would make the second one not compile

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520617):
no I am an idiot

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520618):
it works fine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520619):
I am still very unsteady on my feet with typeclasses

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520659):
all I know is "it sometimes doesn't work" and it's something about where the colon is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520797):
```lean
structure Huber_pair :=
(R : Type) 
[RHuber : Huber_ring R]
(Rplus : set R)
[intel : is_ring_of_integral_elements Rplus]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520800):
This is annoying

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520804):
I don't think I can use type class inference to get a Huber pair structure on R, because I want the freedom to change $$R^+$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520809):
`postfix `⁺` : 66 := λ R : Huber_pair _, R.Rplus  `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520813):
and if I add it as a family of structures on R

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520814):
then I am forever having to make R and then the pair

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520817):
I can't just say "Let $$R$$ be a Huber Pair" like we'd say in maths

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520863):
So, often a good solution when you want two different typeclasses on the same underlying type,

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520868):
is to use the trick that Mario showed me, of making a "wrapper".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520871):
As an example, to define the opposite category, I use:
````
def op (C : Type u₁) : Type u₁ := C

notation C `ᵒᵖ` := op C

variable {C : Type u₁}
variable [𝒞 : category.{u₁ v₁} C]
include 𝒞

instance Opposite : category.{u₁ v₁} (Cᵒᵖ) := ...
````

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520912):
Here the idea is that `op C` is of course just `C`, "thought of" as objects of the opposite category.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520922):
It's something mathematicians do all the time and are perfectly comfortable with, and maybe works for your Huber pairs setting, in particular when you want to change R+, but leave R alone.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127520975):
On the other hand, I suspect that you never ever actually want to look at an element of the `R` of a Huber pair, so making a typeclass on `R` maybe doesn't have that much value.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127521056):
I think I will forever be playing around with pi's and p's in R I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127521060):
as I explicitly evaluate my completions etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 04 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127521063):
Scratch that suggestion then!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 04 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127540813):
```quote
I can't just say "Let $$R$$ be a Huber Pair" like we'd say in maths
```
I think it is important that we try to keep this "feature". But I don't see how to implement it in Lean, and also give you the freedom to change `R⁺`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 04 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127540890):
Unless we also have some postfix accessor notation for the ambient ring. So that a Huber pair `R` is `(R^?,R⁺)`. But I don't have any cute ideas for what `?` should actually be. And it is going to be annoying and offputing for mathematicians anyway.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 04 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127541067):
Could that notation for the ambient ring just be a coercion?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 04 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127541198):
```lean
structure Huber_pair :=
(R : Type)
[is_ring : ring R]
(Rp : set R)
(huber : true)

instance : has_coe_to_sort Huber_pair :=
{ S := Type, coe := Huber_pair.R }   

instance Huber_pair.ring (R : Huber_pair) : ring R := R.is_ring
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 04 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127541212):
I think @**Kevin Buzzard** is currently the only one who knows enough about Huber pairs to see if this will give trouble down the road.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 04 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127541258):
```lean
notation R `⁺`:99 := R.Rp
variables {R : Huber_pair} {x : R} {h : x ∈ R⁺}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 04 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127541260):
Yes, probably.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 04 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127541391):
So far that looks promising, I would say.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Jun 04 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127541994):
 I am trying to understand the maths a little bit more, to see if I can help. But I am a bit lost. In @**Kevin Buzzard**'s  [first ref](http://www2.math.uni-paderborn.de/fileadmin/Mathematik/People/wedhorn/Lehre/AdicSpaces.pdf), p46 defines what an f-adic ring is, but there is no f right? Can I understand them as an I-adic ring? Then, for the question on Huber pairs. I do not understand this "pair" vocabulary yet. Can I think of $$R$$ as an ambiant (topological) ring, and $$R^+$$ as the actual interesting thing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 04 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127542016):
I think both rings in a Huber pair are interesting...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 04 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127542064):
It is like $$\mathbb{Z} \subset \mathbb{Q}$$ on steroids.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 04 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127542079):
Also, I think the "f" in *f-adic* stands for finite: there is a finiteness condition in both items in the condition, first on the subset $$T$$, and then on the ideal $$I$$ in the second condition of the definition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 04 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127542135):
Disclaimer: I'm not an expert on this stuff. Only followed some seminars on this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Jun 04 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127542992):
Sorry my sentence was misleading and in fact I think it was even nonsensical, as  $$A^+$$ should be integrally closed in $$A$$.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 04 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127543129):
~~Don't you mean it the other way round?~~

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Jun 04 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127543178):
Thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127543965):
```quote
 I am trying to understand the maths a little bit more, to see if I can help. But I am a bit lost. In @**Kevin Buzzard**'s  [first ref](http://www2.math.uni-paderborn.de/fileadmin/Mathematik/People/wedhorn/Lehre/AdicSpaces.pdf), p46 defines what an f-adic ring is, but there is no f right? Can I understand them as an I-adic ring? Then, for the question on Huber pairs. I do not understand this "pair" vocabulary yet. Can I think of $$R$$ as an ambiant (topological) ring, and $$R^+$$ as the actual interesting thing?
```
Yes "f-adic ring" is a terrible name, there is no f, "f-adic ring" is just a ring with some structure and some axioms. In fact it's such a terrible name that Scholze proposed renaming it to "Huber ring" and that's what we're going to use in the project.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127544039):
The modern terminology is that $$R$$ is a Huber ring and $$(R,R^+)$$ is a Huber pair. In the old terminology $$R$$ is an f-adic ring and $$R^+$$ is a ring of integral elements (I guess this definition will stay)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127544056):
So many of the proofs do not care about $$R^+$$, but I am beginning to see more about how this is going to work. I suspect often we will not make the Huber pair -- we will just have a ring $$R$$ and a subring $$R^+$$ and do calculations with them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564051):
Should I have `structure perfectoid_space := (X : Type) ...` or `structure perfectoid_space (X : Type) := ...`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564056):
I was using the latter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564063):
but here's something I ran into.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564135):
A perfectoid space is a topological space equipped with a presheaf of rings and satisfying a bunch of axioms.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564153):
A presheaf of rings on a topological space is the assignment, for every open subset U of the topological space, of a ring $$F(U)$$, and a bit more data, and some axioms.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564242):
Given a perfectoid space $$X$$, and an open subset $$U$$ of the underlying topological space (which is also called $$X$$), I can pull back all the structure and get a perfectoid space structure on $$U$$ (e.g. I need to associate a ring to an open subset of $$U$$, but an open subset of $$U$$ is an open subset of $$X$$ so we use the presheaf of rings on $$X$$ to do this).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564243):
So far so good.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564264):
But I was kind of expecting `perfectoid_space` to be a typeclass

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564288):
and (finally the question!) I don't know how to get type class inference to get us from X to U

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564346):
because U is an open set in X so it's not even a type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564366):
and if we use the associated subtype `{x : X // x \in U}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564378):
then I don't know how to say "...oh, and U needs to be open" to type class inference.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564399):
In short -- if I have `(X : Type) [perfectoid_space X]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564446):
(perfectoid space extends topological space)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564461):
and if `(U : set X)` is open

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564501):
then my instance wants to look like `(X : Type) [perfectoid_space X] (U : set X) (HU : is_open U) : perfectoid_space {x : X // x \in U}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564555):
"an open subset of a perfectoid space is a perfectoid space"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564574):
but how is type class inference going to spot that U is open?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564631):
I guess I could work with subtypes and make is_open a typeclass on them? Is this crazy? Would it even work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564861):
Or should I just give up on making perfectoid space a typeclass?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127564911):
Presumably typeclass inference only works on things which have been tagged as classes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Jun 04 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127565448):
I would say it makes sense to make them either both typeclasses or plain structures (you can still write a function to do what you want to do with typeclass inference there, I think); perhaps it wouldn’t hurt to start with all the structure explicit, and then determine what could be converted to use typeclass machinery ...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Jun 04 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127565546):
`theorem perfectoid_space_on_open_set (X : Type) (U : set X) (HU : is_open U) : perfectoid_space X -> perfectoid_space {x : X // x \in U}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127565731):
So I can prove that theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127565739):
my question is whether I can persuade the type class inference system to use it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127565748):
if `perfectoid_space` is a class

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127565756):
and what I can't get my head around

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127565766):
is how type class inference can possibly guess that a subset is open

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Jun 04 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127565777):
I agree, that’s why I think `is_open` would also have to be a typeclass

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127565788):
but there is a technical problem there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127565792):
because U is not a type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127565793):
it's a term

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127565853):
hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127565857):
I am just assuming that it's impossible to make this work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127565861):
Does it actually work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127565903):
I somehow can't get it all to fit together but maybe it's possible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Jun 04 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127565961):
aren’t the (ring, group) homomorphisms classes? I don’t see how a set would be much different

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Jun 04 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127566151):
`class is_ring_hom`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127566567):
That's true!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127566572):
Maybe it all just works?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127566720):
`variables {X : Type} [topological_space X]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127566745):
```lean
class is_open (U : set X) : Prop :=
(is_open : is_open U)
```
 or some such thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 04 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127566800):
hmm maybe I need to think a bit about variable names...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 04 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127567528):
You can potentially also just make `is_open` into a class, with `attribute [class] is_open` (or `local attribute`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127571664):
I don't have time for this now but hopefully I'll be able to get to it tomorrow. Once I've resolved this I think I'm ready to go. I've been writing stuff from the top down, i.e. I have a definition of a perfectoid space but it depends on several other definitions, some of which I have and some of which I don't. Up here it feels very close to maths and looks very close to maths too.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127586717):
Are doing all this privately in the end?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127588260):
No not at all -- but I wanted to get the definition of perfectoid space written (modulo lots of other definitions which are not written)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127588261):
before I "went public" as it were

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127588263):
I am currently struggling with type class inference issues but I think I had the same ones before

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127588266):
so I will look in the old thread

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589169):
Patrick here's the state of things:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589172):
```lean
import adic_space 

--notation
postfix `ᵒ` : 66 := power_bounded_subring

/-- A perfectoid ring, following Fontaine Sem Bourb-/
class perfectoid_ring (R : Type) (p : ℕ) [is_prime p] extends Tate_ring R :=
(is_complete : complete R)
(is_uniform  : uniform R)
(ramified    : ∃ ω : R ᵒ, (is_pseudo_uniformizer ω) ∧ (ω ^ p ∣ p))
(Frob        : ∀ a : R ᵒ, ∃ b : R ᵒ, (p : R ᵒ) ∣ (b ^ p - a))

structure perfectoid_space (X : Type) (p : ℕ) [is_prime p] extends adic_space X :=
(perfectoid_cover : 
  -- gamma is our indexing set, U_i are the open cover for i in gamma
  ∃ {γ : Type} (U : γ → set X) [U_open : ∀ i, is_open (U i)] (U_cover : is_cover U)
  -- U i is isomorphic to Spa(A_i,A_i^+) with A_i a perfectoid ring
  (A : γ → Huber_pair) (is_perfectoid : ∀ i, perfectoid_ring (A i) p),
  ∀ i, is_preadic_space_equiv {x : X // x ∈ (U i)} (Spa (A i))    ) 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589173):
doesn't quite typecheck

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589195):
but once it does it's very readable if you already know pretty much what a perfectoid space is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589225):
`adic_space` full of sorries

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589233):
I am in the middle of writing some long issues explaining exactly what needs to be done to finish the job, plus references

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589248):
`is_preadic_space_equiv` extends `homeo` -- did you get that into mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589367):
The problem, by the way, is `failed to synthesize ⊢ preadic_space {x // x ∈ U i}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589375):
`instance preadic_space_restriction {X : Type} [preadic_space X] {U : set X} [is_open U] :
  preadic_space {x : X // x ∈ U} := sorry`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589393):
so all the ingredients are there -- a proof that U i is open, an instance saying an open subspace of a preadic space is a preadic space, oh and adic_space extends preadic_space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Jun 05 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589489):
The  ``` ∃ {γ : Type}``` looks very suspicious to me. Is it really what you want? And not a set of some type?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 05 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589621):
@**Assia Mahboubi** , could you explain why it looks suspicious? I've seen the same sentiment expressed about similar things, but never really understood how you decide between indexing by a type, and having a set of things. The one time I tried both approaches (defining a Grothendieck topology), it eventually became clear that the set approach was smoother, but I didn't really grok why that was the case.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589634):
This is supposed to say "my topological space has a cover by nice topological subspaces"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589636):
but the actual cover is not part of the structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589642):
it's just the fact that such a cover exists

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589657):
for each `i : gamma` I need an open set U_i and a ring A_i and an isomorphism Spa(A_i) = U_i

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589718):
Here's a MWE of my final problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589723):
```lean
import analysis.topology.topological_space

attribute [class] is_open 

class preadic_space (X : Type) extends topological_space X 

class adic_space (X : Type) extends preadic_space X

structure Huber_pair : Type 

definition Spa (A : Huber_pair) : Type := sorry

instance Spa_topology (A : Huber_pair) : topological_space (Spa A) := sorry 

structure preadic_space_equiv (X Y : Type) [AX : preadic_space X] [AY : preadic_space Y] extends equiv X Y

definition is_preadic_space_equiv (X Y : Type) [AX : preadic_space X] [AY : preadic_space Y] := 
  nonempty (preadic_space_equiv X Y)

structure not_perfectoid_space (X : Type) (p : ℕ) extends adic_space X :=
(perfectoid_cover :
  -- gamma is our indexing set, U_i are the open cover for i in gamma
  ∃ {γ : Type} (U : γ → set X) [U_open : ∀ i, is_open (U i)]
  (A : γ → Huber_pair),
  ∀ i, is_preadic_space_equiv {x : X // x ∈ (U i)} (Spa (A i))) 

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589727):
I might have just made a stupid mistake

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589806):
oh ignore all this I am sure I have made a stupid mistake -- my error is somewhere else now in the MWE. I just need to sort this out myself. I think I'm there but just being stupid

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589859):
```lean
import analysis.topology.topological_space

attribute [class] is_open 

class preadic_space (X : Type) extends topological_space X 

class adic_space (X : Type) extends preadic_space X

structure Huber_pair : Type 

definition Spa (A : Huber_pair) : Type := sorry

instance Spa_topology (A : Huber_pair) : topological_space (Spa A) := sorry 

instance (A : Huber_pair) : preadic_space (Spa A) := sorry 

structure preadic_space_equiv (X Y : Type) [AX : preadic_space X] [AY : preadic_space Y] extends equiv X Y

definition is_preadic_space_equiv (X Y : Type) [AX : preadic_space X] [AY : preadic_space Y] := 
  nonempty (preadic_space_equiv X Y)

structure not_perfectoid_space (X : Type) (p : ℕ) extends adic_space X :=
(perfectoid_cover :
  -- gamma is our indexing set, U_i are the open cover for i in gamma
  ∃ {γ : Type} (U : γ → set X) [U_open : ∀ i, is_open (U i)]
  (A : γ → Huber_pair),
  ∀ i, is_preadic_space_equiv {x : X // x ∈ (U i)} (Spa (A i))) 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589862):
`failed to synthesize type class instance for ⊢ preadic_space {x // x ∈ U i}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589865):
That's my problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589876):
I think maybe type class inference doesn't know `U i` is open

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589884):
but I thought that `[U_open : ∀ i, is_open (U i)]` would tell it this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589885):
but it might all be happening too quickly for type class inference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 05 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127589932):
Is it because you should be using a coercion to subtype instead of this `{x // x ∈ U i}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Jun 05 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127590175):
@**Scott Morrison** : disclaimer: I do not know what Groethendick topology is. But it is much more difficult to "combine" things which have different types. For instance, if two families are indexed using two a priori distinct types, then in order to speak about the family obtained as the union of these two, you always first have to craft a new type for the indices of this union, which will be something like the sum type of the two previous index types (phew). As opposed to offering the option, when possible, to use the union set of two sets (indexed with the same nature of datas, ie. with sets of a same type).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127590308):
```quote
This is supposed to say "my topological space has a cover by nice topological subspaces"
```
You could consider $$\mathcal{U}$$ a subset of the powerset of `X`, and then demand for every `U : calU` that it is open, and that `calU` is a cover.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127590358):
I guess that `is_cover` is something you defined yourself. I didn't find it in mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127590450):
@**Assia Mahboubi** But with indexing sets you usually don't want to take the union (in some ambient set) right? You would want to take the disjoint union. And the mathematician in me doesn't really see why disjoint unions or sum types differ in complexity. Please enlighten this DTT newbie (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127590761):
```lean
instance preadic_space_restriction {X : Type} [preadic_space X] {U : set X} [is_open U] :
  preadic_space {x : X // x ∈ U} := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127590858):
```lean
import analysis.topology.topological_space

attribute [class] is_open 

class preadic_space (X : Type) extends topological_space X 

class adic_space (X : Type) extends preadic_space X

structure Huber_pair : Type 

definition Spa (A : Huber_pair) : Type := sorry

instance Spa_topology (A : Huber_pair) : topological_space (Spa A) := sorry 

instance (A : Huber_pair) : preadic_space (Spa A) := sorry 

structure preadic_space_equiv (X Y : Type) [AX : preadic_space X] [AY : preadic_space Y] extends equiv X Y

definition is_preadic_space_equiv (X Y : Type) [AX : preadic_space X] [AY : preadic_space Y] := 
  nonempty (preadic_space_equiv X Y)

instance preadic_space_restriction {X : Type} [preadic_space X] {U : set X} [is_open U] :
  preadic_space {x : X // x ∈ U} := sorry

structure test (X : Type) extends adic_space X :=
(loc: ∃ (U : set X) [U_open : is_open U] (A : Huber_pair),
  is_preadic_space_equiv {x : X // x ∈ U} (Spa (A)))  -- fails ⊢ preadic_space {x // x ∈ U}

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127590861):
Kevin, isn't there some coercion that turns `U` into a (sub)type? Because `{x : X // x ∈ U}` is really weird to a mathematician. (I understand that you are having troubles here... but I think we should aim to get rid of that expression in the end.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127590922):
We can't have everything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127590977):
```lean
import analysis.topology.topological_space

attribute [class] is_open 

class preadic_space (X : Type) extends topological_space X 

class adic_space (X : Type) extends preadic_space X

structure Huber_pair : Type 

definition Spa (A : Huber_pair) : Type := sorry

instance Spa_topology (A : Huber_pair) : topological_space (Spa A) := sorry 

instance (A : Huber_pair) : preadic_space (Spa A) := sorry 

structure preadic_space_equiv (X Y : Type) [AX : preadic_space X] [AY : preadic_space Y] extends equiv X Y

definition is_preadic_space_equiv (X Y : Type) [AX : preadic_space X] [AY : preadic_space Y] := 
  nonempty (preadic_space_equiv X Y)

instance preadic_space_restriction {X : Type} [preadic_space X] {U : set X} [is_open U] :
  preadic_space U := sorry

structure test (X : Type) extends adic_space X :=
(loc: ∃ (U : set X) [U_open : is_open U] (A : Huber_pair),
  is_preadic_space_equiv U (Spa (A)))  -- fails ⊢ preadic_space ↥U

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127590986):
Right, so the issue remains...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127590992):
Which is really annoying.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127591056):
Now we have weird arrows

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127591057):
I'm sure it can be fixed. The only reason I'm chatting about this at all is that Patrick wanted to know what was going on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127591062):
It would be a shame to have to start going on about letI or whatever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127591071):
My problem, i now realise, is that whilst Mario showed me how to overcome various typeclass inference issues in the schemes project

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127591111):
I don't actually understand what is going on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127591120):
I don't understand what the "type class inference machine" has access to at any time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127591125):
For example I am not even sure if it knows X is an adic space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127591240):
Kevin, the first lines of the error are:
```lean
failed to synthesize type class instance for
X : Type,
to_adic_space : adic_space X,
to_preadic_space : (λ {X : Type} (c : adic_space X), preadic_space X) to_adic_space := adic_space.to_preadic_space X,
```
That last line shows how to turn `X` into a `preadic_space`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127591242):
But it hasn't actually done it!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127591287):
Maybe if that term was actually an instance, then the machine would do the rest for you.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127591424):
Hmm, no. Because if I change the class of `X` to `adic_space` in `preadic_space_restriction`, then it still fails in `test`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127592068):
It's very easy to get Lean to say things like "I know `X : Y` and type class inference is failing to find anything of type `Y`"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127593408):
Do we know of any strategy for attacking this issue? Or should we wait 3 weeks till Mario and Johannes are back?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127594010):
```lean
structure test (X : Type) extends adic_space X :=
(loc: ∃ (U : set X) [U_open : is_open U] (A : Huber_pair),
  @is_preadic_space_equiv U (Spa (A)) (@preadic_space_restriction _ _ U U_open) _)
```
The trouble is with `U_open`. If I replace that with an `_`, then typeclass inference can't figure it out itself...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127594207):
```lean
--failed to synthesize type class instance for
⊢ _root_.is_open U
```
Is `_root_` a pointer to the trouble?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127594781):
Maybe. Kenny pointed this out to me too. There's a long typeclass thread which might solve my problems.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127594789):
Kenny suggested making another typeclass for subtypes being open

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127594794):
I don't see why that would fix things...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127594838):
The stupid system is looking in the root namespace for an instance of `is_open U`, but it should just look 2 lines up in the local context...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127594847):
It feels very much like a bug to me. (Wait. I'll first run this with `pp.all` set to true.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595002):
Ok, so this is another (ugly) way to get it to work.
```lean
structure test (X : Type) extends adic_space X :=
(loc: ∃ (U : set X) [U_open : @_root_.is_open.{0} X _ U] (A : Huber_pair),
  is_preadic_space_equiv U (Spa (A)))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595071):
I doubt it's a bug.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595074):
It's probably just how typeclass inference works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595075):
Yes, I also think that now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595093):
So, what the heck is the difference between `@_root_.is_open.{0} X _ U` and `is_open U`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595234):
One more golf (@**Kevin Buzzard**):
```lean
structure test (X : Type) extends adic_space X :=
(loc: ∃ (U : set X) [U_open : _root_.is_open U] (A : Huber_pair),
  is_preadic_space_equiv U (Spa (A))) 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595282):
So it really is about this `_root_` thingy. But at least now it looks somewhat readable again.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595308):
Of course a mathematician (like me!) doesn't know at all what `_root_` means, or what it is doing there. But hey! Cargo cult proofs for the win (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jun 05 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595461):
The problem is that `is_open` refers to two things here: the inherited field `topological_space.is_open` and the global definition `_root_.is_open`, which are different.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595510):
Aah, because of a long chain of `extends`, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595521):
Right, that makes a lot (*a whole lot*!) of sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595527):
It has been staring us right in the face, all the time.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595542):
So it is just some stupid overloading, and preferably one of the two `is_open`s should have another name.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595874):
Anyway, @**Gabriel Ebner** thanks for enlightening me!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595894):
@**Kevin Buzzard** 'nother problem solved. Next!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595943):
Definition currently looks like this:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595944):
```lean
structure perfectoid_space (X : Type) (p : ℕ) [is_prime p] extends adic_space X :=
(perfectoid_cover : 
  -- gamma is our indexing set, U_i are the open cover for i in gamma
  ∃ {γ : Type} (U : γ → set X) [Uopen : ∀ i, @_root_.is_open X _ (U i)] (U_cover : is_cover U)
  -- U i is isomorphic to Spa(A_i,A_i^+) with A_i a perfectoid ring
  (A : γ → Huber_pair) (is_perfectoid : ∀ i, perfectoid_ring (A i) p),
  ∀ i, is_preadic_space_equiv {x : X // x ∈ (U i)} (Spa (A i))    ) 

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595948):
Typechecks fine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595956):
The `is_open` overloading is one thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595957):
I guess you can remove the `@` and the `X _ `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595959):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127595960):
thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127596017):
And just a `(U i)` on the last line? Instead of all the `{x ... }`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127596119):
```lean
structure perfectoid_space (X : Type) (p : ℕ) [is_prime p] extends adic_space X :=
(perfectoid_cover : 
  -- gamma is our indexing set, U_i are the open cover for i in gamma
  ∃ {γ : Type} (U : γ → set X) [Uopen : ∀ i, _root_.is_open (U i)] (U_cover : is_cover U)
  -- U i is isomorphic to Spa(A_i,A_i^+) with A_i a perfectoid ring
  (A : γ → Huber_pair) (is_perfectoid : ∀ i, perfectoid_ring (A i) p),
  ∀ i, is_preadic_space_equiv (U i) (Spa (A i))    ) 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127596120):
I'm not happy with that `_root_` but everything else is great

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127596124):
Yes, completely agree.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127596126):
We should just overhaul the definition in `topological_space.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127596168):
It's only a silly namespacing issue.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127596174):
I it has a field `open_subsets` instead of `is_open`, then we're fine.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127596190):
can I fix this by writing my own `open` or `is_open'` or whatever?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127596248):
Probably even ``notation `is_open` := _root_.is_open`` would work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127596251):
Here's the full file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127596253):
```lean
import adic_space 

--notation
postfix `ᵒ` : 66 := power_bounded_subring

/-- A perfectoid ring, following Fontaine Sem Bourb-/
class perfectoid_ring (R : Type) (p : ℕ) [is_prime p] extends Tate_ring R :=
(is_complete : complete R)
(is_uniform  : uniform R)
(ramified    : ∃ ω : R ᵒ, (is_pseudo_uniformizer ω) ∧ (ω ^ p ∣ p))
(Frob        : ∀ a : R ᵒ, ∃ b : R ᵒ, (p : R ᵒ) ∣ (b ^ p - a))

structure perfectoid_space (X : Type) (p : ℕ) [is_prime p] extends adic_space X :=
(perfectoid_cover : 
  -- gamma is our indexing set, U_i are the open cover for i in gamma
  ∃ {γ : Type} (U : γ → set X) [Uopen : ∀ i, _root_.is_open (U i)] (U_cover : is_cover U)
  -- U i is isomorphic to Spa(A_i,A_i^+) with A_i a perfectoid ring
  (A : γ → Huber_pair) (is_perfectoid : ∀ i, perfectoid_ring (A i) p),
  ∀ i, is_preadic_space_equiv (U i) (Spa (A i))    ) 

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127596266):
I am really happy with all of it apart from the `_root_`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127596272):
Some mathlib classes have the actual field name with a trailing `'` to avoid this kind of collision

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127596317):
except now I can't find any

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127599582):
```quote
can I fix this by writing my own `open` or `is_open'` or whatever?
```
Sure, but you would also need all the simp-lemmas etc. That's why I suggested we might as well overhaul `topological_space.lean`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127599673):
And we have 6 commits! The game is on!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127600758):
@**Kevin Buzzard** What is your git workflow for this repo? fork -> feature branch -> push? Or just write access for everyone interested?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127602811):
Yeah, it should run. I have absolutely no idea about git workflows.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127602911):
I guess I do understand the question. For the stacks project I just let Kenny push anything -- I gave him write access. But for mathlib I have to do that fork feature push thing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127605457):
Ok, so this is your chance to level-up in git!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127607754):
Next job is the roadmap. I'll hopefully do this this evening (some issues explaining what needs to be done). Basically it's "type in a bunch of stuff from Wedhorn's paper"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127607824):
Kenny did chapter 1 but I'm sitting on it because it needs some non-mathlib imports

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127610418):
I like it that you moved the `_root_` issue out of the perfectoid file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127616339):
I'm sorry I missed this early fight. I was busy with administration all day (including writing letter to Jean-Pierre Serre explaining how to come to our new math building next week).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127616361):
Is there a reason why `perfectoid_spaces.lean` is not inside the `src` directory?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127616450):
```quote
Yeah, it should run. I have absolutely no idea about git workflows.
```
Did you try using https://github.com/jlord/git-it-electron to learn? I never tried but it seems to be popular

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617146):
Why not using ϖ (\varpi)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617158):
Here it looks ugly but in my VScode it looks ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617235):
Why the space in `R ᵒ`? It works fine and looks better as `Rᵒ`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617242):
I'm such an expert about perfectoid spaces now...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617264):
Is `instance subring_to_ring (R : Type) : has_coe (power_bounded_subring R) R := ⟨subtype.val⟩` meant to be useful right now? Deleting it changes nothing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617602):
Is there any reason to use gamma instead of iota for the indexing type?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617609):
no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617613):
iota is the mathlib tradition, and consistent with using `i` as a variable name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617619):
OK

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617622):
I guess the thing is never named in math papers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617623):
I can change all these things. Thanks for the review!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617632):
Now, serious question:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617674):
$$\coprod R_i$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617677):
who needs a name for the index set

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617679):
maybe I'll call it `_`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617683):
You should not use existential quantification over `Type` in your definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617688):
eew

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617691):
for the index set

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617695):
Is this the thing Assia was also unhappy about?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617699):
Yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617702):
What about this strange way of putting things before and after the existential comma?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617707):
It will needlessly push up the universe level of the definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617712):
How do you do it then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617715):
And why naming instance implicit variables you don't use in the def?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617722):
Even though it's inside an `\ex`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617723):
Instead you should quantify over all families that could possibly matter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617724):
What about:
```lean
structure perfectoid_space (X : Type) (p : ℕ) [is_prime p] extends adic_space X :=
(perfectoid_cover : 
  -- gamma is our indexing set, U_i are the open cover for i in gamma
  ∃ (ι : Type) (U : ι → set X) [∀ i, is_open (U i)]
  -- U i is isomorphic to Spa(A_i,A_i^+) with A_i a perfectoid ring
  (A : ι → Huber_pair) [∀ i, perfectoid_ring (A i) p],
  (is_cover U) ∧ ∀ i, is_preadic_space_equiv (U i) (Spa (A i)))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617732):
Does it make any difference (what I wrote vs Kevin's version)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617793):
oh, actually reid you're right, impredicativity makes it okay

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617805):
Note that all data and instance implicit stuff is left of comma, and conditions are right of comma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617809):
Still, I would prefer to quantify over subsets of set X

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jun 05 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617820):
Maybe you should make `ι` a field of `perfectoid_space` (and the others as well).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617824):
unless there is a reason that having many duplicates adds power?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617850):
What Gabriel says was my next question

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617853):
There are a lot of equivalent ways one could write this definition, but this way matches the way we speak

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617898):
I agree it looks more mathematicial, I'm asking if this will bring pain

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617906):
alternatively, name the thing "perfectoid cover" or something and existentially quantify in the structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617927):
^ also sounds nice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617928):
i.e. define what is a perfectoid cover and define a perfectoid space to be one which has a cover

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617948):
But again it would sound further away from math-speak

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617952):
It think having the cover be a term of type `set (set X)` is not "un-mathematical". Except for the fact that we would call `set X` something like `subset_of X`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127617967):
or "powerset"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618031):
My definition is readable by mathematicians

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618032):
In fact, in math usually open covers are defined to be subsets of the collection of open sets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618039):
and I don't understand what the problem with it is yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618049):
This thing with the indexing set makes it look like some kind of étale covering but it's actually a honest covering, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618057):
I have an exotic construction "Spa" which basically takes a ring and spits out a "special" topological space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618058):
The thing is that often one has some auxiliary data attached to each member of the cover, and then indexing the set with the set itself is awkward (what if the other data is not a function of the set)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618078):
and the claim is that my perfectoid space has a covering by these "special" spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618081):
that's the theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618099):
What Reid wrote seems important to me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618101):
@**Patrick Massot** yes it's just an honest covering of a topological space by open subsets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618104):
It's good to know that you only "need" to talk about small things in the definition and prove that you can do it even for large families

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618142):
@**Patrick Massot**, did you ever write down a definition of manifold?
Even if it is just parameterized on a variable (i.e., not yet defined) notion of "smooth" maps of R^n, it might be an interesting exercise.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618154):
```quote
Maybe you should make `ι` a field of `perfectoid_space` (and the others as well).
```
The covering and the set indexing the covering are *not* part of the data of a perfectoid space.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618160):
Even if you quantify over type 0 in the definition, you might want a family in type 1 and then you have a theorem to prove anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618165):
A perfectoid space is a space for which such a cover exists

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618183):
No I'm stuck in type class loops, `out_param` hell when I try to put a norm on R^n

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618202):
But indeed I could try to write the definition sorrying the definition of diffeomorphisms between open subsets of R^ n

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618205):
I understood everything Patrick said but I'm having trouble with these CS objections about iota. Can someone suggest something which you'd be happy with but which is the same idea and which is still readable by mathematicians?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618281):
Note that my version of `perfectoid_space` quoted above is a variation in a direction orthogonal to this question of iota vs subsets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618291):
just use `U : set (opens X)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618295):
```quote
i.e. define what is a perfectoid cover and define a perfectoid space to be one which has a cover
```
Aah I do understand this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618353):
for more readability, it should probably be more like `cover : set (opens X)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618388):
Oh wait, you already have an example of the issue I was bringing up earlier here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618399):
We also have this `(A : ι → Huber_pair) [∀ i, perfectoid_ring (A i) p]` stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618415):
BTW I think the `p` should come first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618421):
because it's the parameter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jun 05 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618473):
> The covering and the set indexing the covering are not part of the data of a perfectoid space.

Existentials are problematic since you'll have to use choice to access them, and in general you won't get the data back that you used to construct the perfectoid space in the first place.  If you make them fields, then you can actually get back the Huber pair `A` that you used to construct the perfectoid space---just via definitional reduction.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618493):
He doesn't want to get it back

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618507):
It's not part of the structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618938):
```quote
for more readability, it should probably be more like `cover : set (opens X)`
```
and now I need a Huber Pair for each element of the cover

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618944):
What about Reid's concern? That we are not only indexing open subsets, but also other stuff with the same indexing set/type?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127618989):
I think in this case, you could write something like "there exists a set of open subsets which cover X and for each of these subsets, a Huber pair" such that ...". But there is a small subtlety here, in that the original definition allows you to choose the same open subset repeatedly with different Huber pairs. Here, there's no reason why you would want to do that, so it ends up not mattering.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619007):
But if you try to define a smooth manifold, you cannot begin "there exists a set of open subsets which cover M and for each of these subsets, a continuous function to R^n such that ..."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619013):
that's what makes the theorem not completely trivial

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619035):
```quote
But if you try to define a smooth manifold, you cannot begin "there exists a set of open subsets which cover M and for each of these subsets, a continuous function to R^n such that ..."
```
Huh, why not?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619036):
theorem claiming this doesn't matter?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619046):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619052):
Or, maybe you can?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619103):
that given the definition using sets of opens you can recover the version with families indexed in an arbitrary type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619104):
```quote
Huh, why not?
```
Because it wouldn't be correct

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619114):
but it's not the usual definition of an atlas, since there you can have multiple charts on the same open but with different coordinates

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619120):
but in general you should try to minimize your domain of quantification to something which is somehow bounded by the original input data

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619130):
You can build exotic spheres by gluing two open balls

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619150):
if you don't, this is when mathematicians have to write "chapter 4" or whatever on ZFC embedding subtleties

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619161):
All the exotictness is in the gluing map

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619191):
in the manifold case, I'm sure you can bound it by all the ways that maps can possibly fit together

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619246):
isn't it kind of a moot point anyways, since we are also asking for these Huber pairs, which also contain types?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619271):
maybe the Huber pairs can't get that large either

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619279):
in the manifold case the atlas is a set of pairs (U_i, f_i) where U_i is an open set and f_i is a homeomorphism from U_i to some open set in R^n.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619284):
I totally agree that if you find yourself with something that looks like a perfectoid space, but the indexing family is large, then it's a nontrivial theorem to show that you actually have a genuine perfectoid space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619340):
anyway, let's focus on the perfectoid case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619374):
I'm sort of speculating here, but really if you need all that extra indexing power, then the definition is probably not correct anyway because then Type is probably not enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 05 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619397):
it's an arbitrary stopping point in the ZFC world

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619462):
Kevin disappeared. Maybe he suddenly realized Scholze's perfectoid business makes no sense at all because of this issue

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619586):
Ok, I don't know enough about manifolds. (They are weird, because they aren't defined as locally ringed spaces with some property.) But in the scheme case (and I think also in the perfectoid case) it should be fine to just work with a set of opens. Every point has an affine neighbourhood. That is what you need/want. Or am I messing up?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619667):
Nevertheless, if we use a set of opens, I don't know if that is a pretty thing to use as indexing set for the Huber pairs, and other data indexed on it. It might lead to ugly formalisation, it might lead to "un-mathematical" code. I really don't know.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619686):
You can define smooth manifolds as ringed space, see https://bookstore.ams.org/gsm-65

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619772):
I'm trying to do 10 things at once. I was hoping to get some work done tonight but my partner just got back from Canada and her sleeping patterns are in chaos; it might be bedtime.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619781):
I am not sure that anyone has ever used a perfectoid space for which the index set is any bigger than countably infinite

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619783):
hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619791):
maybe the size of the real numbers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619861):
I can't imagine anything bigger. Mario's "chapter 4" reference is pertinent -- this is the same paper as the one I've taken the definition of perfectoid space from.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127619894):
```quote
maybe the Huber pairs can't get that large either
```
I am not sure there is a single object in this story that has size > 2^aleph_0

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127620277):
Which "chapter 4" are we referring to?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127620286):
https://arxiv.org/abs/1709.07343

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127620309):
We should have a file/issue with references. Because now there is the diamonds paper, Fontaine's bourbaki notes, Wedhorn's notes...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127620323):
I have all these things as pdfs in my project directory but just didn't push them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127620370):
Maybe some list of links on the README?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127620423):
Yes, that should be fine.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 05 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127620435):
I can PR the readme tomorrow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127620917):
Maybe make a separate repository with the pdfs, if you want to commit them somewhere. Then people don't have to download them if they don't want to

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 05 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127621535):
I don't see the point of hosting the pdf on github if they were taken from arXiv

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Jun 05 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127622457):
It would also be great to have a "Getting it working" section in your README.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 05 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127622699):
```quote
I don't see the point of hosting the pdf on github if they were taken from arXiv
```
Agreed, I meant "better not to commit pdfs to the main repository, whether or not you host them elsewhere"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127623463):
```quote
It would also be great to have a "Getting it working" section in your README.
```
ha ha, I guess it currently doesn't work :-) (unless you allow sorrys). OK I'll write something about that in the README.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127624740):
```quote
It would also be great to have a "Getting it working" section in your README.
```
https://github.com/kbuzzard/lean-perfectoid-spaces/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127624758):
On my TODO list: (1) refactor definition of perfectoid space according to comments above, and move it into `src` (2) write a couple of issues explaining the details of what needs to be done to finish formalising the definition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127624806):
Any comments / criticism / suggestions / anything -- I'd be happy to hear it. Once I've written the issues I will perhaps begin to circulate a link to the project amongst my mathematician chums

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 05 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127624810):
And of course, many thanks to those who have already commented!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127626651):
*boggle* Every change I made bring new typeclass inference problems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127626706):
```lean
structure perfectoid_cover (p : ℕ) [is_prime p] (X : Type) [adic_space X] :=
(𝓤 : set (set X))
[𝓤_open : ∀ U ∈ 𝓤, is_open U]
(𝓤_cover : ∀ x : X, ∃ U ∈ 𝓤, x ∈ U)
(𝓤_affinoid_perfectoid : ∀ U ∈ 𝓤, 
  ∃ (A : Huber_pair) (Aperf : perfectoid_ring p A), is_preadic_space_equiv U (Spa (A)))   )

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 06 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127626709):
𝓤

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127626712):
and now I'm back with failing to synthesize `⊢ preadic_space ↥U`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127626723):
```quote
𝓤
```
Collection of open sets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127626728):
except that Lean does not notice they're open

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127626740):
```lean
instance preadic_space_restriction {X : Type} [preadic_space X] {U : set X} [@_root_.is_open X _ U] :
  preadic_space {x : X // x ∈ U} := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127627182):
I guess I really liked the idea of typeclass inference showing automatically that if X is some kind of nice top space (an adic space or perfectoid space) and U is an open subset then U inherits the niceness. I might just give up and spell it out.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127627396):
I've given up on typeclass inference because it's midnight.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127627414):
In the old version above, I had `is_preadic_space_equiv (U i) (Spa (A i))`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127627417):
and the preadic space structure on `U i` came from typeclass inference.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127627420):
I can't get it to work for U in some covering set

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127627423):
but this works:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127627463):
```lean
-- definitions of adic_space, preadic_space, Huber_pair etc
import adic_space 

--notation
postfix `ᵒ` : 66 := power_bounded_subring

/-- A perfectoid ring, following Fontaine Sem Bourb-/
class perfectoid_ring (p : ℕ) [is_prime p] (R : Type) extends Tate_ring R :=
(is_complete : complete R)
(is_uniform  : uniform R)
(ramified    : ∃ ϖ : Rᵒ, (is_pseudo_uniformizer ϖ) ∧ (ϖ ^ p ∣ p))
(Frob        : ∀ a : Rᵒ, ∃ b : Rᵒ, (p : Rᵒ) ∣ (b ^ p - a))

structure perfectoid_cover (p : ℕ) [is_prime p] (X : Type) [adic_space X] :=
(𝓤 : set (set X))
[𝓤_open : ∀ U ∈ 𝓤, is_open U]
(𝓤_cover : ∀ x : X, ∃ U ∈ 𝓤, x ∈ U)
(𝓤_affinoid_perfectoid : ∀ U ∈ 𝓤, ∃ (A : Huber_pair) (Aperf : perfectoid_ring p A),
  is_preadic_space_equiv (preadic_space_pullback U) (Spa A)  )      

class perfectoid_space (p : ℕ) [is_prime p] (X : Type) extends adic_space X :=
(exists_perfectoid_cover : perfectoid_cover p X)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127627484):
`preadic_space_pullback U` is just `U` again :-) (actually it's {x : X // x \in U})

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127627491):
but the instance can key on it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127627494):
I only half-know what those words mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127627499):
but type class inference works with this trick

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 06 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127632328):
I said `set (opens X)` for a reason

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 06 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127632374):
it's past time you had a `opens X` type of open subsets of X

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127635899):
I don't have Lean here, so there might be stupid typos. But how about something like this?
```lean
class perfectoid_space (p : ℕ) [is_prime p] (X : Type) extends adic_space X :=
(perfectoid_cover : ∀ x : X, ∃ (U : opens X) (A : Huber_pair) (Aperf : perfectoid_ring p A),
  (x ∈ U) ∧ is_preadic_space_equiv U (Spa A))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127635907):
That seems very readable to me. And I basically just squashed some lines together.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127641910):
```quote
it's past time you had a `opens X` type of open subsets of X
```
@**Mario Carneiro** do you imagine something like this?
```lean
class opens (X : Type*) [topological_space X] :=
(U : set X)
(U_open : is_open U)

instance open_is_subset {X : Type*} [topological_space X] :
has_coe (opens X) (set X) := ⟨λU, U.U⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 06 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127642757):
Yes. You will also want a `has_mem A (opens A)` instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 06 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127642759):
You could also use `subtype` for the definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127643208):
Voila, another attempt.
```lean
section opens

variables (X : Type*) [t : topological_space X]
include X t

@[class] def opens := subtype (topological_space.is_open t)

instance : has_coe (opens X) (set X) := ⟨subtype.val⟩

instance : has_mem X (opens X) := ⟨λx U, x ∈ U.val⟩

end opens
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 06 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127643260):
It shouldn't make too much difference, but you should use `is_open` instead of `topological_space.is_open`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127643434):
Done.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127643443):
But I'm having type class inference issues with Kevin's latest code (that he posted above).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127643446):
And it doesn't help if I change `set (set X)` to `set (opens X)`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127643487):
Somehow Lean starts looking for an instance of `has_coe_to_sort nat`, and I have no idea why Lean would do that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127643707):
Never mind... error was between keyboard and chair.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127643712):
```lean
-- definitions of adic_space, preadic_space, Huber_pair etc
import adic_space

--notation
postfix `ᵒ` : 66 := power_bounded_subring

/-- A perfectoid ring, following Fontaine Sem Bourb-/
class perfectoid_ring (p : ℕ) [is_prime p] (R : Type) extends Tate_ring R :=
(is_complete : complete R)
(is_uniform  : uniform R)
(ramified    : ∃ ϖ : Rᵒ, (is_pseudo_uniformizer ϖ) ∧ (ϖ^p ∣ p))
(Frob        : ∀ a : Rᵒ, ∃ b : Rᵒ, (p : Rᵒ) ∣ (b^p - a))

class perfectoid_space (p : ℕ) [is_prime p] (X : Type) extends adic_space X :=
(perfectoid_cover : ∀ x : X, ∃ (U : opens X) (A : Huber_pair) [perfectoid_ring p A],
  (x ∈ U) ∧ is_preadic_space_equiv U (Spa A))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127643724):
I think it would be really nice if we also made the `[p : Prime]` stuff work. I'll try to look into it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127644045):
Oh yes, I remember. That means that `ϖ^p` breaks. And we don't want up-arrows or `p.val` or the likes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 06 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127644065):
Well, you can use `[fixed_prime]` plus `fixed_prime.p` to avoid the coercion stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127644117):
Right, with your "hack" we get
```lean
-- definitions of adic_space, preadic_space, Huber_pair etc
import adic_space

--notation
postfix `ᵒ` : 66 := power_bounded_subring

open nat.Prime
variable [nat.Prime] -- fix a prime p

/-- A perfectoid ring, following Fontaine Sem Bourb-/
class perfectoid_ring (R : Type) extends Tate_ring R :=
(is_complete : complete R)
(is_uniform  : uniform R)
(ramified    : ∃ ϖ : Rᵒ, (is_pseudo_uniformizer ϖ) ∧ (ϖ^p ∣ p))
(Frob        : ∀ a : Rᵒ, ∃ b : Rᵒ, (p : Rᵒ) ∣ (b^p - a))

class perfectoid_space (X : Type) extends adic_space X :=
(perfectoid_cover : ∀ x : X, ∃ (U : opens X) (A : Huber_pair) [perfectoid_ring A],
  (x ∈ U) ∧ is_preadic_space_equiv U (Spa A))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127644121):
Look ma! No primes in our type signatures!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127644170):
```lean
#check @perfectoid_space -- perfectoid_space : Π [_inst_1 : nat.Prime], Type → Type
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127644441):
@**Kevin Buzzard** Is there a reason why `perfectoid_ring` has hypothesis `is_complete` and `is_uniform` and also `ramified`. Why not `is_ramified`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127644488):
It's just random -- like in Lean. It's `group` but `is_group_hom` right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 06 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127644494):
`is_group_hom` because that's a prop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 06 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127644499):
`group` is not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127644506):
Aah!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127644513):
So how about `is_perfectoid_space`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127644516):
because it's an adic space plus some prop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127644573):
I guess that makes sense. And similarly `is_perfectoid_ring`, and I guess `is_ramified`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127644624):
Hmmm, but `group` is also just a `monoid` with some props, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127644717):
But maybe its type is not Prop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127644725):
That's the distinction I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127644779):
Right, that makes sense. So then it is `is_ramified`, and the rest stays as it is.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127645043):
@**Kevin Buzzard** Does it also make sense to call the last condition `is_perfect` instead of `Frob`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127645837):
If you search for "perfect ring" then you get ads for weddings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127645886):
I thought Frobenius was bijective for a perfect ring, not surjective. What do you think?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127645889):
Hmm, you are probably right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127645905):
Bam! https://github.com/kbuzzard/lean-perfectoid-spaces/pull/1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127645945):
@**Kevin Buzzard** Your first PR (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127645950):
I've pushed Kenny's valuation stuff by the way (first chapter of Wedhorn)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127645981):
And there is also https://github.com/jcommelin/lean-perfectoid-spaces/tree/opens

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127645983):
```quote
@**Kevin Buzzard** Your first PR (-;
```
One day when we have a gigantic maths brain that's taking over the universe, you'll be able to tell your children that you made the first PR.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127646027):
if we decided to spare them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127646031):
Which defines the `opens` class. And uses it in the `perfectoid_space` definition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127646089):
Kevin, should I also PR the `opens` stuff? Or do you not like that direction?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127646096):
```quote
I said `set (opens X)` for a reason
```
I couldn't find `opens` in the topological space stuff so I left it and decided I should ask where it was later

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127646099):
```quote
it's past time you had a `opens X` type of open subsets of X
```
Ohh!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127646265):
I see that @**Kenny Lau** made `ker f` a subset instead of a subtype. I really don't know when I should use which. Can someone clarify this for me?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 06 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127646316):
you can coerce a subset to a subtype anytime

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127646318):
I can't. I'm constantly switching between them. I guess subsets are easier to work with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127646323):
[I can't clarify, I can coerce]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127646327):
Random screed by Hazewinkel claims perfect is bijective \lam x, x^p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127646342):
Ok, so `Frob` it is. I already reverted it on my branch.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 06 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127649540):
I don't understand https://github.com/kbuzzard/lean-perfectoid-spaces/blob/b1e6489145be504e64a009226c6811bfd84a5070/src/perfectoid_space.lean#L22 Why isn't there a `∃` here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 06 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127649589):
Do we have a roadmap saying which parts of Wedhorn are needed?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127650170):
It is equivalent up to a choice, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127650175):
And I think the roadmap is under construction.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127651738):
Ooh, there is a tiny typo in `subrel.lean`. We need `\alpha` to be of type `Type*`. Without the `*` Kenny's code gets an error.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127652798):
```quote
Do we have a roadmap saying which parts of Wedhorn are needed?
```
It's on the way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127652800):
I keep trying to do everything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127652804):
maybe I should post some basic info and then work on it more

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127666129):
Yes, some issues with basics would be totally fine.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 06 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127669147):
I ran into [Guy Henniart](https://en.wikipedia.org/wiki/Guy_Henniart) on the train this morning. I told him about schemes and perfectoid spaces in Lean, he was very interested. He told me proof assistants will probably be part of the future of mathematics and we should try to use this opportunity to tighten our links with the CS department, maybe hiring someone working on this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 06 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127669203):
@**Kevin Buzzard**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 06 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127669223):
he proved local langland for GL(n) :o

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 06 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127669251):
Yes it's that level: stuff Scholze reproved when he was a 1st year undergrad

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 06 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127669259):
very impressive from Guy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 06 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127669267):
> "Une preuve simple des conjectures de Langlands pour GL(n) sur un corps p-adique"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 06 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127669269):
"une preuve simple"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 06 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127669317):
and one of my body parts is made of chicken

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 06 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127669338):
maybe the proof has no nontrivial subproofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127669449):
Patrick, that's cool news! I really like it that people are enthusiastic about these formalisations. So far most people I encounter only shrug their shoulders...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 06 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127669474):
It was also funny seeing him reacting when I said there would be riots if Scholze doesn't get his medal in Rio. He completely failed to picture how this could happen (Scholze not getting the medal).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 06 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127669505):
Johan: yes, this is why I tell this story here. It was a pretty unusual reaction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 06 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127669560):
Especially since Guy is from a generation that can barely use a computer to write an email

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 06 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127669574):
Next week I should try to ask Serre what he thinks about proof assistants

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127669580):
Trollolol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 06 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127669878):
An algebraist in my department went to the Loeser conference last week and said that Hales had mentioned the schemes work in his talk. But I guess Hales is biased :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127670020):
Ok, but this is only an encouragement that we really should get perfectoid spaces in Lean before Rio!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 06 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127670044):
It looks like it's almost done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127670049):
If Scholze showed some interest, and now Henniart...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 06 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127670057):
who is Rio?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 06 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127670524):
```quote
It looks like it's almost done
```
I guess you have to place quite a bit of emphasis on *looks*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735398):
https://github.com/kbuzzard/lean-perfectoid-spaces/issues/3

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735457):
I had a good look through the maths last night and I don't see any major difficulties, but who knows.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 07 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735490):
"Page numbers are all for Huber's notes." I guess you meant Wedhorn?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735493):
ooh thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735498):
I do that a lot!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 07 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735549):
Lean 7 will tell you about such typos on Github

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 07 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735742):
I'm not sure I understand the dependency graph

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735754):
I'm not surprised

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735755):
Should I explain it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735758):
In the issue, I mean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 07 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735763):
It would help if you want help on this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 07 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735815):
Because currently it's not clear how the work could be divided

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 07 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735841):
Is Spv(A) a typo or something different from Spa(A)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 07 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735842):
Maybe v is valuation?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735843):
something different

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735844):
I didn't make the notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 07 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735848):
it appears only once in the issue

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735889):
It's an auxilary definition :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735896):
I'll add some comments

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 07 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127735998):
Roughly, how many pages of Wedhorn are actually required for this definition of adic spaces?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736514):
In retrospect I don't think that many.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736560):
The hard work might be proving that an affinoid adic space is an adic space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736562):
however

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736570):
that might be easier than proving that an affine scheme is a scheme

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736573):
because O_X is a sheaf on Spec(R)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736577):
and the analogous fact for Spa(R) is not true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736581):
so an affinoid adic space is Spa(R) for an R for which it is true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736587):
Aah, I've got it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736591):
The hard thing will be proving that an affinoid perfectoid space is a perfectoid space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736594):
That will need far more stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736737):
but we don't need to advertise that, right? ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 07 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736757):
Is there any easier example of a perfectoid space?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736817):
The empty space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736826):
there is literally no simple example of a perfectoid space other than this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 07 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736835):
That's what I feared

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736836):
because the second simplest example is Spa(K,K^o) with K a perfectoid field

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 07 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736840):
So we can't really escape that example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736847):
well, at least it's a field

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736863):
Something like C_p, the completion of an algebraic closure of the p-adic numbers, is a relatively straightforward example of a perfectoid field

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736872):
don't worry, it's algebraically closed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736875):
you don't have to go on forever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 07 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736878):
And if we want to prove any result about this definition, beyond having an example, is it super hard to prove that tilting thing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736879):
We number theorists tell people that C_p is our version of the complex numbers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 07 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736921):
Corollary 3.20 in the diamonds paper

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736923):
Oh yeah the tilting thing needs a whole bunch of commutative algebra

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736931):
almost etale extensions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736932):
probably cotangent complex

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736936):
although actually maybe you could instead use my work with Verberkmoes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736947):
a bunch of almost mathematics though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736956):
derived categories

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736962):
yeah it would be a good challenge

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127736976):
If you did that then serious people would get interested

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127737029):
because that is like an odd order theorem but one that people are interested in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 07 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127737067):
The proof is only two lines long in that diamonds paper: "The tilting process glues to give a functor X \maptos X^b . Theorem 3.13 globalizes to the following result." and the proof of Theorem 3.13 is "In [Sch12], these are only proved over a perfectoid field, but the proof works in general."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 07 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127737115):
doesn't looks too bad

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127737413):
Yes the work is tilting an affinoid perfectoid and...I guess writing down the definition of the tilt might not be so hard, come to think of it. It's proving that the space and its tilt have the same geometry that's hard

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127737432):
A huge generalisation of Fontaine-Wintenberger and Faltings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 07 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127737728):
OK so I just looked at the paper (I'm travelling currently). The hard part is the equivalence, that is a lot of content. Maybe the definition of tilting might be possible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 07 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127737756):
Is there  anything simpler but still significant that could be proved about those spaces?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127741865):
I guess one could prove that if A is perfectoid then Spa (A) is a perfectoid space. Scholze's original proof used tilting and a whole bunch of machinery. Verberkmoes and I found a much shorter direct proof. But doing basic stuff like defining perfectoids is the sort of thing we can do "in our spare time" -- formalising my paper would be a serious endeavour, although of course it's something I've considered. Most things in the area are impossibly hard or just very long. There are hundreds of pages by gabber and Romero that would be a joy to do but would take forever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127751773):
I do think that it would be dissapointing if we have no examples at all... Defining tilting will be very nice PR I think. But it would be more 'honest' to first prove that Spa(A) is perfectoid (given that you have a proof without tilting).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127758361):
I think that most mathematicians will not really understand what is going on, and wouldn't know the difference between defining a perfectoid space and defining tilting. But I'd happily be proved wrong. There are two independent questions. The one I was interested in (and still am) is: "given that most of the non-trivial work doing maths on computers is of a Kepler conjecture / odd order theorem nature, i.e. hundreds of lemmas about relative simply things, are these programs even _capable_ of doing mathematics with non-trivial objects?"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127758370):
I now think they are. But there's a different question, which is much more complicated:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127758374):
how to get one non-trivial theorem about one non-trivial object into these systems?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127758376):
And that will cost time and money

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127758416):
it's not just a "hobby project" like defining a perfectoid space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127758424):
I have 4.5 hours of meetings with the UK science funding council EPSRC today (it's one big reason that I couldn't go to Hanoi)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127758429):
and this will come up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127758430):
Ok, good luck!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127758432):
Sounds like today is an important day

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127758433):
but if they're not interested then I don't quite know what happens next

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127758435):
I guess I am more interested in hearing their thoughts about setting up something big

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127758437):
and whether they'd encourage me to apply for funding

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127758735):
So, when does the meeting start? (Or rather, when will you be back to tell us about the good news :wink:?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127759770):
I don't think any decisions will be made today!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127759772):
But there will be a chance to test the water.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127760289):
www.math.columbia.edu/~harris/otherarticles_files/perfectoid.pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127760292):
I hadn't been aware of this article until the other day

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127760379):
The introduction is really nice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127761231):
[sorry, double post fail]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127765205):
Kevin, do we even need the notion of Tate ring?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127769845):
Maybe not but it's pretty easy to formalise if you have everything else. A perfectoid ring is a Tate ring plus ...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127771741):
If type class inference tries to turn an ideal into a module it starts looping to find a ring. Same issue that Patrick has I guess.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 08 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127771945):
modules are very dangerous for type class resolution. I'm still waiting for Mario, Johannes and Sebastian to really solve this issue

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127772171):
Hmmz... we need finitely generated ideals. It would be very useful to have `span` from linear algebra. But then we need to treat an ideal as a module.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127772199):
If there are actual technical problem with modules being a typeclass then surely one solution is just to stop them being a typeclass?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127772245):
And have all the code be utterly unreadable to mathematicians...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127772268):
By the way, Kevin, are the meetings over yet? Were they receptive to your ideas/plans?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127772447):
@**Kevin Buzzard** Is it ok to add https://github.com/johoelzl/mason-stother as dependency. Then we have univariate polynomials. And this is scheduled to go into mathlib anyway, so the dependecy would be temporary.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127774148):
https://github.com/jcommelin/lean-perfectoid-spaces/tree/Huber_pair is a clumsy attempt to define Huber rings (up to the topological stuff).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127774162):
But there is still a sorry to turn an ideal into a module.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127788416):
Money: I was encouraged to apply for it. Mason-Stothers -- is there a risk that we make this a dependency and then M-S gets PRed to mathlib and then stuff gets changed and then our code doesn't work? Or doesn't this matter?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127788447):
Not so much... we really use very little of it. That part of the interface shouldn't change.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127788507):
I can PR my subring branch into your repo if you want... it adds Mason-Stothers as dep.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127788511):
So then another question is: if we only use very little of it, is it best to just cut and paste a small part of it into our repo directly and then delete it later?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127788514):
I just have no idea how to run a project like this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127788527):
No, I would just go with the dependency.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127788536):
And move on to interesting stuff (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127788540):
Ok then I'll add the dependency. Can it wait a day? Can you do it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127788542):
I did it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127788545):
I have relatives here so I should go

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127788546):
Shall I PR?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127788547):
thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127788550):
yes please PR

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127788551):
Aaah, ok, see you later.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 08 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127788598):
I will look over it later. Assia suggested that I understand all the code I accept so I'd like to read through it before I accept it but I'm sure I will

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127788625):
Well, I'm a newbie... so maybe you want to improve little things...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 08 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127788974):
Don't you think we should write a LaTeX file describing what has been formalized so far, and update it each time something is added? If we do this in real time it shouldn't be too painful. And I think it would be really useful. It could even include some comments about the formalization choices.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 08 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127789019):
`class normal_add_subgroup [add_group α] (s : set α) extends is_add_subgroup s : Prop := (normal : ∀ n ∈ s, ∀ g : α, g + n - g ∈ s)` WTF?!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127789070):
You can have tick boxes in Github issues, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 08 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127789076):
Do perfectoid spaces include non commutative groups with additive notations?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127789077):
That might be useful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127789090):
I didn't write that file. I just copy-pasted it, and then find-replaced stuff to get additive versions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 08 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127789104):
But this bit is evil

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127789114):
I agree. I am just saying that I didn't actually read that part of the file.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127789123):
I am still annoyed that I even had to do all that duplication.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127789455):
Patrick, I think it might also be a good idea to have accompanying comments (like Kevin did in parts of the files).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127789470):
That will help interested mathematicians to figure out what is going on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 08 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127789481):
Sure. Every documentation is good

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127789546):
Concerning the LaTeX-file, I think that's fine. But then maybe we shouldn't have issues as well. Otherwise we will have Zulip, issues, comments in the code, TeX-file,...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127789552):
And then we get lost.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 08 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127789561):
Issues are about things to do. LaTeX file would be about things that are done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 08 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127789639):
Yes, and PR's form the boundary, and Zulip is the glue that keeps everything together.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 09 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127816932):
Family request me, but see https://github.com/PatrickMassot/lean-perfectoid-spaces/commit/334581954ca07e38d16526a264ac85807ee221df to see what I'm working on (comments are already welcome)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 09 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127816937):
@**Kevin Buzzard**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 09 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127816987):
when I'll be done proving that uniform_space instance I will quickly be stuck waiting for Johan's PR merge

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127817563):
Cool!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127817564):
In my `Huber_pair` branch I have a stupid definition of `I`-adic topology

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127817566):
But it doesn't give a uniform_space. So it is pretty useless.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127817720):
This:
```lean
+-- Somehow we need R° both as a subset of R and a subtype. 
+-- There is a coercion from the set to the subtype but relying naively on it seems to bring 
+-- type class resolution issues
+definition power_bounded_subring := {r : R // is_power_bounded r}
+definition power_bounded_subring_set := {r : R | is_power_bounded r}
```
That is exactly the kind of trouble that I have also been having with subrings. I have them both as subset and subtype.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127818859):
Have you tried sticking rigidly to the set notation, and always using coercions and never the subtype. If there's an instance about `↥{r : R | is_power_bounded r}`, it won't apply it to `{r : R // is_power_bounded r}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819376):
What is the advantage of working with subsets instead of subtypes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819469):
Aah, @**Chris Hughes** , here's a problem: we have `topological_space.induced` which happily gives you a topology on a subtype. But not—I think—on a subset. So if you want a topological subring, you need the subring as a subtype.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819478):
The point is don't mix `↥{r : R | is_power_bounded r}` and `{r : R // is_power_bounded r}` if you want type class inference to work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819518):
And if some of your code requires sets, you have to stick to the former.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819525):
And if some of it requires subtypes? Then you stick with the latter...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819526):
But what is an example of "code [that] requirese sets"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819528):
If it requires subtypes, then you use the coercion from a set and not `//`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819568):
I am new to all this type theory stuff, and so far I have been thinking of types as "sets for computer scientists", and I just treat them as sets. And then all of a sudden there are subsets and subtypes, and I don't see why we smuggle subsets in through the backdoor.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819569):
Unless you only ever need subtypes. In which case don't use sets.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819574):
```quote
If it requires subtypes, then you use the coercion from a set and not `//`
```
seems to conflict with
```quote
The point is don't mix ↥{r : R | is_power_bounded r} and {r : R // is_power_bounded r} if you want type class inference to work.
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819575):
No it doesn't. Only use the first one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819620):
I tried, and then it couldn't infer a topological space on it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819622):
Because coercion and type inference don't work together.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Jun 09 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819628):
types are not sets; the difference is that values are assigned exactly one type (typing judgments are rigid; although, of course, you can prove that two types are equal and use `eq.mp(r)` ...), whereas set membership in set theory says nothing about the type of object in the set, which is totally ridiculous imho

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819629):
Use the coercion for your topological space instance as well?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819630):
I still haven't seen (here or in other threads where the topic came up) any reason to use subsets. I am just confused, and I would like to know why they are cool.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819634):
i.e. prove `↥{r : R | is_power_bounded r}` is a topological space not `{r : R // is_power_bounded r}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819673):
```quote
types are not sets; the difference is that values are assigned exactly one type (typing judgments are rigid; although, of course, you can prove that two types are equal and use `eq.mp(r)` ...), whereas set membership in set theory says nothing about the type of object in the set, which is totally ridiculous imho
```
@**Nicholas Scheel** Ok, great, so why do we smuggle set membership back in, if it is so ridiculous?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Jun 09 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819674):
the model for a type-theoretic “set” is `set a := a -> Prop` which is precisely a “set” of elements (of a particular type) satisfying that predicate (conceptually)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819676):
Or always stick to subtypes. Subsets are good because they can intersect each other and be subsets of each other.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819677):
Ok, and subtypes find that hard?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819684):
We can define an intersection of subtypes right? Just take `\and` of their properties.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Jun 09 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819685):
but `set` just a predicate, it doesn’t contain any elements of the type ... which is what a subtype is for: it contains an element and the proof that it is in the corresponding set, essentially

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819687):
Because everything only has one type, there's no such thing really as the intersection of two subtypes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (Jun 09 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819728):
the subtypes would need to have the same supertype, otherwise it doesn’t make sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819736):
Right, I see.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819776):
But if I have two subtypes of X, say `S` and `T`, then I can do `subtype (\lam x, S.property x \and T.property x)`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819784):
But I understand that this is a clumsy way of doing intersections, and for subsets it is just a lot easier.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819824):
So we need subsets and subtypes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819827):
And that would be hard to use if you had a proof that `∀ x : s, p x` and you had `x : subtype (\lam x, S.property x \and T.property x)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819834):
So, at some point in my code I prove that if the subset `S` is a subring, then we have an instance of `ring S`. And I think here `S` is silently coerced to a subtype, for otherwise `ring S` doesn't typecheck.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819836):
yes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819837):
But then some other code couldn't infer an instance of `ring (subtype S)`, and I got confused.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819879):
So I also proved explicitly that I had an instance of `ring (subtype S)` by copy-pasting the other proof verbatim.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819880):
Because it has to be the same expression for type class inference to work. definitional equality isn't good enough I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819881):
And then it worked. But now I don't see the point of the silent coercion.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819889):
Which is why it's best to stick to coercions the whole time.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819891):
I tried, but it didn't work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819893):
Maybe I didn't try hard enough (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819894):
What didn't work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819935):
Sticking to coercions. (Or do you mean explicit coercions, instead of silent ones?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819941):
There both the same. What in particular didn't work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819982):
Let me try to find it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819991):
I think it was these lines: https://github.com/jcommelin/lean-perfectoid-spaces/blob/Huber_pair/src/adic_space.lean#L36-L38

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127819992):
But I don't have Lean here, so I can't test it. Sorry.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127820047):
I couldn't find `for_mathlib.subring`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127820050):
Aah, that is in the `subring` branch

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127820089):
Found it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127820090):
I thought `Huber_pair` was a branch of `subring`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 09 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127820091):
need to be in branch `subring`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127820144):
Did the `is_ideal I` not work. Or something else?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127820152):
No, I think it was with subrings and topological spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127820155):
Ok, maybe it was both.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127820164):
Because the `is_ideal I` needed to infer a ring structure `ring (subtype S)`, and that `(subtype S)` was explicit because of the topological stuff in those lines.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127820257):
I think this might be the issue `instance subtype.comm_ring [comm_ring R] {S : set R} [is_subring S] : comm_ring (subtype S)`
should be `instance subtype.comm_ring [comm_ring R] {S : set R} [is_subring S] : comm_ring S`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127820314):
Worst case scenario if you can't get the coercion to work is to literally do `@has_coe_to_sort.coe whatever` instead of `subtype S`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127820321):
Ok, thanks! I'll try it out when I get back to lean!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 09 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127822057):
I need help with the following annoying lemma:
```lean
example (R : Type*) [comm_ring R] (V : set R) : 
  prod.swap '' {p : R × R | ∃ (x : R), x ∈ V ∧ -x = p.snd + -p.fst} = {p : R × R | p.snd + -p.fst ∈ V} :=
sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 09 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127822064):
part of the problem is I'm not able to use `neg_eq_iff_neg_eq`, even inside `conv`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 09 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127822155):
I'm also stuck on
```lean
variables (R : Type) [comm_ring R] [topological_space R] [comm_ring R] [topological_ring R]  
def nhd_zero := (nhds (0 : R)).sets

lemma nhd_zero_symmetric {V : set R} : V ∈ nhd_zero R →  (λ a, -a) '' V ∈ nhd_zero R :=
begin
  intro H,
  dsimp [nhd_zero],
  have := continuous.tendsto (topological_add_group.continuous_neg R) 0,
  unfold filter.tendsto at this,
  simp at this,
  have almost:= this H, 
  sorry
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 09 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127822157):
But this is one is nastier since it involves filters

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 09 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127822393):
How about this
```lean
example (R : Type*) [comm_ring R] (V : set R) :
  prod.swap '' {p : R × R | ∃ (x : R), x ∈ V ∧ -x = p.snd + -p.fst} = {p : R × R | p.snd + -p.fst ∈ V} :=
begin
  rw set.image_swap_eq_preimage_swap, ext p, cases p with r1 r2,
  change (∃ x, x ∈ V ∧ -x = r1 - r2) ↔ (r2 - r1 ∈ V),
  have : ∀ x, -x = r1 - r2 ↔ x = r2 - r1,
    by intro x; rw [neg_eq_iff_neg_eq, eq_comm]; simp,
  simp only [this], simp
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 09 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127822493):
For the second one, what you proved is `(λ a, -a) ⁻¹' V ∈ nhd_zero R`, so then show that `(λ a, -a) ⁻¹' V = (λ a, -a) '' V` somehow.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 09 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127824162):
Thank you very much @**Reid Barton**. `change` was the key for the first one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 09 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127824168):
For the second one I guess I only needed some encouragement ;-)
```lean
lemma nhd_zero_symmetric {V : set A} : V ∈ nhd_zero A →  (λ a, -a) '' V ∈ nhd_zero A :=
begin
  intro H,
  have := continuous.tendsto (topological_add_group.continuous_neg A) 0,
  rw (show (λ (a : A), -a) 0 = 0, by simp) at this,
  have almost:= this H,
  have aux : { r : A | -r ∈ V } = (λ a, -a) '' V, by simp[set.image, neg_eq_iff_neg_eq],
  simpa [filter.mem_map, aux] using almost
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127825898):
```quote
But then some other code couldn't infer an instance of `ring (subtype S)`, and I got confused.
```
Johan -- I think the point is that given a subset there are two ways to get a subtype, the explicit and the implicit way, because someone set up a coercion. Because the coercion is set up, you're never supposed to use the explicit constructor, you are completely handing the job over to the type class inference system. So when you use commands like `subtype S` explictly, instead of that funky up-arrow, this confuses the type class inference system.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127825945):
[nonsense deleted]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127825961):
A "subtype" really does not mean a subset of a type, a subtype is a completely new and different inductive type; if you want to get back to the original type you can use coercion but this is still applying a function, sending a term of the subtype to its value.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127826005):
subtypes are better than subsets because subtypes are types. It's easy to interact with them with the `.1` and `.2` notation and the `\<_,_\>` notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127826074):
Right, but I can imagine that at some point people want to take the intersection of two subrings, are maybe generate a subring, etc... And it seems that sutsets are useful in those cases.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 09 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127826907):
Sometimes things come as subsets, for instance power bounded elements

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127826908):
I'm doing group_theory at the moment, and it is a little bit awkward proving things about a subgroup that's normal within another subgroup for example, or worse, quotienting by a subgroup within another subgroup. I've been copying the proofs os Sylow's theorem's over from coq, using this paper https://arxiv.org/pdf/cs/0611057.pdf, and most of the group theory in coq seems to be proved on subgroups rather than groups, i.e. they often talk about a subgroup H of a group G, without mentioning anything in G which is not in H.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 09 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127826950):
This is the story Assia is always telling us

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127826960):
/me feels his inner mathematician shudder and cringe.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127827013):
Somehow this *shouldn't* be necessary.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 09 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127827144):
I agree

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127827196):
I'm not sure how much it would help, particularly with the quotienting issue. If you didn't quotient within the subtype, you wouldn't end up with a group, You'd have some type which had a subtype which is a group. It might help avoid notation like `subtype.val '' S`, which I seem to have to do rather a lot.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127827625):
@**Kenny Lau** Should `is_valuation` be a typeclass? It currently is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 09 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127827630):
I don't know

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127827728):
Me neither

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127827731):
I'm writing brief LaTeX notes as Patrick suggested

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828207):
@**Johan Commelin** I don't understand github well enough to review your PR. I tried to add a comment and got the error `Start commit oid is not part of the pull request`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828252):
Hmm, I don't know how that happened...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828293):
I can't make sense of it... all commits in its "local context" are either already in your master branch, or in my PR...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828295):
I can't seem to make comments on your PR.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828296):
Or at least I can't say the following:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828302):
So I was envisaging that stuff in `for_mathlib` was stuff which it was our responsibility to try and get into mathlib. But this code looks like it was written by other people -- is it even Ok to put it in our project? And then is our job to try and PR this to mathlib or will the authors take care of that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828307):
It's attached to the line `Authors: Johannes Hölzl, Mitchell Rowett, Scott Morrison`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828308):
Right... that's a good point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828309):
(I hate all those license things)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828356):
Anyway, all I did was take their code and translate from multiplicative notation to additive...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828358):
I don't know what is appropriate in this case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828453):
@**Mario Carneiro** What do you think of this subring code?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828455):
```lean

+/-- `S` is a subring: a set containing 1 and closed under multiplication, addition and and additive inverse. -/
+class is_subring  (S : set R) extends is_add_subgroup S, is_submonoid S : Prop.
+
+instance subset.ring {S : set R} [is_subring S] : ring S :=
+{ add_comm      := assume ⟨a,_⟩ ⟨b,_⟩, subtype.eq $ add_comm _ _,
+  left_distrib  := assume ⟨a,_⟩ ⟨b,_⟩ ⟨c,_⟩, subtype.eq $ left_distrib _ _ _,
+  right_distrib := assume ⟨a,_⟩ ⟨b,_⟩ ⟨c,_⟩, subtype.eq $ right_distrib _ _ _,
+  .. subtype.add_group,
+  .. subtype.monoid }
+
+instance subtype.ring {S : set R} [is_subring S] : ring (subtype S) :=
+{ add_comm      := assume ⟨a,_⟩ ⟨b,_⟩, subtype.eq $ add_comm _ _,
+  left_distrib  := assume ⟨a,_⟩ ⟨b,_⟩ ⟨c,_⟩, subtype.eq $ left_distrib _ _ _,
+  right_distrib := assume ⟨a,_⟩ ⟨b,_⟩ ⟨c,_⟩, subtype.eq $ right_distrib _ _ _,
+  .. subtype.add_group,
+  .. subtype.monoid }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828466):
We will be playing with several subrings of a given Huber ring so we will surely need some way to formalise the idea of `is_subring`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828507):
Why use both `ring S` and `ring (subtype S)` ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828508):
But should we just avoid subsets completely? Or is it hard to say without context?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828514):
Chris I am just cutting and pasting what Johan wrote. I don't know what is best. My understanding is that you're saying `ring (subtype S)` is unnecessary

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828515):
I think so.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828516):
and we should use typeclass inference at all times

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828519):
but what I am unclear about is if we should be using sets at all

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828565):
Whenever possible it's better to. I think you have to use sets. `is_subring` has to be defined on a predicate anyway. How would you define it on a subtype?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828570):
I see your point!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828624):
The reason that both versions are there is simply that stuff doesn't typecheck without the `(subtype S)` version. Which is probably due to "mistakes" I made in other parts of the code.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828629):
I would love to get rid of it, because it looks "unmathematical"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 09 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828630):
and `x \in S` is more natural than `S x` so it may as well be a set. Going between sets and subtypes isn't the hard part, it's when you have to deal with subtypes of subtypes, and then the same set but as a subtype.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828726):
So what exactly breaks when you remove the subtype version?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828772):
I think some code in my `Huber_pair` branch. The topology on `S` is the induced topology, via `subtype.val`. And this turns `S` into `subtype S`. But then you also want a ring structure on it...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828974):
Kevin, I will get back to the PR on monday morning I guess...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828975):
Yeah, let's figure out how it all works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828977):
this PR business

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127828978):
there's no hurry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127829131):
Ok, let's do that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 09 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127829173):
(Oh and by the way, you can `git rm *.aux` etc in the LaTeX folder, to get rid of those files that you don't actually want to track.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 09 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127831710):
And put them in `.gitignore` file: at root of project, a file containing lines like `*.aux`, `*.dvi` (dvi?!)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 10 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127834784):
I'm the king of filters! https://github.com/kbuzzard/lean-perfectoid-spaces/pull/5

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 10 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127850654):
> What do you think of this subring code?

It's fine, except that the two instances are defeq so you need not prove it twice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 10 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127852926):
```quote
(Oh and by the way, you can `git rm *.aux` etc in the LaTeX folder, to get rid of those files that you don't actually want to track.)
```
Sure, but every time the file is updated they come back, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 10 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127853064):
```quote
> What do you think of this subring code?

It's fine, except that the two instances are defeq so you need not prove it twice
```
Johan -- defeq is not the same as equal (for example rw won't make some random change from a thing to a defeq thing before rewriting), so Mario is not saying "your code is bound to still work if you remove the second instance", but my impression is that we should kill that last instance and then try and understand how to correctly work around the problems that this causes. The type class inference system is not something you can just add to -- my understanding is that careful thought needs to go into it. The moment there is more than one route from A to B, or a non-trivial way of getting from A to A, there's a risk that there will be problems down the line (time-outs, obscure errors).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 10 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127853257):
That's not quite what I'm saying. You should have both instances, but you can prove one by just referencing the other

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 10 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127853394):
This whole type class inference thing is still a mystery to me in places.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 10 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127855360):
```quote
```quote
(Oh and by the way, you can `git rm *.aux` etc in the LaTeX folder, to get rid of those files that you don't actually want to track.)
```
Sure, but every time the file is updated they come back, right?
```
`git` will never track a file without being explicitly instructed to do so. You could issue this instruction by mistake, using a careless `git add *`. This is where `.gitignore` comes in. In a file matches a pattern listed in `.gitignore` you need a `git add -f file_name` to add it. This way you can safely add `*.pdf` in `.gitignore` but still put, say Wedhorn's lecture notes, in the repository if you want to. Adding compiled versions of the TeX files present in the repository is pointless.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 11 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127886064):
@**Patrick Massot** Does
```lean
instance toplogical_ring.to_uniform_space : uniform_space R
```
use the ring structure?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 11 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127886304):
Cool PR by the way! I added some comments.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 11 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127886319):
No, it should be about topological groups. I PR'ed this quickly to make sure no work is duplicated (we should maybe declare somewhere on what part we intend to work), but really it should go to the `for_mathlib` directory, and be stated for topological groups (maybe even non abelian). @**Johannes Hölzl** did you intend to build this instance (canonical uniform structure on commutative topological groups) at some point?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 11 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127886536):
Yes, it would be nice to know who is working on what.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 11 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127886537):
But I think we have done most low-hanging fruit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 11 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127886651):
Sure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 11 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127904303):
Isn't it all low-hanging fruit? ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 11 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127904307):
I guess someone needs to think about completions at some point. Perhaps we need some more issues, perhaps of a smaller nature.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 11 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127908740):
```quote
Isn't it all low-hanging fruit? ;-)
```
Well, I think that `Spa` will be non-trivial (Leanwise).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 11 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127909048):
@**Mario Carneiro** Will stuff like the following line mess up the type class system?
```lean
instance toplogical_ring.to_uniform_space : uniform_space R := stuff_goes_here
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 11 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127909061):
I don't see any obvious reason for this to cause a problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 11 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127909091):
Ok, I thought you would get a non-trivial route `topological_ring → uniform_space → topological_space`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 11 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127909150):
oh, well that's true, I suppose you need to make sure that this is defeq to the other path to topological space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 11 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127909168):
A uniform space extends a topological space, so you just need to let the topological component be the one inherited from `topological_ring`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 11 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127909171):
that means that you can't use the default proof of `is_open_uniformity`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 11 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127909634):
This might create some trouble...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 11 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127909696):
@**Mario Carneiro** Does this suggest that in fact `topological_ring` should extend `ring` and `uniform_space`. And have constructor from ring + top_space ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 11 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127909701):
(In fact, this is more about topological groups... the ring structure is not relevant.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 11 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127914420):
@**Mario Carneiro** we are talking about https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/top_rings/src/adic_space.lean#L60 It uses [uniform_space.of_core](https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean#L117) I'm not sure about things that should be defeq are defeq

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 11 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127914468):
I'll try to ask Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 11 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127915787):
It doesn't want to answer, which is probably not good. I tries
```lean
example : (@toplogical_ring.to_uniform_space R _ _ _ _).to_topological_space  = (by apply_instance : topological_space R) := rfl
```
but Lean says `tactic failed, type mismatch` on the opening parenthesis on RHS. Checking the type of LHS and RHS looks good, even with pp.all

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 12 2018 at 03:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127930196):
Ah yes, you shouldn't use `uniform_space.of_core`, that generates the uniformity topology but you want to pick up the default topology on a topological ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jun 12 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127931824):
```quote
No, it should be about topological groups. I PR'ed this quickly to make sure no work is duplicated (we should maybe declare somewhere on what part we intend to work), but really it should go to the `for_mathlib` directory, and be stated for topological groups (maybe even non abelian). @**Johannes Hölzl** did you intend to build this instance (canonical uniform structure on commutative topological groups) at some point?
```
Yes, I would like to see uniform spaces derived from topological groups.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127939941):
Right, but picking up the existing topology is going to be pretty hard, I guess.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940012):
Noob question: if we have a situation like this in the type class system, or more generally... to paths $$f$ and $$g$$ to go from $$A$$ to $$B$$, and they are not defeq, but there is a proof that they are equal. Would parametricity help out? Or is it an idle hope to envision some synergy between this lambda-Prolog unification and parametricity?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940054):
(I still don't know if parametricity is the promising silver bullet that I want it to be. If it is, then I think I ought to spend most of my time in bringing it to Lean... but I fear that it doesn't actually help that much in doing maths.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 12 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940207):
well, that would require a lot more brains on the part of the type class inference system

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940273):
/me loves type class inference systems with brains :graduation_cap:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 12 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940278):
while I personally haven't encountered it, Leo is already worried about the performance of the type class inference system

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 12 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940284):
so I don't think it's a practical thing to hope for in the future

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 12 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940288):
the more you ask a tactic to do, the slower it runs...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 12 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940345):
i wonder if anyone here is interested in old-style chess engines

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940353):
Hmmm too bad. And Kudos to human brains...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 12 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940354):
type class inference works like that, it searches all the possible ways to get from A to B

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 12 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940355):
the number of possible paths grows exponentially

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 12 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940356):
with each step

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940357):
Yes, how would the old-style Chess engines help? (I never studied them.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 12 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940399):
they don't help, it's a comment on how hard the problem is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 12 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940420):
type class inference is something that must be done in a sane amount of time, or users of Lean will get really frustrated when their proof takes ages to type-check

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940462):
Would new-style chess engines help? I wonder if we are willing to give up "determinism" to win a lot of speed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 12 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940472):
no, because if lean manages to synthesize a proof at 2 pm and then doesn't at 4pm, you've got a problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 12 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940522):
I mean, maybe you can find some way to cache the proof, but.... this is very out there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940530):
Right. I would think that maybe Lean could output some hints that will help it to verify the proof deterministically and fast the next time round.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 12 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940543):
There's also no need to give up determinism merely because you have good heuristics for searching the "interesting" parts of the tree first.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940546):
Hmm, true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940554):
But, do you know of good heuristics?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 12 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940618):
I really need to explore uses of my `rewrite_search` tactic outside of category theory. It attempts to prove `A = B` by exploring the graph of all possible rewrites by a given set of lemmas, but targets the search by exploring the parts of the graph with least "edit distance" between the LHS and the RHS, for various interpretations of "edit distance".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940678):
Sounds promising.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940687):
Can't wait to have such stuff available at my fingertips (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 12 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940850):
@**Johan Commelin** Do you understand the consequences of all this for the perfectoid project?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127940967):
@**Kevin Buzzard** What do you mean? The consequences of Scott's tactics, or the consequences of this topological diamond?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127941012):
Now that I think of it, we can probably remove the diamond by just not making it an instance. That means we can write nice stuff like `is_complete R` but we can still write `is_complete (to_uniform R)`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 12 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127941017):
I just mean whether you now know the answer to the question "will stuff like [instance top_ring_to_uniform_space] mess up the type class system?"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127941020):
And then, when those with more Lean-fu then the mortal mathematicians have some time,  they can fix the diamond issue, and we can write nice code again.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 12 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127941026):
I mean that I have not really been following the details of this typeclass discussion and am wondering if you now know enough to tell me how to set up the perfectoid project.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127941071):
Maybe @**Patrick Massot** can join in. But my suggestion would be to have an explicit map from top_rings to uniform_spaces, and just use it explicitly when needed. (Because I think we don't need it that often.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 12 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127941129):
I should note that when I started writing schemes I didn't use type class inference for anything (I had lots of rings and didn't use it for them). You don't have to use it. It's just supposed to make things easier. If it doesn't make them easier then we can probably avoid it. If we convince ourselves that it's not robust enough then we can avoid it. Is there some sort of underlying unfixable problem with modules?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127941192):
We don't need modules for this project, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127941201):
Modules seem to be rather easy to agitate in Lean. I think we could write `module'` that avoids the type class system, but it would duplicate a lot of effort; and ultimately it is not the path we want to take.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127941240):
But in the current situation it seems to me that modules are almost unusable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127941312):
In that Gitter link, Mario said that the ring shouldn't be a field in the `module` structure. But I don't really understand why not. I think it would solve a lot of problems, and I don't really see what kind of problems it creates.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127941414):
@**Mario Carneiro** If you have time, could you say a few words about why the ring shouldn't be a field of the `module` structure?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 12 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127941683):
```lean
noncomputable def poly.map {S : Type} [ring S] (f : S → R) [is_ring_hom f] : polynomial S → polynomial R :=
finsupp.map_range f (is_ring_hom.map_zero f)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 12 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127941723):
@**Johannes Hölzl** Should this map be noncomputable, or should we try to make it computable by making extra assumptions on `R` and/or `S` and then over-riding them later?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127941728):
I think it is fine to have this in `for_mathlib`, but it should go into the mason_stothers lib at some point.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 12 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127941732):
err... it should go in mathlib!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127941737):
Yes, by transitivity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127941775):
And then in mason_stothers they can make it as computable as they want :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 12 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127944104):
> Right, but picking up the existing topology is going to be pretty hard, I guess.

It is not difficult to set this up with the current setup. You should just not use `uniform_space.to_core`, just construct the uniform space using the constructor

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jun 12 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127944105):
```quote
@**Johannes Hölzl** Should this map be noncomputable, or should we try to make it computable by making extra assumptions on `R` and/or `S` and then over-riding them later?
```
this should be computable now, in the recent mathlib versions, `finsupp.map_range` is computable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 12 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127944182):
>  If you have time, could you say a few words about why the ring shouldn't be a field of the module structure?

At least with the current setup, it is generally not a good idea to have types as fields in the structure. If you did this with the scalar ring of module, you wouldn't be able to talk about ℝ-modules without imposing an equality condition, which would cause cast headaches

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127944318):
Hmm, do you mean that all of a sudden you have 1 type for *all* modules? So, if you would have fields `(R : Type) (hR : ring R)` in the structure, then you want to define `is_linear_map [module M] [module N] (M -> N) : Prop`, but now they might be modules over different rings!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127944319):
Or do you mean something more subtle?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 12 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127945989):
If you have rings `A` and `B` and a ring map `A -> B`, and an `A`-module `M` and a `B`-module `N` then mathematicians would quite happily talk about `A`-module homomorphisms `M -> N`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 12 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127945991):
because `N` inherits an `A`-module structure from the map `A->B`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 12 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127946051):
but as Johan points out, this discussion is, at least at this point, in the wrong thread, this is Patrick's type class woes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127946876):
Right, so returning to perfectoid spaces... what is the next step?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 12 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127946880):
Should we pull stuff on presheaves in from your schemes-repo?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 12 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127951650):
The next step is for me to accept these PRs and then have a look at what is left.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 12 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127951658):
I think I want to do presheaves because I did them before

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 12 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127951663):
I think the next step is the topological space Spa(A)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 12 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127951665):
for A a Huber pair

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 12 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/127951668):
and that goes via Spv(R)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 13 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128030961):
```quote
It is not difficult to set this up with the current setup. You should just not use `uniform_space.to_core`, just construct the uniform space using the constructor
```
What do you call "the constructor"? I'm not worried at all, I'm pretty sure I have the mathematical content right, and I used the filter library so we will have all lemmas we need. But I'm not quite sure what I should do (And I had no time at all since Saturday, because of a conference and invited people).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 14 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128034520):
I mean the default, built in constructor for a structure, the thing that you get with `{ x := ... }` notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 14 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128034532):
I guess the constant is called `uniform_space.mk`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 14 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128034688):
If you just delete the `of_core` function application in the instance, and just use that structure directly as the instance, it will more or less work, except there will be a new proof obligation for the part of the proof that `of_core` was doing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 20 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128382738):
I've spent the last few days doing non-Lean stuff but I would like to accept these PRs soon; I read through them all properly today. One thing that occurred to me about this uniform space business is that Patrick's construction of a uniform space on a topological ring should (a) probably work for a topological group and (b) might already be in mathlib (if the docstring for `uniform_space` is anything to go by). @**Johannes Hölzl** you wrote "A topological group also has a natural uniformity, even when it is not metrizable" in the docstring for uniform space -- is this theorem somewhere in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 20 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128382990):
This is in the pipeline last I checked. it should appear soonish

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 20 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128383004):
I think Johannes is working on merging Patrick's normed space stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 20 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128383352):
Thanks. I've not been at all Lean-active for the last week or so, and today I tried to catch up with perfectoid spaces but there's a whole bunch of stuff which should be in mathlib but isn't; I could open about 8 small PRs but I didn't want to add to the pile because I can happily store them in my project. However stuff like polynomials in 1 variable, which is lengthy, presents more of a problem because mason-stother doesn't compile at the minute. Patrick has explicitly proved that a topological ring has a uniform space structure and it wouldn't surprise me if his proof worked for topological groups. So we have something if you or Johannes want it. For the schemes project I just kept bundling everything in my repo but this time I'd rather do it more sensibly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 20 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128383430):
I'm not sure how useful this will be given that Johannes is working on this stuff at the moment - it may just be additional merging overhead. You should coordinate with him

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 20 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128383472):
OK thanks for the tips.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 20 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128385520):
I'm sorry I haven't talk at all since last saturday. I'm attending a conference and have extremely bad internet access in my hotel (only my phone is able to use the wifi, at very slow speed). I have completely rewritten my uniform structure stuff, and I hope to PR it tomorrow from the lecture hall. It now provides a uniform structure on commutative topological groups which gives back a topology defeq to the original one. I'm very grateful for Johannes work but it seems both over-engineered and nit enough. I have no idea what kind of generalization he has in mind.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 20 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128385715):
Polynomials in 1 variable I'd really like to see in mathlib; so even if Kevin can "happily store them in my project", let's try to accumulate as little as possible in the perfectoid repository.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 21 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128387586):
```quote
Polynomials in 1 variable I'd really like to see in mathlib; so even if Kevin can "happily store them in my project", let's try to accumulate as little as possible in the perfectoid repository.
```
Currently we're unhappy when it comes to polynomials. We tried using Johannes' mason-stother but not all of it compiles. Currently we're sorrying stuff.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 21 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128387592):
I proved its UMP :P although Chris did much more than me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 21 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128387602):
```lean
def polynomial.UMP (A : Type v) [comm_ring A] [algebra R A] :
  A ≃ alg_hom (polynomial R) A :=
(ℕ.UMP A).trans (monoid_ring.UMP _ _ _)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 21 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128387603):
https://github.com/kckennylau/local-langlands-abelian/blob/master/src/polynomial.lean#L37

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 21 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128387688):
o_O there is group cohomology, Galois theory, and local class field theory in that repo too!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 21 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128387692):
You have been busy.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 21 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128387745):
well I can’t talk too much ‘bout it now :p

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 21 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128387750):
we both know the reason

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 21 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128387762):
I shall be grilling you on it in about 36 hours.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 21 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128411780):
@**Kevin Buzzard**  the situation with uniform structures is now as follows. Contrary to what the docstrings you mentioned suggests, mathlib currently doesn't know that a commutative topological group has a canonical uniform structure. What @**Johannes Hölzl** did recently was to write https://gist.github.com/johoelzl/ca90562c46b49a1bbb1be36272ec3b1a At the same time I decided to use my flight to learn a bit about filters instead of complaining I'm not used to them. Then I wrote https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/top_rings/src/for_mathlib/topological_structures.lean. What are the differences then? The obvious one is that Johannes' code is shorter and most probably cleaner. But it also doesn't address the main question. He defines a class `group_with_nhds_zero` which seems to be a generalization of topological groups, remembering just enough about properties of neighborhoods of zero in a topological group to define the uniform structure. He doesn't prove topological groups give instances of this new class but this should be easy (one would need to be careful with the topology induced by the uniform structure to be defeq to the original one, which is what I messed up in my first attempt). My concern is over-engineering: I see no use of this new class beyond topological group. AFAIK this only adds a layer of complexity. Actually I was already completely puzzled by [this section](https://github.com/leanprover/mathlib/blob/905345a2ceaa5d0c7bc2f6310026961416b2cae4/analysis/topology/topological_structures.lean#L198). I have no idea how this could be useful beyond the obvious case where the uniform structure is the canonical one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 21 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128431953):
I don't think these CS people worry about over-engineering. I guess as we just saw from the filter stuff, it's actually sometimes convenient to have these things around. I've written a paper about adic spaces and I don't understand filters, but that's only because for actual adic spaces you only basically deal with rings whose topology is generated by a finitely-generated ideal, when sanity is restored. [by "generated by" I mean that powers of the ideal form a basis of neighbourhoods of zero]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 21 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128437221):
Oh wow I have universe issues! 

A valuation on a ring $$R$$ is a map from $$R$$ to a totally ordered commutative monoid satisfying some axioms. Two valuations $$v$$ and $$w$$ are *equivalent* if $$v(r)\leq v(s) \iff w(r)\leq w(s)$$. The *valuation spectrum* $$Spv(R)$$ of $$R$$ is the set of equivalence classes of valuations.   As a ZFC-ist I did a little calculation here -- I checked that every valuation (which could take values in a monoid which gigantic cardinality, far far bigger than that of R) was equivalent to a valuation taking values in basically the monoid generated by the image of R (I'm being a bit sloppy -- one has to check that there is no issue here with the axioms for a valuation). But at the end of the day I have a set.

In Lean I have

```lean
structure valuations (R : Type) [comm_ring R] :=
{α : Type}
[Hα : linear_ordered_comm_group α]
(f : R → option α)
(Hf : is_valuation f)
```

and I can define two valuations to be equivalent 

```lean
instance valuations.setoid (R : Type) [comm_ring R] : setoid (valuations R) :=
{ r := λ f g, ∀ r s : R, f r ≤ f s ↔ g r ≤ g s,
  iseqv := ...
```

but the associated quotient has type `Type 1`, so in theory I have left the world of ZFC. As I just outlined above, in ZFC I know how to claw my way back [I can put an upper bound on the cardinality of alpha and hence build a *set* containing at least one instance of every equivalence class]. Can I do this in Lean somehow?
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 21 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128438592):
If you don't care about computational content (I hear you Kenny, keep it down), you can notice that a valuation equivalence class is determined by the relation `S : R ->  R -> Prop` defined by `S r s <-> v r <= v s`. That is, two valuations are equivalent if and only if they have equal induced relations on R. Thus you can define the spectrum to be the collection of all relations that arise from some valuation (from a commutative monoid in the same universe as R).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 21 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128440055):
This is a good example of the kind of situation I was asking about here -- https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/type.20resizing/near/127424550

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 21 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128441152):
The answer is ad hoc. Essentially you figure out the "reason" why your set is small, which will take the form of some small set that enumerates your large objects, and use that as the index instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 22 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128445451):
The "reason" for me was a standard ZFC-ish one: one can "shrink" the target until it's generated by the image of R, and hence has the same cardinality of R (or aleph_null if R is finite). So we get a bound on the cardinality of the target and this suffices because the set of isomorphism classes is now a set. The relation argument is alien to me, although obviously I believe it. I am torn about whether I should care about this -- should I write my own "section 4" or just forget it? Interestingly, I notice that the foundational paper https://arxiv.org/abs/math/0409584 (section 1 page 7) which is strongly related to the foundations of what Scholze is doing, assumes that every set is contained in a universe. This paper would be really nice to formalise! Although those that look at it will quickly see what the issue is...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 22 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128448999):
There is nothing wrong with your argument, and indeed you can also use it to get a bound as well. The relation argument just seemed easier since it literally defines the equivalence relation, making the quotient trivial. Actually you would probably want to run that argument anyway to prove that given a valuation in any universe you get a relation, since this amounts to constructing an equivalent valuation in the same universe as the ring.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128551939):
So I finally followed up on this. Here's what the code looks like (I removed the actual definition of valuation to simplify things):

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128551947):
```lean
import data.equiv 

def is_valuation {R : Type} [comm_ring R] {α : Type} [linear_order α] (f : R → α) : Prop := sorry

structure valuations (R : Type) [comm_ring R] :=
(α : Type) [Hα : linear_order α] (f : R → α) (Hf : is_valuation f)

instance to_make_next_line_work (R : Type) [comm_ring R] (v : valuations R) : linear_order v.α := v.Hα

instance valuations.setoid (R : Type) [comm_ring R] : setoid (valuations R) := {
  r := λ v w, ∀ r s : R, valuations.f v r ≤ v.f s ↔ w.f r ≤ w.f s,
  iseqv := ⟨λ v r s,iff.rfl,λ v w H r s,(H r s).symm,λ v w x H1 H2 r s,iff.trans (H1 r s) (H2 r s)⟩
}

def Spv1 (R : Type) [comm_ring R] := quotient (valuations.setoid R)

def Spv2 (R : Type) [comm_ring R] := 
  {ineq : R → R → Prop // ∃ v : valuations R, ∀ r s : R, ineq r s ↔ v.f r ≤ v.f s}

#check Spv1 _ -- Type 1
#check Spv2 _ -- Type
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552037):
`Spv1` is the equivalance classes of valuations, and `Spv2` is the associated vague notions of order (it's not antisymmetric because `f` might not be injective -- maybe it's a preorder?) on `R`. The constructions live in different type universes. But are they equiv?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 24 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552038):
equiv can take different universes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552039):
In other words, should I expect to be able to prove `noncomputable definition they_are_the_same (R : Type) [comm_ring R] : equiv (Spv1 R) (Spv2 R) := sorry`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552040):
Yes Kenny, I noticed this -- so at least my question typechecks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552048):
Here are perhaps the functions:
```lean
def to_fun (R : Type) [comm_ring R] : Spv1 R → Spv2 R :=
quotient.lift (λ v,(⟨λ r s, valuations.f v r ≤ v.f s,⟨v,λ r s,iff.rfl⟩⟩ : Spv2 R))
  (λ v w H,begin dsimp,congr,funext,exact propext (H r s) end) 

noncomputable def inv_fun (R : Type) [comm_ring R] : Spv2 R → Spv1 R :=
λ ⟨ineq,H⟩,⟦classical.some H⟧
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552092):
I don't know if that's going to give me trouble because I used tactics in a definition -- but it was for a proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552471):
To prove either direction I need to show something about a map constructed using quotient.lift (assuming this is the way to define `to_fun`). For example `right_inv` boils down to

```lean
R : Type,
_inst_1 : comm_ring R,
rel : R → R → Prop,
Hrel : ∃ (v : valuations R), ∀ (r s : R), rel r s ↔ v.f r ≤ v.f s,
r s : R
⊢ (to_fun R ⟦classical.some Hrel⟧).val r s = rel r s
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552571):
Is this quotient.something?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552610):
and `left_inv` looks like
```lean
R : Type,
_inst_1 : comm_ring R,
vs : Spv1 R
⊢ inv_fun R (to_fun R vs) = vs
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 24 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552613):
just `unfold` everything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552614):
I don't need this equiv, but I'm trying to get a feeling for the relative merits of either definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552619):
If you unfold everything you end up with classical.somes which don't behave

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552620):
or at least I did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552657):
you end up with a goal of the form `classical.some _ a <= classical.some _ b iff classical.some _ a <= classical.some _ b` or something, and iff.refl doesn't work because the `_`s are slightly different -- or at least they were for me (with the definition of valuation filled in)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 24 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552662):
what is the property of each some

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552663):
Kenny it must be more than an unfold -- the `left_inv` goal has `vs` in it and we know nothing about `vs` other than its type --

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552672):
I don't know if I'm making a wrong turn, but I tried `quotient.exists_rep`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552813):
Here's an example of the sort of mess I get into:
```lean
  left_inv := λ vs,begin
    cases (quotient.exists_rep vs) with v Hv,
    rw ←Hv,
    apply quotient.sound,
    intros r s,
    have H := classical.some_spec (to_fun R vs).property,
    rw (H r s).symm, -- fails
    /-
    rewrite tactic failed, did not find instance of the pattern in the target expression
  (classical.some _).f r ≤ (classical.some _).f s
state:
R : Type,
_inst_1 : comm_ring R,
vs : Spv1 R,
v : valuations R,
Hv : ⟦v⟧ = vs,
r s : R,
H : ∀ (r s : R), (to_fun R vs).val r s ↔ (classical.some _).f r ≤ (classical.some _).f s
⊢ (classical.some _).f r ≤ (classical.some _).f s ↔ v.f r ≤ v.f s
    -/
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128552819):
I wondered if I'd made a wrong turn

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128553388):
https://gist.github.com/kbuzzard/e0b36acade48f955212e8ea5142cb7b1 is where I'm at. Somehow I was expecting this to be easier. Various failures deleted.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128553587):
Perhaps I should outline the reason I'm even thinking about this. Part of me still wants to work in ZFC so everything should live in `Type`. But the natural definition of `Spv R` lives in `Type 1`. I just wanted to weigh up the pros and cons of the two approaches. If I can prove they're equiv then many of the assertions I'll be making about one type will be true for the other one by some general "canonical isomorphism" principle. I figured that if I kept track of both then I could see to what extent my code was affected by the choice I'll ultimately make. But if I can't prove the equiv then I am less sure that the two approaches are "the same". Probably the equiv is fine and it's just my general incompetence with quotient types. Maybe I should instead be proving that `to_fun` is a bijection?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 24 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128553768):
I wish there was an option to display the type of proofs in the pp.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 24 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128553915):
Proved` left_inv`
```lean
noncomputable definition they_are_the_same (R : Type) [comm_ring R] : equiv (Spv1 R) (Spv2 R) :=
{ to_fun := to_fun R,
  inv_fun := inv_fun R,
  left_inv := λ vs, quotient.induction_on vs begin
    assume vs,
    apply quotient.sound,
    intros r s,
    have := (to_fun R ⟦vs⟧).property,
    have H := classical.some_spec (to_fun R ⟦vs⟧).property r s,
    refine H.symm.trans _,
    refl,
  end,
  right_inv := λ s2,begin
    cases s2 with rel Hrel,
    apply subtype.eq,
    dsimp,
    unfold inv_fun,
    funext r s,
    sorry
  end 
}

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 24 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128553921):
Often when the inverse function is `classical.some`, it's much easier to use `equiv.of_bijective`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 24 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128554214):
Done
```lean
open function
noncomputable definition they_are_the_same (R : Type) [comm_ring R] : equiv (Spv1 R) (Spv2 R) :=
equiv.of_bijective (show bijective (to_fun R), 
from ⟨λ x y, quotient.induction_on₂ x y (λ x y h, 
  quotient.sound (λ r s, iff_of_eq (congr_fun (congr_fun (subtype.mk.inj h) r) s))),
  λ ⟨x, ⟨v, hv⟩⟩, ⟨⟦v⟧, subtype.eq $ funext (λ r, funext (λ s, propext (hv r s).symm))⟩⟩)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 24 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128555828):
Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 24 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128556386):
> I wish there was an option to display the type of proofs in the pp.

`set_option pp.proofs true`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 24 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128558361):
That displays the proofs, not their type.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 24 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128567000):
```quote
I think Johannes is working on merging Patrick's normed space stuff
```
@**Mario Carneiro** @**Johannes Hölzl**  What do you mean? Is he extracting stuff from https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/norms.lean? This effort is completely stopped because of type class resolution issues in the very last declaration of that file that seems to be related again to the modules and rings issue.  I would really love to be able to move forward. Especially since I should have quite a lot of time for Lean in the coming weeks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jun 25 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128583585):
Yes, I want to work on normed spaces. I won't have time this week (we have two workshops in Amsterdam) but the following week.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 25 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128583975):
Do you intend to fix my stuff or restart from scratch?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 25 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128584020):
Also, did you see my new version of uniform structures on topological groups (that I discussed  in this thread four days ago)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 25 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128602123):
I wanted to start working on completions of abelian topological groups and noticed I forgot to prove the uniform group instance. This is now done in https://github.com/PatrickMassot/lean-perfectoid-spaces/commit/adb5140ecc46a577325cda46dcf6626424f5ef02

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 25 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128602198):
`sub_eq_add_neg` being a simp rule is really a nuisance. I can't imagine any situation where I would want to replace `a - b` with `a + -b`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 25 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128609748):
The idea that neg is a "simpler" function than sub I guess. Computer scientists seem to have some crazy ordering of things which is very counterintuitive to mathematicians. Concepts which we regard as having equal weight often don't have equal weight in Lean. I guess Lean is trying to put something into some kind of canonical form with simp, and clearly this canonical form isn't supposed to have any subs in.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 25 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128610190):
I guess some `simp` lemmas deal with add and neg, but not sub. It's not that weird, everyone writes $$a b^{-1}$$ in a group, but never $$a / b$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 25 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128610297):
Conversely no schoolkid writes 5 + (-3), they all write 5 - 3

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 26 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128634201):
I just discovered the `[norm]` simp set thanks to Simon:
> Add [norm] simp set. It contains all lemmas tagged with [simp] plus any lemma tagged with [norm]. These rules are used to produce normal forms and/or reduce the number of constants used in a goal. For example, we plan to add the lemma f <$> x = x >>= pure ∘ f to [norm].

I agree that the sub elimination theorem is a horrible simp lemma, and it's a candidate for `[norm]` if anything is.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 27 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128703012):
I think we can improve readability of the code that uses valuations by using slightly longer names in https://github.com/kbuzzard/lean-perfectoid-spaces/blob/cc415fe8834b4886a5305feb89ac566d7b04ba94/src/valuations.lean#L338
I suggest that the field `f` be called `fun` and `Hf` be called `is_val`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 28 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128759497):
Hmm, I see that there was a coercion that would coerce `v` to `v.f`. @**Kevin Buzzard** Why was that removed? I think it greatly improves readability...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 28 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128759506):
And it hides the `.f` so then I don't care so much how that field is called (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 28 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128759708):
It didn't work sometimes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 28 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128759763):
But I was too lazy to debug. I was sitting next to Chris when I wrote it and he said "oh yeah, has coe to fun is a bit rubbish and doesn't always work" and although I interpreted this as "we need to ask Mario why it is failing" I just wanted the code to work so I removed it. Put it back, see what breaks, and ask for help!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 28 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128759780):
Yeah, my experience of coercions is that the pain of them mysteriously not working (usually it's not so mysterious, just Lean isn't quite as clever as you are guessing what you really meant to say) far outweighs the smoothness when they do work. But I like writing verbose code, anyway. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 28 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128759886):
Ok, will do (-; So far nothing is breaking...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 28 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128759965):
Scott, yes I understand that. But in this case I think there are some crucial parts of the code that should be as readible as possible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 28 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128768192):
I removed the coercion for all the wrong reasons. It was Thursday night at Xena, I was low on battery, I had nearly finished a file, it was time to go home, I asked Chris why my code didn't work and he said he'd had trouble with `has_coe_to_fun` and I thought "sod it I'll just remove it". I commented it out specifically to remind future me to come back to it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 28 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128768441):
In other news, I discovered a subtlety in the definition of continuous. Two valuations `v : R -> option alpha` and `v' : R -> option beta` are equivalent if $$v(r)\leq v(s)\iff v'(r)\leq v'(s)$$ for all $$r,s$$. There are other equivalent ways of writing the equivalence, and it's a lemma that they all coincide. Unsurprisingly, at some point I found I needed the lemma, but surprisingly it was in the definition of continuous. My slightly superficial (as it turns out) understanding of the definition of a continuous valuation was that $$v$$ was continuous iff the pre-image of `a : option alpha // a < b` was open for all b in alpha -- but this is not always constant on an equivalence class! The problem is that alpha might be embedded as some infinitesimally small subgroup of beta, and then beta contains elements smaller than everything in the image other than 0 (the `none` option) which have no analogue in alpha. One has to restrict to b's which are in the group generated by the image of v. I'd never noticed this before. 

So we need to prove 1.25 and 1.27 in Wedhorn -- but then it turns out that we don't even have quotient rings and the fact that the quotient of a comm ring by a prime ideal is an integral domain. These are not hard -- but it's funny to see how holey everything still is. I am about to ask Kenny to fill in my sorries :-) [I just committed some stuff]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 02 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128955982):
That actually sounds pretty technical! I would have glossed over this for sure...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 02 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/128956469):
Working on the definition of manifolds in Lean also taught me that the well known fact that the relation of equivalence of atlases is an equivalence relation has slightly more content that I was aware of. I don't think there is any book proving this fact. Most of them simply use the word "equivalence class" without writing "equivalence relation" anywhere (this includes my own lecture notes on differential topology). Some write "is easily seen to be an equivalence relation". I haven't seen any proof anywhere except on my scratchpad.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008758):
@**Kevin Buzzard** I'm confused: why are you changing `is_valuation` to `valuation`? I thought that it should be `is_*` because the type is `Prop`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008765):
Is there a good explanation of these naming conventions somewhere?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008771):
We can have `is_` if you like.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008781):
Well... you're the boss :rolling_on_the_floor_laughing:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008784):
It is just that I got a bit confused... but I'm not sure if there even is a solid convention.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008794):
Boss -- not really. And I don't understand the rules properly. I think Kenny had a namespace `is_valuation` which I thought was going a bit far.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008844):
What is the convention in question? (I think I am the MC - Master of Conventions)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008854):
So a function f from a ring R to some totally ordered monoid M is a _valuation_ if it satisfies some axioms.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008884):
Is it a property of the function, or an augmented function?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008899):
```lean
class valuation {α : Type} [linear_ordered_comm_group α]
  {R : Type} [comm_ring R] (f : R → option α) : Prop :=
(map_zero : f 0 = 0)
(map_one  : f 1 = 1)
(map_mul  : ∀ x y, f (x * y) = f x * f y)
(map_add  : ∀ x y, f (x + y) ≤ f x ∨ f (x + y) ≤ f y)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008901):
That used to say `class is_valuation`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008949):
I think it should be `is_valuation` then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008954):
The next line in the code is `namespace valuation`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008957):
Kevin, you see `Prop` stands for *property* :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008961):
and did it used to say `namespace is_valuation`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008974):
`namespace valuation` will be annoying since it's not accessed by projection

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008976):
since it's a typeclass

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008981):
I don't understand that. I've never understood projection properly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129008999):
I just muddle through with projections. I write `G.mul_assoc` and if it doesn't work I write `group.mul_assoc G`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009031):
To use projection you have to be projecting on an expression whose type has the same name as the namespace

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009033):
and I never have a clue which one I'm supposed to use or which one will work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009044):
If you use typeclass inference, then the operative name is in a hidden parameter, so it doesn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009049):
These words are too hard for me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009064):
i.e. you can't write `f.map_zero` when you know `is_valuation f` because lean looks at the type of `f`, which is `pi`, and then checks the `pi` namespace only

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009071):
(actually that doesn't really work, `pi` isn't a namespace)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009118):
but for inductive types like `nat` which are also namespaces, it works well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009119):
Kevin, you can write `H.bla` for `[H: is_valuation f]`, but not `f.bla`. But then, we want `H` to be implicit (type class inference, etc...) so in practice you won't be able to type `H.bla` because there is no explicit `H`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009130):
What I do not understand (at all) is whether I should have _something_ called `valuation`. We have `group G`, right? Why can't I have `valuation f`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009133):
I don't see the difference

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009135):
I think lean might complain if `H` turns out to be implicit in `is_valuation.bla` though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009136):
Because `group` has extra structure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009156):
Why do I want to use type class inference for valuations?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009160):
I do not understand what we want here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009162):
I was just sick of writing is_

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009166):
If you use the augmented function approach you can use the name `valuation` and call functions by projection

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009169):
So, if you have a `monoid` or something like that, you could have a `is_group G : Prop`, but `group G` is not a `Prop`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009214):
You can also just ignore conventions if you think `valuation` will never be defined

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009220):
What's worse is that "valuation" in the literature actually means "equivalence class of valuations"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009224):
You didn't like my valuation = relation suggestion?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009235):
I don't know about that either. I implemented both

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009240):
I have `zfc.valuation` too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009244):
ooh, mysterious

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009254):
just means "I only use Type"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009263):
why would you do that? You can just restrict the universe variables of polymorphic functions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009310):
I've just realised I don't even know what is being suggested. (1) I change `class valuation ... : Prop` back to `class is_valuation`. Then what? Is `namespace valuation` changing back to `namespace is_valuation`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009315):
"I only use Type" is just a maths thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009329):
You can put it in a namespace if you want, or use `valuation_*` pseudo-namespacing, or put the theorems in the parent namespace

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009332):
Kevin, I think Mario would want
```lean
structure valuations (R : Type) [comm_ring R] :=
{α : Type}
[Hα : linear_ordered_comm_group α]
(f : R → option α)
(Hf : is_valuation f)
```
to be called `valuation`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009341):
But I am not sure about that...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009343):
Only the `f` and `hf` should be in the structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009345):
No...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009385):
Two valuations are equivalent if they "only differ by the alpha"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009388):
you can still state that with the alpha as parameter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009398):
But then `valuations` depends on `alpha`, that becomes horrible right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009399):
I have valuations defined to be something else

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009402):
no, that becomes tractable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009414):
(I would drop the `s` though)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009419):
no I don't, I have valuations to be defined exactly like that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009441):
then
```
instance valuations.setoid (R : Type) [comm_ring R] : setoid (valuations R) :=
{ r := λ v w, ∀ r s : R, v.f r ≤ v.f s ↔ w.f r ≤ w.f s,...
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009442):
Mario, then you have defined "valuation on R with value group alpha" (why not `Gamma`?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009486):
alpha not Gamma because Kenny wrote it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009488):
Note that `valuations` as Johan quotes lives in `Type 1`, so if it's aiming for zfc land it's not doing so great

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009494):
I don't know whether I should be worrying about ZFC or not. It seems futile really because I use so much other stuff with universes in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009498):
Yes, and *I* am completely fine with that (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009512):
Maybe I'm just making sure that one day I can write my own section 4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009521):
> Mario, then you have defined "valuation on R with value group alpha" (why not Gamma?)

Yes, that's the point. The equivalence relation can span two value groups

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009581):
```quote
Only the `f` and `hf` should be in the structure
```
I don't understand how to make the setoid if alpha is not where Johan put it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009608):
Kevin, someday I will write a treatise on lean in ZFC and there will be an automated analysis to find out if your theorem uses universes in an essential way. Until then, just write things that are intuitively not using universes essentially and don't otherwise worry about it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009616):
There is a "minimal" alpha associated with every valuation, which is unique up to unique isomorphism -- it's just the group generated by the image of teh valuation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009623):
Mario -- that's great news about ZFC. I'm sure there will be mathematicians out there who genuinely care (those who read the section 4's in this world)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009665):
*I* care

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009680):
There was a lot of fuss after FLT was proved, on the foundations of maths mailing list, because Wiles had used categories

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009685):
so a rumour started that the proof didn't fit into ZFC

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009688):
but the analysis is not quite as easy as "just stick to Type", even if it is morally just that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009696):
Isn't the analysis just "just stick to Type, and demand that all your libraries do the same"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009699):
Or is even that not enough?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009704):
The problem is that almost everything you write is trivially not just in Type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009709):
?!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009710):
for example, any function Type -> Type is not in Type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009754):
i.e. `huber_ring` or whatever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009765):
these are justifiable in ZFC as class functions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009772):
Ok I give in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009796):
As far as I am concerned, universes are just the axiom of infinity on steroids. Which means I am not concerned...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009801):
But my point is that this analysis, when it eventually arrives, will handle universe polymorphic functions, so you shouldn't avoid polymorphism for the sake of "chapter 4"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009850):
Mario, so how do we write an alpha-agnostic setoid with your version of `valuation`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009861):
You shouldn't literally write a setoid

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009862):
it's too big

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009872):
instead you just use the equivalence relation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009877):
and use the relation as a small representative when you need one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009879):
But we need the actual valuation functions all the time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009928):
Mario, so what is morally wrong with the current version that I quoted?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009929):
Line 1 of `valuation_spectrum.lean` is
```lean
definition Spv (A : Type) [comm_ring A] : Type 1 := quotient (valuation.valuations.setoid A)

namespace Spv 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009935):
and this is a fundamental object

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009940):
Spv is almost an adic space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009941):
Right, and `Spv` is the basic building block of all this theory. It is all over the place.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009943):
You can define the setoid, but it is one of the things that "essentially uses universes"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009945):
and we're constantly choosing points

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009954):
The fundamental topological space which we use all the time is the space of equivalence classes of valuations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009956):
so we have to get this right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009960):
```quote
You can define the setoid, but it is one of the things that "essentially uses universes"
```
Is that its only moral failure?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009961):
What's wrong, again, with defining `Spv` as the collection of all valuation relations?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129009967):
All proofs need an actual valuation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010011):
You can define your own version of `quot.lift` and `quot.mk` that take valuations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010013):
valuation functions that is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010014):
Aah

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010026):
You only use the relations as inhabitants of the type so that the universe isn't pushed up, but all the work uses functions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010027):
So we hide all the noncomputable stuff in some functions like this, and prove everything we need about them. Is this going to cause problems later?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010086):
We define Spv as the preorders on R (or whatever the word is) for which there exists a valuation inducing it, and then write some horrible-looking functions which actually produce a valuation...wait. The valuation is only defined up to equivalence. How does this work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010087):
You will need to prove the computation rule, so it won't be definitional, but otherwise it should work smoothly if your API is solid

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010096):
Is my API the thing I sometimes call my interface?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010101):
No function to produce a valuation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010105):
that's not how `quot` works either

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010114):
The function produces an equivalence class? Do we make the setoid anyway?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010115):
The "I" in API is "interface"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010162):
No equivalence class needed either

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010164):
Like I said, `quot.mk` and `quot.lift`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010169):
`quot.mk` takes a valuation function and produces an element of `Spv`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010174):
`quot.lift` takes a function defined on valuation functions and produces a function defined on `Spv`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010188):
So what about proofs which go "Spv(R) is compact. Proof: take an element of Spv(R), call it v or f or whatever, and now manipulate f in the following way..."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010195):
That's `quot.lift`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010200):
Actually you will want `quot.ind` as well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010210):
or equivalently `quot.exists_rep`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010262):
that is, for every element of `Spv` there is a valuation function that `quot.mk`'s to it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010274):
Note it's not actually a function producing valuation functions, it's an exists

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010284):
So if I step back here, you're saying "Experts wrote an API for `quot`. Because of some design decisions I'm suggesting about alphas, you can't use this, but write your own, everything will be fine"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010289):
Just because you don't want an alpha inside a structure?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010291):
The definitions on `quot` are all very canonical

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010296):
they are essentially the universal property of quotients

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010297):
Can you define "very canonical" in Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010299):
That sounds even harder than defining canonical

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010343):
if you prove analogues of those theorems for your type, then you have constructed the quotient up to isomorphism

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010345):
up to canonical isomorphism maybe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010348):
indeed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010350):
It had better be canonical, because if R -> S then I need Spv(S) -> Spv(R)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010368):
Not that I can define canonical in Lean...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010409):
This all has a category theoretic interpretation as a coequalizer, and all constructions are natural in that category

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010411):
As opposed to, say, `quot.out`, which picks an element from an equivalence class

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010428):
Although in your case if I understand correctly you also have a canonical way to define `quot.out` satisfying some other universal property to do with the ordered group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010534):
So in summary, we should have
```lean
structure valuation (R : Type) [comm_ring R]
(α : Type) [Hα : linear_ordered_comm_group α] :=
(f : R → option α)
(Hf : is_valuation f)
```

and then maybe `namespace valuation` except I still don't properly understand what the word projection means and what it has to do with namespaces, and then we define `Spv` to be 

```lean
definition zfc.Spv (A : Type) [comm_ring A] : Type := 
  {ineq : A → A → Prop // ∃ v : valuations A, ∀ r s : A, ineq r s ↔ v.f r ≤ v.f s}
```

except "valuations" there isn't quite right yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010537):
and then we need to write quot.mk, quot.lift, quot.ind and quot.ind

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010539):
I see www.quot.mk is available

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010547):
For augmented functions, I recommend a `has_coe_to_fun` instance so you can write `v r <= v s` at the end there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010596):
Yeah I want to move back to the coe_to_fun approach. I dumped it too early when Chris told me he'd had trouble with it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010605):
```
definition zfc.Spv (A : Type) [comm_ring A] : Type :=
{ineq : A → A → Prop // ∃ (A : Type) [linear_ordered_comm_group A]
  (v : valuation R A), ∀ r s : A, ineq r s ↔ v r ≤ v s}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010667):
If you want to be polymorphic, I suggest writing
```
 def zfc.Spv (A : Type u) [comm_ring A] : Type :=
{ineq : A → A → Prop // ∃ (A : Type u) [linear_ordered_comm_group A]
  (v : valuation R A), ∀ r s : A, ineq r s ↔ v r ≤ v s}
```
where the valuation and ring have to share the same universe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010679):
You can prove that the universe need not be the same as part of the universal properties

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010727):
i.e. `Spv.mk` takes as input a valuation function ` (v : valuation R A)` where `{R : Type u}` and `{A : Type v}` (so it isn't just instantiating the exists)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010827):
"If you want to be polymorphic" -- I just want to do maths. I have no idea if I want to be polymorphic. If I just want to define a perfectoid space, do I want to be polymorphic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129010994):
In lean, you should usually be polymorphic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129011010):
at least in contravariant positions (i.e. the inputs should be maximally polymorphic, the output should be minimally polymorphic)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129011016):
This is why we don't have `nat : Type u`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jul 03 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129012912):
If I read correctly, you want to have a class `is_valuation`, and then a structure type `valuation` made of all functions `f` satisfying the valuation axioms, i.e., with `is_valuation f`. What is the advantage of this approach (with typeclass inference) over the more direct approach with a structure type `valuation` in which you put directly the axioms, and then when you want to work with a valuation you just use `(v : valuation R A)` (so, getting rid completely of the typeclass `is_valuation`)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129013477):
The problem is that a valuation is a function from a ring to some totally ordered monoid, and there's an equivalence relation which needs to be taken into account, of the form "these monoids might not be the same, but there's a map from the image of one function to the image of the other which makes lots of things commute". `Spv R` is the equivalence classes of valuations.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jul 03 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129014391):
I understand this. My question is about the beginning of the discussion, with this `is_valuation` class at the start of your formalization.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129015550):
I am not the person to ask, I don't think. I have no understanding of how best to do these things in Lean, that's why I'm floundering around here. I understand the maths perfectly. Let me try and read your messages. Yes we have an inductive prop `is_valuation f`which is a class although I don't know if that's sensible (I think Kenny made it a class so it probably is). We then apparently are supposed to have  a type `valuation R alpha` which is all valuations taking values in alpha; I have no real understanding of why this is needed because I definitely don't care about all valuations taking values in alpha. You mention typeclass inference but I have no idea what should be a class because whilst I now understand what typeclass inference is and how to use it when other people have made the typeclasses, I am still extremely unclear myself about which of my own objects should be typeclasses. You now suggest I could be making a structure type `valuation` -- would this take alpha as part of the structure? I think we used to have that; Johan maybe mentioned it, and Mario said that alpha should not be part of the structure. Is A the totally ordered monoid? The only reason we have is_valuation is that someone else wrote it. I say again -- I completely understand the mathematics I want to do; I am extremely foggy about how to do it in Lean in the sense that I can see several ways and simply do not possess the toolkit necessary to work out the best way. There's my attempt to answer your question in full. At the end of the day I want `Spv R` to be the equivalence classes of valuations on R, and I have no idea whether `valuation` or `valuations` or `is_valuation` or structure or class or what is the best approach. I would happily be told explicitly what to do.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129015600):
Am I right in thinking that Mario basically told me a way of doing it above, and you are suggesting another way?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129015763):
I don't think Sebastien is suggesting anything different from what I recommended (using augmented functions)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129015837):
> I have no real understanding of why this is needed because I definitely don't care about all valuations taking values in alpha. 

The general rule is to keep types out of classes if at all possible. Lean behaves better when the types are given as "alpha" rather than "the type inside v", particularly if you start manipulating the functions (adding them, say)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129015903):
Although you want to deal with "the collection of all valuations" (which is what `Spv` is for), when doing a concrete calculation you will have a *fixed* alpha with respect to which to do your monoid algebra stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129019297):
```quote
> I have no real understanding of why this is needed because I definitely don't care about all valuations taking values in alpha. 

The general rule is to keep types out of classes if at all possible. Lean behaves better when the types are given as "alpha" rather than "the type inside v", particularly if you start manipulating the functions (adding them, say)
```
Hmmm, can you be more precise about how Lean would misbehave? Because it seems "mathematically natural/convenient" to make `alpha` part of the structure, instead of a parameter.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129019647):
it is the same things that make the difference between bundled vs unbundled groups. When working "internally", i.e. calculations using the monoid structure, it is better for the type to be exposed as a variable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129019693):
When working externally, there is already the type `Spv` to do this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 03 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129019728):
Also, there is a universe issue for the ZFC diehards

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 03 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129020385):
If I understand Sebastien correctly, then he suggesting to just merge `is_valuation f`and `valuation R Gamma` into one class. In other words, substitute the fields of `is_valuation` for the `Hf` field in `valuation`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 03 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129025279):
```quote
it is the same things that make the difference between bundled vs unbundled groups. When working "internally", i.e. calculations using the monoid structure, it is better for the type to be exposed as a variable
```
I am still not up to speed with notation. "bundled" means alpha is part of the structure? exposed type means it's not?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jul 03 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129044880):
```quote
If I understand Sebastien correctly, then he suggesting to just merge `is_valuation f`and `valuation R Gamma` into one class. In other words, substitute the fields of `is_valuation` for the `Hf` field in `valuation`.
```
Exactly (except that I don't think it should be a class, only a structure, as typeclass inference will not help you there and you want to put several valuations on the same object).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 16 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129734678):
So I didn't think about perfectoid spaces for two weeks because I've been running my summer project, doing a bunch of Lean but not this sort of thing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 16 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129734680):
I just pushed everything I had which wasn't pushed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 16 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129734940):
But I remember exactly where I was when things got crazy -- I had defined `Spv` to be the equivalence class of valuations, and then I wanted to define `Cont` to be the subset of continuous valuations. However the naive definition of continuous is not constant on equivalence classes! Every equivalence class of valuations contains some sort of canonical subset, consisting of the valuations v taking values in Gamma union 0, where the image of v in Gamma generates Gamma, and it's these valuations that have to be continuous. To isolate this canonical subclass I had to prove Wedhorn 1.27, giving various equivalent criteria for what it meant for two valuations to be equivalent. I began to formalise this but quickly realised that I needed to extend a valuation on A to A/P (P the prime ideal corresponding to the support of v) and then to Frac(A/P) (the field of fractions) and nothing was there. I began to formalise this and then never finished, and then my summer project started. I believe Chris Hughes pushed a PR over the weekend which did this ring theory stuff though, so perhaps we can get going again. Independent of all this was the naming changes, where `blah` was changed to `is_blah` and I think I managed to half-change everything and break most of the code.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 16 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129735065):
Perhaps I should have the decency to actually try and make it all compile (various names are changed in some files but noe others -- I was persuaded to go for the `is_blah` notation for Props...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 16 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129735159):
I have a class `is_valuation` now, and then a namespace `valuation` which needs to be changed to `is_valuation`. Hopefully that's an acceptable name for a namespace...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129735173):
```quote
Hopefully that's an acceptable name for a namespace...
```
Why not? Is you want to prove lemma's about `is_valuation`, then it would make a lot of sense to do that in the `is_valuation` namespace.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 16 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129735251):
Oh -- I remember the other thing which happened -- Mario suggested that the target group alpha for a valuation be moved from the structure into the input.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 16 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129735255):
I didn't do any of this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 16 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129735457):
OK it should mostly compile

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129735877):
(Zulip ought to have a :compiling: emoji...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129735947):
Kevin, I think the last few lines in valuations.lean should not be in the `is_valuation` namespace. Because that is actually about `valuations`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 16 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129736294):
Johan feel free to fix up everything. I had `valuation` and `valuations`, and then `valuation` changed to `is_valuation`, and then random `valuations` turned into `is_valuations` etc etc. I can quite believe some namespaces are wrong / don't exist etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129736306):
Ok, I'll see what I can do (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 16 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129736611):
I may as well explain the subtlety more carefully. If Gamma is some totally ordered abelian group with group law `*` then we can consider the totally ordered monoid Gamma union {0}, with {0} less than everything in Gamma (think Gamma = positive reals and the extension is the non-negative reals). A valuation on R is a map R -> Gamma union {0} plus some axioms. But in general Gamma is too big -- one only needs the subgroup of Gamma generated by v(a) for a in R and v(a) non-zero, so there's some notion of equivalent valuations. 

If the ring R has a topology then we say that v is continuous if for all g in Gamma, the pre-image of {x in Gamma union 0 | x < g} is open (definition 7.7, page 58 of Wedhorn). But this definition is not constant on equivalence classes! If v is a sensible valuation (e.g. the usual valuation on the p-adic numbers) and then we enlarge Gamma by throwing in a new variable G which is bigger than 0 but less than every element of Gamma (i.e. replace Gamma with Z x Gamma, Z the integers, with lexicographic ordering) then now all of a sudden there are lots of new elements of our value group so we can consider sets such as {x in Z x Gamma | x < G} whose pre-image is now just the support of v, which is not in general open even if v is continuous (e.g. {0} is not an open subset of the p-adics). Hence one has to stick to Gamma generated by v. That's the subtlety which stopped me working.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129736720):
Do we still want to move `alpha` out of the structure `valuations` into a parameter? I thought this was mostly to keep universes at bay...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129737343):
Isn't the easy fix to just say that we only consider preimages of {x in Gamma union 0 | x < v(a)} for some a?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129737360):
or perhaps g in the subgroup of Gamma generated by the range of v

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129737414):
That would work, but I guess we will still want to know that in fact you just replaced the valuation with something equivalent.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129737432):
I didn't change the valuation there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129737440):
I thought that the valuation equivalence relation was already defined; I mean that's what `Spv` was all about

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129737514):
I mentioned that one of the axioms you want for `Spv` is an equivalent to either `quot.ind` or `quot.exists_rep`; you can strengthen this theorem to say that every equivalence relation has a representative valuation on some Gamma union 0 such that the valuation is surjective (or essentially surjective? The range generates the group)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129737556):
Hopefully such a Gamma is unique up to isomorphism on the equivalence class

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129737571):
(Note that it would be very hard to state this theorem if `alpha` in the structure `valuations` was a field)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129737617):
because here we need to say that `alpha` is `with_zero Gamma` for some `Gamma`, but we don't want to impose an equality to cast over

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129737769):
Ok, I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129737772):
This might be a good way to go forward with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129738129):
What is the best way to prove that the intersection of two neighbourhoods is a neighbourhood?
```lean
Va ∩ Vb ∈ (nhds 0).sets
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129738131):
I guess this is already in mathlib somewhere, but I can't find it...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129738181):
It's a filter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129738191):
use `inter_mem_sets`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 16 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129738246):
Johan, what are you working on? I'd like to be sure we don't duplicate efforts.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129738353):
Trying to prove that power_bounded_subring is in fact a subring.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129738441):
You weren't doing something similar, were you?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 16 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129740202):
No, I'm working on completions of topological rings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129750955):
I have a continuous map `f`, a point `x` and a nhd `U` of `f x`. How do I prove that the inverse image of `U` under `f` is a nhd of `x`? That should be in mathlib already, I guess... but I can't find it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129750979):
Concretely, I have a top ring `R`, and a nhd `U` of `0 : R`. And I want to prove that `{u | -u \in U}` is also a nhd of `0`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 16 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129751036):
https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/topological_structures.lean#L52

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 16 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129751041):
This is exactly this lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 16 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129751043):
also why are we using `nhds` instead of `nbhd`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 16 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129751062):
the filter `nhds x` is the filter of all neighborhoods of `x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129751066):
The plural is because it is a filter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 16 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129751071):
`nbhds`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129751116):
I like four letters

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 16 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129751147):
it took me a while to get to the point where I could type `nhds` on the first try

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129751363):
Patrick, thanks. I somehow didn't see how to apply that lemma. I'll try again.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129751576):
Done! And thanks again.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 16 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129751740):
After that lemma, you can get to your statement with:
```lean
example : ∀ U ∈ (nhds (0:G)).sets, {x | -x ∈ U} ∈ (nhds (0:G)).sets :=
begin
  intros U U_in,
  rw ←nhds_zero_symm,
  rw mem_vmap_sets,
  existsi [U, U_in],
  intro x,
  simp
end
```
but maybe there is a shorter way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129751916):
I just copied part of the proof: `apply continuous.tendsto (topological_add_group.continuous_neg R) 0, simpa`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129754628):
Just posting this here to report on what I've tried so far: https://github.com/jcommelin/lean-perfectoid-spaces/blob/power_bounded/src/power_bounded.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129754641):
Nothing serious done yet...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 16 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129754690):
And off to catch a train :train:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 17 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129806596):
@**Kevin Buzzard** I proved that power bounded elements form a submonoid, containing 0 and closed under negation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 17 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129806652):
To prove that it is a ring we need extra conditions on the topology. (Powers of 2 are not bounded in `\R`.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 17 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129806657):
Do we need the fact that the power bounded elements form a subring? If so, in which generality?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 17 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129819314):
I am not 100% convinced that we need that they form a subring (but we definitely need the notion of the set of power-bounded elements). This [power bounded elements are a subring] might be one of those things which is natural to define but which it turns out that we don't logically need. I _do_ know for sure that the only topological rings we care about are Huber rings a.k.a. f-adic rings; these are topological rings $$A$$ which have an open subring $$A_0$$ and a finitely-generated ideal $$I$$ of $$A_0$$ such that the induced topology on $$A_0$$ is the $$I$$-adic one (see Def 6.1 Wedhorn, p46). In particular $$A$$ is non-archimedean (definition 5.23 of Huber) and and Wedhorn 5.30(3) is the result in this case. However for perfectoid spaces we only care about Tate rings (def 6.10 p48) and these rings have the property that there's some unit $$\pi$$ of $$A$$ such that $$\pi A_0$$ is an ideal of definition, i.e. you can assume $$I$$ is principal. In that case $$A=A_0[1/\pi]$$ and boundedness just says "I'm contained in $$\pi^{-n}A_0$$ for some $n$". Proofs are probably easier in this case.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 17 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129824275):
Ok, then I'll stop working on the power_bounded branch for a while.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 17 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129824315):
I had a couple of silly definitions (like ideal_of_definition, etc...) in a Huber_pair branch. I will take a look at those tomorrow, maybe I can turn that into something useful.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129856374):
@**Kevin Buzzard**  https://github.com/jcommelin/lean-perfectoid-spaces/blob/Huber_pair/src/adic_space.lean contains some definitions for Huber pairs. Do you think this is useful?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129856377):
I admit that it could use some tidying.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 18 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129860713):
So both Patrick and Johan have made me aware of files in their own forks of the perfectoid repo which they've asked for comments on. But I am miles away from this. I (or someone) really needs to understand all these comments made on 3rd July just before the big pause in this thread (which was to a large extent caused by the fact that I knew I'd need to find some time to understand them, and am only just finding this time). 

I now have

```lean
class is_valuation {α : Type*} [linear_ordered_comm_group α]
  {R : Type*} [comm_ring R] (f : R → option α) : Prop :=
(map_zero : f 0 = 0)
(map_one  : f 1 = 1)
(map_mul  : ∀ x y, f (x * y) = f x * f y)
(map_add  : ∀ x y, f (x + y) ≤ f x ∨ f (x + y) ≤ f y)
```

in the root namespace -- is that even right? Is that ever right for a niche notion like this? 

I have

```lean
structure valuation (R : Type*) [comm_ring R] (Γ : Type*) [linear_ordered_comm_group Γ] :=
(f : R → option Γ)
[Hf : is_valuation f]
```

-- is this supposed to go in the same namespace as `is_valuation` or it is supposed to be `is_valuation.valuation`? And am I right in thinking that there's no point putting the square brackets there? I have re-instated the coe to fun:

```lean
instance (R : Type*) [comm_ring R] (Γ : Type*) [HΓ : linear_ordered_comm_group Γ] :
has_coe_to_fun (valuation R Γ) := { F := λ _,R → option Γ, coe := λ v,v.f}
```

and in an attempt to use type class inference (which I have no idea whether I should be using or not) I have

```lean
instance {R : Type} [comm_ring R] {Γ : Type*} [linear_ordered_comm_group Γ]
(v : valuation R Γ) : is_valuation (v) := v.Hf 

attribute [instance] valuation.Hf
```

I am unclear about which one is right or whether I'm supposed to have both. 

I am now attempting to define the "equivalence classes" for an equivalence relation that I will never define even though mathematicians talk about it:

```lean
definition Spv (A : Type) [comm_ring A] : Type := 
  {ineq : A → A → Prop // ∃ (Γ : Type*) [linear_ordered_comm_group Γ] (v : valuation A Γ), ∀ r s : A, ineq r s ↔ v r ≤ v s}
```

and I discover that type class inference won't let me do this:

```lean 
failed to synthesize type class instance for
A : Type,
_inst_1 : comm_ring A,
ineq : A → A → Prop,
Γ : Type ?,
_inst_2 : linear_ordered_comm_group Γ
⊢ linear_ordered_comm_group Γ
```

The mathematical hold-up with the project is that I need to define what it means for an equivalence class to be a continuous (equivalence class of) valuation(s) so I can work on this, but the above is where I am with the infrastructure issue and as you can see I'm not there yet, and not 100% clear that what I've already done is OK.
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129860942):
```quote
in the root namespace -- is that even right? Is that ever right for a niche notion like this? 
```
Well, Wiki knows about 3 mathematical uses for `valuation`, so I don't think it is very niche. At some point we might need to move it into a namespace, but I don't think we need to worry about that now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861074):
And I keep getting confused why type class inference doesn't grab the instance from the local context. I really don't understand that behaviour. Because sometimes it does... and sometimes it doesn't (from my layman's POV).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861179):
Kevin, of course you can fix it by giving the instance a name, and then writing `@valuation _ _ _ foo _ _ A \Gamma` or something like that (didn't check the number of `_` that you need).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861356):
I'm not sure this is the universally agreed notion of "valuation" though. What's up with that last axiom?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861376):
Oh, wikipedia says you have the inequality backwards

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861427):
No?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861447):
> v(a + b) ≥ min(v(a), v(b))

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861454):
That is the additive version

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861463):
> `∀ x y, f (x + y) ≤ f x ∨ f (x + y) ≤ f y`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861464):
not the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861475):
They add infinity to an additive group. If you scroll down, you get the multiplicative version, with 0 added.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861526):
I guess at some point we will also have `is_add_valuation`...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861550):
Oh, so `(f : R → option α)` should be `(f : R → with_zero α)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 18 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861553):
Yes the notation is a nightmare. Our valuations should be called seminorms.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 18 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861557):
and yes, option alpha is alpha plus a bottom. option (positive reals) = non-negative reals in this context.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861601):
If you call it a seminorm, then I think you don't have to worry about naming conflicts at all (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 18 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861619):
Huber's decision to call it a valuation is very unfortunate.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861620):
I mention this because mathlib defines like 6 meanings for the none element of option depending on the name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861632):
`with_zero`, `with_bot`, `with_top`, `with_one`,...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 18 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861648):
Kenny wrote the code extending <= etc to option alpha before these things existed, I believe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 18 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861660):
and I had trouble using `with_top` recently; I posted a question about it but I don't think I got any responses.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 18 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861719):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset.20min.20on.20with_top

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 18 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129861722):
so I'm slightly scared of these things now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 18 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129862031):
```quote
Kevin, of course you can fix it by giving the instance a name, and then writing `@valuation _ _ _ foo _ _ A \Gamma` or something like that (didn't check the number of `_` that you need).
```
Now the problem moves to

```
failed to synthesize type class instance for
⊢ has_le (option Γ)
```

because if Gamma is known by type class inference to be a linear_ordered_comm_group then type class inference knows what the le is on option Gamma, but it doesn't.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 18 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129862044):
There's some weird way of making all this work with haveI or exactI or something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129862111):
put a `by exactI` in the middle

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129862118):
between the instance binder and the definition that uses it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 18 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129862135):
```lean
definition Spv (A : Type*) [comm_ring A] := 
{ineq : A → A → Prop // ∃ (Γ : Type*) [HΓ : linear_ordered_comm_group Γ] (v : @valuation A _ Γ HΓ), 
  by exactI ∀ r s : A, ineq r s ↔ v r ≤ v s}
```

Black magic!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 18 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129862214):
I keep meaning to write some docs on this -- I asked about 5 questions of this nature on the typeclass woes thread but then I didn't write up a coherent summary (I just starred a bunch of messages from Mario) and it still comes back to burn me because I can no longer remember anything which I don't use regularly so I need notes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 18 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129862222):
Thanks Mario.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129862312):
@**Mario Carneiro** Would it be possible to use `exactI` and avoid the explicit mention of `H\Gamma`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129862360):
yes, just move it earlier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129862363):
Also, is this something that Lean 4 will fix? So that Kevin's first attempt will just work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129862366):
```
definition Spv (A : Type*) [comm_ring A] :=
{ineq : A → A → Prop // ∃ (Γ : Type*) [HΓ : linear_ordered_comm_group Γ],
  by exactI ∃ (v : valuation A Γ) ∀ r s : A, ineq r s ↔ v r ≤ v s}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129862378):
~~No, you still have `H\Gamma`.~~ :thumbs_up:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129862438):
I have no idea if lean 4 will fix this. It was "broken on purpose" by leo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129867159):
Does it make sense to add `def is_unit (r : R) : Prop := ∃ r' : units R, r = r'.val`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129867166):
Or am I thinking to classical?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129867232):
For reference:
```lean
-- Scholze : "Recall that a topological ring R is Tate if it contains an
-- open and bounded subring R0 ⊂ R and a topologically nilpotent unit pi ∈ R; such elements are
-- called pseudo-uniformizers.

def topologically_nilpotent (r : R) : Prop :=
∀ U ∈ (nhds (0 :R)).sets, ∃ N : ℕ, ∀ n : ℕ, n > N → r^n ∈ U

def is_unit (r : R) : Prop := ∃ r' : units R, r = r'.val

definition is_pseudo_uniformizer (r : R) : Prop :=
topologically_nilpotent r ∧ is_unit r
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129867238):
I think there is a set for this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129867257):
oh, no, there is a set for `nonunits` though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129867304):
Ok, so should I make `units_set : set R`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 18 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129867323):
You could have `pseudo_uniformizer` be a property of `units R`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129867377):
Ok, that make sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 18 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129874533):
Ok, I finished the definition of pseudo-uniformisers and Tate rings. Nothing deep happening: https://github.com/jcommelin/lean-perfectoid-spaces/blob/Huber_pair/src/adic_space.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 18 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129887843):
I have not looked at either Johan's or Patrick's commits. I've been concerned today with trying to get valuations right, following the discussion on July 3rd. @**Sebastien Gouezel** I now understand what you are saying. I now have

```lean
structure valuation (R : Type*) [comm_ring R] (Γ : Type*) [linear_ordered_comm_group Γ] :=
(f : R → option Γ)
(map_zero : f 0 = 0)
(map_one  : f 1 = 1)
(map_mul  : ∀ x y, f (x * y) = f x * f y)
(map_add  : ∀ x y, f (x + y) ≤ f x ∨ f (x + y) ≤ f y)
```

and a coercion to fun. I refactored a bunch of Kenny's code today. We now finally have a `valuation` namespace instead of an `is_valuation` one. 

One technical question I now have @**Mario Carneiro**  : I have now decided to give up on making everything in `Type`, so I have to choose whether to make `R` and `Gamma` live in the same universe `u` or let one be in `u` and the other be in `v`. There was a subtlety in the Jul 3 comments I didn't understand with `Spv` : my definition of `Spv` is now

```lean
definition Spv (R : Type u) [comm_ring R] := 
{ineq : R → R → Prop // ∃ (Γ : Type u) [linear_ordered_comm_group Γ],
  by exactI ∃ (v : valuation R Γ), ∀ r s : R, ineq r s ↔ v r ≤ v s}
``` 

with my two types in the same universe. Do the same ideas (which I don't understand) apply to `valuation`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 19 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129924606):
OK so I have refactored valuations. The valuation spectrum now uses the "ZFC" approach -- instead of it being "equivalence classes" on an "equivalence relation" defined on a class, it's a concrete thing (preorders with some property). I have the correct definition of continuous, the main fundamental theorem about them is sorried (being continuous is constant on equivalence classes), I have a topology on the type of all valuations, and we can put the subspace topology on the continuous valuations. Although I haven't looked at Johan's work yet I am hoping that it will let us easily define Spa(R) for R a Huber pair (it's just continuous valuations which are bounded by 1 on R^+). Although I haven't looked at Patrick's work yet I am hoping that it will easily let us put a presheaf on some "basic" open sets in Spa(R) [we need to localise and then complete; Kenny has localised and Patrick is completing]. Then we extend from a basis to the whole space using some limit procedure. That's it. This sorried theorem about continuous valuations is what I will work on next. I can see my way to the end of this now, but my experience with schemes was that there were some things which were far harder to formalise in practice than I had imagined.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 19 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129926038):
I had no time for Lean yesterday and this morning, but I hope to move on during this afternoon

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 19 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129934215):
On 3rd July Mario said
```quote
If you want to be polymorphic, I suggest writing
```lean
 def zfc.Spv (R : Type u) [comm_ring R] : Type :=
{ineq : R → R → Prop // ∃ (Γ : Type u) [linear_ordered_comm_group Γ]
  (v : valuation R Γ), ∀ r s : R, ineq r s ↔ v r ≤ v s}
```
where the valuation and ring have to share the same universe
```
I don't understand why these two universes need to be the same. It seems to directly contradict the advice to be as polymorphic as possible. It's a *theorem* (I think!) that if there exists Gamma of type v such that blah, then there exists Gamma of type u such that blah. The proof (in maths) is "I only care about the subgroup of Gamma generated by the image of v, which is a function from R to Gamma". So why don't we do it this way -- with a definition which allows two universes and then a theorem remarking that we could get away with one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129934289):
because then the definition will have an "internal universe variable", and these are always unpleasant to work with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129934310):
you will have to write stuff like `zfc.Spv.{u v}` all the time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129934363):
the advice is to be polymorphic in your inputs, and monomorphic in your outputs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 19 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/129934395):
since the valuation or commutative group are not inputs (arguments to the function), they should not involve additional universe variables

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130068343):
Over 200 lines of code later...

```lean
definition Spv (R : Type u) [comm_ring R] := 
{ineq : R → R → Prop // ∃ (Γ : Type u) [linear_ordered_comm_group Γ],
  by exactI ∃ (v : valuation R Γ), ∀ r s : R, ineq r s ↔ v r ≤ v s}
```

[note both in universe u]

and its universe-polymorphic constructor

```lean
definition Spv.mk {R : Type u1} [comm_ring R] [decidable_eq R] {Γ2 : Type u2} [linear_ordered_comm_group Γ2]
(v : valuation R Γ2) : Spv R := quot.mk v.f
```

[note `R` and `Γ2` in different universes]. I hope I understood correctly what you said I should do @**Mario Carneiro**  because it's taken hours! I had to prove the universal property for quotient groups! And define quotient abelian groups! I'm trying to be a good student (and avoid Patrick's universe hell). 

I needed decidable equality for `R` (which ironically will never be true, `R` is always something like a power series ring over the p-adic numbers) for some intermediate `finsupp` calculation involving the free abelian group on `R` (Thanks @**Reid Barton** ).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130068396):
Now to finally get onto what I was supposed to be doing yesterday, which was defining continuous valuations...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130068405):
Hopefully you now also have that "canonical valuation" you mentioned

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130068434):
Yes I guess I do.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130068461):
Actually, that's a very pertinent comment because it was the fact that I'd not constructed the canonical valuation which was stopping me from defining continuity -- the equiv class is continuous iff the canonical valuation is continuous.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130068472):
I was initially going to do it another way but perhaps I can dodge that now (and run into trouble later on ;-) )

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130068531):
I had to use the first isomorphism theorem to move my universe. Kind of funny. Basically an elaborate version of the following observation: if `G` and `H` are groups in different universes with a map `f `between them, then `G/ker(f)` and `im(f)` are isomorphic, but the latter is in `G`'s universe and the former in `H`'s.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 21 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130068571):
yep, that's the idea

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 21 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130068577):
except I had to do it with totally ordered commutative monoids

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 22 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130075632):
Oh dear there is so much basic stuff about group closures which is not there. Or is it there? Here's what I think I need:

```lean
import group_theory.coset 
-- and hence group_theory.subgroup -- note this only arrived in mathlib a few weeks ago

-- for images
import data.set.basic

-- finsupp for free abelian groups
import data.finsupp 

universes u v 

variables (G : Type u) [group G] (H : Type v) [group H] (S : set G)

-- maybe use group.in_closure?
theorem closure_image (f : G → H) [is_group_hom f] : 
f '' (group.closure (is_group_hom.ker f) ∪ S) = group.closure (f '' S) := sorry 

-- don't know why we need decidable equality -- maybe some finsupp reason
example (X : Type u) [decidable_eq X] : add_comm_group (X →₀ ℤ) := by apply_instance

definition group.free_ab_gens (X : Type u) [decidable_eq X] : 
X → (X →₀ ℤ) := λ x, finsupp.single x (1 : ℤ)

-- do we have to copy out all of the definitions here?
definition group.add_closure {G : Type u} [add_group G] (S : set G) : set G := sorry 

-- maybe use finsupp.induction?
theorem closure_free_gens (X : Type u) [decidable_eq X] : 
group.add_closure ((group.free_ab_gens X) '' set.univ) = set.univ := sorry 

```

I have to go to bed now and I'm not sure I have time for Lean tomorrow. This is the current hold-up for defining continuous valuations and hence the topological space `Spa R` associated to a Huber pair.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 22 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130075906):
I did quotient groups: https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/quotient_group.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 22 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130075911):
or at least the stuff I needed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 22 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130090336):
Did you use `elan toolchain link` to create that `master` version you indicated in the `leanpkg.toml`? Is it a link to `nightly-2018-06-21`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 22 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130091434):
I didn't really know what I was doing. I had `lean_version = "3.4.1"` there before, I just changed it manually because I updated my Lean ( knew that `group_theory/coset.lean` had changed relatively recently and I wanted to be 100% sure I had the correct version because I was thinking of PR-ing my write-up of basic properties of quotient groups). If `lean_version` is set to `3.4.1` then I think `leanpkg upgrade` upgrades to a now-fixed version of mathlib, which is *perfect* for me and my students, but might not be so ideal for a project which is nearer to the boundaries of mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 22 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130091435):
Feel free to change it back

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 22 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130092071):
I created the `master` link at home and was able to proceed. See also https://github.com/kbuzzard/lean-perfectoid-spaces/pull/6

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130246268):
OK so I have a topological space `Cont R`. I am not sure how usable it will be because some key lemmas about valuations remain unproved.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130246618):
Next step is Spa(R) for R a Huber pair. This is easy, except for all the missing things which I've lost track of. `is_integral` is not defined in `for_mathlib/subring.lean` -- @**Johan Commelin** is this now easy now we have polynomials?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 25 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130257814):
```quote
Next step is Spa(R) for R a Huber pair. This is easy, except for all the missing things which I've lost track of. `is_integral` is not defined in `for_mathlib/subring.lean` -- @**Johan Commelin** is this now easy now we have polynomials?
```
Right. This shouldn't be hard to do now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 25 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130258076):
I haven't updated my local copy of the perfectoid project yet (and rebuilds are slow....). But I guess you can just uncomment those lines in `subring.lean`. Everything looks fine to my eyeball-parse.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130258256):
Yesterday Kevin complained we don't have fraction fields. Johan, isn't it something you could rather easily do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 25 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130258285):
@**Kevin Buzzard** Fraction fields are already in mathlib, in the localization file. (`kenny` is a wonderful tactic!)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 25 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130258345):
I quote from the bottom of that file:
```lean
def quotient_ring.field.of_integral_domain : field (quotient_ring β) := implementation_follows...
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130258367):
Well done Johan! That's efficient.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130258416):
I'm a bit confused by terminology. Is `quotient_ring` the localization with respect to non-zero elements?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130258421):
The name seems a bit too general.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 25 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130258567):
```lean
def quotient_ring := loc α (non_zero_divisors α)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130262120):
Yes there are definitions but it's the API that's always missing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130262638):
That's how Kevin speaks nowadays :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 25 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130262856):
```quote
Yes there are definitions but it's the API that's always missing.
```
Is Kevin turning into a CS person? It wasn't too long ago he was asking what an “interface” was, and now he's throwing around terms like “API” as if they were second nature.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130263113):
For example there was a definition of quotient group -- but nothing else; I needed that if f:G->H and g:G->K and ker(f) was a subset of ker(g) then there was some induced map etc etc, I needed facts about kernels for additive groups and everything was set up for multiplicative groups etc. I've now managed to understand this whole API business. I want my maths students to be able to write maths! In some sense I want their Lean code to look the same as the maths they write on paper, so when I start on formalizing example sheet questions I will take all the "obvious" things like 2x=x+x and prove them myself and tell the students what these functions are called (I'll put them all in a xena library and tell them to import it) so they can have the feeling of formalization without having to get bogged down in all the details like I got bogged down when I was solving my own problem sheets last Oct.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 25 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130263141):
@**Kevin Buzzard** the quotient group lemmas are in [my local langlands project](https://github.com/kckennylau/local-langlands-abelian/blob/master/src/quotient_group.lean)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130263150):
This is also something I will have to do for my classes next spring. I plan to prepare specialized files to import for each session.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130263164):
```quote
@**Kevin Buzzard** the quotient group lemmas are in [my local langlands project](https://github.com/kckennylau/local-langlands-abelian/blob/master/src/quotient_group.lean)
```
We really really need more mathlib PR

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130303814):
```quote
Next step is Spa(R) for R a Huber pair. This is easy, except for all the missing things which I've lost track of. `is_integral` is not defined in `for_mathlib/subring.lean` -- @**Johan Commelin** is this now easy now we have polynomials?
```
OK I've got a definition of `is_integrally_closed`. Just pushing now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130303911):
PS @**Patrick Massot** we really do need Lean "master" now, or at least mathlib beyond 3.4.1, because I'm using Chris' recent monster polynomial PR (which has been accepted).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130303980):
I don't see the link between Lean master and "mathlib beyond 3.4.1"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130304598):
I think that before it said `lean_version = "3.4.1"` and Mario, either intentionally or by accident, has created a branch of mathlib called 3.4.1 and has stopped updating it, which is great for my students because we can all stay on the same version and code that one of them works for another one (they are all running the same version of Lean and mathlib), but is not so great if we want bleeding edge stuff, which we do want here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130304668):
Oh -- perhaps you're saying that the reason the behaviour has changed for me is not because I've changed `lean_version` but because I've changed which version of lean i'm actually running?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130304676):
mathlib version has nothing to do with Lean version, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130304698):
All I know is that when my students type `leanpkg upgrade` they all upgrade to the same version regardless of when they type it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 25 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130304706):
which is good because new ones arrive (e.g. we've got two new students this week)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130304781):
Anyway, how did you get that `master` toolchain for `elan`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 26 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130305339):
I just edited the .toml file. I've never used elan. I think I should start -- I now have a situation where I genuinely want to use different versions of Lean for different projects.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 26 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130305402):
Oh, so maybe that's why it doesn't work the same here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 26 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130306015):
Why don't you merge https://github.com/kbuzzard/lean-perfectoid-spaces/pull/7?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 27 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130375846):
Thanks to crucial help from Johannes, I was able to unlock ["completions of products are products of completions" ](https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L226). With some more effort and much help from the `change` tactic I also proved the [lifting property](https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L238) of this isomorphism (basically it does what it should to elements present before completion). Then I made a huge push and unsorried https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/topological_structures.lean#L261. It means that every topological abelian group G now has a Hausdorff completion which is an abelian group, and the map from G to its completion is a group morphism. Next step is to prove some more properties and push to rings.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 27 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130391508):
So I have a topological space Spa(R,R+) [in the sense that I have an unsorried definition in Lean, where (R,R+) is a Huber pair), and I want to put a sheaf on it. Its global sections are the completion of R; R is a commutative topological ring and, thought of as an abelian group, a basis of neighbourhoods of zero for the topology is induced by a (countable, if this matters) decreasing family of subgroups. More generally its sections on some appropriate opens are completions of other such rings. If I have the sections on the appropriate opens I can get the sheaf on all opens by some direct limit procedure, and then we have affinoid pre-adic spaces. The hard work in schemes was then to prove that this presheaf was a sheaf -- but this is not true in this generality, because completeness is quite a poorly-behaved functor when it comes to algebraic properties (unlike localisation it doesn't preserve exactness), so an affinoid adic space is simply *defined* to be a preadic space for which the presheaf is a sheaf. An adic space is something glued from affinoid adic spaces, and a perfectoid space is an adic space glued from affinoids built from (R,R+) which are perfectoid rings. The end is in sight!

So given a topological ring with the topology defined by a collection of additive subgroups, how do I complete it? Will you push to my repo?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 27 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130395480):
Of course I will PR to your repo. I can do it now if you want but, as explained yesterday, there is still work to be done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 27 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130402876):
I worked a bit this morning, but I'm stuck in type class inference hell, and it's lunch time. See https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/topological_structures.lean#L366

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 27 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130402893):
This instance should be a trvial consequence of the previous one, but suddenly Lean doesn't find the relevant intermediate type classes instances.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 27 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130402954):
But I do have the universal mapping property of completions of abelian topological groups modulo https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/topological_structures.lean#L200 claiming that continuity of group morphisms implies uniform continuity (there I'm not stuck, I haven't found time to try yet)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 27 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130408236):
I'm done with uniform continuity to continuous (abelian) group morphisms. But I'd be really grateful if someone can sort out the type class inference hell at the end of https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/topological_structures.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 27 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130408302):
I'm afraid I can't minimize this, it's precisely the complexity of type classes that triggers the issue. But feel free to clone and fix, I need to go back to real world for a while.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 27 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130417136):
Johannes explained the source of my trouble. I have an interesting diamond here. I have an instance saying that every abelian topological group is a uniform space. Another one says every completion of a uniform space is a uniform space. And the last one says the completion of an abelian topological group is an abelian topological group. Question: what is the uniform space structure on the completion of an abelian topological group? The completion one or the group one?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130419183):
Are they (non-definitionally) equal? Presumably! Maybe use some cool priority trick ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 27 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130426702):
Of course there are equal, `by otherwise_we_would_know_it`. But there certainly not definitionally equal. I'll see if I can get around that. But my family will return from vacation in a couple of minutes, so I may slow down a bit on the Lean side (I was alone at home for the past two weeks).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 28 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130438821):
You should prove a theorem that the two instances are equal and add it to the type class inference system in some way that's presumably impossible. You should decide which instance you prefer and give it a higher priority. Let the system carry around both proofs and if your favourite one doesn't pan out then we can try the other one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 28 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130465792):
OK so the perfectoid library currently compiles, with some sorries, and I want to spend some time today trying to figure out what we need to do next. I'd be happy to accept WIP PR's as long as they compile (sorrys are fine). Johan did PR something but I screwed up the merge and just rewrote history so it never happened.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 28 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130466055):
I feel like a bunch of things need refactoring but I'm worried I'll screw up everyone's forks if I start moving stuff around.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 28 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130466968):
@**Patrick Massot** @**Johan Commelin** Currently `adic_space.lean` is just a dumping ground for everything which hasn't got a proper file to live in. We need a file `Spa.lean` containing the definition of Spa of a Huber pair, and perhaps a file `Huber_pair.lean` containing basic definitions of Huber rings, Huber pairs and things like bounded subsets and power-bounded elements. If I make all this refactoring before I accept your PRs then you will both have messes to tidy up, right? Currently all these definitions are in `adic_space.lean`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 28 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130484907):
No problem with me. All my work is in files independant from `adic_space.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 28 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130484954):
I'm also fine with this. If I have any mess to tidy up, it won't be too huge.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 31 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130607206):
https://github.com/kbuzzard/lean-perfectoid-spaces/pull/10

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 31 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130638624):
https://mathoverflow.net/questions/65729/what-are-perfectoid-spaces#307239

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 05 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130936504):
Patrick -- somewhere you asked how close we were to actually finishing this project. I'm on holiday at the minute so I have time for this sort of thing (I implored my xena students to bother me with questions but of course inevitably things are less busy than when I'm spending about 20 hours a week in the same room as them). I tried to just finish the job, as it were, and the main thing that is left now is the definition of the presheaf on Spa(A). This is a multi-stage process. The first stage is to locate some "nice" open sets (analogous to the basic open sets D(f) in Spec(A)) and to define the presheaf on these. To do that we need to show that the completion of a topological commutative ring is a topological commutative ring. To define the restriction maps we'll need some commutative algebra, which I had a superficial look at and decided it shouldn't be too bad, plus the universal property of completions (we will have a ring map B -> C and we'll want to extend it to B-hat -> C-hat). This gives the presheaf defined on these nice open sets. We then want to extend to all open sets via some limit procedure and this should hopefully be easy. Then that's pretty much it, as far as the definition goes. Thanks a lot for your work on completions. I now feel like I know enough about uniform spaces to understand what is going on in these files -- I spent the last 24 hours or so trying to understand all this basic maths that's in Lean which I was never taught and of course now I've done it I just realise that I should have done it much earlier instead of whingeing about how I didn't understand all this uniform stuff.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 05 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130942351):
Thanks Kevin. I'm still slowly working on completions when  I'm not at the beach. There are a couple of things I need to figure out, on the mathematical side, and then explain to Lean. But you can easily sorry the desired properties and keep going.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 05 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130942514):
Of course I agree we should have learned about filters and uniform spaces earlier this year. Now I'm getting used to them. Of course knowing how to translate everything back to sets and topology is only the beginning. Unwrapping all definitions before doing anything else only brings chaos. You really need to use all those lemmas about direct and inverse image of filters. For instance, the proof I'm trying to wrap up right now begins with 
```lean 
 rw uniformity_eq_vmap_nhds_zero,
 rw prod_map_map_eq,
 rw ←map_le_iff_le_vmap,
 rw filter.map_map,
 rw prod_vmap_vmap_eq,```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 05 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130942560):
I keep it that way instead of one `rw` because I still want to be able to see what each of them does

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 05 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130942652):
You can still see what each one does if you put them in a `[ , , ]` list

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 05 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130942656):
Really?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Aug 05 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130942666):
In emacs at least

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 05 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130942716):
Indeed!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 05 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130942717):
Thanks for the tip!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 05 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130945352):
It's just more of a pain because you have to do more precise clicking rather than just moving the cursor up and down :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 06 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130945458):
regarding multiple rewrites and unfolding -- yes, I learnt from working with multisets that random unfolding is often not the right thing to do :-) But Johannes [and sometimes Mario] wrote all this stuff and I am now beginning to appreciate the art of it all; it would not surprise me if everything were there, once you have got the hang of how to think about these things...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 06 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130945670):
I don't know what you mean by "it would not surprise me if everything were there" but I can tell you that there were nothing about  uniform structures on  topological groups, and that's quite a bit of maths

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 06 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/130945713):
Oh!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 08 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131134402):
Uniform continuity is overrated. Remember you can build the completion of a commutative topological group by extending the addition by continuity. The result is continuous because addition is uniformly continuous. When going for rings, things are more complicated because multiplication is not uniformly continuous (even on real numbers). But uniform continuity is an overly expensive way to assume that Cauchy filters go to Cauchy filters. And bilinearity is enough to ensure this, as explained in https://github.com/kbuzzard/lean-perfectoid-spaces/pull/11/files#diff-83f5ebe2bcf6329ac3366ea2deb7848dR70

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 08 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131134458):
This is by far the most subtle theorem I ever explained to Lean, and the proof is about 170 lines long. Actually this is typically the kind of subtle proof where I love that Lean can tell me I didn't miss anything, although I would prefer if formalizing this proof were easier.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 08 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131134525):
I haven't yet applied this theorem to the case of multiplication, but it should immediately imply extension to the Cauchy filter space. Then I'll need to see what happens to the separation relation (Bourbaki first gets rid of the separation issue and then completes, so things are a bit different).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 08 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131134640):
I did prove that, before Cauchyfication, the separation relation is `x - y ∈ closure ({0} : set G)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 08 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131134696):
Kevin, I'd be very interested to know if you can read this big proof of extension of bilinear stuff. It's clearly not in the category "this is trivial hence the proof must be obfuscated".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 08 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131134769):
I think `neg_left` follows from `add_left`, right? A Z-linear map between abelian groups just satisfies f(x+y)=f(x)+f(y) and you can deduce everything else from that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 08 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131134791):
I wrote that part *very* quickly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131135055):
You proved Z-bilinear maps on dense subgroups extend uniquely. Presumably also Z-linear maps on dense subgroups extend uniquely. Can you deduce the bilinear case from the linear case? If not, then will we need some trilinear version some day?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 09 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131135125):
Bourbaki states it that way, presumably this generality is good enough for a number of things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131135326):
It's hard to read. I mean, it's not impossible, because I can see what every line does, but I look at it and I think "I'd rather be reading GT for sure". I certainly didn't get to the end of it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131135371):
Too many filters :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 09 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131135395):
Don't forget that most filter-fu is hidden in the lemma I posted here yesterday https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/continuity.lean#L82

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 09 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131135405):
which has been taken out of the main proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131135410):
And I see what you mean about all those instances! What can you do about that? 

```
_inst_12 : topological_space A,
_inst_13 : add_comm_group A,
_inst_14 : topological_add_group A,
```

because of the way the typeclasses work, and you have five of these, so you've already just lost 15 lines the output window.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 09 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131135476):
and I was even worse in the beginning, because I followed Bourbaki and assumed E and F were complete Hausdorff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 09 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131135504):
Btw this is a great use of Lean: I proved the theorem but thought those hypotheses were useless. Then I removed the hypotheses and Lean was still happy.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 09 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131135519):
No need to go through the proof to triple check I wasn't implicitly using them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 09 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131135586):
Now I try to apply this lemma to `A` inside `Cauchy A` and get into class resolution hell. It's time to go to bed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131135596):
I know exactly what you mean about the satisfaction of going through this sort of a proof and at the end knowing *for sure* that you've dotted all the i's and crossed all the t's -- I mean, maybe not 100% sure, but I'm not even sure I operate at 99% accuracy with pencil and paper whereas I feel like I'm operating at 99.999% accuracy here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 09 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131135615):
```quote
It's hard to read. I mean, it's not impossible, because I can see what every line does, but I look at it and I think "I'd rather be reading GT for sure". I certainly didn't get to the end of it.
```
You should read GT, but really it took me Lean to understand it's much more subtle that I originally thought.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131135781):
```lean
    have : (δ ∘ λ (p : (A × B) × A × B), (φ p.1, φ p.2)) = (λ (p : (A × B) × (A × B)), φ p.2 - φ p.1)
      := rfl,
    rw this, clear this,
```

You know you can do stuff like `rw (show blah, from refl)`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131135859):
You seem to be saying that the proof is *not* "just follow your nose". Even that I find interesting -- if you'd asked me to guess beforehand, I would have suggested that it's just one of those proofs where anyone could work it out given enough paper and time by just heading slowly and surely towards the goal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 09 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131135992):
There are epsilon/4's :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 09 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131136011):
Would have you guessed the role of https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/complete_groups.lean#L206?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 09 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131136023):
I'm not saying this is super difficult or deep. But this is far beyond anything I wrote in Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 09 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131136094):
This epsilon/4 is exactly the key formula trick

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 09 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131136104):
But all the subtlety comes from constantly going back and forth between the dense subgroups and the ambient groups

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 09 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131136155):
using limits in the subgroup for the filter induced from the neighborhood filter of a point *not* in the subgroup

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 09 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131136174):
Now I'll sleep.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 10 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/131220048):
By the way, https://mathoverflow.net/questions/65729/what-are-perfectoid-spaces#307239 is now  the second answer, with 27 upvotes!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 30 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133069116):
https://github.com/kbuzzard/lean-perfectoid-spaces/pull/15

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 30 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133069232):
Posting on Zulip is a much better strategy for letting me know about PR's :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 30 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133069237):
Oh, maybe I know how to fix this -- I have to follow my own repo or something.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 02 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133210528):
Thanks for the PR's Johan and Patrick. I'm going to spend some time today seeing what compiles and what doesn't. After our conversation last Tues I'm tempted to start sorrying theorems we need if they properly belong in "standard Masters level commutative algebra" (whatever that means) and see what actually needs doing. I had planned on doing this sort of thing in Paris but in practice I spent Monday and Tuesday evening doing admin :-(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 02 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133212852):
The units of a ring $$R$$ are traditionally denoted $$R^\times$$ or $$R^*$$ (I prefer the former). Is there a unicode "small cross" character which we can use as postfix notation, like the power-bounded subring notation $$R^\circ$$ which we already are using?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 02 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133213085):
@**Patrick Massot** In `for_mathlib/quotient_group.lean` there is `local attribute [instance] left_rel normal_subgroup.to_is_subgroup` and I have `unknown declaration 'left_rel'`. Do you know what this is?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 02 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133213087):
On the next line I have `unknown identifier 'left_cosets'` -- @**Chris Hughes** is this called something else now? I have the current mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 02 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133213743):
`left_rel` seems to be still here: https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 02 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133213795):
it's `quotient_group.left_rel` now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 02 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133214046):
about units, at worse we could use https://github.com/leanprover/vscode-lean/blob/master/translations.json#L1698

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 02 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133214243):
kenny is that a no?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 02 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133214343):
no, that's the unit symbol that he proposed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 02 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133224672):
@**Patrick Massot** am I doing something wrong? Many files in `for_mathlib` in the perfectoid repo now clash with files in mathlib. This is presumably because things got merged. But because I don't know exactly what is merged and what isn't, I am not entirely sure what I am doing. For example there is a file `for_mathlib/quotient_group.lean` which is apparently copyright you and me, and then there is also a file in mathlib called `group_theory/quotient_group.lean` which is also apparently copyright you and me, looks quite different (they seem to share a function `lift_mk` but  not too much else...). Am I now supposed to delete `for_mathlib/quotient_group.lean` and change all the imports in all the other files? I am fine doing this, I just wanted to check I'm not doing something stupid. I know there are plenty of sorrys in the project it but when I try to build it I currently get plenty of errors too.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 02 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133224733):
> looks quite different

This is usually the way these things go. It's been rewritten two or three times by now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 02 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133224745):
Now that it is merged, your job is to adjust your repo to the changes. If there are any difficulties that arise, ask, since there may be a trick, or the mathlib version may need more adjustment given your needs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 02 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133224844):
One of the invariants I try to maintain in mathlib changes is that anything you can do in a previous version of mathlib or using a PR that was merged but modified to unrecognizability, should still be possible and at most epsilon harder (ideally it should be either much easier or about the same)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 02 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133224974):
Thanks for the explanations. This didn't happen so much with the schemes project because we just filled up `for_mathlib` on the whole. Anything that got PR'ed was done by Kenny and Kenny dealt with these issues when they arose.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 02 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133226760):
I'm sorry, I did some cleanup related to mathlib update, but I didn't finish the job. I got distracted by the issue is the ramified condition, hence couldn't go all the way to make it compile again. Is it ok now?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 02 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133228903):
It's better than it was. I see what needs to be done but have not had the time to do it yet. I feel like there's such momentum with the Noetherian stuff that I want to do some more of that. Kenny pointed out a proof of integral closure being a subring which didn't need Noetherian hypotheses and went via some lemma in Atiyah--Macdonald, but this one needs Cayley-Hamilton which we don't have either. I'm sure I saw a write-up by someone (Gonthier?) explaining how this was done in Coq -- or am I confusing this with det(AB)=det(A)det(B)? Is it in the big operators paper?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 02 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133228954):
```quote
Is it in the big operators paper?
```
Yes, looks like it's in [section 6.2](https://hal.inria.fr/inria-00331193/document).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 02 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133229011):
Thanks. @**Chris Hughes** how far are we from this? @**Kenny Lau** are you interested in doing it? I am going to push on with the Noetherian proof even though it needs Hilbert basis, because Noetherian stuff is so important in general that it should be in mathlib. 

It's worth remarking that algebra is coming on in leaps and bounds (encroaching on Masters level stuff, and there's all this Zariski topology stuff in the schemes repo too), and we still don't have the definition of exp(x) or the derivative of a differentiable function.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 02 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133229054):
Keji proved it. I might sort it out, but there's a lot of lean things I have going on to finish off.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 02 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133229106):
I know Keji did det(AB)=det(A)det(B) -- he did C-H too?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 02 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133229107):
Kenny might do a really good job of making it all mathlib-ready -- he likes to have other people planning the code out first :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 02 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133229116):
He didn't do Cayley Hamilton

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 02 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133229160):
It's pretty much the next thing in the paper after det(AB)=det(A)det(B) :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 03 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133230907):
@**Kevin Buzzard**, perhaps "read-the-effing-repository" is the answer, but in your schemes project did you construct any examples? e.g. just a topological space as Spec C(X)? I'm trying to set up filtered colimits in such a way that it's actually possible to describe the stalk of a sheaf in practice, and not enjoying it. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 03 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133231085):
No, we are proud to be example free. But if you give me a commutative ring then I can give you an affine scheme plus proof it's a scheme so in some sense we have examples

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 03 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133231523):
Out of curiosity, what would e.g. Spec $$\mathbf{C}[x]/(x^2)$$ look like in lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 03 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133248288):
It looks like a topological space with a sheaf of rings, like every other scheme. I'm not sure I understand the question :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 03 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133248503):
it looks like a point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133248552):
Also in Lean? :stuck_out_tongue_wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 03 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133248558):
it looks like a bunch of code in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133248562):
Is there a `looks_like` predicate?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133248643):
```lean
def k_epsilon (k :Type) [field k] := Spec (ring.quotient (span (X*X) : set(polynomial k) ))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133248645):
Something like that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 03 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133255737):
Sorry for the vague question, I was curious what the code defining it would look like.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 03 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133255800):
I have a function `Spec` from commutative rings to schemes which works for any commutative ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 03 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133255851):
I guess that's not entirely true. Spec goes from commutative rings to types

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 03 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133268730):
Huge cleanup in https://github.com/kbuzzard/lean-perfectoid-spaces/pull/16

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 03 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133268738):
We are compiling against current mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 03 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133268801):
@**Johan Commelin** I had to sorry away your `is_integral` definition which needs fixing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133268808):
Ok, but that shouldn't be hard.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 03 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133268827):
it's currently in Huber_pair since for_mathlib/subring was blasted

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 03 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133268884):
`valuation_spectrum.lean` length was almost divided by two

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133268889):
In a couple of days it can move to `integral_closure.lean` in mathlib... if the noetherian momentum keeps going.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 03 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133268898):
that's partly why I didn't care too much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 03 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133269462):
For integral closure the main thing we need now is Hilbert basis, which should be really nice to prove. Then the quotient thing should give that rings finitely-generated over a Noetherian ring are finitely-generated, and then we have one of the two proper maths proof of integral closure done. I might just try Hilbert basis now; I haven't written any Lean code for ages, it's really nice to be able to get back to it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 03 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133269465):
Patrick -- many thanks for fixing up the repo.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133270365):
So, to get the `is_integral` stuff working we will need some form of `polynomial.map` or `eval\2`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133270403):
I currently don't have much time for Lean, alas...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133270410):
But I think it is best if the `eval\2` from `mv_polynomial` gets a little brother for univariate polynomials.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133270411):
This might be a nice project to experiment with transfer rules.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 03 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133270418):
(Unless this has malign computational ramifications; about which I know no-thing.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 03 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133275596):
Kevin, you should carefully review the new [valuation_spectrum.lean](https://github.com/kbuzzard/lean-perfectoid-spaces/blob/702f50b9bb1951626a10cb5098415c002f719c35/src/valuation_spectrum.lean). I tried to write something equivalent to what was there, but I didn't try to make sure I understood the math

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 04 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133287065):
@**Kevin Buzzard**, @**Patrick Massot**, @**Johan Commelin**, @**Reid Barton**, I wrote a draft of a roadmap for getting a simple example of an affine scheme into `mathlib`.

It's at https://github.com/semorrison/lean-category-theory/blob/master/schemes_roadmap.md

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 04 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133287069):
I suspect some things on the list already exist, and I would love to have pointers to these.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 04 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133287115):
Perhaps @**Kenny Lau** can PR (co)products of (commutative) (topological) rings into mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 04 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133287116):
and/or filtered (or just direct) colimits of (commutative) (topological) rings?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 04 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133287172):
A while ago I tried proving that the forgetful functor `CommRing ⥤ Type u` is represented by `ℤ[x]` (i.e. this just says that ring homomorphisms `ℤ[x] ⟶ R` are the same as elements of `R`), but got frustrated dealing with polynomials. I think we now have much better polynomials, and perhaps I can tempt someone who has worked with them into showing this fact. (@**Chris Hughes**?).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 04 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133287174):
It's not strictly necessary for the shortest path on the roadmap, however.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133291784):
```quote
A while ago I tried proving that the forgetful functor `CommRing ⥤ Type u` is represented by `ℤ[x]` (i.e. this just says that ring homomorphisms `ℤ[x] ⟶ R` are the same as elements of `R`), but got frustrated dealing with polynomials. I think we now have much better polynomials, and perhaps I can tempt someone who has worked with them into showing this fact. (@**Chris Hughes**?).
```
I actually proved that A[X] is the universal A-algebra... in my langlands repo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133291789):
but it's actually easy to prove

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 04 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133294149):
Could you PR it in usable form?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133294245):
maybe ignore my comment about langlands repo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133295147):
I was lazy with locally ringed spaces. I knew that it was a theorem (in real life, not in mathlib) that Spec(R) was a locally ringed space, so any ringed space which was covered by affine schemes had to be locally ringed, it seemed to me. So I skipped the definition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 04 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133295150):
https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_space.lean#L944

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 04 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133295166):
this is on the list

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 04 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133295172):
We should probably start a new thread if you want to discuss this list, this is not directly about the perfectoid project

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 04 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133297866):
@**Scott Morrison** That's a really nice list! But I agree it might be better to discuss this in a new thread.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133299021):
I think we should build monoid rings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133299022):
and then make mv_polynomial a special case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133299199):
I think monoid rings are a great idea. I have group cohomology on my todo list -- I think it would be really nice to do in Lean, even though I don't have the time to take it on right now. Monoid and group rings are the start of this. Then some nonsense commutative algebra about ext and tor which would be probably quite fun to do in Lean, and if it turns out not to be fun then this is Lean's fault and might give us more of a concrete goal for `transportable` -- my impression of this is that something non-trivial got written by @**Simon Hudon** and homological algebra would be a nice testing ground for getting a baby strategy working. Then things like group cohomology would be a really nice application.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 04 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133299417):
I did write something non-trivial, you're right. Then @**Johannes Hölzl** cast doubt to its usefulness because he already implemented `transfer` which I still have to look into.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133299675):
Simon this is a few months away at least. The only reason I mentioned it was that when trying to apply a general result about some abelian groups in a situation where I had isomorphic groups, it was tough (hence my moaning last time round which started it all off). Doing a big homological algebra project will give rise to a slightly simpler use case which will be showing up in every second line of the argument.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133299726):
It might be a better test case for what we want and how far we can get it to go, because I'm asking for less but conversely the thought of doing it "by hand" would be a nightmare.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 04 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133300209):
That sounds like an interesting example. And maybe a good motivation to look more closely at Johannes' work. I'm certainly willing to pick up the project again but maybe we don't have start from scratch (or my scraps, anyway)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133304087):
[@**Scott Morrison** 04/09/2018 02:15:15 (UTC):](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/Perfectoid.20spaces/near/133287172)
```quote
A while ago I tried proving that the forgetful functor `CommRing ⥤ Type u` is represented by `ℤ[x]` (i.e. this just says that ring homomorphisms `ℤ[x] ⟶ R` are the same as elements of `R`), but got frustrated dealing with polynomials. I think we now have much better polynomials, and perhaps I can tempt someone who has worked with them into showing this fact. (@**Chris Hughes**?).
```
done:
```lean
example : {f : polynomial ℤ → R // is_ring_hom f} ≃ R :=
{ to_fun := λ f, f.1 polynomial.X,
  inv_fun := λ r, ⟨polynomial.eval' ℤ R r,
    @is_alg_hom.to_is_ring_hom ℤ _ _ _ (polynomial.algebra ℤ) _ _
      (polynomial.is_alg_hom _ _ r)⟩,
  left_inv := λ ⟨f, hf⟩, subtype.eq $ funext $ λ p,
    eq.symm $ @polynomial.eval'_unique ℤ _ _ _ _ f
      (@is_ring_hom.to_is_ℤ_alg_hom _ (polynomial.algebra ℤ) _ _ f hf) _,
  right_inv := λ r, by simp }
```
https://github.com/kckennylau/Lean/blob/master/polynomial.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133304101):
I won't PR this until the typeclass issues with algebra can be resolved

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 04 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133304295):
Cool! Thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133304350):
I can't believe I spent 6 hours to write 210 lines of code

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 04 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133304590):
Is that a lot or not many? :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 04 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133304735):
a lot of time and not many lines of code

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133306823):
Lean code has a lot more content than, say, python code. If you spent 6 hours writing 210 lines of python code you were either doing something super-hard, or being lazy. But 6 hours for 210 lines of Lean code looks fine to me. I saw Mario spending 3 hours writing about 100 lines of code last week.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 04 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133317508):
6 hours for 210 lines sounds quite fast to me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 10 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133682677):
So, what is the status here. We now have basic stuff on Noetherian modules.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 10 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133682693):
@**Kevin Buzzard** Hilbert basis isn't there yet, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 10 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133682704):
And I remember something about `V_pre`. Can we now define that, using all Scott's stuff?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 10 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133682707):
Yeah, who cares about matrices when we still don't have perfectoid spaces?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 10 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133682786):
I think @**Scott Morrison** was working on sheaves with values in another category.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 10 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133682912):
Hmmm, this only seems to be about sheaves of types: https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/sheaves/of_types.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 10 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133683704):
I did matrices because I was spending the day with undergraduates. Hilbert Basis I'm working on. Polynomials are subtle beasts.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133683813):
Ok cool. I really love how fast things are moving.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 10 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133683867):
Completions are not moving fast :sad:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 10 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133683876):
It's partly because real life caught me, partly because I really need help

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 10 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133683994):
Hmmm... I've looked a bit a filters recently. But I'm really a novice. Can you indicate in one or two lines what the problem is?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 10 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133683996):
I have fewer Lean students now, many of them stopped at the end of August; two MSc student went back to France and next week my UK MSc students will hand in their projects. I need to think hard about UG teaching but I think Patrick is right, we've said we'll do perfectoids, there's nothing in theory that prevents us from doing it, it looks good, it's a good ad for Lean, we should do it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 11 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133713456):
The better file to look at for sheaves is <https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/sheaves.lean>. The one Johan linked above is actually a convenience: if you have the right sort of concrete category (the forgetful functor is `faithful`, `continuous`, and `reflects_isos`) then to check the sheaf condition it's enough to check the sheaf condition on the underlying presheaf of types.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 11 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133713463):
(Not that I actually prove that there: it's just the statement for now!)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 11 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133713467):
I should look at this V_pre thing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 11 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133713545):
[Screenshot-2018-09-11-16.58.27.png](/user_uploads/3121/iSqAQpjcqT1pLw65lBtIkCbo/Screenshot-2018-09-11-16.58.27.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 11 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133713604):
Right... as far as I can see almost all ingredients for this definition exist.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 11 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714540):
Just some comments on the definition. (1) we will be interested in sheaves of course; the presheaf category is just a bigger category where some auxiliary constructions take place. (2) Line 4 of the screenshot means "compute the stalk in the category of presheaves of rings not topological rings" (i.e. forget the topology) rather than "these stalks form a presheaf in some way". (3) An equivalence class of valuations on a commutative ring `R` is simply a term of type `Spv R`, with `Spv` (the "valuation spectrum") defined in `valuation_spectrum.lean` in the perfectoid project, and the condition about the support being the maximal ideal is just a predicate (which only makes sense if `R` is local and hence is not yet there). I'm hoping that this is all the information Scott needs.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 11 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714676):
I made a start of `prev_V`: https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/V_pre.lean. So far no hurdles, it's just like building Lego.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 11 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714681):
I'm not sure whether I really want to add `perfectoid` as a dependency.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714700):
I guess I should move across to the perfectoid project to do that bit.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714701):
Why don't you do the opposite? PR to perfectoid-spaces?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714710):
Is it okay having perfectoid depend on lean-category-theory?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714715):
you might be surprised to hear that defining an equivalence class of valuations was extremely painful. There were universe issues.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 11 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714716):
:-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 11 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714771):
Dependencies -- my only worry is that when I did that in the past (with the schemes project I think) what happened was that my code never seemed to compile, because category theory was very much a WIP at that time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 11 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714774):
(this was months ago, when the category theory library was undergoing major refactoring)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 11 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714776):
I think perfectoid depending on category theory is fine, especially since merges come in at a steady pace

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 11 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714783):
so it will soon be depending on mathlib only

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 11 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714787):
My instinct is not to push for perfectoids to go into mathlib until after Lean 4. Is that crazy?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 11 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714789):
[if indeed they go in at all]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 11 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714826):
I meant: category-theory will be in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 11 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714833):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 11 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714837):
I was just thinking aloud

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 11 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133714856):
If we manage to define perfectoid spaces then many things will go into mathlib without hesitation. And then you'l be left with a couple of files that could go as well, in a somewhat lonely directory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 11 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133734386):
Ugh. I just finished a construction of the category of presheaves (that is, the objects are pairs (X, O), for X a topological space and O a presheaf of somethings on it, and the morphisms are pairs (f, f'), f a continuous map X \to Y, and f' a natural transformation from O_Y to the pushforward of O_X).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 11 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133734418):
Hopefully after this, `V_pre` is just picking out an appropriate subcategory.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 11 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133734442):
Unfortunately, at some point it stopped being easy --- the proofs I've written that morphisms of presheaves compose, and compose correctly, are really really deeply horrible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 11 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/133734495):
https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/V_pre.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134008420):
Here's a perfectoid update. 

We need integral closures and for this we need either Cayley-Hamilton or Hilbert Basis. Somebody will do Cayley-Hamilton some day (we do have matrices after all ;-) ) so I'm doing Hilbert basis. It's taking a long time because whilst I now know a beautiful way to do it thanks to @**Reid Barton** , working with the theory of polynomial rings and modules over multiple rings has given me a clear picture about exactly what needs doing, and I still have problems with the underlying set-up, basically because a type M might be a module for more than one ring. I am not even sure if typeclass inference is appropriate for the kind of calculations I am doing, and it's not something strange -- the ideas I'm formalising show up everywhere in commutative algebra. So that's the situation regarding integral closure. @**Mario Carneiro** did you say you were going to refactor...something to do with modules? Should I wait until you finish this? The Hilbert basis code relies on the `poly_coeffs` branch of community mathlib, which has been PR'ed. Let me know if any work needs doing on this PR. Here is an explicit question. In maths, if $$J$$ is an $$R[X]$$-submodule of $$R[X]$$ then it is naturally an $$R$$-submodule of $$R[X]$$. How to say this in Lean? That is the goal I am looking at now and I think I might take a break until it's clearer to me what mathlib's general approach to this sort of question is.

Completion of a ring -- @**Patrick Massot**  has done a *lot* of stuff about completions, but I think he said the other day that something was blocking him from proceeding. Maybe we have completions of topological abelian additive groups, but not yet of commutative rings?

And finally this category. Thanks @**Scott Morrison**  for the valiant V_pre effort! I stopped "racing to the goal" a while ago because I didn't know whether we could make V_pre easily or not and I thought I'd defer to you. I think that what I need to do now is to actually think about how much of this category we actually need. Ultimately one should prove that there's a morphism from the category of Huber pairs to V_pre, however whether we need something so strong depends on exactly how far we want to go. Merely writing down the definition of a perfectoid space might not need it, but saying anything at all about them will surely need something like this.

Maybe it is time to think about things in a "top-down" way a bit more, and in particular it might be worth formalising the *statements* of integral closure and completion of a ring, leaving them as "TODO" (Scott -- these are exactly the things which are stopping me from constructing objects of V_pre -- to make an object corresponding to a Huber Pair A I need to build a presheaf on Spa(A) and the above constructions are part of the infrastructure I need for building this presheaf).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134008922):
I pushed (non-working) branch `kmb_hilbert2` to community mathlib in case anyone wants to see the status of Hilbert basis. The proof I'm aiming for goes like this: if $$I$$ is an ideal in $$R[X]$$ and if $$R[X]_{\le n}$$ is the sub-$$R$$-module of polys of degree at most $$n$$ (`deg_le R n` in Lean) then $$J_n$$, the ideal of terms of the form `coeff f n` as $$f$$ runs through the elements of $$I$$ with degree at most $$n$$, is an increasing sequence of ideals. There are several ways to define $$J_n$$ but this one does not need the gazillion edge cases which I had before. Then it's just the standard proof -- the union of the $$J_n$$ is finitely-generated so is $$J_N$$ for some $$N$$ and choosing generators of $$J_i$$ for $$i\leq N$$ and looking at corresponding polynomials finishes the job easily.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134008983):
But I propose not working on it any more for a while until I understand what Mario is doing with modules and the poly_coeffs PR; I'll instead concentrate on the top down questions (i.e. how far are we from a definition modulo a few concrete sorries which are basically independent simpler questions)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134009618):
Again, the status for completion is I'm stuck at three points: 
* https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L124 where I'm also not clear on the math proof (and Bourbaki doesn't really help because Johannes didn't follow Bourbaki when defining completions of uniform spaces) but I should be able to understand this.
* I don't know how to use the previous point (even sorried) in order to unlock https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L132 Because it seems hard to opt out of the automatic instance resolution to manually insert a propositional equality of two uniform structure on the same type. I think this is the crucial point where I really need help
* when I try to use https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L132 with multiplication on topological rings I have instance loops (I could push my failed attempt if needed)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 15 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134017508):
```lean
noncomputable def completion.map₂ (f : α → β → γ) : completion α × completion β → completion γ := 
  completion.map (uncurry f) ∘ completion.prod
```
Why do you uncurry in `completion.lean`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 15 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134019674):
Here `α`, `β` and ` γ` are uniform spaces.  `α × β` is also a uniform space, but `β → γ` isn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 17 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134088693):
@**Kevin Buzzard** while you wait for Mario's module refactor, why don't try to LaTeX a precise roadmap? As I said in the very beginning of the project (we even have a LaTeX_docs folder) it would be much easier to have a full LaTeX writeup of the definition of a perfectoid space, assuming only knowledge of basic theory of topological rings and sheaves

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134089151):
You mean of what still needs to be done, or everything?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134089166):
Wedhorns paper defines an adic space and it's 100 pages

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 17 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134089206):
Of course everything would be better, but what still needs to be done would be enough for now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 17 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134089214):
You claimed earlier that those 100 pages are not all necessary for the definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 17 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134089236):
I'm not suggesting to rewrite that paper, which obviously contains preparation for things coming after the definition, as well as motivation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 17 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134089245):
We don't need any of this to define perfectoid spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134089548):
Patrick I'm going to do this right now. What exactly do you want me to cover?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134089575):
Just statements such as "if R is a topological ring then there's a completion R-hat which satisfies a universal property -- for the property see section blah of Wedhorn and for the construction see section blah"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134089621):
Have I now completely covered completions of topological rings, once I fill in the references, as far as this document is concerned?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134089624):
The reason I want to do it now is that I was thinking about exactly this sort of thing when you suggested it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 17 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134089627):
Yes, at least until you reach the end goal (definition of perfectoid space). Then we may or may not want to add details

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134089628):
and I have an hour before my first meeting this morning. But I don't want to write something and then you say something else was better.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134091570):
OK I pushed a first draft. Patrick -- let me know what else you want from this doc. All refs are to Wedhorn, I didn't put the citation in explicitly because I'm in a rush

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 17 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134094182):
It's looks like a good start, but obviously more details are needed in Section 3

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 17 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134125363):
Today I spent some time working out the maths part of why the two natural uniformities on the completion of a commutative topological group coincide. It won't be easy to Lean, but it should work. Then I would really need to think about how to get Lean to use this fact...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 17 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134125768):
Returning to the LaTeX documentation, I guess the real test would be: Kevin, could you finish the definition by sorrying only lemmas and no definition?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134126506):
We need to define the presheaf on `Spa A`. The reason I stopped is because for a rational open subset `U`, the value of the presheaf is a completion, and we don't have ring completions yet. Nice work on the group completion, by the way. After that we need to define the presheaf on all open sets, and that's via a projective limit construction; we need a statement that this limit is unique up to unique isomorphism. Then we need to define the valuations on the stalks etc etc. Are you saying I should write more Lean code or more LaTeX?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 17 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134129017):
You could write both more Lean and LaTeX. You can sorry the ring completion thing.  State the existence of the completion and its universal property and move on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134129693):
I'm watching these Zurich videos though :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134146650):
```quote
It's looks like a good start, but obviously more details are needed in Section 3
```
I am unclear about what you want to know (in particular you are saying things are obvious but they're not obvious to me yet). Sorry to go on about this. I'm happy to write stuff, I'm just not sure what I am supposed to be writing. 

Let me pick out a few examples from section 3 to make my question more explicit. 

I say that Spa(A) is an equivalence class of valuations. I imply that these are "done". In fact the maths definition of valuation is in Wedhorn chapter 1 and the Lean definition is in `valuation.lean`, which has no sorrys.  Do you also want me to write out the definition in LaTeX or just make the references more precise or what?

Next I say Spa(A) is a topological space. Here I am lazier -- the maths in in Wedhorn and the formalisation is in `Spa.lean` but I just say it can be done. Do you want more precise references, or an explicit definition of the topology in the document?

Finally for this message, the presheaf. Here I just say it can be defined on the rational subsets and then it can be extended. This is not in Lean for the simple reason that here we are part of the "bottom up" way of thinking, and the definition of the global sections of the presheaf on Spa(A) is equal to the completion of A. Here I say nothing, and there is no Lean file, but I give a precise citation to Wedhorn. Is there a problem with the LaTeX file here or is the only problem that we need more Lean code?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134156459):
@**Patrick Massot** I updated the file a bit. Let me know what you want from this file -- I will have some time on the tube home this evening to work on it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134159914):
I tried to clarify my question by opening an empty PR. It adds sorried statements in `ring_completions.lean`. Question is: would proving this be enough for you to finish everything?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134160873):
It would take me some time, I guess, and time is something I don't have much of at the minute. We need to take an integral closure, for sure. I don't see any obstruction to finishing everything apart from the fact that someone actually has to do it. But I have 250 students arriving here in 13 days' time and I need to be ready for them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134160890):
PS to take integral closure we either need Cayley-Hamilton or working modules, and currently we have neither, but both are possible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134162113):
@**Johannes Hölzl** do you know if `separated α`implies  `separated (Cauchy α)`? I'm still struggling a bit with with uniform spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 18 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134162185):
No, for example the rationals are separated, but `Cauchy` over the rationals isn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134162197):
Kevin, if you don't have time for this and don't have time for a detailed LaTeX file then I guess we are stuck. Otherwise people (Johan or me say) could try to do the Lean job from the LaTeX file (although I have a lot to do with completions)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134162214):
Johannes, this is what I suspected. But somehow it should be true that if α is separated then it should inject into its separated completion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134162267):
I'm struggling because you set up everything to avoid minimal Cauchy filters that Bourbaki uses everywhere

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134162286):
Bourbaki first makes things separated and then takes the space of minimal Cauchy filters

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134162295):
And the second operation is always injective

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134162340):
So we get injection of separated stuff into their separated completion for free

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134162369):
But it should still work with your way of doing things, since I proved the separated complete space obtained and the separation space of Cauchy α satisfies the obvious universal property

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 18 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134162375):
I had a proof for the reals that the usual embedding `α -> quotient (Cauchy α)` was injective if `separated α`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 18 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134162378):
I thought also you had this already

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134162390):
No I don't have it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 18 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134162555):
Ah, I had it directly on `rat`: https://github.com/leanprover/mathlib/blob/7fd7ea8c323c5f622bda6bc8de6dd352cc2732a8/analysis/real.lean#L401

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134162622):
It looks like a specific proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 18 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134162635):
yes :(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134162759):
Do you remember where you saw this story of the space `Cauchy α` (as opposed to the space of minimal Cauchy filters)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 18 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134163062):
Hm no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 18 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134163074):
But I will try to proof this injectivity now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 18 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134163694):
@**Patrick Massot**  it was surprisingly straight-forward:
```lean
example : function.injective (λa:α, ⟦pure_cauchy a⟧) | a b h :=
have a_rel_b : (pure_cauchy a, pure_cauchy b) ∈ ⋂₀ (@uniformity (Cauchy α) _).sets, from quotient.exact h,
classical.by_contradiction $ assume : a ≠ b,
let ⟨s, hs, ne⟩ := separated_def'.1 s a b this in
begin
  rw [← (@uniform_embedding_pure_cauchy α _).right, filter.mem_comap_sets] at hs,
  rcases hs with ⟨t, ht, hts⟩,
  have : (pure_cauchy a, pure_cauchy b) ∈ t, by simp at a_rel_b; exact a_rel_b t ht,
  exact ne (@hts (a, b) this)
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134163821):
Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134163878):
I'll need to decipher this now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 18 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134165812):
actually the contradiction is not necessary: https://github.com/leanprover/mathlib/commit/7dedf3ca65f4a183909f51879cffddd6edc6e20a

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134167252):
Thanks! Too bad this proof is locked into term mode. I'd love to know the maths there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134172968):
I need to make sure that I'm ready for the students so I should concentrate on that for the next 13 days, but hopefully then the modules are refactored, I'll know what I'm doing with CoCalc, and I can come back to this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134172988):
Could you still review my PR?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134174890):
```quote
I'll need to decipher this now
```
Ok, I managed to read it. It contained enough tactic mode. I also deduced from it that the map to the Hausdorff completion is a uniform embedding when the original space is Hausdorff.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 18 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134183580):
Patrick I don't review your PR's, I just accept them :-) I will "review" this one later on today hopefully. Does `for_mathlib/topological_structures.lean` work for you? It has an import `for_mathlib.function` which isn't there for me...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134184098):
Oh crap, it works here because `for_mathlib/function.olean` is still there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134184166):
This is so annoying. Is there any drawback to making sure `leanpkg build` deletes `olean` files that don't have `lean` file?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134184170):
I guess this question was already asked many times

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134184302):
I just manually removed 9 dangling olean files

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134184305):
Let's see where we are

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134184321):
Maybe that also explains why I needed to "fix" stuff and Johan complained about the fixes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134184558):
No, the fixes are still needed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134184569):
Kevin: it should compile on your end now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 18 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134184686):
You should still make sure my fixes didn't change the intended semantic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222042):
@**Patrick Massot** @**Johan Commelin** I reviewed Patrick's changes. If neither of you have any more to say then I am happy to merge.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222118):
I just explained how to ignore whitespace :lol:  Other than that... `-- no comments`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222156):
I really need to take two weeks off from the perfectoid repo at this point. It looks to me that it's in good shape. Other than ring completions and integral closures (which are disjoint independent problems) the main thing that is needed is the definition of the presheaf on Spa(A) and the valuation on the stalks -- i.e. constructing an object of the category V^pre from a Huber pair. Assuming a sorried (ring completion + universal property) and a sorried (integral closure of a ring is a ring) this seems to be the key remaining construction.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222181):
I will see if I can do some work on this. But I'm currently in a train to Ben's birthday party, and beginning of next week I'm also busy in NL. So I won't be back at Lean until Thursday next week.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222242):
I would like to try some stuff with the presheaves. As soon as @**Scott Morrison** is back at Lean, I hope he will also get some sheafy PR ready. Or do you think this is something that I could get PR ready myself, Scott?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222265):
The integral closure project is currently blocked by the module refactorisation, I guess.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222314):
With completions I don't think I can be of much help, because my filter-fu is nilpotent

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 19 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222322):
Regarding sheafy stuff... That stuff can't actually make it into mathlib before all the work on limits gets to mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 19 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222325):
That is pretty close, mostly filling in gaps.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 19 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222335):
I got distracted last time I was working on it by the prospect of writing tactics to work with diagrams.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222339):
Aaah, I see. Is it best if we just sit back and wait? Or can we contribute in a constructive way?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 19 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222352):
The diagram stuff could be pretty cool, but maybe more on that later. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 19 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222405):
I had wanted to prove some basic facts like "has_limits implies has_equalizers", etc. etc., but as none of that is necessary for basic sheafy stuff, I should just leave that for a later PR.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222544):
We probably also want all sort of lemmas about defining a sheaf on a basis of a topology and extending it to a sheaf by blah, etc...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222546):
But that is something *we* could do, once the definition of a sheaf is in mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222557):
Can't we add Scott's lib to the perfectoid project dependencies ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222564):
Hmmm, that has been discussed before. I think it is a good idea.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222622):
Patrick, did you recently look through `for_mathlib` to see if we could PR stuff from there?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222634):
Otherwise that might be something I could do somewhere on this trip

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134222868):
I guess `add_subgroup.lean` is already in mathlib... `ideals.lean` should probably wait till the module-refactorisation is done. Afterwards we can see how much survives. `option_inj` and `quotient` and `topology`could at least partly be PR'd I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134223515):
https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/uniform_space.lean could go in, those bits were forgotten in a previous PR

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134223533):
Are you sure add_subgroup.lean is in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134223534):
No

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134223543):
I just couldn't imagine it wasn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134223619):
I think Mario at some point merged it into mathlib using `to_additive` magic that I still don't understand. But maybe my memory is bad.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134225024):
I think this was is_add_group_hom

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134225054):
No, you're right, https://github.com/leanprover/mathlib/blob/master/group_theory/subgroup.lean is also there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134225201):
I removed it (including the olean...) and I confirm it doesn't change anything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134228990):
I have to make a confession about this $${\mathcal V}^{pre}$$ stuff: a natural question when you read Wedhorn is "can Lean do stuff like $${\mathcal V}^{pre}$$ nowadays?", and can we prove that `Spa` is a functor from Huber pairs to $${\mathcal V}^{pre}$$? But actually the category theory language is just a convenient language for mathematicians to use here, because it's a way of saying "5 lemmas about `Spa` are true" all in one go. I am not so sure that we need to make a structure called "the category $${\mathcal V}^{pre}$$ in order to achieve our primary objective.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134229055):
Whether or not the category $${\mathcal V}^{pre}$$ goes into the repo, this does not change the fact that someone, probably me, needs to actually construct the map on objects.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134229142):
So if it helps to have the category theory repo as a dependency then that's fine, and of course ultimately if one is going to actually define the category of perfectoid spaces then one will need to be able to talk about categories -- but if one is just going to define the structure and then say "we did it" then we might not need $${\mathcal V}^{pre}$$. It depends on what the ultimate goal is. It should be there but we can work around it is I guess what I'm saying. I never defined a morphism of schemes in the schemes project.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134229450):
As you wrote elsewhere, we want mathematicians to recognize the theory when browsing the perfectoid repository. So it would probably be better to have the category where it belongs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134260907):
I think we should go the way of the category (-;
If this means that we have to pay for it because there is too much bundled stuff or so... then we have identified a pain point that has to be fixed. Like you say the categories will be inevitable anyway.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134261243):
I am happy if both of you want to do this. But I don't quite see the logic -- it's like saying we need Scott's repo as a dependency if we're working with groups, because we can't say that groups form a category otherwise. What I'm trying to say is that just need to construct a *function*, not a *functor*, which eats `A` and spits out a structure which happens to be an object in a category which we don't strictly speaking need (we don't need to take limits, or products, or even compose morphisms -- or even use morphisms -- indeed it will be hard work to define the morphisms and we won't need them).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134262632):
Ok, so maybe we don't need `V^pre` as a category. But if we add Scott's lib as a dependency we do get immediate access to sheaves. That seems enough reason for me to add the dependency.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134263777):
I didn't understand that getting V^pre a category would mean useless work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134263799):
But it's a virtual discussion anyway if nobody can work on this. I have a *lot* of work to do on the topological group front

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134323352):
`definition power_bounded_subring := {r : R | is_power_bounded r}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134323354):
Should this be a set or a subtype?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134323397):
Someone will have to prove it's a subring at some point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134323631):
It should be a subring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134531313):
I think I want to focus on the perfectoid project for the next few days.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134531324):
@**Patrick Massot** You had some discussion with Kevin on where the gaps are.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134531331):
Do you see a gap that isn't "completions" on which I could work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134531347):
(I finished several maths projects, so I will treat myself on some Lean time.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134531357):
Should I try to define V_pre?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134533591):
Have you checked the outline tex file which Kevin added somewhat recently?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134533826):
Scott has been trying to define V_pre over in the category theory repo, I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134533855):
But maybe it's not quite the same thing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134533912):
Ok, I'll try to dig those up.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134534018):
It looks like what Scott is doing specifically is the category where an object is a topological space X plus a C-valued presheaf on X, for some arbitrary category C.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134534031):
Is V_pre a specialization of that for C = something?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134534157):
I looked it up--not exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134534216):
but I guess a good start would be to define a category of complete topological rings?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134534434):
Yes, I agree.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134534462):
I was doing that, and then I got distracted. I'm doing a small cleanup of Huber pair atm.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134534474):
But let's return to complete topological rings.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134534672):
This might be too nitpicky, but possibly it would be better to have the subcategory of all topological rings.
Because on p. 80, V is defined to be the full subcategory of V^pre on the objects for which O_X is a sheaf of topological rings, and a priori the definition of "sheaf of topological rings" is not the same as "sheaf of complete topological rings".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134534694):
Agreed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134534766):
Do we have subcategories yet?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134534767):
(I am happy to see Remark 8.19--I wondered if they would notice that a sheaf of topological rings is genuinely not the same thing as a sheaf of rings)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134534769):
I think so, category_theory/embedding.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134534904):
You have to attach this extra valuation data anyways, so I think the definition of V^pre is going to be rather custom

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134534907):
Ok, good.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134534932):
It's not a subcategory of a presheaf category in an obvious way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134534941):
No, I agree...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134534971):
So, what do you suggest. (1) topological rings. (2) subcategory of complete topological rings. (3) presheaf with values in (2).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134535014):
And then just going on with the custom stuff?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134535179):
I think it might be simpler to skip 2 and put the completeness condition in the custom stuff, since later you're going to want to assert that the presheaf of topological rings is a sheaf, but it probably doesn't matter much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134535259):
Ok, I'll try to define a category of topological rings.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134535264):
I don't understand where all these conditions come from, so my opinion might be ill-informed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134535310):
Well, I'm not an expert either (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134536345):
It appears to me that
* a limit of complete topological rings is complete,
* consequently, the sheaf on any pre-adic space takes values in complete topological rings automatically, even if we did not require it in the definition,

and so it shouldn't matter where you insert "complete", if anywhere. But I'm not 100% sure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134536785):
So, how would you define the category of topological rings? Start from scratch? Or build on top of `Ring`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134536983):
We can't do `bundled topological_ring` because that requires `ring` and `topological_space` to be present.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134536999):
What goes wrong with that exactly?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537005):
```lean
type mismatch at application
  bundled topological_ring
term
  topological_ring
has type
  Π (α : Type ?) [_inst_1 : topological_space α] [_inst_2 : ring α], Prop : Type (?+1)
but is expected to have type
  Type ? → Type ? : Type (max (?+1) (?+1))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537009):
Oh I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537064):
I guess we could bundle up `[topological_space a] [ring a] [topological_ring a]` into one class for use when defining the category

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537077):
So start from scratch

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537100):
Well, using `bundled` with a custom class which can just be `extends ...`, I think, with an empty body

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537174):
Aaah, I can try that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537185):
```lean
class actual_topological_ring (α : Type u)
  extends ring α, topological_space α, topological_ring α
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537203):
Right.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537253):
I was going for a `'` at the end, but `actual` is also a good idea.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537259):
Should we do `ring` or `comm_ring`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537268):
Or just do both, and make the `comm_` explicit: `actual_topological_comm_ring`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537383):
Oops, `comm_ring` of course. Oh wait, there is no `topological_comm_ring`. So you could just use that name...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537385):
Probably too confusing...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537400):
I thought my `actual_` sounded a bit irritated :smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537409):
Hales topological commutative ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537473):
I think then you should get all three of those classes on the underlying type of an object for free

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537587):
Haha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537588):
`class is_topological_ring_hom` or `class is_continuous_ring_hom`. What do we choose?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537920):
Wedhorn says "continuous ring homomorphism"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537924):
I guess go with that one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134537943):
I bet Wedhorn doesn't say `add_comm_group`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134538394):
Nope.
"Let $$G$$ be a filtered abelian group (written additively), ..."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 24 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134540645):
```quote
Do you see a gap that isn't "completions" on which I could work?
```
Unfortunately I don't have anything better than https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/LaTeX_docs/overview.tex and Wedhorn. I think it's pretty hard to work on this without a clear view of the maths. However it should be rather easy for you to work on extracting from Wedhorn and Kevin's overview a detailed LaTeX file containing the full definition we are trying to formalize. Then everything would be easier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 24 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134540769):
I really think that it would be super useful for everybody to have a complete LaTeX'ed version of the perfectoid project, including everything from the beginning (of course LaTeXing the definition of a group would be really low priority). It would be useful before finishing the Lean project but also after finishing, since people could then go back and forth between LaTeX and Lean, trying to match things.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 24 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558347):
Sorry, late to the party.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 24 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558396):
On the `working` branch of `lean-category-theory` there is a file defining the category of topological rings.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558412):
Does it work? :smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 24 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558417):
Sorry this wasn't on `master` -- I've been trying to keep that compiling, and not depending on PRs to mathlib, but I have a stack of open PRs waiting on mathlib so it's been hard to reunite my `working` branch with `master`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558435):
So `working` is the non-working branch

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 24 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558522):
It may actually work :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 24 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558526):
Haven't actually looked at it in a few days.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 24 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558539):
It depends on commits to `leanprover-community/mathlib`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558629):
which branch?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 24 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558630):
It looks like `TopRing.lean` itself compiles fine :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 24 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558643):
It depends on a branch called `scott/supremum` which is the supremum of my PRs. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 24 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558657):
I should enquire sometime if there is an obstacle for those PRs. I think they're ready to go.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558664):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558680):
You don't happen to have a branch with limits do you? I was thinking of making one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558746):
because most of the things I want to do are dependent on limits, and it's somewhat less convenient to use lean-category-theory as a dependency (for example I might want to modify the files related to limits)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558771):
I started on making one, but then it seemed like it might involve pulling in nontrivial amounts of lean-tidy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 24 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558850):
No, there's not yet. I did start porting, but realised I really wanted `backwards_reasoning` available in `mathlib` first, and then hit pause because I already have too many open PRs, and needed to do other work too. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 24 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558892):
If you happen to want to push that to happen, you could either PR `backwards_reasoning` yourself, or review some of my open PRs so I either retract them or they get merged. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134558990):
Yes, I might take a stab at backwards_reasoning, since I also want it for other things (continuity).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 25 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134580882):
Sorry I'm even later -- after quite a hectic weekend I'm spending Mon and Tue focussed on real life issues. @**Johan Commelin** I had a lot of energy for doing the Hilbert Basis Theorem last week, but when I realised that I had to fight with the old module system and then Mario kindly decided to refactor everything I decided I would use this as an excuse for focussing on my upcoming teaching (my class starts in 9 days' time and I'm still not ready). I did find the time to look at the repo from the top down. Johan if you're looking for some easy pickings then here are a couple of things which need doing. 

1) in valuations.lean I skipped a proof and this will surely bite us later. A valuation is continuous if (blah -- see Wedhorn). Note that in this definition you replace the target group Gamma with the subgroup generated by the image of the valuation -- this is important. With this definition, if two valuations are equivalent then one is continuous iff the other is. I did not prove this because at the time it involved extending a valuation on `R` to a valuation on `Frac(R/P)` with P the kernel (the "support") of the valuation and we didn't have field of fraction of an integral domain or proof that R/P is an integral domain for P prime -- I believe these are now there.

2) in Spa.lean we need to prove completely trivial stuff about the topology, I'm in a rush now but basically the we have something like basic opens and rational opens, and for one of these things (maybe rational opens) the definition of the presheaf is "the set is defined by |t1|<=1,|t2|<=1,... and |s|>0, so localise R at s and then look at the ideal of R0 generated by the t_i and complete". If we have a sorried ring completion we can make this definition and then ones attention turns to extending this definition across all of Spa(R) via a limit construction (if U is a union of rational opens Ui then define O_X(U) = proj lim of O_X(U_i)). You'll then run into the problem of having defined O_X(U) twice for U a rational open, so the first definition might be O_X^aux or something. But all this stuff is very do-able right now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 25 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134581284):
Thanks Kevin! I'll see if I can make progress on those while I'm on the train back to Freiburg tomorrow. Today is the PhD defense of my PhD brother. So I won't have much time for Lean today.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134591981):
Do we really need Wedhorn's "Remark and definition 8.5" in order to define adic spaces? To me it looks like we could use the same kind of loophole as in the early scheme formalization, at a time when affine schemes were not yet schemes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134592095):
Maybe I should write 8.6 instead of 8.5. I meant: do we need to prove that, in the model case of Spa(A), stalks of the structure sheaf are local, with maximal ideal the support of the associated valuation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 25 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134593124):
I think we do. The problem is that whilst the stalks and support are defined by the sheaf, the valuation is not. An adic space has a cover by affinoid adic spaces. If we only demand that the identification of an element of this cover with Spa(A) is an isomorphism of top spaces + presheaf of rings then we risk there potentially being the issue that two different rings corresponding to two open sets which have non-trivial intersection give rise to two different valuations on the local ring with the same support, so this would not be an adic space. I have absolutely no idea whether this can happen.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 26 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134661684):
So there is a `quot.lift_beta` which I think is called `lift_mk` for other quotient types. But for `quotient` itself I didn't find anything like `lift_mk`... did I miss something?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 28 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134812584):
@**Kevin Buzzard** Is there a reason why `valuation.map_add` uses `.. ≤ .. ∨ .. ≤ ..` instead of `.. ≤ max .. ..`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 28 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134812601):
Did @**Kenny Lau** write this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 28 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134812607):
If you didn't: yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 28 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134812648):
I am 50 now, I can't remember what I wrote :-(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 28 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134812661):
Wait, you're 50? When did that happen? :lol:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 28 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134825074):
@**Kevin Buzzard** I've unlocked `rational_open_is_open`. So I think we can now define the sheaf on the rational open sets (up to ring completions).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 28 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134825112):
After that we want to extend it to all opens, but this seems like a very generic procedure. So maybe we should prove some categorical lemmas about sheaves on basic opens

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 28 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134825830):
Kevin, I created a PR for this. It also fixes some notations and coercions. Please only merge the PR from my `Spa` branch.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 28 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134825847):
After that, I guess there will be merge conflicts for my other two PR's. I will fix those later.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 28 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134831626):
I have PR's??

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 28 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134831634):
I do not get notified about these in any way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 28 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134831653):
Johan -- can you follow Patrick's lead and just bluntly tell me about them? ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 28 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134831666):
I am even watching the repo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 28 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134832218):
Weird... I expected you to get notified.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 28 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134832220):
Anyway, you've got 3 PR's :lol:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 28 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134834619):
@**Kevin Buzzard** In the upper right hand corner of the Github screen there is a bell icon :bell:. If there is a blue dot :blue_circle: on it, then it means you have notifications.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 28 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134834682):
In that notification area I see all the activity on PR's to mathlib etc... I hope you would also see PR's to your repos there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 28 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134835382):
Not for me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 28 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134836268):
Oh thanks, I have some notification thing switched off.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 28 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134838777):
```quote
So I think we can now define the sheaf on the rational open sets (up to ring completions). After that we want to extend it to all opens, but this seems like a very generic procedure. So maybe we should prove some categorical lemmas about sheaves on basic opens
```
@**Scott Morrison|110087** Can you give an idea of how far we are from being able to do these things with our library? I guess the important thing we need is to be able to write down a (directed?) limit of complete topological rings (and prove that it exists...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 28 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134844825):
wait wait. We need a projective limit of topological rings with its topology, and we need a direct limit of topological rings but taken in the category of rings.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 29 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134858374):
My PR of limits into mathlib is held up at the moment because I want to PR `backwards_reasoning` first, and that is held up because I can significantly improve `backwards_reasoning`, essentially making it a generalisation of `solve_by_elim`, but I have a PR extending the behaviour of `solve_by_elim` already waiting for merge/review.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 29 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134858416):
https://github.com/leanprover/mathlib/pull/324

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 29 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134860508):
Oh, I hadn't realized you were working on `backwards_reasoning`. I took a look at it today, but all I really did was clean up the code some--no functional changes (hopefully!)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 29 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134860515):
I could PR my changes (to lean-tidy?) if that would still be useful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 29 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134861412):
Absolutely! Maybe my comment above overstated what work I'd actually done. I've been _thinking_ about how to unify backwards_reasoning and solve_by_elim, but no code got written yet. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 29 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134867397):
I'm really looking forward to all this new stuff. @**Scott Morrison|110087** what is the status of colimits? In Orsay we discussed several strategies. Is there still something that needs to be resolved, or is it mostly a matter of time and administration?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 29 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134888527):
@**Kevin Buzzard** Github says that there are no merge conflicts for the other 2 PR's. So I think they are good to go.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 30 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134900439):
OK, as good things go, they went.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 30 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134901337):
So it seems that we're getting nearer. I added some comments in spa.lean briefly outlining the way. Proving things are presheafs -- we'll need some maps. We might need Wedhorn 8.2(2), not sure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 30 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134910845):
@**Reid Barton**, my plan for `backwards_reasoning` was to build on the new functionality for `solve_by_elim`, which lets you specify lemmas (or attributes to gather collections of lemmas) to also apply. 

Step 1 is probably to add `solve_by_elim!` which will succeed even if it doesn't finish the goal, as long as it can apply something (this one won't do any backtracking -- once some applies, it's applied). 

Step 2 is then just to define
```
meta  def backwards_reasoning = solve_by_elim [back]
```
(i.e. use solve_by_elim, but also use any lemma with attribute `back), and
```
meta def backwards_reasoning! = solve_by_elim! only [back!]
```
which will apply any lemmas tagged with `back!` (but won't use apply local hypotheses), even it it can't finish the goal.

Step 3 is possibly to realise that there's almost no space between `solve_by_elim` and `backwards_reasoning`, decide which name should survive, and merge them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 30 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134910850):
Step 1b is to add an output mode which actually reports the successful `apply` steps, for creating tactic scripts.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 30 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134910892):
@**Johan Commelin** the status of colimits is exactly the same as the status of limits: both are waiting on me finding time to either remove the use of `backwards_reasoning` from their proofs, or PR `backwards_reasoning` as outlined to Reid just above.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134939944):
@**Kevin Buzzard** Thanks for merging those PR's.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134940002):
Pretty soon there should be a more general cleanup of the valuation files. All the `option` stuff can be replaced by `with_zero` for great good. Also, some of the files can probably be merged.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134952532):
I think Kenny might have written those things just before those with bot etc types appeared

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134953041):
I agree. But now that they are there, it is nice to use them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134955166):
Kevin, I have defined a `Spv.lift` which should allow for "nicer" definitions, where we can treat valuations as actual valuation functions instead of inequality relations on the ring.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134956471):
Oh that would be great! I was looking at the code the other day thinking how unreadable it was because of that inequality notation . It's done this way (inequalities) for universe reasons.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134956696):
Yes... I did have to impose `decidable_eq R` everywhere. I guess you don't care.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134956705):
Not at all

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134956911):
@**Kevin Buzzard** Is this ok (see the other thread):
```lean
definition Spa (A : Huber_pair) := quotient.mk '' {v : Valuation A | v.is_continuous ∧ ∀ r, r ∈ A⁺ → v r ≤ 1}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134956956):
I'm changing it to something that isn't defeq, but provably the same as you had. And I think this is pretty readable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134957178):
it would be even more readable with `∀ r ∈ A⁺` if the elaborator can do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134957458):
@**Patrick Massot** Agreed, but alas. It doesn't like that :sad:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134957513):
I already had this issue, sometimes it needs a tiny bit of extra characters to put things in order

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134957526):
This is frustrating because it doesn't need `∀ r : A, r ∈ A⁺` so it looks like it could figure it out

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134957643):
Yes, but compared to what we had before this is a really minor inconvenience.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134959313):
Mario told me to use the inequality definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134959358):
I don't have access to lean right now but there are universe issues if you're not careful. I will have to collect my thoughts and try and remember what they were. Didn't I leave a bunch of Mario comments in the source code?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134959401):
You did

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134959410):
But your `minimal_valuation` stuff fixes those issues.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134959423):
So you define `Valuation R` to be all the valuations that live in the same universe as `R`. And then you quotient by equivalence.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134959435):
Given any valuation, you can always take the associated minimal one to lower your universe.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134959446):
So `Spv.mk` takes any valuation, and gives an element of `Spv R`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134970436):
@**Kevin Buzzard** Voila
```lean
definition Spa (A : Huber_pair) :=
Spv.lift (λ v : Valuation A, v.is_continuous ∧ ∀ r, r ∈ A⁺ → v r ≤ 1)
(λ v₁ v₂ heq,
begin
  ext, split; intro; split,
  { exact Valuation.is_continuous_of_equiv_is_continuous heq a.left },
  { rw ← v₁.val.map_one at a,
    rw ← v₂.val.map_one,
    intros r h,
    exact (heq r 1).mp (a.right r h) },
  { exact Valuation.is_continuous_of_equiv_is_continuous (setoid.symm heq) a.left },
  { rw ← v₁.val.map_one,
    rw ← v₂.val.map_one at a,
    intros r h,
    exact (heq r 1).mpr (a.right r h) },
end)
```
Of course there is still a `sorry` hidden behind `Valuation.is_continuous_of_equiv_is_continuous`. But otherwise this stuff seems to be working.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134970607):
Is it sufficiently universe polymorphic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134970636):
I have no idea what this question means, but it sounds cool when Mario write it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134970737):
Well, `Spv R` should live in the same universe as `R`:
```lean
def Spv : Π (R : Type u₁) [_inst_1 : comm_ring R] [_inst_2 : decidable_eq R], Type u₁ :=
λ (R : Type u₁) [_inst_1 : comm_ring R] [_inst_2 : decidable_eq R],
  {ineq // ∃ (v : Valuation R), ∀ (r s : R), ⇑v r ≤ ⇑v s ↔ ineq r s}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134970741):
And `Spa` is just a subset

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134974057):
The question is whether we think this is more readable then the inequalities.
```lean
definition basic_open {A : Huber_pair} (r s : A) : set (Spa A) :=
Spv.lift (λ v : Valuation A, v r ≤ v s ∧ v s ≠ 0)
(λ v₁ v₂ heq,
begin
  ext, split; intro; split,
  { exact (heq r s).mp a.left },
  { exact Valuation.ne_zero_of_equiv_ne_zero heq a.right },
  { exact (heq r s).mpr a.left },
  { exact Valuation.ne_zero_of_equiv_ne_zero (setoid.symm heq) a.right }
end)
∘ subtype.val
```
Note the last line. Isn't it ugly :stuck_out_tongue_wink: ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134974090):
With the inequalities, all these definitions are one-liners. But there is a mathematical disconnect with the code.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134974162):
With all this `Spv.lift`, we are actually formalising the maths. But I'm not sure if readability increases...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134974758):
@**Kevin Buzzard** I think that all the rewriting I've done so far is probably useful. Now I feel I'm at a fork: either we decide to use the ugly inequalities, or we decide to use the ugly lift. I'dd like to get feedback (from Kevin, but also from others) what the best path is.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134974817):
For comparison, this is what we used to have: https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/Spa.lean#L8-L12
```lean
definition Spa (A : Huber_pair) := {vs : Spv A | Spv.is_continuous vs ∧ ∀ r, r ∈ A⁺ → vs.val r 1}

/-- basic open corresponding to r, s is v : v(r) <= v(s) and v(s) isn't 0 ( = v(0) ) -/
definition basic_open {A : Huber_pair} (r s : A) : set (Spa A) :=
{vs | vs.val.val r s ∧ ¬ vs.val.val s 0}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975154):
And https://github.com/jcommelin/lean-perfectoid-spaces/blob/valuations/src/Spa.lean#L11-L43 is my branch

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975244):
One thing I do know is that by the time I wrote `basic_open` I realised I was very unhappy with the definition, which is simple and readable in Wedhorn and looks awful the way I wrote it. It says $$v(r)\leq v(s)$$ and $$v(s)>0$$, but what I wrote looks nothing like this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975272):
But what is your first impression when you see my version?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975295):
Regarding lifts -- why not just prove that continuity is constant across equivalence classes first, and then make a beautiful definition?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975308):
What would that sorried definition look like?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975312):
I don't think that continuity is the problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975497):
I have sorried the proof that continuity is constant on equivalence classes. But you still get something ugly. You could factor out the `Cont`, but then the second condition would remain, and it would require a `Spv.lift` that is about as long and nasty as what I have now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975510):
I hope a CS wizard sees some pattern in what we are doing, and knows how to improve it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975588):
I think the CS people will never read this stuff until we produce a MWE which is comprehensible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975598):
One can abstract away all the maths and get straight to the point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975604):
@**Mario Carneiro** understands what we are up to.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975612):
Oh OK. I thought he said he still couldn't run the code.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975624):
I am only half paying attention today, I'm busy in Cambridge

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975692):
I haven't even understood what this `Valuation` is. Did the v change to a capital for a reason? What I'm saying is that I'm not at all on top of the point of this thread yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975710):
`Valuation` bundles `valuation` with groups in the same universe as `R`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975726):
In my experience it makes `mk` and `lift` etc easier to work with.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975745):
Even though `Spv` is still defined via inequalities, instead of using `quot`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134975828):
Anyway, I need to be caught by a train. See you later.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134976338):
Those statements aren't in contradiction. I know what you guys are doing, but I still can't run the code

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134976400):
As for "sufficiently universe polymorphic", now the goal is to prove the defining equation of `basic_open`, which BTW will be much easier to read since it won't have that well definedness part in the statement

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134976484):
The reason for fussing about minimal valuations is so that you can prove it even when the valuation lives in a universe other than the one over which the quotient is defined

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134976845):
I am just going to try and write some minimal working code right now because I have half-forgotten the definitions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134979116):
Here's what I remember. @**Johan Commelin** I have written two definitions of `Spa` corresponding to the way I did it at

https://gist.github.com/kbuzzard/a3ef594410cd184c992e73d06cbad229

Can you summarise what you're saying?

I am wondering whether Spv is just a waste of time by the way. I'm not sure we ever use it. See my Spa2 which avoids it completely.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134982114):
@**Mario Carneiro** We had a working `Spa` including topology. When you say
```quote
now the goal is to prove the defining equation of basic_open, which BTW will be much easier to read since it won't have that well definedness part in the statement
```
Do you mean to prove it in terms of the inequalities?
My objection to that is that it looks very unfamiliar to a mathematician. Let me put it like this: the definition in terms of inequalities is provably equal to the one mathematicians use, but it is not *defeq*.
Hence I started working on `lift`, and now we can define these things in the way a mathematician does. But it comes with more proof obligations, and it seems that readability decreases.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134982465):
defeq is impossible here, because the "definition" would have to quantify over all universes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134982885):
In terms of kevin's MWE:
```
def Spa2.mk {R : Type u} {Γ : Type v} [preorder Γ] (v : valuation R Γ) : Spa2 R := sorry

theorem mem_basic_open2 {R : Type u} [has_zero R] (r s : R) {Γ : Type v} [preorder Γ] (v : valuation R Γ) :
  Spa2.mk v ∈ basic_open2 r s ↔ v r ≤ v s ∧ v 0 < v s := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134982951):
Re: Spv is a waste of time, how much do discontinuous valuations matter for your work? You could just bundle continuity into the properties of a valuation otherwise

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134983081):
@**Mario Carneiro** Of course it is impossible to make those definitions defeq. But we have to choose a definition in the end. So my question to Zulip is: is there a clear preference for one or the other?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134983089):
Concerning `Spv`, I think it would also be useful for Zariski-Riemann spaces. But I'm not planning to work on those in the near future.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134983189):
I would have a preference either for the relational version (because it's short and correct), which you could also clean up with some notations probably, or using the `quotient.mk ''` approach, written out as `\ex {Γ : Type v} [preorder Γ] (v : valuation R Γ), Spa.mk v = q /\ facts about v`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134983270):
Bundling valuations is also an option, but I think that since you don't get to pick the valuation group with this approach, it has little to recommend it over plain relations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134983390):
If I recall correctly the content of `minimal_valuation` is that for any `Spa` there is a canonical valuation that represents it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134983407):
I think we can even construct a valuation given an `ineq`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134983411):
that's what I mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134983625):
interface is something like this
```lean
def Spa2.Γ {R : Type u} (v : Spa2 R) : Type u := sorry
instance Spa2.preorder {R : Type u} (v : Spa2 R) : preorder v.Γ := sorry
def Spa2.minimal_valuation {R : Type u} (v : Spa2 R) : valuation R v.Γ := sorry
instance {R : Type u} : has_coe_to_fun (Spa2 R) := ⟨_, λ v, v.minimal_valuation.f⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134983730):
then you can just write
```lean
definition basic_open3 {R : Type u} [has_zero R] (r s : R) : set (Spa2 R) := 
{vs | vs r ≤ vs s ∧ vs 0 < vs s}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984137):
What I meant is that I think you can pick everything. The value group would be a subgroup of `units (Frac (R/P))` where `P` is the prime ideal `{ x | ineq x 0 }`. But I should add that I haven't worked out the math details... so maybe I'm wrong.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984156):
right, kevin did this already

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984182):
So there should be a (computable?) map from `Spv` to `quot Valuation.setoid`. And `mk` goes the other way. This pair is then an equiv.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984184):
and that's what would go in for the `sorry`s above

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984189):
No, Kevin, didn't do that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984207):
(the map is not computable but w/e)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984209):
Kevin constructed a minimal candidate given a `v : valuation`, but not starting from `ineq`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984229):
By definition, that candidate is equivalent to the original valuation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984290):
and it only uses facts about the relation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984308):
Could you link to it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984312):
To what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984396):
`minimal_valuation`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984405):
What I am saying is that currently `lift` is `noncomputable`, but I think we can remove the `noncomputable`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984407):
Ok, I'll look it up.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984417):
https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/valuation_spectrum.lean#L99

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984419):
That's Kevin's version.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984434):
My current version is the same up to moving stuff around and bundling.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984478):
What we currently do not have is anything about `Frac (R / P)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984492):
But that stuff should certainly be doable. I tried it and ran into trouble with `ideal` instances, and decided to wait for you module refactor.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984694):
In Kevin's definition, the Gamma is `quotient (is_group_hom.ker φ)` where `φ : FG → Γ2 := λ f, finsupp.prod f (λ r n,(φ₀ r) ^ n)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984706):
is there a way to write that in terms of the `ineq` generated by the valuation?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984791):
There is a map from `R` to `with_zero (units (Frac (R/P)))`, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984813):
You take the subgroup generated by the non-zero elements in the image

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984830):
No universe issues, if I'm not silly again.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984834):
Is that what's happening here? It's hard to tell

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984847):
Kevin has the free Z module and an extension to option

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984893):
Right, but the `option` is just `with_zero`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984904):
and the free `Z`-module is for universe lowering.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984905):
yes, this used to be the only option :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984929):
There is no universe lowering needed if you start from the `ineq`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984939):
Right, that's exactly what I'm saying.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134984951):
You do need an API to fraction fields etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985007):
What is needed in mathlib's fraction fields?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985016):
I think Kenny wrote localizations a while back

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985022):
I think most of it is there. I'm just hoping that it works more smoothly after your refactoring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985032):
Currently all my code gravitates to a lot of `@`s

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985034):
I don't like that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985060):
Then stop preventing Mario from working on his module refactoring!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985087):
it occurs to me that perhaps I should try to avoid letting expectations rise too much on this refactoring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985089):
@**Mario Carneiro** So you are saying we should just go for the `ineq` statements everywhere, even though that is *non-trivially* equal to what mathematicians write. Is that correct?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985118):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985150):
Hmmm, I don't like that... but you are probably right.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985152):
This is the replacement for using `quot.lift`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985167):
It also means that we don't need any form of `lift` anymore

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985170):
you have to use operations that are manifestly invariant of the choice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985302):
For example `v s \ne 0` becomes `\not ineq s 0`. That the two are equal requires thought. Not much, but it means that every time we have to triple check if we are actually still doing the same as in the "maths world".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985499):
This sounds bad

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985610):
You can write the statement as `v' s \ne 0` where `v' : Spa R` has a coercion to the minimal valuation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985618):
that's what I did above

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985628):
Aah, that's smart! I like that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985630):
Where did you do that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985637):
I didn't register a `coe` anywhere

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985641):
https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/Perfectoid.20spaces/near/134983625

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985721):
Nice. That is good!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985724):
Then you can write theorems (simp lemmas) saying `Spa.mk v s = 0 <->  v s = 0` and so on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985763):
and these are using the fact that the minimal valuation is equivalent to the generator

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985783):
Right. And that is a non-trivial theorem.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985853):
So we could already do this now. Even though the `minimal_valuation` is currently not computable from `ineq`, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985928):
Also, does the inverse of `mk` have a canonical name?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134985988):
it doesn't usually have an inverse

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134986012):
mathlib uses `quot.out` for a noncomputable inverse

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134986232):
`section`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134986451):
Ok, and I guess no one will be angry if `out` turns out to be computable in the end, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134986487):
If there is no choice...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134986497):
@**Patrick Massot** The computer scientists keep stealing all our favourite keywords and letters....

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/134986504):
lambda, section, etc...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 02 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135000526):
```quote
What I meant is that I think you can pick everything. The value group would be a subgroup of `units (Frac (R/P))` where `P` is the prime ideal `{ x | ineq x 0 }`. But I should add that I haven't worked out the math details... so maybe I'm wrong.
```
I made the value group a quotient group of the free abelian group on $$R$$ if I remember correctly, and this was because at the time I believe that neither "$$R/P$$ is an ID" nor construction of field of fractions of an ID were in mathlib. I asked Chris explicitly if he'd do them and I believe he did (they might be next to each other somewhere in an algebra file?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 02 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135000686):
I like the look of this `coe` trick. Sorry, I've been away all day marketing (telling Coates and Wiles about Lean).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 02 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135000963):
@**Patrick Massot** and @**Johan Commelin** thanks a lot both of you for your work on the perfectoid project during this very busy time for me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135018113):
```quote
Sorry, I've been away all day marketing (telling Coates and Wiles about Lean).
```
Did you get any interesting reactions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135018609):
@**Kevin Buzzard** Voila
```lean
definition Spa (A : Huber_pair) : set (Spv A) :=
{ v | (v : Valuation A).is_continuous ∧ ∀ r, r ∈ A⁺ → v r ≤ 1}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135018652):
I think that is looking really nice! Kudos to Mario!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135018667):
The `coe` isn't transparent, but maybe that's not a problem.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 02 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135018671):
Coates said I'd be putting everyone out of a job (and whenever anyone makes that comment I tell them that this is exactly my plan). With Wiles I had a technical discussion involving papers we both knew and which had technical flaws in, and how formal proof verification methods were nowhere near being able to help with these issues. But then I argued that it was not impossible that computers would be able to help in the future, perhaps with basic sanity checks or edge cases, and to make this a reality we needed to engage. My case was helped a great deal by Jack Thorne, a young guy who is Cambridge math's newest full professor, being present too, and Thorne randomly announced very early on in the discussion that he followed my blog and found it very interesting. That was basically when I decided I'd go for it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135018679):
Of course this means that we aren't checking independence of `v`. We are just imposing conditions on a "canonical" representative.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135018728):
Aah, that's cool!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135018735):
Did you invite Jack to this Zulip?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 02 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135018740):
```quote
I think that is looking really nice! Kudos to Mario!
```
And to you sir. That is looking much better. Thanks for thinking about this! I really have my hands full until Thursday. I am hoping to get some Lean done over the weekend.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135018741):
No problem.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 02 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135018758):
We need that if $$U\subseteq V$$ are rational opens then there's a continuous restriction map.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135018759):
I am still on the fence about the "well-definedness" thing. Mathematicians almost never mention it. They just keep track when they think it is necessary to mention it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135018804):
Somehow checking on a canonical representative comes close enough. And I really don't like interspersing everything with long proofs.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135018813):
Maybe an `auto_param` could make `obviously` take care of those things in the near future. That would be really nice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135018824):
@**Kevin Buzzard** I am going to rewrite the rest of the Spa file with this new setup, and then you can expect another PR.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019272):
You should define `Spa.is_continuous`, as both a way to eliminate the coercion in the middle and also to indicate that this is an invariant property

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019393):
@**Kevin Buzzard**  https://github.com/kbuzzard/lean-perfectoid-spaces/pull/21

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019437):
@**Mario Carneiro** Yes, we could do that. But then you prove that continuity is an invariant property, but you don't prove this for the other conditions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019444):
I think we could indeed rewrite it into `v \in (Cont A)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019519):
I think that all the definitions on Spa should be invariant, since it is morally a quotient, even though your canonical representative means you don't strictly speaking need to be invariant when you don't want to

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019603):
@**Mario Carneiro** Sure, but should they be invariant because *we* know they are (a proof exists), or because *Lean* knows they are?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019668):
https://github.com/kbuzzard/lean-perfectoid-spaces/blob/ba77b91b6108cfa3f6327fb49cd9dbe903452201/src/Spa.lean#L11-L12 now says
```lean
definition Spa (A : Huber_pair) : set (Spv A) :=
{v | (v ∈ Cont A) ∧ ∀ r, r ∈ A⁺ → v r ≤ 1}
```
That's almost literally what Wedhorn writes! (I'm so happy :lol:)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019670):
we know they are, and we tell lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019677):
Cool

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019688):
Do you have a good suggestion on how to do that, without ruining all our nice readable formulas?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019731):
I don't really see how.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019740):
the theorems will look reasonably nice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019753):
`P (Spa.mk v) <-> P' v` where `P` and `P'` are properties on `Spa` and `valuation` respectively

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019812):
i.e. `Spa.mk v ∈ Cont A <-> v.is_continuous`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019850):
I see. And you just state those theorems. But they don't appear in the definitions of `Spa` and `basic_open` etc...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019898):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019904):
you might want to set them up as simp lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019907):
How would you name these?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019910):
`Spa.sound` and `basic_open.sound` etc?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019916):
`Spa.mk_mem_Cont`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019928):
`sound` is a specific property of quotients that I don't think has come up yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019934):
`v \equiv v' -> Spa.mk v = Spa.mk v'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019976):
I see. Should I prove that one?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019977):
I guess so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019980):
yes, I don't think it follows from the other stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019986):
How about `basic_open.well_defined`?
```lean
definition basic_open (r s : A) : set (Spa A) :=
{v | v r ≤ v s ∧ v s ≠ 0 }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135019988):
but it's pretty trivial given what you know about the minimal valuation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135020001):
`Spa.mk v \in basic_open r s <-> v r ≤ v s ∧ v s ≠ 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135020011):
note that the stuff on the right is not the same as what was in the set builder

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 02 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135020058):
I'd call it `mk_mem_basic_open`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135020223):
Ok, I see.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135022593):
@**Mario Carneiro** Next problem :lol: :
```lean
definition basic_open (r s : A) : set (Spa A) :=
{v | v r ≤ v s ∧ v s ≠ 0 }

lemma mk_mem_basic_open {r s : A} {v : Valuation A} : mk v ∈ basic_open r s ↔ v r ≤ v s ∧ v s ≠ 0 := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135022595):
It is unhappy about the `\in`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135022643):
Because `mk v` lives in `Spv A` and now `Spa A` is a subtype of `Spv A`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135022651):
Should I just create a `has_mem (Spv A) (Spa A)`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 02 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135022652):
you mathematicians always making identifications

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135022668):
Well, it brought us quite far. We're still ahead of the formalisation community...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135022673):
I agree we had a couple thousand years head start

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135023984):
Does this make sense. Or is it evil?
```lean
instance set_Spa_has_mem_Spv {A : Huber_pair} : has_mem (Spv A) (set (Spa A)) :=
⟨λ v S, dite (v ∈ Spa A) (λ h, (⟨v, h⟩ : Spa A) ∈ S) (λ _, false)⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135024077):
why not using the `if h : v ∈ Spa A then (⟨v, h⟩ : Spa A) ∈ S else false` syntax?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 02 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135024083):
This is so much easier to read

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135024789):
You are right. But in the end I think we shouldn't do this anyway. It might be better to just carry the `h : v ∈ Spa A` around.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135025390):
@**Kevin Buzzard** Ok, I pushed one more commit. I'm really happy about this now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 02 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135025395):
Thanks for letting me know Johan.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 02 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135025396):
And thanks a lot for your work on this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 02 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135038909):
@**Kevin Buzzard** Oops. There was a silly tiny bug left. I opened a new PR. It also deletes the file `valuation_universes` because that is now merged into the other files.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 04 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135155301):
```quote
Now stop kidding: where is our sheaf theory?
```
If module refactoring and completion of rings and integral closure were all done, and I had the time to write some more code myself, my *first question* would be: "Am I supposed to prove that a projective limit of complete topological rings is a complete topological ring? If so, should I just prove it from first principles? Or am I supposed to be waiting for some sort of category-theoretic knight in shining armour to come and whisk me away, and he'll tell me it's OK because the category of complete topological rings is known to have all limits by some sort of magic?" This is the first question I do not know the answer to.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135155572):
If the knight in shining armour exists I would definitely suggest waiting for him.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135155574):
Let's ping him then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135155575):
@**Scott Morrison|110087** ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135155578):
And @**Reid Barton**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135155580):
sure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135155635):
but that knight might be sleeping

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135155817):
In the mean, let me say that I wrote https://gist.github.com/PatrickMassot/7b2576129e7f7b61d328f7fb10d5214d yesterday night. I still need some cleanup in the general stuff, but mostly it needs to be rewritten multiplicatively put through the `to_additive` machine, and then see how much this can be reused for rings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135155875):
But today I have six math talks to attend

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135155905):
Ouch. Good luck!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135155953):
And thanks for that gist! Sweet progress

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135155971):
It's our research group official academic year kick off. All those talks are given by new members (one permanent and many post-docs). It's hard to skip since I'm the new head of the group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135156017):
Well, in that case: enjoy!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135156049):
Maybe I should ping @**Johannes Hölzl** about that gist: it's not yet push-ready but you can already have a look. My plan is to put everything before groups into `continuity.lean`, and the end into `topological_structure.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135156111):
I should also point out something weird: I cannot `open quotient_add_group` at the beginning of the file, or even one declaration earlier, Lean complains that's an invalid name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135156126):
`lemma quotient_group_saturate` would go in `quotient_group.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 04 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135156581):
The gist looks good to me. I guess for the `is_open_map.prod` it would help to express `is_open_map` in terms of neighborhoods:
`∀(a:α) (U ∈(nhd a).sets), f '' U ∈(nhd (f a)).sets`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135159185):
@**Kevin Buzzard** When Wedhorn says that a ring is *adic*, this just means that there exists an ideal $$I \subset A$$ such that the topology on $$A$$ is the $$I$$-adic topology. Is that right? Maybe it includes the condition that $$I$$ is finitely generated?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135159205):
I am looking at Wedhorn's lemma 6.2, and wondering if (i) => (ii) is `rfl`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135159250):
In the proof he says that implication is trivial. But you never know if that actually means `rfl` (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 04 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135160986):
```quote
@**Kevin Buzzard** When Wedhorn says that a ring is *adic*, this just means that there exists an ideal $$I \subset A$$ such that the topology on $$A$$ is the $$I$$-adic topology. Is that right? Maybe it includes the condition that $$I$$ is finitely generated?
```
It's definition 5.18 and yes, there appears to be no finitely-generated condition here. But for Huber rings (a.k.a. f-adic rings) there is a finite generation condition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 04 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135161884):
```quote
If the knight in shining armour exists I would definitely suggest waiting for him.
```
I am still unclear about how this is working. Module refactoring, completion of rings, integral closure, I understand exactly what needs to be done and who is doing it. I am in no hurry (although I know Patrick is; I am using module refactoring as an excuse to concentrate on other projects at the minute, e.g. informal documentation for mathematicians which I am actually now writing and which needs to be done because my course started today). But projective limit of complete rings is a complete ring has some content, there is as far as I know not some magic category theory button which proves this. If Scott is intending to actually do this work then great -- but I had not picked up on this as one of his plans. @**Patrick Massot** is an arbitrary product of complete topological rings complete, and is a closed subring of a complete topological ring complete? That's what we need. This whole completion thread terrifies me. I had no idea it was going to be so subtle. Unlike Patrick I have not engaged with the mathematics involved here at all. My huge summer project is over and I am not yet clear on how much time I will have for Lean this term, but I am hoping that I can contribute more in the near future.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 04 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135165309):
I have no plan to magically produce projective limits of complete rings for you. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 04 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135165405):
Hopefully in a PR or two mathlib will have the language to _say_ in a uniform way that something is a limit of some other thing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 04 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135165458):
But as far as I'm aware there's no magic to produce that limit in this case. (The limit of rings is trivial, and will be an example, but I'll leave to someone else the case of complete rings.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 04 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135192953):
I think you should prove first that complete topological rings form a reflective subcategory of topological rings. You already need the reflector--this is the completion of a topological ring. Then you also need its universal property: a continuous ring homomorphism from a topological ring A to a complete topological ring B factors uniquely through the completion of A (you might need this anyways as well).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 04 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135192970):
Then, it follows by general nonsense that complete topological rings have the same limits as topological rings, and that case I think is best to just do by hand.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 04 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135199578):
Reid I always enjoy your comments -- they are often very insightful. Yes I'm sure we need universal property of completions. What's happening here is that it's a bit like defining the structure sheaf on an affine scheme. If R is a ring and f in R then we want the structure sheaf on the D(f) of Spec(R) (the points where f doesn't vanish) to be R[1/f], and then we extend to all opens using that D(f) form a basis and we constantly need universal property of localisation. Here it's a very similar story, we're defining a presheaf on Spa(A) which is some modification of Spec(A) for A a topological ring, there are "special" open sets for which the structure presheaf is "localise and then complete", and then for general open sets it's "take limits", but to define all the morphisms you constantly have to use universal property of localisation and then universal property of completion. I didn't know enough of this abstract nonsense to know that the notion of a reflective subcategory could help.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135201442):
I'm back. Of course we (almost) have that "reflector". I didn't know the terminology, but this is what we have been very slowly building since July, and indeed this is not formal. The question is: can we plug this into the category theory repository stuff to get the formal consequences for free

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135201580):
```quote
Hopefully in a PR or two mathlib will have the language to _say_ in a uniform way that something is a limit of some other thing.
```
Can we already have your repo as a dependency and use that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135203616):
```quote
The gist looks good to me. I guess for the `is_open_map.prod` it would help to express `is_open_map` in terms of neighborhoods:
`∀(a:α) (U ∈(nhd a).sets), f '' U ∈(nhd (f a)).sets`.
```
Using that reformulation leads to the proof:
```lean
  rw is_open_map_iff_nhds at *,
  rintro ⟨a, c⟩ U U_nhd,
  rw [nhds_prod_eq, filter.mem_prod_iff] at U_nhd,
  rcases U_nhd with ⟨s, s_in, t, t_in, h⟩,
  apply filter.sets_of_superset _ _ (image_subset (λ (p : α × γ), (f (p.fst), g (p.snd))) h),
  rw [←prod_image_image_eq, nhds_prod_eq],
  exact filter.prod_mem_prod (hf a s s_in) (hg c t t_in)
```
I'm not sure if it's really an improvement

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135203631):
It's shorter but less natural for the average mathematician

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135204356):
And I proved your lemma:
```lean
lemma is_open_map_iff_nhds (f : α → β) : is_open_map f ↔ ∀(a:α) (U ∈(nhds a).sets), f '' U ∈(nhds (f a)).sets :=
begin
  split,
  { intros H a U U_nhd,
    rw mem_nhds_sets_iff at *,
    rcases U_nhd with ⟨s, s_sub, ⟨s_op, a_in_s⟩⟩,
    existsi [f '' s, image_subset _ s_sub],
    exact ⟨H s s_op, mem_image_of_mem _ a_in_s⟩ },
  { intros H U U_op,
    rw is_open_iff_mem_nhds,
    rintros b ⟨a, a_in, fa⟩,
    rw ←fa,
    exact H _ _ (mem_nhds_sets U_op a_in) }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135204389):
Ten minutes to Lean this, without writing a proof on paper first. I may end up comfortable with this filter non-sense!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 04 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135206249):
Hm, I was a little bit off with my nhds version of `is_open_map`. It can expressed directly using `filter.map`:
```lean
lemma is_open_map_iff_nhds_le (f : α → β) : is_open_map f ↔ ∀(a:α), nhds (f a) ≤ (nhds a).map f :=
begin
  rw [is_open_map_iff_nhds],
  refine forall_congr (assume a, _),
  split,
  exact assume h s hs, let ⟨t, ht, hts⟩ := filter.mem_map_sets_iff.1 hs in
    filter.mem_sets_of_superset (h t ht) hts,
  exact assume h u hu, h (filter.image_mem_map hu)
end

protected lemma prod {f : α → β} {g : γ → δ} (hf : is_open_map f) (hg : is_open_map g) :
  is_open_map (λ p : α × γ, (f p.1, g p.2)) :=
begin
  rw [is_open_map_iff_nhds_le],
  rintros ⟨a, b⟩,
  rw [nhds_prod_eq, nhds_prod_eq, ← filter.prod_map_map_eq],
  exact filter.prod_mono ((is_open_map_iff_nhds_le f).1 hf a) ((is_open_map_iff_nhds_le g).1 hg b)
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 04 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135206477):
I think this is similar to you wanting to write `is_ideal` using sets and functions, instead of points. Its the same with filters!
Many things can be nicely expressed using `map` or `comap` and `<=`. Using this operators we don't need to handle points (i.e. sets)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135211096):
I've been betrayed! I copied you statement without thinking. But of course this is consistent with how the open set definition relates to the continuity definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135211104):
Of course I also prefer set-free filter reasoning

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135211133):
Oh, I could tfae it!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135213439):
```quote
```quote
Hopefully in a PR or two mathlib will have the language to _say_ in a uniform way that something is a limit of some other thing.
```
Can we already have your repo as a dependency and use that?
```
It is already a dependency since a week or so.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135213464):
I understand, but is it actually usable for us, or half incompatible with what is in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135213590):
I think the stuff on limits should be mostly compatible with what is in mathlib. But I don't know for sure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135213619):
Do you know how to state that the category of topological rings has projective limits?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135213662):
Well, we would first need a category of topological rings.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135213751):
```quote
It looks like `TopRing.lean` itself compiles fine :-)
```
Aah, Scott already wrote that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135213793):
I'm always confused about Scott's repositories because I was never able to find the pieces of sheaf theory that he showed us in Orsay

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135213850):
And then we would need to use: https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/limits/limits.lean#L82

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135213945):
@**Patrick Massot** Do you mean things like this: https://github.com/semorrison/lean-category-theory/blob/6c2a7b340f19bf0da3f1904204791c343d5c3213/src/category_theory/sheaves.lean#L32

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135213983):
Oh I was looking in the presheaf file!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135214001):
while are stalks in sheaves and not presheaves?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135214015):
https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/examples/rings/universal.lean#L43 is sorried :sad:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135214106):
Right. But colimits are quite a bit harder... you need tensor products.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135214116):
I know we have those. But you still need to use them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135214118):
It's not as formal as limits.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135214134):
but stalk is a colimit, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135214139):
Aaah, sure, it is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135214184):
So you mean we don't have stalks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 04 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135214198):
Hmm... work to do (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135215398):
```quote
Oh, I could tfae it!
```
Doesn't work:
```lean
lemma is_open_map_iff (f : α → β) : tfae [is_open_map f, 
  ∀(a:α), nhds (f a) ≤ (nhds a).map f, ∀(a:α) (U ∈(nhds a).sets), f '' U ∈(nhds (f a)).sets] :=
begin
  tfae_have : 1 → 3,
  { intros H a U U_nhd,
    rw mem_nhds_sets_iff at *,
    rcases U_nhd with ⟨s, s_sub, ⟨s_op, a_in_s⟩⟩,
    existsi [f '' s, image_subset _ s_sub],
    exact ⟨H s s_op, mem_image_of_mem _ a_in_s⟩ },
  tfae_have : 3 → 1,
  { intros H U U_op,
    rw is_open_iff_mem_nhds,
    rintros b ⟨a, a_in, fa⟩,
    rw ←fa,
    exact H _ _ (mem_nhds_sets U_op a_in) },
   tfae_have : 3 ↔ 2,
   { refine forall_congr (assume a, _),
     split,
     exact assume h s hs, let ⟨t, ht, hts⟩ := filter.mem_map_sets_iff.1 hs in
       filter.mem_sets_of_superset (h t ht) hts,
     exact assume h u hu, h (filter.image_mem_map hu) },
   tfae_finish,
end
```
The `tfae_finish` errors like:
```
α : Type u_1,
_inst_1 : topological_space α,
β : Type u_2,
_inst_2 : topological_space β,
f : α → β,
tfae_1_to_3 : is_open_map f → ∀ (a : α) (U : set α), U ∈ (nhds a).sets → f '' U ∈ (nhds (f a)).sets,
tfae_3_to_1 : (∀ (a : α) (U : set α), U ∈ (nhds a).sets → f '' U ∈ (nhds (f a)).sets) → is_open_map f,
tfae_3_iff_2 :
  (∀ (a : α) (U : set α), U ∈ (nhds a).sets → f '' U ∈ (nhds (f a)).sets) ↔
    ∀ (a : α), nhds (f a) ≤ filter.map f (nhds a)
⊢ tfae  [is_open_map f, ∀ (a : α), nhds (f a) ≤ filter.map f (nhds a), ∀ (a : α) (U : set α), U ∈ (nhds a).sets → f '' U ∈ (nhds (f a)).sets]

exact tactic failed, type mismatch, given expression has type
  (∀ (a : α), nhds (f a) ≤ filter.map f (nhds a)) ↔ ∀ (a : α), nhds (f a) ≤ filter.map f (nhds a)
but is expected to have type
  (∀ (a : α), nhds (f a) ≤ filter.map f (nhds a)) ↔ is_open_map f
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 04 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135215405):
time to sleep

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135229951):
@**Simon Hudon**  :up: Do you know what we did wrong? I succesfully used `tfae` in another example today.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 05 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135235526):
What do I need to import for that example?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135235777):
4 entire projects? :lol:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135235788):
Lol, just kidding.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135235789):
This doesn't depend on the perfectoid project in any way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135235843):
I guess `analysis/topology/embedding.lean` or something. I don't really know. You need to get `is_open`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135235845):
So you will need some topological files.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135237511):
The proof of 6.1 and 6.2 in Wedhorn is one big mess.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135237798):
Do we need those?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135237824):
If the proof is really messy, you will probably be faster if you fist LaTeX a precise organized proof, and then Lean it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135237871):
Right. I don't know exactly if we need them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135237873):
I thought they belonged to the api of Huber and Tate rings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135237884):
I'll dig in a bit deeper.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135237935):
What is this Remark 6.3? Does it mean all top rings we actually care about are metrizable?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135238026):
Yes, I think so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135238030):
Is that good or bad news?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135238239):
Is this actually ok?
```lean
class perfectoid_space (X : Type*) extends adic_space X :=
(perfectoid_cover : ∀ x : X, ∃ (U : opens X) (A : Huber_pair) [perfectoid_ring A],
  (x ∈ U) ∧ is_preadic_space_equiv U (Spa A))
```
We ask for a `A : Huber_pair` to exist, and then also for the structure `perfectoid_ring A`. But we don't ask for any sort of compatibility between those...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135238703):
sounds very fishy. It looks like the issue discussed about Hilbert spaces last summer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135238893):
Also, in
```lean
/-- A perfectoid ring, following Fontaine Sem Bourb-/
class perfectoid_ring (R : Type*) extends Tate_ring R :=
(complete : is_complete R)
(uniform  : is_uniform R)
(ramified : ∃ ϖ : units R, (is_pseudo_uniformizer ϖ) ∧ ((ϖ^p : R) ∣ p))
(Frob     : ∀ a : Rᵒ, ∃ b : Rᵒ, (p : R) ∣ (b^p - a))
```
I think we want the $$\varpi$$ not to just exist, but to actually be the one that comes with the `Tate_ring` structure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135239028):
I can hear Assia laughting...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135239040):
Hmmm... I'm not sure if top-down vs bottom-up is at issue here. Although it is certainly related.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135239044):
The issue seems to be that we don't have examples.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135239049):
@**Kenny Lau** Where are our algebraic closures?!!!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135239050):
Yes, that's what she predicted

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135239051):
(Kidding)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135239093):
somewhere... over the rainbow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 05 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135239164):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/stacks.20project.20.2F.20schemes/near/123090992

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 05 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135239378):
Thanks for that link @**Patrick Massot**. It was from the time where I hadn't really started using Lean yet. I think Assia's comment is extremely valuable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135243624):
I am writing a blog post with an update on the perfectoid project and related things. I was not going to mention modules at all, I was going to focus on the issues which the "completion of a topological ring" API has run into. I don't think that mathematicians even understand that these issues are there. This whole thing has been very eye-opening.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135243700):
On writing it I realise that I am interested in the question of whether we have the predicate `is_complete R` for `R` a commutative topological ring.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135243818):
I have been reluctant to embark upon definition of the presheaf on Spa(A) because (a) I was super-busy, as yesterday was lecture 1 of my course and meeting 1 of Xena and (b) I knew that after this unexpected (to me -- probably not to Johannes!) hold-up regarding completions of top rings it would mean that I would have to sorry stuff when doing the last part, and I have this vague idea that sorrying stuff is bad.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135244014):
I have this vague idea that to prove the thing I need (the universal property for projective limits in the category of complete topological rings) I would probably need what Patrick is doing. But now I am realising that if you think about the notion of being complete (for a topological ring) as just being some typeclass `is_complete` then I think the third thing can be thought of as an `instance`, and now I realise that I am a little unclear about whether I could just attempt to write this instance in a completely sorry-free way if I just had the definition of the predicate `is_complete R` for `R` a topological ring.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135244065):
Should predicates like `is_complete` be typeclasses? @**Johannes Hölzl** you always seem to have clear ideas on things like this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135244071):
@**Reid Barton**  points out that they form a reflective subcategory.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135245115):
@**Patrick Massot** Is there a full proof of the universal property of the completion of a topological ring in the mathematical literature?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135245284):
i.e. if C is a complete topological ring then Hom(M, C) = Hom(completion(M), C)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135245818):
Right.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135245830):
Of course you have to define the completion first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135245873):
but my understanding now is that defining the completion and proving the universal property is in some sense one problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135245905):
and then the trick of deducing that projective limits in the category of complete topological rings exist by showing that projective limits exist in the category of topological rings is a totally different problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135245967):
and might be approachable using some category-theory magic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 05 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135248850):
we have already `complete_space` which is a type class, a predicate on uniform spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135494373):
I'm almost done with https://github.com/kbuzzard/lean-perfectoid-spaces/blob/huber_tate/src/Spa.lean#L193
It proves that rational opens form a basis.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135494387):
But first I will sleep a bit.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135494390):
Nice Johan!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 09 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135495188):
Good job!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 09 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135495258):
what is rational?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135495325):
It's some version of $$D(f)$$ for adic spaces.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135495429):
Definition 7.29 p62 of https://www2.math.uni-paderborn.de/fileadmin/Mathematik/People/wedhorn/Lehre/AdicSpaces.pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135512569):
There is one annoying subgoal left:
```lean
A : Huber_pair,
U₁ U₂ : set ↥(Spa A),
v : ↥(Spa A),
hv : v ∈ U₁ ∩ U₂,
s₁ : ↥A,
T₁ : set ↥A,
hfin₁ : fintype ↥T₁,
s₂ : ↥A,
T₂ : set ↥A,
hfin₂ : fintype ↥T₂,
_inst : fintype ↥T₁,
_inst_1 : fintype ↥T₂,
H₂ : U₂ = rational_open s₂ (insert s₂ T₂),
H₁ : U₁ = rational_open s₁ (insert s₁ T₁)
⊢ fintype
    ↥{t :
         ↥A | ∃ {t₁ : ↥A} {H : t₁ ∈ insert s₁ T₁} {t₂ : ↥A} {H : t₂ ∈ insert s₂ T₂},
         t = t₁ * t₂}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135512572):
Does anyone have some hints on how to tackle that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135512741):
I want to use `set.fintype_image` but it doesn't apply directly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135512946):
Use choice to turn the goal back into `finite ...`, and then use `finite_subset` and `finite_image`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135512960):
actually you can use `fintype_subset` instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135513096):
You should be able to prove `fintype (uncurry (*) '' set.prod (insert s₁ T₁) (insert s₂ T₂))`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135513106):
Ok, I can try that one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 04:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135513196):
actually I don't even think you have to prove that, typeclass inference will solve it... you just have to prove your set is a subset of it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 04:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135513204):
(in fact it's equal but who cares)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135513493):
@**Mario Carneiro** I'm now stuck with this kludge:
```lean
    { haveI : fintype {p : A × A | p.1 ∈ (insert s₁ T₁) ∧ p.2 ∈ (insert s₂ T₂)} :=
      begin
        sorry
      end,
      convert set.fintype_image
        {p : A × A | p.1 ∈ (insert s₁ T₁) ∧ p.2 ∈ (insert s₂ T₂)}
        (λ p, p.1 * p.2),
      funext t,
      ext, split,
      { rintros ⟨t₁, ht₁, t₂, ht₂, H⟩,
        existsi (⟨t₁,t₂⟩ : A × A),
        split, exact ⟨ht₁, ht₂⟩, exact H.symm },
      { rintros ⟨p, ⟨h₁, h₂⟩⟩, dsimp at h₂,
        exact ⟨(p.1 : A),h₁.left,(p.2 : A),h₁.right, h₂.symm⟩ } },
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135513497):
I don't feel like I'm doing this the right way...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135513498):
you should use `set.prod` for that set abstraction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135513500):
The `uncurry` didn't work, because Lean could figure out `has_insert` classes...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135513505):
then lean will be able to fill in the sorry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135513547):
if lean has trouble with the has_insert class, put a type ascription on it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135513549):
`uncurry (*) '' set.prod (insert s₁ T₁ : set A) (insert s₂ T₂ : set A)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135513572):
Hurray:
```lean
    { convert set.fintype_image
        (set.prod (insert s₁ T₁) (insert s₂ T₂))
        (λ p, p.1 * p.2),
      funext t,
      ext, split,
      { rintros ⟨t₁, ht₁, t₂, ht₂, H⟩,
        existsi (⟨t₁,t₂⟩ : A × A),
        split, exact ⟨ht₁, ht₂⟩, exact H.symm },
      { rintros ⟨p, ⟨h₁, h₂⟩⟩, dsimp at h₂,
        exact ⟨(p.1 : A),h₁.left,(p.2 : A),h₁.right, h₂.symm⟩ } },
    apply rational_open_inter; simp },
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135513614):
Still silly that I need 10 lines for this. But at least it is `sorry`-free now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135513618):
Like I said, use `fintype_subset` instead of `convert` and one of your proof obligations goes away

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135513636):
I'll look into that after I catchup some sleep. Thanks again!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135513688):
Also the reason this is work is because you "rolled your own" set abstraction rather than composing existing constructions so that you get something "manifestly finite". I would question why you had that goal to prove in the first place

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135515107):
I pushed some more finiteness theorems to allow you to write `(*) <$> insert s₁ T₁ <*> insert s₂ T₂` and have lean automatically figure out this is finite

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135520406):
```quote
I pushed some more finiteness theorems to allow you to write `(*) <$> insert s₁ T₁ <*> insert s₂ T₂` and have lean automatically figure out this is finite
```
@**Kevin Buzzard** @**Patrick Massot** @**Scott Morrison|110087** What do you think of such notation? Is this something we should just get used to, or are we deviating too much from the maths we are formalising if we do that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 10 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135520525):
What are the alternatives on offer?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135521990):
I am using `{t : A | ∃ {t₁ ∈ insert s₁ T₁} {t₂ ∈ insert s₂ T₂}, t = t₁ * t₂}` at the moment.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522001):
The problem with what I am currently using is that it is readable, and therefore unstructured.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522007):
You wouldn't even use this in regular maths

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522010):
you would give that thing a name/notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522060):
The advantage of the monad notation is that it is ridiculously general

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522061):
Nope, we definitely write `{t_1 * t_2 | t_1 \in T_1, t_2 \in T_2}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522068):
Not A * B?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 10 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522077):
I would write something like $$\{t\in A\mid \exists t_1\in \{s_1\}\cup T_1, t_2\in \{s_2\}\cup T_2 \mathrm{\ such\ that\ }t=t_1t_2\}$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522083):
I still don't believe you. You might write that on line 1 but you would never write it twice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 10 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522131):
Fair point.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 10 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522140):
My brain can't cope with two conventions for typing maths notation into a computer :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522208):
I write `\cup` in lean too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522209):
@**Mario Carneiro**, right. So we use `let T := blah`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522211):
And if you did write it that way, you would also have to explain (briefly) why it is finite

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522213):
But in this `let`, we definitely use the unstructured set builder notation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522214):
and in doing so you would identify it as an image

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522233):
```quote
And if you did write it that way, you would also have to explain (briefly) why it is finite
```
No we don't. It's done by an auto_param that calls `this_is_easy`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522234):
I'm thinking math textbook level here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522236):
I'm not sure what level you are talking

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522295):
Same level

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522298):
I can believe that a mathematician proof would skip this step, maybe using "by clearly", but I think they would also recognize it as skipping a step and would use images when asked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522347):
(as opposed to some step skippage which are not even recognized as such when considered explicitly)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522349):
Sure. So can I just tell Lean `work_harder [use := it_is_an_image]` ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522350):
Instead of a 10-line proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522357):
Sure, I mean at this point we are talking about machine learning or other ATP to prove this theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522366):
All the pieces are there, go find it computer minion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522367):
I want an ATP inside my ITP.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522415):
but my point is there is also a notation for this, and I want to maximize use of "constructions" for building sets because this provides a focus for theorems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522431):
Ok, I'll just use it and see what happens. I prefer the version with `uncurry`. Is that structured enough? Or do I need the crazy monadic combinators?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522437):
the advantage of the funny monadic version is you don't have to fuss with products

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522479):
which is a side effect of the fact that (*) is a curried function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522496):
Ok, I'll bite the bullet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522498):
Unfortunately, even the funny monad version isn't exactly the same as your set notation up to defeq

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522543):
because it uses `⋃ x ∈ s` instead of `{y | ∃ x ∈ s, ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522548):
which is not defeq because of reasons

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522555):
still, you should be able to prove it by simp

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522625):
@**Mario Carneiro** I don't like the look of this
```lean
⇑v (t₁ t₂) ≤ ⇑v (s₁ * s₂)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522635):
All of a sudden `t₁` is a function `A → A`...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522637):
what am I looking at?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522655):
```lean
lemma rational_open_inter.aux1 {s₁ s₂ : A} {T₁ T₂ : set A} [fintype T₁] [fintype T₂] (h₁ : s₁ ∈ T₁) (h₂ : s₂ ∈ T₂) :
let T := (*) <$> T₁ <*> T₂ in
rational_open s₁ T₁ ∩ rational_open s₂ T₂ ⊆ rational_open (s₁ * s₂) T :=
begin
  intros T v h,
  have vmuls : v (s₁ * s₂) = v s₁ * v s₂ := valuation.map_mul _ _ _,
  split,
  { intros t ht,
    rcases ht with ⟨t₁, ht₁, t₂, ht₂, ht⟩,
    rcases h with ⟨⟨hv₁, hs₁⟩, ⟨hv₂, hs₂⟩⟩,
    subst ht,
--- snip, the goal is now
A : Huber_pair,
s₁ s₂ : ↥A,
T₁ T₂ : set ↥A,
_inst_1 : fintype ↥T₁,
_inst_2 : fintype ↥T₂,
h₁ : s₁ ∈ T₁,
h₂ : s₂ ∈ T₂,
T : set ↥A := has_mul.mul <$> T₁ <*> T₂,
v : ↥(Spa A),
vmuls : ⇑v (s₁ * s₂) = ⇑v s₁ * ⇑v s₂,
t₁ : ↥A → ↥A,
ht₁ : t₁ ∈ has_mul.mul <$> T₁,
t₂ : ↥A,
ht₂ : t₂ ∈ T₂,
hv₁ : ∀ (t : ↥A), t ∈ T₁ → ⇑v t ≤ ⇑v s₁,
hs₁ : ⇑v s₁ ≠ 0,
hv₂ : ∀ (t : ↥A), t ∈ T₂ → ⇑v t ≤ ⇑v s₂,
hs₂ : ⇑v s₂ ≠ 0
⊢ ⇑v (t₁ t₂) ≤ ⇑v (s₁ * s₂)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522702):
I want it to be `v (t₁ * t₂) ≤ v (s₁ * s₂)`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522874):
I would like to understand how to use this goofy monad stuff. But currently I'm mystified. I think it is turning `t₁` into the function that multiplies on the left with the "old" `t₁ : A`. But now I can't use the multiplicative property of valuations on this expression...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522987):
Sorry, I was distracted by some poor simp lemmas that fail to simplify that expression the way you would want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522989):
you can fix the `t1` is a function thing by `rcases ht1 with <t1, ht1, rfl>`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135522995):
Ok, let me try.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135523336):
It seems to work. Thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135523396):
```
example {A : Type u} [has_mul A] (T₁ T₂ : set A) :
  {t : A | ∃ (t₁ ∈ T₁) (t₂ ∈ T₂), t = t₁ * t₂} = (*) <$> T₁ <*> T₂ :=
begin
  ext t, split,
  { rintro ⟨t₁, ht₁, t₂, ht₂, rfl⟩, exact ⟨_, ⟨_, ht₁, rfl⟩, _, ht₂, rfl⟩ },
  { rintro ⟨_, ⟨t₁, ht₁, rfl⟩, t₂, ht₂, rfl⟩, exact ⟨_, ht₁, _, ht₂, rfl⟩ }
end
```
We need a tactic for these kinds of "bracket reassociation" equivalences

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135524227):
@**Mario Carneiro** O.ooo....
```lean
⊢ fintype ↥(has_mul.mul <$> insert s₁ T₁ <*> insert s₂ T₂)
```
This isn't solved by `apply_instance`... Or do I need to pull latest mathlib for that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135524239):
latest mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Oct 10 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135524303):
```quote
We need a tactic for these kinds of "bracket reassociation" equivalences
```

Yes, we do!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135526582):
@**Mario Carneiro** Am I supposed to use
```lean
def fintype_seq {α β : Type u} [decidable_eq β]
  (f : set (α → β)) (s : set α) [fintype f] [fintype s] :
  fintype (f <*> s) :=
by rw seq_eq_bind_map; apply set.fintype_bind'

theorem finite_seq {α β : Type u} {f : set (α → β)} {s : set α} :
  finite f → finite s → finite (f <*> s)
| ⟨hf⟩ ⟨hs⟩ := by haveI := classical.dec_eq β; exactI ⟨fintype_seq _ _⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135526587):
type class search isn't proving the finiteness for me by itself...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135526589):
oh dear, that first `def` should be an `instance`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135526658):
eh, just put `attribute [instance] set.fintype_seq` in your file, I'll deal with it later

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135527597):
Is this a simp-lemma?
```lean
lemma rational_open_inter {s₁ s₂ : A} {T₁ T₂ : set A} [fintype T₁] [fintype T₂] (h₁ : s₁ ∈ T₁) (h₂ : s₂ ∈ T₂) :
let T := (*) <$> T₁ <*> T₂ in
rational_open s₁ T₁ ∩ rational_open s₂ T₂ = rational_open (s₁ * s₂) T := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135527663):
I don't think so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135527671):
I guess it depends on how you interpret `rational_open`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135527727):
but it isn't a simp lemma in the other direction, and unless you want intersections of rational opens to "compute" to another rational open this is a bit of a strange simp lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135527862):
Ok, I'll give it as data to `simp` when I need it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135527912):
also I'm not positive but the `let` might get in the way in rewrites

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135528071):
Yes, I removed the `let`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 10 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135528592):
Regarding "bracket reassociation": if the types actually uniquely constrain the answer, then telling `tidy` it's allowed to use either `assumption` or `solve_by_elim` will usually do it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 10 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135528646):
I guess you may also need to tell it it's allowed to case bash a bit too, to break apart the hypotheses. For hypotheses covered by `auto_cases` it should just work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135528670):
here the cases are all pairs and rfls

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 10 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135528716):
If you're talking about
```
example {A : Type u} [has_mul A] (T₁ T₂ : set A) :
  {t : A | ∃ (t₁ ∈ T₁) (t₂ ∈ T₂), t = t₁ * t₂} = (*) <$> T₁ <*> T₂ :=
begin
  ext t, split,
  { rintro ⟨t₁, ht₁, t₂, ht₂, rfl⟩, exact ⟨_, ⟨_, ht₁, rfl⟩, _, ht₂, rfl⟩ },
  { rintro ⟨_, ⟨t₁, ht₁, rfl⟩, t₂, ht₂, rfl⟩, exact ⟨_, ht₁, _, ht₂, rfl⟩ }
end
```
then `tidy` actually does it out of the box.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 10 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135528741):
producing the somewhat unhelpful proof:
```
ext1, dsimp at *, simp at *, fsplit, work_on_goal 0 { intros a, cases a, cases a_h, cases a_h_right, cases a_h_right_h, fsplit, work_on_goal 0 { intros a }, work_on_goal 1 { simp at *, fsplit, work_on_goal 0 { fsplit, work_on_goal 1 { fsplit, work_on_goal 0 { assumption }, refl } }, fsplit, work_on_goal 1 { fsplit, work_on_goal 0 { assumption }, simp at *, solve_by_elim } } }, intros a, cases a, cases a_h, cases a_h_h, cases a_h_w, cases a_h_w_h, cases a_h_h_h, induction a_h_h_h_h, induction a_h_w_h_right, fsplit, work_on_goal 1 { fsplit, work_on_goal 0 { assumption }, simp at *, fsplit, work_on_goal 1 { fsplit, work_on_goal 0 { assumption }, refl } }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Oct 10 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135528958):
If tidy is slow, and its output is ugly but much faster to compile, would it make sense to expand the tidy proofs but put some markings around them and tell vscode to fold them by default?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135529641):
```quote
```quote
I pushed some more finiteness theorems to allow you to write `(*) <$> insert s₁ T₁ <*> insert s₂ T₂` and have lean automatically figure out this is finite
```
What do you think of such notation? Is this something we should just get used to, or are we deviating too much from the maths we are formalising if we do that?
```
I think we need to learn how to use the power of this arcane thing. But of course I would prefer to hide this into obscure proofs of obvious facts rather than having it user-facing. But that opinion could change if suddenly some mathematician-oriented explanation appear.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 10 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135529842):
I must confess that I am absolutely with Patrick here. I've been using Lean for a year and I look at that line and I don't know what `<$>` or `<*>` mean. This is some cool monad trick? Don't have time to chase this up right now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135553331):
It is indeed some cool monad trick. As you know, `$` means application in lean, and `<$>` is a "lifting" operation on a function, that is, `(<$>) : (A -> B) -> F A -> F B`, so `<$>` turns a plain function into a function on the mapped objects. (This is just a functor operation on a morphism, so I doubt it requires much more explanation for a mathematician.)

`<*>` is similar, but in this case the function itself is wrapped in the functor. That is, `(<*>) : F (A -> B) -> F A -> F B`. This gives it a sort of behavior like binary product on the objects `F(-)`, except it deals with functions directly. Functors that have an operation like this are, reasonably enough, called applicative functors. (You can also axiomatize applicative functors using a pairing function `F A -> F B -> F (A x B)` plus the functor operation on objects and morphisms.)

Now the cool thing you can do by combining these two is lifting n-ary functions. If `f : A -> B -> C -> D` and `a : A`, `b : B` and `c:C` then of course `f a b c : D`, and you should parallel this with `f <$> a <*> b <*> c : F D` when `a : F A`, `b : F B`, `c : F C`. If you ignore the funny infix monad parts, it's just like `f a b c` except everything has been lifted across `F` (except the original function `f`, which is why the first symbol is `<$>` instead of `<*>`).

What does this have to do with sets? There is a natural functor instance on `set`, where the map function, of type `(A -> B) -> set A -> set B`, is the forward image of a set by a function. This has an applicative structure: recalling that we want a type `set (A -> B) -> set A -> set B`, the action of this operator is to apply all the functions to all the inputs and collect all the resulting outputs. That is, `fs <*> s = {y | ∃ f ∈ fs, ∃ x ∈ s, y = f x}`. When you apply this specifically to the case of lifting an n-ary function as above, you get `f <$> A <*> B <*> C = {y | ∃ (a ∈ A) (b ∈ B) (c ∈ C), y = f a b c}`, which is exactly what you would want by the mathematician's notation `f(A,B,C)` where `f` has been implicitly lifted to a set function. Here `<$>` and `<*>` are explicitly notating this lifting process.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135553602):
The downside of using this notation with `(*)` is that now it is no longer in infix position, which makes it a bit stranger to read and bunches up the symbols. It would have been nicer to have some kind of notation like `A <(*)> B` where the `*` stays in the middle but this is more ad hoc and also a bit notationally crazy still.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 10 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135554392):
Thank you Mario for the explanation! I was talking to an undergraduate over lunch today and I mentioned that I was surprised to find that I was needing to have to learn more and more category theory to do number theory properly in Lean, and a logician overheard me and she asked me if I was bad-mouthing category theory, and when I said I wasn't she said not to worry because at the end of the day it was all trivial anyway :-) I still somehow believe this -- it's just that I don't quite know enough of the language (e.g. applicative functor) to talk the talk yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135847266):
@**Kevin Buzzard** Would you mind taking a look at the Huber and Tate rings files? I think there is a definition of Huber ring that extends Tate ring. But it is not the one we currently use. Is this for a good reason, or should we change the definition of Huber ring?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 15 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135849476):
A Tate ring is a Huber ring plus an axiom (there exists a topologically nilpotent unit) [this is the definition in [Wedhorn](https://www2.math.uni-paderborn.de/fileadmin/Mathematik/People/wedhorn/Lehre/AdicSpaces.pdf) ]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 15 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135849657):
In `Huber_ring.lean` the subring and ideal are not part of the data of a Huber ring. The current definition of `Huber_ring` in the repo is a "Huber ring plus extra piece of data" and a Huber ring is a topological ring for which there exists S and J such that the axioms are true.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 15 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135849684):
The definition of `Tate_ring` which we have in `Tate_ring.lean` is from Scholze's [etale cohomology of diamonds](https://arxiv.org/abs/1709.07343) (beginning of section 3).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 15 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135849758):
The proof that it's a Huber ring in the sense we have defined it is that S is R_0 and J is (pi).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 15 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135849874):
actually that's not quite true -- pi might not be in R_0.  Maybe the easiest thing to say is S = R^o and J is (pi)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135850501):
Right, I was confused. So my question is: should `Tate_ring` extend `Huber_ring` and just only require the extra condition about the topologically nilpotent unit. Or do you want to leave the definitions as is? (Which means that the instance from `Tate_ring` to `Huber_ring` is non-trivial.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 15 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135850638):
How am I supposed to know? They're all the same mathematically. This is an implementation issue and I have no idea :-( Does it even matter?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135850701):
I get the impression that it is nice to have the `extend` keyword there (-; @**Mario Carneiro** @**Johannes Hölzl** Is there a general guideline for this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135850746):
@**Kevin Buzzard** Do we need both equivalent definitions of `Huber_ring`, or is 1 of them sufficient? I confess that I haven't looked deep enough into the theory to know the answer...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 15 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135850762):
So I spent the last couple of hours trying to figure out how close we are. There is still a way to go. Module refactoring is holding some stuff up but there is actually some other stuff we can do now -- to define the restriction maps on the presheaf is longer than I expected. See https://github.com/kbuzzard/lean-perfectoid-spaces/issues/25 . We need a random bunch of lemmas from section 7 (nothing looks hard but it might be a bit long :-( ) and also a lemma from an old paper of Huber.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 15 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135850808):
So where are these two definitions of Huber ring? I don't understand the question.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135850890):
Currently `Huber_ring` is defined in terms of rings of definitions. But it can also be defined as a bounded, complete ring with an adic topology. Is that right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 15 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135850949):
a Huber ring is not what it says in `Huber_ring.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 15 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135850971):
A Huber ring is a topological ring for which there exists S and J such that the axioms mentioned in the incorrect structure hold

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135851006):
Ok, I see. So what I mean is that there is Lemma 6.2 in Wedhorn.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135851014):
So we can choose one of those three equivalent properties as a definition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135851018):
One of them closely matches what is in `Tate_ring`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135851064):
And my question is: do we need all three. Or is 1 of them sufficient.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135851075):
I.e., do we need Lemma 6.2 or can we cut a corner there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 15 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135851126):
It would not surprise me if we need 6.2 at some point but we don't need it for the definition of a Huber ring.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135851230):
Ok. That answers my question. On my `huber_tate` branch I have proved some implications of 6.2. But the hard one (iii) -> (i) is not yet done.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 15 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135851292):
Are all proofs involving ideals going to break when module refactoring hits?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135851628):
You should ask the only one that knows :lol: @**Mario Carneiro** :up:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 15 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135851816):
Johan I know you were thinking about the sheaf on Spa(A). It's like schemes. For an affine scheme first you define the presheaf on a basis and then extend. When I was writing that stuff I would imagine that the extension really was some gadget which extended the earlier object. Now I would regard it as a completely different object.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 15 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135851840):
Hmm. Is there some fancy name for the relationship between the the category of presheaves on a basis and the category of presheaves on the whole space?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135852129):
You get a fully faithful functor from presheaves on a basis to presheaves on the whole space. And if you restrict this functor to sheaves on a basis, you get an equivalence to sheaves on the whole space.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 15 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135852201):
I tried to figure out if this was some sort of example of a morphism of sites. But that doesn't work out. I don't know if other abstract nonsense applies. I guess in the end some maintainer of mathlib might show up and suggest we formalise "pre-sites" and invent some new mathematics along the way :grinning_face_with_smiling_eyes: :upside_down:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135852310):
Yes, anything that makes any reference to modules or ideals will break, although the breakage is probably minor

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Michael Roberts (Oct 17 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135957292):
```quote
I tried to figure out if this was some sort of example of a morphism of sites. But that doesn't work out. I don't know if other abstract nonsense applies. I guess in the end some maintainer of mathlib might show up and suggest we formalise "pre-sites" and invent some new mathematics along the way :grinning_face_with_smiling_eyes: :upside_down:
```
What is usually called a 'morphism of sites' is to me far stronger than is necessary. The best definition I know is in MacLane and Moerdijk's book (https://ncatlab.org/nlab/show/Sheaves+in+Geometry+and+Logic) I'd have to look up the result, though.

Also note that sheaves on a site can be defined relative to a "coverage" (https://ncatlab.org/nlab/show/coverage) rather than a Grothendieck (pre)topology, and the underlying category of a basis of a topology on a space has a coverage (see https://ncatlab.org/nlab/show/coverage#Examples), such that the comparison functor to the category of open sets with the usual topology induces an equivalence on categories of sheaves.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Michael Roberts (Oct 17 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135957332):
So don't say "pre-sites", but "categories equipped with a coverage" and you will be alright wrt the category theory literature

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Michael Roberts (Oct 17 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135958401):
Actually, the best notion of a map between sites (or 'categories with coverage') inducing a map between sheaf categories would be in the Elephant (https://ncatlab.org/nlab/show/Elephant), I can track it down tomorrow at work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Michael Roberts (Oct 17 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135959843):
An important example in circles I move in is the category Cart whose objects are {R^n| n ≥0} and Cart(R^n,R^m) = C^\infty(R^n,R^m). This has a coverage whereby a family of maps u_i: R^n --> R^n is covering precisely when they all open embeddings and the image is all of the codomain. It's certainly *not* a Grothendieck (pre) topology!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 17 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135963362):
@**David Michael Roberts** Cool. That helps. We certainly need to define what a coverage is! I don't have a copy of the Elephant. But a reference would still be helpful.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Michael Roberts (Oct 17 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135964391):
https://ncatlab.org/nlab/show/coverage

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Michael Roberts (Oct 17 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135964399):
Ah, sorry, you meant define as in formally, and a reference for the map of sites result.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 17 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135964410):
Right. That page is also going to help me a lot! But I meant the other result.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Michael Roberts (Oct 17 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135964478):
For reference, Elephant C.2.1 is "Sites and coverages"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 17 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135964529):
Thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Michael Roberts (Oct 17 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135964645):
Remark 2.3.7 in Part C gives a definition of morphism of sites where the underlying categories may fail to have finite limits (so, for example, the poset of opens in a basis for a topology), dependent on Definition 2.3.1.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Michael Roberts (Oct 17 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135964708):
[Screen-Shot-2018-10-17-at-9.39.13-pm.png](/user_uploads/3121/rH_WHewJbvPBi9OomOBJOY0x/Screen-Shot-2018-10-17-at-9.39.13-pm.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Michael Roberts (Oct 17 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135964712):
[Screen-Shot-2018-10-17-at-9.40.02-pm.png](/user_uploads/3121/8MhB3RPWKTZ-m-uxF57hfAle/Screen-Shot-2018-10-17-at-9.40.02-pm.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 17 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135964797):
I had never realised that nLab had a different definition of *site* than I'm used to. TIL! :bulb:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Michael Roberts (Oct 17 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135964804):
[Screen-Shot-2018-10-17-at-9.42.16-pm.png](/user_uploads/3121/egI1m7Y5fw34odhWBTFVUBIT/Screen-Shot-2018-10-17-at-9.42.16-pm.png) 
[Screen-Shot-2018-10-17-at-9.42.35-pm.png](/user_uploads/3121/OiIH5Dic9MPk7EzR3aignuXl/Screen-Shot-2018-10-17-at-9.42.35-pm.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Michael Roberts (Oct 17 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135964818):
And that last stuff is from Mac Lane–Moerdijk VII.10

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Michael Roberts (Oct 17 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135964866):
Sorry, that's not what I meant to give you! Didn't read it properly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) David Michael Roberts (Oct 17 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/135964969):
Here's the real bit you need
[Screen-Shot-2018-10-17-at-9.45.38-pm.png](/user_uploads/3121/0ZJwc7aM2yIyLFMLKEa4XxpB/Screen-Shot-2018-10-17-at-9.45.38-pm.png) 
[Screen-Shot-2018-10-17-at-9.46.08-pm.png](/user_uploads/3121/5O0FDJQTKBKFj-QwJrxOSceA/Screen-Shot-2018-10-17-at-9.46.08-pm.png) 
(Handy having format-shifted backups of books that are on my shelf at work ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 28 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/136658083):
Should we delete [`for_mathlib/data/set/basic.lean`](https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/data/set/basic.lean)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 28 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/136658156):
and just how outdated is the rest of the `for_mathlib`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 28 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/136661108):
I don't have time to think about perfectoid stuff right now, but Kenny if you want to do some tidying then feel free -- I'd appreciate it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 28 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/136670419):
Kenny, do you mean the current content of that file has been merged in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 28 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/136670430):
yes: https://github.com/leanprover/mathlib/blob/a33ab1294b386f5fc6465b7221d48a052412bcd8/data/set/basic.lean#L953

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 28 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/136670470):
indeed it was part of the completion merge of course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 28 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/136670472):
so yes we can delete that one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 28 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/136670479):
and everything about completions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 28 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/136670483):
it's all merged upstream

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 28 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/136670556):
This has always been the plan. We could indeed have a big cleanup, but this is a bit pointless if nobody is working on the project. On the Lean front we are waiting for module and category theory refactor everywhere. And on the math side we are waiting for Kevin to have time, which won't happen soon.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 07 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/146942589):
Kenny, why don't you PR your cleanup to the perfectoid project?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 08 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/147288728):
@**Kenny Lau** :up:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 08 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/147288779):
I don't think I have cleaned up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 08 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/147288782):
Weren't removing lots of stuff that is now in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 03 2019 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/154271724):
@**Kevin Buzzard**  @**Johan Commelin**  Some news about perfectoid spaces: I-adic topology at https://gist.github.com/PatrickMassot/59c63e7d005350120d6a81f3a0276c87

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 03 2019 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/154271853):
It's a bit rough, some lemmas should be easier, I probably have a suboptimal setup. I builds on @**Johannes Hölzl** efforts starting at https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_groups.lean#L108

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 04 2019 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/154273293):
It's a nice idea to make `adic_ring I` definitionally equal to `R`. I am slowly but surely beginning to understand the ideas behind this trick. I knew that Lean could unify stuff well, and was under the impression for a while that definitionally equal types were "just equal", but it's more subtle than that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 04 2019 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/154417384):
I like how people are immediately making good use of `use` :grinning:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 04 2019 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/154417394):
It reads so much better than `existsi`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 04 2019 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/154421371):
four fewer characters, what's not to love

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 17 2019 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/155317920):
@**Kevin Buzzard** @**Patrick Massot**  I'm not so happy with the `decidable_eq` instances throughout `Huber_pair`. What do you think of adding a
```lean
local attribute [instance, priority 0] classical.prop_decidable
```
to the top of the file, so that the rest of the file can focus on actual mathematics?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/155317992):
What's the difference?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/155318005):
Actually I realise I don't even understand what's going on here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/155318024):
Does lean make different terms depending on whether you say h is decidable or everything is decidable including h?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 17 2019 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/155318025):
Readability. Mathematicians will gloss over that incantation in the header. But if they look at the definition of `Huber_pair`, and all of a sudden they see a condition `[decidable_eq R]`, they will think "What the hack is that doing there? That isn't in Wedhorn's text!".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/155318101):
I think I'm firmly in the "I don't care" camp

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/155318124):
I imagine it would be easy to change things later if the constructivists take over

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 17 2019 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/155320282):
I think we should hide this, as Johan suggests

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Neil Strickland (Jan 17 2019 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/155329632):
I have only glanced at the definitions, but it looks like no interesting example of a Huber ring will have constructive decidable equality.  If that's right, it seems more natural to have a global blanket assumption that you are going to use `classical.prop_decidable`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/155341505):
Whilst in theory one could consider non-complete Huber rings like $$\mathbb{Z}[T]$$ with the $p$-adic topology, the moment one does anything with Huber rings one assumes they're complete. I guess $$\mathbb{Z}_p$$ does not have decidable equality, and more generally I would imagine that only the most trivial of complete rings (like some finite rings) have decidable equality.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 17 2019 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/155345541):
what do you need decidability for?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 17 2019 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/155345704):
Polynomials

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 17 2019 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/155345714):
Because we need integral closures

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 17 2019 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/155346071):
yeah, that sounds pretty hopeless

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 17 2019 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfectoid%20spaces/near/155346150):
you can define polynomials in a way that doesn't need decidable eq, but you don't get algebraic closure or integral closure as such in constructive analysis

