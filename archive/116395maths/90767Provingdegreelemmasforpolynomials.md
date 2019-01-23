---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/90767Provingdegreelemmasforpolynomials.html
---

## Stream: [maths](index.html)
### Topic: [Proving degree lemmas for polynomials](90767Provingdegreelemmasforpolynomials.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 07 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proving%20degree%20lemmas%20for%20polynomials/near/131063700):
I wrote some stuff on polynomials recently, which has been merged, but I was never that happy with it, because I knew that proving basic lemmas about degree was going to be quite hard. For example
```lean
import data.polynomial

example {α : Type*} [integral_domain α] [decidable_eq α] :
  degree ((X : polynomial α) ^ 2 + 1) = 2 :=
have h₁ : degree ((X : polynomial α) ^ 2) = 2, 
  by rw [degree_pow_eq, degree_X]; refl,
have h₂ : degree (1 : polynomial α) < degree ((X : polynomial α) ^ 2),
  by rw [degree_one, h₁]; exact dec_trivial,
by rw [add_comm, degree_add_eq_of_degree_lt h₂, h₁]
```
What's the best way of dealing with problems like this, tactics or lemmas?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proving%20degree%20lemmas%20for%20polynomials/near/131064645):
That looks like the proof I would have written -- but are you suggesting that the proof should be `dec_trivial`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proving%20degree%20lemmas%20for%20polynomials/near/131064754):
because I guess there's an algorithm; however it reminds me a bit of the `ring` tactic. Do you think you could modify that simple baby `ring` tactic that Mario wrote to turn it into a tactic which computes degree?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 07 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proving%20degree%20lemmas%20for%20polynomials/near/131066276):
It would be `dec_trivial` if it was integers, the fact that the type is a variable is the problem.


{% endraw %}
