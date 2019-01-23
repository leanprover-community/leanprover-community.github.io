---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/70527prime617challenge.html
---

## Stream: [maths](index.html)
### Topic: [prime 617 challenge](70527prime617challenge.html)

---

#### [Kevin Buzzard (Jul 26 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130359176):
```lean
import data.nat.prime 

open nat 

example : prime 617 := sorry 
```

I tried `dec_trivial` with `local attribute [instance] decidable_prime_1` but it times out on my machine. There is a lemma that says p is prime iff no factors <= sqrt(p) -- can one somehow persuade Lean to use this?

#### [Kevin Buzzard (Jul 26 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130359652):
The reason this is even a thing is that a question on the number theory example sheet that students are working on asks them to use quadratic reciprocity to evaluate whether something is a square mod 617. They managed to solve the question assuming quadratic reciprocity and that 617 was prime :-) The smaller numbers we can handle

#### [Rob Lewis (Jul 26 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130360645):
It looks like `decidable_prime` already does this: https://github.com/leanprover/mathlib/blob/master/data/nat/prime.lean#L90

#### [Rob Lewis (Jul 26 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130360660):
Why are you trying to use `decidable_prime_1`?

#### [Rob Lewis (Jul 26 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130360768):
`#eval if nat.prime 617 then tt else ff` is  instant without adding the local instance.

#### [Mario Carneiro (Jul 26 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130361003):
You can also use `#eval to_bool (nat.prime 617)` for the same purpose

#### [Kevin Buzzard (Jul 26 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130361928):
I want a proof!

#### [Kevin Buzzard (Jul 26 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130361929):
```lean
import data.nat.prime 

open nat 

theorem sqrt617 : sqrt 617 = 24 :=
begin
  symmetry,
  rw eq_sqrt,
  split,
    exact dec_trivial,
    exact dec_trivial
end 

theorem prime617iff : prime 617 ↔ ∀ m, 2 ≤ m → m ≤ 24 → ¬ (m ∣ 617) :=
begin
  rw prime_def_le_sqrt,
  rw sqrt617,
  apply and_iff_right,
  exact dec_trivial
end 

theorem prime617 : prime 617 :=
begin
  rw prime617iff,
  show ∀ (m : ℕ), 2 ≤ m → m ≤ 24 → ¬m ∣ 617,
  exact dec_trivial -- times out :-(
end
```

Is it possible to work out how close I got?

#### [Kevin Buzzard (Jul 26 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130362377):
Hmm, I think I only make it up to 6 :-/

#### [Kevin Buzzard (Jul 26 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130362737):
Ok I have a strat. I can prove 617 = 154 * 4 + 1 using norm_num and then use some lemmas about division to reduce non-divisibility of 617 by 4 to non-divisibility of 1 by 4, which I can prove with `dec_trivial`. I then repeat up to 24. I write a python script which generates the code I want.

#### [Kevin Buzzard (Jul 26 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130363560):
```lean
import tactic.norm_num 
import data.nat.prime 

open nat 

theorem sqrt617 : sqrt 617 = 24 :=
begin
  symmetry,
  rw eq_sqrt,
  norm_num,
end 

theorem prime617iff : prime 617 ↔ ∀ m, 2 ≤ m → m ≤ 24 → ¬ (m ∣ 617) :=
begin
  rw prime_def_le_sqrt,
  rw sqrt617,
  apply and_iff_right,
  exact dec_trivial
end 


theorem prime617 : prime 617 :=
begin
  rw prime617iff,
  show ∀ (m : ℕ), 2 ≤ m → m ≤ 24 → ¬m ∣ 617,
  intros m hm1 hm2,
  cases m,cases hm1,
  cases m,cases hm1,cases hm1_a, -- m = 1
  cases m,show ¬ (2 ∣ 617), have h : 617 = 1 + 308 * 2 := by norm_num,rw h,intro h2,
    have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
  cases m,show ¬ (3 ∣ 617), have h : 617 = 2 + 205 * 3 := by norm_num,rw h,intro h2,
    have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
  cases m, show ¬ (4 ∣ 617), have h : 617 = 1 + 154 * 4 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (5 ∣ 617), have h : 617 = 2 + 123 * 5 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (6 ∣ 617), have h : 617 = 5 + 102 * 6 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (7 ∣ 617), have h : 617 = 1 + 88 * 7 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (8 ∣ 617), have h : 617 = 1 + 77 * 8 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (9 ∣ 617), have h : 617 = 5 + 68 * 9 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (10 ∣ 617), have h : 617 = 7 + 61 * 10 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (11 ∣ 617), have h : 617 = 1 + 56 * 11 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (12 ∣ 617), have h : 617 = 5 + 51 * 12 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (13 ∣ 617), have h : 617 = 6 + 47 * 13 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (14 ∣ 617), have h : 617 = 1 + 44 * 14 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (15 ∣ 617), have h : 617 = 2 + 41 * 15 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (16 ∣ 617), have h : 617 = 9 + 38 * 16 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (17 ∣ 617), have h : 617 = 5 + 36 * 17 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (18 ∣ 617), have h : 617 = 5 + 34 * 18 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (19 ∣ 617), have h : 617 = 9 + 32 * 19 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (20 ∣ 617), have h : 617 = 17 + 30 * 20 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (21 ∣ 617), have h : 617 = 8 + 29 * 21 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (22 ∣ 617), have h : 617 = 1 + 28 * 22 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (23 ∣ 617), have h : 617 = 19 + 26 * 23 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
cases m, show ¬ (24 ∣ 617), have h : 617 = 17 + 25 * 24 := by norm_num,rw h,intro h2,
have h3 := mod_eq_zero_of_dvd h2,rw add_mul_mod_self_right at h3,cases h3,
revert hm2,exact dec_trivial,
end
```

#### [Kevin Buzzard (Jul 26 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130363563):
There's a proper proof.

#### [Mario Carneiro (Jul 26 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130363582):
I'm on it...

#### [Kevin Buzzard (Jul 26 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130363741):
/me thinks that `#eval` should be renamed `#evil`

#### [Rob Lewis (Jul 26 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130364211):
Ah, sorry, I shouldn't try to read this while listening to talks.

#### [Rob Lewis (Jul 26 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130364221):
I end up missing obvious things in both places!

#### [Mario Carneiro (Jul 28 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130449391):
Challenge accepted
```
example : nat.prime 617 := by norm_num
```

#### [Kenny Lau (Jul 28 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130451800):
```lean
import tactic.norm_num data.nat.prime

theorem prime_617 : nat.prime 617 := by norm_num

/-
norm_num failed to simplify
state:
⊢ nat.prime 617
-/
```

#### [Johan Commelin (Jul 28 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130453651):
A wonderful example of the theorem that examples aren't theorems.

#### [Kevin Buzzard (Jul 28 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130455413):
Maybe you should have tried 57

#### [Kevin Buzzard (Jul 28 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130455453):
Looks like I need to update my blog post :-)

#### [Kevin Buzzard (Jul 28 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130455877):
```quote
```lean
import tactic.norm_num data.nat.prime

theorem prime_617 : nat.prime 617 := by norm_num

/-
norm_num failed to simplify
state:
⊢ nat.prime 617
-/
```
```
Kenny it works for me. Did you update your mathlib? This is code that Mario just wrote.

#### [Kevin Buzzard (Jul 28 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/prime%20617%20challenge/near/130455927):
And thanks Mario! I think my students were going to have some trouble with the example sheet questions if they couldn't get as far as 617.

