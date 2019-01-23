---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/66460Definingcyclicgroups.html
---

## Stream: [maths](index.html)
### Topic: [Defining cyclic groups](66460Definingcyclicgroups.html)

---


{% raw %}
#### [ Chris Hughes (Jul 29 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130522081):
I have quite a bit of group theory waiting to be merged, Sylow's theorems and parity of permutation over a `fintype`. I cannot merge it because it all depends on some definition of $$C_n$$. Is it worth having both $$ \mathbb{Z}_n $$ and $$C_n$$? It would be nice to only have one, but then $$\mathbb{Z}_n$$ is an `add_group` which obviously causes problems.

#### [ Kevin Buzzard (Jul 29 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130522287):
We surely need a cyclic group with * as the group law. Another issue is that Z/nZ has a canonical generator, namely 1, whereas a cyclic group of order n is a group of order n with the property that a generator exists. A great example of a cyclic group is the units in (Z/pZ), with p prime. The standard proof that it's cyclic is completely nonconstructive.

#### [ Chris Hughes (Jul 29 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130522597):
Why would the presence of a canonical generator be a problem? If you don't want it, just ignore it. Any sensible computable version of $$C_n$$ will have a canonical generator anyway, as it should probably be defeq to $$\mathbb{Z}_n$$ anyway.

#### [ Kenny Lau (Jul 29 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130522607):
```quote
We surely need a cyclic group with * as the group law. Another issue is that Z/nZ has a canonical generator, namely 1, whereas a cyclic group of order n is a group of order n with the property that a generator exists. A great example of a cyclic group is the units in (Z/pZ), with p prime. The standard proof that it's cyclic is completely nonconstructive.
```
under which definition of nonconstructive?

#### [ Chris Hughes (Jul 29 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130522652):
If you gave me a proof of that I could very easily construct a generator.

#### [ Mario Carneiro (Jul 29 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523620):
I think `is_cyclic` should be a *property* of a `group`, not a particular group

#### [ Mario Carneiro (Jul 29 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523623):
and the Fundamental Theorem of Cyclic groups says that two cyclic groups with the same cardinality are isomorphic

#### [ Kenny Lau (Jul 29 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523672):
```lean
class cyclic_group (α : Type*) extends group α :=
(cyclic : ∃ a, ∀ b : α, ∃ i : ℤ, a^i = b)
```

#### [ Kenny Lau (Jul 29 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523674):
https://github.com/dorhinj/leanstuff/blob/master/gourp1.lean

#### [ Mario Carneiro (Jul 29 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523681):
yes, except I don't think it should be part of the hierarchy

#### [ Kenny Lau (Jul 29 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523685):
code not by me

#### [ Mario Carneiro (Jul 29 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523724):
I know, chris reads this too

#### [ Mario Carneiro (Jul 29 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523733):
It is certainly not true that you can construct a generator given a cyclic group

#### [ Mario Carneiro (Jul 29 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523734):
you can at best construct a `trunc generator` given a `fintype` or `enumerable` cyclic group

#### [ Chris Hughes (Jul 29 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523773):
```quote
I think `is_cyclic` should be a *property* of a `group`, not a particular group
```
But we also obviously need the fact that for all n, there exists a cyclic group of order n.

#### [ Mario Carneiro (Jul 29 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523778):
maybe, but it depends on how you want to say it

#### [ Mario Carneiro (Jul 29 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523783):
How would you need that?

#### [ Chris Hughes (Jul 29 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523828):
Parity of a permutation is a homomorphism into $$C_2$$. In my Sylow proof I needed to use the group action of $$C_p$$ that rotated the elements of a vector $$G^p$$

#### [ Mario Carneiro (Jul 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523874):
For the parity example, I'm on board with Kenny's `mu2`, although I'm not sure what the name stands for

#### [ Kenny Lau (Jul 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523876):
mu_n is the set of the n-th roots of unity in a field

#### [ Mario Carneiro (Jul 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523877):
For the group action, that's obviously a subgroup of the group action of the symmetric group

#### [ Kenny Lau (Jul 29 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523878):
I learnt it from LCFT, but I don't know if it is used elsewhere

#### [ Kenny Lau (Jul 29 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523883):
and for the record Kevin wrote that part (and the name)

#### [ Chris Hughes (Jul 29 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523927):
For the Sylow one, I needed to use the map from the naturals to $$\mathbb{Z}_n$$, so some random subgroup is not that easy to use.

#### [ Mario Carneiro (Jul 29 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523976):
I guess you want to know that `rotate` is a group hom from `Z` to the symmetric group

#### [ Mario Carneiro (Jul 29 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523980):
and its image is cyclic, because the image of any group hom from Z is cyclic

#### [ Chris Hughes (Jul 29 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130523984):
More or less. Maybe I could do it differently.

#### [ Mario Carneiro (Jul 29 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130524043):
I realize that mathematicians are used to treating $$C_n$$ as one thing, but keeping in mind the isomorphism is equality abuse of notation in this area, it's best to allow for cyclic groups to appear in situ

#### [ Mario Carneiro (Jul 29 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130524095):
That said, if you really need a concrete cyclic additive group `Zmod n` will do the job

#### [ Kenny Lau (Jul 29 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130524100):
`multiplicative (Zmod n)`

#### [ Chris Hughes (Jul 29 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Defining%20cyclic%20groups/near/130524105):
That's what I used for Sylow. It wasn't that pretty.


{% endraw %}
