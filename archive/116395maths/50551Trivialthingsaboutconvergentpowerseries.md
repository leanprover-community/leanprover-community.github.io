---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/50551Trivialthingsaboutconvergentpowerseries.html
---

## Stream: [maths](index.html)
### Topic: [Trivial things about convergent power series](50551Trivialthingsaboutconvergentpowerseries.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 07 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Trivial%20things%20about%20convergent%20power%20series/near/131066562):
I would very much like to see some progress towards a definition of pi in mathlib. Here is my proposal: (1) define cos as an infinite power series (2) prove it's continuous (3) check cos(1)>0 and cos(2)<0 (4) define pi to be twice the smallest positive real zero of cos. I don't see any problem doing any of this in mathlib. However even though @**Chris Hughes** has defined exp as a function on the complexes and proved exp(x+y)=exp(x)exp(y) [which involved some hard work manipulating power series] this is still not in mathlib for some reason. All the basic facts about sin and cos should follow from this one fact. I know that all the CS guys have a pathological fear of [the theorem we don't talk about](https://en.wikipedia.org/wiki/Cauchy%27s_integral_theorem) but this stuff is way easier than that, it is basic real analysis, and given that mathlib has measure spaces, topological rings, Pell's equation etc etc it is surely about time that mathlib proved basic stuff about infinite sums of real numbers. If you want it done with filters, we can do it with filters. If some people put together a basic PR defining power series in one real or complex variable (or even over a general complete topological field if you like -- this is fine by me given that I spend half my life thinking about power series over the p-adic numbers), radius of convergence, proof that a function was continuous within its radius of convergence, and then definition of exp, sin and cos -- say that PR existed -- would it get accepted? @**Edward Ayers** I think the answer to your question is that we haven't got much at all when it comes to basic real analysis.

#### [ Patrick Massot (Aug 07 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Trivial%20things%20about%20convergent%20power%20series/near/131066919):
GT III.5

#### [ Patrick Massot (Aug 07 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Trivial%20things%20about%20convergent%20power%20series/near/131066929):
That's how I talk nowadays.

#### [ Kevin Buzzard (Aug 07 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Trivial%20things%20about%20convergent%20power%20series/near/131067011):
In 20 years' time we will have killed Bourbaki and other people will talk about `data/real/basic.lean#12345` in the same way. I mean -- why not?


{% endraw %}
