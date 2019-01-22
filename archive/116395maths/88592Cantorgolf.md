---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/88592Cantorgolf.html
---

## [maths](index.html)
### [Cantor golf](88592Cantorgolf.html)

#### [Kevin Buzzard (Dec 12 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151537525):
1) Is there a very short proof of this in Lean / mathlib?

```lean
example (X : Type) (x : X) (f : X → set X) (H : x ∈ f x ↔ x ∉ f x) : false := sorry
```

2) Can anyone golf the mathlib proof of Cantor's Diagonal Argument (using only imports in mathlib):

```lean
theorem cantor_surjective {α} (f : α → α → Prop) : ¬ function.surjective f | h :=
let ⟨D, e⟩ := h (λ a, ¬ f a a) in
(iff_not_self (f D D)).1 $ iff_of_eq (congr_fun e D)
```

#### [Rob Lewis (Dec 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151537662):
For 1), `by tauto!`It shouldn't need classical logic but `by tauto` fails.

#### [Kevin Buzzard (Dec 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151537663):
My answer to (1):

```lean
example (X : Type) (x : X) (f : X → set X) (H : x ∈ f x ↔ x ∉ f x) : false :=
begin
  revert H,
  generalize : x ∈ f x = p,
  cc  
end
```

I'm sure something much better will exist.

#### [Kevin Buzzard (Dec 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151537700):
...and indeed it existed before I even posted! Many thanks Rob!

#### [Kevin Buzzard (Dec 12 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151538379):
Why my code no work?

```lean
import tactic.interactive

open function

theorem no_bijection_to_power_set'
  (X : Type)
  (f : X → set X) :
bijective f → false :=
λ ⟨Hi, Hs⟩, -- unexpected occurrence of recursive function error
begin
  cases Hs {x : X | x ∉ f x} with x Hx,
    have Hconclusion_so_far : x ∈ f x ↔ x ∈ _ := by rw [Hx],
      have Hlogical_nonsense : (x ∈ f x) ↔ ¬ (x ∈ f x) := Hconclusion_so_far,
  tauto!
end
```

#### [Kevin Buzzard (Dec 12 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151538702):
Changing `tauto!` to `sorry` fixes the error. Is it a combination of the equation compiler and the tactic? Why is this happening?

#### [Kevin Buzzard (Dec 12 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151538742):
```lean
import tactic.interactive

open function

theorem no_bijection_to_power_set'
  (X : Type)
  (f : X → set X) :
bijective f → false :=
λ Hb, let ⟨Hi,Hs⟩ := Hb in -- unexpected occurrence of recursive function
begin
  cases Hs {x : X | x ∉ f x} with x Hx,
    have Hconclusion_so_far : x ∈ f x ↔ x ∈ _ := by rw [Hx],
      have Hlogical_nonsense : (x ∈ f x) ↔ ¬ (x ∈ f x) := Hconclusion_so_far,
  tauto!
end
```

Also doesn't work.

#### [Reid Barton (Dec 12 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151538747):
For some reason using lambda with pattern matching like this makes a hypothesis (I think it's called `_fun_match`) which I guess represents some kind of recursion

#### [Reid Barton (Dec 12 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151538832):
if you use a tactic which tries to apply everything like `tauto`, it'll try to apply `_fun_match` and then you get this error

#### [Reid Barton (Dec 12 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151538880):
Same with let but I think the hypothesis name is different

#### [Reid Barton (Dec 12 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151538901):
You could use `begin rintros \<Hi,Hs\>, cases ...`

#### [Kevin Buzzard (Dec 12 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151541033):
I was trying to get out of tactic mode, on this occasion.

#### [Kevin Buzzard (Dec 12 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151541245):
Here's the game. I have a version of Cantor's theorem in Lean, spelt out so that mathematicians with epsilon Lean experience can still understand it:

```lean
-- Cantor's theorem in Lean

import tactic.interactive

open function

/- Theorem: If X is any type, then there is no bijective function
   f from X to the power set of X.
-/
theorem no_bijection_to_power_set (X : Type) :
∀ f : X → set X, ¬ (bijective f) :=
begin
  -- Let f be a function from X to the power set of X
  intro f,
  -- Assume, for a contradiction, that f is bijective
  intro Hf,
  -- f is bijective, so it's surjective.
  cases Hf with Hi Hs,
  -- it's also injective, but I don't even care
  clear Hi,
  -- Let S be the usual cunning set
  let S : set X := {x : X | x ∉ f x},
  -- What does surjectivity of f say when applied to S?
  have HCantor := Hs S,
  -- It tells us that there's x in X with f x = S!
  cases HCantor with x Hx,
  -- That means x is in f x if and only if x has is in S.
  have Hconclusion_so_far : x ∈ f x ↔ x ∈ S := by rw [Hx],
  -- but this means (x ∈ f x) ↔ ¬ (x ∈ f x)
  have Hlogical_nonsense : (x ∈ f x) ↔ ¬ (x ∈ f x) := Hconclusion_so_far,
  -- automation can now take over.
  tauto!,
end
```

and I was trying to compress it into a term mode function.

I also have the mathlib proof

```lean
import tactic.interactive

theorem cantor_surjective {α} (f : α → α → Prop) : ¬ function.surjective f | h :=
let ⟨D, e⟩ := h (λ a, ¬ f a a) in
(iff_not_self (f D D)).1 $ iff_of_eq (congr_fun e D)
```

and I was attempting to expand this into a tactic mode proof. I could just use rcases, as you say.

#### [Rob Lewis (Dec 12 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cantor%20golf/near/151551702):
You can use `simpa using Hlogical_nonsense` to avoid the weird `tauto` behavior, but I guess it doesn't look quite as good when you have to name the hypothesis.

