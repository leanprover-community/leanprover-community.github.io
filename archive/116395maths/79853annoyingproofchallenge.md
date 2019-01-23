---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/79853annoyingproofchallenge.html
---

## Stream: [maths](index.html)
### Topic: [annoying proof challenge](79853annoyingproofchallenge.html)

---

#### [Chris Hughes (Dec 01 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698181):
Is there a nice way to prove this?
```lean
example {a b : with_bot ℕ} (h : a + b = 1) : a = 0 ∨ b = 0
```

#### [Kenny Lau (Dec 01 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698441):
```lean

import algebra.ordered_group data.nat.basic

example : ∀ {a b : with_bot ℕ}, a + b = 1 → a = 0 ∨ b = 0
| (some a) (some 0) H := or.inr rfl
| (some a) (some (b+1)) H := or.inl $ (add_eq_zero_iff.1 (nat.succ_inj $ option.some.inj H)).1.symm ▸ 
```

#### [Kenny Lau (Dec 01 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698444):
@**Chris Hughes**

#### [Kevin Buzzard (Dec 01 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698524):
Didn't your mother tell you never to end a sentence with a `▸`?

#### [Chris Hughes (Dec 01 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698586):
Maybe it's some super duper eta reduction.

#### [Kenny Lau (Dec 01 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698638):
oops it's supposed to end in `rfl`

#### [Kenny Lau (Dec 01 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698639):
```lean
import algebra.ordered_group data.nat.basic

example : ∀ {a b : with_bot ℕ}, a + b = 1 → a = 0 ∨ b = 0
| (some a) (some 0) H := or.inr rfl
| (some a) (some (b+1)) H := or.inl $ (add_eq_zero_iff.1 (nat.succ_inj $ option.some.inj H)).1.symm ▸ rfl
```

#### [Kevin Buzzard (Dec 01 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698647):
oh that works better :-)

#### [Kevin Buzzard (Dec 01 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698701):
What does the equation compiler actually *do* to decide that it can ignore the `none` cases? I mean, what does it try?

#### [Kenny Lau (Dec 01 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698712):
```lean
import algebra.ordered_group data.nat.basic

theorem test : ∀ {a b : with_bot ℕ}, a + b = 1 → a = 0 ∨ b = 0
| (some a) (some 0) H := or.inr rfl
| (some a) (some (b+1)) H := or.inl $ (add_eq_zero_iff.1 (nat.succ_inj $ option.some.inj H)).1.symm ▸ rfl

#print test
/-
theorem test : ∀ {a b : with_bot ℕ}, a + b = 1 → a = 0 ∨ b = 0 :=
λ {a b : with_bot ℕ} (a_1 : a + b = 1),
  option.cases_on a
    (λ (a : none + b = 1),
       option.cases_on b
         (λ (a : none + none = 1),
            eq.dcases_on a (λ (a_1 : some 1 = none), option.no_confusion a_1) (eq.refl 1) (heq.refl a))
         (λ (b : ℕ) (a : none + some b = 1),
            eq.dcases_on a (λ (a_1 : some 1 = none), option.no_confusion a_1) (eq.refl 1) (heq.refl a))
         a)
    (λ (a : ℕ) (a_1 : some a + b = 1),
       option.cases_on b
         (λ (a_1 : some a + none = 1),
            eq.dcases_on a_1 (λ (a_2 : some 1 = none), option.no_confusion a_2) (eq.refl 1) (heq.refl a_1))
         (λ (b : ℕ) (a_1 : some a + some b = 1),
            nat.cases_on b (λ (a_1 : some a + some 0 = 1), id_rhs (some a = 0 ∨ some 0 = 0) (or.inr rfl))
              (λ (b : ℕ) (a_1 : some a + some (nat.succ b) = 1),
                 id_rhs (some a = 0 ∨ some (b + 1) = 0)
                   (or.inl (eq.symm ((add_eq_zero_iff.mp (nat.succ_inj (option.some.inj a_1))).left) ▸ rfl)))
              a_1)
         a_1)
    a_1
-/
```

#### [Kenny Lau (Dec 01 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698713):
it does `option.no_confusion`

#### [Kevin Buzzard (Dec 01 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/annoying%20proof%20challenge/near/150698763):
`option.no_confusion` is such a great name for a function. I might get it on a t-shirt.

