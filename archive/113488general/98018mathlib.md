---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98018mathlib.html
---

## Stream: [general](index.html)
### Topic: [mathlib](98018mathlib.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 10 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871039):
Is it strange that we have `monoid.pow` and `gpow` (for groups)? Can we make these more uniform?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871398):
you mean the names? Do you have a better idea?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 10 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871470):
`group.pow`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871581):
eh, I think the reason I didn't do that to begin with is because that puts all the group.pow theorems in the `group` namespace, which makes stuff longer since it's usually not open.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 10 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871623):
I would generally vote for longer over obscure, but I don't have a sense of how bad this would be here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 10 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871671):
So why isn't this an argument for `mpow`, thus not putting all the `monoid.pow` theorems in the `monoid` namespace, which is also usually not oen?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 10 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871681):
```quote
So why isn't this an argument for `mpow`, thus not putting all the `monoid.pow` theorems in the `monoid` namespace, which is also usually not open?
```
you win

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871716):
you will notice that I only use the `monoid` namespace when I need to in theorems, as disambiguation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 10 2018 at 07:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124871722):
but I didn't say the current way is at all consistent, nor am I averse to changing it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 10 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib/near/124874371):
I am not suggesting it be changed, I was just being a pedant.


{% endraw %}
