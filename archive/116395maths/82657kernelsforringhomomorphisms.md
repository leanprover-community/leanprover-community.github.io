---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/82657kernelsforringhomomorphisms.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [kernels for ring homomorphisms](https://leanprover-community.github.io/archive/116395maths/82657kernelsforringhomomorphisms.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Casper Putz (Jan 14 2019 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/kernels%20for%20ring%20homomorphisms/near/155081960):
<p>Hi, I wanted to use kernels of ring homomorphisms for the finite fields stuff I am working on with <span class="user-mention" data-user-id="143810">@Joey van Langen</span> . They are not implemented for ring homs, but you would define them exactly the same as is done for linear maps (in linear_algebra.basic). I cannot easily reuse the one for linear maps as a ring homomorphism is not necessarily a linear map of modules. However, all the basic properties of the kernel of a linear map (and ring hom) only depend on the underlying additive group stucture. One could define a kernel of a group_hom and then the kernel (pullback) can be lifted.</p>
<p>I was wondering if there are any reasons for not making linear_map and ring_hom extend group_hom (which would be needed to be defined as only is_group_hom is defined now). This could be done for a lot of these algebraic structures which extend each other, but it could maybe be a bit cumbersome. So I wanted to know some of your opinions about this.</p>

#### [ Johan Commelin (Jan 14 2019 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/kernels%20for%20ring%20homomorphisms/near/155082040):
<p>There are kernels for <code>is_group_hom</code>, I think</p>

#### [ Johan Commelin (Jan 14 2019 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/kernels%20for%20ring%20homomorphisms/near/155082051):
<p>And currently I think we only have <code>is_ring_hom</code>. Not the bundled <code>ring_hom</code>.</p>

#### [ Johan Commelin (Jan 14 2019 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/kernels%20for%20ring%20homomorphisms/near/155082105):
<p>I agree that it would be good if <code>is_ring_hom</code> extended <code>is_add_group_hom</code>.</p>

#### [ Casper Putz (Jan 14 2019 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/kernels%20for%20ring%20homomorphisms/near/155082569):
<p>Ah I see, yes you can reuse the kernel of <code>is_group_hom</code> (didn't see it before). Thanks!</p>

#### [ Casper Putz (Jan 14 2019 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/kernels%20for%20ring%20homomorphisms/near/155082592):
<p>Yes, makes a lot of sense I think</p>

#### [ Johan Commelin (Jan 14 2019 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/kernels%20for%20ring%20homomorphisms/near/155082709):
<p>Beware! In Lean there is currently a difference between <code>group</code> and <code>add_group</code>.</p>

#### [ Johan Commelin (Jan 14 2019 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/kernels%20for%20ring%20homomorphisms/near/155082770):
<p>You would have to refactor <code>is_ring_hom</code>. Which I think makes sense... but it might cause a lot of breakage (it shouldn't).</p>


{% endraw %}
