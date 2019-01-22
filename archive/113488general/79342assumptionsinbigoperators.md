---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79342assumptionsinbigoperators.html
---

## [general](index.html)
### [assumptions in big_operators](79342assumptionsinbigoperators.html)

#### [Johan Commelin (Oct 02 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135034421):
I was browsing through big_operators and found:
```lean
#print finset.sum_nat_cast
-- gives
theorem finset.sum_nat_cast : ∀ {α : Type u} {β : Type v} [_inst_1 : comm_monoid β] [_inst_2 : add_comm_monoid β] [_inst_3 : has_one β]
(s : finset α) (f : α → ℕ), ↑(sum s f) = sum s (λ (a : α), ↑(f a)) :=
λ {α : Type u} {β : Type v} [_inst_1 : comm_monoid β] [_inst_2 : add_comm_monoid β] [_inst_3 : has_one β]
(s : finset α) (f : α → ℕ), eq.symm (sum_hom coe nat.cast_zero nat.cast_add)
```
Is this bad? I assume `[_inst_1 : comm_monoid β] [_inst_2 : add_comm_monoid β]` is not intended.

#### [Kevin Buzzard (Oct 02 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035071):
How does Lean know that the up-arrows mean "coerce to beta"?

#### [Johan Commelin (Oct 02 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035165):
I don't know. Probably `nat.cast`

#### [Chris Hughes (Oct 02 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035363):
Johan just posted the output of `#print`. In the actual theorem, the type is given explicitly

#### [Johan Commelin (Oct 02 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035637):
Sorry, I could have been clearer about that...

#### [Johan Commelin (Oct 02 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035695):
Is there a way to see if this happens more often in mathlib?

#### [Johan Commelin (Oct 02 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035707):
Chris, you can probably use your tools to figure out if this theorem is actually ever used.

#### [Johan Commelin (Oct 02 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035716):
I predict it isn't. Because otherwise this double instance problem would have been noticed before.

#### [Patrick Massot (Oct 02 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035754):
I'm not sure. As  I already pointed out, there are theorems with redundant instances in mathlib

#### [Kevin Buzzard (Oct 02 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135035756):
```quote
Johan just posted the output of `#print`. In the actual theorem, the type is given explicitly
```
Oh -- I'm an idiot. Thanks Chris.

#### [Johan Commelin (Oct 02 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135036066):
@**Patrick Massot** hmmm... can your tools help to discover this? Of course not very automatically. But maybe generate a list of all theorems that assume `[blah X]` and `[add_blah X]`. I guess it almost never happens that this is intended.

#### [Patrick Massot (Oct 02 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135036552):
doing this is in my long TODO list, but it's very low priority

#### [Chris Hughes (Oct 02 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/assumptions%20in%20big_operators/near/135036869):
Searching `sum_nat_cast` in VScode tells me it's used once in `probability mass function`. It's casting to $$\mathbb{R}$$ there, so no problems synthesizing the `comm_monoid` instance. It is a mistake though and should be changed.

