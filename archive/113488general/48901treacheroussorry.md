---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48901treacheroussorry.html
---

## Stream: [general](index.html)
### Topic: [treacherous sorry](48901treacheroussorry.html)

---


{% raw %}
#### [ Patrick Massot (Jun 28 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128764182):
I'm slowing beginning to understand why trying to formalize math in a top to down way is very dangerous, even if this is very appealing to mathematicians. Today's lesson is about sorried properties. In the minimized version below, say we are trying to build of stub of continuous functions theory.
```lean
variables {α β γ : Type}

-- function f is continuous at point x
def continuous_at (x : α) (f : α → β) : Prop := sorry

def continuous (f : α → β) : Prop := ∀ x, continuous_at x f

lemma continuous_at_comp {f : α → β} {g : β → γ} {x : α} :
continuous_at x f → continuous_at (f x) g → continuous_at x (g ∘ f) := sorry

lemma continuous_comp (f : α → β) (g : β → γ) :
  continuous f → continuous g → continuous (g ∘ f) := 
assume cont_f cont_g x, continuous_at_comp (cont_f x) (cont_g (f x))
```
Looks good to me. It tells the story of continuity being a property of a function that can be checked near each point, and the composition property of this local thing implies composition for the global thing.

#### [ Patrick Massot (Jun 28 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128764231):
Now let's look at the following "simplified" version:

#### [ Patrick Massot (Jun 28 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128764236):
```lean
variables {α β γ : Type}

-- function f is continuous at point x
def continuous_at (x : α) (f : α → β) : Prop := sorry

def continuous (f : α → β) : Prop := ∀ x, continuous_at x f

lemma continuous_comp (f : α → β) (g : β → γ) :
  continuous f → continuous g → continuous (g ∘ f) := 
assume cont_f cont_g x, cont_g (f x)
```
:scream:

#### [ Patrick Massot (Jun 28 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128764253):
It reminds me of traps of unit testing using mocks.

#### [ Mario Carneiro (Jun 28 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765257):
The problem is that `continuous_at` has been defined as a constant wrt `x` and `f`, since `sorry : Prop` has no stated dependence on `x` and `f`. One solution is to sorry at the function level:
```
def continuous_at : α → (α → β) → Prop := sorry
```
(you can also write `∀ (x : α) (f : α → β), Prop` if you prefer to name the variables)

#### [ Mario Carneiro (Jun 28 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765385):
That said, I completely agree with you about the dangers of axiomatizing things without a cross-check. I did not notice the issue in the first code block until you pointed it out

#### [ Patrick Massot (Jun 28 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765392):
Indeed this fixes this problem. But my point remains: one needs to be extremely careful with this kind of sorries

#### [ Patrick Massot (Jun 28 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765402):
I'd like to understand better what you call "cross-check".

#### [ Mario Carneiro (Jun 28 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765448):
It is hard to check an axiom or a definition for correctness, since lean can't help you

#### [ Mario Carneiro (Jun 28 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765515):
In a sense, proving theorems about a definition or theorems that follow from axioms form a kind of testing on the definition, since they can (but not necessarily will) expose issues and edge cases that were not originally considered

#### [ Patrick Massot (Jun 28 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765518):
Something else mysterious to me: replacing `def continuous_at (x : α) (f : α → β) : Prop := sorry` by `constant continuous_at (x : α) (f : α → β) : Prop` also allows to uncover the issue

#### [ Mario Carneiro (Jun 28 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765536):
That's because in `axiom` and `constant` it is always defined as a single global constant abstracted over any variables

#### [ Mario Carneiro (Jun 28 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765576):
so it's exactly the same as `constant continuous_at : α → (α → β) → Prop`

#### [ Mario Carneiro (Jun 28 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765597):
You should think of `sorry` as providing a term of the specified type, without necessarily pulling in all the assumptions in the context but only the ones needed to typecheck the type of the sorry

#### [ Mario Carneiro (Jun 28 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765640):
while `axiom` / `constant` only produces terms in the empty context so it gets all the variables

#### [ Patrick Massot (Jun 28 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765641):
Indeed that clearly explains the flaw: `x` and `f` are not needed to construct a term with type `Prop`

#### [ Patrick Massot (Jun 28 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765648):
I mean: it explains why `sorry` is dangerous here, it doesn't quite explain why `constant` works

#### [ Mario Carneiro (Jun 28 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765652):
another option would be to write `sorry x f`, but this doesn't typecheck so you have to annotate the type, which kind of defeats the point

#### [ Mario Carneiro (Jun 28 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765696):
i.e.
```
def continuous_at (x : α) (f : α → β) : Prop :=
(sorry : α → (α → β) → Prop) x f
```

#### [ Mario Carneiro (Jun 28 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765755):
```
constant continuous_at (x : α) (f : α → β) : Prop
#print continuous_at
-- constant continuous_at : Π {α β : Type}, α → (α → β) → Prop
```
what else would it do? A `def` doesn't randomly drop variables that are given in its statement, so it would be weird for `constant` to do so

#### [ Patrick Massot (Jun 28 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765766):
Ok, thanks

#### [ Mario Carneiro (Jun 28 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765769):
note that even with `def continuous_at (x : α) (f : α → β) : Prop := sorry`, `continuous_at` has exactly that same type

#### [ Mario Carneiro (Jun 28 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765779):
the only difference is that `constant continuous_at` can't be unfolded

#### [ Patrick Massot (Jun 28 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765781):
My train ride is almost finished, I'll disappear from here (I love trains with WIFI).

#### [ Patrick Massot (Jun 28 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765792):
You can answer emails in the meantime :wink:

#### [ Sebastien Gouezel (Jun 28 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128780496):
Instead of sorrying stuff, you could work in an axiomatic kind of way, just putting as assumptions all the stuff you need and starting from there. If you want to work with general pseudo-groups, maybe this is the way to go. For instance, if you define a smoothness class as follows, then I guess this is enough to define manifolds based on the smoothness class. And then you will just need to show that your favorite class (say symplectomorphisms, but maybe it is better to work with homeos to start with) satisfies your axioms, to get symplectic manifolds or C^0 manifolds.
```lean
import analysis.real data.set.function 

noncomputable theory
local attribute [instance] classical.decidable_inhabited classical.prop_decidable

universes u v
variables {α : Type u} [inhabited α] {β : Type v}

open set

def inverse_on (U : set α) (f : α → β) : β → α :=
λ b, if h : b ∈ f '' U then classical.some h else default α

def homeomorphism_on (U : set α) (f : α → β) := inj_on f U -- agreed, this definition is not optimal

structure smoothness_class (α : Type u) [topological_space α] [inhabited α] :=
(smooth_on : (set α) → (α → α) → Prop)
(open_domain: ∀U f, smooth_on U f → is_open U)
(homeo: ∀U f, smooth_on U f → homeomorphism_on U f)
(restriction: ∀U V f, smooth_on U f → is_open V → V ⊆ U → smooth_on V f)
(composition: ∀U V f g, smooth_on U f → smooth_on V g → f ''(U) ⊆ V → smooth_on U (g ∘ f))
(inversion: ∀U f, smooth_on U f → smooth_on (f ''(U)) (inverse_on U f))

variables [topological_space α] (S: smoothness_class α)
-- and now I want to define manifolds based on the class of maps S...
```
Maybe I forgot some important axiom, but you see the idea.

And I also enjoy the wifi on trains :)

#### [ Kevin Buzzard (Jun 28 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128781917):
This is very interesting to me because we started at the top with perfectoid spaces: https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/perfectoid_space.lean ; and I had no idea that this could cause any problems at all. The perfectoid space link is what looks like a fully written definition of a perfectoid space, but the import contains a gazillion sorries.

#### [ Simon Hudon (Jun 28 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128782917):
Is `gazillion` defined as `def gazillion : nat := sorry`?


{% endraw %}
