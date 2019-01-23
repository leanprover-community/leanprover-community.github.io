---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90686groupring.html
---

## Stream: [general](index.html)
### Topic: [group ring](90686groupring.html)

---


{% raw %}
#### [ Kenny Lau (Mar 29 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361143):
Do we have group rings? It's an instance of finsupp

#### [ Kevin Buzzard (Mar 29 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361238):
so you just need to define the multiplication and then prove things like associativity

#### [ Kenny Lau (Mar 29 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361248):
right

#### [ Kevin Buzzard (Mar 29 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361250):
which might be a bit icky

#### [ Kevin Buzzard (Mar 29 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361252):
induction on size of support?

#### [ Kenny Lau (Mar 29 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361253):
well we have the master of finite sums

#### [ Kevin Buzzard (Mar 29 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361255):
he's revising mechanics

#### [ Kenny Lau (Mar 29 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361256):
...

#### [ Kevin Buzzard (Mar 29 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361302):
For those who don't know the mathematics, if `R` is a commutative ring and `G` is a group (or even a monoid) then the group ring `R[G]` (or monoid ring) has as elements the finite formal combinations `r1*g1+r2*g2+...+rn*gn`

#### [ Kevin Buzzard (Mar 29 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361305):
and multiplication is `R`-linear and extends the multiplication on the group.

#### [ Kevin Buzzard (Mar 29 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361450):
There are a whole load of things which it would be natural and fun to do in Lean. We have modules over a ring, and tensor products, so if we have exact sequences then we could do Ext and Tor (projective and injective modules should be straightforward). If we also had group rings we could then do group cohomology. A lot of this is very dry homological algebra which should be very easy in Lean although there might be some foundational work to do to make diagram chases painless.

#### [ Kevin Buzzard (Mar 29 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361456):
Kenny -- Sjoerd de Vries was talking about implementing group cohomology in Lean over the summer, so it's one of the things on my todo list for July, but if you want to start earlier then that's fine by me.

#### [ Johannes Hölzl (Mar 29 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361560):
In  https://github.com/leanprover/mathlib/blob/master/data/finsupp.lean#L646 is the following **definition**: 
`def to_ring [add_monoid α] [ring β] : ring (α →₀ β)`
There is also a commutative version.

I didn't set it up as a type class instance as I think it is better to define a copy for this purpose.

#### [ Johannes Hölzl (Mar 29 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361614):
Hm, actually I'm not sure if this is the one you are looking for ...

#### [ Johannes Hölzl (Mar 29 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361925):
The problem is that `to_ring` is defined on the additive class for `monoid` and I guess you want to see it using the multiplicative structure. But otherwise it should work, it extends the multiplication in the group:
```math
(r_1 * g_1 + \dots + r_n * g_n) * (1 * g') = r_1 * g_1g' + \dots + r_n * g_ng'
```

#### [ Kevin Buzzard (Mar 29 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124363883):
At first glance this looks like exactly the right thing

#### [ Kevin Buzzard (Mar 29 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124363886):
Yes, usually in maths the monoid is written multiplicatively, because the multiplication on the ring extends that on the monoid.

#### [ Kevin Buzzard (Mar 29 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124363928):
In fact I suspect that the monoid ring R[M] is probably some adjoint functor to the forgetful functor sending an R-algebra to the underlying multiplicative monoid


{% endraw %}
