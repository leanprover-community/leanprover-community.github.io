---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/62584polynomials.html
---

## Stream: [maths](index.html)
### Topic: [polynomials](62584polynomials.html)

---


{% raw %}
#### [ Scott Morrison (Apr 04 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomials/near/124608289):
Where can I find the following facts: `Z[x] is a commutative ring`, and `evaluation at x = i is a ring homomorphism`?

#### [ Mario Carneiro (Apr 04 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomials/near/124608402):
I don't think we have specialized to univariate polynomials, but `mv_polynomial` and an evaluation operation on it are defined in `multivariate_polynomial`

#### [ Kevin Buzzard (Apr 04 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomials/near/124615375):
Scott -- Kenny has been working on adjoint functors of various forgetful functors, and I pointed out to him that the adjoint of the forgetful functor from commutative rings to sets would give both of the things you ask about for free. Are you back to an internet connection yet? He should talk to you about category theory!

#### [ Kenny Lau (Apr 04 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomials/near/124615433):
@**Kevin Buzzard**  https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/category.20theory.20libraries/near/124608241


{% endraw %}
