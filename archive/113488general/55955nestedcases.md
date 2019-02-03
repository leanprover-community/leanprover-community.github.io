---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55955nestedcases.html
---

## Stream: [general](index.html)
### Topic: [nested cases](55955nestedcases.html)

---


{% raw %}
#### [ Reid Barton (Feb 26 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nested%20cases/near/123003168):
<p>Is there a more convenient way to unpack the components of a conclusion of the form <code>∃ x y, p x ∧ q y ∧ r x y</code> in a tactics block than using multiple <code>cases</code> tactics?</p>

#### [ Andrew Ashworth (Feb 26 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nested%20cases/near/123003198):
<p>you want mathlib's <code>rcases</code> or core's <code>cases_matching</code></p>

#### [ Reid Barton (Feb 26 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nested%20cases/near/123003381):
<p>oh yeah, <code>rcases</code> is what I want. Much better!</p>

#### [ Sean Leather (Feb 27 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nested%20cases/near/123041049):
<p><span class="user-mention" data-user-email="rwbarton@gmail.com" data-user-id="110032">@Reid Barton</span> Also, in case you didn't know, the anonymous constructor notation <code>⟨..., ...⟩</code> is right-associative for nested constructors. So, for example, you can do <code>rcases h with ⟨x, y, px, qy, rxy⟩</code> with your type. I learned this recently, and it's quite convenient.</p>


{% endraw %}
