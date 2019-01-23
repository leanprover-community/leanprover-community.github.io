---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16734typeclasstracedump.html
---

## Stream: [general](index.html)
### Topic: [type class trace dump](16734typeclasstracedump.html)

---

#### [Johan Commelin (Aug 07 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20trace%20dump/near/131025671):
Is this expected behaviour?
```lean
import linear_algebra.multivariate_polynomial

set_option trace.class_instances true

instance foobar : comm_ring (mv_polynomial ℕ ℚ) := by apply_instance
```
I won't copy-paste the trace here, it is pretty long.

