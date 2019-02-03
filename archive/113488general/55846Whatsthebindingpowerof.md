---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55846Whatsthebindingpowerof.html
---

## Stream: [general](index.html)
### Topic: [What's the binding power of →?](55846Whatsthebindingpowerof.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 13 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20binding%20power%20of%20%E2%86%92%3F/near/123657373):
<p><code>#print notation →</code> doesn't tell me, presumably because it's not notation. I was trying to verify without looking at the source code that <code>P ∧ Q → R</code> was indeed parsed as <code>(P ∧ Q) → R</code>.</p>

#### [ Kevin Buzzard (Mar 13 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20binding%20power%20of%20%E2%86%92%3F/near/123663651):
<p>Aah, got it. From <a href="https://leanprover.github.io/reference/other_commands.html#notation-declarations" target="_blank" title="https://leanprover.github.io/reference/other_commands.html#notation-declarations">https://leanprover.github.io/reference/other_commands.html#notation-declarations</a> (even though I don't think it's notation) "The implication arrow binds with strength 25"</p>


{% endraw %}
