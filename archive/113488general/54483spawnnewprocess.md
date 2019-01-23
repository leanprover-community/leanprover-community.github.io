---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54483spawnnewprocess.html
---

## Stream: [general](index.html)
### Topic: [spawn new process](54483spawnnewprocess.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 02 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spawn%20new%20process/near/123202790):
Would it be at all possible for a lean tactic to spawn a new process? For example call `coqtop`? If so, any recommendation as to what file to take a look at? (I don't suppose it's documented.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 02 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spawn%20new%20process/near/123203007):
leanpkg spawns external processes for almost everything: https://github.com/leanprover/lean/blob/d6d44a19947e2575b3fceed6d61167d258c661fb/leanpkg/leanpkg/main.lean
You can do the same in tactics by lifting the io monad to the tactic monad (don't remember the name of the function)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 02 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spawn%20new%20process/near/123203069):
I guess there must be hints in that "Lean talks to mathematica" paper

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 02 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spawn%20new%20process/near/123203071):
Thank you. I am giving you 10 out of 10 for today :P! :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 02 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spawn%20new%20process/near/123203084):
https://arxiv.org/abs/1712.09288

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Mar 02 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spawn%20new%20process/near/123203156):
Next thing you know we'll be querying google for proofs! ;)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 03 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/spawn%20new%20process/near/123206400):
> You can do the same in tactics by lifting the io monad to the tactic monad (don't remember the name of the function)

`tactic.unsafe_run_io` :) .  The unsafe part should vanish soon by basing `tactic` on `io`.

