---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/30267morelimitstuff.html
---

## Stream: [maths](index.html)
### Topic: [more limit stuff](30267morelimitstuff.html)

---


{% raw %}
#### [ Johan Commelin (Dec 17 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more%20limit%20stuff/near/151910753):
I've got the following lemmas
```lean
lemma colimit.pre_map {K : Type v} [small_category K] [has_colimits_of_shape.{u v} K C]
  (F : J ⥤ C) {E₁ E₂ : K ⥤ J} (α : E₁ ⟹ E₂) :
  colimit.pre F E₁ = colim.map (whisker_right α F) ≫ colimit.pre F E₂ :=
begin
  ext1, dsimp,
  conv {to_rhs, rw ←category.assoc},
  simp,
end

lemma colimit.pre_id (F : J ⥤ C) :
colimit.pre F (functor.id _) = colim.map (functor.left_unitor F).hom := by tidy

lemma colimit.pre_comp
{K : Type v} [small_category K] [has_colimits_of_shape.{u v} K C]
{L : Type v} [small_category L] [has_colimits_of_shape.{u v} L C]
(F : J ⥤ C) (E : K ⥤ J) (D : L ⥤ K) :
colimit.pre F (D ⋙ E) = colim.map (functor.associator D E F).hom
≫ colimit.pre _ D ≫ colimit.pre F E :=
begin
  tidy {trace_result := tt},
  erw ← category.assoc,
  erw colim_ι_map (functor.associator D E F).hom j,
  dsimp [functor.associator],
  simp,
  erw is_colimit.fac,
  refl
end
```
Should I put these (and their duals) into a new PR? Or should this be cast into some other form first?

#### [ Reid Barton (Dec 17 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more%20limit%20stuff/near/151911327):
Isn't the third one `colimit.pre_pre`?

#### [ Reid Barton (Dec 17 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more%20limit%20stuff/near/151911330):
Oh I missed the actual second one.

#### [ Reid Barton (Dec 17 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more%20limit%20stuff/near/151911339):
The associator is a definitional equality, so you don't really need it.

#### [ Reid Barton (Dec 17 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more%20limit%20stuff/near/151911403):
Though sometimes Lean tries to be too smart, and gets confused by the reassociation unless you spell things out for it.

#### [ Johan Commelin (Dec 17 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/more%20limit%20stuff/near/152007178):
Aah, I see. So the third one can go. That leaves the other 2.


{% endraw %}
