---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/13714howtousethepowaddtheorem.html
---

## [maths](index.html)
### [how to use the pow_add theorem](13714howtousethepowaddtheorem.html)

#### [Truong Nguyen (Sep 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133225323):
Dear Alls,
The pow_add theorem is as follow:

#check pow_add
pow_add : ∀ (a : ?M_1) (m n : ℕ), a ^ (m + n) = a ^ m * a ^ n

By why can't I prove the consequence theorem: 

theorem th01 (a: ℕ ): ∀ m n:ℕ, a ^ (m + n) = (a ^ m) * (a ^ n) :=
begin
rw pow_add (a:ℕ)
end

Here is the error that I got:

rewrite tactic failed, did not find instance of the pattern in the target expression
  a ^ (?m_1 + ?m_2)
Thank you,

#### [Kenny Lau (Sep 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133225393):
(deleted)

#### [Chris Hughes (Sep 02 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133225436):
It's because you need to use `nat.pow_add`

#### [Kenny Lau (Sep 02 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133225444):
because the `^` are different

#### [Mario Carneiro (Sep 02 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133225445):
`nat` has a different instance for the power function, so it has its own theorems to go with it, like `nat.pow_add`

#### [Chris Hughes (Sep 02 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133225446):
This is a very annoying feature of current lean. There are two definitions of `pow` on the naturals.

#### [Mario Carneiro (Sep 02 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133225489):
If `nat.pow_add` was not proven, you could also use `by simpa using pow_add a` to prove it

#### [Truong Nguyen (Sep 02 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133225601):
Dear Mario,
can you be more specific, what is  `by simpa using pow_add a`.

#### [Truong Nguyen (Sep 02 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133225696):
I changed to this:

theorem th01 (a: ℕ ): ∀ m n:ℕ, a ^ (m + n) = (a ^ m) * (a ^ n) :=
begin
rw [nat.pow_add (a:ℕ )]
end

But, it did not work neither.

#### [Mario Carneiro (Sep 02 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133225757):
```lean
import algebra.group_power

theorem th01 (a m n : ℕ) : a ^ (m + n) = (a ^ m) * (a ^ n) :=
by simpa using pow_add a m n
```

#### [Mario Carneiro (Sep 02 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133225765):
```lean
theorem th01 (a m n : ℕ) : a ^ (m + n) = (a ^ m) * (a ^ n) :=
by rw nat.pow_add
```

#### [Mario Carneiro (Sep 02 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133225767):
```lean
theorem th01 (a m n : ℕ) : a ^ (m + n) = (a ^ m) * (a ^ n) :=
nat.pow_add _ _ _
```

#### [Mario Carneiro (Sep 02 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133225813):
note that you need to have all the variables left of the colon for `rw` to work here

#### [Truong Nguyen (Sep 02 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133226550):
Oh, great
Do you know how can I find the tutorial of using "simpa".

I have the following issue as well. I think it can be done in similar way.

How to use the theorem:
#check cardinal.mul_power 
cardinal.mul_power : (?M_1 * ?M_2) ^ ?M_3 = ?M_1 ^ ?M_3 * ?M_2 ^ ?M_3

To prove that:
theorem th07 (a b n: \N): (a * b)^n = a ^n*b^n.

#### [Mario Carneiro (Sep 02 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133226706):
That is an unrelated use of power; although it is possible it would be a weird way to prove that theorem for natural numbers

#### [Mario Carneiro (Sep 02 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133226715):
the theorem itself is `nat.mul_pow`

#### [Truong Nguyen (Sep 02 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133226815):
when I run the command:
#check nat.mul_pow

it gave me nothing.

#### [Patrick Massot (Sep 02 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133227003):
you need to import https://github.com/leanprover/mathlib/blob/dd0c0aeefcaf6a438ab4273d7a1f42e1b8225847/data/nat/basic.lean

#### [Patrick Massot (Sep 02 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133227007):
`import data.nat.basic`

#### [Truong Nguyen (Sep 03 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133268897):
Hello,
do you know where can I find the tutorial of using "simpa".

#### [Patrick Massot (Sep 03 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133268911):
I think we don't have anything better than https://github.com/leanprover/mathlib/blob/master/docs/tactics.md#simpa

#### [Truong Nguyen (Sep 03 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how to use the pow_add theorem/near/133270921):
Oh, thank you

