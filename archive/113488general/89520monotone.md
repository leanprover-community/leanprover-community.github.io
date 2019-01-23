---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/89520monotone.html
---

## Stream: [general](index.html)
### Topic: [monotone](89520monotone.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monotone/near/124357030):
sehr geehrter @**Johannes Hölzl** , monotone doesn't mean what you think it means

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Mar 29 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monotone/near/124357527):
What is the difference between https://github.com/leanprover/mathlib/blob/master/order/basic.lean#L19
`def monotone (f : α → β) := ∀⦃a b⦄, a ≤ b → f a ≤ f b`
and
` class is_ord_hom (f : α → α) : Prop :=  (ord : ∀ x y, x ≤ y → f x ≤ f y) `?
Monotone is a little bit more general, but not a type class...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monotone/near/124357537):
@**Johannes Hölzl** monotone means increasing **or** decreasing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monotone/near/124357538):
at least in where I'm from

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Mar 29 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monotone/near/124357653):
Not in order theory, the "Monotonicity in order theory" section in https://en.wikipedia.org/wiki/Monotonic_function tells us that it means what you maybe call an increasing function.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 29 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monotone/near/124357695):
fair enough

