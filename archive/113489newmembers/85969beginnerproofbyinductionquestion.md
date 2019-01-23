---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/85969beginnerproofbyinductionquestion.html
---

## Stream: [new members](index.html)
### Topic: [beginner proof by induction question](85969beginnerproofbyinductionquestion.html)

---

#### [Bryan Gin-ge Chen (Aug 30 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133037403):
I'm trying to prove that $$ \sum_{k=0}^{n-1}F_k = F_{2k-1} $$, where $$F_{k}$$ is the kth Fibonacci number. Here's my attempt so far:
```lean
import algebra.big_operators

def fibonacci : ℕ → ℕ
| 0 := 0
| 1 := 1
| (n+2) := fibonacci n + fibonacci (n+1)

def fib_even_sum : ℕ → ℕ := λ n, (finset.range n).sum (λ m, fibonacci (2*m))

theorem sum_even_fib_eq_fib_double_sub_one: ∀ (n : ℕ),
fib_even_sum n = fibonacci (2*n - 1)
| 0 := rfl
| (nat.succ n) := 
have f1 : (finset.range n).sum (λ m, fibonacci (2*m)) = fib_even_sum n, by refl,
begin
unfold fib_even_sum,
rw [finset.sum_range_succ, f1, sum_even_fib_eq_fib_double_sub_one, 
add_comm, nat.succ_eq_add_one, mul_add],
sorry
end
```
As you can see, my goal looks like this:
```lean
⊢ fibonacci (2 * n - 1) + fibonacci (2 * n) = fibonacci (2 * n + 2 * 1 - 1)
```
But I can't figure out how to simplify `2*n + 2*1 -1` inside `fibonacci` to `2*n - 1`. If I could do that then I would happily finish with `refl`.

Other style or efficiency suggestions would also be appreciated. Is there a smart way to apply `simp`? I haven't managed that either.

#### [Kenny Lau (Aug 30 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133040385):
what you wrote at the beginning of this message is false

#### [Kenny Lau (Aug 30 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133040681):
also what you stated in your lean code is false

#### [Kenny Lau (Aug 30 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133040726):
```lean
import algebra.big_operators

def fibonacci : ℕ → ℕ
| 0 := 0
| 1 := 1
| (n+2) := fibonacci n + fibonacci (n+1)

def fib_even_sum : ℕ → ℕ := λ n, (finset.range n).sum (λ m, fibonacci (2*m))

theorem not_sum_even_fib_eq_fib_double_sub_one: ¬∀ (n : ℕ),
fib_even_sum n = fibonacci (2*n - 1) :=
λ H, absurd (H 1) dec_trivial
```

#### [Kenny Lau (Aug 30 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133042012):
```lean
import algebra.big_operators

def fibonacci : ℕ → ℕ
| 0 := 0
| 1 := 1
| (n+2) := fibonacci n + fibonacci (n+1)

def fib_even_sum : ℕ → ℕ := λ n, (finset.range n).sum (λ m, fibonacci (2*m))

theorem sum_even_fib_eq_fib_double_sub_three (n : ℕ) :
  fib_even_sum n = fibonacci (2*n - 1) - 1 :=
begin
  cases n with n, {refl},
  change _ = fibonacci (2 * n + 2 - 1) - 1,
  rw [nat.add_sub_assoc],
  change _ = fibonacci (2 * n + 1) - 1,
  unfold fib_even_sum,
  rw [finset.sum_range_succ],
  induction n with n ih, {refl},
  rw [finset.sum_range_succ, ih, add_comm],
  change fibonacci (2*n+1) - 1 + fibonacci (2*n+2) = fibonacci (2*n+3) - 1,
  rw [← nat.sub_add_comm], refl,
  { clear ih,
    induction n with n ih, {refl},
    change 1 ≤ fibonacci (2*n+3),
    unfold fibonacci,
    transitivity, {exact ih},
    apply nat.le_add_right },
  from dec_trivial
end
```

#### [Kevin Buzzard (Aug 30 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133053991):
Note that your goal about `fibonacci (2 * n - 1) + fibonacci (2 * n) = fibonacci (2 * n + 2* 1 - 1)` is false if `n = 0`, because `0 - 1 = 0`.

#### [Bryan Gin-ge Chen (Aug 30 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133056271):
Ah, thanks! That was  really silly of me... I got lazy because I had previously proved this:
```lean
def odd : ℕ → ℕ := λ n, 2*n+1

def fib_odd_sum : ℕ → ℕ := λ n, (finset.range n).sum (λ m, fibonacci (odd m))

theorem sum_odd_fib_eq_fib_double : ∀ (n : ℕ), 
fib_odd_sum n = fibonacci (2*n) 
| 0 := rfl
| (nat.succ n) := 
have f1 : (finset.range n).sum (λ m, fibonacci (odd m)) = fib_odd_sum n, by refl,
begin
unfold fib_odd_sum, 
rw [finset.sum_range_succ, f1, sum_odd_fib_eq_fib_double, add_comm],
refl
end
```
and I just wanted to copy and paste stuff. Granted, I should still have checked what I was trying to prove...

#### [Patrick Massot (Aug 30 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133056881):
We will soon have tools to avoid such kind of mistakes

#### [Kevin Buzzard (Aug 30 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133057027):
You mean Kenny?

#### [Patrick Massot (Aug 30 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133057171):
I mean the tactic [sanity_check](https://github.com/robertylewis/mathematica_examples/blob/master/src/sanity_check.lean) that Rob showed in Orsay, Simon's [SlimCheck](https://github.com/cipher1024/slim_check), and [Nunchaku](https://arxiv.org/abs/1606.05945) in Lean

#### [Johannes Hölzl (Aug 30 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133058279):
You find Pablo's Nunchaku-Lean prototype in https://gitlab.binets.fr/pablo.le-henaff/nunchaku-lean

#### [Johannes Hölzl (Aug 30 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133058343):
it doesn't yet implement the dependent type as proposed by the arxiv paper, but hopefully in the future it does

#### [Patrick Massot (Aug 30 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133058502):
is there any documentation explaining how to use it?

#### [Johannes Hölzl (Aug 30 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133059392):
Not yet. It is only a prototype. Currently, it doesn't even have a `leanpkg.toml`.
What should work is:
```lean
import nunchaku

example (n : nat) : n > 1  := by nunchaku
```
and it should report n = 0 as counterexample.

#### [Patrick Massot (Aug 30 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133064702):
Thanks. I guess I'll need to see more documentation (including how to install all the dependencies)

#### [Bryan Gin-ge Chen (Aug 30 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133069870):
Returning to my original problem, here's my fixed up proof:
```lean
import algebra.big_operators

def fibonacci : ℕ → ℕ
| 0 := 0
| 1 := 1
| (n+2) := fibonacci n + fibonacci (n+1)

def fib_even_sum : ℕ → ℕ := λ n, (finset.range n).sum (λ m, fibonacci (2*m))

lemma succ_gt_zero (n : ℕ): nat.succ n > 0 := dec_trivial

theorem sum_even_fib_eq_fib_double_sub_one: ∀ (n : ℕ),
n>0 → fib_even_sum n + 1 = fibonacci (2*n - 1)
| 0 := begin
intro h,
exact false.elim ((gt_irrefl 0) h)
end
| 1 := begin
intro h,
refl
end
| (nat.succ (n+1)) := 
have f1 : (finset.range (n+1)).sum (λ m, fibonacci (2*m)) = fib_even_sum (n+1), by refl,
have f2 : fib_even_sum (n+1) + 1 = fibonacci (2*(n+1) - 1), by exact sum_even_fib_eq_fib_double_sub_one (n+1) (succ_gt_zero n),
begin
intro h,
unfold fib_even_sum,
rw [finset.sum_range_succ, f1, add_assoc, add_comm, f2, add_comm, nat.succ_eq_add_one, mul_add, add_comm],
change fibonacci (2 * n + 1) + fibonacci (2 * n + 2) = fibonacci (2 * n + 3),
refl
end
```

#### [Bryan Gin-ge Chen (Aug 30 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133069890):
Thanks to Kenny for his proof as well, which was very instructive.

#### [Bryan Gin-ge Chen (Sep 04 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333244):
If anyone has a strong stomach, I'd appreciate feedback on this ugly proof of yet another silly Fibonacci fact (this time, $$F_{n+1}^2-F_nF_{n+2}=(-1)^n $$):
```lean
import algebra.big_operators algebra.group_power

def F : ℕ → ℕ
| 0 := 0
| 1 := 1
| (n+2) := F n + F (n+1)

variables (a b c d e:ℤ)
lemma abcde : a*b + c*d - (e + d*c) = (-1)*(e - b*a) :=
begin
  rw [add_comm, sub_eq_add_neg, neg_add,
  ←add_assoc, add_comm, mul_comm,
  ←add_assoc, ←add_assoc, neg_add_self, zero_add],
  simp [mul_comm]
end

open nat

variable n : ℕ
local notation [parsing_only] `F_n` := ↑(F n)
local notation [parsing_only] `F_n1` := ↑(F (succ n))
local notation [parsing_only] `F_n2` := ↑(F (succ n+1))

theorem ex10 : ((F (n+1) ^ 2):ℤ) - (F n) * (F (n+2)) = (-1) ^ n :=
begin
  induction n with n ih, {refl},
  unfold pow monoid.pow,
  unfold pow monoid.pow at ih,
  rw [←ih, mul_one, mul_one],
  change ↑((F (succ n + 1)) * (F n + F (succ n)))
    - (F_n1 * (F_n1 + F_n2))
    = (-1:ℤ) * (F_n1 * F_n1 - F_n * F_n2),
  rw [mul_add, mul_add, int.coe_nat_add],
  change F_n2 * F_n + F_n2 * F_n1
    -(F_n1 * F_n1 + F_n1 * F_n2)
    = (-1:ℤ) * (F_n1 * F_n1 - F_n * F_n2),
  rw [abcde]
end
```
Is there a better tactic to use for proving `abcde` (or better, getting around it entirely)? Constructing these long sequences of `rw`s is very tiresome but I don't have a good idea of when I can throw in `simp`.

#### [Patrick Massot (Sep 04 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333346):
abcde is `by ring`

#### [Patrick Massot (Sep 04 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333369):
don't forget `import tactic.ring` at top

#### [Chris Hughes (Sep 04 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333488):
```lean
theorem ex10 : ((F (n+1) ^ 2):ℤ) - (F n) * (F (n+2)) = (-1) ^ n :=
begin
  induction n with n ih, 
  { refl },
  { simp [F, _root_.pow_succ, ih.symm],
    ring },
end
```

#### [Bryan Gin-ge Chen (Sep 04 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333501):
Ah, right. I could have sworn I tried that..

Indeed, I can just delete `abcde` entirely and finish with `ring`.

#### [Bryan Gin-ge Chen (Sep 04 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333626):
@**Chris Hughes** that's not working for me, unfortunately...

#### [Patrick Massot (Sep 04 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333634):
works here

#### [Chris Hughes (Sep 04 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333646):
Did you import `tactic.ring`?

#### [Patrick Massot (Sep 04 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333708):
Chris, can you also golf my limit computation?

#### [Chris Hughes (Sep 04 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333726):
Probably not. I know nothing about analysis in lean.

#### [Bryan Gin-ge Chen (Sep 04 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133333816):
OK, it works now. I had some other notation in my main file that was interfering somehow.

#### [Bryan Gin-ge Chen (Sep 04 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133334372):
@**Chris Hughes** If you don't mind, could you explain your thought process when you came up with that? For instance, did you peek at my ugly proof first, or did those lemmas immediately jump into your head.

Is the take-away that `simp`, then `ring`should be my go-to for this sort of thing?

#### [Mario Carneiro (Sep 04 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133334439):
`ring` does equalities between ring expressions, i.e. addition, subtraction, multiplication and powers by constants

#### [Chris Hughes (Sep 04 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133334506):
I used your proof a little bit, to see that I needed induction. Other than that, it's just unfold everything, find some way of substituting in the induction hypothesis, and then hope `ring` works.

#### [Bryan Gin-ge Chen (Sep 04 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/beginner%20proof%20by%20induction%20question/near/133334537):
Thanks, that's very helpful!

