---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/92147thingstoformalise.html
---

## Stream: [maths](index.html)
### Topic: [things to formalise](92147thingstoformalise.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 07 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131056409):
Dear all, I've dabbled with Lean about a year ago. I worked through _theorem proving with lean_ but I didn't go much beyond that. I would like to formalise some easy undergraduate maths just to get back in to it. Any recommendations? I was thinking of doing just some basic groups, ring theory or linear algebra. Last time I looked at Lean they didn't have a formalisation of the reals. Is that still the case? If the reals have been formalised then perhaps doing some simple real analysis. What active existing libraries should I look at for this kind of thing? I am aware of Xena and the official lean library repo.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131056440):
https://github.com/leanprover/mathlib/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131056445):
is the main place

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 07 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131056659):
thanks. I now realise I should have put this in #**new members**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131056737):
see also https://www.youtube.com/watch?v=5tS4j_A1ZvU

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131057164):
I hear from my undergrads that they are one lemma shy of proving det(AB)=det(A)det(B)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131057204):
There is still no definition of the derivative of a function so no chain rule or product rule

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131057291):
There is still no proof that a power series is continuous within its radius of convergence which is the main holdup for defining pi

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131057313):
The chain rule is waiting for the norms PR

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131057343):
What is the problem with the norms PR?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131057674):
Mario and Johannes want to work on it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131057680):
that's all I know

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 07 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131065103):
@**Kevin Buzzard** can you point me to the relevant files in mathlib for the power series proof please?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131065196):
I don't think power series are in mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131065209):
So most likely there is no particular file to point to.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131065405):
Hmm. Did @**Chris Hughes** 's work on the exponential function get accepted yet?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131065515):
no. I think it tries to become the most venerable PR in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131065602):
We are really bad at basic analysis. When Patrick says that the chain rule will come after normed spaces, he means the correct general chain rule for functions $$\mathbb{R}^a \to\mathbb{R}^b$$ but there's some hold-up with normed spaces that I'm not clear about. Johan might be right -- there might not even be a basic theory of power series in mathlib, although Chris must have done something because I'm pretty sure he defined $$x\mapsto e^x : \mathbb{C}\to\mathbb{C}$$. There was some hold-up with that PR as well -- I think that Mario and Johannes had different opinions about it and for a while at least we were just stuck in an impasse.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131065666):
Oh! Looking at the comments, it seems that people were concerned that the PR did not use enough filters :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131065875):
Come on Kevin. I mean functions between normed spaces, not  $$\mathbb{R}^a \to\mathbb{R}^b$$. And I don't mean finite dimensional

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131066937):
```quote
@**Kevin Buzzard** can you point me to the relevant files in mathlib for the power series proof please?
```
`data/real/cau_seq.lean` and `data/real/basic.lean` in mathlib are what seem to be the state of the art for sequences. I am not even sure that there is a theory of infinite sums in mathlib, although the definition of a convergent infinite sum (that the finite sums converge) could easily be put into mathlib; the thing is that the moment you put this in, you have to prove a whole bunch of lemmas. Over at the xena project we are a bit less fussy than mathlib, you can look at https://github.com/ImperialCollegeLondon/xena-UROP-2018/tree/master/src/chris_hughes_various/exponential to see some theorems about limits which aren't written in the language of filters and a whole bunch of unofficial theorems like sum of a geometric series written in what might not be the maximal generality.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131066961):
GT III.5

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 07 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/things%20to%20formalise/near/131067009):
That's how people in the arithmetic and algebraic geometry group talk in Orsay. Except they rather start with AC (yes they refer to the French version too)


{% endraw %}
