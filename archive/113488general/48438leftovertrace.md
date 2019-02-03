---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48438leftovertrace.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [leftover trace?](https://leanprover-community.github.io/archive/113488general/48438leftovertrace.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Sep 29 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leftover%20trace%3F/near/134895750):
<p>When I build mathlib, I see:</p>

#### [ Patrick Massot (Sep 29 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leftover%20trace%3F/near/134895751):
<div class="codehilite"><pre><span></span>@[class, priority 100, to_additive name.mk_string &quot;add_group&quot; name.anonymous]
structure group : Type u → Type u
fields:
group.mul : Π {α : Type u} [c : group α], α → α → α
group.mul_assoc : ∀ {α : Type u} [c : group α] (a b c_1 : α), a * b * c_1 = a * (b * c_1)
group.one : Π (α : Type u) [c : group α], α
group.one_mul : ∀ {α : Type u} [c : group α] (a : α), 1 * a = a
group.mul_one : ∀ {α : Type u} [c : group α] (a : α), a * 1 = a
group.inv : Π {α : Type u} [c : group α], α → α
group.mul_left_inv : ∀ {α : Type u} [c : group α] (a : α), a⁻¹ * a = 1
</pre></div>

#### [ Patrick Massot (Sep 29 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leftover%20trace%3F/near/134895753):
<p>Is there a debug trace left somewhere?</p>

#### [ Simon Hudon (Sep 30 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leftover%20trace%3F/near/134899203):
<p>You can use <code>grep</code> on the mathlib directory. It's probably one of the flavors of <code>#print</code></p>


{% endraw %}
