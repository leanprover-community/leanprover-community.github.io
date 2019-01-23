---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/48739euclideandomain.html
---

## Stream: [maths](index.html)
### Topic: [euclidean domain](48739euclideandomain.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 15 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147742225):
Euclidean domains are extending integral domains, but the entire file doesn't use this. We could just as well extend `comm_ring`. @**Kevin Buzzard** Do you know if every *Euclidean ring* is automatically an integral domain?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 15 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147742459):
I think the following theorems imply they are
```lean
lemma mul_div_cancel (a) {b : α} (b0 : b ≠ 0) : (a * b) / b = a :=
by rw mul_comm; exact mul_div_cancel_left a b0

@[simp] lemma zero_div {a : α} (a0 : a ≠ 0) : 0 / a = 0 :=
by simpa only [zero_mul] using mul_div_cancel 0 a0
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 15 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147742484):
Good catch!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 15 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147742532):
Chris and Lean helped me prove a theorem!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 15 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147744070):
Wait, I was wrong. There's no way to prove `zero_ne_one`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 15 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147744291):
Both a theorem, and a counterexample :slight_smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 15 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147745230):
Haha, sure. Zerology bites me again.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 15 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147755173):
Maybe it should extend `nonzero_comm_ring` instead.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 15 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758098):
Wouldn't that create a possibility for diamonds? Say we prove that integral closures are integral domains. And then for certain of those we prove that they are euclidean rings. And then this would give a new proof that those things are integral domains...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 15 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758146):
Maybe we should just have `euclidean.core` and then `of_core`... that seems to be a common trick.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 15 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758439):
Yes, but they would be definitionally equal diamonds, which happen all the time and are fine.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 15 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758480):
Why would they be defeq? Because `integral_domain` extends `comm_ring` by a `Prop`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 15 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758635):
But all the fields would be the same, because they all come from the same place ultimately.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758657):
No we would have two different proofs that certain rings are integral domains...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758675):
One coming from the fact that it's an integral closure, the other from the fact that it is a euclidean ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758682):
Proofs are irrelevant.

The same thing happens with say, polynomials over an integral domain are an integral domain which means they're a ring, but polynomials over a ring are a ring. So there's two different paths, but they're defeq.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 15 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758765):
Ok, good.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 15 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147759127):
This worked when I tried changing integral domain.
```lean
example : euclidean_domain.integral_domain ℤ = linear_ordered_comm_ring.to_integral_domain := rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Nov 15 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147762970):
Great!

