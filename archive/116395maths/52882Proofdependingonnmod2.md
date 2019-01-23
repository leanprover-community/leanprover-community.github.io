---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/52882Proofdependingonnmod2.html
---

## Stream: [maths](index.html)
### Topic: [Proof depending on n mod 2](52882Proofdependingonnmod2.html)

---


{% raw %}
#### [ Johan Commelin (Jul 16 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129743513):
I need to prove a fact about `(-a)^n`, with `n : nat`. I would like to split into two cases, depending on whether `n` is odd or even. What is the best way to do this in mathlib?

#### [ Kenny Lau (Jul 16 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744299):
what is it that you want to prove?

#### [ Kenny Lau (Jul 16 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744303):
you might be able to rewrite `n` into `(n/2)*2 + (n%2)` if you use the division algorithm

#### [ Chris Hughes (Jul 16 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744396):
`nat.mod_two_eq_zero_or_one` I believe

#### [ Kenny Lau (Jul 16 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744408):
my point is, sometimes you don't need to split into two cases

#### [ Johan Commelin (Jul 16 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744766):
Ok, I'll try that.

#### [ Johan Commelin (Jul 16 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744770):
So, here is another substep that I currently have:
```lean
rw show v * (-a)^n = ((-1)^n * v) * a^n,
    begin
      rw [neg_eq_neg_one_mul, mul_pow], ring,
    end,
```

#### [ Kenny Lau (Jul 16 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744815):
could you include the types of `v` and `a`?

#### [ Johan Commelin (Jul 16 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744818):
Should `ring` be able to do those rewrites itself? I think it would make sense to me to teach `ring` about negatives...

#### [ Johan Commelin (Jul 16 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744829):
`v` and `a` live in some comm ring.

#### [ Kenny Lau (Jul 16 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744918):
it isn't about negatives

#### [ Kenny Lau (Jul 16 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744920):
it's about powers

#### [ Kenny Lau (Jul 16 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129744924):
`ring` can't prove this:
```lean
example : x^n * y^n = (x * y)^n := by ring
```

#### [ Johan Commelin (Jul 16 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129745010):
Should ring be able to prove it, by `rw mul_pow` whenever possible?

#### [ Kenny Lau (Jul 16 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129745014):
I don't know what `ring` knows

#### [ Johan Commelin (Jul 16 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129745076):
My "Should" was a *moral* should. As in, does it make sense to give `ring` these extra powers?

#### [ Mario Carneiro (Jul 16 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129745230):
No. It is not a rewrite system, it is a decision procedure for polynomial equalities. `x^n` is not a polynomial (of two variables `x`, `n`)

#### [ Kenny Lau (Jul 16 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129745235):
fair enough

#### [ Johan Commelin (Jul 16 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129745425):
Mario, so would it make sense to rename `ring` into `semiring`, and have a `ring` tactic that is `semiring` + some other superpowers?

#### [ Mario Carneiro (Jul 16 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129745483):
`ring` deals with commutative rings and commutative semirings

#### [ Mario Carneiro (Jul 16 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129745495):
Negatives are supported

#### [ Johan Commelin (Jul 16 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129746954):
Ok, so what is the fastest way to prove `H : ∀ {n : ℕ}, ((-1 : R)^n = 1) ∨ ((-1 : R)^n = -1)`, where `R` is a `comm_ring`.

#### [ Mario Carneiro (Jul 16 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747046):
that could probably go in `group_power.lean`

#### [ Patrick Massot (Jul 16 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747062):
That's the fastest way: have Mario write it in mathlib

#### [ Mario Carneiro (Jul 16 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747072):
but you can prove it either by induction or by quotient remainder theorem like kenny suggested

#### [ Johan Commelin (Jul 16 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747095):
I'm halfway a proof by induction, but everytime I need a stupid little fact from mathlib it costs me 15 minutes to find it...

#### [ Kenny Lau (Jul 16 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747269):
```lean
import tactic.ring

universe u
variables (R : Type u) [comm_ring R] (n : nat)

example : ((-1 : R)^n = 1) ∨ ((-1 : R)^n = -1) :=
begin
  induction n with n ih, {simp},
  rw [pow_succ, neg_one_mul, neg_inj', neg_eq_iff_neg_eq, eq_comm, or_comm],
  assumption
end
```

#### [ Kenny Lau (Jul 16 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747273):
that's 7 minutes :P

#### [ Kenny Lau (Jul 16 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747459):
```lean
import tactic.ring

universe u
variables (R : Type u) [comm_ring R] (n : nat)

example : ((-1 : R)^n = 1) ∨ ((-1 : R)^n = -1) :=
begin
  induction n with n ih, {simp},
  cases ih with ih ih,
  { right, simp [pow_succ, ih] },
  { left, simp [pow_succ, ih] }
end
```

#### [ Kenny Lau (Jul 16 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747482):
```lean
import tactic.ring

universe u
variables (R : Type u) [comm_ring R] (n : nat)

example : ((-1 : R)^n = 1) ∨ ((-1 : R)^n = -1) :=
begin
  induction n with n ih, {simp},
  cases ih with ih ih; [right, left];
  simp [pow_succ, ih]
end
```

#### [ Johan Commelin (Jul 16 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747491):
You win (-;

#### [ Mario Carneiro (Jul 16 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747550):
Now you are just showing off :P

#### [ Mario Carneiro (Jul 16 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747557):
What's it look like using the equation compiler for the induction?

#### [ Kenny Lau (Jul 16 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747574):
not much difference, I think

#### [ Mario Carneiro (Jul 16 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747711):
I think it's a bit neater
```
theorem neg_one_pow_eq_or {R} [comm_ring R] : ∀ n : ℕ, ((-1 : R)^n = 1) ∨ ((-1 : R)^n = -1)
| 0     := by simp
| (n+1) := by cases neg_one_pow_eq_or n; simp [pow_succ, h]
```
also `left` and `right` are unnecessary

#### [ Kenny Lau (Jul 16 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747723):
I see

#### [ Kenny Lau (Jul 16 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Proof%20depending%20on%20n%20mod%202/near/129747746):
```lean
import tactic.ring

universe u
variables (R : Type u) [comm_ring R] (n : nat)

example : ((-1 : R)^n = 1) ∨ ((-1 : R)^n = -1) :=
begin
  cases nat.mod_two_eq_zero_or_one n;
  rw [← nat.mod_add_div n 2, pow_add, pow_mul, h];
  simp [pow_two]
end
```


{% endraw %}
