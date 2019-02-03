---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55671convertrefl.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [convert, refl](https://leanprover-community.github.io/archive/113488general/55671convertrefl.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Nov 27 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert%2C%20refl/near/148646168):
<p>This is a new one for me--<code>convert</code> left a goal which I could close with <code>refl</code></p>

#### [ Patrick Massot (Nov 27 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert%2C%20refl/near/148646555):
<p>You can easily play with <code>convert</code> and, especially <code>congr'</code> code, they are easy to understand, as long as you don't try to understand what <code>congr_core</code> is doing, which I suspect you won't need to try</p>

#### [ Reid Barton (Nov 27 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert%2C%20refl/near/148646599):
<p>Maybe <code>refl</code> closed some later goal, fixing a metavariable, and that caused an earlier goal to also be closable by <code>refl</code></p>

#### [ Reid Barton (Nov 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert%2C%20refl/near/148646658):
<p>I do have a <code>_</code> in the argument to <code>convert</code></p>


{% endraw %}
