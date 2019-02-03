---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/14013LeadingTermofMultivariatePolynomial.html
---

## Stream: [new members](index.html)
### Topic: [Leading Term of Multivariate Polynomial](14013LeadingTermofMultivariatePolynomial.html)

---


{% raw %}
#### [ AHan (Nov 18 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leading%20Term%20of%20Multivariate%20Polynomial/near/147908130):
<p>I wanted to write a function which return the leading term of a multivariate polynomial<br>
But I have no idea how to do it with the multivariate polynomial in mathlib ....</p>

#### [ Mario Carneiro (Nov 18 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leading%20Term%20of%20Multivariate%20Polynomial/near/147908281):
<p>what is the leading term of a multivariate polynomial?</p>

#### [ Mario Carneiro (Nov 18 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leading%20Term%20of%20Multivariate%20Polynomial/near/147908320):
<p>like <code>y^2 + x*y + x^2 + y</code></p>

#### [ AHan (Nov 18 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leading%20Term%20of%20Multivariate%20Polynomial/near/147908327):
<p>For example: <br>
leading term of (XY + X + Y) is XY</p>

#### [ AHan (Nov 18 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leading%20Term%20of%20Multivariate%20Polynomial/near/147908423):
<p>leading term of <code>y^2 + x*y + x^2 + y</code> will depends on our choice</p>

#### [ AHan (Nov 18 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Leading%20Term%20of%20Multivariate%20Polynomial/near/147908473):
<p>So have to define a monomial ordering first<br>
i.e If <code>u ≤ v</code> and <code>w</code> is any other monomial, then <code>u w ≤ v w</code></p>


{% endraw %}
