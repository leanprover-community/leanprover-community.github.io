---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/24838Constructivetensorproduct.html
---

## [maths](index.html)
### [Constructive tensor product](24838Constructivetensorproduct.html)

#### [Kenny Lau (Jul 25 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive tensor product/near/130248625):
https://github.com/kckennylau/Lean/blob/master/constructive_tensor_product.lean

#### [Kenny Lau (Jul 25 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive tensor product/near/130248632):
I built a constructive tensor product and proved that it is a module. I have not proved its properties.

#### [Kenny Lau (Jul 25 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive tensor product/near/130248642):
But inside there is also a constructive version of free abelian group

#### [Kevin Buzzard (Jul 25 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive tensor product/near/130263337):
I needed free abelian group on a type and the finsupp approach demanded I had decidable equality on the type. Is this to be expected?

#### [Kenny Lau (Jul 25 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive tensor product/near/130263345):
my version does not need decidable equality

#### [Kenny Lau (Jul 25 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive tensor product/near/130263346):
but finsupp does need decidable equality

#### [Kevin Buzzard (Jul 25 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive tensor product/near/130263419):
Oh great! I was a bit confused as to why I suddenly needed it.

#### [Kenny Lau (Jul 25 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive tensor product/near/130271063):
https://github.com/kckennylau/Lean/blob/master/constructive_tensor_product.lean

#### [Kenny Lau (Jul 25 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive tensor product/near/130271066):
I proved the property

#### [Kenny Lau (Jul 25 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive tensor product/near/130271073):
@**Kevin Buzzard**

#### [Kevin Buzzard (Jul 25 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive tensor product/near/130275233):
So now back to alg closure? ;-)

#### [Kenny Lau (Jul 25 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive tensor product/near/130293171):
hmm

#### [Kenny Lau (Jul 25 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Constructive tensor product/near/130293213):
let's prove the separability lemma first

