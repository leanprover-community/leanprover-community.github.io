---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73720failedtoadddeclaration.html
---

## Stream: [general](index.html)
### Topic: [failed to add declaration](73720failedtoadddeclaration.html)

---


{% raw %}
#### [ Keeley Hoek (Sep 15 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20add%20declaration/near/134011400):
<p>Has anyone ever seen the error <code>failed to add declaration 'xxxx.my_defn' to environment, type has metavariables</code> while writing a tactic?</p>

#### [ Keeley Hoek (Sep 15 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20add%20declaration/near/134011412):
<p>How can I see what the metavariables are?</p>

#### [ Simon Hudon (Sep 15 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20add%20declaration/near/134023923):
<p><code>mathlib</code> has <code>list_meta_vars</code> in <code>tactic.basic</code>. It may be enough to just <code>instantiate_mvars</code> before adding your definition.</p>


{% endraw %}
