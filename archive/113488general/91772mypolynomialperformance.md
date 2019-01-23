---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91772mypolynomialperformance.html
---

## Stream: [general](index.html)
### Topic: [my_polynomial performance](91772mypolynomialperformance.html)

---


{% raw %}
#### [ Reid Barton (Nov 17 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147887874):
I tried proving that the polynomial ring functor is left adjoint to the forgetful functor CommRing -> Set but I gave up because doing anything with `mv_polynomial` was so slow. @**Kenny Lau** you were having similar problems with `mv_polynomial` right?
I think something is wrong there, but I couldn't figure out what.

#### [ Kenny Lau (Nov 17 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147887984):
yes, something is wrong

#### [ Kenny Lau (Nov 17 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147887985):
@**Mario Carneiro** what do you think?

#### [ Mario Carneiro (Nov 18 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147895390):
I think something is wrong

#### [ Kenny Lau (Nov 18 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147895486):
...

#### [ Mario Carneiro (Nov 18 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147895501):
my impression is that lean is having to solve enormous typeclass problems, I'm not sure if that's the whole problem

#### [ Kenny Lau (Nov 18 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147895542):
would you know specifically what is the problem with mv_polynomial and polynomial?

#### [ Mario Carneiro (Nov 18 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147895552):
if you look at the pp.all versions of any of the theorem statements, what looks like five tokens fills several pages

#### [ Kenny Lau (Nov 18 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147895597):
I don't think `pp.all` tells us *all* about the situation

#### [ Kenny Lau (Nov 18 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147895603):
but sure it tells us a lot

#### [ Mario Carneiro (Nov 18 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial%20performance/near/147895604):
yeah it doesn't know when to shut up


{% endraw %}
