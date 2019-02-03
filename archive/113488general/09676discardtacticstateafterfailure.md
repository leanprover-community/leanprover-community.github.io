---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09676discardtacticstateafterfailure.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [discard tactic_state after failure?](https://leanprover-community.github.io/archive/113488general/09676discardtacticstateafterfailure.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Oct 03 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/discard%20tactic_state%20after%20failure%3F/near/135090187):
<p>Is there an existing tactic that runs a tactic, then restores the original tactic_state if it fails?</p>

#### [ Patrick Massot (Oct 03 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/discard%20tactic_state%20after%20failure%3F/near/135090200):
<p>try?</p>

#### [ Scott Morrison (Oct 03 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/discard%20tactic_state%20after%20failure%3F/near/135090235):
<p>(I've run into a problem where failed tactics are having unwanted side effects, e.g. unifying metavariables.)</p>

#### [ Simon Hudon (Oct 03 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/discard%20tactic_state%20after%20failure%3F/near/135091267):
<p>So you write <code>try tac</code>, <code>tac</code> unifies variables and then fails and the unification persists?</p>

#### [ Mario Carneiro (Oct 03 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/discard%20tactic_state%20after%20failure%3F/near/135091455):
<p><code>try</code> definitely restores the original tactic state after failure, so it's possible you've stumbled upon one of lean's less functional sides</p>

#### [ Scott Morrison (Oct 03 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/discard%20tactic_state%20after%20failure%3F/near/135091563):
<p>Hmm, it seems I was wrong, as sticking such a tactic into the place I thought would fix things, hasn't fixed things. Maybe more later, sorry for the noise!</p>


{% endraw %}
