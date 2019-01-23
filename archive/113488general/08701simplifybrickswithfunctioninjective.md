---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08701simplifybrickswithfunctioninjective.html
---

## Stream: [general](index.html)
### Topic: [simplify bricks with function.injective](08701simplifybrickswithfunctioninjective.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 10 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simplify%20bricks%20with%20function.injective/near/133641530):
```lean
example (α β) (f : α → β) (H : function.injective f) : false :=
by simp [function.injective] at H
```
trace:
```
--------------
[simplify] iff: function.injective f
[simplify] eq: function.injective f
[simplify] eq: f
[simplify] eq: function.injective
109. [simplify.rewrite] [function.injective.equations._eqn_1]: function.injective f ==> ∀ ⦃a₁ a₂ : α⦄, f a₁ = f a₂ → a₁ = a₂
[simplify] eq: f a₁ = f a₂ → a₁ = a₂
[simplify] eq: f a₁ = f a₂
[simplify] eq: f a₁
[simplify] eq: a₁
[simplify] eq: f
[simplify] eq: f a₂
[simplify] eq: a₂
[simplify] eq: f
[simplify] eq: eq
111. [simplify.rewrite_failure] fail to match 'ite_eq_ff_distrib':
f a₁ = f a₂
=?=
ite ?x_0 ?x_2 ?x_3 = ff
--------------
```
ad nauseam


{% endraw %}
