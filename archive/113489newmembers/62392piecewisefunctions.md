---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/62392piecewisefunctions.html
---

## [new members](index.html)
### [piecewise functions](62392piecewisefunctions.html)

#### [Aymon Wuolanne (Dec 20 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152232475):
Does anyone have any tips for dealing with piecewise functions, in particular showing that they're continuous? I have something like the following in mind:
```
variables (a : ℝ) (f : ℝ → ℝ) (g : ℝ → ℝ) 
def pw : ℝ → ℝ := λ x, if x ≤ a then f x else g x 
lemma continuous_pw : continuous f → continuous g → f a = g a → continuous (pw a f g) := sorry 
```

#### [Jeremy Avigad (Dec 20 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152234041):
Coincidentally, I just issued a pull request with some additions to the analysis library. There is a lemma called `tendsto_if` which will be helpful: https://github.com/avigad/mathlib/blob/limit_stuff/order/filter.lean#L1257-L1261. I'd use the fact that a function is continuous if it is continuous at every point (which used to be called `continuous_iff_tendsto` but in my PR is `continuous_iff_continuous_at`. Using `metric_space` you can unwrap the definition of neighborhoods in terms of distance.

#### [Reid Barton (Dec 20 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152236649):
There's also `continuous_if` and `continuous_subtype_is_closed_cover`

#### [Patrick Massot (Dec 20 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152238561):
```quote
Coincidentally, I just issued a pull request with some additions to the analysis library. 
```
 You should expect a lot of homework now, that Mario guy is merciless...

#### [Patrick Massot (Dec 20 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152238630):
Seriously I'm very excited to see some PR from your analysis work. I hope you already discussed it enough with Mario, and will convince Johannes quickly. It would be very nice to have a topology PR merge sprint before Amsterdam (or even before Christmas, and then a second one before Amsterdam)

#### [Kenny Lau (Dec 20 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152238643):
@**Patrick Massot** merciless

#### [Johan Commelin (Dec 20 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152239509):
Completely agree. Let's get these PRs moving.

#### [Aymon Wuolanne (Dec 20 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240099):
Thanks! I think I should be able to get it working with `continuous_if`

#### [Aymon Wuolanne (Dec 20 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240118):
Side note: `frontier` is defined as `closure s \ interior s`, isn't this usually referred to as the boundary?

#### [Johan Commelin (Dec 20 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240169):
I've never heard of `frontier` before. I learned it as `boundary`.

#### [Mario Carneiro (Dec 20 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240177):
I thought frontier was `closure s \ s`

#### [Johan Commelin (Dec 20 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240204):
So what is `s \ interior s` called?

#### [Reid Barton (Dec 20 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240214):
apparently it is sometimes called the boundary! not even making this up

#### [Reid Barton (Dec 20 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240216):
https://en.wikipedia.org/wiki/Boundary_(topology)

#### [Mario Carneiro (Dec 20 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240264):
```quote
So what is `s \ interior s` called?
```
 outliers?

#### [Johan Commelin (Dec 20 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240292):
https://www.thesaurus.com/browse/boundary enough words to choose from (-;

#### [Mario Carneiro (Dec 20 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240303):
periphery is nice

#### [Johan Commelin (Dec 20 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240314):
is borderline acceptable

#### [Mario Carneiro (Dec 20 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240318):
it's borderline acceptable

#### [Mario Carneiro (Dec 20 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240374):
but actually I find very little use for these concepts, they are more a historical note for me

#### [Mario Carneiro (Dec 20 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152240378):
boundary is useful though

#### [Jeremy Avigad (Dec 20 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152284935):
Mario has gone easy on me so far. I am about to get on a flight to California to visit my in-laws, but I should be able to make the corrections there.

#### [Mario Carneiro (Dec 20 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152285351):
It looks pretty good. there is absolutely no chance of a conflict of interest, yep

#### [Patrick Massot (Dec 20 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/piecewise%20functions/near/152285645):
Would you give this PR a master's thesis?

