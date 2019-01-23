---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40609Whatsthefastestwaytoprovethis.html
---

## Stream: [general](index.html)
### Topic: [What's the fastest way to prove this?](40609Whatsthefastestwaytoprovethis.html)

---

#### [Kenny Lau (May 27 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127145665):
```lean
example : ∀ m n : ℕ, m = m * n → m = 0 ∨ n = 1 := sorry
```

#### [Nicholas Scheel (May 27 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127146413):
I would do `by_cases m = 0` and `eq_of_mul_eq_mul_left`

#### [Nicholas Scheel (May 27 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127146414):
(after `mul_one`)

#### [Nicholas Scheel (May 27 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127146464):
or maybe even `by_cases n = 1` and `eq_zero_of_mul_eq_self_right`

#### [Nicholas Scheel (May 27 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127146473):
(both of those long theorems are from integral domains https://github.com/leanprover/lean/blob/master/library/init/algebra/ring.lean#L290 )

#### [Kenny Lau (May 27 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127146560):
but they don't apply to natural numbers

#### [Nicholas Scheel (May 27 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127146567):
oh whoops, you’re right ... rings and all

#### [Nicholas Scheel (May 27 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127146620):
https://github.com/leanprover/lean/blob/master/library/init/data/nat/lemmas.lean#L332

#### [Kenny Lau (May 27 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%27s%20the%20fastest%20way%20to%20prove%20this%3F/near/127146625):
thanks

