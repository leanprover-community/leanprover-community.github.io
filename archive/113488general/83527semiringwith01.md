---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83527semiringwith01.html
---

## Stream: [general](index.html)
### Topic: [semiring with 0 ≠ 1](83527semiringwith01.html)

---


{% raw %}
#### [ Chris Hughes (May 12 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126453723):
Is there a type class for a semiring with `0 ≠ 1`?

#### [ Chris Hughes (May 12 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126453838):
I tried `[semiring α] [zero_ne_one_class α]` but then I ended up with two different definitions of one.

#### [ Kenny Lau (May 12 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126453884):
try to use old structure command and build a new class

#### [ Kenny Lau (May 12 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126453888):
the diamond death you just experienced

#### [ Johan Commelin (May 12 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126454045):
```quote
I tried `[semiring α] [zero_ne_one_class α]` but then I ended up with two different definitions of one.
```
Did you also end up with two different definitions of zero?

#### [ Chris Hughes (May 12 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126454136):
Yes.

#### [ Chris Hughes (May 12 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126454244):
Same question for `ring`.

#### [ Chris Hughes (May 12 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126454826):
Would it have been better to define `zero_ne_one_class` as 
```lean
class zero_ne_one_class (α : Type*) [has_zero α] [has_one α] : Prop :=
(zero_ne_one : 0 ≠ 1)
```

#### [ Mario Carneiro (May 12 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126454972):
Yes. There is not much I can do about it

#### [ Johan Commelin (May 12 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126454984):
Well, we can define our own `has_zero_ne_one`, right?

#### [ Johan Commelin (May 12 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126454986):
In the way that Chris suggested

#### [ Mario Carneiro (May 12 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455074):
Sure. I would ask the reason for the use though, it seems not so useful

#### [ Chris Hughes (May 12 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455083):
I'm doing univariate polys, and I'm trying to prove `degree_of (X : uv_polynomial α) = 1`

#### [ Mario Carneiro (May 12 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455142):
how is degree_of defined?

#### [ Mario Carneiro (May 12 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455145):
and X

#### [ Chris Hughes (May 12 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455188):
after unfolding it looks like this `sup ((single 1 1).support) id = 1`

#### [ Chris Hughes (May 12 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455190):
unfolding single makes it become this `sup (ite (1 = 0) ∅ (singleton 1)) id = 1`

#### [ Mario Carneiro (May 12 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455201):
is there decidable equality?

#### [ Mario Carneiro (May 12 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455202):
or are you classical

#### [ Chris Hughes (May 12 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455241):
Yes.

#### [ Chris Hughes (May 12 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455242):
there is decidable equality

#### [ Chris Hughes (May 12 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455340):
I could probably get around it by proving alternative lemmas like `degree_of_monomial`. Or just make `0 \ne 1` an argument to the theorem.

#### [ Mario Carneiro (May 12 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455572):
I used a typeclass `nonzero_ring` in my metamath formalization of this one. Perhaps `is_nonzero` can be a typeclass depending on `ring` instead of `has_zero` and `has_one`?

#### [ Mario Carneiro (May 12 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455622):
nonzero semiring seems like a bad idea though, it's not nearly as nice as it sounds since it is not cancellative

#### [ Kevin Buzzard (May 12 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126455825):
Chris, from a mathematical point of view I am not so sure that people care too much about semirings. However I know lean is different. All I'm saying is that if it's easier to work with rings than semirings then from the point of view of mathematical applications you'll be losing essentially nothing.

#### [ Chris Hughes (May 12 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126457579):
I have the same problem with rings.

#### [ Chris Hughes (May 12 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126458132):
```quote
I used a typeclass `nonzero_ring` in my metamath formalization of this one. Perhaps `is_nonzero` can be a typeclass depending on `ring` instead of `has_zero` and `has_one`?
```
Do you mean extending `ring` or with `ring` as an argument?

#### [ Mario Carneiro (May 12 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiring%20with%200%20%E2%89%A0%201/near/126460138):
`nonzero_ring` would `extends ring`, `is_nonzero : Prop` would have `[ring A]`


{% endraw %}
