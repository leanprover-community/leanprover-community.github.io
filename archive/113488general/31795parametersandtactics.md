---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31795parametersandtactics.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [parameters and tactics](https://leanprover-community.github.io/archive/113488general/31795parametersandtactics.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Nov 30 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parameters%20and%20tactics/near/148863078):
<p>There's some issue with referring to top-level definitions which mention currently-active <code>parameters</code> from within a tactic block, where the parameters don't get passed automatically. I found a workaround, though--if you wrap the tactic block in <code>let foo := foo in ...</code> then the second <code>foo</code> correctly gets its automatic parameters, and inside the tactic block <code>foo</code> will refer to the one we just defined.</p>

#### [ Simon Hudon (Nov 30 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parameters%20and%20tactics/near/148876383):
<p>It is a known issue. I believe the developers intend on fixing that behavior in Lean 4.</p>


{% endraw %}
