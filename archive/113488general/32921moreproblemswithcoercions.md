---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32921moreproblemswithcoercions.html
---

## Stream: [general](index.html)
### Topic: [more problems with coercions](32921moreproblemswithcoercions.html)

---


{% raw %}
#### [ Scott Morrison (Aug 06 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958740):
<p>So... I've been trying to implement <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>'s suggestion that I define the coercion allowing <code>F X</code> for a functor <code>F</code> on an object <code>X</code>, and define a @[simp] lemma unfolding the coercion.</p>

#### [ Scott Morrison (Aug 06 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958750):
<p>I immediately run into trouble, however, where <code>simp</code> fails to apply the simp lemma, because a <code>motive is not correct</code>:</p>

#### [ Scott Morrison (Aug 06 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958756):
<p>Here's my slightly minimised example:</p>

#### [ Scott Morrison (Aug 06 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958758):
<div class="codehilite"><pre><span></span>namespace category_theory

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
             simp, /- why didn&#39;t that unfold the coercion? -/
             rw unfold_obj_coercion F X /- oh. -/
            end,
  functoriality := begin intros, simp end }
end

end Functor

end category_theory
</pre></div>

#### [ Scott Morrison (Aug 06 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958801):
<p>(Being told my motive is not correct always makes me feel very guilty.)</p>

#### [ Scott Morrison (Aug 06 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958803):
<p>Hopefully I'm just doing something dumb here...</p>

#### [ Scott Morrison (Aug 06 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958904):
<hr>

#### [ Mario Carneiro (Aug 06 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958979):
<p>You have to use <code>dsimp</code></p>

#### [ Mario Carneiro (Aug 06 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958983):
<p>is there a reason you use <code>by refl</code> instead of <code>rfl</code> to prove rfl-lemmas?</p>

#### [ Mario Carneiro (Aug 06 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130958989):
<p>this messes up dsimp</p>

#### [ Scott Morrison (Aug 06 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959028):
<p>ah..</p>

#### [ Scott Morrison (Aug 06 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959029):
<p>I never knew that.</p>

#### [ Scott Morrison (Aug 06 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959043):
<p>Okay. That should fix my problems, but wow, gross! :-)</p>

#### [ Mario Carneiro (Aug 06 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959047):
<p>You should always prove definitional theorems by <code>rfl</code></p>

#### [ Mario Carneiro (Aug 06 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959096):
<p>because lean reads that specially: <code>A = B := rfl</code> means <code>A === B</code></p>

#### [ Scott Morrison (Aug 06 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959098):
<p>what does <code>by refl</code> do?</p>

#### [ Mario Carneiro (Aug 06 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959100):
<p>It proves the theorem normally, so you just end up learning <code>A = B</code></p>

#### [ Scott Morrison (Aug 06 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959101):
<p>surely that's the same thing</p>

#### [ Scott Morrison (Aug 06 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959109):
<p>but isn't the proof term the same either way?</p>

#### [ Scott Morrison (Aug 06 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959111):
<p>I guess I can check.</p>

#### [ Mario Carneiro (Aug 06 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959112):
<p>it is, but the literal token <code>rfl</code> is used by the lean parser to add the <code>@[_refl_lemma]</code> attribute</p>

#### [ Johan Commelin (Aug 06 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959361):
<p>It really is a pity that <code>refl</code> and <code>rfl</code> have such important but subtle distinctions, while only differing by one letter.</p>

#### [ Johan Commelin (Aug 06 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130959364):
<p>And then <code>rfl</code> (without <code>e</code>) adds <code>@[_refl_lemma]</code> (with <code>e</code>)!</p>

#### [ Mario Carneiro (Aug 06 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130960266):
<p>to be fair, one is a tactic and one is a term, so they differ by more than one letter</p>

#### [ Mario Carneiro (Aug 06 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130960280):
<p>although you shouldn't confuse <code>rfl</code> with <code>eq.refl</code> either</p>

#### [ Mario Carneiro (Aug 06 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130960327):
<p>similarly there is <code>iff.rfl</code> and <code>iff.refl</code>, etc. The naming convention has <code>rfl</code> have an implicit argument and <code>refl</code> has an explicit arg</p>

#### [ Scott Morrison (Aug 06 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20problems%20with%20coercions/near/130961287):
<p>Thanks for explaining this <code>rfl</code> vs <code>refl</code> thing. Switching to <code>rfl</code> really helps, both here and elsewhere. :-)</p>


{% endraw %}
