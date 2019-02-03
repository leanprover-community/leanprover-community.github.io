---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22700Tailcallelimination.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Tail-call elimination?](https://leanprover-community.github.io/archive/113488general/22700Tailcallelimination.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Keeley Hoek (Aug 12 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tail-call%20elimination%3F/near/131992962):
<p>Because I have no idea how the VM actually works I tempt asking a meaningless question here, but here we go regardless: does the VM do tail-call elimination? Will my IO reading loops eventually explode if left to their own devices for long enough?</p>

#### [ Simon Hudon (Aug 12 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tail-call%20elimination%3F/near/132004521):
<p>I don't remember seeing that mentioned anywhere but that's a pretty basic optimization and Leo is pretty aggressive on optimization so I don't doubt he saw to it right away.</p>

#### [ Sebastian Ullrich (Aug 12 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tail-call%20elimination%3F/near/132004618):
<p>Lean 3's bytecode interpreter is quite basic. It does not do TCO.</p>

#### [ Sebastian Ullrich (Aug 12 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tail-call%20elimination%3F/near/132004665):
<p>However, <code>io.iterate</code> needs only constant stack space: <a href="https://github.com/leanprover/lean/blob/28f4143be31b7aa3c63a907be5443ca100025ef1/src/library/vm/vm_io.cpp#L412" target="_blank" title="https://github.com/leanprover/lean/blob/28f4143be31b7aa3c63a907be5443ca100025ef1/src/library/vm/vm_io.cpp#L412">https://github.com/leanprover/lean/blob/28f4143be31b7aa3c63a907be5443ca100025ef1/src/library/vm/vm_io.cpp#L412</a></p>


{% endraw %}
