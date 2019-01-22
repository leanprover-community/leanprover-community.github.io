---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/37885finntoTvsfinsuppfinnT.html
---

## [maths](index.html)
### [`fin n \to T` vs `finsupp (fin n) T`](37885finntoTvsfinsuppfinnT.html)

#### [Johan Commelin (May 28 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/`fin n \to T` vs `finsupp (fin n) T`/near/127206339):
General question: (`T` is a type) is it easy to move back and forth between `fin n \to T` and the finsupp variant?
Specific question: I am working with `nnreal^n`, and I model it as `fin n \to nnreal`. Now I have a map `fin n \to fin m` and I want to get the induced map `nnreal^n \to nnreal^m`. This is almost `finsupp.map_domain`. Except that I finitely supported functions, but general ones. Is it easy to still use `map_domain`?

#### [Chris Hughes (May 28 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/`fin n \to T` vs `finsupp (fin n) T`/near/127207254):
I guess you could just turn your fin n \to T into a finsupp quite easily. Just by doing `support := univ.filter (\la x, fx \ne!= 0)` etc.
Might e useful in general to define that function from a `fintype → T` to `fintype →₀ T`

#### [Johan Commelin (May 28 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/`fin n \to T` vs `finsupp (fin n) T`/near/127207269):
Should that go into mathlib?

#### [Johannes Hölzl (May 28 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/`fin n \to T` vs `finsupp (fin n) T`/near/127207324):
Yes. Just not for `fin n` specifically but for each `fintype`.

#### [Johan Commelin (May 28 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/`fin n \to T` vs `finsupp (fin n) T`/near/127207358):
Ok, I'll put it into finsupp.lean

#### [Johan Commelin (May 28 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/`fin n \to T` vs `finsupp (fin n) T`/near/127207407):
What is the canonical name for this beast?

#### [Johan Commelin (May 28 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/`fin n \to T` vs `finsupp (fin n) T`/near/127207409):
Some sort of `coe`?

#### [Johan Commelin (May 28 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/`fin n \to T` vs `finsupp (fin n) T`/near/127207412):
I've never done anything with `coe`

#### [Johan Commelin (May 28 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/`fin n \to T` vs `finsupp (fin n) T`/near/127207991):
```lean
def foobar {T : Type*} [has_zero T] [decidable_eq T] {X : Type*}  [fintype X] (f : X → T) : (X →₀ T) :=
{ support := univ.filter (λ x, f x ≠ 0),
  to_fun := f,
  mem_support_to_fun := λ x, ⟨λ h, (mem_filter.mp h).2, λ h, (mem_filter.mpr ⟨mem_univ x, h⟩)⟩}
```

