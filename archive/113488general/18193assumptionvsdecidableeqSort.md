---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/18193assumptionvsdecidableeqSort.html
---

## [general](index.html)
### [assumption vs decidable_eq Sort*](18193assumptionvsdecidableeqSort.html)

#### [Kenny Lau (Oct 01 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumption vs decidable_eq Sort*/near/134952908):
How does `assumption` work if we don't have `decidable_eq Sort*`?

#### [Johannes Hölzl (Oct 01 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumption vs decidable_eq Sort*/near/134952971):
`assumption` is `meta`. So it does not compare propositions on the logic level, but at the level of expressions.

