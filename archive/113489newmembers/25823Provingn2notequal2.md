---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/25823Provingn2notequal2.html
---

## Stream: [new members](index.html)
### Topic: [Proving n^2 not equal 2](25823Provingn2notequal2.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Yuhan Du (Aug 31 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133132228):
I am trying to prove the statement that $$n^2 \neq 2$$
```lean
import algebra.group_power
theorem what_i_need: ¬ (∃ n : ℤ , n ^ 2 = 2 ) := sorry
```
Could someone possibly help me?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 31 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133132637):
Yesterday there was some chat about proving integer squares were 0 or 1 or 4 mod 8. It just occurs to me that an analogous approach mod 4 would do this (or mod 3)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 31 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133132650):
https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/0.3C.3Dd.3C3.20implies.20d.3D0.2C1.2C2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 31 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133132662):
have you looked at https://github.com/leanprover/mathlib/blob/master/data/nat/prime.lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 31 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133133995):
Well, this is quite a bit easier than proving that sqrt 2 is irrational

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 31 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133134009):
You can do it by cases on `n.nat_abs`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 31 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133134023):
too small when it is 0 or 1, too big when it is >= 2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 31 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133134030):
This is one method.
```lean
import data.zmod

example : ¬ ∃ n : ℤ, n ^ 2 = 2 :=
λ ⟨n, hn⟩, have h : ∀ n : zmod 3, n ^ 2 ≠ (2 : ℤ), from dec_trivial,
by have := h n; rw ← hn at this; simpa
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 31 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133134087):
The congruence trick is somehow better -- if a positive integer is not a square then it's not a square mod p for infinitely many p, and so you can just work in zmod p for the smallest such p :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 31 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133134103):
It's also not very easy to come up with.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 31 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133134107):
Even easier, you can square the square root and see if it matches

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 31 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133134115):
that should make it an easy dec_trivial proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 31 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133134185):
Oh that's a good idea -- prove that n is a square iff (sqrt n)^2=n

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 31 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133134869):
Not quite sure why this doesn't work
```lean

instance h (m : ℤ) : decidable (∃ n : ℤ, n ^ 2 = m) :=
decidable_of_iff (0 ≤ m ∧ m.nat_abs.sqrt ^ 2 = m.nat_abs) 
⟨λ h, ⟨nat.sqrt m.nat_abs, by rw [← int.coe_nat_pow, h.2, int.nat_abs_of_nonneg h.1]⟩,
 λ ⟨s, hs⟩, ⟨hs ▸ (pow_two_nonneg _), by rw [← hs, pow_two, int.nat_abs_mul, nat.sqrt_eq, nat.pow_two]⟩⟩

#eval (¬ ∃ n : ℤ, n ^ 2 = 2 : bool)

lemma two_not_square : ¬ ∃ n : ℤ, n ^ 2 = 2 := dec_trivial

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 31 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133134933):
`nat.sqrt` is defined through well founded recursion, which may cause a problem on all but the simplest problems. A similar issue came up with `nat.prime`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 31 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133134946):
I assume the `#eval` worked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 31 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133134958):
The eval did work. So the issue is that it's just too slow?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 31 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133135006):
I think it won't reduce well founded proofs because it requires evaluating theorems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 31 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133135016):
you can probably get `#reduce` to do it but that's not so helpful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 31 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133135036):
We need another `norm_num` extension for this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 31 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133135213):
Why can I prove `example : nat.gcd 4 5 = 1 := rfl`? That uses well founded recursion I take it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 31 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133135479):
I think it is just a complexity problem. The `#reduce` times out for the sqrt example but not gcd

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 01 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133171042):
This thread is really depressing. Sometimes I feel like we are going somewhere (like when we make progress on topological groups or noetherian modules) but then some super elementary problem is raised and we abruptly come back to reality: trivial things are not trivial at all in Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 01 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133171440):
The proof that there's no integer whose square is 2 is "it doesn't work for small n, and big n are too big". Formalising this is a bore. Automating it is possible, but it hasn't been done yet. That's not depressing, it just means things need to be done. Chris made an attempt. In 1 year's time there might be 10 Chris's at Imperial (here's hoping).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ali Sever (Sep 01 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133175553):
I aspire to be a Chris one day

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 01 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133175779):
That would be great Ali :-) come along on Thursday evenings in Oct and help me deal with the inevitable pile of freshers!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 01 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133177505):
```lean
import data.nat.basic algebra.group_power

instance nat.decidable_bex_lt (n : nat) (P : Π k < n, Prop) :
  ∀ [H : ∀ n h, decidable (P n h)], decidable (∃ k h, P k h) :=
begin
  induction n with n IH; intro; resetI,
  { exact is_false (λ ⟨_, h, _⟩, nat.not_lt_zero _ h) },
  cases IH (λ k h, P k (nat.lt_succ_of_lt h)) with h,
  { by_cases p : P n (nat.lt_succ_self n),
    { exact is_true ⟨n, nat.lt_succ_self n, p⟩ },
    { apply is_false,
      intro hk,
      rcases hk with ⟨k, hk1, hk2⟩,
      cases nat.lt_succ_iff_lt_or_eq.1 hk1 with hk hk,
      { exact h ⟨k, hk, hk2⟩ },
      { subst hk, exact p hk2 } } },
  apply is_true,
  rcases h with ⟨k, hk1, hk2⟩,
  exact ⟨k, nat.lt_succ_of_lt hk1, hk2⟩
end

instance nat.decidable_bex_le (n : nat) (P : Π k ≤ n, Prop)
  [Π n h, decidable (P n h)] : decidable (∃ k h, P k h) :=
decidable_of_iff (∃ k < n + 1, P k (nat.le_of_lt_succ H))
⟨λ ⟨k, h1, h2⟩, ⟨k, nat.le_of_lt_succ h1, h2⟩,
λ ⟨k, h1, h2⟩, ⟨k, nat.lt_succ_of_le h1, h2⟩⟩

instance decidable_mul_self_nat (n : ℕ) : decidable (∃ k, k * k = n) :=
decidable_of_iff (∃ k ≤ n, k * k = n)
⟨λ ⟨k, h1, h2⟩, ⟨k, h2⟩, λ ⟨k, h1⟩, ⟨k, h1 ▸ nat.le_mul_self k, h1⟩⟩

instance decidable_sqr_nat (n : ℕ) : decidable (∃ k, k^2 = n) :=
decidable_of_iff (∃ k, k * k = n)
⟨λ ⟨k, h⟩, ⟨k, by rwa [nat.pow_two]⟩, λ ⟨k, h⟩, ⟨k, by rwa [nat.pow_two] at h⟩⟩

instance decidable_mul_self_int : Π (n : ℤ), decidable (∃ k, k * k = n)
| (int.of_nat n) := decidable_of_iff (∃ k, k * k = n)
    ⟨λ ⟨k, hk⟩, ⟨k, by rw [← int.coe_nat_mul, hk]; refl⟩,
    λ ⟨k, hk⟩, ⟨int.nat_abs k, by rw [← int.nat_abs_mul, hk]; refl⟩⟩
| -[1+ n] := is_false $ λ ⟨k, h1⟩, not_lt_of_ge (mul_self_nonneg k) $
    h1.symm ▸ int.neg_succ_of_nat_lt_zero n

instance decidable_sqr_int (n : ℤ) : decidable (∃ k, k^2 = n) :=
decidable_of_iff (∃ k, k * k = n)
⟨λ ⟨k, h⟩, ⟨k, by rwa [pow_two]⟩, λ ⟨k, h⟩, ⟨k, by rwa [pow_two] at h⟩⟩

theorem what_i_need: ¬ (∃ n : ℤ , n ^ 2 = 2 ) := dec_trivial
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 01 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133177509):
btw the first part of my code is from [this discussion](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/bounded.20exists.20decidable/near/125567139) four months ago

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 01 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133177515):
(and mathlib still doesn't know it's true :P)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 01 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133177567):
```quote
This thread is really depressing. Sometimes I feel like we are going somewhere (like when we make progress on topological groups or noetherian modules) but then some super elementary problem is raised and we abruptly come back to reality: trivial things are not trivial at all in Lean.
```
@**Patrick Massot** Well this is just a puzzle that cannot be generalized to more useful maths...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 01 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133177980):
Yes, of course this is the other option - to check n is a square, just look at all the squares and see if n is in the list. It is much slower than squaring the square root, but it works better in small cases in the kernel since there are no wf definitions involved

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 01 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133178989):
Kenny, why don't you PR the general stuff above? That could be useful in lots of small annoying situations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 01 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133178993):
Following Patrick Massot's suggestion to look at `data.nat.prime`, I started trying to prove it using `nat.not_prime_mul`but I got stuck.
```lean
import algebra.group_power data.nat.prime

theorem what_i_need: ¬ (∃ n : ℤ , n ^ 2 = 2 ) := 
have p2: nat.prime 2, from nat.prime_two,
begin
unfold pow, unfold monoid.pow,
intro h,
exact exists.elim h (assume n, 
begin
clear h,
rw [mul_one],
assume h1,
_
--have pnn : nat.prime (n*n), by sorry,
--exact false.elim ((nat.not_prime_mul (sorry) (sorry)) h1)
end
)
end
```
I think the main thing I'm missing how to do is showing that proving it for $$1<n \in \mathbb{N}$$ suffices to show it for all $$n\in\mathbb{Z}$$.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 01 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133179095):
In this direction, I suggest proving `¬ nat.prime (n*n)`. It has no assumptions, but you have to special case 0 and 1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 01 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133179096):
yes, this is what I had in mind

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 01 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133179135):
I hoped that proving that from prime.lean wouldn't be too hard

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 01 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133179143):
I thought it was a theorem already but I could be mistaken

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 01 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133179146):
there is `not_prime_mul` which takes care of the large n case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 01 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133179308):
Even without trying to go to the heart of the matter, natural number hell strikes:
```lean
import algebra.group_power data.nat.prime

lemma aux (n : ℕ) : ¬ nat.prime (n*n) :=
sorry

theorem what_i_need: ¬ (∃ n : ℕ , n ^ 2 = 2 ) :=
begin
  rintro ⟨n, h⟩,
  apply aux n,
  rw ←pow_two,
  rw h,
  exact nat.prime_two,
end
```
The `rw h` doesn't work. `simp [h]` does work, but these kind of things is really the worse of Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 01 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133179314):
And I'm not even talking about trying to deduce the result with integers instead of natural numbers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 01 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133179481):
you have to use `rw ← nat.pow_two`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 01 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133179740):
I'm sure there is a solution, but having to know all that is really painful

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 01 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133179820):
most of this "ambient knowledge" is encoded in the simp lemmas, which is why `simp [h]` worked. If you look at the rewrites used you will see normalization of the group_power instance on nat to `nat.pow`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 01 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133179863):
the problem is that `nat` has two power notations, one elementary from `nat.pow` and another from the group power instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 01 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133179866):
`nat.pow` is the canonical one, at least until it is removed (it's in core)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 01 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133180082):
@**Bryan Gin-ge Chen** 
```lean
import algebra.group_power data.nat.prime

open nat

lemma aux (n : ℕ) : ¬ nat.prime (n*n) :=
begin
  intro h,
  cases n,
  { simpa [not_prime_zero] using h },
  { cases n,
    { simpa [not_prime_one] using h },
    { have : succ (succ n) > 1 := dec_trivial,
      exact not_prime_mul this this h } }
end

theorem what_i_need: ¬ (∃ n : ℕ , n ^ 2 = 2 ) :=
begin
  rintro ⟨n, h⟩,
  apply aux n,
  rw [←nat.pow_two, h],
  exact nat.prime_two,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 01 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133180087):
This is still cheating because there is nothing about negative integers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 04 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133288582):
A few days late and not very pretty, but I managed to complete your proof @**Patrick Massot** 
```lean
import algebra.group_power data.nat.prime

open nat

lemma aux (n : ℕ) : ¬ prime (n*n) :=
begin
  intro h,
  cases n,
  { simpa [not_prime_zero] using h },
  { cases n,
    { simpa [not_prime_one] using h },
    { have : succ (succ n) > 1 := dec_trivial,
      exact not_prime_mul this this h } }
end

theorem what_i_need_N: ¬ (∃ n : ℕ , n ^ 2 = 2 ) :=
begin
  rintro ⟨n, h⟩,
  apply aux n,
  rw [←nat.pow_two, h],
  exact prime_two,
end

open int

lemma sq_eq_nat_abs_sq {n : ℤ} {m : ℕ} : n^2 = (nat_abs n^2) := 
by rw [_root_.pow_two, _root_.pow_two, 
← int.coe_nat_mul, nat_abs_mul_self]

lemma nat_sq_of_int_sq {n : ℤ} {m : ℕ} : n^2 = m → (∃ nn : ℕ, nn ^ 2 = m) :=
begin
  intro h,
  existsi (nat_abs n),
    apply int.coe_nat_inj,
    rw [nat.pow_two, int.coe_nat_mul, ← _root_.pow_two, 
    ← sq_eq_nat_abs_sq],
  exact h,
  exact m
end

theorem what_i_need : ¬ (∃ n : ℤ, n^2 = 2) :=
begin
  rintro ⟨n,h⟩,
  exact false.elim (what_i_need_N (nat_sq_of_int_sq h))
end
```
I think I learned a few things along the way, though it still feels like I've got a long way to go before I can do anything useful...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 04 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20n%5E2%20not%20equal%202/near/133295018):
of course anyone reading this thread and seeing several very long proofs that 2 isn't a square might argue that we all have a long way to go before we can do anything useful...

