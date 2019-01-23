---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/73742atlases.html
---

## Stream: [maths](index.html)
### Topic: [atlases](73742atlases.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128648910):
I decided to try to move forward in my differential topology project without waiting for experts to sort out the module type class issues. So let's say I'm ready to sorry the definition of a diffeomorphism between two open subsets of R^n. Then the definition to formalize is https://en.wikipedia.org/wiki/Differentiable_manifold#Atlases I have no idea how to attack this coercion mess. I'd like to understand the definition of the transitions maps, and understand they are maps between open subsets of R^n

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128648973):
Even restricting a function to a subset is non-trivial in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128649000):
and here I need that the restriction of a homeo to a subset is a homeo onto its image

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 26 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128651578):
```quote
Even restricting a function to a subset is non-trivial in Lean
```
Can't you compose with `subtype.val`? And then you need that `subtype.val` is an immersion, and C^k for every value of k.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128653776):
I need to invert the restriction of an `equiv` to some subset

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 26 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128656888):
Is this any use?
```lean
import analysis.topology.continuity
variables {α : Type*} {β : Type*} [topological_space α] [topological_space β]
  (A : set α) (f : {f : α ≃ β // continuous f})

def restriction : {g : A ≃ f '' A // continuous g} :=
⟨{  to_fun := (λ a, ⟨f a.1, a, a.2, rfl⟩),
    inv_fun := λ b, ⟨(equiv.symm (f : α ≃ β)) b, let ⟨a, ha₁, (ha₂ : f a = b)⟩ := b.2 in 
      calc _ = a : by rw ← ha₂; exact equiv.inverse_apply_apply _ _
      ... ∈ A : ha₁⟩,
    left_inv := λ ⟨_, _⟩, subtype.eq (f.1.3 _),
    right_inv := λ ⟨_, _⟩, subtype.eq (f.1.4 _)  },
  continuous_subtype_mk (λ x, ⟨x, x.2, rfl⟩) 
  (continuous.comp continuous_subtype_val f.2)⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128656981):
Maybe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128656994):
I'm exploring a lot of ways to try to make Lean understanding this definition or variations on this definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657042):
I already knew there were plenty of variations on the definition of manifolds but I'm discovering many more

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657449):
A variation on this kind of effort could be to adapt
```lean
protected noncomputable def image {α β} (f : α → β) (s : set α) (H : injective f) :
  s ≃ (f '' s) :=
⟨λ ⟨x, h⟩, ⟨f x, mem_image_of_mem _ h⟩,
 λ ⟨y, h⟩, ⟨classical.some h, (classical.some_spec h).1⟩,
 λ ⟨x, h⟩, subtype.eq (H (classical.some_spec (mem_image_of_mem f h)).2),
 λ ⟨y, h⟩, subtype.eq (classical.some_spec h).2⟩
```
from `equiv.lean` to a version where `H` would be `inj_on f s`, which seems like a much more relevant hypothesis anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657525):
But maybe I don't care. I don't know. There are so many ways to try to setup this thing...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 26 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657624):
You're losing computability with that def, though I'm not sure you care.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657642):
Ah, at least there is something I know: I don't care about computability.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657660):
Chris, this remark worries me. I think you may be spending too much time with Kenny.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657843):
I'm completely confused about https://github.com/leanprover/mathlib/blob/master/data/equiv.lean#L527 How do you access this definition? It seems to be in namespace `set` but is obviously not the same as `set.range`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 26 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657903):
the `equiv` namespace never ended :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jun 26 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657904):
`equiv.set.range`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657930):
Oh, that's nasty

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657932):
thanks Kenny

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657987):
hum, I hear I urgently need to go to the main lecture hall in IHES

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657994):
it seems the match started already

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jun 26 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128677951):
Are you planning to implement only C^\infty manifolds over the reals, or manifolds with different classes of smoothness (say C^0, or C^1, or C^k, or analytic, or PL, or whatever you like, over R or C)? It seems to me that it would be better to implement various classes of smoothness in the same framework. For instance, one could axiomatize what one needs to have a "smoothness class" (families of maps which are all homeos between open subsets of a given topological space, stable under restriction and composition and inverses), and then one could define a manifold with respect to this smoothness class. Two advantages of this approach: 
- this is more general, and useful
- you don't need to define R^n and smooth maps to start working with this definition (but of course, you will have no example at the beginning, except maybe for C^0 manifolds which would be the first example to work out)
Any thoughts?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128678095):
Unfortunately I'm pretty far from being able to do that. The trouble is partially defined functions are everywhere. A chart is defined on part of the manifold, a transition function is defined on the image of part of the domain of a chart. I really struggle with this. How is this handled in Isabelle? Do you have smooth functions defined on open subsets of R^n and a convenient way to restrict a smooth function to an open subset?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128678162):
But, to answer your question, I was indeed hoping to implement manifolds modeled on any pseudo-group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128678223):
I also find it very interesting to see that, once again, the only source which seems to be suitable for formalization is Bourbaki.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jun 26 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128678435):
In Isabelle, I would model a smoothness class by a set of pairs `(U, f)` where `U` is an open subset of `R^n` and `f` is a map from `R^n`to itself such that its restriction to `U` is a homeomorphism. So, I would have a predicate `homeomorphism_on U f` saying that `f` is a homeomorphism on `U`, together with basic properties of homeomorphisms (say, if `f` is a homeomorphism on `U` and `g`is a homeomorphism on `V` and `f(U) \subseteq V`, then `g o f` is a homeomorphism on `U`). Then you don't ever need to restrict your functions to subsets, and you avoid a lot of trouble.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jun 26 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128678493):
and the smoothness on open subsets is also defined for total functions, using a predicate as above.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128678843):
I thought about trying to get functions defined everywhere and asking for injectivity and smoothness only on subsets. But I fear it will be a nightmare when trying to prove things because every function would be defined by `lambda x, if x in U then real_thing x else 42`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128678861):
And also I don't like this has nothing to do with math

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128678876):
It's purely an artefact of the type theoretic foundations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jun 26 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679380):
You would never have any `if` in your definitions. The composition of two homeomorphisms `f`on `U` and `g` on `V` is just `g o f` on `U` (and it only makes sense if `f(U) \subseteq V`, but this is also the case with the true definition). The restriction of a homeomorphism `f`on `U` to a smaller subset `U'` is still `f `. And so on. This may seem surprising at first sight, but in fact it is not so surprising: if you only do meaningful constructions, then the values of your function outside of its "domain of definition" should never play any role, so what happens there is never relevant, and it can behave in the way it wants.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679475):
I know it's the theory, I've seen it countless times with 0/0 and other crazy stuff. But you still need to define an arbitrary crazy value. For 0/0 you can choose 0, fine. What if the target is a manifold?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jun 26 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679491):
It is just like the fact that the division is total on real numbers: surprising and annoying at the beginning, and then when you get used to it you realize you don't care at all what it does at zero because you're not stupid and you never apply it at `0` (and of course you always have to check that the denominator is nonzero -- here in the same way you would always have to check that the points you apply your function to are in the "domain of definition")

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679603):
Do you have the same crazyness in Isabelle then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jun 26 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679604):
At least for the definition of a manifold in terms of an atlas of compatible charts, you would never need to specify a value, it is just some axioms you want to satisfy.
Probably, when you define a manifold structure on some object, yes, you will have to make some arbitrary and irrelevant choice at some point. But that would be very rare, I guess.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679660):
Yes, I want to define actual manifolds, like smooth affine varieties in R^n (say S^{n-1})

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jun 26 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679662):
The crazyness of what? Every function is total, yes. And it turns out to be a non-issue once you're used to it. (Takes some time to get used to it :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679687):
thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jun 26 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679765):
Think of S^{n-1}. Take the two natural stereographic charts: they are defined on the whole of R^{n-1}, so no issue of arbitrary choice when you define them. And then you just have to check the axiom that the composition of one chart and the inverse of the other one, restricted to the good sets, are smooth. No arbitrary choice again.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jun 26 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679794):
Same think if you define Grassmannians, say: the natural local charts using linear maps are defined on the whole R^k. No arbitrary choice again.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679801):
This is not the definition I want to use. This one is only an exercise in understanding the internal plumbing that is the precise definition of a manifold. I want S^{n-1} defined by |x|² = 1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679809):
I want submanifolds of manifolds to be manifolds

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679869):
But I'll try this total function road

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jun 26 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679884):
Then you want to use two theorems, that the preimage of a regular value by a map is a submanifold, and that a submanifold is a manifold. Again no choice :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679902):
Are you sure the second one will require no choice? Maybe.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jun 26 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679961):
The way answers are intermingled is really strange in such a chat. Anyway, to prove that a submanifold is a manifold, essentially you will first straighten your submanifold, and then restrict your charts to the submanifold. Then there should be no `if`in the involved arguments.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128680079):
I'll try all this tomorrow (what I tried today is on https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/manifold.lean if you are curious (there may be stupid things there, I switched gears so many times...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128680108):
thank you very much for this conversation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 26 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128680117):
good night!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128716143):
I try to get used to totalization of functions. What do people think about:
```lean
universes u v
variables {α : Type u} [inhabited α] {β : Type v} 

def inverse_on  {U : set α} {f : α → β} (H : inj_on f U) : β → α :=
λ b, if h : b ∈ f '' U then classical.some h else default α

lemma inverse_on_spec {U : set α} {f : α → β} (H : inj_on f U) : 
  inv_on (inverse_on H) f U (f '' U) :=
begin
  split ; intros x h,
  { have H' := mem_image_of_mem f h,
    cases classical.some_spec H' with h1 h2,
    simp [inverse_on, H', H h1 h h2] },
  { cases classical.some_spec h with h1 h2, 
    simpa [inverse_on, h] using h2 }
end
```
Is it something I should be doing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 27 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717488):
I don't see why it should be necessary to work with total functions here, and this approach has its own disadvantages. I think the root problem is that you currently lack a sufficient Lean vocabulary to work with partial functions and partial bijections

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717549):
What would be that vocabulary?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 27 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717677):
For example, looking at the definition of pseudogroup, you could state most of these axioms immediately given:
* A type `pequiv a b` representing a bijection between a subset of the type `a` and a subset of the type `b`. Note that the subsets of `a` and `b` are not indices of the type `pequiv a b`.
* A "restricted composition" operation `pequiv a b \to pequiv b c \to pequiv a c`.
* A "restricted identity" of type `pequiv a a` for each `s : set a`, which is the identity bijection between `s` and itself. From this and the previous one, you can implement restriction of a `pequiv` to a subset of the domain or codomain.
* A way to extract from a `pequiv a b` the domain `s` as a `set a`, and a function `subtype s \to b`, which you can then check for continuity or smoothness or whatever.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717764):
What would be a "restricted composition" in a world where all functions are total? That's precisely the trouble.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 27 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717766):
Also I forgot the "symmetry" `pequiv a b \to pequiv b a`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 27 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717822):
Well then you are asking about how to implement this interface, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717830):
Everything is about implementation in this discussion, I already know what is a manifold.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 27 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717834):
Or are you asking about the meaning of the operation? It's just the one which, given partial bijections f and g, is defined on x when f(x) is defined and g(f(x)) is also defined

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717858):
Indeed having the subsets as fields instead of parameters may be enough to do the trick

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717952):
I guess this is closer in spirit to the `option a` type than totalizing functions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718006):
You might also want to check out `roption` and the `data.pfun` module

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 27 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718021):
But the main point is that for a computer, everything is hard, even these utterly trivial notions like "bijection between a subset of `a` and a subset of `b`".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 27 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718077):
It helps to decompose the problem into pieces, so you are not thinking about manifolds when trying to define the composition of partial bijections. Of course this concept is not foreign to mathematicians, but here the pieces are much smaller than we are used to.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718180):
Yes I noticed all this (but noticing doesn't make it easy to use Lean)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 27 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718181):
Once you have settled on the right interface for `pequiv`, the choice of implementation is not so important

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718183):
I'll look at roption and pfun

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 27 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718297):
Something that may not be obvious from the pfun module is that because `roption` is a monad, you get a composition operation `(a -> roption b) -> (b -> roption c) -> (a -> roption c)` for free

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 27 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718526):
Apparently it doesn't really have a name in Lean aside from ` >=> `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718545):
I hope I'll be able to avoid this kind of notations...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 27 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718555):
Again, only a question of implementation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 27 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718559):
Of course for `pequiv`, you can choose whichever notation you like

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 27 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718733):
By the way, even though you don't care about constructiveness, I think things will be easier in the long run if you keep the maps in both directions as data in a bijection

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718770):
as in using `equiv` rather than `bijective` you mean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 27 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718777):
Otherwise, when defining the canonical manifold structure on R^n for example, I think the transition maps will turn out to be something like `lam x, classical.choice (\ex y, y = x)` rather than `lam x, x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 27 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718779):
Exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jun 27 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719255):
What about defining rather 
```
def inverse_on  (U : set α) (f : α → β) : β → α :=
λ b, if h : b ∈ f '' U then classical.some h else default α
```
and having the injectivity as an assumption in your lemma `inverse_on_spec`. So that `inverse_on` is really taking as argument a function, and not a proof: formulas with `inverse_on U f` should be much more understandable than `inverse_on H` where you don't remember what `H` is. (This is really an implementation detail, everything is clearly equivalent, but still aiming at readability is always good!)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 27 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719339):
If you keep track of both directions, then you can always produce the inverse using `bijective` and "unique choice" whenever it would be less convenient to provide it manually. But if you throw away the inverse direction and only keep the `Prop` of bijectivity, you can only recover the inverse function up to propositional equality. Then you may be faced with proving some equality these reconstructed inverses, where if you had kept the original inverses the proof would just be `rfl`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719435):
Thanks to both of you, this is all very interesting. I'll keep on working on the totalization path until I can define manifolds modulo the definition of smooth maps (it looks like it will work). But then I'll try to redo everything using the `pequiv` idea, and compare.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719536):
The definition of `inverse_on` without injectivity assumption really looks weird

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719552):
I don't care at all about constructivism, and I don't mind using the axiom of choice. But this really doesn't feel like defining a function.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jun 27 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719704):
I like my functions to be total :) So `inverse_on` is also total with this definition. 
More seriously, in some settings, just taking one (any) preimage will make sense. For instance if you are working in a coarse geometry setting and you know that the preimages of any point have bounded diameter. This is the way one inverts quasi-isometries.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 27 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719719):
The axiom of choice is a pain to use in practice, because you need to keep track of random proof terms. I had two types X and Y in bijection recently, with a computable map X -> Y and a noncomptable map Y -> X, and after failing to construct something of type `equiv X Y` directly because of proof terms giving me problems I just proved X->Y was a bijection and then invoked `equiv.of_bijection`. Working with the axiom of choice can be a pain. Basically if you invoke it twice then there's no guaranteeing you got the same answer twice, so you can only invoke it once and then you have to keep a very careful track of where you invoked it and what you got.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jun 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719812):
The idea would be that you never ever come back to the definition of inverse_on, but only use the two lemmas saying that `f (inverse_on U f y) = y` if `y \in f''(U)`, and that `inverse_on U f( f x) = x` if `x \in U` and `f` is injective on `U`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719876):
My `inverse_on_spec` is the conjunction of these two statements

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jun 27 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719883):
Yes, but for one of them you don't need the injectivity.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719894):
Sure. But I needed injectivity in the definition for psychological confort.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719895):
:)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jun 27 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719914):
Go for the minimal assumptions. It will simplify your proofs if there are less assumptions to check!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128722751):
I noticed Mario sometimes goes for biconditional statements in this situation. It indeed feels weird.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 27 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128722771):
I will need a more precise stub for smoothness if I want to prove that equivalence of atlases is an equivalence relation...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jul 02 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128951168):
`inverse_on` is `inv_fun_on` in `logic/function.lean`. For surjective functions there is also `surj_inv` (there the range doesn't need to be inhabited).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 02 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128954811):
Thanks! I completely failed to see that file. I still don't understand the criterion separating stuff in `data/set/function.lean` and `logic/function.lean`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 02 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128954993):
I would say that the difference is the use of sets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 02 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128955000):
There are sets everywhere in both

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 02 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128955013):
`logic.function` does not import `data.set.basic`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 02 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128955023):
so the only set stuff is what is available in core

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 02 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128955079):
Would putting everything in the same file create dependency issues?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 02 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128955081):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 02 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128955093):
although it is likely that `inv_fun_on` can be moved to set safely

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 02 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128955147):
I like to think of the `logic` directory as covering more or less the "pure type theory" part of lean, just functions and pis and such

