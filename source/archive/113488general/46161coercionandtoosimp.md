---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/46161coercionandtoosimp.html
---

## [general](index.html)
### [coercion and too simp](46161coercionandtoosimp.html)

#### [Sean Leather (Jun 07 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coercion%20and%20too%20simp/near/127703649):
I keep running into the problem of `simp` reducing something to `p = ff` when I really want `¬↥p`. I then end up doing a `rw` explicitly, which is a pain. Is there any way to work around this issue with `simp`?

#### [Kevin Buzzard (Jun 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coercion%20and%20too%20simp/near/127703860):
You can often do `suffices : <what you want>, simpa using this` or `...simp [this]` or similar. You want something neater than this though?

#### [Sean Leather (Jun 07 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coercion%20and%20too%20simp/near/127703975):
I was hoping for something like `simp [-<theorem>]`, disabling a particular rewrite but still using only `simp`. I'm not sure those other options are any better than the `rw` that I do now.

#### [Sean Leather (Jun 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coercion%20and%20too%20simp/near/127703996):
Or, even better, remove the `simp` attribute locally for my whole file. :simple_smile:

#### [Sean Leather (Jun 07 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coercion%20and%20too%20simp/near/127704359):
Ah, found it: `simp [-eq_ff_eq_not_eq_tt]`. I just had to look at the `simp` rules with `set_option trace.simplify.rewrite true`.

#### [Sean Leather (Jun 07 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coercion%20and%20too%20simp/near/127704372):
```lean
@[simp] lemma eq_ff_eq_not_eq_tt (b : bool) : (¬(b = tt)) = (b = ff)
```

#### [Sean Leather (Jun 07 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coercion%20and%20too%20simp/near/127704392):
Not the rule I expected.

#### [Sean Leather (Jun 07 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/coercion%20and%20too%20simp/near/127704475):
But I guess it makes sense due to this instance and defeq:

```lean
@[reducible] instance coe_sort_bool : has_coe_to_sort bool := ⟨Prop, λ y, y = tt⟩
```

