---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52145submodulespan.html
---

## [general](index.html)
### [submodule.span](52145submodulespan.html)

#### [petercommand (Nov 18 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147901978):
I am trying to understand submodule.span, why can the type of ```Inf { p | s \sub p } ``` (set beta) be converted to ```submodule \alpha \beta```? Thanks!

#### [petercommand (Nov 18 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902039):
is there an option to show this information?

#### [Mario Carneiro (Nov 18 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902082):
There is a coercion on `p` there

#### [Mario Carneiro (Nov 18 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902089):
it is the infimum (in the lattice of submodules) of all submodules that when converted to a set are supersets of `s`

#### [Mario Carneiro (Nov 18 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902129):
Lean knows the inf is taken in submodules, and `p` is a submodule, because type inference is done from the outside in and the target type is a `submodule`

#### [petercommand (Nov 18 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902130):
hmm, how can I know that there is a coercion on ```p```?

#### [Mario Carneiro (Nov 18 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902131):
If you print it there will be an up arrow

#### [petercommand (Nov 18 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902137):
ah

#### [petercommand (Nov 18 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902227):
can I know which coercion is applied?

#### [petercommand (Nov 18 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902234):
like where the coercion is defined

#### [petercommand (Nov 18 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/submodule.span/near/147902280):
Ah, there is only one ```submodule.has_coe``` in submodule.lean

