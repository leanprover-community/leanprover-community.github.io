---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08893listoftactics.html
---

## [general](index.html)
### [list of tactics](08893listoftactics.html)

#### [Jakob von Raumer (Mar 20 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20of%20tactics/near/123967762):
Is there a tactic that allows me to give a list of tactics where each one solves one goal?

#### [Simon Hudon (Mar 20 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20of%20tactics/near/123967842):
Yes try this: https://github.com/leanprover/lean/blob/master/library/init/meta/tactic.lean#L845-L847

#### [Mario Carneiro (Mar 20 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20of%20tactics/near/123967976):
The interactive way to write this is `tac; [tac1, tac2, tac3]`

#### [Simon Hudon (Mar 20 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20of%20tactics/near/123968190):
I should really stop assuming people are scripting when answering :stuck_out_tongue_closed_eyes:

