---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32921moreproblemswithcoercions.html
---

## Stream: [general](index.html)
### Topic: [more problems with coercions](32921moreproblemswithcoercions.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958740):
So... I've been trying to implement @**Mario Carneiro**'s suggestion that I define the coercion allowing `F X` for a functor `F` on an object `X`, and define a @[simp] lemma unfolding the coercion.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958750):
I immediately run into trouble, however, where `simp` fails to apply the simp lemma, because a `motive is not correct`:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958756):
Here's my slightly minimised example:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958758):
````
namespace category_theory

universes u v

meta def obviously := `[skip]  

class category (Obj : Type u) : Type (max u (v+1)) :=
(Hom     : Obj → Obj → Type v)
(id      : Π X : Obj, Hom X X)
(comp    : Π {X Y Z : Obj}, Hom X Y → Hom Y Z → Hom X Z)
(id_comp : ∀ {X Y : Obj} (f : Hom X Y), comp (id X) f = f . obviously)
(comp_id : ∀ {X Y : Obj} (f : Hom X Y), comp f (id Y) = f . obviously)
(assoc   : ∀ {W X Y Z : Obj} (f : Hom W X) (g : Hom X Y) (h : Hom Y Z), comp (comp f g) h = comp f (comp g h) . obviously)

notation `𝟙` := category.id -- type as \b1
infixr ` ≫ `:80 := category.comp -- type as \gg
infixr ` ⟶ `:10 := category.Hom -- type as \h

attribute [simp] category.id_comp category.comp_id category.assoc

universes u₁ v₁ u₂ v₂ u₃ v₃

structure Functor (C : Type u₁) [category.{u₁ v₁} C] (D : Type u₂) [category.{u₂ v₂} D] : Type (max u₁ v₁ u₂ v₂) :=
(obj           : C → D)
(map           : Π {X Y : C}, (X ⟶ Y) → ((obj X) ⟶ (obj Y)))
(map_id        : ∀ (X : C), map (𝟙 X) = 𝟙 (obj X) . obviously)
(functoriality : ∀ {X Y Z : C} (f : X ⟶ Y) (g : Y ⟶ Z), map (f ≫ g) = (map f) ≫ (map g) . obviously)

attribute [simp] Functor.map_id Functor.functoriality

infixr ` ↝ `:70 := Functor       -- type as \lea -- unfortunately ⇒ (`\functor`) is taken by core. 

namespace Functor

section
variables {C : Type u₁} [𝒞 : category.{u₁ v₁} C] {D : Type u₂} [𝒟 : category.{u₂ v₂} D]
include 𝒞 𝒟

instance : has_coe_to_fun (C ↝ D) :=
{ F   := λ F, C → D,
  coe := λ F, F.obj }

@[simp] lemma unfold_obj_coercion (F : C ↝ D) (X : C) : F X = F.obj X := by refl
end

section
variables {C : Type u₁} [𝒞 : category.{u₁ v₁} C] {D : Type u₂} [𝒟 : category.{u₂ v₂} D] {E : Type u₃} [ℰ : category.{u₃ v₃} E]
include 𝒞 𝒟 ℰ

set_option trace.check true

definition comp (F : C ↝ D) (G : D ↝ E) : C ↝ E := 
{ obj    := λ X, G (F X),
  map    := λ _ _ f, G.map (F.map f),
  map_id := begin 
             intros, 
             simp, /- why didn't that unfold the coercion? -/
             rw unfold_obj_coercion F X /- oh. -/
            end,
  functoriality := begin intros, simp end }
end

end Functor

end category_theory
````

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958801):
(Being told my motive is not correct always makes me feel very guilty.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958803):
Hopefully I'm just doing something dumb here...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958904):
-----

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 06 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958979):
You have to use `dsimp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 06 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958983):
is there a reason you use `by refl` instead of `rfl` to prove rfl-lemmas?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 06 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958989):
this messes up dsimp

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959028):
ah..

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959029):
I never knew that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959043):
Okay. That should fix my problems, but wow, gross! :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 06 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959047):
You should always prove definitional theorems by `rfl`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 06 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959096):
because lean reads that specially: `A = B := rfl` means `A === B`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959098):
what does `by refl` do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 06 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959100):
It proves the theorem normally, so you just end up learning `A = B`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959101):
surely that's the same thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959109):
but isn't the proof term the same either way?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959111):
I guess I can check.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 06 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959112):
it is, but the literal token `rfl` is used by the lean parser to add the `@[_refl_lemma]` attribute

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 06 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959361):
It really is a pity that `refl` and `rfl` have such important but subtle distinctions, while only differing by one letter.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 06 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959364):
And then `rfl` (without `e`) adds `@[_refl_lemma]` (with `e`)!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 06 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130960266):
to be fair, one is a tactic and one is a term, so they differ by more than one letter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 06 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130960280):
although you shouldn't confuse `rfl` with `eq.refl` either

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 06 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130960327):
similarly there is `iff.rfl` and `iff.refl`, etc. The naming convention has `rfl` have an implicit argument and `refl` has an explicit arg

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Aug 06 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130961287):
Thanks for explaining this `rfl` vs `refl` thing. Switching to `rfl` really helps, both here and elsewhere. :-)


{% endraw %}
