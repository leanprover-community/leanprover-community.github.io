---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55846Whatsthebindingpowerof.html
---

## [general](index.html)
### [What's the binding power of →?](55846Whatsthebindingpowerof.html)

#### [Kevin Buzzard (Mar 13 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's the binding power of →?/near/123657373):
`#print notation →` doesn't tell me, presumably because it's not notation. I was trying to verify without looking at the source code that `P ∧ Q → R` was indeed parsed as `(P ∧ Q) → R`.

#### [Kevin Buzzard (Mar 13 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What's the binding power of →?/near/123663651):
Aah, got it. From https://leanprover.github.io/reference/other_commands.html#notation-declarations (even though I don't think it's notation) "The implication arrow binds with strength 25"

