---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08557howtouselinearcombination.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [how to use linear combination](https://leanprover-community.github.io/archive/113488general/08557howtouselinearcombination.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Blair Shi (Jul 23 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20linear%20combination/near/130142613):
<div class="codehilite"><pre><span></span>variables {k : Type u} {V : Type v}
variable [field k]
variables [ring k] [module k V]
variables {a : k} {b : V}
include k
variables (x y : V)
variable (fvs : finite_dimensional_vector_space k V)

def is_in_vecsp (v : V) (fvs : finite_dimensional_vector_space k V) : Prop :=
v ∈ span {v₁ : V | v₁ ∈ fvs.ordered_basis}

lemma add_closed : is_in_vecsp x fvs ∧ is_in_vecsp y fvs → is_in_vecsp (x + y) fvs :=
begin
intro h₀,
cases h₀ with le ri,
have h₁ : ∃(lc₁ : lc k V), (∀ x∉fvs.ordered_basis, lc₁ x = 0) ∧ x = lc₁.sum (λb a, a • b), from le,
</pre></div>


<p>I don't know why for <code>lc₁</code> in <code>lc₁.sum (λb a, a • b)</code>, it reports </p>
<div class="codehilite"><pre><span></span>synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  no_zero_divisors.to_has_zero k
inferred
  mul_zero_class.to_has_zero k
</pre></div>


<p>Can anyone help me to solve this problem?</p>

#### [ Patrick Massot (Jul 23 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20linear%20combination/near/130143764):
<p>Probably not until you give us a MWE (depending only on mathlib and not your own code).</p>

#### [ Patrick Massot (Jul 23 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20linear%20combination/near/130143772):
<p>You can use gist or pasteall if it's too long</p>

#### [ Reid Barton (Jul 23 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20linear%20combination/near/130149943):
<p>I think you should not have both <code>field k</code> and <code>ring k</code></p>

#### [ Kevin Buzzard (Jul 23 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20linear%20combination/near/130170440):
<p>Yes -- try deleting the <code>variable [field k]</code> line and see if it works. If it doesn't, then follow Patrick's advice and post some code which will work for everyone, if possible.</p>

#### [ Blair Shi (Jul 24 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20linear%20combination/near/130176920):
<p>Yes, I deleted <code>variable [field k]</code>. now it works. Thx!</p>


{% endraw %}
