---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98059constructingexprlam.html
---

## Stream: [general](index.html)
### Topic: [constructing expr.lam](98059constructingexprlam.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20expr.lam/near/133600290):
How do I construct `expr.lam` terms? In particular, I have  an expression `e_1` that already has a `var n` inside it, and another `e_2`, and I want to construct the `expr` representing `lam x, e_1 = e_2`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20expr.lam/near/133600338):
I tried to use ```to_expr ``(%%e_1 = %%e_2)```, but that chokes because `e_1` has a `var` inside it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 09 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20expr.lam/near/133600394):
It's kind of ugly but I recommend 

```lean
feq <- mk_const `eq,
v <- mk_mvar,
let e := lam n bi t (feq v e_1 e_2)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 09 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20expr.lam/near/133600442):
the downside is that you're postponing type checking. If you don't want to postpone type checking, you have to take the long way around, instantiate your `var` with `local_const`, type check, then use `lambdas`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20expr.lam/near/133600976):
Ah, I see. Turning my `var` into a `local_const` is maybe not so bad, in any case. How does one construct the `expr.lam` then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 09 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20expr.lam/near/133601026):
```lean
v <- mk_local_def n t,
e <- mk_app `eq [e_1.instantiate_var v, e_2],
lambdas [v] e,
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20expr.lam/near/133601300):
Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 09 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructing%20expr.lam/near/133601301):
:+1:


{% endraw %}
