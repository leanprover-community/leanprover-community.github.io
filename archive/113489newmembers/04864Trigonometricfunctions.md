---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/04864Trigonometricfunctions.html
---

## Stream: [new members](index.html)
### Topic: [Trigonometric functions](04864Trigonometricfunctions.html)

---


{% raw %}
#### [ Sebastian Zimmer (Sep 29 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134883106):
I'd like to learn how to use lean, by attempting to prove something nontrivial. Looking through the potential projects wiki page, trigonometric functions seems like the most promising (in that I can confidently prove the basic identies, facts about pi, etc. from first principles).

I don't have much experience with theorem provers (I've used idris and coq in the past, but not terribly successfully).

The wiki links to some progress on the exponential function https://github.com/leanprover/mathlib/pull/41/commits/6b1f85b149329be0c9084081668230c2d622f387
but I can't tell if anything came of that.

* Does this seem feasible?
* What is the state of power series / exponential functions / trigonometric functions in mathlib?
* What would I build on top of? Are there other things in development that would be helpful to me?

#### [ Kevin Buzzard (Sep 29 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134883199):
There was a whole bunch of stuff formalised recently. I think we got exp, log, pi, sin, cos, tan

#### [ Kevin Buzzard (Sep 29 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134883200):
and double angle formulae etc. All of this is about a week old

#### [ Kevin Buzzard (Sep 29 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134883209):
Apparently we have cos(pi/2)=0 but we can only deduce that sin(pi/2)=+-1 ;-)

#### [ Sebastian Zimmer (Sep 29 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134883524):
Is that available in a public repo somewhere?

#### [ Chris Hughes (Sep 29 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134883587):
https://github.com/leanprover-community/mathlib/tree/exp

#### [ Sebastian Zimmer (Sep 29 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134883592):
awesome thanks

#### [ Sebastian Zimmer (Sep 29 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134884169):
It's surprising how much  you can prove without calculus

#### [ Johan Commelin (Sep 29 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134884522):
@**Chris Hughes** When will you PR `exp`? Is there some list of things you still want to add to it?

#### [ Chris Hughes (Sep 29 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134884529):
I still need sin(p/2)=1, and the inverses of all 14 functions

#### [ Chris Hughes (Sep 29 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134884530):
After that I'll PR it.

#### [ Sebastian Zimmer (Sep 29 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887265):
Just out of interest @**Chris Hughes** , how are you planning on proving sin(pi / 2) > 0? I can't see a way of doing it without a bit of calculus.

#### [ Chris Hughes (Sep 29 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887449):
I think I should be able to prove some bounds on it in a similar way to the bounds on cos. @**Mario Carneiro** told me the method 
sin (2*x) is positive for all 0<x<=1 because sin x and cos x are
x - x^3/3 < sin x < x and 1 - 2/3 * x^2 < cos x < 1 - x^2/3 on (0, 1] by infinite series bounds

#### [ Kevin Buzzard (Sep 29 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887684):
Chris I mentioned the general result from which this follows to you the other day. If you have a sequence a1,a2,a3,... with the signs of the terms alternating, and the terms tending to zero, then not only does the sum of the sequence converge, but the sum is <= all the odd partial sums (if a1>0) and >= all the even ones.

#### [ Kevin Buzzard (Sep 29 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887725):
This is a fabulous tool for getting bounds for anything. You don't even need 0<x<=1, it will work for any real x because after sufficiently many terms they will start alternating in sign and decreasing

#### [ Sebastian Zimmer (Sep 29 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887734):
that gives you x - x^3/3 < sin(x) but  I don't see why 1 - 2/3 x^2 < cos(x)

#### [ Kevin Buzzard (Sep 29 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887785):
1-x^2/2<cos(x) for 0<x<1 by this result

#### [ Kevin Buzzard (Sep 29 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887786):
which is stronger

#### [ Kevin Buzzard (Sep 29 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887838):
these tricks tell you that the partial sums are good approximations to sin and cos for x small, and because you know where the roots are you can start proving goofy things like sum 1/n^2 = pi^2/6 like this, but the details are messy

#### [ Sebastian Zimmer (Sep 29 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887849):
Can we show that e.g. sin has only one root close to \pi without calculus?

#### [ Sebastian Zimmer (Sep 29 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134887890):
actually I can see how to do it using some identities that are already proven

#### [ Chris Hughes (Sep 30 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134914917):
```quote
Chris I mentioned the general result from which this follows to you the other day. If you have a sequence a1,a2,a3,... with the signs of the terms alternating, and the terms tending to zero, then not only does the sum of the sequence converge, but the sum is <= all the odd partial sums (if a1>0) and >= all the even ones.
```
But it's only less than the partial sums after the sequence starts decreasing right. Which complicates proofs a lot without $$x \le 1$$

#### [ Kevin Buzzard (Sep 30 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134915402):
yes exactly. So e.g. for $$0\le x \le4$$ maybe you only know that $$x-\frac{x^3}{3!} \le \sin(x)\le x-\frac{x^3}{3!}+\frac{x^5}{5!}$$. But if people want to know things like cos(pi) then this approach will work.

#### [ Chris Hughes (Sep 30 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134933965):
I now have $$\sin(x)>0$$ for $$0<x<\pi$$, and therefore $$\sin\left(\frac{\pi}{2}\right)=1$$

#### [ Sebastian Zimmer (Sep 30 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134934076):
Are you going to do $$\sin(x) = 0 \iff x = k * \pi$$?

#### [ Sebastian Zimmer (Sep 30 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134934115):
Probably would be easy from what you have already done

#### [ Kevin Buzzard (Sep 30 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134935322):
One can probably prove that if sin (t)=0 then sin (x+2t)=sin(x) I guess? And the periods of a function are a subgroup of the reals so there's a pure thought approach to the result -- pi is in and no positive real less than pi, so it's the multiples of pi

#### [ Patrick Massot (Sep 30 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134935371):
I don't thing mathlib has the classification of subgroups of reals

#### [ Kevin Buzzard (Sep 30 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134935390):
This one isn't hard though, write any x in the group as n*pi +r with 0<=r<pi and then sin(r)=0 so by Chris's result r=0

#### [ Mario Carneiro (Sep 30 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134936122):
yes, this is basically how I sketched the proof that 2<pi < 4 with the alternate definition of pi as the least positive zero of sin. The addition formula of sin shows that zeros of sin are closed under Z module operations

#### [ Chris Hughes (Oct 01 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134983929):
Today I did arctan, arcsin and arccos, for reals, and proved that they are two-sided inverses within the appropriate intervals. Not sure how to do the same for complexes.

#### [ Mario Carneiro (Oct 01 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134984026):
Do you have complex log?

#### [ Mario Carneiro (Oct 01 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134984071):
How far in https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/subject/sine.20and.20cosine.20and.20pi/near/134258931 have you got?

#### [ Chris Hughes (Oct 01 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134985180):
`complex.log` is my next target. I think that can just be done with `real.log` and `real.arctan`

#### [ Mario Carneiro (Oct 01 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134985360):
hm, I guess you are right... I didn't have inverse trig when I did log

#### [ Mario Carneiro (Oct 01 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/134985447):
still, you want the injectivity statement anyway (`exp z = 0 <-> z/2 pi i` is an integer)

#### [ Kevin Buzzard (Oct 02 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135000763):
Wait -- what is `complex.log`? It'll be discontinuous, right? `log` is multi-valued (except at zero, where it's 37).

#### [ Kevin Buzzard (Oct 02 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135000872):
Geometrically, the map `exp` from the complexes to themselves is an infinite sheeted unramified cover from the complex numbers to the non-zero complex numbers. Unramified means that given any non-zero complex number in the target, you can draw a tiny disc around it and the pre-image of that tiny disc in the source is lots of copies of the tiny disc (in this case countably infinitely many, and a Z-torsor). What information does a presumably non-computable log give you about this picture? Isn't the correct definition of "log" just literally the subset of the complexes whose exp is the thing you're trying to take the log of? `complex.log` is ugly. Is it actually used in pure mathematics?

#### [ Kevin Buzzard (Oct 02 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135000922):
It could map to the product of the reals and $$\mathbb{R}/2\pi\mathbb{Z}$$

#### [ Kevin Buzzard (Oct 02 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135000942):
$$\log(re^{i\theta})=(\log(r),\theta)$$.

#### [ Mario Carneiro (Oct 02 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001106):
> complex.log is ugly. Is it actually used in pure mathematics?

Yes, absolutely yes. Trying to make sense of "multivalued functions" is a hundred times harder than just picking a branch cut and being consistent about it

#### [ Mario Carneiro (Oct 02 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001214):
My proposed mangling of this function: `log x` is the unique value with `exp (log x) = x` and `-pi < Im (log x) <= pi`, with `log 0 = 0`

#### [ Kevin Buzzard (Oct 02 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001264):
You guys think about maths in such an ugly way. I painted a beautiful picture and you just rip a branch out of it.

#### [ Mario Carneiro (Oct 02 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001271):
I'll have you know mathematicians invented branch cuts

#### [ Kevin Buzzard (Oct 02 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001283):
And yet actually Lean taught me a much more beautiful proof of the Hilbert Basis Theorem.

#### [ Kevin Buzzard (Oct 02 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001285):
Maybe I just don't like the definitions.

#### [ Kevin Buzzard (Oct 02 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001292):
I've been grumpy about 1/0 since day 1.

#### [ Mario Carneiro (Oct 02 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001585):
I don't understand why mathematicians have such a hard time coming to grips with the fact that not all functions are continuous

#### [ Mario Carneiro (Oct 02 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001652):
and when faced with evidence to the contrary they assume that points of discontinuity aren't in the domain

#### [ Simon Hudon (Oct 02 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001667):
```quote
I've been grumpy about 1/0 since day 1.
```
I'm not too fond of that either. PVS has a nice answer to that, you always have to prove that the denominator is `\ne 0`. I'm wondering if we could do that nicely with notation like this:

```lean
notation x ` / ` y := div' x y (by assumption)
```

This way, `x / y` would only be type correct if one of your assumption is `y ≠ 0`

#### [ Mario Carneiro (Oct 02 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001673):
0^0 is another example

#### [ Mario Carneiro (Oct 02 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135001742):
partial functions are possible but a bad idea in dtt

#### [ Kevin Buzzard (Oct 02 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135002497):
I'm hapoy not to open this can of worms again. My point is simply that it is still a surprise to me that CS guys think about mathematics in different ways to mathematicians. I really do not ever run into discontinuous functions in my work, and if you think I do (given that I run into division but am careful never to divide by zero) then in some sense I regard this as evidence that you're thinking about it wrongly, but conversely I think Mario's point is far more relevant in this context than what I think beautiful maths looks like. We are thinking about the same things but in some sense the mathematician seems to carry around some extra nuance, or perhaps some unwritten instructions on how to use the function properly and how to avoid the sharp edges. "Warning -- if you're dividing by zero you're probably doing it wrong".

#### [ Mario Carneiro (Oct 02 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135002787):
I think that's fair. Essentially, myself and other logicians / computer scientists are calling the mathematicians out when they talk about functions that don't meet the chapter 1 definition

#### [ Mario Carneiro (Oct 02 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135002812):
mathematical aesthetics decrees that everything interesting is continuous, and so this causes some cognitive dissonance in the mind of the mathematician that requires some additional equivocation on these setups when pressed

#### [ Mario Carneiro (Oct 02 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135002859):
but as soon as you stop pressing they go back to treating $$\log$$ like a plain function

#### [ Mario Carneiro (Oct 02 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135002984):
I think that there absolutely are other construals of this function as a Riemann surface or smooth manifold, but when it gets down to plain calculation you want to be able to pick a locally coherent section of the function and know what's going on there

#### [ Mario Carneiro (Oct 02 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135003054):
Note that from this "principal log", you can still have your manifold by rotating the reference frame so that your point of interest is on the real line

#### [ Patrick Massot (Oct 02 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135017970):
Is there any point in pushing this low-tech trigonometry further? I agree that having `pi`, and real trigonometry functions is nice for teaching. But who will teach complex logarithm without the basics of holomorphic functions? If someone does Cauchy theory then we can properly state that holomorphic functions have primitive on simply connected open subsets of their domain of definition. Then`1/z` will have a primitive function on any simply connected open set not containing zero, and we'll be able to easily relate those primitive to exponential.

#### [ Patrick Massot (Oct 02 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135018034):
Of course we could also do Riemann surfaces if someone prioritizes this, but I don't see happening soon

#### [ Kevin Buzzard (Oct 02 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135018266):
My personal stance on this is very clear: there is an essentially random amount of this stuff which I personally wanted to see in Lean, which is the stuff which shows up in my elementary course. For example $$e^{i\theta}=\cos(\theta)+i\sin(\theta)$$. But now we have all of this, because Chris took my course last year and has now covered everything, so I am no longer pushing for any more of this stuff. I just needed enough to be able to formalise the questions I ask the students. Maybe in the future we will need more but I am not pressing for any of it right now -- I feel that we have enough to look respectable to mathematicians.

#### [ Reid Barton (Oct 02 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135027840):
One of the standard proofs of the fundamental theorem of algebra requires as input the fact that $$z^n = a$$ has a root for any complex $$a$$, which needs about this level of trig. Or to prove $$t \mapsto e^{2\pi i t}$$ is a local homeomorphism from $$\mathbb{R}$$ to the unit circle is similar (which also implies FTA via covering space theory).

#### [ Patrick Massot (Oct 02 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135027892):
Indeed it would be nice to have FTA

#### [ Kevin Buzzard (Oct 02 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135028042):
This is one of those theorems for which there are about 20 proofs, isn't it. Before embarking on one in Lean I guess it's important to see how it is proved in other provers and what other options there are. The proof I saw used complex analysis and integration around a big circle if I remember correctly. But maybe I saw some completely different one years later which went via a real-analytic proof that every polynomial over the reals factored into terms of degree at most 2.

#### [ Reid Barton (Oct 02 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135028274):
metamath uses [this proof](https://ncatlab.org/nlab/show/fundamental+theorem+of+algebra#classical_fta_via_advanced_calculus) as far as I can tell

#### [ Reid Barton (Oct 02 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135028386):
I know this because someone on my Twitch stream mentioned that they were trying to prove FTA in Lean, working from the metamath proof. Kevin I am guessing it is a student of yours based but I'm not sure

#### [ Patrick Massot (Oct 02 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135028550):
I saw dozens of proofs of this theorem. Of course all the nice ones are more or less openly based on elementary algebraic topology. But I also saw a proof using only algebra and existence of roots for odd degree real polynomials (easy consequence of limits and intermediate value theorem)

#### [ Mario Carneiro (Oct 02 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135049069):
The metamath proof of FTA is my favorite (of course, I wrote it!). It is based on [this wikipedia proof](https://en.wikipedia.org/wiki/Fundamental_theorem_of_algebra#Topological_proofs). The main topological prerequisite is the extreme value theorem: A large closed ball about zero in C is compact, so `abs (p z)` takes a minimum value somewhere. The rest is just reasoning about finite sums

#### [ Kenny Lau (Oct 02 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135049190):
I've seen a short proof using a clever contour integral

#### [ Kenny Lau (Oct 02 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135049241):
but I recall it has cosine so maybe it isn't suitable

#### [ Kenny Lau (Oct 02 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135049243):
wait, which thread am I on

#### [ Mario Carneiro (Oct 02 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135049247):
it also has contour integrals

#### [ Mario Carneiro (Oct 02 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135049251):
which we don't have

#### [ Kenny Lau (Oct 02 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135049252):
yes, I mean the proof I saw uses one contour integral

#### [ Kenny Lau (Oct 02 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135049275):
actually I think the proof from Galois theory may have some potential

#### [ Chris Hughes (Oct 03 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135127077):
PRed https://github.com/leanprover/mathlib/pull/386. I stopped at complex log. No inverse complex trig yet. Not sure whether a highbrow method is better for that.

#### [ Mario Carneiro (Oct 03 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129185):
The metamath definitions
$$\arcsin z = -i\log(iz + (1-z^2)^{1/2})$$
$$\arccos z = \pi/2-\arcsin z$$
$$\arctan z = \frac i2\left[\log(1-iz) - \log(1 + iz)\right]$$
make sure to put the branch cuts in the right places

#### [ Kevin Buzzard (Oct 03 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129267):
Chris is writing a calculator emulator.

#### [ Mario Carneiro (Oct 03 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129334):
(I don't see a sqrt in the first expression where the conspicuous space is, but pretend there is one)

#### [ Kevin Buzzard (Oct 03 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129600):
I've been fixing that on this forum by using `^{1/2}`. `\sqrt` never works for me.

#### [ Reid Barton (Oct 03 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129648):
Do we have enough now to show that every complex number can be written in the form $$re^{i \theta}$$?

#### [ Kevin Buzzard (Oct 03 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129757):
This might boil down to showing that if $$x^2+y^2=1$$ then there exists $$\theta$$ such that $$x=\cos(\theta)$$ and $$y=\sin(\theta)$$. If only we'd defined $$\sin$$ as opposite over hypotenuse :-)

#### [ Patrick Massot (Oct 03 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129868):
```quote
If only we'd defined $$\sin$$ as opposite over hypotenuse :-)
```
Finally, someone having common sense!

#### [ Patrick Massot (Oct 03 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129943):
Now stop kidding: where is our sheaf theory?

#### [ Kevin Buzzard (Oct 03 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129979):
Hey, maybe $$atan(y/x)$$ (possibly plus $$\pi$$) can be proved to work.

#### [ Chris Hughes (Oct 03 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135129997):
@**Reid Barton** I didn't prove that directly, but we have `arg` and `cos (arg x) = x.re / abs x` and similar for sin, so it should be easy.

#### [ Kevin Buzzard (Oct 03 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135130561):
If we prove the product rule then mathlib might be able to pass A-level! (UK maths exam for 18 year olds)

#### [ Patrick Massot (Oct 03 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135130643):
We sort of have it in the holomorphic case https://github.com/semorrison/kbb/blob/master/src/holomorphic_functions.lean#L117

#### [ David Michael Roberts (Oct 04 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135141531):
```quote
It's surprising how much  you can prove without calculus
```
it might be worth formalising some of this, if possible: https://ncatlab.org/toddtrimble/published/Characterization+of+sine

#### [ Mario Carneiro (Oct 04 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135141911):
> and we get to invoke the theory of entire analytic functions.

more like the entire theory of analytic functions

#### [ Kevin Buzzard (Oct 04 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135155372):
I never quite know whether it's worth formalising "gimmicks". I mean, I've taught this stuff, and never once have I used or seen the use of this linked result -- the characterisation. It's very cute for sure. But does it deserve to be in mathlib? I genuinely don't know.

#### [ Patrick Massot (Oct 04 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135155563):
I never heard of those characterizations before following the link yesterday

#### [ Bryan Gin-ge Chen (Oct 04 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135155649):
Presumably there are many math results worth formalizing that don't deserve to be in mathlib. I think a well-documented formalization of the above characterization of sine could potentially make a fun tutorial to the new functions that Chris is PRing.

#### [ Kevin Buzzard (Oct 04 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/135160643):
I think that this is a really good way of looking at it.

#### [ Chris Hughes (Oct 27 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trigonometric%20functions/near/136599443):
(deleted)


{% endraw %}
