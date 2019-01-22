---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/87954topologicalspacestuff.html
---

## [maths](index.html)
### [topological space stuff](87954topologicalspacestuff.html)

#### [Kevin Buzzard (May 12 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126462782):
I need some standard topological space arguments. Do we have homeomorphisms and/or open immersions in mathlib yet, and if not then where should I put them? Should a homeomorphism be an equiv or a bijection? (i.e. should I demand a map in the other direction?). I need that something homeomorphic to a compact space is compact -- another thing which a mathematician would not need to supply a proof of because "it's obvious".

#### [Mario Carneiro (May 12 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126463028):
I think Patrick has a definition of `homeo`. It extended `equiv`

#### [Mario Carneiro (May 12 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126463040):
of course homeos are isos in the category of top spaces so you are going to find many of the same parametricity things there as with your group iso stuff

#### [Patrick Massot (May 12 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126464136):
@**Kevin Buzzard** See https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/homeos.lean

#### [Patrick Massot (May 12 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126464137):
It's focused on the group structure on self-homeomorphisms

#### [Patrick Massot (May 12 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126464138):
But mathlib has induced topologies

#### [Patrick Massot (May 12 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126464184):
So I would try to prove that an equiv is a homeo iff both maps induce the same topology on their source as the original one

#### [Patrick Massot (May 12 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126464187):
and then deduce something homeo to a compact space is compact

#### [Reid Barton (May 12 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126465041):
I have a proof of `compact s ↔ compact (univ : set (subtype s))` lying around if you need that

#### [Kevin Buzzard (May 12 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126467384):
Does `open_immersion` go in the root namespace?

#### [Reid Barton (May 12 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126467549):
actually, I basically proved that something homeomorphic to a compact space is compact along the way

#### [Reid Barton (May 12 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126467553):
```lean
lemma compact2 [tβ : topological_space β] {f : α → β} {s : set β} (h : ∀y∈s, ∃x, f x = y) :
  compact s → @compact α (induced f tβ) (f ⁻¹' s) :=
```

#### [Reid Barton (May 12 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126467594):
Currently almost everything related to topological spaces is in the root namespace, which doesn't seem ideal, but surely it would be no worse than having `embedding` there which it is already.

#### [Reid Barton (May 12 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126467700):
Um, it also just follows from `compact_image`. :upside_down_face:

#### [Kevin Buzzard (May 12 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126467747):
I have never really engaged with namespaces until recently; I had other things to worry about. I never used the namespace command and never opened anything. But it's all dawning on me now about how it might all work. I am surprised this stuff is piling up in the root namespace, and the longer it's there the more it will hurt when someone decides that `compact` doesn't apply to all types and hence should be moved to somewhere more topological-spacey.

#### [Kevin Buzzard (May 12 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126467751):
Yes, continuous image of compact is compact will do and probably I will just cheat and use that :-)

#### [Reid Barton (May 12 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126467791):
`embedding` seems even more dubious

#### [Kevin Buzzard (May 12 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126467792):
That's in mathlib now, right?

#### [Reid Barton (May 12 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126467793):
Yep

#### [Kevin Buzzard (May 12 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126467999):
Is there `is_finite` somewhere, a prop saying that a type is finite?

#### [Mario Carneiro (May 12 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126470976):
There is `finite`, but that applies to sets

#### [Mario Carneiro (May 12 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126470981):
`open_immersion` sounds suitably unambiguously topological that it can go in the root namespace

#### [Kenny Lau (May 12 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126471039):
```quote
Is there `is_finite` somewhere, a prop saying that a type is finite?
```
there's `fintype` which isn't a prop

#### [Kenny Lau (May 12 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126471044):
the prop is `nonempty (fintype \a)`

#### [Mario Carneiro (May 12 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126471048):
For `compact2`, I would recommend against theorems that have "weird" topologies inserted in the top space component. It makes them very hard to use. Instead, I would want a hypothesis that says that the topology on `A` is induced from `f` by the topology on `B` (i.e. `topA = induced f topB`, and then you can just use regular typeclass inference to state `compact` on each side

#### [Johan Commelin (May 12 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126471234):
```quote
`open_immersion` sounds suitably unambiguously topological that it can go in the root namespace
```
But there are also *open immersions* in other categories (manifolds, schemes, etc). Wouldn't that create confusion?

#### [Kevin Buzzard (May 22 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126932789):
I have to make a design decision.

#### [Kevin Buzzard (May 22 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126932818):
```lean
structure topological_space.open_immersion
  {α : Type*} [Tα : topological_space α]
  {β : Type*} [Tβ : topological_space β]
  (f : α → β) : Prop :=
(fcont : continuous f)
(finj : function.injective f)
(fopens : ∀ U : set α, is_open U ↔ is_open (f '' U))
```

#### [Kevin Buzzard (May 22 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126932819):
I don't care either way

#### [Kevin Buzzard (May 22 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126932820):
or

#### [Kevin Buzzard (May 22 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126932821):
```lean
def topological_space.open_immersion {X Y : Type u} [tX : topological_space X] [tY : topological_space Y] (φ : X → Y) := 
  continuous φ ∧ 
  function.injective φ ∧ 
  ∀ U : set X, tX.is_open U → tY.is_open (set.image φ U)

```

#### [Kevin Buzzard (May 22 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126932822):
and don't know enough about how things work to know which choice is best

#### [Reid Barton (May 22 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126933209):
There's already `embedding`, by the way. So you could also just add `is_open (range f)` to that and use `embedding_open`.

#### [Reid Barton (May 22 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126933294):
I doubt it matters much which exact definition you take, as you can write lemmas to prove that other definitions are equivalent. Whether to use a `structure` or not is probably more important, but depends on what you want to do with it.

#### [Reid Barton (May 22 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126933483):
Oh, your structure is indexed on `f` also; then it's just a matter of taste I think.

#### [Andrew Ashworth (May 22 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126939770):
I like structures for organizing things that are linked by and statements, I prefer giving names to the hypotheses rather than referring to them as `and.left and.left ...` etc

#### [Sean Leather (May 23 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126962847):
One thing to consider is how you use `simp` and `@[simp]` theorems. With a structure, you have control over what is simplified by carefully choosing where you place your `@[simp]`s. With nested conjunctions, you are at the mercy of the existing `@[simp]` theorems. (Of course, you can “work around” this; it's just a matter of how simple your proofs will be.) On the other hand, with conjunctions, you may find that it's easier to work with simplified proofs, given how much already exists to simplify them. (Of course, you can recover this ease by writing `@[simp]` theorems to do the conversion from the structure to conjunctions. But there goes your control, too.)

#### [Reid Barton (May 23 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126969745):
Another advantage of giving the fields names is that if for some reason you want to change the underlying definition, you can do it in a way that's somewhat transparent by making functions with the names of the old fields.

#### [Reid Barton (May 23 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological space stuff/near/126969806):
Though this doesn't help if you tend to use pattern matching / implicit constructor syntax

