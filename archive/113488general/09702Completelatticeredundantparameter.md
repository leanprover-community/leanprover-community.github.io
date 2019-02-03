---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09702Completelatticeredundantparameter.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Complete lattice redundant parameter](https://leanprover-community.github.io/archive/113488general/09702Completelatticeredundantparameter.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Mar 31 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Complete%20lattice%20redundant%20parameter/near/124445675):
<p>Isn't bot and top provable from supremum and infimum, respectively?</p>

#### [ Mario Carneiro (Mar 31 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Complete%20lattice%20redundant%20parameter/near/124446222):
<p>Yes, and <code>Sup</code> is definable from <code>Inf</code>, and <code>sup</code> is definable from <code>Sup</code>. The reason these additional definitions are in the structure is that sometimes you want a different definitional reduction for the expression than the lattice definition gives you, i.e. <code>Prop</code> is a complete lattice with top <code>true</code>, but if it was defined with <code>Sup</code> then that would be some cumbersome forall false thing</p>


{% endraw %}
