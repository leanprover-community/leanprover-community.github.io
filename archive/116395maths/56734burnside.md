---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/56734burnside.html
---

## Stream: [maths](index.html)
### Topic: [burnside!](56734burnside.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125134940):
```
theorem burnside : nonempty ((Σ g, fixed G X g) ≃ (orbits G X × G)) :=
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

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125134941):
@**Kevin Buzzard**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 16 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125137378):
Now you could do Sylow's theorems :-) but they might not be to your taste. I wonder if there's anything to learn from the Coq presentation of all this. I would imagine they use this sort of stuff everywhere in the odd order theorem.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125137426):
@**Kevin Buzzard** sylow uses burnside?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 16 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125137704):
One proof I've seen does. I'm sure there are others :-) but it wouldn't surprise me if all of them used "counting" in some way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 16 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125138288):
There is also Sylow's first theorem in Lean2 https://github.com/leanprover/lean2/tree/master/library/theories/finite_group_theory/pgroup.lean
We never did the effort to port this development to Lean 3, and a lot of stuff changed since them. But I think it would be worthwhile to take a look.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125138291):
I say, the theory of (finite) cardinality in Lean is not well-developed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 16 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125138541):
Come on, you know that mathlib is a open source project. It's only as developed, as people put an effort into developing it.
This includes by the way answering comments on pull requests ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125138590):
well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125138596):
fixing those things created more error for me, so I need time to de-frustrate myself and to fix those errors

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 16 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125138654):
...and revise for mechanics. I might soon need some other localization facts which aren't there yet, but I still didn't finish wrestling with compactness. Is Johannes talking about localization or something else?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125138658):
free group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 16 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/burnside%21/near/125138659):
https://github.com/leanprover/mathlib/pull/89#discussion_r179398893

