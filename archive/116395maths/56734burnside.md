---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/56734burnside.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [burnside!](https://leanprover-community.github.io/archive/116395maths/56734burnside.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 16 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125134940):
<div class="codehilite"><pre><span></span>theorem burnside : nonempty ((Σ g, fixed G X g) ≃ (orbits G X × G)) :=
⟨calc  (Σ g, fixed G X g)
    ≃ (Σ x, stab G X x) :
  ⟨λ z, ⟨z.2.1, z.1, z.2.2⟩, λ z, ⟨z.2.1, z.1, z.2.2⟩, λ ⟨g, x, h⟩, rfl, λ ⟨x, g, h⟩, rfl⟩
... ≃ (Σ A : orbits G X, Σ x : { x | ⟦x⟧ = A }, stab G X x) :
  ⟨λ z, ⟨⟦z.1⟧, ⟨_, rfl⟩, z.2⟩, λ z, ⟨z.2.1.1, z.2.2⟩, λ ⟨x, z⟩, rfl, λ ⟨A, ⟨x, (hx : ⟦x⟧ = A)⟩, z⟩, sigma.eq hx $ by subst hx⟩
... ≃ (Σ A : orbits G X, Σ x : { x | ⟦x⟧ = A }, stab G X (quotient.out A)) :
  equiv.sigma_congr_right (λ A, equiv.sigma_congr_right (λ ⟨x, (hx : ⟦x⟧ = A)⟩,
    stab_equiv G X _ _ _ (classical.some_spec (quotient.exact (hx.trans (quotient.out_eq A).symm)))))
... ≃ (Σ A : orbits G X, { x | ⟦x⟧ = A } × stab G X (quotient.out A)) :
  equiv.sigma_congr_right (λ A, equiv.sigma_equiv_prod _ _)
... ≃ (Σ A : orbits G X, orbit G X (quotient.out A) × stab G X (quotient.out A)) :
  equiv.sigma_congr_right (λ A, by rw orbit_out_eq_fibre)
... ≃ (Σ A : orbits G X, G) :
  equiv.sigma_congr_right (λ A, classical.choice $ orbit_stab G X _)
... ≃ (orbits G X × G) :
  equiv.sigma_equiv_prod _ _⟩
</pre></div>

#### [ Kenny Lau (Apr 16 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125134941):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kevin Buzzard (Apr 16 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125137378):
<p>Now you could do Sylow's theorems :-) but they might not be to your taste. I wonder if there's anything to learn from the Coq presentation of all this. I would imagine they use this sort of stuff everywhere in the odd order theorem.</p>

#### [ Kenny Lau (Apr 16 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125137426):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> sylow uses burnside?</p>

#### [ Kevin Buzzard (Apr 16 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125137704):
<p>One proof I've seen does. I'm sure there are others :-) but it wouldn't surprise me if all of them used "counting" in some way.</p>

#### [ Johannes Hölzl (Apr 16 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125138288):
<p>There is also Sylow's first theorem in Lean2 <a href="https://github.com/leanprover/lean2/tree/master/library/theories/finite_group_theory/pgroup.lean" target="_blank" title="https://github.com/leanprover/lean2/tree/master/library/theories/finite_group_theory/pgroup.lean">https://github.com/leanprover/lean2/tree/master/library/theories/finite_group_theory/pgroup.lean</a><br>
We never did the effort to port this development to Lean 3, and a lot of stuff changed since them. But I think it would be worthwhile to take a look.</p>

#### [ Kenny Lau (Apr 16 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125138291):
<p>I say, the theory of (finite) cardinality in Lean is not well-developed</p>

#### [ Johannes Hölzl (Apr 16 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125138541):
<p>Come on, you know that mathlib is a open source project. It's only as developed, as people put an effort into developing it.<br>
This includes by the way answering comments on pull requests ;-)</p>

#### [ Kenny Lau (Apr 16 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125138590):
<p>well</p>

#### [ Kenny Lau (Apr 16 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125138596):
<p>fixing those things created more error for me, so I need time to de-frustrate myself and to fix those errors</p>

#### [ Kevin Buzzard (Apr 16 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125138654):
<p>...and revise for mechanics. I might soon need some other localization facts which aren't there yet, but I still didn't finish wrestling with compactness. Is Johannes talking about localization or something else?</p>

#### [ Kenny Lau (Apr 16 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125138658):
<p>free group</p>

#### [ Kenny Lau (Apr 16 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125138659):
<p><a href="https://github.com/leanprover/mathlib/pull/89#discussion_r179398893" target="_blank" title="https://github.com/leanprover/mathlib/pull/89#discussion_r179398893">https://github.com/leanprover/mathlib/pull/89#discussion_r179398893</a></p>


{% endraw %}
