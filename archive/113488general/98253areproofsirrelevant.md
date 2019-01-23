---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98253areproofsirrelevant.html
---

## Stream: [general](index.html)
### Topic: [are proofs irrelevant?](98253areproofsirrelevant.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 15 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/are%20proofs%20irrelevant%3F/near/128121844):
(working example, far from minimal, sorry for that)
https://gist.github.com/kckennylau/4a009e228980fdbe9f6c879f9fa0eca5
Excerpt:
```lean
instance abelianization.topological_group (G : Type*) [topological_space G] [group G]
  [topological_group G] : topological_group (abelianization G) :=

topological_group.coinduced (quot.mk (rel G)) quot.exists_rep $ λ S hs,
have (⋃ x : { x // quot.mk (rel G) x = 1}, (λ y, x.1 * y) ⁻¹' S)
    = quot.mk (rel G) ⁻¹' (quot.mk (rel G) '' S),
  from set.ext $ λ z,
  ⟨λ ⟨S, ⟨⟨g, h1⟩, rfl⟩, h2⟩, ⟨g * z, h2, by simp [is_group_hom.mul (quot.mk (rel G)), h1]⟩,
  λ ⟨g, h1, h2⟩, ⟨_, ⟨⟨g * z⁻¹, by simp [is_group_hom.mul (quot.mk (rel G)), is_group_hom.inv (quot.mk (rel G)), h2]⟩, rfl⟩, by simp [h1]⟩⟩,
this ▸ is_open_Union $ λ x : {x // quot.mk (rel G) x = 1},
continuous_mul continuous_const continuous_id _ hs

/-{ continuous_mul := λ S hs1, is_open_prod_iff.2 $
    have _ := is_open_prod_iff.1 (topological_monoid.continuous_mul G _ hs1),
    by refine quot.ind (λ x, _); refine quot.ind (λ y, _);
    from λ h, let ⟨u, v, hu, hv, hxu, hyv, H⟩ := this x y h in
    ⟨quot.mk _ '' u, quot.mk _ '' v,
    show is_open (quot.mk (rel G) ⁻¹' (quot.mk (rel G) '' u)),
      from have (⋃ x : { x // quot.mk (rel G) x = 1}, (λ y, x.1 * y) ⁻¹' u)
          = quot.mk (rel G) ⁻¹' (quot.mk (rel G) '' u),
        from set.ext $ λ z,
        ⟨λ ⟨S, ⟨⟨g, h1⟩, rfl⟩, h2⟩, ⟨g * z, h2, by simp [is_group_hom.mul (quot.mk (rel G)), h1]⟩,
        λ ⟨g, h1, h2⟩, ⟨_, ⟨⟨g * z⁻¹, by simp [is_group_hom.mul (quot.mk (rel G)), is_group_hom.inv (quot.mk (rel G)), h2]⟩, rfl⟩, by simp [h1]⟩⟩,
      this ▸ is_open_Union $ λ x : {x // quot.mk (rel G) x = 1},
      (continuous_mul continuous_const continuous_id) _ hu,
    show is_open (quot.mk (rel G) ⁻¹' (quot.mk (rel G) '' v)),
      from have (⋃ x : { x // quot.mk (rel G) x = 1}, (λ y, x.1 * y) ⁻¹' v)
          = quot.mk (rel G) ⁻¹' (quot.mk (rel G) '' v),
        from set.ext $ λ z,
        ⟨λ ⟨S, ⟨⟨g, h1⟩, rfl⟩, h2⟩, ⟨g * z, h2, by simp [is_group_hom.mul (quot.mk (rel G)), h1]⟩,
        λ ⟨g, h1, h2⟩, ⟨_, ⟨⟨g * z⁻¹, by simp [is_group_hom.mul (quot.mk (rel G)), is_group_hom.inv (quot.mk (rel G)), h2]⟩, rfl⟩, by simp [h1]⟩⟩,
      this ▸ is_open_Union $ λ x : {x // quot.mk (rel G) x = 1},
      (continuous_mul continuous_const continuous_id) _ hv,
    ⟨x, hxu, rfl⟩, ⟨y, hyv, rfl⟩,
    λ ⟨p, q⟩, by refine quot.induction_on p (λ m, _);
      refine quot.induction_on q (λ n, _);
      from λ ⟨⟨P, hp1, hp2⟩, ⟨Q, hq1, hq2⟩⟩,
      suffices quot.mk (rel G) P * quot.mk (rel G) Q ∈ S,
      by rw [hp2, hq2] at this; simpa using this,
      @H (P, Q) ⟨hp1, hq1⟩⟩,
  continuous_inv := λ S hs,
    show is_open (quot.mk (rel G) ⁻¹' ((λ p : abelianization G, p⁻¹) ⁻¹' S)),
    from have (λ p : G, p⁻¹) ⁻¹' (quot.mk (rel G) ⁻¹' S)
        = quot.mk (rel G) ⁻¹' ((λ p : abelianization G, p⁻¹) ⁻¹' S),
      from set.ext $ λ z, by simp [is_group_hom.inv (quot.mk (rel G))],
    this ▸ (topological_group.continuous_inv G _ $
      continuous_coinduced_rng _ hs) }-/
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 15 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/are%20proofs%20irrelevant%3F/near/128121848):
Problem: If I use the first proof, then there is error below; if I use the second proof, then there is no error.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 15 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/are%20proofs%20irrelevant%3F/near/128121852):
@**Mario Carneiro** please help

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 15 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/are%20proofs%20irrelevant%3F/near/128122041):
why would they be the same?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 15 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/are%20proofs%20irrelevant%3F/near/128122048):
because they're just proofs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 15 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/are%20proofs%20irrelevant%3F/near/128122055):
it's an instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 15 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/are%20proofs%20irrelevant%3F/near/128122058):
what should I do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 15 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/are%20proofs%20irrelevant%3F/near/128122146):
ah I solved it by making `topological_group.coinduced` a theorem


{% endraw %}
