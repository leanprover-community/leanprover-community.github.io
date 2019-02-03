---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/62584polynomials.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [polynomials](https://leanprover-community.github.io/archive/116395maths/62584polynomials.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Apr 04 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomials/near/124608289):
<p>Where can I find the following facts: <code>Z[x] is a commutative ring</code>, and <code>evaluation at x = i is a ring homomorphism</code>?</p>

#### [ Mario Carneiro (Apr 04 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomials/near/124608402):
<p>I don't think we have specialized to univariate polynomials, but <code>mv_polynomial</code> and an evaluation operation on it are defined in <code>multivariate_polynomial</code></p>

#### [ Kevin Buzzard (Apr 04 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomials/near/124615375):
<p>Scott -- Kenny has been working on adjoint functors of various forgetful functors, and I pointed out to him that the adjoint of the forgetful functor from commutative rings to sets would give both of the things you ask about for free. Are you back to an internet connection yet? He should talk to you about category theory!</p>

#### [ Kenny Lau (Apr 04 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomials/near/124615433):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  <a href="#narrow/stream/113488-general/subject/category.20theory.20libraries/near/124608241" title="#narrow/stream/113488-general/subject/category.20theory.20libraries/near/124608241">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/category.20theory.20libraries/near/124608241</a></p>


{% endraw %}
