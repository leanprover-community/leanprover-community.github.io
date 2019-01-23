---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/82657kernelsforringhomomorphisms.html
---

## Stream: [maths](index.html)
### Topic: [kernels for ring homomorphisms](82657kernelsforringhomomorphisms.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Casper Putz (Jan 14 2019 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/kernels%20for%20ring%20homomorphisms/near/155081960):
Hi, I wanted to use kernels of ring homomorphisms for the finite fields stuff I am working on with @**Joey van Langen** . They are not implemented for ring homs, but you would define them exactly the same as is done for linear maps (in linear_algebra.basic). I cannot easily reuse the one for linear maps as a ring homomorphism is not necessarily a linear map of modules. However, all the basic properties of the kernel of a linear map (and ring hom) only depend on the underlying additive group stucture. One could define a kernel of a group_hom and then the kernel (pullback) can be lifted.

I was wondering if there are any reasons for not making linear_map and ring_hom extend group_hom (which would be needed to be defined as only is_group_hom is defined now). This could be done for a lot of these algebraic structures which extend each other, but it could maybe be a bit cumbersome. So I wanted to know some of your opinions about this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/kernels%20for%20ring%20homomorphisms/near/155082040):
There are kernels for `is_group_hom`, I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/kernels%20for%20ring%20homomorphisms/near/155082051):
And currently I think we only have `is_ring_hom`. Not the bundled `ring_hom`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/kernels%20for%20ring%20homomorphisms/near/155082105):
I agree that it would be good if `is_ring_hom` extended `is_add_group_hom`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Casper Putz (Jan 14 2019 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/kernels%20for%20ring%20homomorphisms/near/155082569):
Ah I see, yes you can reuse the kernel of `is_group_hom` (didn't see it before). Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Casper Putz (Jan 14 2019 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/kernels%20for%20ring%20homomorphisms/near/155082592):
Yes, makes a lot of sense I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/kernels%20for%20ring%20homomorphisms/near/155082709):
Beware! In Lean there is currently a difference between `group` and `add_group`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/kernels%20for%20ring%20homomorphisms/near/155082770):
You would have to refactor `is_ring_hom`. Which I think makes sense... but it might cause a lot of breakage (it shouldn't).

