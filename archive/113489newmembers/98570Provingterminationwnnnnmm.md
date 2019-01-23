---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/98570Provingterminationwnnnnmm.html
---

## Stream: [new members](index.html)
### Topic: [Proving termination w/ (n' < n \/ (n' = n /\ m' < m))](98570Provingterminationwnnnnmm.html)

---

#### [cbailey (Jan 10 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20termination%20w/%20%28n%27%20%3C%20n%20%5C/%20%28n%27%20%3D%20n%20/%5C%20m%27%20%3C%20m%29%29/near/154824198):
Is there any way to convince Lean that a function  f (n : nat, m : nat) -> T, where each recursive call satisfies ( n' < n \/ ( n' = n /\ m' < m ) ) is indeed terminating without explicitly adding a third parameter to represent (n + m) or gas?
Thank you!

#### [Kenny Lau (Jan 10 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20termination%20w/%20%28n%27%20%3C%20n%20%5C/%20%28n%27%20%3D%20n%20/%5C%20m%27%20%3C%20m%29%29/near/154824668):
1. give us an example 2. custom well-founded tactic

#### [Jeremy Avigad (Jan 10 2019 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20termination%20w/%20%28n%27%20%3C%20n%20%5C/%20%28n%27%20%3D%20n%20/%5C%20m%27%20%3C%20m%29%29/near/154824899):
You can do arbitrary well-founded recursion in Lean, though it doesn't always work as smoothly as one would like. 

https://leanprover.github.io/theorem_proving_in_lean/induction_and_recursion.html#well-founded-recursion-and-induction

In your case, I think the equation compiler (the system that compiles your function specification down to a function expressed in terms of the foundational primitives) will guess that you want to use lexicographic order, and with luck you'll be able to convince it that the recursive call is decreasing (as described in TPIL).

Generally speaking, though, life will be easier if you can find a structural recursion that will do the job.

#### [Kevin Buzzard (Jan 10 2019 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20termination%20w/%20%28n%27%20%3C%20n%20%5C/%20%28n%27%20%3D%20n%20/%5C%20m%27%20%3C%20m%29%29/near/154826761):
https://github.com/leanprover/mathlib/blob/master/docs/extras/well_founded_recursion.md

#### [cbailey (Jan 10 2019 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20termination%20w/%20%28n%27%20%3C%20n%20%5C/%20%28n%27%20%3D%20n%20/%5C%20m%27%20%3C%20m%29%29/near/154827110):
Thank you for the links @**Jeremy Avigad**  and @**Kevin Buzzard** ,  this looks like exactly what I need.

@**Kenny Lau**  I'm just using Euclid's algorithm. I'll try and put together a tactic with the reading material you guys referenced

Thanks!

#### [Wojciech Nawrocki (Jan 13 2019 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20termination%20w/%20%28n%27%20%3C%20n%20%5C/%20%28n%27%20%3D%20n%20/%5C%20m%27%20%3C%20m%29%29/near/155045083):
I found that definining the entire recursive function as an equation-compiler-expression and then ignoring some of the match variables in cases where they don't matter works best, e.g.:
```lean
def rec_fn: ℕ → ℕ → (ℕ → ℕ) → ℕ → ℕ
| _ b f 0 := f b
| a b f (n+1) := rec_fn a (b+a) f n
```
but then I end up having to type things like (real example):
```lean
def applyTypeSub: ∀ {Γ Γ' T}, SubFn Γ Γ' → Term Γ T → Term Γ' T
| _ _ _ s (Var v) := s _ v
| _ _ _ _ (Nat n) := Nat n
| _ _ _ _ (Bool b) := Bool b
| _ _ _ s (Abs e) := Abs (applyTypeSub (STmL s) e)
| _ _ _ s (App fn arg) := App (applyTypeSub s fn) (applyTypeSub s arg)
```
in order to make all the variables unify correctly.

