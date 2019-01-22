---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/80189weirdtypeclassissue.html
---

## [maths](index.html)
### [weird type class issue](80189weirdtypeclassissue.html)

#### [Johan Commelin (Oct 18 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136026131):
Consider this code:
```lean
import category_theory.category

open category_theory

universes u u₁ u₂ v v₁ v₂ w w₁ w₂

variables {C : Type u₁} [𝒞 : category.{u₁ u₂} C] --[@has_limits.{u₁ u₂} C 𝒞]
include 𝒞

-- todo should this be done as a subfunctor?
structure covering_family (U : C) :=
(I : Type u₂)
(obj : I → C)
(hom : Π {i : I}, obj i ⟶ U)

#print covering_family

structure coverage :=
(covers : Π {U : C}, set (covering_family U)) -- red squiggles under "covering_family"
```
I get the following error:
```lean
failed to synthesize type class instance for
C : Type u₁,
𝒞 : category C,
C : Type u₁,
𝒞 : category C,
U : C
⊢ category C
```

#### [Johan Commelin (Oct 18 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136026148):
Why are `C` and the category structure duplicated there? And why can't it resolve the type class issue?

#### [Johannes Hölzl (Oct 18 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136026219):
what happens if you remove the `include` and write the variables directly as parameters for `coverage`?

#### [Johan Commelin (Oct 18 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136026236):
These includes are all over the place in Scott's library. If you remove it you get red squiggles under the `⟶` in `obj i ⟶ U`.

#### [Johan Commelin (Oct 18 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136026298):
```lean
def coverage := Π {U : C}, set (covering_family U)
```
gives the error
```lean
failed to synthesize type class instance for
C : Type u₁,
𝒞 : category C,
U : C
⊢ category C
```
So now the duplication is gone. But it still can't resolve the type class...

#### [Johan Commelin (Oct 18 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136026368):
The following works but is very ugly.
```lean
def coverage := Π {U : C}, set (@covering_family _ 𝒞 U)
```

#### [Johan Commelin (Oct 18 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136034898):
In general I think the fact that we need `include 𝒞` all the time is a sign that something is wrong. But I have no clue what is wrong and how to fix it.

#### [Reid Barton (Oct 18 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136039835):
I usually include the universe parameters when I run into this kind of issue, like `covering_family.{u\1 u\2}`. (BTW, usually we use a `v`-type letter for the morphism universe.)
I have no idea about the duplicate display in the error message though.

#### [Johan Commelin (Oct 18 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136040495):
I currently have
```lean
import category_theory.examples.topological_spaces
import category_theory.opposites
import category_theory.yoneda
import category_theory.limits.equalizers
import category_theory.limits.products

open category_theory

universes u u₁ u₂ v v₁ v₂ w w₁ w₂

namespace category_theory.limits
variables {C : Type u₁} [𝒞 : category.{u₁ u₂} C]
include 𝒞

variables [has_coequalizers.{u₁ u₂} C] {Y Z : C} (f g : Y ⟶ Z)

def coequalizer.cofork := has_coequalizers.coequalizer.{u₁ u₂} f g
def coequalizer := (coequalizer.cofork f g).X
def coequalizer.π : Z ⟶ (coequalizer f g) := (coequalizer.cofork f g).π
@[search] def coequalizer.w : f ≫ (coequalizer.π f g) = g ≫ (coequalizer.π f g) := (coequalizer.cofork f g).w
def coequalizer.universal_property : is_coequalizer (coequalizer.cofork f g) :=
has_coequalizers.is_coequalizer.{u₁ u₂} C f g

def coequalizer.desc (P : C) (h : Z ⟶ P) (w : f ≫ h = g ≫ h) : coequalizer f g ⟶ P :=
(coequalizer.universal_property f g).desc { X := P, π := h, w := w }

@[extensionality] lemma coequalizer.hom_ext {Y Z : C} {f g : Y ⟶ Z} {X : C}
(h k : coequalizer f g ⟶ X) (w : coequalizer.π f g ≫ h = coequalizer.π f g ≫ k) : h = k :=
begin
  let s : cofork f g := ⟨ ⟨ X ⟩, coequalizer.π f g ≫ h ⟩,
  have q := (coequalizer.universal_property f g).uniq s h,
  have p := (coequalizer.universal_property f g).uniq s k,
  rw [q, ←p],
  solve_by_elim, refl
end

end category_theory.limits

section presheaf
open category_theory.limits
variables (X : Type u₁) [𝒳 : category.{u₁ v₁} X] (C : Type u₂) [𝒞 : category.{u₂ v₂} C]
include 𝒳 𝒞

def presheaf := Xᵒᵖ ⥤ C

variables {X} {C}

instance : category (presheaf X C) := by unfold presheaf; apply_instance

omit 𝒞
instance : has_coproducts (presheaf X (Type v₂)) := sorry

#print presheaf.category_theory.category

end presheaf

-- todo should this be done as a subfunctor?
structure covering_family {X : Type u₁} [category.{u₁ v₁} X] (U : X) :=
(index : Type v₁)
(obj : index → X)
(hom : Π (i : index), obj i ⟶ U)

namespace covering_family
open category_theory.limits
variables {X : Type u₁} [𝒳 : category.{u₁ v₁} X]
include 𝒳

variables {U : X}

def sieve (f : covering_family U) : presheaf X (Type v₁) :=
@coequalizer _ _ (sorry)
(@Sigma _ _ _ (f.index × f.index) (λ p, _))
(@Sigma _ _ _ f.index (((yoneda X) : X → presheaf X (Type v₁)) ∘ f.obj))
_ _

def sheaf_condition (f : (covering_family U)) {C : Type u₂} [category.{u₂ v₂} C] (F : presheaf X C) : Prop := sorry

end covering_family

structure coverage {X : Type u₁} [category.{u₁ u₂} X] :=
(covers   : Π (U : X), set (covering_family U))
(property : ∀ {U V : X} (g : V ⟶ U) (f : (covering_family U)),
            ∃ h : (covering_family V), ∀ j : h.index, ∃ {i : f.index} {k : h.obj j ⟶ f.obj i},
            h.hom j ≫ g = k ≫ f.hom i)

class site (X : Type u₁) extends category.{u₁ u₂} X :=
(coverage : @coverage X (by assumption))

section sheaf
variables (X : Type u₁) [𝒳 : site.{u₁ v₁} X] (C : Type u₂) [𝒞 : category.{u₂ v₂} C]
include 𝒳 𝒞

structure sheaf :=
(presheaf : presheaf X C)
(sheaf_condition : ∀ {U : X} (f : (@covering_family _ 𝒳.to_category U)), f.sheaf_condition presheaf)

end sheaf



namespace topological_space

variables {X : Type u} [topological_space X]

instance : site (opens X) :=
{ coverage :=
  { covers := λ U, λ Us, begin sorry -- the union of the Ui should be U
    end,
    property := sorry } }

end topological_space
```
Lean is especially unhappy about the part where I try to define the `sieve`.

#### [Johan Commelin (Oct 18 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136040514):
Currently I'm just going to wait till some PR's get merged.

#### [Reid Barton (Oct 18 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136041150):
Lots of those `_`s in sieve still need to be filled in, right?

#### [Reid Barton (Oct 18 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136041176):
Or at least... 3 I guess?

#### [Johan Commelin (Oct 18 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136041777):
Yes, that is right. But I need fibre products for the for the `_` in the first `Sigma`. :sad:

#### [Reid Barton (Oct 18 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136043495):
```quote
In general I think the fact that we need `include 𝒞` all the time is a sign that something is wrong. But I have no clue what is wrong and how to fix it.
```
So there are two issues which come up a lot due to the way category theory uses universe variables.
1. The `include 𝒞` thing is a workaround for a specific elaborator bug where it doesn't correctly account for universe parameters of variables that have been included by the "square bracket rule". If you hit this bug then you will see an error about something like "bad tactic or buggy elaborator".
2. It also often happens that you have to help Lean out with some explicit universe parameters. I think what is going on is that one of the parameters is not constrained by anything (usually the `v`), and so Lean is looking for a `category.{u ?u_1} C` instance. Apparently it's unwilling to take an instance `category.{u v} C` for some specific `v` and specialize `?u_1` to `v`. I'm not sure whether this is a bug or just something where the system doesn't work in the way we would usually prefer.

#### [Johan Commelin (Oct 18 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136043564):
I see. I wouldn't mind if universe unification was slightly more greedy in this case.

#### [Reid Barton (Oct 18 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136043615):
Your `covering_family` thing is the second issue.

#### [Reid Barton (Oct 18 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136043903):
Maybe we would like to have something like `out_param` on the universe parameter `v`, but that's not currently possible

#### [Reid Barton (Oct 18 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136043980):
Also I don't really understand how `out_param` works, so I could be way off-base.

#### [Reid Barton (Oct 18 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136044517):
Maybe the clearest example of this is something like `terminal_object (C : Type u) [category.{u v} C] [has_terminal_object.{u v} C] : C` where you could have a type `C : Type u` equipped with two totally different `category.{u v}` and `category.{u w}` structures with different terminal objects. The type of `terminal_object C` is just `C` which has `Type u` so there is no way you could ever constrain the `v` parameter.

#### [Johan Commelin (Oct 19 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136107468):
The issues aren't gone, but my definition of `sieve` is converging onto something far more readable then I had before:
```lean
import category_theory.examples.topological_spaces
import category_theory.opposites
import category_theory.yoneda
import category_theory.limits

open category_theory

universes u u₁ u₂ v v₁ v₂ w w₁ w₂

namespace category_theory.limits
variables {C : Type u₁} [𝒞 : category.{u₁ u₂} C]
include 𝒞

variables [has_coequalizers.{u₁ u₂} C] {Y Z : C} (f g : Y ⟶ Z)

def coequalizer.cofork := has_coequalizers.coequalizer.{u₁ u₂} f g
def coequalizer := (coequalizer.cofork f g).X
def coequalizer.π : Z ⟶ (coequalizer f g) := (coequalizer.cofork f g).π
@[search] def coequalizer.w : f ≫ (coequalizer.π f g) = g ≫ (coequalizer.π f g) := (coequalizer.cofork f g).w
def coequalizer.universal_property : is_coequalizer (coequalizer.cofork f g) :=
has_coequalizers.is_coequalizer.{u₁ u₂} C f g

def coequalizer.desc (P : C) (h : Z ⟶ P) (w : f ≫ h = g ≫ h) : coequalizer f g ⟶ P :=
(coequalizer.universal_property f g).desc { X := P, π := h, w := w }

@[extensionality] lemma coequalizer.hom_ext {Y Z : C} {f g : Y ⟶ Z} {X : C}
(h k : coequalizer f g ⟶ X) (w : coequalizer.π f g ≫ h = coequalizer.π f g ≫ k) : h = k :=
begin
  let s : cofork f g := ⟨ ⟨ X ⟩, coequalizer.π f g ≫ h ⟩,
  have q := (coequalizer.universal_property f g).uniq s h,
  have p := (coequalizer.universal_property f g).uniq s k,
  rw [q, ←p],
  solve_by_elim, refl
end

end category_theory.limits

section presheaf
open category_theory.limits
variables (X : Type u₁) [𝒳 : category.{u₁ v₁} X] (C : Type u₂) [𝒞 : category.{u₂ v₂} C]
include 𝒳 𝒞

def presheaf := Xᵒᵖ ⥤ C

variables {X} {C}

instance : category (presheaf X C) := by unfold presheaf; apply_instance

omit 𝒞
instance presheaf.has_coequalizers : @has_coequalizers (presheaf X (Type v₁)) presheaf.category_theory.category := sorry
instance presheaf.has_coproducts : @has_coproducts (presheaf X (Type v₁)) presheaf.category_theory.category := sorry
instance presheaf.has_pullbacks : @has_pullbacks (presheaf X (Type v₁)) presheaf.category_theory.category := sorry

end presheaf

-- todo should this be done as a subfunctor?
structure covering_family {X : Type u₁} [category.{u₁ v₁} X] (U : X) :=
(index : Type v₁)
(obj : index → X)
(map : Π (i : index), obj i ⟶ U)

namespace covering_family
open category_theory.limits
variables {X : Type u₁} [𝒳 : category.{u₁ v₁} X]
include 𝒳

variables {U : X}

def sieve (f : covering_family U) : presheaf X (Type v₁) :=
let CP := (((yoneda X) : X → presheaf X (Type v₁)) ∘ f.obj) in
coequalizer
  (Sigma.desc (λ p : (f.index × f.index), (Sigma.ι CP p.1) ∘ (pullback.π₁ ((yoneda X).map (f.map p.1)) ((yoneda X).map (f.map p.2)))))
  (Sigma.desc (λ p : (f.index × f.index), (Sigma.ι CP p.2) ∘ (pullback.π₂ ((yoneda X).map (f.map p.1)) ((yoneda X).map (f.map p.2)))))

def sheaf_condition (f : (covering_family U)) {C : Type u₂} [category.{u₂ v₂} C] (F : presheaf X C) : Prop := sorry

end covering_family
```

#### [Johan Commelin (Oct 19 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/weird type class issue/near/136107519):
But there are still a lot of typeclass issues.

