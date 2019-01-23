---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/76731holecommands.html
---

## Stream: [general](index.html)
### Topic: [hole commands](76731holecommands.html)

---

#### [Johan Commelin (Aug 30 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hole%20commands/near/133076337):
One thing that might be of general interest that got some attention in Orsay: Lean has support for holes, but it isn't up to par to some other theorem provers. Nevertheless, try typing
```lean
import tactic.tidy

example : your_favourite_triviality := {! _ !}
```
and hit Ctrl-. (control-dot) while you are on the hole (`{! _ !}`). You will get a list of hole commands that are available. Three of them are somewhat silly, and one was added in Orsay: the tidy hole command. If your favourite triviality is actually Lean-trivial, then this hole-command will write a complete tactic proof for you.

#### [Johan Commelin (Aug 30 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hole%20commands/near/133076506):
It might be a good idea to think about other useful hole commands.

#### [Kenny Lau (Aug 30 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hole%20commands/near/133076735):
could you show us an example?

#### [Kenny Lau (Aug 30 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hole%20commands/near/133076760):
oh nvm I didn't import `tactic.tidy`

