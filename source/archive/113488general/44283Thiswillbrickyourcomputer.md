---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/44283Thiswillbrickyourcomputer.html
---

## [general](index.html)
### [This will brick your computer!](44283Thiswillbrickyourcomputer.html)

#### [Kenny Lau (Sep 14 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/133943778):
```lean
import data.int.basic
set_option trace.class_instances true
#check λ n : ℤ, (n : ℕ)
```

#### [Kevin Buzzard (Sep 14 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/133945380):
This is well known. Lean will time out trying to coerce an int into a nat rather than give up

#### [Kenny Lau (Sep 14 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/133945390):
remove the first line and it's fine!

#### [Kevin Buzzard (Sep 14 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/133945432):
Hopefully fixed in Lean 4

#### [Kenny Lau (Sep 17 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134082892):
```lean
import data.polynomial

universe u

variables {α : Type u} [comm_semiring α] [decidable_eq α]

def derivative (p : polynomial α) : polynomial α :=
finsupp.sum p $ λ n c, n * polynomial.C c * polynomial.X^(n-1)

@[simp] lemma derivative_C_mul_X (x : α) (n : ℕ) :
  derivative (polynomial.C x * polynomial.X^n) = n * polynomial.C x * polynomial.X^(n-1) :=
begin
  unfold derivative,
  rw [← polynomial.single_eq_C_mul_X, finsupp.sum_single_index],
  all_goals { rw [polynomial.C_0, mul_zero, zero_mul] }
end

--timeout
@[simp] lemma derivative_C (x : α) :
  derivative (polynomial.C x) = 0 :=
derivative_C_mul_X x 0
```

#### [Mario Carneiro (Sep 17 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134082945):
there are some nontrivial defeq simplifications there

#### [Mario Carneiro (Sep 17 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134082985):
at least try `by simpa using derivative_C_mul_X x 0` first

#### [Kenny Lau (Sep 17 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083001):
it's intentionally incorrect

#### [Mario Carneiro (Sep 17 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083004):
then what's the surprise?

#### [Kenny Lau (Sep 17 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083005):
well Lean should tell me instead of time out

#### [Mario Carneiro (Sep 17 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083008):
you just asked it to reduce some big expression to 0

#### [Mario Carneiro (Sep 17 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083048):
it's got to unfold a bunch of definitions and run the power function, etc

#### [Mario Carneiro (Sep 17 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083051):
it's not obviously not defeq

#### [Kenny Lau (Sep 17 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083053):
I don't actually know if it's defeq

#### [Mario Carneiro (Sep 17 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083056):
neither does lean...

#### [Kenny Lau (Sep 17 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083268):
oh wow it's already done

#### [Kenny Lau (Sep 17 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/This%20will%20brick%20your%20computer%21/near/134083271):
i'm lucky i realized so soon

