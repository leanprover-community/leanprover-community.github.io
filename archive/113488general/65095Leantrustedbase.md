---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/65095Leantrustedbase.html
---

## Stream: [general](index.html)
### Topic: [Lean trusted base](65095Leantrustedbase.html)

---


{% raw %}
#### [ Karl Palmskog (Jan 12 2019 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20trusted%20base/near/154966417):
Does anyone know if there is a breakdown of the Lean trusted base somewhere? As in, "to trust your Lean code/proofs, you have to accept ...", which is done for Coq in its wiki: https://github.com/coq/coq/wiki/Presentation#what-do-i-have-to-trust-when-i-see-a-proof-checked-by-coq

And is there anything similar to the Coq `Print Assumptions <name>.` command (https://coq.inria.fr/refman/proof-engine/vernacular-commands.html#coq:cmd.print-assumptions) in Lean?

#### [ Bryan Gin-ge Chen (Jan 12 2019 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20trusted%20base/near/154967503):
I'm sure others are more knowledgeable than me, but for the first question you might be interested in @**Mario Carneiro**'s paper on [the type theory of Lean](https://github.com/digama0/lean-type-theory/releases) and [the 2nd to last question of the FAQ](https://github.com/leanprover/lean/blob/master/doc/faq.md).

For the second question, does:
```lean
#print axioms <name>
```
give you what you want? There's also a [`#where` command in mathlib](https://github.com/leanprover/mathlib/blob/caa2076038e2d5a84fd05e9988fbe31d01a7f6ba/tactic/where.lean) which will give you some more detailed environment info as well.

#### [ Karl Palmskog (Jan 12 2019 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20trusted%20base/near/154972114):
hmm, assumptions seem to be different from axioms (section variables apparently don't count). But I guess print axioms can give some hint of what has been added.

#### [ Reid Barton (Jan 12 2019 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20trusted%20base/near/154973055):
Section variables are added to the types of any definitions in the section which use them, and so they would be supplied where that definition is used.


{% endraw %}
