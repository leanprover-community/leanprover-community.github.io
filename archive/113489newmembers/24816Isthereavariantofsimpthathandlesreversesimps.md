---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/24816Isthereavariantofsimpthathandlesreversesimps.html
---

## [new members](index.html)
### [Is there a variant of `simp` that handles reverse simps?](24816Isthereavariantofsimpthathandlesreversesimps.html)

#### [Abhimanyu Pallavi Sudhir (Nov 18 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Is there a variant of `simp` that handles reverse simps?/near/147897139):
Is there a variant of `simp` so I can write things like `simp [←P, Q]` or `simp only [←P, Q]` where `P` and `Q` may or may not be `simp` lemmas?

#### [Kenny Lau (Nov 18 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Is there a variant of `simp` that handles reverse simps?/near/147897178):
nope. you need to do `P.symm`

#### [Mario Carneiro (Nov 18 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Is there a variant of `simp` that handles reverse simps?/near/147897184):
and you alsso need to remove `P` if it is a simp lemma or it will go into a loop

#### [Chris Hughes (Nov 18 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Is there a variant of `simp` that handles reverse simps?/near/147897700):
remove `P`, means do `simp [P.symm, -P]`

#### [Mario Carneiro (Nov 18 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Is there a variant of `simp` that handles reverse simps?/near/147898210):
maybe we should write `simp'`? I'm sure this isn't the last tweak we will want

