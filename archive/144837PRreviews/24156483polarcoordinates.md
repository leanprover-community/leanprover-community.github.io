---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/24156483polarcoordinates.html
---

## Stream: [PR reviews](index.html)
### Topic: [#483 polar coordinates](24156483polarcoordinates.html)

---

#### [Kevin Buzzard (Nov 17 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147885598):
I proved some basic stuff in my undergraduate course, e.g. using polar coordinates to prove that a non-zero complex number has exactly n n'th roots if n>=1 (I am still a bit confused as to why n>=1 comes up so often in maths and so rarely in computer science; maybe we count stuff more). Anyway, @**Abhimanyu Pallavi Sudhir** has written up some of this stuff in Lean, including polar coordinates, which I guess didn't seem to be there before.

#### [Kevin Buzzard (Nov 17 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147885899):
I guess the main thing I'm not sure about is how to put the concept of "angle" into Lean -- in maths it's the unit circle in the complexes, or $$\mathbb{R}/2\pi\mathbb{Z}$$, or $$[0,2\pi)$$ or whatever. But there are implementation issues in Lean which I feel less confident about.

#### [Kevin Buzzard (Nov 17 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147885901):
The thing you want is a map from the reals to the angles, so perhaps the quotient is best?

#### [Reid Barton (Nov 17 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147887375):
Nice! It looks like complex nth roots are quite close then. With those someone could try to prove FTA.

#### [Chris Hughes (Nov 17 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147887385):
Do you have a link to a proof that uses the existence of complex nth roots?

#### [Reid Barton (Nov 17 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147887425):
https://ncatlab.org/nlab/show/fundamental+theorem+of+algebra#classical_fta_via_advanced_calculus

#### [Chris Hughes (Nov 17 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147887436):
Thaanks

#### [Reid Barton (Nov 17 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147887718):
Think it looks doable?

#### [Reid Barton (Nov 17 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147887757):
There are some bits having to do with estimating sums which could be a little awkward

#### [Chris Hughes (Nov 17 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147888275):
I'm not sure how to do Bolzano Weirstrass, because I don't know too much about analysis in Lean, or analysis in general for that matter. I think it's stated in a different way. The rest looks doable. What are the parts about estimating sums that you thought looked difficult?

#### [Reid Barton (Nov 17 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147888549):
I guess just the statement that f(z) goes to infinity as z does. I was also thinking of the last bit of (2), but that's just continuity.

#### [Chris Hughes (Nov 17 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147888552):
Yeah, I didn't quite notice that bit. Probably the hardest part.

#### [Reid Barton (Nov 17 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147888558):
I think paragraph 1 is easier than it sounds from the proof written out there

#### [Reid Barton (Nov 17 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147889672):
Minus the part about f(z) going to infinity as z does, I mean.

#### [Reid Barton (Nov 17 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147891219):
Well, it's easy modulo some more basic facts which we don't seem to have yet

#### [Reid Barton (Nov 17 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147891311):
The proof I had in mind was: We want to show that |f| attains a global minimum somewhere. Pick r large enough so that |z| > r implies |f(z)| > |f(0)|. The ball {|z| <= r} is compact (missing fact 1), so its image under |f| is a nonempty compact subset of R and therefore contains a smallest element (missing fact 2). If w is some preimage of this smallest element, then |f| is globally minimized at w, by cases on whether or not |z| <= R.

#### [Kenny Lau (Nov 17 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147891331):
I think we know that [0,1] is compact

#### [Kenny Lau (Nov 17 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147891333):
I don't know if we have extreme value theorem

#### [Reid Barton (Nov 17 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147891385):
Missing fact 1 is not really missing, it's just not stated in that exact form. I'm not sure about missing fact 2

#### [Sebastien Gouezel (Nov 17 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147891495):
I have missing fact 2 somewhere.

#### [Sebastien Gouezel (Nov 17 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147891555):
Maybe it is time for me to dump a PR with a lot of useful random facts...

#### [Mario Carneiro (Nov 18 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147895430):
useful random facts are my favorite

#### [Sebastien Gouezel (Nov 18 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147918444):
Done in #PR484. The extreme value theorem is here under the sweet name of `exists_forall_le_of_compact_of_continuous` :)

#### [Chris Hughes (Nov 18 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147929675):
I mostly proved this today, apart from a few annoying, but not too difficult sorries. Is this the right statement?
```lean
lemma easy_growth_lemma : ∀ (p : polynomial ℂ), 0 < degree p →
  ∀ x : ℝ, ∃ r : ℝ, ∀ z : ℂ, r < z.abs → x < (p.eval z).abs
```

#### [Chris Hughes (Nov 18 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147932354):
Sorries now filled in.

#### [Kevin Buzzard (Nov 18 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147932422):
You've proved polynomials are continuous at infinity. There will be a way of stating this with filters

#### [Kevin Buzzard (Nov 18 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147932475):
Think of x as being the epsilon for infinity, and r as being the delta

#### [Kevin Buzzard (Nov 18 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147932484):
Degree > 0 is just the assumption that p sends infinity to infinity

#### [Chris Hughes (Nov 18 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147932497):
Haven't I proved p sends infinity to infinity?

#### [Chris Hughes (Nov 18 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147932540):
More or less. Does that mean anything rigorously?

#### [Chris Hughes (Nov 18 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147932553):
I think I get what you mean actually.

#### [Chris Hughes (Nov 18 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147932607):
If I extended the complex numbers with infinity, then p sends infinity to infinity, but you need continuity at infinity to prove the limit is the same as the evaluation.

#### [Kevin Buzzard (Nov 18 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933297):
Right. There's a topological space "complex numbers union infinity" with the "open balls centre infinity" being exactly infinity union these regions |z| > M for M large, and polynomials, thought of as continuous maps from C to C, extend to continuous maps from this extended space to itself.

#### [Chris Hughes (Nov 18 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933314):
Is there some clever easy proof of this by just proving add mul and neg are continuous at infinity.

#### [Kevin Buzzard (Nov 18 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933366):
So this new space is called $$\mathbb{P}^1(\mathbb{C})$$, and if you put the effort into topologising it then not only are mul and neg continuous, but so is reciprocal (it swaps infinity and 0). I don't know whether it's worth the effort doing it this way in Lean but that's typically how it's done in a Riemann Surfaces course.

#### [Kevin Buzzard (Nov 18 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933410):
Note that power series are typically not continuous at infinity, e.g. $$\sin(x)$$ is zero for arbitrarily large real $$x$$, but $$\sin(ix)$$ is something like $$i\mathrm{sinh}(x)$$ which is huge for $$x$$ large.

#### [Kevin Buzzard (Nov 18 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933418):
The lingo is that functions like `sin` have "essential singularities" at infinity.

#### [Chris Hughes (Nov 18 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933473):
I think I could write a shorter proof inspired by that idea though.

#### [Chris Hughes (Nov 18 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933478):
Without going to a load of trouble definining a new topological space

#### [Kevin Buzzard (Nov 18 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933796):
Of course, one day someone will define projective n-space in Lean anyway, and you'll be able to use that.

#### [Kevin Buzzard (Nov 18 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933837):
The variety, the scheme, the real manifold and the complex manifold all need doing :-)

#### [Chris Hughes (Nov 18 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147934663):
How would one state continuous at infinity in the simplest way?

#### [Kevin Buzzard (Nov 19 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147935871):
if `nhds infinity` exists (and it might well not) then you could use that, but it would just be a fancy translation of your "epsilon delta" statement.

#### [Kenny Lau (Nov 19 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147935931):
what is "infinity" in Q_p?

#### [Chris Hughes (Nov 19 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147936317):
```quote
if `nhds infinity` exists (and it might well not) then you could use that, but it would just be a fancy translation of your "epsilon delta" statement.
```
 I guess it's `at_top`, which is defined on a preorder, so I think `abs x \le abs y` is a preorder.

#### [Chris Hughes (Nov 19 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147936393):
But that's not really what I want I don't think. Because at some point I still need to define multiplication by infinity to go down that route.

#### [Mario Carneiro (Nov 19 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147944261):
by the way, I find that statement interesting not because of this continuity business but because that's part 1 of FTA

#### [Reid Barton (Nov 19 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147944271):
that's why it's in a thread titled "polar coordinates" :)

#### [Mario Carneiro (Nov 19 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147944940):
> Note that power series are typically not continuous at infinity, e.g. sin(x) is zero for arbitrarily large real x

I don't think this is true...

#### [Scott Morrison (Nov 19 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147945389):
surely "for arbitrarily large" implies an existential quantifier, not a universal one...?

#### [Kevin Buzzard (Nov 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953327):
I meant the true thing, regardless of how one can parse what I wrote and I agree that there may be a debate here. I am just pointing out that the analogue of Chris'lemma is false. Kenny -- you know what projective 1 space is over any field, as a variety. Making it an object that you can do analysis on is a different matter.

#### [Kevin Buzzard (Nov 19 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953362):
I have several volumes in my office about how to do analysis and geometry over totally disconnected fields. The most fashionable answer nowadays is to use adic spaces.

#### [Mario Carneiro (Nov 19 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953367):
I don't think CP^1 is as nice as you say, there is a reason infinity isn't normally treated as a number

#### [Mario Carneiro (Nov 19 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953409):
I don't think multiplication is continuous?

#### [Mario Carneiro (Nov 19 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953416):
plus I think there are still some undefined combinations like infty + infty and infty * 0

#### [Patrick Massot (Nov 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953699):
Mario, Kevin never said CP¹ has a nice algebraic structure

#### [Mario Carneiro (Nov 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953776):
he claimed that all polynomials are continuous?

#### [Mario Carneiro (Nov 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953783):
multiplication is a polynomial

#### [Patrick Massot (Nov 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953787):
The only case where infinity is sometimes treated as a number in this context is when discussing homographies

#### [Patrick Massot (Nov 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953799):
He wrote that polynomial extend to P¹ as continuous functions

#### [Kevin Buzzard (Nov 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953800):
Any rational function is continuous

#### [Kevin Buzzard (Nov 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953806):
(2+z)/(3+z^2) is continuous

#### [Kevin Buzzard (Nov 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953815):
but the trick is not to use infinity in your polynomials

#### [Kevin Buzzard (Nov 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953817):
just in your values it can take

#### [Kevin Buzzard (Nov 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953819):
and eat

#### [Mario Carneiro (Nov 19 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953862):
I agree that there should be a nicer way to deal with meromorphic functions to avoid all the horrible case splits

#### [Mario Carneiro (Nov 19 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953880):
defining 1/0 = 0 helps a lot, but it doesn't solve all the problems

#### [Patrick Massot (Nov 19 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953964):
meromorphic functions can be defined as CP¹-valued holomorphic functions

#### [Patrick Massot (Nov 19 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953977):
no problem

#### [Mario Carneiro (Nov 19 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953986):
what's a holomorphic function

#### [Mario Carneiro (Nov 19 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953989):
in a general sense

#### [Patrick Massot (Nov 19 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953999):
you ask for local charts are source and target where you see an undergraduate holomorphic function

#### [Patrick Massot (Nov 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147954051):
same as definining smooth functions between smooth manifolds

#### [Mario Carneiro (Nov 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147954059):
wait so it's just a manifold?

#### [Patrick Massot (Nov 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147954060):
complex manifold

#### [Patrick Massot (Nov 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147954063):
coordinate changes have to be holomorphic

#### [Mario Carneiro (Nov 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147954084):
hm... I'm sensing some circularity

#### [Patrick Massot (Nov 19 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147954093):
in case of CP¹ you can get away with two charts

#### [Patrick Massot (Nov 19 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147954096):
and coordinate change is 1/z

#### [Chris Hughes (Nov 27 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/148409615):
I mostly finished off a proof of the fundamental theorem of algebra today. The missing parts are complex nth roots and, the fact that it attains it's minimum value, given that it tends to infinity.

#### [Chris Hughes (Nov 28 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/148678532):
Do we have that closed balls of complexes are compact?

#### [Reid Barton (Nov 28 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/148679171):
We have it for R but it looks like a little bit of work is required to get it for C. I would guess that @**Sebastien Gouezel** has something useful here

#### [Sebastien Gouezel (Nov 28 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/148694231):
No, we don't have it. Even for reals, this is only in #PR484. I will add the complex case to this PR, it is not hard and definitely useful.

#### [Sebastien Gouezel (Nov 28 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/148705208):
#PR484 now contains the fact that C is proper, i.e., closed balls (and therefore any bounded closed set) are compact.

#### [Reid Barton (Nov 28 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/148712221):
Oh thanks! Somehow I had missed #484 entirely.

#### [Chris Hughes (Nov 28 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/148748308):
Back to the original topic, I feel like `nth_root` should return real nth roots of negative numbers when they exist. Currently it defaults to zero for negative numbers

#### [Kevin Buzzard (Dec 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/150679507):
Maybe it could just return `-nth_root (-x)` for negative `x`.

#### [Mario Carneiro (Dec 01 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/150679806):
but that's wrong for even n

#### [Johan Commelin (Dec 01 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/150679860):
???

#### [Johan Commelin (Dec 01 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/150679866):
We're talking about `real.nth_root`, not the complex version

#### [Kevin Buzzard (Dec 01 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/150679922):
It's junk for even n

#### [Kevin Buzzard (Dec 01 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/150679923):
There's no right answer

#### [Johan Commelin (Dec 01 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/150679973):
37

#### [Reid Barton (Dec 25 2018 at 05:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152496581):
```quote
#PR484 now contains the fact that C is proper, i.e., closed balls (and therefore any bounded closed set) are compact.
```
 And now it is merged, so we are one step closer to FTA.

#### [Chris Hughes (Dec 25 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152500414):
I do have FTA on my PC. Just waiting for polar coordinates and multiplicity to be merged.

#### [Mario Carneiro (Dec 25 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152502597):
Re: `nth_root`, do we need this definition? I didn't read it close enough last time but I see now that it only allows natural number roots. Why not just give `real` a has_pow instance?

#### [Mario Carneiro (Dec 25 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152502603):
i.e. `x ^ y = exp (y * log x)` discounting edge cases

#### [Mario Carneiro (Dec 25 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152502604):
then you can use `x ^ (1/n)` for `nth_root`

#### [Chris Hughes (Dec 25 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152502794):
I think that makes a lot of sense.

#### [Sebastien Gouezel (Dec 26 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152543457):
```quote
```quote
#PR484 now contains the fact that C is proper, i.e., closed balls (and therefore any bounded closed set) are compact.
```
 And now it is merged, so we are one step closer to FTA.
```
 Thanks a lot @**Mario Carneiro** , for all the hard work and cleaning up the mess.

#### [Patrick Massot (Dec 26 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152545869):
Sébastien, did you manage to learn something from this effort? It's difficult to see what Mario did because he squashed everything into one commit (I guess I could diff with the relevant branch)

#### [Sebastien Gouezel (Dec 26 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152556998):
Mario added a commit to the branch, before squashing everything when he commited to mathlib. So, you can see the modifications he made, at https://github.com/leanprover/mathlib/pull/484/commits/76fa5711faa89549e7b4e234715d256711f32f33. Very instructive!

#### [Patrick Massot (Dec 26 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152559779):
Nice. I wish we could still keep your way of announcing intermediate statements, and then Mario-compress the proof. But I guess the compressed proof often skip your intermediate statements anyway

#### [Sebastien Gouezel (Dec 26 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152560611):
I hope that in longer proofs it will be possible to keep the intermediate statements, but for 10-lines proofs that are compressed down to 3 lines I really don't care.

In Isabelle, there is really strong emphasis on proofs that are a sequence of `have ...`, for (at least) the three following reasons:
* readability
* maintainability (if a proof breaks because the statement of a theorem has changed, or automation has changed, then with `have ...` you can see what was being proved, and the breakage is very localized, while with a sequence of tactics or a very long expression you can notice the breaking much later after it has happened, and this is much harder to fix)
* speed: different `have` statements can be handled in parallel, so on modern machines with a lot of cores even the proof of a single theorem can be split into many subtasks and therefore be processed very quickly.

If I understand correctly, readability is not a goal in mathlib (although  I would very much like the opposite, but my opinion is not really important). For maintainability, if Mario is ready to maintain everything by himself this is not really an issue :) And for speed, if I understand correctly the proof of a single theorem is processed sequentially in Lean 3 (or am I wrong? is this going to change in Lean 4?)

#### [Patrick Massot (Dec 26 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152560741):
Maybe one day Mario will get tired, or too busy, so maybe we should worry more about maintainability. It seems to me he is already less available than one year ago. About parallel processing, you are correct about Lean 3, and it could change in Lean 4 (that's one of the improvement that was flagged as very difficult to build in Lean 3)

#### [Mario Carneiro (Dec 27 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152577881):
You can see now why it took so long for me to merge this PR. Every time I looked at it I thought that it can be done better but I couldn't find the time to do the cleanup. As for intermediate statements, I agree that they are useful but I think they should be chosen carefully. Sometimes you can even do a necessary part of the proof by a judiciously chosen `change` that also reports a bit of info about what's going on at the same time. But in the long term I have more hope for methods like `#explode` for displaying proofs regardless of how they are proven. This separates concerns between the proof construction process and proof review for people who actually want to learn some maths from the proof

#### [Mario Carneiro (Dec 27 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152577938):
Speed was another reason I felt it necessary to revise many of Sebastien's proofs. I'm not entirely sure why but they mostly took 10s or more, and it was really noticeable. I tried to refrain from too much `simp` in the revisions

#### [Mario Carneiro (Dec 27 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152578095):
But I'm glad I haven't discouraged him from submitting PRs - I see a bunch more now. Hopefully we can make some more progress on analysis with the new additions

#### [Sebastien Gouezel (Dec 27 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152592048):
I am trying to submit much smaller PRs, hopefully this is a better strategy.

#### [Sebastien Gouezel (Dec 27 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152592297):
If you haven't started looking at #PR464 Bounded continuous functions, I can also split it into smaller chunks if you want. Tell me!

