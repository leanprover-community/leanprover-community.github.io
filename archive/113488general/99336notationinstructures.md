---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99336notationinstructures.html
---

## [general](index.html)
### [notation in structures](99336notationinstructures.html)

#### [Johan Commelin (Jan 22 2019 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation in structures/near/156598822):
Can someone explain me how notation in structures works? Simon changed the definition of a category to:
```lean
class category (obj : Type u) : Type (max u (v+1)) :=
(hom      : obj → obj → Type v)
(infixr ` ⟶ `:10 := hom) -- Interesting!
(id       : Π X : obj, X ⟶ X)
(notation `𝟙` := id)
(comp     : Π {X Y Z : obj}, (X ⟶ Y) → (Y ⟶ Z) → (X ⟶ Z))
(infixr ` ≫ `:80 := comp)
(id_comp' : ∀ {X Y : obj} (f : X ⟶ Y), 𝟙 X ≫ f = f . obviously)
(comp_id' : ∀ {X Y : obj} (f : X ⟶ Y), f ≫ 𝟙 Y = f . obviously)
(assoc'   : ∀ {W X Y Z : obj} (f : W ⟶ X) (g : X ⟶ Y) (h : Y ⟶ Z),
  (f ≫ g) ≫ h = f ≫ (g ≫ h) . obviously)
```
But if I `#print category`, then I don't see this notation being introduced, even though it's still used by the pretty printer.

#### [Reid Barton (Jan 22 2019 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation in structures/near/156598955):
I assumed the notation commands are still logically independent of the structure, they are just interspersed in the file (so that you can use the notation earlier).

#### [Sebastian Ullrich (Jan 22 2019 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation in structures/near/156599043):
Local notations (in sections or structures) are gone completely after parsing. Just like tactic blocks are gone after elaboration.

#### [Johan Commelin (Jan 22 2019 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation in structures/near/156599310):
Ok, so why does the pretty printer use the notation when I ask for `#print category`? Because the notation was reintroduced afterwards?

#### [Sebastian Ullrich (Jan 22 2019 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation in structures/near/156599501):
Ah, yes

#### [Johan Commelin (Jan 22 2019 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation in structures/near/156599516):
Ok, thanks. Everything's cleared up (-;

