---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39883Appliedstatistics.html
---

## Stream: [general](index.html)
### Topic: [Applied statistics](39883Appliedstatistics.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129172046):
I haven't done any statistics in a while. Can someone point me to a formula I can use to calculate the probability that `x ≤ y` if both are normally distributed random variables?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 06 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129172106):
mean and variance?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129172114):
Yes using the mean and variance.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129172989):
Do you have a formula for that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176063):
This is like taking the 2D Gaussian and drawing a line across the distribution; if you project parallel to that line the projected distribution is another Gaussian so the answer should be Erf of some simple term involving the mean and variance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176241):
I'm not knowledgeable enough to make sense of that answer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176391):
Maybe it would be useful to reveal more context of my problem. I have two tactics. I'm running them each ~30 times, measuring average running time and variance. I'd like to check if one is actually faster than the other

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 03:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176399):
The difference is not big but I'd like to know where I'm heading with the optimization

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176445):
If the variables are $$X \sim N(a, \sigma_X)$$ and $$Y \sim N(b, \sigma_Y)$$ then let $$X = a + \sigma_X X'$$ and $$Y = b + \sigma_Y Y'$$ where $$X'$$ and $$Y'$$ are standard normal variables; then $$a+\sigma_X X' \le b + \sigma_Y Y'$$ iff $$\sigma_Y Y' - \sigma_X X' \ge a - b$$. But $$\sigma_Y Y' - \sigma_X X'$$ is a Gaussian with SD $$\sqrt{\sigma^2_X + \sigma^2_Y}$$, so the probability is $$\mathrm{erf}\frac{a-b}{\sqrt{\sigma^2_X + \sigma^2_Y}}$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176560):
At the first order the answer to your question is easy: If the mean is less then it's probably an improvement

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176562):
but the larger the standard deviation the less confidence you have in this assertion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176570):
Right. One of them has a pretty large standard deviation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176571):
Is it weird that it only started making sense when you brought up the formula? :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176636):
By the way there is a square root in the last two math blocks there, but in my mathjax display I only see a conspicuous space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176681):
I see the same. You were missing a bracket and a $ so I ended up compiler your latex myself. I see both square roots

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176734):
I think I've fixed all the delimiter problems above, but the square root still isn't rendering. You know how to fix it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176781):
You're right, it's now rendering almost properly. I haven't played with mathjax so I wouldn't know where to start

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176801):
MSE uses mathjax and there isn't much trouble using $$\sqrt x$$ there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 06 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176803):
Zulip actually uses katex, not mathjax

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176804):
$$x$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176844):
you have to use double dollar delimiter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176847):
does \[\sqrt x\] work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176848):
Nice thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176855):
\[ \sqrt x \]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176856):
No

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176857):
$$\sqrt x $$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176858):
Not sure how to do display math either

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176862):
```math
\sqrt  x
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176863):
oh, there it is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129176915):
If you do "three ticks" math (like you would for Lean code), then it seems to work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177084):
If I try my tactic on three problems, I evaluate the formula you gave me for each problem, how do you recommend I aggregate the data (if I need to)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177639):
To make it a bit easier, you can subtract the two times for each problem, resulting in a random variable that you want to compare to zero

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177647):
then you take an average weighted by how many trials were performed in each problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177736):
the standard deviation would be the sqrt-sum of the individual SDs, divided by 3 since there are three subproblems (assuming equal weights on the three problems)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177788):
Does it matter than one of the problem is much harder than the others? It has a run time around 16s while the others are around 7s and 3s

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177798):
Oh, I see, yes that changes things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177858):
I'm assuming in this analysis that we have two gaussian variables X and Y and want to estimate them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177859):
but this supposes that the mean and SD are fixed across the sample

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177861):
That sounds right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177865):
I don't understand your last sentence. What's the opposite of fixed?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177921):
We can assume that problem 1 has a gaussian distrib of times for each tactic, but there is no reason to believe that this same gaussian describes the times for problem 2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129177970):
I think that's reasonable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178035):
So we have to make some assumption about what we are estimating. Let's say we have good data on each problem, so we can say things like problem 1 is 2s +- .1s for tac 1 and 4s +- 1s for tac 2, and similarly for problem 2. If the goal is to minimize total run time over all future uses of tac1 vs tac2, then we need to assume that problem 1 and problem 2 are somehow representative of those future uses

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178038):
If we think problem 2 is more common than problem 1, then it will get a higher weight in the average

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178079):
The three problems are deriving transportable for monoids, groups and rings. Rings are very expensive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178085):
We could believe that the complexity is linear in the number of fields of the structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178090):
I think it is safe to say that each of those will be run only once, but perhaps you want to extrapolate to even larger examples, or smaller?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178132):
In other words you should estimate the common use case size

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178183):
Digression: should there be an absolute value in your formula? It's giving me negative numbers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178187):
I think as you say there will be an average size for the problems where this is used

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178349):
You mean the a-b/sqrt(sd) formula?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178421):
there should not be an absolute value, although I think I may have a sign error in there - one sign means tac1 is better, the other means tac2 is better

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178474):
Ah I see! The highest probability I get is 50%. I'll keep the optimization in but that doesn't seem conclusive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178477):
when you use erf it turns the number into a probability which is close to 100% for positive numbers and close to 0 for negative numbers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178484):
50% means you have a very small difference, of course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178486):
Really? I don't get that. Maybe I should be suspicious of my erf implementation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178523):
you can report the number without the erf, that gives the number of SDs away from the mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178532):
wait, did you just push some haskell to mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178535):
On my branch yes. I'll take it out before pushing for a merge

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178711):
I checked with another `erf` implementation, the results are consistent. I get the following numbers, one for each problem:

```
0.3548605107843447
0.392231363819503
0.5018422725422864
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178714):
Is the last one 50% or 0.50%?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178716):
I would assume 50%

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178755):
erf returns numbers in the range 0-1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 05:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178759):
Ok, I got confused when you said:

```quote
when you use erf it turns the number into a probability which is close to 100% for positive numbers and close to 0 for negative numbers
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178826):
Oh, I just checked wikipedia and it looks like the normalization conventions are a bit different for erf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178831):
there is a factor sqrt 2 on the inputs, and it returns a value in the range -1 to 1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178876):
Maybe you should just leave the erf off and interpret the number of SDs away from the mean directly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178888):
what I really want there is the CDF of the standard normal distribution

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178899):
which is basically erf but needs some preprocessing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129178978):
wikipedia says the CDF is
```math
CDF_{N(\mu,\sigma)}(x)=\frac{1}{2}\left[1+\mathrm{erf}\left(\frac{x-\mu}{\sigma\sqrt 2}\right)\right]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179041):
The `erf` library in haskell has a function `normcdf` with `normcdf x = erfc(-x  sqrt 2) ^ 2` does that make sense?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179053):
based on the name that's likely to be the right one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179062):
try evaluating it at -1, 0, 1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179137):
```
0.15865525393145705
0.5
0.8413447460685429
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179181):
that's correct

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179192):
use that in place of erf in the formula I gave before

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179238):
Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179256):
That looks much better!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179263):
```
0.6276517385920415
0.6416715838500027
0.6840264065071848
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179303):
And if I flip `a`and `b` in `a - b`, I get:

```
0.37234826140795846
0.3583284161499974
0.3159735934928151
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179313):
If we use `b - a`, that's the probability that `b ≥ a`, is correct?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179356):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179359):
Cool

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 05:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179362):
The interpretation is something like "given the data you gathered, there is a 62% chance that in fact tac 1 is better than tac 2 on problem 1"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179367):
Btw, `unfold_projs` yielded a big improvement in the end: Lean stopped crashing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179372):
ooh, what caused the crash?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179378):
Timeout

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179427):
I suspect that definitions generated by a tactic don't play nicely with `simp` / `dsimp` / `unfold` / `dunfold` if you try to unfold them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179477):
you can write your own simp lemmas for them if you want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 05:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179494):
Yes, I tried that. It did help a bit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179539):
But not as much as `unfold_projs`. It removed the need to hard code `has_mul.mul` et cie

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 06 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129179778):
I don't know about you but I'm having so much fun with that stuff (Lean) lately :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 06 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129185447):
```quote
I haven't done any statistics in a while. Can someone point me to a formula I can use to calculate the probability that `x ≤ y` if both are normally distributed random variables?
```
oh of course it's 50%, it's symmetric

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 06 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Applied%20statistics/near/129186725):
```quote
oh of course it's 50%, it's symmetric
```
I think the means are different


{% endraw %}
