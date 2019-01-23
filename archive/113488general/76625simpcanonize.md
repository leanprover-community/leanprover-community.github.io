---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/76625simpcanonize.html
---

## Stream: [general](index.html)
### Topic: [simp canonize](76625simpcanonize.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jan 22 2019 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20canonize/near/156622369):
I'm trying to get rid of some simp loops and I just realized that there is a part of it I don't understand and it seems to be getting into a loop. Here is the trace that Lean prints for it:

```
[simplify.canonize] 
category_theory.types
==>
category_theory.types
[simplify.canonize] 
category_theory.types
==>
category_theory.types
[simplify.canonize] 
_inst_2
==>
_inst_2
[simplify.canonize] 
category_theory.types
==>
category_theory.types
[simplify.canonize] 
category_theory.types
==>
category_theory.types
[simplify.canonize] 
_inst_2
==>
_inst_2
```

How do I prevent it from looping? I tried `simp [-category_theory.types]` and it doesn't work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 22 2019 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20canonize/near/156622930):
But `category_theory.types` isn't even marked as `[simp]`. How come the simplifier is using it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jan 22 2019 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20canonize/near/156627682):
I am puzzled too. My tentative answer is that it comes from the `canonize` phase of `simp` which I did not know of. It seems like a phase where class instances are reduced but I can't say more. @**Sebastian Ullrich**, would you care to enlighten us?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jan 22 2019 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20canonize/near/156638222):
Update: using `set_option trace.debug.dsimplify true` and using `dsimp` instead of `simp`, I managed to find the offender which was unrelated to `canonize`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20canonize/near/156643964):
MWE

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jan 23 2019 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20canonize/near/156649250):
```lean

import category_theory.category
import category_theory.types

universes u

class comonad (w : Type u → Type u)
extends functor w :=
(extract : Π {α}, w α → α)
(extend : Π {α β}, (w α → β) → w α → w β)

def Cokleisli (m) [comonad.{u} m] := Type u

open category_theory comonad
instance {m} [comonad.{u} m] : category.{u} (Cokleisli m) := sorry

def copipe {w α β γ} [comonad w] (f : w α → β) (g : w β → γ) : (w α → γ) :=
g ∘ extend f

infix ` =>= `:55 := copipe

instance Cokleisli.category {m} [comonad m] : category (Cokleisli.{u} m) :=
{ hom := λ α β, m α → β,
  id := λ α, extract,
  comp := λ X Y Z f g, f =>= g,
  id_comp' := sorry,
  comp_id' := sorry,
  assoc' := sorry }

@[simp] lemma Cokleisli.comp_def {m : Type* → Type*} [comonad m] (α β γ : Cokleisli m)
  (xs : α ⟶ β) (ys : β ⟶ γ) :
  xs ≫ ys = xs =>= ys := sorry

variables {α β : Type u}

example {m} [comonad m] (f : α ⟶ m α) (g : m α ⟶ α) : f ≫ g = 𝟙 _ :=
by { simp, }
-- deep recursion was detected at 'expression replacer' (potential
-- solution: increase stack space in your system)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jan 23 2019 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20canonize/near/156649296):
If you comment out `Cokleisli.comp_def`, the error disappears


{% endraw %}
