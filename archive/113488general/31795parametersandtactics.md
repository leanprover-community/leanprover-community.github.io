---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31795parametersandtactics.html
---

## Stream: [general](index.html)
### Topic: [parameters and tactics](31795parametersandtactics.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 30 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parameters%20and%20tactics/near/148863078):
There's some issue with referring to top-level definitions which mention currently-active `parameters` from within a tactic block, where the parameters don't get passed automatically. I found a workaround, though--if you wrap the tactic block in `let foo := foo in ...` then the second `foo` correctly gets its automatic parameters, and inside the tactic block `foo` will refer to the one we just defined.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Nov 30 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/parameters%20and%20tactics/near/148876383):
It is a known issue. I believe the developers intend on fixing that behavior in Lean 4.


{% endraw %}
