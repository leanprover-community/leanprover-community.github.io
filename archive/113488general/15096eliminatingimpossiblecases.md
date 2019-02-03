---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/15096eliminatingimpossiblecases.html
---

## Stream: [general](index.html)
### Topic: [eliminating impossible cases](15096eliminatingimpossiblecases.html)

---


{% raw %}
#### [ Reid Barton (Dec 20 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eliminating%20impossible%20cases/near/152279702):
<p>If I have <code>hi : i &lt; 0</code> as a hypothesis (<code>i</code> is a <code>nat</code>), what tactic will let me solve the goal most efficiently?</p>

#### [ Reid Barton (Dec 20 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eliminating%20impossible%20cases/near/152279750):
<p>Is <code>exact absurd hi (nat.not_lt_zero _)</code> really the easiest way?</p>

#### [ Kenny Lau (Dec 20 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eliminating%20impossible%20cases/near/152279761):
<p><code>cases hi</code></p>


{% endraw %}
