---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/61020finiteintersectionproperty.html
---

## Stream: [general](index.html)
### Topic: [finite intersection property](61020finiteintersectionproperty.html)

---


{% raw %}
#### [ Kenny Lau (Nov 27 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20intersection%20property/near/148672762):
Does Lean know that a space is compact iff it has the finite intersection property?

#### [ Johannes Hölzl (Nov 27 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20intersection%20property/near/148673442):
No this is missing, but I think it is related to the ultrafilter property?!

#### [ Johannes Hölzl (Nov 27 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20intersection%20property/near/148673666):
Sorry it was the other way round. But I guess FIP and `compact_iff_finite_subcover` are easy to relate

#### [ Kenny Lau (Nov 28 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20intersection%20property/near/148682619):
```lean
import analysis.topology.topological_space

universe u

variables {α : Type u} [topological_space α] {S : set α}

theorem compact_iff_fip : compact S ↔
  ∀ T, (∀ t ∈ T, is_closed t) →
    (∀ s ⊆ T, set.finite s → ∃ x, x ∈ S ∩ ⋂₀ s) →
    ∃ x, x ∈ S ∩ ⋂₀ T :=
begin
  classical, split,
  { intros hcs T ht1 ht2, by_contra ht3,
    simp only [not_exists, set.mem_inter_iff, not_and,
      (set.mem_compl_iff _ _).symm, set.compl_sInter, set.compl_image] at ht3,
    have : ∀ t ∈ set.compl ⁻¹' T, is_open t,
      from λ t ht, set.compl_compl t ▸ ht1 (-t) ht,
    rcases compact_elim_finite_subcover hcs this ht3 with ⟨c, hc1, hc2, hc3⟩,
    rcases ht2 (set.compl '' c) (set.image_subset_iff.2 hc1) (set.finite_image _ hc2) with ⟨x, hx1, hx2⟩,
    rcases set.mem_sUnion.1 (hc3 hx1) with ⟨t, htc, hxt⟩,
    exact hx2 (-t) (set.mem_image_of_mem _ htc) hxt },
  { intro H, rw compact_iff_finite_subcover, intros c hc1 hc2, by_contra hc3,
    simp only [not_exists, not_and, set.not_subset,
      (set.mem_compl_iff _ _).symm, set.compl_sUnion] at hc3,
    have : ∀ t ∈ set.compl ⁻¹' c, is_closed t,
      from λ t ht, hc1 (-t) ht,
    have hc4 : ∀ s, s ⊆ set.compl ⁻¹' c → set.finite s → ∃ x, x ∈ S ∩ ⋂₀ s,
    { intros s hs1 hs2,
      have := hc3 _ (set.image_subset_iff.2 hs1) (set.finite_image _ hs2),
      rwa set.compl_compl_image at this },
    rcases H (set.compl ⁻¹' c) this hc4 with ⟨x, hxs, hx⟩,
    rcases set.mem_sUnion.1 (hc2 hxs) with ⟨t, htc, hxt⟩,
    rw ← set.compl_image at hx,
    exact hx _ (set.mem_image_of_mem _ htc) hxt }
end
```

#### [ Kenny Lau (Nov 28 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20intersection%20property/near/148682623):
that was easier than I thought


{% endraw %}
