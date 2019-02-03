---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/18193assumptionvsdecidableeqSort.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [assumption vs decidable_eq Sort*](https://leanprover-community.github.io/archive/113488general/18193assumptionvsdecidableeqSort.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Oct 01 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumption%20vs%20decidable_eq%20Sort%2A/near/134952908):
<p>How does <code>assumption</code> work if we don't have <code>decidable_eq Sort*</code>?</p>

#### [ Johannes Hölzl (Oct 01 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumption%20vs%20decidable_eq%20Sort%2A/near/134952971):
<p><code>assumption</code> is <code>meta</code>. So it does not compare propositions on the logic level, but at the level of expressions.</p>


{% endraw %}
