---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70030assertionviolation.html
---

## Stream: [general](index.html)
### Topic: [assertion violation](70030assertionviolation.html)

---

#### [Kevin Buzzard (Mar 26 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/124242811):
Kenny found an assertion violation back in Feb or so: `instance foo (α : Type) : group α := { mul_assoc := λ x y z, rfl }`. I just mention it here because it still seems to be there.

#### [Kevin Buzzard (Mar 26 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/124242814):
Should I file an issue?

#### [Patrick Massot (May 23 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/126993921):
An old friend is back:
```
m_ctx.match(e, *val2)
LEAN ASSERTION VIOLATION
File: /home/travis/build/leanprover/lean/src/frontends/lean/elaborator.cpp
Line: 3167
```

#### [Kevin Buzzard (May 23 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/126994421):
did you catch it?

#### [Kevin Buzzard (May 23 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/126994467):
It's always line 3167

#### [Kevin Buzzard (May 23 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/126994468):
they should fix that line

#### [Kevin Buzzard (May 23 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/126994470):
maybe remove the assertion

#### [Patrick Massot (May 23 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/126994558):
I don't think this qualifies as serious enough for a Lean 3.X fix

#### [Kevin Buzzard (May 23 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/126994564):
Can you reproduce it?

#### [Patrick Massot (May 23 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assertion%20violation/near/126994657):
Right now it happens every time I touch anything in my norms.lean

