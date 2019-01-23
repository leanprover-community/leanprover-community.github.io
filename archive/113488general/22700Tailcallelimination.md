---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22700Tailcallelimination.html
---

## Stream: [general](index.html)
### Topic: [Tail-call elimination?](22700Tailcallelimination.html)

---

#### [Keeley Hoek (Aug 12 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tail-call%20elimination%3F/near/131992962):
Because I have no idea how the VM actually works I tempt asking a meaningless question here, but here we go regardless: does the VM do tail-call elimination? Will my IO reading loops eventually explode if left to their own devices for long enough?

#### [Simon Hudon (Aug 12 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tail-call%20elimination%3F/near/132004521):
I don't remember seeing that mentioned anywhere but that's a pretty basic optimization and Leo is pretty aggressive on optimization so I don't doubt he saw to it right away.

#### [Sebastian Ullrich (Aug 12 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tail-call%20elimination%3F/near/132004618):
Lean 3's bytecode interpreter is quite basic. It does not do TCO.

#### [Sebastian Ullrich (Aug 12 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tail-call%20elimination%3F/near/132004665):
However, `io.iterate` needs only constant stack space: https://github.com/leanprover/lean/blob/28f4143be31b7aa3c63a907be5443ca100025ef1/src/library/vm/vm_io.cpp#L412

