---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98018mathlib.html
---

## [general](index.html)
### [mathlib](98018mathlib.html)

#### [Scott Morrison (Apr 10 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871039):
Is it strange that we have `monoid.pow` and `gpow` (for groups)? Can we make these more uniform?

#### [Mario Carneiro (Apr 10 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871398):
you mean the names? Do you have a better idea?

#### [Scott Morrison (Apr 10 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871470):
`group.pow`?

#### [Mario Carneiro (Apr 10 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871581):
eh, I think the reason I didn't do that to begin with is because that puts all the group.pow theorems in the `group` namespace, which makes stuff longer since it's usually not open.

#### [Scott Morrison (Apr 10 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871623):
I would generally vote for longer over obscure, but I don't have a sense of how bad this would be here.

#### [Kevin Buzzard (Apr 10 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871671):
So why isn't this an argument for `mpow`, thus not putting all the `monoid.pow` theorems in the `monoid` namespace, which is also usually not oen?

#### [Kenny Lau (Apr 10 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871681):
```quote
So why isn't this an argument for `mpow`, thus not putting all the `monoid.pow` theorems in the `monoid` namespace, which is also usually not open?
```
you win

#### [Mario Carneiro (Apr 10 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871716):
you will notice that I only use the `monoid` namespace when I need to in theorems, as disambiguation

#### [Mario Carneiro (Apr 10 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871722):
but I didn't say the current way is at all consistent, nor am I averse to changing it

#### [Kevin Buzzard (Apr 10 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124874371):
I am not suggesting it be changed, I was just being a pedant.

