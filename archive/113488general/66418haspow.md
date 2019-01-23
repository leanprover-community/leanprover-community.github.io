---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66418haspow.html
---

## Stream: [general](index.html)
### Topic: [has_pow](66418haspow.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 31 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_pow/near/124446352):
what's the impact of the new has_pow typeclass being an out_param?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 31 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_pow/near/124446978):
I'm not sure about this change. Sebastian suggested it and it was merged before we had much discussion about it, but I don't know if it's reasonable. `mathlib` already had and discarded an earlier typeclass proposal. In particular, the reals are going to have at least three power operations on them, and it's not clear to me how to disambiguate the typeclass search

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 31 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_pow/near/124449165):
@**Mario Carneiro** Would that be `monoid_pow`/`group_pow`/`real_pow` (or whatever class that last one is defined on)? Since each one is strictly more general in its out_param type than the ones before it, would it make sense to give them increasing instance priorities?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_pow/near/124509461):
@**Sebastian Ullrich**  I've started working on fixing mathlib after the has_pow change. Here's an example of a problem that arises:
```
variables {α : Type*} [group α]
def gpow : α → ℤ → α := sorry
instance group.has_pow : has_pow α ℤ := ⟨gpow⟩

example (a : α) : a ^ 0 = 1 := sorry -- failed to synth ⊢ has_pow α ℕ
example (a : α) : a ^ (0:ℕ) = 1 := sorry -- ok, coerces
example (a : α) : a ^ (0:ℤ) = 1 := sorry -- ok
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_pow/near/124509510):
Do out_params not propagate type information to the arguments for the purpose of avoiding the nat default for number literals?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 02 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_pow/near/124520043):
Okay, this update isn't going to happen today, I need to sleep. The change is generally making me put in more type ascriptions than before, but it wasn't disambiguating anything before so maybe that's reasonable. It's not going to be fun explaining why this happens though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 02 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_pow/near/124520306):
@**Mario Carneiro** Hmm, this is certainly unexpected

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 02 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_pow/near/124546919):
@**Mario Carneiro** Okay, it's unfortunate scheduling between the class inference and the coercion, which I don't think is a perfectly solvable problem in general. I don't know if we can do a better job for this common case, hmm.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 02 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_pow/near/124547413):
Would you suggest to just remove the out_param (for now)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 03 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_pow/near/124550421):
My gut says that will perform better on the whole. We will have to give the type of things in that slot if they aren't derivable normally, but this will give more freedom to have multiple possibly incompatible power functions which are selected by type. I'll finish updating mathlib wrt the current version, and then if you change it to remove the out_param and I fix mathlib again we will have a basis for comparison.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 03 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_pow/near/124567281):
Okay, I'll remove it

