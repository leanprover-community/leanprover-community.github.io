---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72933hascoetosortonset.html
---

## [general](index.html)
### [`has_coe_to_sort` on set](72933hascoetosortonset.html)

#### [Kevin Buzzard (Jul 16 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747338):
What am I doing wrong:

```lean
import data.set.basic

example (X : Type) : has_coe_to_sort (set X) := by apply_instance -- works
theorem foo (X : Type) : has_coe_to_sort (set X) := by apply_instance -- error
/-
tactic.mk_instance failed to generate instance for
  has_coe_to_sort (set X)
state:
X : Type
⊢ has_coe_to_sort (set X)
-/
```

?

#### [Mario Carneiro (Jul 16 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747359):
check your universe variables

#### [Kevin Buzzard (Jul 16 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747379):
*boggle*

#### [Kevin Buzzard (Jul 16 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747752):
I remember now, I've seen this before. `definition foo...` works, `example` works, `theorem` doesn't. Thanks!

#### [Mario Carneiro (Jul 16 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747757):
`theorem` works too if you assign the universe variables first

#### [Kenny Lau (Jul 16 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747806):
```lean
import data.set.basic

example (X : Type) : has_coe_to_sort (set X) := by apply_instance -- works
theorem foo (X : Type) : has_coe_to_sort.{1 2} (set X) := by apply_instance -- works
```

#### [Mario Carneiro (Jul 16 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747807):
but `has_coe_to_fun` is an instance so it's best to use `instance` or `def`

#### [Kenny Lau (Jul 16 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747808):
you mean this?

#### [Mario Carneiro (Jul 16 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747812):
yes

#### [Kenny Lau (Jul 16 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747820):
because the default Sort is Sort 0?

#### [Kenny Lau (Jul 16 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747825):
so I have to say 2?

#### [Mario Carneiro (Jul 16 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747889):
I think you only need to state the second one, which is the universe level of the target type, which must be `Sort u` for some `u`

#### [Kenny Lau (Jul 16 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747899):
how do I state the second one without stating the first one?

#### [Mario Carneiro (Jul 16 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747902):
`.{_ 2}`

#### [Kenny Lau (Jul 16 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747911):
well

#### [Mario Carneiro (Jul 16 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747932):
I realize it doesn't save any chars, but it does save some working-out

#### [Sean Leather (Jul 16 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747981):
```quote
I realize it doesn't save any chars, but it does save some working-out
```
But one should work out to stay Lean... :thinking_face:

