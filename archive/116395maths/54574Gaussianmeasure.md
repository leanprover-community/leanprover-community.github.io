---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/54574Gaussianmeasure.html
---

## Stream: [maths](index.html)
### Topic: [Gaussian measure](54574Gaussianmeasure.html)

---

#### [Kevin Buzzard (Oct 02 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gaussian%20measure/near/135049503):
Today the subject of formalising Gaussian measure in Lean came up at work. I asked Johannes about it privately and he seemed optimistic that it was within reach. But then he mentioned some work done at Dagstuhl on the Lebesgue integral which is...possibly not accessible at this point? @**Mario Carneiro** do you have access to this stuff and is it in any state to be made public? As Patrick has pointed out in the past, our analysis is weak in places, and this probably simply because us number theorists / geometers are working on our pet projects where a bunch of foundational stuff has been done already, whereas any potential analysts will soon discover that there are still gaps in the coverage of 1st year undergraduate analysis (did anyone do the product rule yet??).

#### [Kevin Buzzard (Oct 02 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gaussian%20measure/near/135049832):
I guess we'll also need $$\pi$$ :-) Did it make it into mathlib yet? I glanced through recent commits and PRs and couldn't spot it.

#### [Reid Barton (Oct 02 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gaussian%20measure/near/135050032):
You mean the product rule for the formal derivative of polynomials?

#### [Kevin Buzzard (Oct 02 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gaussian%20measure/near/135050222):
heh, no, for differentiable functions $$\mathbb{R}\to\mathbb{R}$$ :-)

#### [Johan Commelin (Oct 02 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gaussian%20measure/near/135050692):
We don't have derivatives yet, do we?

#### [Chris Hughes (Oct 02 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gaussian%20measure/near/135050771):
No. There is something called `polynomial.derivative` or something, just for polynomials without mentioning analysis.

#### [Mario Carneiro (Oct 02 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gaussian%20measure/near/135051272):
Here's the integration file, which I've pushed to community mathlib: https://github.com/leanprover-community/mathlib/commit/10e3f42dc73fa9148e0f1847f6201bc608aa2488

#### [Patrick Massot (Oct 02 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gaussian%20measure/near/135055356):
It looks like a good start. Let's hope algebra will soon leave you some time for working on this

