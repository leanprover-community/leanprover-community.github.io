---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99459itetermgolf.html
---

## [general](index.html)
### [ite term golf](99459itetermgolf.html)

#### [Andrew Ashworth (May 27 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ite%20term%20golf/near/127155648):
Suppose I need to prove `ite (x = y) tt ff = tt → x = y` and `x = y → ite (x = y) tt ff = tt`. Is there a succint way to do this in term mode? (I know `simp` and `split_ifs` is amazing here, but I'd like to do inversion by hand if possible)

#### [Nicholas Scheel (May 27 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ite%20term%20golf/near/127156020):
this should take care of the second part: https://github.com/leanprover/lean/blob/master/library/init/logic.lean#L839

#### [Nicholas Scheel (May 27 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ite%20term%20golf/near/127156150):
for the first part I wonder if something like the following would work (untested):
```
λ h,
if p : (x = y) then p else
  bool.no_confusion (eq.trans (eq.symm h) (if_neg p))
```
basically you decide the proposition (equivalent to the by_cases tactic) and then return the true case, or prove the false case is absurd

#### [Nicholas Scheel (May 27 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ite%20term%20golf/near/127156160):
maybe this is easier than no_confusion: https://github.com/leanprover/lean/blob/master/library/init/logic.lean

#### [Nicholas Scheel (May 27 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ite%20term%20golf/near/127156203):
`absurd (eq.symm (eq.trans .....)) bool.ff_ne_tt`

#### [Nicholas Scheel (May 27 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ite%20term%20golf/near/127156220):
btw I think this is just `if p then tt else ff`: https://github.com/leanprover/lean/blob/master/library/init/logic.lean#L590

#### [Mario Carneiro (May 27 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ite%20term%20golf/near/127164043):
use `to_bool`, it has lots of lemmas for this

#### [Andrew Ashworth (May 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ite%20term%20golf/near/127165905):
thanks Nicholas / Mario for the pointers

