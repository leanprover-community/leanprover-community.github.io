---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25923hottinjection.html
---

## Stream: [general](index.html)
### Topic: [hott injection](25923hottinjection.html)

---

#### [Jakob von Raumer (Oct 22 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hott%20injection/near/136298806):
what is the hott-safe replacement for `injection`? Say I have `e : sum.inl a = sum.inr b` in the context and want to solve the goal by pointing out that contradiction...

#### [David Michael Roberts (Oct 23 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hott%20injection/near/136301319):
Presumably that the homotopy fibre is a subsingleton...

#### [Floris van Doorn (Oct 23 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hott%20injection/near/136302873):
The automatically generated `no_confusion` is not compatible with HoTT, and currently, there is no automatically-generated replacement. You have to prove yourself that `sum.inl a = sum.inr b` is impossible and that `sum.inl` and `sum.inr` are injective.

#### [Floris van Doorn (Oct 23 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hott%20injection/near/136302884):
It's done here for `nat` which works essentially in the same way: https://github.com/gebner/hott3/blob/master/src/hott/types/nat/basic.lean#L51-L71

#### [Floris van Doorn (Oct 23 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hott%20injection/near/136302902):
(`succ_inj` is proven a couple lines below that)

#### [Jakob von Raumer (Oct 23 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hott%20injection/near/136304626):
Okay, I started porting `types/sum.hlean`...

#### [Floris van Doorn (Oct 23 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/hott%20injection/near/136313121):
Just so you know: there is more ported on my branch, https://github.com/fpvandoorn/hott3
I haven't ported sum yet. Also, it doesn't currently compile. If I have time I'll look at it tomorrow, and see if I can clean it up and push it to the main repo.

