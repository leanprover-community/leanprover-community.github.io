---
author: 'Patrick Massot'
category: 'New in mathlib'
date: 2021-08-07 21:49:56 UTC+02:00
description: ''
has_math: true
link: ''
slug: continuous-partitions-of-unity
tags: ''
title: Continuous partitions of unity
type: text
---
In [PR #8281](https://github.com/leanprover-community/mathlib/pull/8281), Yury
Kudryashov completed his work on continuous and smooth partitions of unity.

A continuous partition of unity on a topological space $X$ is a collection of continuous functions
$f_i : X → ℝ$ such that:

* the supports of $f_i$ form a locally finite family of sets, i.e., for every point $x$ in $X$, there
  exists a neighborhood $U$ of $x$ such that all but finitely many functions $f_i$ are zero on $U$;
* the functions $f_i$ are nonnegative;
* the sum $\sum_i f_i(x)$ is equal to one for all $x$.

While the above definition is completely standard, it is often useful to have a collection of
function that act as a paritition of unity only on some part $s$ of $X$. In that more general case,
we keep the above two conditions everywhere but ask that the sum in the last item equals one on $s$
and is less than or equal to one everywhere. This is encoded in the following Lean structure, from
`topology.partition_of_unity`.

```lean
structure partition_of_unity (ι X : Type*) [topological_space X] (s : set X := univ) :=
(to_fun : ι → C(X, ℝ))
(locally_finite' : locally_finite (λ i, support (to_fun i)))
(nonneg' : 0 ≤ to_fun)
(sum_eq_one' : ∀ x ∈ s, ∑ᶠ i, to_fun i x = 1)
(sum_le_one' : ∀ x, ∑ᶠ i, to_fun i x ≤ 1)
```

The main result from that file is then the following existence theorem.

```lean
/-- If `X` is a paracompact normal topological space and `U` is an open covering of a closed set
`s`, then there exists a `partition_of_unity ι X s` that is subordinate to `U`. -/
lemma exists_is_subordinate [normal_space X] [paracompact_space X] (hs : is_closed s)
  (U : ι → set X) (ho : ∀ i, is_open (U i)) (hU : s ⊆ ⋃ i, U i) :
  ∃ f : partition_of_unity ι X s, f.is_subordinate U
```


