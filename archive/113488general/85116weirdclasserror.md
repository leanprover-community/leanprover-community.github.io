---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85116weirdclasserror.html
---

## Stream: [general](index.html)
### Topic: [weird class error](85116weirdclasserror.html)

---


{% raw %}
#### [ Reid Barton (Dec 07 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/weird%20class%20error/near/151060003):
```lean
import category_theory.limits.limits
import category_theory.limits.types

universes u v

open category_theory

section
variables (C : Type u) [𝒞 : category.{u v} C] [limits.has_colimits C]
include 𝒞
def is_good : Prop := sorry
lemma is_good_of_has_object (X : C) : is_good C := sorry
end

def MyCat := Type v
instance : category MyCat := by dunfold MyCat; apply_instance
instance : limits.has_colimits.{v+1 v} MyCat := by dunfold MyCat; apply_instance
lemma MyCat_is_good : is_good MyCat.{v} := is_good_of_has_object MyCat.{v} punit.{v+1}

/-
error: failed to synthesize type class instance for
⊢ Π (J : Type v) (𝒥 : small_category J) (F : J ⥤ MyCat), limits.has_colimit F
error: synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  ⁇
inferred
  λ (J : Type v) (𝒥 : small_category J) (F : J ⥤ MyCat), MyCat.category_theory.limits.has_colimits F
-/
```

#### [ Reid Barton (Dec 07 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/weird%20class%20error/near/151060023):
Is my definition
```lean
@[class] def has_colimits :=
Π {J : Type v} {𝒥 : small_category J}, by exactI has_colimits_of_shape J C
```
already asking too much of the class system?

#### [ Reid Barton (Dec 07 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/weird%20class%20error/near/151060658):
Also strange: if I change `has_colimits` to a structure, then I need to add universe annotations to many of its use sites, even if I control for all the variables I'm aware of (same syntactic return universe, both assigned `class` after the fact, both given `elab_simple`)

#### [ Johan Commelin (Dec 07 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/weird%20class%20error/near/151120501):
I think I witnessed similar problems when I tried to get the stuff on presheaves in line with the merged limits PR. But I didn't investigate further.


{% endraw %}
