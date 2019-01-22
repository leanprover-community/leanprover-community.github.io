---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86798wellfoundedfix.html
---

## [general](index.html)
### [well_founded.fix](86798wellfoundedfix.html)

#### [Kenny Lau (Jul 28 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded.fix/near/130481709):
```lean
attribute [elab_as_eliminator] well_founded.fix
```

#### [Kenny Lau (Jul 28 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded.fix/near/130481714):
can we put this somewhere in mathlib?

#### [Kevin Buzzard (Jul 28 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded.fix/near/130482868):
What does it do?

#### [Kenny Lau (Jul 28 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded.fix/near/130482873):
well-founded recursion

#### [Kenny Lau (Jul 28 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded.fix/near/130482875):
oh, it makes sure that the motive is computed

#### [Kenny Lau (Jul 28 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/well_founded.fix/near/130482917):
you need `elab_as_eliminator` in things like `rec_on`

