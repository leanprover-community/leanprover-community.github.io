---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/39139Constructinganiteexpressionwithout.html
---

## Stream: [new members](index.html)
### Topic: [Constructing an ite expression without %%](39139Constructinganiteexpressionwithout.html)

---

#### [Ken Roe (Jul 24 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Constructing%20an%20ite%20expression%20without%20%25%25/near/130183355):
I entered the following code to construct an ite expression in a meta def:
```lean
def xeval (a : ℕ) (b : ℕ) := if a=0 then 0 else b.

def beq_nat : ℕ → ℕ → bool
| 0 0 := tt
| (x+1) (y+1) := (beq_nat x y)
| (x+1) 0 := ff
| 0 (x+1) := ff


meta def evaluate_xeval_helper : expr → expr
| `(xeval %%x %%y) :=
      (app (app (app `(ite)
                     (app (app `(beq_nat))) x `(0))
                     `(0))
                     y)
| x := x
```
The word "ite" gets the error
```lean
failed to synthesize type class instance for
evaluate_xeval_helper : expr → expr,
_x : list level,
x y : expr
⊢ reflected ite
```
How do I fix this error?

#### [Sebastian Ullrich (Jul 25 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Constructing%20an%20ite%20expression%20without%20%25%25/near/130244278):
The error is because the universe parameter of `ite` could not be inferred. If you use the full quotation
```
`(if beq_nat %%x 0 then (0 : nat) else %%y)
```
it should work

