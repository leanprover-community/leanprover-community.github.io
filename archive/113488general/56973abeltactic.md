---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56973abeltactic.html
---

## Stream: [general](index.html)
### Topic: [abel tactic](56973abeltactic.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 10 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abel%20tactic/near/133643278):
Say hello to the `abel` tactic, which does the same thing as `ring` but for commutative additive monoids and commutative groups. It doesn't currently support `*` on rings, since it would require a bit more support for `nat.cast` and `int.cast` in `norm_num`, but otherwise it is full featured using `+`, `-`, and `add_monoid.smul`, `gsmul`.

I'm sure it won't be long before someone asks me to make a multiplicative version, I'll look into it. I plan to just use `additive` to get the multiplicative version.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 10 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abel%20tactic/near/133643396):
Great! How far is the module version then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 10 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abel%20tactic/near/133643560):
The module version is basically a combination of `abel` and `ring`. It might be possible to generalize the coefficient ring to uniformize the treatment of additive groups as Z-modules, but we will need semimodules first, or else we will lose support for additive monoids with such a generalization


{% endraw %}
