---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/29815uniquelimit.html
---

## [maths](index.html)
### [unique limit](29815uniquelimit.html)

#### [Patrick Massot (Jan 19 2019 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/unique limit/near/156454309):
@**Kevin Buzzard** I looked at https://github.com/ImperialCollegeLondon/M1P1-lean/blob/master/src/limits.lean There is a comment saying you don't know how to use `wlog`. I think what you were looking for is:
```lean
lemma limits_aux (a : ℕ → ℝ) (l m : ℝ) (hl : is_limit a l)
(hm : is_limit a m) : l = m :=
begin
  by_contradiction h,
  wlog h' : l < m,
  { have := lt_trichotomy l m, tauto, },
```
and then put the proof exactly as it was (and remove "_aux" from the name of the lemma since it's now directly proving what you want)

#### [Patrick Massot (Jan 19 2019 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/unique limit/near/156454331):
But your proof is rather contrived. Why not doing:
```lean
lemma zero_of_abs_lt_all (x : ℝ) (h : ∀ ε, ε > 0 → |x| < ε) : x = 0 :=
eq_zero_of_abs_eq_zero $ eq_of_le_of_forall_le_of_dense (abs_nonneg x) $ λ ε ε_pos, le_of_lt (h ε ε_pos)

theorem limits_are_unique (a : ℕ → ℝ) (l m : ℝ) (hl : is_limit a l)
(hm : is_limit a m) : l = m :=
begin
  suffices : ∀ ε : ℝ, ε > 0 → |l - m| < ε,
  from eq_of_sub_eq_zero (zero_of_abs_lt_all _ this),
  intros ε ε_pos,
  cases hl (ε/2) (by linarith) with Nl H,
  cases hm (ε/2) (by linarith) with Nm H',
  let N := max Nl Nm,
  specialize H  N (le_max_left  _ _),
  specialize H' N (le_max_right _ _),
  exact calc |l - m| ≤ |a N - m| + |a N - l| : triangle' _ _ _
   ... < ε/2 + ε/2 : add_lt_add H' H
   ... = ε : by ring,
end
```
which seems to obey your stylistic constraints?

