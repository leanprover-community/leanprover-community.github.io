---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/50225characterisationofreals.html
---

## [maths](index.html)
### [characterisation of reals](50225characterisationofreals.html)

#### [Kevin Buzzard (Nov 17 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/characterisation of reals/near/147869830):
```lean
import algebra.archimedean
import data.real.basic

-- non-empty and bounded -> LUB
definition is_complete (k : Type*) [has_le k] : Prop :=
∀ (S : set k), (∃ x, x ∈ S) → (∃ x, ∀ y ∈ S, y ≤ x) →
  ∃ x, ∀ y, x ≤ y ↔ ∀ z ∈ S, z ≤ y

-- this is already in Lean
theorem real.complete : is_complete ℝ := λ S, real.exists_sup S 

-- have I got this right?
theorem characterisation_of_reals_first_attempt
(k : Type*) [linear_ordered_field k] [archimedean k] :
is_complete k → ∃ f : k → ℝ, function.bijective f ∧ is_ring_hom f := sorry
```
I remember talking about this sort of thing with Patrick and others several months ago. I was teaching this stuff recently and I meant to get around to looking at this, but we ended up doing constructions of the reals via Dedekind cuts and Cauchy sequences and proving basic stuff like existence of floor function and density of rationals in reals from the completeness axiom instead. 

Is this already in mathlib?

