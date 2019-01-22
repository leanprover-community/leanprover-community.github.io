---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58237equivalencerelationonwrongtype.html
---

## [general](index.html)
### [equivalence relation on wrong type](58237equivalencerelationonwrongtype.html)

#### [Kevin Buzzard (Aug 10 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equivalence%20relation%20on%20wrong%20type/near/131202972):
Luca defined an equivalence relation (homotopy equivalence) on `path x y`, the paths from x to y in a topological space. He defined `loop x` to be `path x x` and then wanted to define `pi_1` to be the equivalence classes. Lean seemed to obstinately refuse to put the equivalence relation on `loop x`, insisting it was on `path x x`. Here's some code that doesn't run, plus some commented out code which fixes the problem.

```lean
variable {α  : Type*}

def path : α → α → Type := sorry
def comp_of_path {x y z : α} : path x y → path y z → path x z := sorry
def is_homotopic_to (x y : α) : path x y → path x y → Prop := sorry
definition is_equivalence (x y : α) : equivalence (is_homotopic_to x y) := sorry
definition loop (x : α) := path x x


/-
-- This fixes the problem below -- is it safe to have both instances floating around?

instance setoid_hom_path (x : α)  : 
setoid (path x x) := setoid.mk (is_homotopic_to x x) (is_equivalence x x)
  
instance setoid_hom_loop (x : α) : 
setoid (loop x) := by unfold loop; apply_instance
-/

instance setoid_hom_loop (x : α)  : 
setoid (loop x) := setoid.mk (is_homotopic_to x x : loop x → loop x → Prop)
  (is_equivalence x x : equivalence (is_homotopic_to x x : loop x → loop x → Prop))

def space_π_1 (x : α) := 
quotient (setoid_hom_loop x : setoid (loop x))

-- error here
def mul {x : α}  : 
space_π_1 x → space_π_1 x → space_π_1 x := 
quotient.lift₂ (λ f g : loop x, ⟦((comp_of_path (f : loop x) (g : loop x)) : loop x)⟧) sorry
/-
-- error is on ⟦ and it's

failed to synthesize type class instance for
α : Type u_1,
x : α,
f g : loop x
⊢ setoid (path x x)
-/

```

I tell Lean so many times that we're talking about `loop x` but the error seems to indicate that whilst I beg Lean to believe that `comp_of_path f g` has type `loop x`, it complains that `path x x` is not a setoid.

So I found a fix -- instead of making one instance I make two -- I make an instance on `path x x` and then deduce one on `loop x`. I am not sure what's going on here and in some sense I'm now not even sure which of the equivalence relations I'm even using. Does it matter that I now have two instances? Why can't I just get away with my uncommented approach?

#### [Simon Hudon (Aug 10 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equivalence%20relation%20on%20wrong%20type/near/131203664):
I think the problem is that `((comp_of_path (f : loop x) (g : loop x)) : loop x)` does not have type `loop x` because `comp_of_path` does not have type `loop x`.  The `(_ : _)` notation does not change the type of the expression, it only provides hints to fill in gaps in the type information.

#### [Simon Hudon (Aug 10 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equivalence%20relation%20on%20wrong%20type/near/131203723):
The only alternative I can see to the two instances solution is to create a coercion function. I think I like your solution better. You could make it only one instance (on `path x x` if you made `loop` reducible.

#### [Chris Hughes (Aug 10 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equivalence%20relation%20on%20wrong%20type/near/131203885):
This also works 
```lean
def mul {x : α} : space_π_1 x → space_π_1 x → space_π_1 x :=
quotient.lift₂ (λ f g, show space_π_1 x, from ⟦comp_of_path f g⟧) 
sorry
```

#### [Simon Hudon (Aug 10 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equivalence%20relation%20on%20wrong%20type/near/131203956):
Ah! That's true! So this probably works as well: 
```lean
(⟦(comp_of_path (f : loop x) (g : loop x))⟧ : space_π_1 x)
```

#### [Chris Hughes (Aug 10 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equivalence%20relation%20on%20wrong%20type/near/131204005):
yes it does, much more sensible

#### [Kevin Buzzard (Aug 10 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equivalence%20relation%20on%20wrong%20type/near/131230021):
But Luca would then have to write that all through his code, which kind of stinks -- I wanted him to use type class inference precisely because it was supposed to be making his life easier.

