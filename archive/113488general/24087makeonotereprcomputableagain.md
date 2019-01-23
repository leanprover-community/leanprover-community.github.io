---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24087makeonotereprcomputableagain.html
---

## Stream: [general](index.html)
### Topic: [make onote.repr computable again](24087makeonotereprcomputableagain.html)

---

#### [Kenny Lau (Apr 20 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125412217):
```lean
/-- The ordinal denoted by a notation -/
@[simp] noncomputable def repr : onote → ordinal.{0}
| 0 := 0
| (oadd e n a) := ω ^ repr e * n + repr a
```
This is in `set_theory/ordinal_notation.lean`. This definition is currently noncomputable. Should I start working on it to make it computable? (I believe I know how to make it computable, my only worry is that my PR will be rejected)

#### [Kenny Lau (Apr 20 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125412264):
(cc @**Mario Carneiro**)

#### [Kenny Lau (Apr 20 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125413219):
(cc @**Johannes Hölzl** )

#### [Kenny Lau (Apr 20 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125419192):
maybe I'll do some analysis to show that I know how to make it computable

#### [Kenny Lau (Apr 20 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125419783):
`ω` depends on `nat.lt.is_well_order`, which depends on `has_lt.lt.is_strict_total_order'`, which depends on `lt_trichotomy`, which depends on `lt_or_eq_of_le`, which uses `classical.by_cases`, so we only need to change one of them

#### [Gabriel Ebner (Apr 20 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125420264):
`classical.by_cases` is in `Prop`, so it has zero effect on noncomputability.

#### [Kenny Lau (Apr 20 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125421754):
you're right. I need to redo my analysis.

#### [Kenny Lau (Apr 20 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125422169):
@**Gabriel Ebner** do you have any idea which part is noncomputable?

#### [Gabriel Ebner (Apr 20 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125424751):
`ord.has_pow` is noncomputable because it 1) has an if-then-else on `a=0`, and 2) uses `limit_rec_on`

#### [Gabriel Ebner (Apr 20 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125425296):
I wonder if there is a cheap trick where you "eta-expand" an arbitrary ordinal to make it computable.  All components of ordinals are props or types after all.

#### [Mario Carneiro (Apr 21 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125471318):
Ordinals are a noncomputable theory, so there isn't much point. Furthermore, as Gabriel observes, ordinals are "cheaply noncomputable" since they contain only erasable data, so the VM never computes with them anyway. I think a future version of lean may mark this function computable simply because it doesn't compute anything.

#### [Mario Carneiro (Apr 21 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125471438):
You may wonder why so many things are noncomputable, when the choice usage is only in things like `ord`; the reason is because there is a lot of use of "unique choice", which is okay in ZF but not in lean. For example, can you even decide `a = 0`? This is easy in ZF, where everything is decidable by unique choice, but to do in lean you would have to decide if an arbitrary type is empty, for example `plift p` where `p` is a nondecidable proposition.

#### [Mario Carneiro (Apr 21 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125471516):
My question to you: why do you care that `repr` is noncomputable? If the goal is to compute with ordinals, that's the whole reason I wrote the `ordinal_notation` file - it gives computational analogues of the ordinal functions. You will note that `onote.add` and such are all computable. `repr` is only there to make it possible to state correctness results, assuming full choice.

