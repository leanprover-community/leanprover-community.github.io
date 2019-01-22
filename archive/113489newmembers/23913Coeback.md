---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/23913Coeback.html
---

## [new members](index.html)
### [Coe back](23913Coeback.html)

#### [Alexandru-Andrei Bosinta (Nov 25 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148320607):
If I have a positive integer, how do I get a natural number out of it? For more context, I need to use the floor function which outputs an integer and then do induction with this integer, with`let p : ℤ → Prop := λ (m : ℕ), m ≤ n → (n - m ∈ s ∨ (0 : ℤ) ∈ s), ` (s is a set of positive integers). I basically need to prove that if n is in the set, then 0 is in the set as well,  but induction on integers won't work because I can't prove a special case.

#### [Rob Lewis (Nov 25 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148321896):
I'm not sure I understand your situation exactly. Does `int.nat_abs` help you? `int.nat_abs (int.of_nat k)` reduces to `k`, and there are lemmas like `int.nat_abs_of_nonneg`.

#### [Kevin Buzzard (Nov 25 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148324816):
Although it's counter-intuitive to mathematicians, the way to get a nat back from a non-negative int is indeed to take the absolute value. You could think of the absolute value function as a function from int to nat which reverses the inclusion from nat to int, and returns junk for values not in the image; there are loads of such functions in Lean. Whenever a mathematician thinks they want a partial function (i.e. a function only defined on some elements of a nice set) the computer scientists tend to have defined it on all the set and either given it junk values on the other elements (e.g. log, which does some random thing to negative reals, and division, which does some random thing when you divide by 0) or observed that actually the function you want is the special case of a natural function which you might well want in general. For example the partial inverse of nat to int is called absolute value, the partial inverse of int to rat or real is called the floor function, the partial inverse of int to rat is called the numerator function. In all cases there will be a lemma which says that this function is indeed the one-sided inverse (i.e. `abs (n : Z) = n` if `n : nat` -- this is called `nat_abs_of_nat` and the proof is `rfl`), and if the image is easily classifiable (which it is for nat to int -- it's the non-negative ints) then there will be another lemma saying that the image is what you think it is it's (`of_nat_nonneg` in the nat to int case) and finally a lemma saying that if you're in the image and you go back then forward you get back to where you start ( Rob pointed out the relevant function in the nat to int case).

#### [Alexandru-Andrei Bosinta (Nov 25 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148328259):
Thanks for the explanation! It worked, but I've been having a lot of trouble with coercions so I had to rewrite my entire proof (which is already long). Now I am in the final stage of this proof.

#### [Kevin Buzzard (Nov 25 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148328316):
Coercions are really meh. Mathematicians don't know they are there. I think Lean is bad at handling them though. I would like to see Lean letting mathematicians use them as if they weren't there. Did you read my notes on cast? https://github.com/leanprover/mathlib/blob/master/docs/extras/casts.md Maybe they help. But it should all be easier.

#### [Kevin Buzzard (Nov 25 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148328371):
I occasionally think about whether one could handle all of this with typeclasses. Instead of going from int back to nat, have a typeclass `int.is_nat`on `int` which keeps track of whether something is a nat (and which nat it is). See if we can get the typeclass system to do the coersions for us, rather than `simp`.

Basic idea:

```lean
import data.real.basic

class real.nat (r : ℝ) :=
(n : ℕ)
(pf : r = ↑n)

class real.rat (r : ℝ) :=
(q : ℚ)
(pf : r = ↑q)

instance real.rat_of_nat (r : ℝ) [H : real.nat r] : real.rat r :=
⟨(H.n : ℚ),by simpa using H.pf⟩


```

#### [Alexandru-Andrei Bosinta (Nov 25 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148328491):
I didn't read your notes yet. I will have a look later, but I figured out how to do it. I basically tried to avoid using the `↑` operator and just try to use the functions which give you the coercions (`rat.mk n 1` for integer `n` to rational `n` and `int.nat_abs` for naturals to integers). It was really annoying because in my first attempt I was even getting an error about metavariables and `calc` wasn't working.

#### [Kevin Buzzard (Nov 25 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148328498):
Yeah, that's not how you're supposed to do it at all :-) No wonder it was a frustrating experience :-)

#### [Kevin Buzzard (Nov 25 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148328507):
I just use (n : rat) to get from nat to rat

#### [Kevin Buzzard (Nov 25 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148328552):
If you use the coercions then simp will do a lot of the dirty work for you. If you use the explicit functions then simp doesn't know about these so you have to do everything by hand.

#### [Kevin Buzzard (Nov 25 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148328569):
`simp` is a tool for proving *equalities*. Any two things which should "obviously be equal", like `\u a + \u b` and `\u (a + b)` -- `simp` should know this. You can figure out the lemmas yourself, but it's much easier to use simp.

#### [Alexandru-Andrei Bosinta (Nov 25 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148328626):
I started getting annoyed debugging my code, so I gave up and decided to do it my implicit functions which are way more clear to me.  It was probably not a very good way of doing my proof. I may try to fix the code later.

#### [Kevin Buzzard (Nov 25 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148328642):
If you post something here I can look at it. I've had to deal with a lot of coercions from nat to int in the past, so I know some tips.

#### [Alexandru-Andrei Bosinta (Nov 25 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148329229):
I will post it in a bit when I finish my whole proof. It shouldn't be long until I am done.

#### [Kevin Buzzard (Nov 25 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148329360):
If you look at my solutions to my example sheet questions from last year you will see me in coercion hell often -- Mario used to have to drag me out of the mire. Now at least I understand the way Lean has been designed with coercions, or at least well enough to mean I don't get stuck any more. Over the summer I had some people doing number theory, and they were forever coercing from nat to int and back again, and they struggled too (and Chris would have to drag them out of the mire).

#### [Alexandru-Andrei Bosinta (Nov 25 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148329649):
```
import data.rat data.set.basic order.bounds tactic.ring tactic.linarith data.nat.basic
open classical
local attribute [instance, priority 0] classical.prop_decidable

structure Dedekind_real :=
(carrier : set ℚ)
(nonemp : ∃ a, a ∈ carrier)
(nonrat : ∃ a, a ∉ carrier)
(down : ∀ (p : ℚ), p ∈ carrier → ∀ (q : ℚ), q ≤ p → q ∈ carrier)
(nomax : ∀ (p : ℚ), p ∈ carrier → ∃ (q : ℚ), q ∈ carrier ∧ p < q)

notation `ℝ` := Dedekind_real

lemma bounded_by_non_elements (α : ℝ) (x : ℚ): x ∉ α.carrier ↔ (∀ (q : ℚ), q ∈ α.carrier → q < x) := sorry

lemma suff_small_bound (α : ℝ) (ε : ℚ) (hε : ε > 0) : ∃ (a b : ℚ), a ∈ α.carrier ∧ b ∉ α.carrier ∧ b - a < ε :=
exists.elim α.nonemp (λ a ha, exists.elim α.nonrat (λ b hb, begin 
let n : ℤ := rat.floor ( (b-a)/ε ),
let s : set ℚ := {n | ∃ (a b : ℚ), a ∈ α.carrier ∧ b ∉ α.carrier ∧ ε*n ≤ b-a ∧ b-a < ε*(n+1)},
let p : ℕ → Prop := λ m, int.of_nat m ≤ n → rat.mk (n - int.of_nat m) 1 ∈ s ∨ (0 : ℚ) ∈ s,
have hn : p (int.nat_abs n), from nat.case_strong_induction_on (int.nat_abs n) 
(λ hpos, or.inl ⟨a, b, ha, hb, by calc
ε * (rat.mk (n - int.of_nat 0) 1) = ε * (rat.mk (n - 0) 1) : rfl 
... = ε * (rat.mk n 1) : by rw sub_zero
... = ε * ↑n : by rw rat.coe_int_eq_mk
... = ε * ↑(rat.floor ( (b-a)/ε ) ) : rfl
... ≤ ε * ( (b-a)/ε ) : (mul_le_mul_left hε).mpr (rat.floor_le ( (b-a)/ε ) )
... = ε * (b-a)/ε : by rw mul_div_assoc
... = b - a : by rw mul_div_cancel_left (b-a) (ne_of_gt hε), 
by calc b - a = ε * (b - a)/ε : by rw mul_div_cancel_left (b-a) (ne_of_gt hε)
... = ε * ( (b-a)/ε ) : by rw mul_div_assoc
... < ε * ↑(int.succ (rat.floor ( (b-a)/ε ) ) ) : (mul_lt_mul_left hε).mpr (rat.lt_succ_floor ( (b-a)/ε ) )
... = ε * (rat.mk (int.succ (rat.floor ( (b-a)/ε ) ) ) 1 ) : by rw rat.coe_int_eq_mk
... = ε * (rat.mk (rat.floor ( (b-a)/ε ) + 1) 1 ) : rfl
... = ε * ( (rat.mk (rat.floor ( (b-a)/ε ) ) 1 ) + (rat.mk 1 1) ) : by simp
... = ε * ( (rat.mk n 1) + 1) : rfl
... = ε * ( (rat.mk (n - 0) 1 ) + 1) : by rw sub_zero
... = ε * ( (rat.mk (n - int.of_nat 0) 1) + 1) : rfl⟩ ) 
(λ i hpi hpos, or.elim (hpi i (le_refl i) (trans (le_of_lt (lt_add_one i) ) hpos) ) 
(λ h, exists.elim h (λ a0 hb, exists.elim hb (λ b0 hab, (em (b0 - ε ∈ α.carrier)).elim 
(λ hb0, exists.elim (α.nomax (b0-ε) hb0) (λ b1 hb1, or.inr ⟨b1, b0, hb1.left, hab.right.left, le_of_lt (by calc
ε * 0 = 0 : by rw mul_zero
... < b0 - b1 : sub_pos_of_lt ( (bounded_by_non_elements α b0).mp hab.right.left b1 hb1.left)), by calc
b0 - b1 < ε : sub_lt.mp hb1.right
... = ε*1 : by rw mul_one
... = ε*(1-0) : by rw sub_zero⟩ ) ) 
(λ hb0, or.inl ⟨a0, b0-ε, hab.left, hb0, by calc
ε * (rat.mk (n - int.of_nat (nat.succ i) ) 1) = ε * (rat.mk (n - int.of_nat (i + 1) ) 1) : rfl
... = ε * ( rat.mk ( n - (int.of_nat i + int.of_nat 1) ) 1 ) : rfl
... = ε * ( rat.mk (n - (int.of_nat i + 1) ) 1) : rfl
... = ε * ( rat.mk (n - int.of_nat i - 1) 1 ) : by rw sub_sub
... = ε * ( rat.mk (n - int.of_nat i + -1) 1) : rfl
... = ε * ( ( rat.mk (n - int.of_nat i) 1) + (rat.mk (-1) 1) ) : by simp
... = ε * ( ( rat.mk (n - int.of_nat i) 1) + -1) : rfl
... = ε * ( rat.mk (n - int.of_nat i) 1) + ε * -1 : by rw mul_add
... = ε * ( rat.mk (n - int.of_nat i) 1) - ε : by simp
... ≤ b0-a0-ε : sub_le_sub_right hab.right.right.left ε
... = b0-ε-a0 : by rw sub_right_comm, 
by calc b0-ε-a0 = b0-a0-ε : by rw sub_right_comm
... < ε * (rat.mk (n - int.of_nat i) 1 + 1) - ε : sub_lt_sub_right hab.right.right.right ε
... = ε * (rat.mk (n - int.of_nat i) 1 + 1) - ε * 1 : by rw mul_one
... = ε * (rat.mk (n - int.of_nat i) 1 + 1 - 1) : by rw mul_sub
... = ε * (rat.mk (n - int.of_nat i) 1) : by rw add_sub_cancel
... = ε * (rat.mk (n - int.of_nat i) 1 - 1 + 1) : by rw sub_add_cancel
... = ε * (rat.mk (n - int.of_nat i) 1 - rat.mk 1 1 + 1) : rfl
... = ε * (rat.mk (n - int.of_nat i - 1) 1 + 1) : by simp
... = ε * (rat.mk (n - (int.of_nat i + 1) ) 1 + 1) : by rw sub_sub
... = ε * (rat.mk (n - (int.of_nat (i + 1) ) ) 1 + 1) : rfl
... = ε * (rat.mk (n - (int.of_nat (nat.succ i) ) ) 1 + 1) : rfl
⟩ ) ) ) ) or.inr),
have s0 : (0 : ℚ) ∈ s, 
apply or.elim (hn (trans_rel_right int.le (by calc 
int.of_nat (int.nat_abs n) = ↑(int.nat_abs n) : rfl
... = n : int.nat_abs_of_nonneg (trans_rel_right _ rfl (rat.le_floor.mpr 
    (trans_rel_right rat.le (eq.symm (zero_div ε) ) ( (div_le_div_right hε).mpr (le_of_lt (sub_pos.mpr ( 
        (bounded_by_non_elements α b).mp hb a ha) ) ) ) ) ) ) ) (le_refl n) ) ), 
{
    intro h0,
    have h1 : rat.mk (n - int.of_nat (int.nat_abs n)) 1 = 0, from by calc
    rat.mk (n - int.of_nat (int.nat_abs n)) 1 = rat.mk (n - ↑(int.nat_abs n)) 1 : rfl
    ... = rat.mk (n - n) 1 : by rw int.nat_abs_of_nonneg (trans_rel_right _ rfl (rat.le_floor.mpr 
    (trans_rel_right rat.le (eq.symm (zero_div ε) ) ( (div_le_div_right hε).mpr (le_of_lt (sub_pos.mpr ( 
        (bounded_by_non_elements α b).mp hb a ha) ) ) ) ) ) )
    ... = rat.mk 0 1 : by rw sub_self n
    ... = 0 : rfl,
    rw ←h1,
    exact h0
},
{
    intro h0,
    exact h0
},
apply exists.elim s0,  
intros, 
apply exists.elim a_2,
intros,
exact ⟨a_1, a_3, a_4.left, a_4.right.left, by calc a_3 - a_1 < ε*(0+1) : a_4.right.right.right
... = ε*1 : by rw zero_add
... = ε : by rw mul_one⟩
end ) ) 
```
The code is very long unfortunately, but it's finally done.

#### [Kevin Buzzard (Nov 25 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148329938):
Oh wooah! You did the Dedekind Cuts question in Lean! Nice!

#### [Alexandru-Andrei Bosinta (Nov 25 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148331184):
It's far from done. But I thought you already knew I was working on it.

#### [Kevin Buzzard (Nov 25 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148333814):
Yeah I guess we talked about it on Thurs. I guess several people have done bits and bobs but that `suff_small_bound` is a pain!

#### [Mario Carneiro (Nov 26 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coe%20back/near/148351790):
Hm, this piqued my interest. Here's my attempt, including a missing library theorem in `algebra.archimedean`:
```lean
import data.rat algebra.archimedean

theorem exists_pos_nat_one_div_lt {α} [linear_ordered_field α] [archimedean α]
  {ε : α} (hε : ε > 0) : ∃ n : ℕ, 0 < n ∧ 1 / (n : α) < ε :=
let ⟨n, h⟩ := exists_nat_gt (1/ε) in
have 0 < (n:α), from lt_trans (one_div_pos_of_pos hε) h,
⟨n, nat.cast_pos.1 this, (div_lt_iff this).2 $ (div_lt_iff' hε).1 h⟩

lemma suff_small_bound (α : ℝ) (ε : ℚ) (hε : ε > 0) : ∃ (a b : ℚ), a ∈ α.carrier ∧ b ∉ α.carrier ∧ b - a < ε :=
begin
  rcases exists_pos_nat_one_div_lt hε with ⟨n, n0, hn⟩,
  have n0' : 0 < (n:ℚ) := nat.cast_pos.2 n0,
  have hi : ∃ (b : ℤ), ∀ (z : ℤ), (z / n : ℚ) ∈ α.carrier → z ≤ b,
  { cases α.nonrat with b hb,
    refine ⟨⌈b * n⌉, λ z hz, le_of_not_lt $ λ h, _⟩,
    have := (le_div_iff n0').2 (ceil_le.1 (le_of_lt h)),
    refine hb (α.down _ hz _ this) },
  have lo : ∃ (z : ℤ), (z / n : ℚ) ∈ α.carrier,
  { cases α.nonemp with a ha,
    exact ⟨⌊a * n⌋, α.down _ ha _ ((div_le_iff n0').2 (floor_le _))⟩ },
  haveI := classical.dec,
  rcases int.exists_greatest_of_bdd hi lo with ⟨z, hz₁, hz₂⟩,
  refine ⟨z / n, (z+1:ℤ) / n, hz₁,
    λ h, not_le_of_lt (lt_add_one z) (hz₂ (z+1) h), _⟩,
  rw [← sub_div, ← int.cast_sub], simpa using hn
end
```

