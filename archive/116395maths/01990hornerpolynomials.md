---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/01990hornerpolynomials.html
---

## [maths](index.html)
### [horner polynomials](01990hornerpolynomials.html)

#### [Chris Hughes (Nov 29 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/horner%20polynomials/near/148810007):
I remember @**Johannes Hölzl**  saying something in Orsay about having an interface for polynomials in horner form? What exactly did he mean by this? Is something like this worth having, and is it worth proving the equation lemmas for this, and proving it in a semiring? It does make some proofs easier.
```lean
@[elab_as_eliminator] def rec_on_horner {α : Type*}
  [nonzero_comm_ring α] [decidable_eq α]
  {M : polynomial α → Sort*} : Π (p : polynomial α),
  M 0 →
  (Π p a, coeff p 0 = 0 → a ≠ 0 → M p → M (p + C a)) →
  (Π p, p ≠ 0 → M p → M (p * X)) →
  M p
| p := λ M0 MC MX,
if hp : p = 0 then eq.rec_on hp.symm M0
else
have wf : degree (p /ₘ X) < degree p,
  from degree_div_by_monic_lt _ monic_X hp (by rw degree_X; exact dec_trivial),
by rw [← mod_by_monic_add_div p monic_X, mod_by_monic_X, ← coeff_zero_eq_eval_zero,
  add_comm, mul_comm] at *;
  exact
  if hcp0 : coeff p 0 = 0
  then by rw [hcp0, C_0, add_zero];
    exact MX _ (λ h : p /ₘ X = 0, by simpa [h, hcp0] using hp)
      (rec_on_horner _ M0 MC MX)
  else MC _ _ (coeff_mul_X_zero _) hcp0 (if hpX0 : p /ₘ X = 0
    then show M (p /ₘ X * X), by rw [hpX0, zero_mul]; exact M0
    else MX (p /ₘ X) hpX0 (rec_on_horner _ M0 MC MX))
using_well_founded {dec_tac := tactic.assumption}
```

#### [Johannes Hölzl (Nov 30 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/horner%20polynomials/near/148849553):
My idea was a little bit different. Instead of using `p + C a` and assuming `coeff p 0 = 0` we only use
```lean
def horner p a := p * X + C a
```
My hope is that some proofs are easier using this construction, especially proofs about `coeff` `degree` etc. 
And it would not be limited to a recursor, but would also include a lot of rewrite rules for `horner`. 

I also tried to define polynomials using the horner scheme, i.e. `subtype` on `list` with an additional non-leading zero assumption.

