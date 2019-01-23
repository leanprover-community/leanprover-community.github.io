---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45701rwbugletIthink.html
---

## Stream: [general](index.html)
### Topic: [rw buglet (I think)](45701rwbugletIthink.html)

---

#### [Kevin Buzzard (Apr 02 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528036):
before : 38 hypotheses including ` HyT2 : y ∈ T ` and ` HTUih : T = Ui h `

#### [Kevin Buzzard (Apr 02 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528039):
Then I do ` rw HTUih at HyT2`

#### [Kevin Buzzard (Apr 02 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528041):
and I end up with 39 hypotheses

#### [Kenny Lau (Apr 02 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528042):
quite hard to confirm it if you don't have MWE

#### [Kenny Lau (Apr 02 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528044):
oh that isn't a bug

#### [Kenny Lau (Apr 02 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528049):
because that hypothesis can't be replaced

#### [Kevin Buzzard (Apr 02 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528050):
including ` HyT2 : y ∈ T ` and ` HyT2 : y ∈ Ui h `

#### [Kenny Lau (Apr 02 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528051):
because it's being used by other things

#### [Kenny Lau (Apr 02 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528052):
so instead it creates another hypothesis

#### [Kevin Buzzard (Apr 02 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528055):
Oh I see...

#### [Kevin Buzzard (Apr 02 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528057):
...with the same name?

#### [Kenny Lau (Apr 02 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528096):
well what other name would it be

#### [Kenny Lau (Apr 02 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528097):
you can do `dedup` if you don't like it

#### [Kevin Buzzard (Apr 02 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528098):
`revert HyT2,intro HyT`

#### [Kevin Buzzard (Apr 02 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20buglet%20%28I%20think%29/near/124528114):
It could have called it `a` ;-)

