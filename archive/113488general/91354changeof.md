---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91354changeof.html
---

## Stream: [general](index.html)
### Topic: [change of ^](91354changeof.html)

---

#### [Kevin Buzzard (Apr 06 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/change%20of%20%5E/near/124717957):
Are there any general tips for how to fix up files which no longer compile because of changes to `^`? I have files which start ``local  infix ` ^ ` := monoid.pow``, and for x and y in a comm_semiring ` (x + y) ^ 0 = x ^ 0 * y ^ 0` used to be solved by simp and now does not seem to be.

#### [Kevin Buzzard (Apr 06 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/change%20of%20%5E/near/124717960):
I should say that I'm looking at @**Chris Hughes** 's code here so I might not have got this 100 percent right

#### [Kevin Buzzard (Apr 06 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/change%20of%20%5E/near/124718005):
but basically our stacks project is quite broken now I upgraded to the current nightly

#### [Chris Hughes (Apr 06 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/change%20of%20%5E/near/124719712):
`simp [pow_succ, pow_zero]`?

