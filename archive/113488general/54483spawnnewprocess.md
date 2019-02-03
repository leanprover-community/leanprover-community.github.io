---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54483spawnnewprocess.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [spawn new process](https://leanprover-community.github.io/archive/113488general/54483spawnnewprocess.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Moses Schönfinkel (Mar 02 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spawn%20new%20process/near/123202790):
<p>Would it be at all possible for a lean tactic to spawn a new process? For example call <code>coqtop</code>? If so, any recommendation as to what file to take a look at? (I don't suppose it's documented.)</p>

#### [ Gabriel Ebner (Mar 02 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spawn%20new%20process/near/123203007):
<p>leanpkg spawns external processes for almost everything: <a href="https://github.com/leanprover/lean/blob/d6d44a19947e2575b3fceed6d61167d258c661fb/leanpkg/leanpkg/main.lean" target="_blank" title="https://github.com/leanprover/lean/blob/d6d44a19947e2575b3fceed6d61167d258c661fb/leanpkg/leanpkg/main.lean">https://github.com/leanprover/lean/blob/d6d44a19947e2575b3fceed6d61167d258c661fb/leanpkg/leanpkg/main.lean</a><br>
You can do the same in tactics by lifting the io monad to the tactic monad (don't remember the name of the function)</p>

#### [ Patrick Massot (Mar 02 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spawn%20new%20process/near/123203069):
<p>I guess there must be hints in that "Lean talks to mathematica" paper</p>

#### [ Moses Schönfinkel (Mar 02 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spawn%20new%20process/near/123203071):
<p>Thank you. I am giving you 10 out of 10 for today :P! :)</p>

#### [ Patrick Massot (Mar 02 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spawn%20new%20process/near/123203084):
<p><a href="https://arxiv.org/abs/1712.09288" target="_blank" title="https://arxiv.org/abs/1712.09288">https://arxiv.org/abs/1712.09288</a></p>

#### [ Moses Schönfinkel (Mar 02 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spawn%20new%20process/near/123203156):
<p>Next thing you know we'll be querying google for proofs! ;)</p>

#### [ Sebastian Ullrich (Mar 03 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spawn%20new%20process/near/123206400):
<blockquote>
<p>You can do the same in tactics by lifting the io monad to the tactic monad (don't remember the name of the function)</p>
</blockquote>
<p><code>tactic.unsafe_run_io</code> :) .  The unsafe part should vanish soon by basing <code>tactic</code> on <code>io</code>.</p>


{% endraw %}
