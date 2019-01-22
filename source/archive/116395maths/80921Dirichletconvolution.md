---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/80921Dirichletconvolution.html
---

## [maths](index.html)
### [Dirichlet convolution](80921Dirichletconvolution.html)

#### [Elliott Macneil (Aug 15 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182031):
I'm trying to define the Dirichlet convolution on two arithmetic functions f,g but I'm having difficulty with writing the following sum in Lean.
```math
\Sigma_{d \mid n } f(d) g(n/d)
```
Could anyone possibly  write this in Lean?

#### [Kevin Buzzard (Aug 15 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182207):
Elliott I pushed a function which did this this morning.

#### [Kevin Buzzard (Aug 15 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182215):
What does this mean if n=0?

#### [Kevin Buzzard (Aug 15 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182218):
I stuck to `pnat`

#### [Kevin Buzzard (Aug 15 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182242):
https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/M3P14/sum_over_divisors.lean

#### [Kevin Buzzard (Aug 15 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182326):
so it's `\lam (n : pnat), divisor_sum (\lam d, f d * g (n / d)) n`

#### [Mario Carneiro (Aug 15 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182441):
```
lemma mem_factors_iff_divides (d : ℕ+) (e : ℕ) : e ∈ factors d ↔ e ∣ d :=
by simp [factors, -add_comm, nat.lt_succ_iff];
   exact and_iff_right_of_imp (le_of_dvd d.2)
```

#### [Mario Carneiro (Aug 15 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182491):
see, `logic.basic` is useful

#### [Mario Carneiro (Aug 15 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132182531):
you can also define `factors` using `finset.filter` to avoid the nodup proof

#### [Kevin Buzzard (Aug 15 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132185364):
Thanks and thanks! I was surprised that the divisors function (sending a pnat to a finset of its divisors) wasn't there, but Chris said he hadn't seen it (he had seen `factors` which in my mind is synonymous, however he said `factors` was the list of prime factors of n, which is not how the word is usually used in mathematics: factor does not imply prime).

#### [Mario Carneiro (Aug 15 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132185538):
I had the same train of thought

#### [Mario Carneiro (Aug 15 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132185596):
maybe it should be called `factorization`

#### [Mario Carneiro (Aug 15 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132185612):
note that it is not just the set of prime factors, it is like a multiset

#### [Kevin Buzzard (Aug 15 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132185688):
I should use simp for iff statements more...

#### [Elliott Macneil (Aug 15 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Dirichlet%20convolution/near/132191813):
Thanks for the help!

