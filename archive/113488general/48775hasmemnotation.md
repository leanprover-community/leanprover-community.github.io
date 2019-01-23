---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48775hasmemnotation.html
---

## Stream: [general](index.html)
### Topic: [has_mem notation](48775hasmemnotation.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20notation/near/155075639):
{% raw %}
Does anyone know how to fix this notation hack?
```lean
def covering_family {X : Type u} [category.{v} X] (U : X) : Type (max u v) :=
Π {{V}}, set (V ⟶ U)

local notation a `∈`:50 b:50 := b a -- Aaahrg!

structure coverage (X : Type u) [category.{v} X] :=
(covers   : Π (U : X), set (covering_family U))
(property : ∀ {U V : X} (g : V ⟶ U),
            ∀ f ∈ covers U, ∃ h ∈ covers V,
            ∀ Vj (k : Vj ⟶ V), k ∈ h →
            ∃ Ui (l : Ui ⟶ U), l ∈ f ∧ ∃ m : Vj ⟶ Ui, m ≫ l = k ≫ g)
```{% endraw %}

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20notation/near/155075643):
Ooh, and here is the relevant top of the file
```lean
import category_theory.presheaf
import category_theory.comma
import category_theory.full_subcategory
import analysis.topology.topological_space
import category_theory.examples.topological_spaces
import tactic.where

universes v u

namespace category_theory
open category_theory
open category_theory.limits
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 14 2019 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20notation/near/155075774):
Could you do a `has_mem` instance instead?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_mem%20notation/near/155077701):
No, I don't think `has_mem` works. I want to say that `f : V ⟶ U` is a member of `c`. But the type of `f` depends on `V`, which ranges over all of `X`.

