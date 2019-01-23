---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/141825kbb/47024sineandcosineandpi.html
---

## Stream: [kbb](index.html)
### Topic: [sine and cosine and pi](47024sineandcosineandpi.html)

---


{% raw %}
#### [ Chris Hughes (Sep 15 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134008790):
I've started working on sine and cosine. I have cleaned the proofs up until `exp (x + y)` and I'm currently working on things like `sin (x + y)`. I have no idea how to define pi however. @**Mario Carneiro** what's the best way to do this?

#### [ Patrick Massot (Sep 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134009489):
Do you have complex exp or only real?

#### [ Chris Hughes (Sep 15 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134010115):
complex. I'll define real.exp in terms of complex.exp

#### [ Patrick Massot (Sep 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011693):
Ok, so `sin (x + y)` and friends follow immediately from `exp(x+y)`.

#### [ Johan Commelin (Sep 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011700):
You're such a mathematician.

#### [ Johan Commelin (Sep 15 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011706):
Remember that you get a `/2` in those expressions. You need to convince Lean that you aren't dividing by zero.

#### [ Johan Commelin (Sep 15 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011751):
But Chris is pushing progress to the `exp` branch on community mathlib

#### [ Patrick Massot (Sep 15 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011752):
For `pi` you can prove that cos vanishes somewhere between 0 and 2 using the intermediate value theorem, and define pi as twice the first zero of cos. This is cheap but I guess proving other properties from that is painful. A better solution is probably to prove the classification of subgroups of (R, +), and define 2pi as the positive generator of ker(t mapsto exp(i*t)) (this kernel cannot be dense because exp is continuous and non-constant)

#### [ Johan Commelin (Sep 15 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011758):
Rights, so we need continuity of `exp`.

#### [ Johan Commelin (Sep 15 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011759):
For either definition.

#### [ Patrick Massot (Sep 15 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011760):
I both cases yes

#### [ Johan Commelin (Sep 15 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011807):
What is the best way to do this continuity proof?

#### [ Johan Commelin (Sep 15 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011809):
Generalise to arbitrary power series?

#### [ Patrick Massot (Sep 15 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011813):
We could also cheat and define pi using a random series, but then the link with exp and cos would be harder to establish

#### [ Johan Commelin (Sep 15 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011817):
I like your second definition.

#### [ Johan Commelin (Sep 15 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011821):
We should probably just check what Coq/Mizar/Isabelle do

#### [ Reid Barton (Sep 15 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011825):
If you have $$e^{x+y} = e^x e^y$$ then it suffices to show that $$e^x$$ is continuous at 0, and for this you can use a crude bound on the power series.

#### [ Johan Commelin (Sep 15 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011879):
Ok, sounds good.

#### [ Reid Barton (Sep 15 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011923):
Patrick, you still have to prove that $$e^{it} = 1$$ for some nonzero real $$t$$ first, right?

#### [ Patrick Massot (Sep 15 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134011977):
indeed we must exclude that the kernel is trivial

#### [ Reid Barton (Sep 15 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012154):
Does the definition of pi really rely on some explicit estimate like $$\cos 2 < 0$$? 
I guess if you have differential calculus at your disposal, you could show that $$\sin t$$ is bounded, and then conclude that $$\cos t$$ cannot be positive everywhere... wait no, I don't even see how to make this work.

#### [ Patrick Massot (Sep 15 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012167):
https://isabelle.in.tum.de/dist/library/HOL/HOL/Transcendental.html seems to use my first method

#### [ Reid Barton (Sep 15 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012218):
Okay--if $$\cos t$$ was positive everywhere then $$\sin t$$ would be increasing, and then $$\cos t$$ would have to lie below some line of negative slope, a contradiction.
Not sure if one can extract an "elementary" (no differential calculus) proof along these lines.

#### [ Patrick Massot (Sep 15 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012328):
This all looks super tedious

#### [ Patrick Massot (Sep 15 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012331):
Let's do perfectoid spaces

#### [ Johan Commelin (Sep 15 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012706):
Hmmm, @**Reid Barton** I can easily follow your maths proof that `exp` is continuous if it is ctu at `0`.

#### [ Johan Commelin (Sep 15 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012709):
But how do I put this into Lean?

#### [ Patrick Massot (Sep 15 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012791):
https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L289 may help

#### [ Johan Commelin (Sep 15 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012906):
Aah thanks, that indeed looks useful.

#### [ Johan Commelin (Sep 15 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012930):
Do we know that `(exp x) \ne 0`?

#### [ Patrick Massot (Sep 15 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012932):
It's not yet merged in mathlib, but doesn't depend on much

#### [ Johan Commelin (Sep 15 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012936):
Because then we know that `exp` is a group hom, which might also help.

#### [ Chris Hughes (Sep 15 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134012999):
We do know exp \ne 0

#### [ Johan Commelin (Sep 15 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013589):
Hmmm, I'm horrible with these continuity proofs...

#### [ Johan Commelin (Sep 15 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013597):
So there is `squeeze_zero`, but I don't think there is a generic squeeze lemma, right?

#### [ Patrick Massot (Sep 15 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013604):
there is

#### [ Johan Commelin (Sep 15 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013612):
Ooh, my VScode didn't find it.

#### [ Johan Commelin (Sep 15 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013653):
Let me try again

#### [ Johan Commelin (Sep 15 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013665):
Aah, it only has squeeze in its docstring

#### [ Johannes Hölzl (Sep 15 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013667):
grep for sandwich in mathlib

#### [ Patrick Massot (Sep 15 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013671):
https://github.com/leanprover/mathlib/blob/5613d2ecc92ce8fae9555745bd94756dec61a323/analysis/topology/topological_structures.lean#L438

#### [ Patrick Massot (Sep 15 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013680):
grep for squeeze also works

#### [ Patrick Massot (Sep 15 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013687):
but grep for gendarme doesn't work

#### [ Johan Commelin (Sep 15 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013912):
Hmm snap, of course that doesn't help for continuity of the complex version.

#### [ Patrick Massot (Sep 15 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134013997):
Anyway, the long term reasoning is clear: we don't want a trick, we want general results on power series

#### [ Johan Commelin (Sep 15 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014067):
Right. And I think I'dd rather work on the long term

#### [ Johan Commelin (Sep 15 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014074):
So, should we create `power_series.lean` on cocalc?

#### [ Johan Commelin (Sep 15 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014085):
Maybe Kevin will see it. I think I don't care

#### [ Johan Commelin (Sep 15 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014151):
Is that ok with others? Then we could multiplayer power series into existence.

#### [ Johan Commelin (Sep 15 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014152):
I'm quite addicted to that experience.

#### [ Patrick Massot (Sep 15 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014192):
I would wait until @**Johannes Hölzl** tells us about how this is done in Isabelle (they have a lot of analysis there)

#### [ Johannes Hölzl (Sep 15 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014543):
I will take a look

#### [ Johannes Hölzl (Sep 15 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014907):
So, continuity of `exp` is proved using derivability. There is a section "Term-by-Term Differentiability of Power Series" in http://isabelle.in.tum.de/dist/library/HOL/HOL/Transcendental.html where most of it is proved. The central part is `termdiffs` which states: `DERIV (λx. ∑n. c n * x^n) x :> (∑n. (diffs c) n * x^n)`.  Where `diffs c := (λn. of_nat (Suc n) * c (Suc n))` (`Suc` is `nat.succ` and `of_nat` is the coercion nat to a real_algebra).

#### [ Johannes Hölzl (Sep 15 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134014963):
The lemma `termdiffs` assumes that various power series converge.

#### [ Johan Commelin (Sep 15 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015048):
So it would make sense to define power series, and then we need to change the definition of exp to use those power series.

#### [ Johan Commelin (Sep 15 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015049):
Is that right?

#### [ Johan Commelin (Sep 15 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015051):
I mean, there won't change that much

#### [ Johannes Hölzl (Sep 15 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015240):
Yes, I think it would make sense to define power series. Also derivatives...

#### [ Johan Commelin (Sep 15 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015325):
Ok, and this is purely algebraic stuff, right?

#### [ Johan Commelin (Sep 15 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015338):
Or do you also mean the analytic derivative?

#### [ Johannes Hölzl (Sep 15 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015355):
I guess we need to analytic derivative to prove continuity

#### [ Johan Commelin (Sep 15 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015413):
Hmmm, ok

#### [ Johan Commelin (Sep 15 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015419):
And we really need all of this to define pi?

#### [ Johan Commelin (Sep 15 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015436):
Well, we will need this stuff anyway

#### [ Johan Commelin (Sep 15 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015498):
I'm going to create a `power_series.lean` on CoCalc

#### [ Johannes Hölzl (Sep 15 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015586):
In Isabelle:
`pi = 2 * (THE x. 0 ≤ x ∧ x ≤ 2 ∧ cos x = 0)` 
and then even more algebric facts about `cos` and `sin`

#### [ Johan Commelin (Sep 15 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015647):
Right, but I guess there is a hidden proof that such `x` exists, not?

#### [ Johannes Hölzl (Sep 15 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015653):
of course

#### [ Johannes Hölzl (Sep 15 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015655):
`cos_is_zero: "∃!x::real. 0 ≤ x ∧ x ≤ 2 ∧ cos x = 0"`

#### [ Johannes Hölzl (Sep 15 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015666):
it uses IVT

#### [ Johan Commelin (Sep 15 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015678):
Right, so we need continuity

#### [ Johannes Hölzl (Sep 15 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015726):
it also uses derivative of `cos` and that `sin 2 > 0`

#### [ Johan Commelin (Sep 15 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134015749):
Ok

#### [ Chris Hughes (Sep 15 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134021725):
I just pushed a load of stuff to the `exp` branch of community mathlib. It's about as far as I can go without continuity of `exp` and I'm not sure what the best approach for that is.

#### [ Mario Carneiro (Sep 15 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134023255):
@**Chris Hughes** In metamath we used a very low brow approach to exp (it comes before analysis), which I think worked quite well.
* I assume you already have things like the addition formula and other algebraic stuff on sin and cos.
* `exp` is continuous iff it is continuous at each point. By facts about multiplying functions continuous at a point, you can show that it suffices to prove `exp` is continuous at zero.
* `1 + x <= exp x` for positive `x` by taking away the rest of the summands; `exp x <= 1/(1-x)` by comparing the infinite series of these two. Thus `exp` is continuous and even differentiable at zero by the sandwich lemma.
* It follows from basic topological ring action that `sin` is continuous.
* `pi` is the infimum of the positive zeros of the `sin` function. We need to show this is well defined and a zero of the sin function.
* Suppose `a` is a zero of `sin` in the range `(2,4)`, and `b` is a positive zero of sin. Show that if `pi < a` then `(pi + a) / 2 <= b`, because `2*a - b` is also a zero of `sin`.
* By the intermediate value theorem applied to `sin`, and `sin 2 > 0` and `sin 4 < 0`, there is a zero `a` in this range, and `pi` exists. if `pi < a`, then `(pi + a) / 2 <= pi` by the above lemma, since `pi` is the infimum of all positive roots of sin. Thus `a <= pi` and thus `pi` is the unique zero of sin in this range.

#### [ Chris Hughes (Sep 15 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134023510):
Can you point me to the sandwich lemma, and the facts about multiplying functions continuous at points? I've never touched anything in the analysis folder before now.

#### [ Mario Carneiro (Sep 15 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134023552):
For the bounds:
* `sin 4 = 2 * sin 2 * cos 2` is negative because `sin 2` is positive and `cos 2` is negative
* `-7/9 < cos 2 < -1/9` because `cos 2 = 2 * (cos 1)^2 - 1` and `1/3 < cos 1 < 2/3`
* `sin (2*x)` is positive for all `0<x<=1` because `sin x` and `cos x` are
* `x - x^3/3 < sin x < x` and `1 - 2/3 * x^2 < cos x < 1 - x^2/3` on `(0, 1]` by infinite series bounds

#### [ Mario Carneiro (Sep 15 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134023609):
I'm not sure we have it, but it should be easy to show over the reals (or whatever generalization best encompasses the reals)

#### [ Mario Carneiro (Sep 15 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134023667):
By the way, metamath used to have a direct proof before analysis was developed, but now continuity of exp follows from differentiability, and continuity uses various topological notions and proofs. I think the definition of `exp` can be in `data.{real,complex}.basic`, but `pi` and other facts that depend on continuity should go in the topological part, at `analysis.{real,complex}`

#### [ Chris Hughes (Sep 15 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134023818):
Where are the relevant theorems in the lean library? Do we have IVT?

#### [ Mario Carneiro (Sep 15 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134023917):
I don't think we do. I would want to just prove it over the reals for now

#### [ Chris Hughes (Sep 15 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024102):
How do I state continuous at a point?

#### [ Mario Carneiro (Sep 15 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024208):
In topology, `f : X -> Y` is continuous at `x` if `tendsto f (nhds x) (nhds (f x))`

#### [ Chris Hughes (Sep 15 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024352):
And what are the lemmas that let me prove that it's continuous everywhere if it's continuous at 0?

#### [ Chris Hughes (Sep 15 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024397):
I'm not even sure why that's true.

#### [ Patrick Massot (Sep 15 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024517):
I think I already answered that earlier today

#### [ Chris Hughes (Sep 15 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024523):
I think I've worked out vaguely why it's true in maths, but not in lean.

#### [ Patrick Massot (Sep 15 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024526):
https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L289

#### [ Patrick Massot (Sep 15 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024575):
Importing that and apply it to reals prove that `tendsto f (nhds x) (nhds (f x))` iff `tendsto (lambda h, f (x+h)) (nhds 0) (nhds (f x))`

#### [ Mario Carneiro (Sep 15 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024581):
this is a consequence of `(\lam x, x + h)` being a homeo

#### [ Patrick Massot (Sep 15 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024583):
In case of exp you can rewrite f (x+h) as exp(x)*exp(h), use exp(x) converges (it's constant) and the result at zero

#### [ Chris Hughes (Sep 15 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024634):
Is this the correct statement of `exp` is continuous at x = 0 
```lean
lemma continuous_exp : tendsto exp (nhds 0) (nhds 1)
```

#### [ Mario Carneiro (Sep 15 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024638):
yes, hopefully you know `exp 0 = 1` already by algebraic stuff

#### [ Patrick Massot (Sep 15 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024640):
The name is bad, but the statement is ok

#### [ Patrick Massot (Sep 15 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024646):
assuming you know exp 0

#### [ Mario Carneiro (Sep 15 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024648):
that's true, it should say `tendsto_exp_zero` or something

#### [ Patrick Massot (Sep 15 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024700):
We should probably prove the lemma for general homomorphisms between topological group (continuity at zero implies continuity)

#### [ Chris Hughes (Sep 15 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024770):
And this only works for `real.exp` right?

#### [ Patrick Massot (Sep 15 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024810):
Why?

#### [ Patrick Massot (Sep 15 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024811):
Didn't you prove the addition formula for complex numbers?

#### [ Chris Hughes (Sep 15 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024860):
Yes, but `tendsto_of_tendsto_of_tendsto_of_le_of_le` requires a partial order on complexes, unless I'm doing something wrong.

#### [ Patrick Massot (Sep 15 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024868):
Oh, I meant that continuity at zero in C implies continuity everywhere

#### [ Mario Carneiro (Sep 15 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024869):
The metamath comment says that the key step is `abs (exp x - x - 1) <= (abs x) ^ 2 * 3/4`

#### [ Patrick Massot (Sep 15 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024871):
But Mario's idea to prove continuity at zero works in R

#### [ Patrick Massot (Sep 15 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024882):
but he seems to have a new idea

#### [ Mario Carneiro (Sep 15 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024883):
this bound works on complexes too

#### [ Mario Carneiro (Sep 15 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024925):
it is a special case of the tail bound on exp

#### [ Mario Carneiro (Sep 15 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024939):
`abs (sum k = m,...,infty (x ^ n / n!)) <= (abs a)^m * ((m + 1) / (m! * m))`

#### [ Mario Carneiro (Sep 15 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024982):
when `abs x <= 1`

#### [ Patrick Massot (Sep 15 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024988):
I need to go, sorry

#### [ Chris Hughes (Sep 15 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134024991):
How does the bound work on the complexes when they don't have linear order? What's the correct statement? `abs ∘ exp` is continuous doesn't seem like enough to prove `exp` is continuous. Bear in mind I know very little about analysis.

#### [ Chris Hughes (Sep 15 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025095):
If I manage to turn my goal into something in terms of functions I recognize, I;m sure I'll be fine, but I just need to work out how to get from `nhds` to something I recognize.

#### [ Kenny Lau (Sep 15 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025197):
you should go revise M1P1 :P

#### [ Chris Hughes (Sep 15 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025204):
That doesn't mention anything to do with complex numbers.

#### [ Mario Carneiro (Sep 15 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025251):
The statement `abs (exp x - x - 1) <= (abs x) ^ 2 * 3/4` is enough to prove that `exp` is differentiable at 0

#### [ Mario Carneiro (Sep 15 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025253):
here `x` is a complex number

#### [ Chris Hughes (Sep 15 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025255):
I could probably manage that.

#### [ Chris Hughes (Sep 15 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025261):
You'll have to help me turn that into anything about continuity.

#### [ Mario Carneiro (Sep 15 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025263):
For continuity you could probably just do the zeroth order tail bound, which is `abs (exp x - 1) <= (abs x) * 2`

#### [ Kenny Lau (Sep 15 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025306):
is it realistic to develop a general theory of complex power series?

#### [ Mario Carneiro (Sep 15 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134025308):
maybe, but I'd prefer to defer it

#### [ Patrick Massot (Sep 17 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134088538):
@**Chris Hughes** are you currently working on exp?

#### [ Chris Hughes (Sep 17 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134088612):
No, and I am doing other things today. I might work on it tomorrow.

#### [ Chris Hughes (Sep 17 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134117371):
I made some progress. I proved IVT, though I'm not sure if there is some clever simple proof.
```lean
lemma IVT {f : ℝ → ℝ} (hf : continuous f) {x y : ℝ} (hx : f x ≤ 0) (hy : 0 ≤ f y)
  (hxy : x ≤ y) : ∃ z : ℝ, x ≤ z ∧ z ≤ y ∧ f z = 0 :=
let z := Sup {a | f a ≤ 0 ∧ x ≤ a ∧ a ≤ y} in
have hz₁ : ∃ a, ∀ g ∈ {a : ℝ | f a ≤ 0 ∧ x ≤ a ∧ a ≤ y}, g ≤ a := ⟨y, λ _ h, h.2.2⟩,
have hz₂ : ∃ a, a ∈ {a : ℝ | f a ≤ 0 ∧ x ≤ a ∧ a ≤ y} := ⟨x, hx, le_refl _, hxy⟩, 
⟨z, le_Sup _ hz₁ ⟨hx, le_refl _, hxy⟩, 
  (Sup_le {a | f a ≤ 0 ∧ x ≤ a ∧ a ≤ y} hz₂ hz₁).2 (λ _ h, h.2.2), 
  eq_of_forall_dist_le $ λ ε ε0,
    let ⟨δ, hδ0, hδ⟩ := tendsto_nhds_of_metric.1 (continuous_iff_tendsto.1 hf z) ε ε0 in 
    (le_total 0 (f z)).elim
      (λ h, le_of_not_gt $ λ hfε, begin
        rw [dist_0_eq_abs, abs_of_nonneg h] at hfε,
        refine mt (Sup_le {a | f a ≤ 0 ∧ x ≤ a ∧ a ≤ y} hz₂ hz₁).2 
          (not_le_of_gt (sub_lt_self z (half_pos hδ0))) 
          (λ g hg, le_of_not_gt 
            (λ hgδ, not_lt_of_ge hg.1
              (lt_trans (sub_pos_of_lt hfε) (sub_lt_of_sub_lt 
                (lt_of_le_of_lt (le_abs_self _) _))))),
        rw abs_sub,
        exact hδ (abs_sub_lt_iff.2 ⟨lt_of_le_of_lt (sub_nonpos.2 (le_Sup _ hz₁ hg)) hδ0, 
          by simp only [z] at *; linarith⟩)      
        end)
      (λ h, le_of_not_gt $ λ hfε, begin
        rw [dist_0_eq_abs, abs_of_nonpos h] at hfε,
        refine mt (le_Sup {a | f a ≤ 0 ∧ x ≤ a ∧ a ≤ y}) 
          (λ h : ∀ k, k ∈ {a | f a ≤ 0 ∧ x ≤ a ∧ a ≤ y} → k ≤ z,
            not_le_of_gt ((lt_add_iff_pos_left z).2 (half_pos hδ0)) 
              (h _ ⟨le_trans (le_sub_iff_add_le.2 (le_trans (le_abs_self _) 
                    (le_of_lt (hδ $ by rw [dist_eq, add_sub_cancel, abs_of_nonneg (le_of_lt (half_pos hδ0))]; 
                      exact half_lt_self hδ0)))) 
                  (le_of_lt (sub_neg_of_lt hfε)),
                le_trans (le_Sup _ hz₁ ⟨hx, le_refl _, hxy⟩) (le_of_lt ((lt_add_iff_pos_left _).2 (half_pos hδ0))), 
                le_of_not_gt (λ hδy, not_lt_of_ge hy (lt_of_le_of_lt (show f y ≤ f y - f z - ε, by linarith) 
                  (sub_neg_of_lt (lt_of_le_of_lt (le_abs_self _) 
                    (@hδ y (abs_sub_lt_iff.2 ⟨by simp only [z] at *; linarith, 
                      sub_lt_iff_lt_add.2 (by rw add_comm; exact lt_add_of_le_of_pos 
                        ((Sup_le _ hz₂ hz₁).2 (λ _ h, h.2.2)) hδ0)⟩))))))⟩)) hz₁
        end)⟩
```

#### [ Johan Commelin (Sep 17 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134117436):
Well done!

#### [ Johan Commelin (Sep 17 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134117495):
@**Chris Hughes** I guess you could quite easily change the `0`s in the statement into a parameter, right?

#### [ Johan Commelin (Sep 17 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134117550):
Hmm, but you are use `half_pos` and things like that.

#### [ Johan Commelin (Sep 17 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134117558):
So maybe you should just leave this like it is.

#### [ Chris Hughes (Sep 17 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134117956):
I can deduce the general statement from this quite easily I imagine.

#### [ Johan Commelin (Sep 17 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134117967):
Yes, agreed.

#### [ Chris Hughes (Sep 17 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134117976):
The more important generalisation is that it only needs to be continuous on the interval.

#### [ Kenny Lau (Sep 17 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118217):
@**Chris Hughes** how much topology do you know?

#### [ Chris Hughes (Sep 17 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118244):
More or less none.

#### [ Kenny Lau (Sep 17 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118305):
if x<y and f(x)<0 and f(y)>0, then {t | f(t) < 0} and {t | f(t) > 0} are two disjoint open subsets of [x,y]. Since [x,y] is connected, the union of those two sets can't be the entirety of [x,y], so there must be something not belonging to those two sets, i.e. t such that f(t) = 0

#### [ Johan Commelin (Sep 17 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118524):
Do we know that intervals are connected?

#### [ Johan Commelin (Sep 17 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118620):
Does Lean even know what an interval is?

#### [ Reid Barton (Sep 17 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118624):
I don't think we have connectedness yet

#### [ Reid Barton (Sep 17 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118642):
We do have intervals though and Lean knows closed ones are compact

#### [ Reid Barton (Sep 17 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118740):
Basically it's a similar proof to the one above I think, except the set {a | f a <= 0 ...} is now called U

#### [ Kenny Lau (Sep 17 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134118868):
right, we know they're compact but not that they're connected...?

#### [ Mario Carneiro (Sep 17 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134119204):
right, the meat of this proof is showing that R is connected

#### [ Mario Carneiro (Sep 17 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134119343):
I think you can pretty trivially generalize the assumption to `∀ x, a < x → x < b → tendsto f (nhds x) (nhds (f x))`

#### [ Mario Carneiro (Sep 17 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134119442):
If you prefer, you can prove the version assuming `continuous f` as a corollary

#### [ Mario Carneiro (Sep 17 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134119455):
other than that, I think this is fine for the first cut

#### [ Chris Hughes (Sep 17 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134120625):
I almost generalized it to `∀ x, a < x → x < b → tendsto f (nhds x) (nhds (f x))`. I have `lt` instead of `le`. Generalizing it to `lt` seems to add quite a bit of complication.
```lean
lemma IVT {f : ℝ → ℝ} {x y : ℝ} 
  (hf : ∀ a, x ≤ a → a ≤ y → tendsto f (nhds a) (nhds (f a))) (hx : f x ≤ 0) (hy : 0 ≤ f y)
  (hxy : x ≤ y) : ∃ z : ℝ, x ≤ z ∧ z ≤ y ∧ f z = 0 :=
let z := Sup {a | f a ≤ 0 ∧ x ≤ a ∧ a ≤ y} in
have hz₁ : ∃ a, ∀ g ∈ {a : ℝ | f a ≤ 0 ∧ x ≤ a ∧ a ≤ y}, g ≤ a := ⟨y, λ _ h, h.2.2⟩,
have hz₂ : ∃ a, a ∈ {a : ℝ | f a ≤ 0 ∧ x ≤ a ∧ a ≤ y} := ⟨x, hx, le_refl _, hxy⟩,
have hxz : x ≤ z, from le_Sup _ hz₁ ⟨hx, le_refl _, hxy⟩,
have hzy : z ≤ y, from (Sup_le _ hz₂ hz₁).2 (λ _ h, h.2.2), 
⟨z, hxz, hzy,
  eq_of_forall_dist_le $ λ ε ε0,
    let ⟨δ, hδ0, hδ⟩ := tendsto_nhds_of_metric.1 (hf _ hxz hzy) ε ε0 in
    (le_total 0 (f z)).elim
      (λ h, le_of_not_gt $ λ hfε, begin
        rw [dist_0_eq_abs, abs_of_nonneg h] at hfε,
        refine mt (Sup_le {a | f a ≤ 0 ∧ x ≤ a ∧ a ≤ y} hz₂ hz₁).2
          (not_le_of_gt (sub_lt_self z (half_pos hδ0)))
          (λ g hg, le_of_not_gt
            (λ hgδ, not_lt_of_ge hg.1
              (lt_trans (sub_pos_of_lt hfε) (sub_lt_of_sub_lt
                (lt_of_le_of_lt (le_abs_self _) _))))),
        rw abs_sub,
        exact hδ (abs_sub_lt_iff.2 ⟨lt_of_le_of_lt (sub_nonpos.2 (le_Sup _ hz₁ hg)) hδ0,
          by simp only [z] at *; linarith⟩)
        end)
      (λ h, le_of_not_gt $ λ hfε, begin
        rw [dist_0_eq_abs, abs_of_nonpos h] at hfε,
        refine mt (le_Sup {a | f a ≤ 0 ∧ x ≤ a ∧ a ≤ y})
          (λ h : ∀ k, k ∈ {a | f a ≤ 0 ∧ x ≤ a ∧ a ≤ y} → k ≤ z,
            not_le_of_gt ((lt_add_iff_pos_left z).2 (half_pos hδ0))
              (h _ ⟨le_trans (le_sub_iff_add_le.2 (le_trans (le_abs_self _)
                    (le_of_lt (hδ $ by rw [dist_eq, add_sub_cancel, abs_of_nonneg (le_of_lt (half_pos hδ0))];
                      exact half_lt_self hδ0))))
                  (le_of_lt (sub_neg_of_lt hfε)),
                le_trans hxz (le_of_lt ((lt_add_iff_pos_left _).2 (half_pos hδ0))),
                le_of_not_gt (λ hδy, not_lt_of_ge hy (lt_of_le_of_lt (show f y ≤ f y - f z - ε, by linarith)
                  (sub_neg_of_lt (lt_of_le_of_lt (le_abs_self _)
                    (@hδ y (abs_sub_lt_iff.2 ⟨by simp only [z] at *; linarith,
                      sub_lt_iff_lt_add.2 (by rw add_comm; exact lt_add_of_le_of_pos
                        hzy hδ0)⟩))))))⟩)) hz₁
        end)⟩
```

#### [ Chris Hughes (Sep 17 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134120816):
In fact generalizing to `lt` makes the statement false I think.

#### [ Johan Commelin (Sep 17 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134120937):
Right, you need the closed interval.

#### [ Mario Carneiro (Sep 17 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121041):
ah yes, you're right. In order to properly say "continuous on [a, b]" you would need `tendsto f (nhds a ⊓ principal (Icc a b)) (nhds (f a))`

#### [ Chris Hughes (Sep 17 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121162):
What does that mean, and how is it different from my assumption?

#### [ Chris Hughes (Sep 17 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121414):
Is it weaker or stronger than my assumption?

#### [ Johan Commelin (Sep 17 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121530):
@**Chris Hughes** you know about left/right-continuity at a point?

#### [ Mario Carneiro (Sep 17 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121551):
My predicate says that `f` restricted to `[a, b]` is continuous

#### [ Mario Carneiro (Sep 17 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121563):
so it might have discontinuity at a or b from outside the interval

#### [ Chris Hughes (Sep 17 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121604):
I see.

#### [ Johan Commelin (Sep 17 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121609):
Eg: `f x = if x \in [a,b] then 0 else 1`

#### [ Mario Carneiro (Sep 17 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134121627):
But you should be able to extend any continuous function on [a,b] to one continuous in your sense anyway, so I wouldn't make a big deal about it

#### [ Chris Hughes (Sep 19 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256188):
I managed to prove this today. 
```lean
lemma exp_continuous_aux {x : ℂ} (hx : abs x ≤ 1) : 
  abs (exp x - x - 1) ≤ abs x ^ 2 * (5 / 6) :=
``` 
It's `5 / 6` instead of `3/4`, is that going to be a problem? I'm not sure where my extra `1/12` went

#### [ Chris Hughes (Sep 19 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256238):
I suppose it depends on whether I can still prove the cos inequalities

#### [ Mario Carneiro (Sep 19 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256650):
that's weird, how did you prove it?

#### [ Mario Carneiro (Sep 19 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256727):
I don't think we need any particular bound for this part, that's enough for continuity of course

#### [ Chris Hughes (Sep 19 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256880):
This is my proof. I think the lost information is probably in the step
`sum (range (j - 3)) (λ m, 1 / (m + 3).fact) ≤ sum (range (j - 3)) (λ m, 1 / 6 * (1 / 2) ^ m)`

```lean
lemma exp_continuous_aux {x : ℂ} (hx : abs x ≤ 1) : 
  abs (exp x - x - 1) ≤ abs x ^ 2 * (5 / 6) :=
have onesubhalf : (1 : ℝ) - 1 / 2 = 1 / 2, by norm_num,
have abshalf : abs (1 / 2 : ℂ) = 1 / 2 :=
  calc abs (1 / 2 : ℂ) = abs ((1 / 2 : ℝ) : ℂ) : congr_arg abs $ by simp [of_real_div, of_real_bit0, of_real_inv]
  ... = (1 / 2 : ℝ) : by rw [abs_of_nonneg]; norm_num,
begin
  conv in (exp x - x) {congr, skip, rw ← lim_const x},
  rw [exp, sub_eq_add_neg, sub_eq_add_neg, ← lim_const 1,
    ← lim_neg, ← lim_neg, lim_add, lim_add, ← lim_abs],
  refine real.lim_le _ _ (cau_seq.le_of_exists ⟨3, (λ j hj, _)⟩),
  show (abs (sum (range j) (λ m, x ^ m / m.fact) - x - 1) ≤ abs x ^ 2 * (5 / 6)),
  exact calc abs ((sum (range j)) (λ m, x ^ m / m.fact) - x - 1) = 
      abs x ^ 2 * abs (sum (range (j - 2)) (λ m, x ^ m / (m + 2).fact)) :
    by conv {to_lhs, rw [← nat.sub_add_cancel (nat.le_of_succ_le hj), sum_range_succ', sum_range_succ']};
      simp [pow_succ, mul_sum.symm, abs_mul, mul_div_assoc, mul_assoc]
  ... = abs x ^ 2 * abs (sum (range (j - 3)) (λ m, x ^ (m + 1) / (m + 3).fact) + 1 / 2) :
    by conv {to_lhs, rw [← nat.succ_sub_succ, nat.succ_sub hj, sum_range_succ'] };
      simp [nat.fact, bit0]
  ... ≤ abs x ^ 2 * (5 / 6) : mul_le_mul_of_nonneg_left 
    (calc abs (sum (range (j - 3)) (λ m, x ^ (m + 1) / (m + 3).fact) + 1 / 2)
          ≤ abs (sum (range (j - 3)) (λ m, x ^ (m + 1) / (m + 3).fact)) + abs (1 / 2) :
        abs_add _ _
      ... = abs (sum (range (j - 3)) (λ m, x ^ (m + 1) / (m + 3).fact)) + 1 / 2 :
        by rw abshalf
      ... ≤ sum (range (j - 3)) (λ m, abs (x ^ (m + 1) / (m + 3).fact)) + 1 / 2 : 
        add_le_add_right (abv_sum_le_sum_abv _ _) _
      ... ≤ sum (range (j - 3)) (λ m, 1 / (m + 3).fact) + 1 / 2 : 
        add_le_add_right (sum_le_sum (λ n _,
          by rw [abs_div, is_absolute_value.abv_pow abs, ← of_real_nat_cast,
            abs_of_nonneg (nat.cast_nonneg _)];
          refine (div_le_div_right (nat.cast_pos.2 (nat.fact_pos _))).2 
            (pow_le_one _ (abs_nonneg _) hx))) _
      ... ≤ sum (range (j - 3)) (λ m, 1 / 6 * (1 / 2) ^ m) + 1 / 2 : 
        add_le_add_right (sum_le_sum $ λ n hn, begin
          clear hn,
          induction n with n ih,
          { simp [bit0, bit1, mul_add, add_mul] },
          { rw [nat.fact_succ, pow_succ', one_div_eq_inv, nat.cast_mul, mul_inv', ← mul_assoc (1 / 6 : ℝ)],
            refine mul_le_mul (by rwa inv_eq_one_div) _ 
              (inv_nonneg.2 (nat.cast_nonneg _)) 
              (mul_nonneg (by norm_num) (pow_nonneg (by norm_num) _)),
            rw [one_div_eq_inv],
            refine (inv_le_inv (nat.cast_pos.2 (nat.succ_pos _)) (by norm_num)).2 
              (by rw ← nat.cast_two; exact nat.cast_le.2 dec_trivial) }
        end) _
      ... = 1 / 6 * ((1 - (1 / 2) ^ (j - 3)) / (1 - 1 / 2)) + 1 / 2 : 
        by rw [← mul_sum, geo_series_eq]; norm_num
      ... ≤ 1 / 6 * (1 / (1 - 1 / 2)) + 1 / 2 : 
        add_le_add_right (mul_le_mul_of_nonneg_left ((div_le_div_right (by norm_num)).2 
          (sub_le_self _ (pow_nonneg (by norm_num) _))) (by norm_num)) _   
      ... = 5 / 6 : by norm_num) 
    (pow_two_nonneg (abs x))
end
```

#### [ Mario Carneiro (Sep 19 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256944):
Oh, you really did the case n=1 directly

#### [ Mario Carneiro (Sep 19 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256959):
I was thinking you would just prove the general case, there is less stuff floating around that way

#### [ Mario Carneiro (Sep 19 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256986):
well, it's done now, we can revisit later

#### [ Chris Hughes (Sep 19 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134256999):
Not sure what the general case is.

#### [ Mario Carneiro (Sep 19 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134257011):
> `abs (sum k = m,...,infty (x ^ n / n!)) <= (abs a)^m * ((m + 1) / (m! * m))`

#### [ Mario Carneiro (Sep 19 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134257073):
You can also write `exp x - finset.sum ...` instead of that tail sum if you prefer

#### [ Chris Hughes (Sep 19 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134257083):
That makes way more sense.

#### [ Reid Barton (Sep 19 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134257611):
By the way, how hard is it to get log once we have exp? Specifically how hard is it to show that every nonzero complex number is in the range of exp?

#### [ Mario Carneiro (Sep 19 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134258931):
This comes fairly late in the development.
* First you do the real log function. exp is easily seen to be increasing so you get an inverse by IVT. I can expand on this
* `sin` is a bijection from [-pi/2, pi/2] to [-1, 1]. Again, this has subparts
* Injectivity of `exp`: `exp x = 1` iff `x = 2*pi*i*n` for some `n`
* The complex square root function exists. You can define it as `sqrt z = sqrt (abs z) * ((abs z + z) / abs (abs z + z))` off the negative real axis
* If `D` is an interval of length 2pi, and `y : D` is chosen to be a multiple of 2 pi from `2 * arcsin (im (sqrt z))`, then `z = exp (I * y)`, which shows surjectivity of the imaginary part
* By combining surjectivity on real and imaginary parts and injectivity, you get that `exp` is bijective in any domain of the form `{z | z.im \in D}`

#### [ Chris Hughes (Sep 19 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134264128):
How do you get the bounds on cosine?

#### [ Chris Hughes (Sep 19 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134264158):
specifically `1/3 < cos 1 < 2 / 3` the fact that `exp x - x - 1 \le abs x ^ 2 * 3 / 4` is only good enough for `1/4 \le cos 1 \le 7 / 4`

#### [ Chris Hughes (Sep 19 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134264219):
do you need bounds on sine 1 and use cos^2 + sin^2 = 1

#### [ Mario Carneiro (Sep 19 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134265225):
The claim is that `abs (cos x - (1 - x^2 / 2)) < x^2 / 6` for `x \in (0, 1]`. By the `m=4` case of the tail bound on exp, `cos x - (1 - x^2 / 2) = re (exp4 (I*x)) <= abs (exp4 (I*x)) <= x^4 * ((4 + 1) / (4! * 4)) < x^4 / 6 <= x^2 / 6`, where `exp4` is the tail of `exp` starting at 4.

#### [ Mario Carneiro (Sep 19 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134265277):
(sorry! looks like you do need more of the tail bound)

#### [ Mario Carneiro (Sep 19 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134265313):
in metamath, each inequality there is a sublemma (or instance of a lemma), probably don't pack it all together since it is independently useful

#### [ Chris Hughes (Sep 20 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308558):
Major progress. The following have now been proved. @**Mario Carneiro** how do I get continuous exp from the first one?
```lean
lemma exp_bound {x : ℂ} (hx : abs x ≤ 1) {n : ℕ} (hn : 0 < n) :
  abs (exp x - (range n.succ).sum (λ m, x ^ m / m.fact)) ≤ abs x ^ n.succ * (n.fact * n)⁻¹

lemma cos_one_bound : abs' (real.cos 1 - 1 / 2) ≤ 1 / 18
```

#### [ Kenny Lau (Sep 20 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308648):
you might want to specialize the `n` first if you want to prove continuity

#### [ Kenny Lau (Sep 20 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308663):
and you want to prove continuity at 0 first

#### [ Kenny Lau (Sep 20 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308717):
(since exp(y)-exp(x) = exp(x) [exp(y-x)-1])

#### [ Mario Carneiro (Sep 20 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308725):
As I mentioned, if you take `n = 1` then you have `abs (exp x - 1) <= abs x`

#### [ Kenny Lau (Sep 20 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308769):
so combining our statements, `|exp(y)-exp(x)| <= exp(x) |y-x|`

#### [ Kenny Lau (Sep 20 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308802):
so set `delta = epsilon/exp(x)`

#### [ Mario Carneiro (Sep 20 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308914):
wait, isn't the bound off by one? the claim was about `sum m=n ... infty (x^m/m!)` which should be `abs (exp x - (range n).sum (λ m, x ^ m / m.fact))`

#### [ Mario Carneiro (Sep 20 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134308960):
the RHS looks right

#### [ Kenny Lau (Sep 20 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134309088):
well n=1 gives `|exp(x)-1-x| <= |x|^2`

#### [ Mario Carneiro (Sep 20 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134309323):
I guess the order is right, the constant is a bit off

#### [ Mario Carneiro (Sep 20 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134309338):
```
lemma exp_bound {x : ℂ} (hx : abs x ≤ 1) {n : ℕ} (hn : 0 < n) :
  abs (exp x - (range n).sum (λ m, x ^ m / m.fact)) ≤ abs x ^ n * (n.succ / (n.fact * n)) := sorry
```

#### [ Chris Hughes (Sep 20 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134312362):
Does it matter? We have everything we need for pi
```lean
lemma cos_one_le : real.cos 1 ≤ 5 / 9 :=
calc real.cos 1 ≤ 1 / 2 + 1 / 18 : sub_le_iff_le_add.1 (abs_sub_le_iff.1 cos_one_bound).1
... = 5 / 9 : by norm_num

lemma le_cos_one : 4 / 9 ≤ real.cos 1 :=
calc 4 / 9 = 1 / 2 - 1 / 18 : by norm_num
... ≤ real.cos 1 : sub_le_of_sub_le (abs_sub_le_iff.1 cos_one_bound).2

lemma cos_two_le : real.cos 2 ≤ -31 / 81 :=
calc real.cos 2 = real.cos (2 * 1) : congr_arg real.cos (by simp [bit0])
... = _ : real.cos_two_mul 1
... ≤ 2 * (5 / 9) ^ 2 - 1 : 
  sub_le_sub_right (mul_le_mul_of_nonneg_left 
  (by rw [pow_two, pow_two]; exact 
    mul_self_le_mul_self (le_trans (by norm_num) le_cos_one) _)
  (by norm_num)) _
... = -31 / 81 : by norm_num
```

#### [ Patrick Massot (Sep 20 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134312866):
Wonderful! Can you get pi before tomorrow then?

#### [ Chris Hughes (Sep 20 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134312999):
If someone tells me how to turn my inequalities about exp into a proof of continuity. I don't know what the lemma is.

#### [ Patrick Massot (Sep 20 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313023):
Did you push everything?

#### [ Patrick Massot (Sep 20 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313051):
Doesn't seem so

#### [ Chris Hughes (Sep 20 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313053):
Not yet

#### [ Patrick Massot (Sep 20 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313077):
It would be easier to see what inequalities you have

#### [ Chris Hughes (Sep 20 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313314):
Just pushing now

#### [ Reid Barton (Sep 20 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313328):
Do we know that $$\mathbb{C}$$ is a normed group?

#### [ Reid Barton (Sep 20 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313791):
I guess it would be quite easy to add. Then you should be able to use `tendsto_iff_norm_tendsto_zero` and `tendsto_of_tendsto_of_tendsto_of_le_of_le` somehow

#### [ Reid Barton (Sep 20 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313820):
or maybe even `squeeze_zero`

#### [ Mario Carneiro (Sep 20 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313883):
There should be a theorem about continuity on metric spaces

#### [ Mario Carneiro (Sep 20 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313917):
`continuous_of_metric`

#### [ Mario Carneiro (Sep 20 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134313943):
oh wait, you just want continuity at zero, that is `tendsto_nhds_of_metric`

#### [ Mario Carneiro (Sep 20 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134314004):
just rewrite `dist 0 x` to `abs x` and you should be set with a straight epsilon delta proof

#### [ Mario Carneiro (Sep 20 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134314065):
You shouldn't make your constants too precise, it makes the proof harder for norm_num and the gain is not that great. In particular you should weaken the second theorem to `cos 2 < 0`

#### [ Chris Hughes (Sep 20 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327309):
So I have `lemma tendsto_exp_zero_one : tendsto exp (nhds 0) (nhds 1) :=`

#### [ Chris Hughes (Sep 20 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327314):
How do I get continuity?

#### [ Kenny Lau (Sep 20 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327360):
note that exp(x+h) = exp(x) exp(h)

#### [ Mario Carneiro (Sep 20 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327365):
do we know that C is a topological ring?

#### [ Chris Hughes (Sep 20 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327446):
@**Mario Carneiro** yes

#### [ Kenny Lau (Sep 20 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327484):
`\forall x, tendsto (\lambda h, exp x * exp h) (nhds 0) (nhds (exp x * 1))`

#### [ Kenny Lau (Sep 20 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327497):
`\forall x, tendsto (\lambda h, exp (x+h)) (nhds 0) (nhds (exp x))`

#### [ Kenny Lau (Sep 20 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327515):
`\forall x, tendsto exp (nhds x) (nhds (exp x))`

#### [ Chris Hughes (Sep 20 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327544):
What lemmas are you applying Kenny?

#### [ Mario Carneiro (Sep 20 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327620):
Ah, found it: `continuous_mul` is what you want

#### [ Mario Carneiro (Sep 20 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327646):
to deduce the first of Kenny's statements

#### [ Mario Carneiro (Sep 20 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327667):
wait no, `tendsto_mul`

#### [ Mario Carneiro (Sep 20 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327741):
the second one is easy/algebraic, and the third is that lemma that Patrick mentioned

#### [ Mario Carneiro (Sep 20 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327920):
Alternatively you could just use continuity of subtraction to avoid mentioning homeos

#### [ Kenny Lau (Sep 20 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327987):
from 2 to 3 can be easily done with epsilon-delta

#### [ Kenny Lau (Sep 20 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134327994):
would not recommend epsilon-delta to deduce 1

#### [ Mario Carneiro (Sep 20 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328003):
don't listen to kenny, you are done with epsilons now

#### [ Kenny Lau (Sep 20 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328021):
we're in the post-epsilon stage of maths, right

#### [ Mario Carneiro (Sep 20 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328141):
if you know `tendsto (\lambda h, exp (x+h)) (nhds 0) (nhds (exp x))` then if you compose with `(\lambda y, y - x)` which is continuous then you get `tendsto (\lambda y, exp (x+(y - x))) (nhds x) (nhds (exp x))`

#### [ Chris Hughes (Sep 20 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328347):
My goal is `tendsto (λ (x_1 : ℂ), exp x) (nhds 0) (nhds 1)` I try `apply tendsto_exp_zero_one`, which looks like this `tendsto_exp_zero_one : tendsto (λ x : ℂ, exp x) (nhds (0 : ℂ)) (nhds (1 : ℂ))` and it hangs.

#### [ Mario Carneiro (Sep 20 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328427):
use exact

#### [ Mario Carneiro (Sep 20 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328505):
apply will go crazy unfolding pis because of a bug

#### [ Chris Hughes (Sep 20 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328583):
`exact this` fails
```lean
x : complex,
this :
  @filter.tendsto.{0 0} complex complex (λ (x : complex), complex.exp x)
    (@nhds.{0} complex
       (@uniform_space.to_topological_space.{0} complex
          (@metric_space.to_uniform_space'.{0} complex complex.metric_space))
       (@has_zero.zero.{0} complex complex.has_zero))
    (@nhds.{0} complex
       (@uniform_space.to_topological_space.{0} complex
          (@metric_space.to_uniform_space'.{0} complex complex.metric_space))
       (@has_one.one.{0} complex complex.has_one))
⊢ @filter.tendsto.{0 0} complex complex (λ (x_1 : complex), complex.exp x)
    (@nhds.{0} complex
       (@uniform_space.to_topological_space.{0} complex
          (@metric_space.to_uniform_space'.{0} complex complex.metric_space))
       (@has_zero.zero.{0} complex complex.has_zero))
    (@nhds.{0} complex
       (@uniform_space.to_topological_space.{0} complex
          (@metric_space.to_uniform_space'.{0} complex complex.metric_space))
       (@has_one.one.{0} complex complex.has_one))
```

#### [ Chris Hughes (Sep 20 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328600):
I see the problem.

#### [ Chris Hughes (Sep 20 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328612):
Silly me

#### [ Mario Carneiro (Sep 20 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328653):
is that sarcasm? because I don't

#### [ Chris Hughes (Sep 20 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328719):
`x_1` instead of `x` on first line

#### [ Mario Carneiro (Sep 20 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134328864):
by the way, `convert` is a nice way to diagnose these bugs

#### [ Chris Hughes (Sep 20 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134329021):
What's the lemma I use for composing with sub

#### [ Chris Hughes (Sep 20 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134329079):
`tends.comp` d'oh

#### [ Chris Hughes (Sep 20 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134330094):
This must be easy surely
```lean
tendsto (λ (y : ℂ), y - x) (nhds x) (nhds 0)
```

#### [ Mario Carneiro (Sep 20 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134330122):
by the way I suggest you do all your compositions at the start, getting something like `tendsto (\lam y, exp x * exp (y - x)) (nhds x) (nhds (exp x * exp (x - x)))`

#### [ Chris Hughes (Sep 20 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134330209):
I worked that bit out. Do I have to use `tendsto_sub` and the identity and constant functions?

#### [ Mario Carneiro (Sep 20 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134330229):
yes

#### [ Mario Carneiro (Sep 20 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134330252):
that's the easiest way, at least

#### [ Chris Hughes (Sep 20 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134331002):
exp is continuous is now a fact.

#### [ Kenny Lau (Sep 20 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134331114):
how much time do we still have?

#### [ Patrick Massot (Sep 20 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134331370):
Here it's 9:27pm

#### [ Patrick Massot (Sep 20 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134331423):
So 8:27pm in London

#### [ Patrick Massot (Sep 20 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134331429):
So we have 12 hours

#### [ Patrick Massot (Sep 20 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134331434):
roughly

#### [ Patrick Massot (Sep 20 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134331458):
Who's going to tell Kevin tomorrow? @**Johan Commelin** ?

#### [ Chris Hughes (Sep 20 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332215):
How do you prove `continuous real.sin` from `continuous complex.sin`?

#### [ Mario Carneiro (Sep 20 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332221):
continuity of real part

#### [ Mario Carneiro (Sep 20 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332228):
and continuity of real injection

#### [ Mario Carneiro (Sep 20 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332274):
How did you define `real.sin`?

#### [ Patrick Massot (Sep 20 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332761):
https://github.com/leanprover-community/mathlib/blob/4c670fc338c3e6cdff8c1f01e03f1279fd3926bd/data/complex/exponential.lean#L349

#### [ Chris Hughes (Sep 20 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332776):
(complex.sin x).re

#### [ Patrick Massot (Sep 20 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332789):
So continuity should indeed follow as Mario wrote

#### [ Chris Hughes (Sep 20 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332800):
I couldn't find `continuous_re`

#### [ Patrick Massot (Sep 20 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134332815):
Do you want us to prove it, or did you do it already?

#### [ Mario Carneiro (Sep 20 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134333423):
I think there is a theorem that `re` is a contracting map, which is enough to prove continuity

#### [ Mario Carneiro (Sep 20 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134333500):
`abs_re_le_abs`

#### [ Chris Hughes (Sep 20 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134334686):
I managed to work it out. I thought there was some simple proof without deltas, but deltas is really short anyway.

#### [ Patrick Massot (Sep 20 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134334711):
How far are you from pi then?

#### [ Chris Hughes (Sep 20 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134334779):
More or less there. Just have to apply IVT which I have already proved.

#### [ Patrick Massot (Sep 20 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134334986):
So, who's writing to Kevin tomorrow?

#### [ Chris Hughes (Sep 20 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134335942):
```lean
def pi : ℝ := 2 * classical.some exists_cos_eq_zero
```

#### [ Kenny Lau (Sep 20 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336002):
then pi can be 3*3.14...?

#### [ Mario Carneiro (Sep 20 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336024):
have you proven that `cos (pi/2) = 0`?

#### [ Chris Hughes (Sep 20 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336148):
`lemma exists_cos_eq_zero : ∃ x, 1 ≤ x ∧ x ≤ 2 ∧ cos x = 0 ` @**Kenny Lau**

#### [ Kenny Lau (Sep 20 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336153):
fair enough

#### [ Mario Carneiro (Sep 20 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336162):
also `sin (pi/2) = 1`

#### [ Mario Carneiro (Sep 20 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336172):
the rest should be easy

#### [ Kenny Lau (Sep 20 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336183):
well sin(pi/2)=1 implies cos(pi/2)=0...

#### [ Mario Carneiro (Sep 20 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336248):
but it looks like he proved `cos (pi/2) = 0`, which only implies `sin(pi/2) = +- 1`

#### [ Mario Carneiro (Sep 20 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336301):
Metamath uses the lemma that `sin x > 0` on `(0, 2]` by double angle formulas on what you already have

#### [ Chris Hughes (Sep 20 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336386):
I'm sure that's all quite easily doable.

#### [ Mario Carneiro (Sep 20 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336400):
yes, it's mostly smooth sailing at this point

#### [ Chris Hughes (Sep 20 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134336439):
I pushed.

#### [ Kenny Lau (Sep 20 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134337086):
I'm afraid it's now 05:03 AM in Hong Kong and I must leave now...

#### [ Kenny Lau (Sep 20 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134337111):
although I will wake up 4 hours later

#### [ Mario Carneiro (Sep 20 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134337124):
ooh, you are 12 hours away from me

#### [ Kevin Buzzard (Sep 21 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134343929):
I've been 50 for about 10 minutes

#### [ Chris Hughes (Sep 21 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134343951):
Happy Birthday!

#### [ Kevin Buzzard (Sep 21 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134343958):
Holey Moley we have pi!

#### [ Kevin Buzzard (Sep 21 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134343964):
I am so happy!

#### [ Kevin Buzzard (Sep 21 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/141825-kbb/topic/sine%20and%20cosine%20and%20pi/near/134344081):
I need to go to bed!


{% endraw %}
