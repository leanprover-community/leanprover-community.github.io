---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90686groupring.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [group ring](https://leanprover-community.github.io/archive/113488general/90686groupring.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Mar 29 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361143):
<p>Do we have group rings? It's an instance of finsupp</p>

#### [ Kevin Buzzard (Mar 29 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361238):
<p>so you just need to define the multiplication and then prove things like associativity</p>

#### [ Kenny Lau (Mar 29 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361248):
<p>right</p>

#### [ Kevin Buzzard (Mar 29 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361250):
<p>which might be a bit icky</p>

#### [ Kevin Buzzard (Mar 29 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361252):
<p>induction on size of support?</p>

#### [ Kenny Lau (Mar 29 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361253):
<p>well we have the master of finite sums</p>

#### [ Kevin Buzzard (Mar 29 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361255):
<p>he's revising mechanics</p>

#### [ Kenny Lau (Mar 29 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361256):
<p>...</p>

#### [ Kevin Buzzard (Mar 29 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361302):
<p>For those who don't know the mathematics, if <code>R</code> is a commutative ring and <code>G</code> is a group (or even a monoid) then the group ring <code>R[G]</code> (or monoid ring) has as elements the finite formal combinations <code>r1*g1+r2*g2+...+rn*gn</code></p>

#### [ Kevin Buzzard (Mar 29 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361305):
<p>and multiplication is <code>R</code>-linear and extends the multiplication on the group.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361450):
<p>There are a whole load of things which it would be natural and fun to do in Lean. We have modules over a ring, and tensor products, so if we have exact sequences then we could do Ext and Tor (projective and injective modules should be straightforward). If we also had group rings we could then do group cohomology. A lot of this is very dry homological algebra which should be very easy in Lean although there might be some foundational work to do to make diagram chases painless.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361456):
<p>Kenny -- Sjoerd de Vries was talking about implementing group cohomology in Lean over the summer, so it's one of the things on my todo list for July, but if you want to start earlier then that's fine by me.</p>

#### [ Johannes Hölzl (Mar 29 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361560):
<p>In  <a href="https://github.com/leanprover/mathlib/blob/master/data/finsupp.lean#L646" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/finsupp.lean#L646">https://github.com/leanprover/mathlib/blob/master/data/finsupp.lean#L646</a> is the following <strong>definition</strong>: <br>
<code>def to_ring [add_monoid α] [ring β] : ring (α →₀ β)</code><br>
There is also a commutative version.</p>
<p>I didn't set it up as a type class instance as I think it is better to define a copy for this purpose.</p>

#### [ Johannes Hölzl (Mar 29 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361614):
<p>Hm, actually I'm not sure if this is the one you are looking for ...</p>

#### [ Johannes Hölzl (Mar 29 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124361925):
<p>The problem is that <code>to_ring</code> is defined on the additive class for <code>monoid</code> and I guess you want to see it using the multiplicative structure. But otherwise it should work, it extends the multiplication in the group:</p>
<p><span class="tex-error">(r_1 * g_1 + \dots + r_n * g_n) * (1 * g&#39;) = r_1 * g_1g&#39; + \dots + r_n * g_ng&#39;</span></p>

#### [ Kevin Buzzard (Mar 29 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124363883):
<p>At first glance this looks like exactly the right thing</p>

#### [ Kevin Buzzard (Mar 29 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124363886):
<p>Yes, usually in maths the monoid is written multiplicatively, because the multiplication on the ring extends that on the monoid.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group%20ring/near/124363928):
<p>In fact I suspect that the monoid ring R[M] is probably some adjoint functor to the forgetful functor sending an R-algebra to the underlying multiplicative monoid</p>


{% endraw %}
