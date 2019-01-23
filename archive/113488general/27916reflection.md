---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27916reflection.html
---

## Stream: [general](index.html)
### Topic: [reflection](27916reflection.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sarah Mameche (Sep 25 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflection/near/134585528):
Hi, 
I'm trying to map meta expressions to an inductive type in the object language (with pattern matching on expr as described in https://leanprover.github.io/papers/tactic.pdf). 
There's a constructor taking a natural number as argument (var : ℕ → term). How can the number be extracted from an expression with this constructor?
Also, how does this work if I go from the inductive type back to exprs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 25 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflection/near/134586345):
I'm not sure if I understand exactly what you're after. You want a function `expr → ℕ` that will return the index if the input is made with `expr.var`?
```lean
meta def var_index : expr → ℕ 
| (expr.var n) := n
| _ := 0
```
You can do the same in the other direction, if the nat appears in a constructor of your inductive type. Match on your type, get the nat argument, and feed it back into `expr.var`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 25 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflection/near/134586346):
Or did you mean something else?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sarah Mameche (Sep 25 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflection/near/134592201):
No, that helped, thanks!


{% endraw %}
