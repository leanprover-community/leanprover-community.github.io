---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19566modeqrefl.html
---

## [general](index.html)
### [modeq.refl](19566modeqrefl.html)

#### [Kevin Buzzard (Apr 30 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911585):
`@[refl] protected theorem refl (a : ℕ) : a ≡ a [MOD n] := @rfl _ _`

#### [Kevin Buzzard (Apr 30 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911591):
looks funny because `rfl` unfolds to exactly `@rfl _ _`

#### [Kevin Buzzard (Apr 30 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911637):
but it's one of those situations where you can't prove the result by the exact three letter combination `rfl`

#### [Kevin Buzzard (Apr 30 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911646):
because you get the error `not a rfl-lemma, even though marked as rfl`

#### [Kenny Lau (Apr 30 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911647):
do you know what the `@[refl]` `@[symm]` `@[trans]` are for (as a sidenote)?

#### [Kevin Buzzard (Apr 30 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911658):
but the funny thing is, it is tagged `[refl]` anyway

#### [Kevin Buzzard (Apr 30 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911673):
what is the difference between being `a rfl-lemma` and being tagged with `@[refl]`?

#### [Kevin Buzzard (Apr 30 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911678):
Kenny here are some ramblings

#### [Kenny Lau (Apr 30 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911683):
they are for the reflexivity symmetry transitivty tactics respectively

#### [Kenny Lau (Apr 30 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911686):
(refl = reflexivity)

#### [Kevin Buzzard (Apr 30 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911688):
If you are in calc mode then calc will use any lemma tagged `trans`

#### [Kenny Lau (Apr 30 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911732):
that also

#### [Kevin Buzzard (Apr 30 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911735):
to concatenate `a R b` and `b R c`

#### [Kevin Buzzard (Apr 30 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911738):
or even `b S c`

#### [Chris Hughes (Apr 30 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125911741):
le_refl is refl but not rfl

#### [Gabriel Ebner (May 01 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/modeq.refl/near/125934512):
`rfl`-lemmas show definitional equalities (i.e. `a = b` where `a` and `b` are def-eq).  The three letters `rfl` are essentially hardcoded into the parser for this purpose.  The reason is that typically lemmas are completely independent of their proofs, (well-founded recursion aside) it should not matter what proof you use for a lemma.  However whether an equality is proved by definitional equality has important consequences: for example, `dsimp` can only use definitional equalities.  Hence we have an easy syntactic criterion to determine whether a lemma is proven by definitional equality.

