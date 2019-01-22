---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/179818LeanTogether2019/30286derivativeAPI.html
---

## [Lean Together 2019](index.html)
### [derivative API](30286derivativeAPI.html)

#### [Kevin Buzzard (Jan 09 2019 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean Together 2019/topic/derivative API/near/154710820):
@**Assia Mahboubi** and @**Cyril Cohen** both were concerned about a stylistic issue which came up in Mario's live coding session. We were looking at differentiating bounded linear maps, but my understanding of the issue (which is generally poor) is that it would apply equally if we were just talking about differentiating functions `f: ℝ → ℝ`. So say `f` and `g` are functions from the reals to the reals. Let's define `V` to be the type of these functions.

My memory of the situation was that Mario defined something like `is_deriv : V -> V -> Prop`, where `is_deriv f g` was the statement that `g` was the derivative of `f`. As an initial definition this is a good first step; mathematicians would often define a partial function `V -> V` which eats an `f`if it is differentiable, and spits out "the" derivative. I write "the" in quotes because we have not even proved yet that a function has at most one derivative. But Lean is not a big fan of partial functions so my instinct (which has very much been honed by Mario) would be to use `is_deriv` as our foundational thing and then go from there.

My memory is that the interesting thing happened when Mario formalised the statement of the chain rule. Oh -- heh -- it just occurs to me that I don't have to rely on memory, because he wrote the code on my laptop :-) 

```
  (h₁ : is_deriv f x L₁)
  (h₂ : is_deriv g (f x) L₂) :
  is_deriv (g ∘ f) x (L₂.comp L₁) :=
```
 
(we're differentiating at x but big deal).

Cyril and Assia then said that this was not the actual chain rule -- the chain rule was

`deriv (g ∘ f) x = (deriv g (f x)).comp(deriv f x)`

where `deriv` is the partial function, totalized by sending every non-differentiable function to 0.

For me, both of these are the chain rule, and questions such as which one is "best" or should be proved first or whatever are just implementation issues, of which I know nothing.

But from what Assia and Cyril were saying, there is some sort of *big deal* here, the nature of which I do not understand. Can someone explain to me what the content of the interaction between Assia/Cyril and Mario was, because there was clearly some content but I missed it the first time.

#### [Kevin Buzzard (Jan 09 2019 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean Together 2019/topic/derivative API/near/154711053):
```lean
import data.real.basic analysis.bounded_linear_maps

structure bounded_linear_map {k : Type*}
  [normed_field k] (E : Type*) [normed_space k E]
  (F : Type*) [normed_space k F]
  extends E →ₗ F :=
(bound' : ∃ M, M > 0 ∧ ∀ x : E, ∥ to_fun x ∥ ≤ M * ∥ x ∥)

local infix ` →bl `:25 := bounded_linear_map

namespace bounded_linear_map
variables  {k : Type*}
  [normed_field k] {E : Type*} [normed_space k E]
  {F : Type*} [normed_space k F]
  {G : Type*} [normed_space k G]
include k

instance : has_coe_to_fun (E →bl F) :=
⟨λ _, E → F, λ x, x.to_fun⟩

theorem bound (f : E →bl F) : ∃ M, M > 0 ∧ ∀ x : E, ∥f x∥ ≤ M * ∥x∥ := f.bound'

@[extensionality] theorem ext {f g : E →bl F}
  (h : ∀ x, f x = g x) : f = g :=
by cases f; cases g; simp; ext; exact h x

theorem is_bounded (f : E →bl F) : is_bounded_linear_map f := ⟨f.1.is_linear, f.bound⟩

def mk' (f : E → F) (h : is_bounded_linear_map f) : E →bl F := ⟨is_linear_map.mk' f h.1, h.2⟩

def comp (f : F →bl G) (g : E →bl F) : E →bl G :=
mk' _ (f.is_bounded.comp g.is_bounded)

@[simp] theorem comp_apply (f : F →bl G) (g : E →bl F) (x : E) : f.comp g x = f (g x) := rfl

instance : has_zero (E →bl F) :=
⟨mk' _ is_bounded_linear_map.zero⟩

end bounded_linear_map

def little_o {α β γ} [normed_group β] [normed_group γ] (f : α → β) (g : α → γ) (F : filter α): Prop :=
∀ c > 0, {x | ∥f x∥ ≤ c * ∥g x∥} ∈ F.sets

def is_deriv {k : Type*}
  [normed_field k] {E : Type*} [normed_space k E]
  {F : Type*} [normed_space k F] (f : E → F) (x : E) (L : E →bl F) : Prop :=
little_o (λ h, f (x + h) - (f x + L h)) id (nhds 0)

def has_deriv {k : Type*}
  [normed_field k] {E : Type*} [normed_space k E]
  {F : Type*} [normed_space k F] (f : E → F) (x : E) : Prop :=
∃ L, is_deriv f x L

noncomputable def deriv {k : Type*}
  [normed_field k] {E : Type*} [normed_space k E]
  {F : Type*} [normed_space k F]
  (f : E → F) (x : E) : E →bl F :=
by classical; exact
if h : has_deriv f x then
  classical.some h
else 0

theorem chain_rule_aux {k : Type*}
  [normed_field k] {E : Type*} [normed_space k E]
  {F : Type*} [normed_space k F]
  {G : Type*} [normed_space k G]
  (f : E → F) (g : F → G) (x : E)
  (L₁ : E →bl F) (L₂ : F →bl G)
  (h₁ : is_deriv f x L₁)
  (h₂ : is_deriv g (f x) L₂) :
  is_deriv (g ∘ f) x (L₂.comp L₁) :=
begin
  unfold is_deriv at *,
  admit
end


theorem chain_rule {k : Type*}
  [normed_field k] {E : Type*} [normed_space k E]
  {F : Type*} [normed_space k F]
  {G : Type*} [normed_space k G]
  (f : E → F) (g : F → G) (x : E)
  (L₁ : E →bl F) (L₂ : F →bl G) :
  deriv (g ∘ f) x = (deriv g (f x)).comp(deriv f x) :=
begin
  ext L,

  unfold is_differentiable at *,

end
```
That was the state of the live coding session when we called it a day.

#### [Sebastien Gouezel (Jan 09 2019 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean Together 2019/topic/derivative API/near/154711250):
```quote
Cyril and Assia then said that this was not the actual chain rule -- the chain rule was

`deriv (g ∘ f) x = (deriv g (f x)).comp(deriv f x)`

where `deriv` is the partial function, totalized by sending every non-differentiable function to 0.
```
I don't think this is true. Take `g(x) = sqrt(x)` and `f(x) = x^2` for `x \geq 0`, and make every function odd. Then `g o f` is the identity, so it should have derivative 1 at 0, but g is not differentiable so if you take the above formula you get 0 for the right hand side. Conclusion: the chain rule only makes sense if you assume additionally that the functions are differentiable.

#### [Cyril Cohen (Jan 09 2019 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean Together 2019/topic/derivative API/near/154713028):
Yes indeed, in my experience, the most usable version of the chain rule in dependent type theory should be https://github.com/math-comp/analysis/blob/master/derive.v#L698-L700

#### [Joseph Corneli (Jan 09 2019 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean Together 2019/topic/derivative API/near/154713252):
I was also wondering: could we make a more abstract definition of "derivative" that would e.g. cover derivatives in the sense of distributions as well as functions and bounded linear maps.

#### [Kevin Buzzard (Jan 09 2019 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean Together 2019/topic/derivative API/near/154713750):
OK so thanks to these comments and talking to Assia, Cyril and others over coffee, I now understand a bit better. This again is the issue of partial functions. The question is should we define `deriv f H = g` where `H` is a proof that `f` is differentiable and then `g` is the derivative, or should we define `deriv f = g` where `g` is the derivative of `f` if `f` is differentiable, or 0 otherwise. As Sebastian points out, if we don't use `H` in our definition of `deriv` then actually we need to put it in the statement of the theorem. The point is that maybe the theorem is a better place to put the assumption, because of the usual rewrite problem -- if `deriv f1 _ = g` and `f1 = f2` then you can't do a simple rewrite to deduce `deriv f2 _ = g` because the proof is a proof of the wrong thing. The point, which is something Assia stressed, is that this is not an issue with Lean, this is an issue with dependent type theory itself, so two people with extensive Coq experience saying we should define `deriv` without the proof represent something we should listen to.

This situation only arises because every function has at most one derivative. If we were dealing with a more general binary predicate for which `D f g` could be true for more than one choice of `g` then one would presumably stick to the predicate approach.

#### [Sebastien Gouezel (Jan 09 2019 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean Together 2019/topic/derivative API/near/154714621):
In Isabelle also, the most efficient way is to have a predicate `is_differentiable f x`, a total function `differential f x`, and two theorems asserting that, if `is_differentiable f x` and `is_differentiable g (f x)`, then `is_differentiable (g o f) x` and `differential (g o f) x = differential g (f x) o differential f x`. Except that the API is richer: you can also define differentiability inside a set, and then the differential is not necessarily unique -- but for most interesting cases it is, for instance if the set is open and `x` belongs to this set. So you also have a predicate `has_differential f x S L`, on which everything is built. This is not just for the sake of generality: in dynamics, we often encounter functions that are only defined on Cantor like sets and differentiable on them, so a good theory should allow this.

#### [Assia Mahboubi (Jan 09 2019 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean Together 2019/topic/derivative API/near/154714728):
```quote
 Conclusion: the chain rule only makes sense if you assume additionally that the functions are differentiable.
```
Sure. Not only the chain rule actually. One could argue that in this case this `deriv` operation is a misnomer.  But I do not know what would be a better name (`pre-deriv` , `pseudo-deriv`?)  It would probably be quite boring to work with such a name anyway. However, `deriv f` means the mathematically sensible derivative of  `f` only when, well,  `f` is actually derivable.

#### [Sebastian Ullrich (Jan 09 2019 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean Together 2019/topic/derivative API/near/154714882):
I do hope no one wants us to call `/` `pre_div`

#### [Kevin Buzzard (Jan 09 2019 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/179818-Lean Together 2019/topic/derivative API/near/154715016):
heh :-) But I have argued in the past that it should not be called `/`; I encourage my students to read it as "computer scientist division", and see it as a division sign with a little "^*" next to it.

