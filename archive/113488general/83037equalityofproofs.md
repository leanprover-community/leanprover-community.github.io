---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83037equalityofproofs.html
---

## [general](index.html)
### [equality of proofs](83037equalityofproofs.html)

#### [Reid Barton (Apr 28 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality of proofs/near/125803504):
Is this lemma true and what is it (or should it be) called?
```lean
lemma hpropext {p q : Prop} (a : p) (b : q) : a == b := sorry
```

#### [Reid Barton (Apr 28 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality of proofs/near/125803608):
`proof_irrel` is the non-heterogeneous version

#### [Reid Barton (Apr 28 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality of proofs/near/125803658):
OK, I managed to prove it

