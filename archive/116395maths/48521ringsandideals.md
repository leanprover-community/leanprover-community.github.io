---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/48521ringsandideals.html
---

## Stream: [maths](index.html)
### Topic: [rings and ideals](48521ringsandideals.html)

---

#### [Patrick Massot (Jul 21 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130050846):
@**Kenny Lau** and @**Chris Hughes** with the recent merge of [PR196](https://github.com/leanprover/mathlib/pull/196) how does current mathlib compare to [Lean 2 lib](https://github.com/leanprover/lean2/blob/master/library/theories/commutative_algebra/ideal.lean)?

#### [Chris Hughes (Jul 21 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130064086):
Is that a hint that I should work on ideals? I was delayed by type class problems, but now I've found a long term solution, so I can work on it properly.

#### [Mario Carneiro (Jul 21 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130064153):
was the lean 2 ideals library significant?

#### [Chris Hughes (Jul 21 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130064270):
Looking at it, although it's much longer than the ideals file in mathlib, a lot of it covers stuff that's already done for modules.

#### [Mario Carneiro (Jul 21 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130064286):
aren't those easy then? I thought mathlib ideals were defined in terms of submodules, so it should just be a theorem application away

#### [Chris Hughes (Jul 21 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130064288):
Exactly.

#### [Chris Hughes (Jul 21 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130064291):
Is it even worth proving them specifically for ideals?

#### [Mario Carneiro (Jul 21 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130064337):
It can be helpful to change the statement the way you need it, if it is going to be used in `rw` for example

#### [Mario Carneiro (Jul 21 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/rings%20and%20ideals/near/130064346):
I have said before that the most important thing about many of the early files is the statements, not the proofs

