---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30622memeqself.html
---

## [general](index.html)
### [mem_eq_self](30622memeqself.html)

#### [Kevin Buzzard (Dec 02 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731070):
Harder than I expected!

```lean
theorem mem_eq_self {α : Type*} (a : α) : a ∈ {x : α | x = a} := sorry
```

#### [Kevin Buzzard (Dec 02 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731071):
Took me three attempts!

#### [Kenny Lau (Dec 02 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731079):
ok too me two attempts
```lean
theorem mem_eq_self {α : Type*} (a : α) : a ∈ {x : α | x = a} := eq.refl a
```

#### [Kevin Buzzard (Dec 02 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731132):
```lean
@[refl] theorem mem_eq_self {α : Type*} (a : α) : a ∈ {x : α | x = a} := eq.refl a

example : 3 ∈ {x : ℕ | x = 3} := by refl

```

@**Reid Barton** is this your suggestion? To those that didn't follow the other thread, the point is that without tagging `mem_eq_self` as `refl`, `by refl` doesn't work for the example.

#### [Kevin Buzzard (Dec 02 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731148):
`example : 3 ∈ {x : ℕ | 3 = x} := by refl` now works too. I don't really understand what is going on here.

#### [Kenny Lau (Dec 02 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731199):
```lean
-- all fail
example : 3 ∈ {x : ℕ | x = 3} := by refl
example : 3 ∈ {x : ℕ | x = x} := by refl
example : 3 ∈ {x : ℕ | 3 = 3} := by refl
example : 3 ∈ {x : ℕ | 3 = x} := by refl

@[refl] theorem mem_eq_self {α : Type*} (a : α) : a ∈ {x : α | x = a} := eq.refl a

-- all work
example : 3 ∈ {x : ℕ | x = 3} := by refl
example : 3 ∈ {x : ℕ | x = x} := by refl
example : 3 ∈ {x : ℕ | 3 = 3} := by refl
example : 3 ∈ {x : ℕ | 3 = x} := by refl
```

#### [Kevin Buzzard (Dec 02 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731247):
`example : 3 ∈ {x : ℕ | 3 = 3} := by refl` -- Doesn't that say `3 \in set.univ`? Why is that `by refl`?

#### [Kenny Lau (Dec 02 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731256):
no, set.univ is true

#### [Kevin Buzzard (Dec 02 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731261):
We're evaluating `lam x, 3 = 3` at `x=3` :-)

#### [Kevin Buzzard (Dec 02 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mem_eq_self/near/150731300):
so indeed it's refl

