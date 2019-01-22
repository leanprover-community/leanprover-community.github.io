---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/36129Sumsoverfinsets.html
---

## [maths](index.html)
### [Sums over finsets](36129Sumsoverfinsets.html)

#### [Johan Commelin (May 22 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Sums%20over%20finsets/near/126924811):
I'm stuck on the following triviality
```lean
lemma sums {m n : ℕ} (f : fin m → fin n) (x : fin m → ℕ)
: sum univ (λ j : fin n, sum (univ.filter (λ i, f i = j)) x) = sum univ x
:= sorry
```
It looks like I might want to use `finset.sum_sigma` but I don't see how to get all the sigma's in place. And the unification magic doesn't do the job either.

#### [Johan Commelin (May 22 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Sums%20over%20finsets/near/126924898):
@**Kevin Buzzard** @**Chris Hughes**  I remember that you were also working on these kind of sum-rewritings about 2 months ago. Is this similar to what you did?

#### [Johannes Hölzl (May 22 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Sums%20over%20finsets/near/126925378):
you can use `finset.sum_bind` to combine both sum to a single one and then use extensionality that the combination of the index sets on the right is `univ`. Or use `finset.sum_subset`  which also uses some sort of extensionality.

#### [Johan Commelin (May 22 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Sums%20over%20finsets/near/126925926):
Ok, thanks!

#### [Johan Commelin (May 22 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Sums%20over%20finsets/near/126933905):
Ok, I proved the lemma using `bind` and `ext.2`. Thanks a lot!

