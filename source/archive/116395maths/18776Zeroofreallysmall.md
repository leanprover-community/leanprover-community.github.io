---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/18776Zeroofreallysmall.html
---

## [maths](index.html)
### [Zero of really small](18776Zeroofreallysmall.html)

#### [Patrick Massot (Jan 19 2019 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156453113):
Where do we find `lemma zero_of_abs_lt_all (x : ℝ) (h : ∀ ε, ε > 0 → |x| < ε) : x = 0`?

#### [Chris Hughes (Jan 19 2019 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156453250):
I think something like `eq_of_forall_abs_sub_lt` is in there.

#### [Patrick Massot (Jan 19 2019 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156453442):
https://github.com/leanprover/mathlib/search?q=eq_of_forall_abs_sub_lt&unscoped_q=eq_of_forall_abs_sub_lt :sad:

#### [Patrick Massot (Jan 19 2019 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156453462):
Do you have any idea where something like this could be?

#### [Patrick Massot (Jan 19 2019 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454123):
```lean
lemma zero_of_abs_lt_all (x : ℝ) (h : ∀ ε, ε > 0 → |x| < ε) : x = 0 :=
eq_zero_of_abs_eq_zero $ eq_of_le_of_forall_le_of_dense (abs_nonneg x) $ λ ε ε_pos, le_of_lt (h ε ε_pos)
```

#### [Patrick Massot (Jan 19 2019 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454138):
@**Mario Carneiro**  Should I PR that, or is it already in?

#### [Patrick Massot (Jan 19 2019 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454184):
with weaker assumptions of course

#### [Patrick Massot (Jan 19 2019 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454188):
(I mean replacing real numbers with something more general)

#### [Mario Carneiro (Jan 19 2019 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454377):
is this a theorem of normed groups or do you want a different abstraction

#### [Patrick Massot (Jan 19 2019 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454434):
I think normed groups is enough for me, but `eq_of_le_of_forall_le_of_dense` has more exotic type classes

#### [Patrick Massot (Jan 19 2019 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454452):
But I don't want you to think too hard about this when you could be hitting that merge button on https://github.com/leanprover/mathlib/pull/610

#### [Patrick Massot (Jan 19 2019 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454640):
```lean
lemma zero_of_norm_lt_all {G : Type*} [normed_group G] (x : G) (h : ∀ ε, ε > 0 → ∥x∥ < ε) : x = 0 :=
(norm_eq_zero _).1 $ eq_of_le_of_forall_le_of_dense (norm_nonneg x) $ λ ε ε_pos, le_of_lt (h ε ε_pos)

lemma zero_of_abs_lt_all (x : ℝ) (h : ∀ ε, ε > 0 → |x| < ε) : x = 0 :=
zero_of_norm_lt_all x h
```
does work

#### [Patrick Massot (Jan 19 2019 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Zero%20of%20really%20small/near/156454642):
of course we could also prove them the other way around

