---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43640examplexyxxyyxysorry.html
---

## Stream: [general](index.html)
### Topic: [`example {x y : ℕ} : x + x = y + y → x = y := sorry`](43640examplexyxxyyxysorry.html)

---

#### [Kevin Buzzard (Apr 05 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60example%20%7Bx%20y%20%3A%20%E2%84%95%7D%20%3A%20x%20%2B%20x%20%3D%20y%20%2B%20y%20%E2%86%92%20x%20%3D%20y%20%3A%3D%20sorry%60/near/124685151):
How about this one? `example {x y : ℕ} : x + x = y + y → x = y := sorry`.  I ended up proving another lemma `x + x = x * 2` and then rewrote twice and used `nat.mul_div_cancel`.  I thought `x + x = x * 2`
was a lemma but I can't find it. There is a lemma ` add_self_div_two : ∀ {α : Type u_1} [_inst_1 : linear_ordered_field α] (a : α), (a + a) / 2 = a` (note: linearly ordered field ensures 2 isn't zero). Is there an argument for adding `nat.add_self_div_two` and `int.add_self_div_two`?

#### [Kevin Buzzard (Apr 05 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60example%20%7Bx%20y%20%3A%20%E2%84%95%7D%20%3A%20x%20%2B%20x%20%3D%20y%20%2B%20y%20%E2%86%92%20x%20%3D%20y%20%3A%3D%20sorry%60/near/124685240):
I'd be interested in seeing any slicker arguments for my original question; `rw nat.add_self_div_two` would do it in one line.

#### [Kevin Buzzard (Apr 05 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60example%20%7Bx%20y%20%3A%20%E2%84%95%7D%20%3A%20x%20%2B%20x%20%3D%20y%20%2B%20y%20%E2%86%92%20x%20%3D%20y%20%3A%3D%20sorry%60/near/124685269):
But there is an underlying issue that I have, which is that both this question and the not (2+x=0) question are things which mathematicians are going to claim are obvious. Is there some general tactic in Coq, say, which would do both of these immediately?

#### [Mario Carneiro (Apr 05 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60example%20%7Bx%20y%20%3A%20%E2%84%95%7D%20%3A%20x%20%2B%20x%20%3D%20y%20%2B%20y%20%E2%86%92%20x%20%3D%20y%20%3A%3D%20sorry%60/near/124685322):
`mul_two` and `two_mul` should exist

#### [Mario Carneiro (Apr 05 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60example%20%7Bx%20y%20%3A%20%E2%84%95%7D%20%3A%20x%20%2B%20x%20%3D%20y%20%2B%20y%20%E2%86%92%20x%20%3D%20y%20%3A%3D%20sorry%60/near/124685323):
mmh, I don't like it when you start complaining that things are obvious or trivial

#### [Mario Carneiro (Apr 05 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60example%20%7Bx%20y%20%3A%20%E2%84%95%7D%20%3A%20x%20%2B%20x%20%3D%20y%20%2B%20y%20%E2%86%92%20x%20%3D%20y%20%3A%3D%20sorry%60/near/124685335):
This stuff falls under the purview of `omega`, but that might be overkill

#### [Kevin Buzzard (Apr 05 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60example%20%7Bx%20y%20%3A%20%E2%84%95%7D%20%3A%20x%20%2B%20x%20%3D%20y%20%2B%20y%20%E2%86%92%20x%20%3D%20y%20%3A%3D%20sorry%60/near/124685379):
I am arguing that if I am trying to sell Lean to mathematicians and they say "OK so how do we prove x + x = y + y -> x = y" and I say "oh that's a fascinating question", that's not a good answer.

#### [Mario Carneiro (Apr 05 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60example%20%7Bx%20y%20%3A%20%E2%84%95%7D%20%3A%20x%20%2B%20x%20%3D%20y%20%2B%20y%20%E2%86%92%20x%20%3D%20y%20%3A%3D%20sorry%60/near/124685416):
I would be aiming for having more theorems that say things like this rather than some big bloated tactic to kill them all

#### [Kevin Buzzard (Apr 05 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60example%20%7Bx%20y%20%3A%20%E2%84%95%7D%20%3A%20x%20%2B%20x%20%3D%20y%20%2B%20y%20%E2%86%92%20x%20%3D%20y%20%3A%3D%20sorry%60/near/124685434):
`two_mul` is there by default, `mul_two` needs `import algebra.ring` but it is proved for semirings.

#### [Mario Carneiro (Apr 05 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60example%20%7Bx%20y%20%3A%20%E2%84%95%7D%20%3A%20x%20%2B%20x%20%3D%20y%20%2B%20y%20%E2%86%92%20x%20%3D%20y%20%3A%3D%20sorry%60/near/124685487):
`algebra.ring` is the mathlib file for ring-like structures (things with addition and multiplication)

#### [Kevin Buzzard (Apr 05 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60example%20%7Bx%20y%20%3A%20%E2%84%95%7D%20%3A%20x%20%2B%20x%20%3D%20y%20%2B%20y%20%E2%86%92%20x%20%3D%20y%20%3A%3D%20sorry%60/near/124685493):
theorems v tactics -- in the past this has been my instinct too; the theorems are mostly named well and are mostly there.

#### [Kevin Buzzard (Apr 05 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60example%20%7Bx%20y%20%3A%20%E2%84%95%7D%20%3A%20x%20%2B%20x%20%3D%20y%20%2B%20y%20%E2%86%92%20x%20%3D%20y%20%3A%3D%20sorry%60/near/124685505):
But I couldn't find mul_two because I was looking for add_self

#### [Kevin Buzzard (Apr 05 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60example%20%7Bx%20y%20%3A%20%E2%84%95%7D%20%3A%20x%20%2B%20x%20%3D%20y%20%2B%20y%20%E2%86%92%20x%20%3D%20y%20%3A%3D%20sorry%60/near/124685519):
You don't want to call this result mul_two_eq_add_self?

#### [Kevin Buzzard (Apr 05 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60example%20%7Bx%20y%20%3A%20%E2%84%95%7D%20%3A%20x%20%2B%20x%20%3D%20y%20%2B%20y%20%E2%86%92%20x%20%3D%20y%20%3A%3D%20sorry%60/near/124685572):
so because I failed I started wishing there was one big bloated tactic which kills them all.

