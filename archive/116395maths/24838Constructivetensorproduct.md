---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/24838Constructivetensorproduct.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Constructive tensor product](https://leanprover-community.github.io/archive/116395maths/24838Constructivetensorproduct.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Jul 25 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive%20tensor%20product/near/130248625):
<p><a href="https://github.com/kckennylau/Lean/blob/master/constructive_tensor_product.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/constructive_tensor_product.lean">https://github.com/kckennylau/Lean/blob/master/constructive_tensor_product.lean</a></p>

#### [ Kenny Lau (Jul 25 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive%20tensor%20product/near/130248632):
<p>I built a constructive tensor product and proved that it is a module. I have not proved its properties.</p>

#### [ Kenny Lau (Jul 25 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive%20tensor%20product/near/130248642):
<p>But inside there is also a constructive version of free abelian group</p>

#### [ Kevin Buzzard (Jul 25 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive%20tensor%20product/near/130263337):
<p>I needed free abelian group on a type and the finsupp approach demanded I had decidable equality on the type. Is this to be expected?</p>

#### [ Kenny Lau (Jul 25 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive%20tensor%20product/near/130263345):
<p>my version does not need decidable equality</p>

#### [ Kenny Lau (Jul 25 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive%20tensor%20product/near/130263346):
<p>but finsupp does need decidable equality</p>

#### [ Kevin Buzzard (Jul 25 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive%20tensor%20product/near/130263419):
<p>Oh great! I was a bit confused as to why I suddenly needed it.</p>

#### [ Kenny Lau (Jul 25 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive%20tensor%20product/near/130271063):
<p><a href="https://github.com/kckennylau/Lean/blob/master/constructive_tensor_product.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/constructive_tensor_product.lean">https://github.com/kckennylau/Lean/blob/master/constructive_tensor_product.lean</a></p>

#### [ Kenny Lau (Jul 25 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive%20tensor%20product/near/130271066):
<p>I proved the property</p>

#### [ Kenny Lau (Jul 25 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive%20tensor%20product/near/130271073):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kevin Buzzard (Jul 25 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive%20tensor%20product/near/130275233):
<p>So now back to alg closure? ;-)</p>

#### [ Kenny Lau (Jul 25 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive%20tensor%20product/near/130293171):
<p>hmm</p>

#### [ Kenny Lau (Jul 25 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive%20tensor%20product/near/130293213):
<p>let's prove the separability lemma first</p>


{% endraw %}
