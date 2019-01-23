---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/18193assumptionvsdecidableeqSort.html
---

## Stream: [general](index.html)
### Topic: [assumption vs decidable_eq Sort*](18193assumptionvsdecidableeqSort.html)

---


{% raw %}
#### [ Kenny Lau (Oct 01 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumption%20vs%20decidable_eq%20Sort%2A/near/134952908):
How does `assumption` work if we don't have `decidable_eq Sort*`?

#### [ Johannes Hölzl (Oct 01 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumption%20vs%20decidable_eq%20Sort%2A/near/134952971):
`assumption` is `meta`. So it does not compare propositions on the logic level, but at the level of expressions.


{% endraw %}
