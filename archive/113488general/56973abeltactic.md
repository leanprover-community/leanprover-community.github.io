---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56973abeltactic.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [abel tactic](https://leanprover-community.github.io/archive/113488general/56973abeltactic.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (Sep 10 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abel%20tactic/near/133643278):
<p>Say hello to the <code>abel</code> tactic, which does the same thing as <code>ring</code> but for commutative additive monoids and commutative groups. It doesn't currently support <code>*</code> on rings, since it would require a bit more support for <code>nat.cast</code> and <code>int.cast</code> in <code>norm_num</code>, but otherwise it is full featured using <code>+</code>, <code>-</code>, and <code>add_monoid.smul</code>, <code>gsmul</code>.</p>
<p>I'm sure it won't be long before someone asks me to make a multiplicative version, I'll look into it. I plan to just use <code>additive</code> to get the multiplicative version.</p>

#### [ Patrick Massot (Sep 10 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abel%20tactic/near/133643396):
<p>Great! How far is the module version then?</p>

#### [ Mario Carneiro (Sep 10 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abel%20tactic/near/133643560):
<p>The module version is basically a combination of <code>abel</code> and <code>ring</code>. It might be possible to generalize the coefficient ring to uniformize the treatment of additive groups as Z-modules, but we will need semimodules first, or else we will lose support for additive monoids with such a generalization</p>


{% endraw %}
