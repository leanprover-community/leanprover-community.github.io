---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/98060idealrestatement.html
---

## Stream: [maths](index.html)
### Topic: [ideal restatement](98060idealrestatement.html)

---


{% raw %}
#### [ Patrick Massot (Sep 29 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ideal%20restatement/near/134885438):
As often, I find myself moving stuff around without doing anything. I just wrote:
```lean
lemma image_subset_iff' {α : Type*} {β : Type*} (f : α → β) (s : set α) (t : set β) :
  f '' s ⊆ t ↔ ∀ a, a ∈ s → f a ∈ t := image_subset_iff
```
which is only restating `f '' s ⊆ t ↔ s ⊆ f ⁻¹' t `in a definitionaly equivalent form, in order to allow rewriting in:
```lean
class is_ideal' {α : Type u} [comm_ring α] (s : set α) : Prop :=
(zero : (0:α) ∈ s)
(add  : (λ p : α × α, p.1 + p.2) ''  set.prod s s ⊆ s)
(mul : ∀ b, (λ s, b*s) '' s ⊆ s)

lemma is_ideal_iff {β : Type*} [comm_ring β] (S : set β) :
 is_ideal S ↔ is_ideal' S :=
begin
  split ; intro h ; haveI := h,
  { split,
    { exact is_ideal.zero S },
    { rintros a ⟨⟨x, y⟩, ⟨x_in, y_in⟩, sum⟩,
      rw ←sum,
      exact is_ideal.add x_in y_in },
    { rintros b s ⟨a, ⟨a_in, prod⟩⟩,
      rw ←prod,
      exact is_ideal.mul_left a_in } },
  { exact { zero_ := h.zero,
      add_ := λ x y x_in y_in, have xy : x + y ∈ (λ (p : β × β), p.fst + p.snd) '' set.prod S S :=
          mem_image_of_mem (λ p : β × β, p.1 + p.2) (mk_mem_prod x_in y_in),
        is_ideal'.add S xy,
      smul := λ b, by rw ←image_subset_iff' ; exact is_ideal'.mul S b }}
end
```
which is restating the definition of an ideal in a functional way, which is suitable for topological reasoning in:
`instance ideal_closure [topological_ring α] (S : set α) [is_ideal S] : is_ideal (closure S)`. Am I doing this right? Should we have a more systematic way of doing such things, or even a tactic (probably transforming the functional form into a pointwise form)?

#### [ Patrick Massot (Sep 29 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ideal%20restatement/near/134885496):
Maybe I should also add the instance proof in order to show why the functional form is useful:
```lean
instance ideal_closure [topological_ring α] (S : set α) [is_ideal S] : is_ideal (closure S) :=
begin
  rcases (is_ideal_iff S).1 (by apply_instance) with ⟨zero, add, mul⟩,
  rw is_ideal_iff,
  split,
  { exact subset_closure zero },
  { rw ←closure_prod_eq,
    exact subset.trans (image_closure_subset_closure_image continuous_add') (closure_mono add) },
  { intro b,
    have : continuous (λ s, b*s) := continuous_mul continuous_const continuous_id,
    exact subset.trans (image_closure_subset_closure_image this) (closure_mono (mul b)) },
end
```

#### [ Patrick Massot (Sep 29 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ideal%20restatement/near/134885537):
By the way, I have no idea why `split` is happy to transform the goal `is_ideal' S` into the expected three goals, but doesn't want to do anything with the goal `is_ideal S`


{% endraw %}
