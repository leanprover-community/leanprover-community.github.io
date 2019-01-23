---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/84699Heisenbug.html
---

## Stream: [general](index.html)
### Topic: [Heisenbug](84699Heisenbug.html)

---

#### [Scott Morrison (Aug 26 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Heisenbug/near/132789693):
I just found a Heisenbug: a proof that doesn't typecheck correctly, but if you add `tactic.result >>= tactic.trace` at the end, it does!

#### [Simon Hudon (Aug 26 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Heisenbug/near/132790782):
those are fun

#### [Simon Hudon (Aug 26 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Heisenbug/near/132790836):
I suspect that pretty printing either does some type checking (forcing some unification) or resolves some meta variables. You can try and see what is the smallest some term of the proof that you can print and which will fix the proof

#### [Scott Morrison (Aug 26 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Heisenbug/near/132790899):
I'm in the midst of further changes that will affect how my metavariables get handled, so I think I'm going to defer diagnosing this bug, hoping that if I don't look at it it will disappear permanently. :-)

