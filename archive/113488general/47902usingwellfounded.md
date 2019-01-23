---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/47902usingwellfounded.html
---

## Stream: [general](index.html)
### Topic: [using_well_founded](47902usingwellfounded.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 28 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132934326):
I'm looking at RB trees again. I found a really good implementation in Coq that I am copying over to Lean: https://github.com/coq/coq/blob/a1fc621b943dbf904705dc88ed27c26daf4c5e72/theories/MSets/MSetRBT.v
Here is the start of my code:
https://github.com/EdAyers/mathlib/blob/rb/data/rb.lean
My problem is that it can't prove that my definition of `append` is terminating automatically. Is there a quick fix for this kind of thing or am I going to have to use well_founded.fix? I can't figure out how to use the `using_well_founded` keyword.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 28 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132934439):
Did you look at the docs at https://github.com/EdAyers/mathlib/blob/rb/docs/extras/well_founded_recursion.md ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 28 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132934463):
Ah thanks I haven't read that one yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 28 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132934551):
I'm not saying it solves your problem, but it does have a bunch of cool tricks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 28 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132934673):
One of the things it can't show is
```lean
⊢ tr.sizeof α lr < tr.sizeof α ll + (tr.sizeof α lr + 2)
```
Is there a tactic that will solve that instantaneously?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 28 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132940133):
https://github.com/leanprover-community/mathlib-nursery/blob/master/src/tactic/monotonicity/interactive.lean#L571-L595 presumably

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 28 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132940151):
not yet in mathlib, but you can temporarily add a dependency to this repo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 28 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132940196):
What's the problem with corelib rbtrees?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 28 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132940302):
Corelib rbtrees don't have `erase`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 28 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132940317):
And there are no proofs about them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 28 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132940341):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 28 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132941632):
I fixed this by adding my own has_well_founded instance
```lean
instance custom_wf : has_well_founded (tr α × tr α) := has_well_founded_of_has_sizeof (tr α × tr α) 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 28 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132941692):
Before it was using wf using lexical ordering which was throwing it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 28 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132941711):
at least I think that's why

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Leonardo de Moura (Aug 28 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132952390):
@**Edward Ayers** The proofs are here https://github.com/leanprover/lean/tree/master/library/data/rbtree

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132953705):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Aug 28 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132953908):
thanks Leo! sorry I didn't spot them.

