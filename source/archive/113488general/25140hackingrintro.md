---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25140hackingrintro.html
---

## [general](index.html)
### [hacking `rintro`](25140hackingrintro.html)

#### [Kevin Buzzard (Sep 05 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hacking%20%60rintro%60/near/133395571):
Sometimes I would like to intro a hypothesis and simultaneously change its type to a defeq type. I don't think this can be done with intro. But could it be done with `rintro`? I just tried `rintro ⟨y,Hy,(Hyx : the_prop_I_want)⟩` but it doesn't work (at least it didn't for me). Is this the kind of thing that could be made to work with hackery or do I just have to put up with it?

#### [Simon Hudon (Sep 05 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hacking%20%60rintro%60/near/133395951):
I think `assume` allows you to do that: `assume x : my_defeq_type`

#### [Scott Morrison (Sep 06 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hacking%20%60rintro%60/near/133421542):
Yes: `assume` works great for this (as I only recently learnt from seeing Reid using it).

