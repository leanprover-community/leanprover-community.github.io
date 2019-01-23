---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19492Definitionalreduction.html
---

## Stream: [general](index.html)
### Topic: [Definitional reduction](19492Definitionalreduction.html)

---

#### [Moses Schönfinkel (Jun 04 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitional%20reduction/near/127532389):
If I can `#eval f a b` to `tt`, should I make sure that `example : f a b = tt`is `rfl`? In my case, `b = g a` and `g` seems to be naughty enough for Lean being to unwilling to expand everything. (`f a a = tt` is indeed `rfl`)

#### [Simon Hudon (Jun 04 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitional%20reduction/near/127540799):
This may be a case where you suffer from the fact that definitional equality is not transitive.

#### [Moses Schönfinkel (Jun 05 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitional%20reduction/near/127618197):
Let's suppose `#reduce f x` evaluates to `tt`. Is there a general easy way to prove `example : f x = tt` if `rfl` doesn't get the job done (probably due to non-transitive defeq)?

#### [Mario Carneiro (Jun 05 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitional%20reduction/near/127618259):
If `#reduce` works, then `rfl` should also

#### [Moses Schönfinkel (Jun 05 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitional%20reduction/near/127618290):
Would there by any difference between `#eval` and `#reduce`?

#### [Mario Carneiro (Jun 05 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitional%20reduction/near/127618298):
yes, the same statement doesn't hold if you use `#eval`

#### [Mario Carneiro (Jun 05 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitional%20reduction/near/127618356):
there are some terms that `#eval` can evaluate which `#reduce` gets stuck on due to axioms like `propext`

#### [Moses Schönfinkel (Jun 05 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Definitional%20reduction/near/127618595):
I would love to at least try `#reduce` but deterministic timeout is making it somewhat impossible. I am pretty sure everything I use is fairly computable tho. Should I just write a tactic that unfolds everything explicitly until `refl` or should I try to find a way to make the whole thing `rfl`? (In the case where `#eval f x` yields `tt` but `f x = tt` is not `rfl`.)

