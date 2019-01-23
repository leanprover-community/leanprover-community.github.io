---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89367naturalsinreals.html
---

## Stream: [general](index.html)
### Topic: [naturals_in_reals](89367naturalsinreals.html)

---

#### [Guillermo Barajas Ayuso (Sep 11 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133730371):
Hi guys, how would you express the natural numbers as a subtype of the reals?

#### [Kevin Buzzard (Sep 11 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133731041):
I guess you could just do

```lean
import data.real.basic

def N := {x : ℝ // ∃ n : ℕ, x = n}
```

but then the term of type `equiv N nat` would be noncomputable. Is there a computable way?

#### [Kenny Lau (Sep 11 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133731224):
it's computable

#### [Kenny Lau (Sep 11 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133731235):
(but Lean doesn't know it yet)

#### [Chris Hughes (Sep 11 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133734407):
How do you do that computably?

#### [Mario Carneiro (Sep 11 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133752152):
It's not computable. It would be if cauchy sequences defining real numbers had a modulus of convergence

#### [Mario Carneiro (Sep 11 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133752221):
this is why I've taken to calling our definition of the reals "computable but not really"

#### [Mario Carneiro (Sep 11 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133752463):
Suppose you have a real number that is known to equal some natural number, and you want to guess which. The convergence criterion says that at some point all the rational numbers will be closer to one natural than any other, and then you can round to get the number, but you don't know when that point is. A more constructive approach would be a sequence of rationals that converges at a specific rate (usually exponential), so you can ask "give me an n-digit approximation of this number", or at least a sequence of rationals together with a function that tells you how long the sequence takes to reach a certain level of approximation

#### [Kenny Lau (Sep 11 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133752494):
fair enough. I thought wrongly.

#### [Johan Commelin (Sep 11 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133752892):
Is our definition of `rat` "computable but not rationally"?

#### [Mario Carneiro (Sep 11 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133753216):
To answer the original question, the standard way to talk about natural numbers inside the reals is to use the coercion. If you want to talk about the whole set of reals-that-are-natural, you can use `set.range (coe : ℕ → ℝ)` which is basically the same as Kevin's suggestion.

#### [Guillermo Barajas Ayuso (Sep 12 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133797345):
I see, thaks a lot! Also how would you prove the following?
```
example (h : n < m) : (n : ℝ) < (m : ℝ) := sorry
```

#### [Guillermo Barajas Ayuso (Sep 12 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133797368):
Sorry I forgot to define n and m
```
example {n m : ℕ} (h : n < m) : (n : ℝ) < (m : ℝ) := sorry
```

#### [Kenny Lau (Sep 12 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133797477):
nat.cast_lt or something

#### [Kenny Lau (Sep 12 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133797482):
(alternatively, induct on `h`)

#### [Guillermo Barajas Ayuso (Sep 12 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naturals_in_reals/near/133797598):
Ok, thanks!

