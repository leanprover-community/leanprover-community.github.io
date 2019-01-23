---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/22756uniformityinuniformaddgroup.html
---

## Stream: [maths](index.html)
### Topic: [uniformity in uniform add group](22756uniformityinuniformaddgroup.html)

---


{% raw %}
#### [ Patrick Massot (Dec 19 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniformity%20in%20uniform%20add%20group/near/152209408):
I guess this question is mostly for @**Johannes Hölzl**, but everyone is welcome to participate. Remember that, given an additive group structure and a uniform structure on a type `a`, the Prop-valued class `uniform_add_group a` states that substraction is uniformly continuous. The key lemma about such groups is https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_structures.lean#L343 stating `uniformity = comap (λx:α×α, x.2 - x.1) (nhds (0:α))`. The key technical ingredient is:
```lean
lemma mem_uniformity_of_uniform_continuous_invarant [uniform_space α] {s:set (α×α)} {f : α → α → α}
  (hf : uniform_continuous (λp:α×α, f p.1 p.2)) (hs : s ∈ (@uniformity α _).sets) :
  ∃u∈(@uniformity α _).sets, ∀a b c, (a, b) ∈ u → (f a c, f b c) ∈ s :=
begin
  rw [uniform_continuous, uniformity_prod_eq_prod, tendsto_map'_iff, (∘)] at hf,
  rcases mem_map_sets_iff.1 (hf hs) with ⟨t, ht, hts⟩, clear hf,
  rcases mem_prod_iff.1 ht with ⟨u, hu, v, hv, huvt⟩, clear ht,
  refine ⟨u, hu, assume a b c hab, hts $ (mem_image _ _ _).2 ⟨⟨⟨a, b⟩, ⟨c, c⟩⟩, huvt ⟨_, _⟩, _⟩⟩,
  exact hab,
  exact refl_mem_uniformity hv,
  refl
end
```
which secretely says that if `f : α → α → α` is uniformly continuous then its partial evaluations `λ a, f a c` are uniformly continuous uniformly in `c`. The key lemma uses this both for substraction and for addition (whose uniform continuity follows from uniform continuity of substraction). 

Both the key technical ingredient and the key technical lemma use members of uniformities :oh_no: I spent some time today trying to get rid of this shameful proof. I managed to get the member-free version of the technical ingredient (also generalized to three different uniform spaces, because why not?):
```lean
lemma partial_ev_uniformly_uniform_continuous [uniform_space α] [uniform_space β] [uniform_space γ]
{f : α → β → γ} (hf : uniform_continuous (λp:α×β, f p.1 p.2)) :
let π_α : (α × β) × (α × β) → α × α := λ p, (p.1.1, p.2.1),
    π_β : (α × β) × (α × β) → β × β := λ p, (p.1.2, p.2.2),
    F   : (α × β) × (α × β) → γ × γ := λ p, (f p.1.1 p.1.2, f p.2.1 p.2.2) in
  map F (comap π_α uniformity ⊓ comap π_β (principal id_rel)) ≤ uniformity :=
le_trans (map_mono $ inf_le_inf (le_refl _) $ comap_mono refl_le_uniformity) (uniform_continuous₂_iff.1 hf)
```
which starts from the criterion of the above thread, and percolates the fact that, by definition of uniform structures,  `principal id_rel ≤ uniformity`.

Going from this statement to the technical ingredient is all about unpacking membership for map, inf and `principal id_rel`:
```lean
lemma mem_partial_ev_uniformly_uniform_continuous [uniform_space α] [uniform_space β] [uniform_space γ]
  {s:set (γ×γ)} {f : α → β → γ} (hf : uniform_continuous (λp:α×β, f p.1 p.2))
  (hs : s ∈ (@uniformity γ _).sets) :
  ∃ u ∈ (@uniformity α _).sets, ∀ a a' b, (a, a') ∈ u → (f a b, f a' b) ∈ s :=
begin
  have key := mem_inf_sets.1 (mem_map.1 $ partial_ev_uniformly_uniform_continuous hf hs),
  rcases key with ⟨t, ⟨u, hu, hut⟩, v, ⟨w, hw, hwv⟩, htv⟩,
  use [u, hu],
  intros a a' b haa',
  rw [mem_principal_sets, id_rel_subset] at hw,
  have : ((a, b), (a', b)) ∈ t ∩ v := by split ; tauto, 
  exact htv this,
end
```
 I also rewrote the main lemma in order to do everything directly using substraction, and without juggling with the map and comap adjunction. I also stated explicitly the key steps. The result is:
```lean
lemma uniformity_eq_comap_nhds_zero : uniformity = comap (λx:α×α, x.2 - x.1) (nhds (0:α)) :=
begin
  suffices : uniformity = comap (λ (x : α × α), ((0 : α), x.2 - x.1)) uniformity,
  by rwa [nhds_eq_comap_uniformity, filter.comap_comap_comp],
  apply le_antisymm,
  { intros s hs,
    rcases mem_comap_sets.1 hs with ⟨u, hu, hus⟩,
    rcases mem_uniformity_of_uniform_continuous_invarant uniform_continuous_sub' hu with ⟨t, ht, hts⟩,
    have key : t ⊆ (λ (x : α × α), ((0 : α), x.2 - x.1)) ⁻¹' u,
    { rw subset_def,
      rintros ⟨a, b⟩ ab_in, 
      simpa using hts a b a ab_in, },
    exact mem_sets_of_superset (mem_sets_of_superset ht key) hus },
  { intros s hs,
    rcases mem_uniformity_of_uniform_continuous_invarant uniform_continuous_sub' hs with ⟨t, ht, hts⟩,
    have key : (λ (x : α × α), ((0 : α), x.2 - x.1)) ⁻¹' t ⊆ s,
    { rw subset_def,
      rintros ⟨a, b⟩ ab_in,
      simpa using hts 0 (b-a) (-a) ab_in },
    exact ⟨_, ht, key⟩ }
end
```
But I couldn't get rid of members and use directly the abstract version of the key ingredient. Any idea?


{% endraw %}
