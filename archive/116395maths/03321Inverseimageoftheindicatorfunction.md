---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/03321Inverseimageoftheindicatorfunction.html
---

## [maths](index.html)
### [Inverse image of the indicator function](03321Inverseimageoftheindicatorfunction.html)

#### [Koundinya Vajjha (Jan 10 2019 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image of the indicator function/near/154825505):
I'm struggling to get a hold of the inverse image of the indicator function:
```lean 
s : Type u

def indicator (a : set s) [decidable_pred (λ (x:s), x ∈ a)]
:= (λ x : s, if (x ∈ a) then (1:ℝ) else 0) 
```
I want to say that if  $$X = \mathbf{1}_A$$ then $$X^{-1}(B)$$ is one of $$A$$ ,$$ A^c$$, $$\emptyset$$ or $$\emptyset^c$$. 
Any help would be appreciated.

#### [Koundinya Vajjha (Jan 10 2019 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image of the indicator function/near/154825541):
Also, how do I LaTeX?

#### [Johan Commelin (Jan 10 2019 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image of the indicator function/near/154825620):
LaTeX with double dollars: `$$ blah $$`

#### [Joey van Langen (Jan 10 2019 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image of the indicator function/near/154825689):
You can get the inverse image with the symbol ``` ⁻¹' ```, which is \inv ' in lean

#### [Joey van Langen (Jan 10 2019 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image of the indicator function/near/154825717):
It is in mathlib/data/set/basic

#### [Koundinya Vajjha (Jan 10 2019 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image of the indicator function/near/154825808):
Yes I saw that, but I'm not able to state what I want to prove...

#### [Johan Commelin (Jan 10 2019 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image of the indicator function/near/154825867):
What have you tried? Can you give your attempt (+ error?)

#### [Koundinya Vajjha (Jan 10 2019 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image of the indicator function/near/154826020):
```lean
def indicator_inv (a: set s) (b : set ℝ) [decidable_pred (λ (x:s), x ∈ a)] : 
indicator s a ⁻¹'  (b) = { -- what goes here ? }
```

#### [Johan Commelin (Jan 10 2019 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image of the indicator function/near/154826164):
I see. I think you want 4 lemmas

#### [Johan Commelin (Jan 10 2019 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image of the indicator function/near/154826179):
But maybe it depends on why you want this, and how you want to use this.

#### [Joey van Langen (Jan 10 2019 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image of the indicator function/near/154826285):
How about this:
```lean
import data.set.basic
import data.real.basic

universe u

variable (s : Type u)

def indicator (a : set s) [decidable_pred (λ (x:s), x ∈ a)]
:= (λ x : s, if (x ∈ a) then (1:ℝ) else 0)

lemma preimage_indicator (a : set s) [decidable_pred (λ (x:s), x ∈ a)] (b : set ℝ):
(indicator s a) ⁻¹' b = a ∨ (indicator s a) ⁻¹' b = ∅ ∨
(indicator s a) ⁻¹' b = - a ∨ (indicator s a) ⁻¹' b = -∅ :=
sorry
```

#### [Koundinya Vajjha (Jan 10 2019 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image of the indicator function/near/154826344):
I'm trying to prove that the indicator function of an event is a random variable.

``` lean
def is_random_variable {s : Type u} [measurable_space s] (X : s → ℝ) := measurable X


lemma is_random_variable_indicator (a : set s) [decidable_eq (set s)] [decidable_pred (λ (x:s), x ∈ a)]:  
is_random_variable (indicator _ a) :=
begin
intros b h, 
unfold measurable_space.map,
unfold set.preimage, dsimp, 
sorry
end
```

#### [Koundinya Vajjha (Jan 10 2019 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image of the indicator function/near/154826454):
I'm stuck at 

```lean 
s : Type u,
_inst_1 : measurable_space s,
a : set s,
_inst_2 : decidable_eq (set s),
_inst_3 : decidable_pred (λ (x : s), x ∈ a),
b : set ℝ,
h : measurable_space.is_measurable (measure_theory.borel ℝ) b
⊢ measurable_space.is_measurable _inst_1 {x : s | indicator s a x ∈ b}
```

#### [Koundinya Vajjha (Jan 10 2019 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image of the indicator function/near/154826480):
I want to prove a lemma which would possibly rewrite the `{x : s | indicator s a x ∈ b}` maybe...

#### [Koundinya Vajjha (Jan 10 2019 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image of the indicator function/near/154826609):
@**Joey van Langen**  thanks I'll try that.

