---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/84699Heisenbug.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Heisenbug](https://leanprover-community.github.io/archive/113488general/84699Heisenbug.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Aug 26 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Heisenbug/near/132789693):
<p>I just found a Heisenbug: a proof that doesn't typecheck correctly, but if you add <code>tactic.result &gt;&gt;= tactic.trace</code> at the end, it does!</p>

#### [ Simon Hudon (Aug 26 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Heisenbug/near/132790782):
<p>those are fun</p>

#### [ Simon Hudon (Aug 26 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Heisenbug/near/132790836):
<p>I suspect that pretty printing either does some type checking (forcing some unification) or resolves some meta variables. You can try and see what is the smallest some term of the proof that you can print and which will fix the proof</p>

#### [ Scott Morrison (Aug 26 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Heisenbug/near/132790899):
<p>I'm in the midst of further changes that will affect how my metavariables get handled, so I think I'm going to defer diagnosing this bug, hoping that if I don't look at it it will disappear permanently. :-)</p>


{% endraw %}
