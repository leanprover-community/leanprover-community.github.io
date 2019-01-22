---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27115listfromktol.html
---

## [general](index.html)
### [list from k to l](27115listfromktol.html)

#### [Patrick Massot (Apr 17 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20from%20k%20to%20l/near/125191252):
Is there a built-in way to generate the list of natural numbers from k to l? I can use `def myrange (k n : ℕ) := list.map (λ i, i + k) (list.range $ n-k+1)` but I'd like to know if this is already in

#### [Kenny Lau (Apr 17 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20from%20k%20to%20l/near/125191309):
```lean
import data.list

#reduce list.range' 3 5 -- [3, 4, 5, 6, 7]
```

#### [Patrick Massot (Apr 17 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20from%20k%20to%20l/near/125191349):
It's almost what I was asking for

#### [Patrick Massot (Apr 17 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20from%20k%20to%20l/near/125191352):
my version would return `[3, 4, 5]`

#### [Mario Carneiro (Apr 17 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20from%20k%20to%20l/near/125191412):
you will have to use `n-k+1` as the upper bound for that

#### [Patrick Massot (Apr 17 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20from%20k%20to%20l/near/125191465):
Ok, so I still need to define a function. Is there any advantage of using `list.range' k (n+k-1)` instead of my implementation? I guess it's a bit faster, but I would be more interested if there are lemmas about range'

#### [Patrick Massot (Apr 17 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20from%20k%20to%20l/near/125191962):
At least I was able to state the next lemma in my small experimentation:
```lean
local notation `Π_{i=` k `..` n `}` f := list.prod ((list.range' k (n-k+1)).map f)

lemma commutators_crunching (U : set X) (φ f : homeo X X)
(wandering_hyp : ∀ i j : ℕ, i ≠ j → ⇑(φ^i) '' U ∩ ⇑(φ^j) '' U = ∅)
(n : ℕ) (a : ℕ → homeo X X) (b : ℕ → homeo X X) 
(supp_hyp : ∀ k : ℕ, supp (a k) ⊆ U ∧ supp (b k) ⊆ U)
(comm_hyp : f = Π_{i=1..n} λ i, [[a i, b i]]) :
∃ A B C D : homeo X X, f = [[A, B]]* [[C, D]] := 
sorry
```
`supp` is the (topological) support of a function, `[[. , .]]` is commutator. This will be a good test to see if I can manipulate products in any non-trivial way.

#### [Patrick Massot (Apr 17 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20from%20k%20to%20l/near/125192018):
Stating it was already some fight because I was unsure whether to use `ℕ`, `fin n` or `finset` as the source of `a` and `b` (I use only `a i` and `b i` when `i` is between `1` and `n`)

#### [Patrick Massot (Apr 17 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20from%20k%20to%20l/near/125192075):
Only `list` has support for non-commutative product. The above statement is the only combination I could get to work

#### [Kenny Lau (Apr 17 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/list%20from%20k%20to%20l/near/125195523):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/.60.5Ba.2Ca.2B1.2Ca.2B2.2C.2E.2E.2E.2Cb-1.5D.60.3F

