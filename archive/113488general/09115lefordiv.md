---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09115lefordiv.html
---

## [general](index.html)
### [le for div?](09115lefordiv.html)

#### [Nicholas Scheel (Apr 04 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124631308):
This seems like a silly question but I've scoured mathlib and init for this lemma and I can't find it: `∀ {n m : ℕ} (h : n ≤ m) {k}, n/k ≤ m/k`
I don't think it can be derived from `div_le_of_le_mul` since `k*(n/k) = n` does not necessarily hold (only if `k | n`)
a version for multiplication would be nice too
does this exist? is there a nice way to prove it?

#### [Simon Hudon (Apr 04 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124631526):
I think `le_div_iff_mul_le`with `div_mul_le_self` should allow you to prove that

#### [Chris Hughes (Apr 04 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124632258):
It doesn't. Applying `le_div_of_mul_le` gives you something false to prove, if say `n=4`, `m=5`, `k=3`

#### [Simon Hudon (Apr 04 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124632310):
Don't use `le_div_of_mul_le`; use `le_div_iff_mul_le` instead

#### [Chris Hughes (Apr 04 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124632336):
Sorry, I was talking about a  `div_le` not `le_div`

#### [Nicholas Scheel (Apr 04 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124632408):
Thanks for the tip! :bow: I think I got it working now:
```
lemma nat.le_mul {n m : ℕ} (h : n ≤ m) {k} : n*k ≤ m*k
:= begin
  cases k with k, rw [nat.mul_zero, nat.mul_zero],
  apply (nat.le_div_iff_mul_le n (m*nat.succ k) (nat.zero_lt_succ k)).1,
  rw [nat.mul_div_left],
  exact h,
  apply nat.zero_lt_succ,
end

lemma nat.le_div {n m : ℕ} (h : n ≤ m) {k} : n/k ≤ m/k
:= begin
  cases k with k, rw [nat.div_zero, nat.div_zero],
  apply (nat.le_div_iff_mul_le (n/nat.succ k) (m) (nat.zero_lt_succ k)).2,
  transitivity,
  apply nat.div_mul_le_self,
  exact h,
end
```

#### [Simon Hudon (Apr 04 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124632672):
A a matter of style, you may prefer `cases lt_or_eq_of_le (zero_le k) with hk hk` instead of `cases k with k`

#### [Matt Wilson (Apr 04 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124632693):
peanut gallery question, but how long does that take to run

#### [Simon Hudon (Apr 04 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124632760):
About 51ms on my system

#### [Simon Hudon (Apr 04 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124632821):
Sorry, wrong proof. @**Nicholas Scheel** 's proof takes 6ms

#### [Simon Hudon (Apr 04 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124637611):
@**Nicholas Scheel** Feel free to send a pull request of that theorem to mathlib. You should call it `nat.div_le_div`.

#### [Kevin Buzzard (Apr 05 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124645163):
` nat.mul_le_mul_right : ∀ {n m : ℕ} (k : ℕ), n ≤ m → n * k ≤ m * k ` is already there

#### [Kevin Buzzard (Apr 05 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124645166):
but I haven't seen the div version before

#### [Mario Carneiro (Apr 05 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124650222):
I'm also surprised to find this is missing. I will add it to mathlib, by the name `nat.div_le_div_right`

#### [Nicholas Scheel (Apr 05 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124650281):
@**Mario Carneiro** @**Simon Hudon**  How about this? https://github.com/MonoidMusician/mathlib/pull/1 ;)

#### [Mario Carneiro (Apr 05 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124650329):
I'm also going to rewrite the proof, since it's a one-liner. I think Simon gave a hint earlier about this, see if you can shorten your proof

#### [Nicholas Scheel (Apr 05 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124650541):
hmm okay, I don’t know enough to see how to shorten it like that and I’ve run out of time tonight, feel free to pick it up if you want 🙂

#### [Mario Carneiro (Apr 05 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124650589):
oh, actually I forgot about the zero case. Anyway here's my attempt at shortening it:
```
protected theorem div_le_div {n m : ℕ} (h : n ≤ m) {k : ℕ} : n / k ≤ m / k :=
(nat.eq_zero_or_pos k).elim (λ k0, by simp [k0]) $ λ hk,
(nat.le_div_iff_mul_le _ _ hk).2 $ le_trans (nat.div_mul_le_self _ _) h
```

#### [Nicholas Scheel (Apr 05 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124650592):
(whoops didn’t realize that I PRed my own repo)

#### [Mario Carneiro (Apr 05 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le for div?/near/124650653):
looking at the differences, I guess I didn't do much besides compactify the same steps, more or less

