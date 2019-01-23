---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/12422HelpwithLean.html
---

## Stream: [new members](index.html)
### Topic: [Help with Lean](12422HelpwithLean.html)

---

#### [Ken Roe (Jul 10 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411503):
I just started using Lean.  Can someone help me by telling me what I need to replace "sorry" with to prove this theorem:

def beq_nat : ℕ → ℕ → bool
| beq_nat 0 0 := tt
| beq_nat (x+1) (y+1) := (beq_nat x y)
| beq_nat a b := ff

example : beq_nat 3 3=tt := by sorry.

#### [Kenny Lau (Jul 10 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411598):
your definition does not compile

#### [Patrick Massot (Jul 10 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411605):
```lean
def beq_nat : ℕ → ℕ → bool
| 0 0 := tt
| (x+1) (y+1) := (beq_nat x y)
| a b := ff

example : beq_nat 3 3=tt := rfl
```

#### [Patrick Massot (Jul 10 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411633):
strange definition

#### [Kenny Lau (Jul 10 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411644):
I don't think it's strange

#### [Kenny Lau (Jul 10 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411649):
it's a viable way to prove that equality is decidable

#### [Patrick Massot (Jul 10 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411658):
it's less efficient than using the maths preamble

#### [Ken Roe (Jul 10 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411729):
I get the following using "rfl":

impHeap.lean:35:28: error
type mismatch, term
  rfl
has type
  ?m_2 = ?m_2
but is expected to have type
  beq_nat 3 3 = tt

#### [Kenny Lau (Jul 10 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411741):
we changed the definition

#### [Kenny Lau (Jul 10 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411747):
your original definition does not compile

#### [Ken Roe (Jul 10 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411943):
How do I fix the definition?

#### [Patrick Massot (Jul 10 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411945):
see my message

#### [Kenny Lau (Jul 10 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411946):
we already gave you the new definition

#### [Kenny Lau (Jul 10 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411966):
```quote
```lean
def beq_nat : ℕ → ℕ → bool
| 0 0 := tt
| (x+1) (y+1) := (beq_nat x y)
| a b := ff

example : beq_nat 3 3=tt := rfl
```
```
:point_up: https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/subject/Help.20with.20Lean/near/129411605

#### [Ken Roe (Jul 10 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129412219):
Thanks--didn't notice they were different.  It appears the syntax for recursive definitions changed from Lean 2.0.  This definition (copied from the Lean 2.0 tutorial) also fails:

definition fib : nat → nat
| fib 0     := 1
| fib 1     := 1
| fib (a+2) := fib (a+1) + fib a

#### [Kenny Lau (Jul 10 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129412223):
how old is Lean 2.0 lol

#### [Kenny Lau (Jul 10 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129412266):
I don't think I ever used Lean 2.0

#### [Kenny Lau (Jul 10 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129412274):
```lean
definition fib : nat → nat
| 0 := 1
| 1 := 1
| (a+2) := fib (a+1) + fib a
```

#### [Patrick Massot (Jul 10 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129416618):
You shouldn't be reading anything written for Lean 2. This is all difficult enough without adding this layer of confusion. Reading https://leanprover.github.io/theorem_proving_in_lean/ will already bring you a long way

