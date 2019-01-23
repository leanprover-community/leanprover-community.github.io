---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/27561Recursorsfordegreeinequalities.html
---

## Stream: [maths](index.html)
### Topic: [Recursors for degree inequalities](27561Recursorsfordegreeinequalities.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 19 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Recursors%20for%20degree%20inequalities/near/147942053):
Today I wrote two proofs of the following lemma, about nonconstant polynomials. They illustrate a use of recursive propositions. For the second proof, I defined `nonconstant` as a recursive Proposition, instead of `degree p > 0`, and it was a much easier proof that didn't have any of the faffing around with degree. Is this sort of stuff worth having in the library. I'm experimenting with finding a useful recursor for `degree p < degree q`.
```lean
lemma polynomial_tendsto_infinity : ∀ {p : polynomial ℂ}, 0 < degree p →
  ∀ x : ℝ, ∃ r : ℝ, ∀ z : ℂ, r < z.abs → x < (p.eval z).abs
```
The first is this very long ugly one. 49 lines
```lean
lemma polynomial_tendsto_infinity : ∀ {p : polynomial ℂ}, 0 < degree p →
  ∀ x : ℝ, ∃ r : ℝ, ∀ z : ℂ, r < z.abs → x < (p.eval z).abs
| p := λ hp x, if h : degree p = 1
then
  let ⟨n, hn⟩ := archimedean.arch (1 : ℝ)
    (show 0 < abs (leading_coeff p),
      from abs_pos.2 (λ hp0, by simp * at *; contradiction)) in
  ⟨↑n * abs (p.eval 0) + n * (_root_.abs x), λ z hz,
    calc x ≤ _root_.abs x : le_abs_self _
    ... < abs (p.eval z) : lt_of_mul_lt_mul_left
      (calc (n : ℝ) * _root_.abs x < abs z - n * abs (eval 0 p) :
          lt_sub_iff_add_lt'.2 hz
        ... ≤ n * abs (leading_coeff p * z) - n * abs (p.eval 0) :
          sub_le_sub_right (by rw [complex.abs_mul, ← mul_assoc];
          exact le_mul_of_ge_one_left (complex.abs_nonneg _)
            (by simpa [mul_comm, add_monoid.smul_eq_mul] using hn)) _
        ... = ↑n * (abs (leading_coeff p * z) - abs (-eval 0 p)) : by simp [mul_add]
        ... ≤ ↑n * (abs (leading_coeff p * z - -eval 0 p)) :
          mul_le_mul_of_nonneg_left
            (le_trans (le_abs_self _) (complex.abs_abs_sub_le_abs_sub _ _))
            (nat.cast_nonneg n)
        ... = ↑n * abs (p.eval z) :
          by conv_rhs {rw degree_eq_one h}; simp [coeff_zero_eq_eval_zero])
      (nat.cast_nonneg n)⟩
else
  have wf : degree (p /ₘ X) < degree p,
    from degree_div_by_monic_lt _ monic_X (λ hp0, by simp * at *)
      (by rw degree_X; exact dec_trivial),
  have hp : 1 < degree p, from match degree p, hp, h with
    | none    := dec_trivial
    | (some n) := λ h0 h1, lt_of_le_of_ne (with_bot.coe_le_coe.2 (with_bot.coe_lt_coe.1 h0)) (ne.symm h1)
    end,
  have hXp : degree X ≤ degree p, from le_of_lt (by rw @degree_X ℂ; exact hp),
  let ⟨r, hr⟩ := @polynomial_tendsto_infinity (p /ₘ X)
    (@lt_of_add_lt_add_left' _ _ (1 : with_bot ℕ) _ _
      (calc (1 : with_bot ℕ) + 0 < degree p : hp
        ... = 1 + degree (p /ₘ X) : by rw [← @degree_X ℂ, degree_add_div_by_monic monic_X hXp]))
  (x + (p.eval 0).abs) in
  ⟨max 1 (r + (p.eval 0).abs), λ z hz,
    calc x < abs (eval z (p /ₘ X)) - abs (eval 0 p) :
      lt_sub_iff_add_lt.2 (hr z (lt_of_le_of_lt (le_add_of_nonneg_right (complex.abs_nonneg _))
        (lt_of_le_of_lt (le_max_right _ _) hz)))
    ... ≤ abs z * abs (eval z (p /ₘ X)) - abs (eval 0 p) :
      sub_le_sub_right (le_mul_of_ge_one_left (complex.abs_nonneg _) (le_trans (le_max_left _ _) (le_of_lt hz))) _
    ... ≤ _root_.abs (abs (z * eval z (p /ₘ X)) - abs (-eval 0 p)) : by rw [complex.abs_neg, ← complex.abs_mul];
      exact le_abs_self _
    ... ≤ abs (z * eval z (p /ₘ X) - -eval 0 p) : abs_abs_sub_le_abs_sub _ _
    ... = abs (eval z p) : by conv_rhs {rw ← mod_by_monic_add_div p monic_X};
      simp [coeff_zero_eq_eval_zero, mod_by_monic_X]⟩
using_well_founded {dec_tac := tactic.assumption}
```
The second is this much shorter one.
```lean
inductive nonconstant : polynomial ℂ → Prop
| X   : ∀ {a}, a ≠ 0 → nonconstant (C a * X) 
| mul : ∀ {p}, nonconstant p → nonconstant (p * X)
| add : ∀ {p} (a), nonconstant p → nonconstant (p + C a)

lemma nonconstant_of_degree_pos : ∀ {p : polynomial ℂ}, 
  0 < degree p → nonconstant p
| p := λ h, 
have wf : degree (p /ₘ X) < degree p,
  from degree_div_by_monic_lt _ monic_X 
  (λ hp0, by simp [hp0, lt_irrefl, *] at *) 
  (by rw degree_X; exact dec_trivial),
by rw [← mod_by_monic_add_div p monic_X,
  add_comm, mod_by_monic_X, mul_comm] at *;
exact nonconstant.add _ 
  (if hpX : 0 < degree (p /ₘ X) 
    then nonconstant.mul (nonconstant_of_degree_pos hpX)
    else by rw [eq_C_of_degree_le_zero (not_lt.1 hpX)] at *;
      exact if hc : coeff (p /ₘ X) 0 = 0
        then by simpa [hc, not_lt_of_ge degree_C_le] using h
        else nonconstant.X hc)
using_well_founded {dec_tac := tactic.assumption}

lemma polynomial_tendsto_infinity' {p : polynomial ℂ} (h : 0 < degree p) :
  ∀ x : ℝ, ∃ r : ℝ, ∀ z : ℂ, r < z.abs → x < (p.eval z).abs :=
nonconstant.rec_on (nonconstant_of_degree_pos h)
  (λ a ha x, ⟨x / a.abs, λ z hz, 
    by simpa [(div_lt_iff' (complex.abs_pos.2 ha)).symm]⟩)
  (λ p hp ih x, let ⟨r, hr⟩ := ih x in
    ⟨max r 1, λ z hz, by rw [eval_mul, eval_X, complex.abs_mul];
        exact lt_of_lt_of_le (hr z (lt_of_le_of_lt (le_max_left _ _) hz)) 
          (le_mul_of_ge_one_right (complex.abs_nonneg _) 
            (le_trans (le_max_right _ _) (le_of_lt hz)))⟩)
  (λ p a hp ih x, let ⟨r, hr⟩ := ih (x + a.abs) in
    ⟨r, λ z hz, by rw [eval_add, eval_C, ← sub_neg_eq_add];
      exact lt_of_lt_of_le (lt_sub_iff_add_lt.2 
        (by rw complex.abs_neg; exact (hr z hz))) 
        (le_trans (le_abs_self _) (complex.abs_abs_sub_le_abs_sub _ _))⟩)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 19 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Recursors%20for%20degree%20inequalities/near/147946548):
Hey, that's a smart approach I think. I think the lemma should be `nonconstant_iff_degree_pos`, so that you can go back and forth.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Recursors%20for%20degree%20inequalities/near/147946661):
another way to express this is to write a "recursor" for `degree p > 0` along these lines

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 19 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Recursors%20for%20degree%20inequalities/near/147946725):
that recursor is equivalent to the theorem `nonconstant_of_degree_pos` but doesn't require defining a new predicate

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Nov 19 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Recursors%20for%20degree%20inequalities/near/147951339):
I love the way you avoid the clunky `using_well_founded` construct :).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 19 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Recursors%20for%20degree%20inequalities/near/147952836):
Vaguely related: when I was working on Hilbert Basis (before module refactoring), I found using degree very hard; there were often case splits. `deg(X)=1` was only true if the ring wasn't the zero ring, `deg(f) * c = deg(f)` was only true when c*leading_coeff(f) was non-zero, `deg(f+g)` was a mass of case splits, and so on. It was only later on that I realised that the natural condition was "deg <= n" not "deg = n"; for "deg <= n" (which produces a sub-R-module of R[X]) all the lemmas are very natural. "Non-constant" is the negation of "deg <= 0" but I don't know if this has anything to do with the obstructions that Chris was running into.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 19 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Recursors%20for%20degree%20inequalities/near/147953494):
I'm sure it would be good to have nicer recursors for polynomial but, for the purpose of this properness proof, what is missing in order to write an efficient proof is the big O library (I should resume work on that). As far as I understand, the best formal proofs are sequences of lemmas with three lines long proofs. Here there is a very clear path where you prove $$aX^ n$$ is $$O(X^n)$$ then $$X^n = o(X^k)$$ if $$k$$ bigger than $$n$$, then  $$O(f) + O(f) = O(f)$$ (this one is already in our WIP I think!) then $$P = O(X^{deg P})$$, then $$f$$ proper implies $$f + o(f)$$ proper and then $X^n$ is proper for positive $$n$$. Maybe I missed one or two lemmas, but you get the idea. This will be a string of reusable 2 lines long proofs lemmas, and will match the paper and pen proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Nov 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Recursors%20for%20degree%20inequalities/near/147953617):
Also the story about the projective line is a bit misleading here, since we don't need any structure on $$P^1$$ in this discussion, except maybe topological. We need filters stuff for sure, maybe also Alexandrov compactification if we want


{% endraw %}
