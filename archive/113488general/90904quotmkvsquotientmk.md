---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90904quotmkvsquotientmk.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [quot.mk vs quotient.mk](https://leanprover-community.github.io/archive/113488general/90904quotmkvsquotientmk.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Dec 17 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.mk%20vs%20quotient.mk/near/152047620):
<p>Do we already have <code>lemma quot_mk_quotient_mk {α :Type*} [setoid α] (a : α) : quot.mk setoid.r a = ⟦a⟧ := rfl</code>? I need this because <code>rintro</code> typically produces the left-hand side.</p>


{% endraw %}
