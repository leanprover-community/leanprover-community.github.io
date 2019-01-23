---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85093doingcastswithsimp.html
---

## Stream: [general](index.html)
### Topic: [doing casts with `simp`](85093doingcastswithsimp.html)

---

#### [Kevin Buzzard (Aug 23 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/doing%20casts%20with%20%60simp%60/near/132631368):
```lean
import set_theory.cardinal

example (m n : ℕ) : (↑m : cardinal) = ↑n → m = n := by simp -- works fine

example (m n : ℕ) (H : (↑m : cardinal) = ↑n) : m = n := by simp [H] -- fails

```

Is there a way of getting the second example to work which doesn't involve (a) reverting H or (b) looking up the name of the lemma which `simp` is using to do the cast [i guess it's going to be `cardinal.nat_cast_inj`, maybe I'm supposed to know that]. Neither (a) nor (b) look "idiomatic" to me (is that the right word?)

#### [Rob Lewis (Aug 23 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/doing%20casts%20with%20%60simp%60/near/132631720):
`simpa using H`?

#### [Kenny Lau (Aug 23 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/doing%20casts%20with%20%60simp%60/near/132631805):
why are you doing cardinals? @**Kevin Buzzard**

#### [Kevin Buzzard (Aug 23 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/doing%20casts%20with%20%60simp%60/near/132631817):
Richard Thomas asked a question about the number 3

#### [Kevin Buzzard (Aug 23 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/doing%20casts%20with%20%60simp%60/near/132631823):
but then complained when I assumed it was finite

