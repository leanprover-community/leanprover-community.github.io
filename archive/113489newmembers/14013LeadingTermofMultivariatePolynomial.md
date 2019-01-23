---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/14013LeadingTermofMultivariatePolynomial.html
---

## Stream: [new members](index.html)
### Topic: [Leading Term of Multivariate Polynomial](14013LeadingTermofMultivariatePolynomial.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Nov 18 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leading%20Term%20of%20Multivariate%20Polynomial/near/147908130):
I wanted to write a function which return the leading term of a multivariate polynomial
But I have no idea how to do it with the multivariate polynomial in mathlib ....

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 18 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leading%20Term%20of%20Multivariate%20Polynomial/near/147908281):
what is the leading term of a multivariate polynomial?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 18 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leading%20Term%20of%20Multivariate%20Polynomial/near/147908320):
like `y^2 + x*y + x^2 + y`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Nov 18 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leading%20Term%20of%20Multivariate%20Polynomial/near/147908327):
For example: 
leading term of (XY + X + Y) is XY

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Nov 18 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leading%20Term%20of%20Multivariate%20Polynomial/near/147908423):
leading term of `y^2 + x*y + x^2 + y` will depends on our choice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Nov 18 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leading%20Term%20of%20Multivariate%20Polynomial/near/147908473):
So have to define a monomial ordering first
i.e If `u ≤ v` and `w` is any other monomial, then `u w ≤ v w`

