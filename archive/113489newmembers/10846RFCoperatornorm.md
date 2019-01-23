---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/10846RFCoperatornorm.html
---

## Stream: [new members](index.html)
### Topic: [RFC: operator norm](10846RFCoperatornorm.html)

---


{% raw %}
#### [ Jan-David Salchow (Dec 28 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/RFC%3A%20operator%20norm/near/152676704):
I've been playing with the space of bounded linear maps between normed space, see https://github.com/jdsalchow/mathlib/blob/calculus/analysis/functional/operator_norm.lean

Before splitting this up into smaller pieces and creating a PR, I thought I better ask for comments. So, comments anybody?

#### [ Kevin Buzzard (Dec 29 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/RFC%3A%20operator%20norm/near/152679652):
`local attribute[instance] classical.prop_decidable` -- people often go for `local attribute [instance, priority 0] classical.prop_decidable` nowadays because it is less likely to break proofs that actually rely on decidability. This might well not be an issue in this code though.

#### [ Jan-David Salchow (Dec 29 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/RFC%3A%20operator%20norm/near/152699240):
Is there a way to forget a local attribute when it's not needed anymore?

#### [ Chris Hughes (Dec 29 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/RFC%3A%20operator%20norm/near/152699337):
put it inside a section


{% endraw %}
