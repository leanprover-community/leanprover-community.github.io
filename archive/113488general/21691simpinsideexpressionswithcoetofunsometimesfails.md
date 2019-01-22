---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21691simpinsideexpressionswithcoetofunsometimesfails.html
---

## [general](index.html)
### [simp inside expressions with coe_to_fun sometimes fails](21691simpinsideexpressionswithcoetofunsometimesfails.html)

#### [Scott Morrison (Aug 06 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130948850):
I've been trying to implement @**Johannes Hölzl** request that in my baby PR for category theory I use coercions to allow applying a functor to an object, as `F X`, rather than having to either write explicitly `F.onObjects X`, or introduce some awkward notation, such as `F +> X`.

#### [Scott Morrison (Aug 06 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130948858):
I would very much like to do this, but I also want to be confident that this doesn't mess up the nice and easy automation I have throughout my category theory library.

#### [Scott Morrison (Aug 06 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130948897):
Unfortunately, I seem to have run into a problem, which is a strange interaction between coercions and the simplifier.

#### [Scott Morrison (Aug 06 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130948901):
Hopefully someone here will explain how to get around this! I fear that the fix would require tweaking the simplifier, which is out of bounds at the moment.

#### [Scott Morrison (Aug 06 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130948911):
In any case, here is a self-contained piece of code, containing some very cut down definitions from the category theory library, that demonstrates the problem.

#### [Scott Morrison (Aug 06 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130948964):
Essentially, it is that `simp` sometimes can't rewrite under a coercion, because it can't build the proof terms (in particular, it can't build some `congr_arg` terms, because of a type checking subtlety).

#### [Scott Morrison (Aug 06 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130948985):
This has the result that in order to be able to use `simp` successfully, I'll have to provide two versions of many lemmas: one for use by humans, that refer to the coercions, and one for use by `simp` (after applying `unfold_coes` to unfold all the coercions), that don't refer to the coercions.

#### [Scott Morrison (Aug 06 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130948986):
In my mind, that's worse than not having the coercions available in the first place.

#### [Scott Morrison (Aug 06 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949027):
````
import tactic.interactive

universe u

class category (Obj : Type u) : Type (u+1) :=
(Hom : Obj → Obj → Type u)
(identity : Π X : Obj, Hom X X)

notation `𝟙` := category.identity     -- type as \b1
infixr ` ⟶ `:10  := category.Hom     -- type as \h

variable (C : Type u)
variable [𝒞 : category C]
variable (D : Type u)
variable [𝒟 : category D]
include 𝒞 𝒟

instance ProductCategory : category (C × D) := 
{ Hom            := λ X Y, ((X.1) ⟶ (Y.1)) × ((X.2) ⟶ (Y.2)),
  identity       := λ X, ⟨ 𝟙 (X.1), 𝟙 (X.2) ⟩ }    

@[simp] lemma ProductCategory.identity (X : C) (Y : D) : 𝟙 (X, Y) = (𝟙 X, 𝟙 Y) := by refl

structure Functor  :=
(onObjects     : C → D)
(onMorphisms   : Π {X Y : C}, (X ⟶ Y) → ((onObjects X) ⟶ (onObjects Y)))
(identities    : ∀ (X : C), onMorphisms (𝟙 X) = 𝟙 (onObjects X))

attribute [simp] Functor.identities

infixr ` +> `:70 := Functor.onObjects
infixr ` &> `:70 := Functor.onMorphisms 
infixr ` ↝ `:70 := Functor -- type as \lea 

variables {C} {D}

structure NaturalTransformation (F G : C ↝ D) : Type u :=
(components: Π X : C, (F +> X) ⟶ (G +> X))

infixr ` ⟹ `:50  := NaturalTransformation

instance {F G : C ↝ D} : has_coe_to_fun (F ⟹ G) :=
{ F   := λ α, Π X : C, (F +> X) ⟶ (G +> X),
  coe := λ α, α.components }

definition IdentityNaturalTransformation (F : C ↝ D) : F ⟹ F := 
{ components := λ X, 𝟙 (F +> X) }

instance FunctorCategory : category (C ↝ D) := 
{ Hom            := λ F G, F ⟹ G,
  identity       := λ F, IdentityNaturalTransformation F }

@[simp] lemma FunctorCategory.identity.components (F : C ↝ D) (X : C) : (𝟙 F : F ⟹ F) X = 𝟙 (F +> X) := by refl

lemma test (E : Type u) [ℰ : category E] (X : C) (Y : D) (F : C ↝ (D ↝ E)) : (F &> (prod.fst (𝟙 (X, Y)))) Y = 𝟙 ((F +> X) +> Y) :=
begin
  -- Really, `simp` should just work, finishing the goal.
  -- However this doesn't work:
  success_if_fail {simp},
  -- Notice that rewriting with that simp lemma succeeds:
  rw ProductCategory.identity,
  dsimp,
  -- Again, this `simp` fails:
  success_if_fail {simp},
  rw Functor.identities,
  -- Finally, at this stage `simp` manages to apply FunctorCategory.identity.components
  simp,
end

lemma test' (E : Type u) [ℰ : category E] (X : C) (Y : D) (F : C ↝ (D ↝ E)) : (F &> (prod.fst (𝟙 (X, Y)))) Y = 𝟙 ((F +> X) +> Y) :=
begin
  -- If we unfold all the coercions first, at least `simp` gets started
  unfold_coes,
  simp, 
  -- But doesn't finish, because with the coercions gone, FunctorCategory.identity.components doesn't apply anymore!
  admit
end

-- We can define an alternative version of that @[simp] lemma, with the coercion removed. 
@[simp] lemma FunctorCategory.identity.components' (F : C ↝ D) (X : C) : (𝟙 F : F ⟹ F).components X = 𝟙 (F +> X) := by refl

lemma test'' (E : Type u) [ℰ : category E] (X : C) (Y : D) (F : C ↝ (D ↝ E)) : (F &> (prod.fst (𝟙 (X, Y)))) Y = 𝟙 ((F +> X) +> Y) :=
begin
  unfold_coes,
  simp,
  -- At this stage, we've recovered reasonable automation, at the expense of having to
  -- state lemmas twice, once with the coercions (for the humans) and once without (for the simplifier).
end
````

#### [Mario Carneiro (Aug 06 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949286):
I've seen this issue before. Unfortunately `simp` does not rewrite inside coercions because they are apparently dependent functions (the nondependency is only visible after you unfold the definition)

#### [Scott Morrison (Aug 06 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949293):
Exactly!

#### [Scott Morrison (Aug 06 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949304):
This is related to why I was writing a `mk_congr_arg_using_dsimp` tactic [above](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/congr_arg.20and.20superficially.20dependent.20functions/near/130827909). (The idea being that if you `dsimp` the function first, sometimes you see that it's not actually a dependent function.)

#### [Mario Carneiro (Aug 06 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949367):
I would look into fixing the congr lemma generation to use this

#### [Scott Morrison (Aug 06 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949411):
Is that something which is fixable? Or is it frozen waiting for Lean 4?

#### [Mario Carneiro (Aug 06 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949414):
there is always the option of making `simp'`

#### [Scott Morrison (Aug 06 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949419):
I see. But isn't much of `simp` written in C++?

#### [Scott Morrison (Aug 06 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949428):
Could we make a patched `simp'` that had similar performance?

#### [Mario Carneiro (Aug 06 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949435):
probably not, but if you use it only when necessary it should be palatable

#### [Mario Carneiro (Aug 06 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949483):
I think you can use `ext_simplify_core` to hook into the traversal part without messing with the core of `simp`

#### [Scott Morrison (Aug 06 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949485):
eek... but my automation really relies on `simp` just doing its thing. As things are, I don't think there's any way to distinguish between the situations "simp failed to do anything" and "simp would have worked, but broke trying to construct a `congr_arg`"

#### [Scott Morrison (Aug 06 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949493):
So it's not like I could just write a tactic that says "do `simp`, unless that breaks, in which case retry with `simp'`".

#### [Scott Morrison (Aug 06 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949495):
Okay, I will investigate `ext_simplify_core` again. I once knew how that worked, but have forgotten.

#### [Mario Carneiro (Aug 06 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949551):
By the way, `dsimp` works under dependent functions

#### [Mario Carneiro (Aug 06 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949557):
so in particular it works in `test`

#### [Sebastian Ullrich (Aug 06 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949606):
Without having thought about it too hard, could a custom congr lemma for non-dependent coercions work?

#### [Mario Carneiro (Aug 06 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949607):
Does `simp` use `@[congr]` lemmas?

#### [Scott Morrison (Aug 06 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949628):
While I've got your attention on this, would you mind having a look at my [`mk_congr_arg_using_dsimp`](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/congr_arg.20and.20superficially.20dependent.20functions/near/130827909) and see if there is a way to avoid polluting the goal with extra hypotheses as a side effect? I'm pretty unhappy about that hack.

#### [Scott Morrison (Aug 06 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949672):
Yes; I know `dsimp` works fine, and indeed in my automation I always attempt `dsimp` before `simp`; sorry if this minimised example is too minimised, but I certainly have cases where `simp` is failing because of this effect.

#### [Scott Morrison (Aug 06 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949675):
@**Mario Carneiro**, sorry, I don't know what you mean by "Does `simp` use `@[congr]` lemmas?".

#### [Mario Carneiro (Aug 06 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949740):
Simp works by using congruence lemmas generated by `mk_congr_lemma` for traversal. If it also accepts user lemmas marked `@{congr]`, then this would solve all our problems, because we could craft congr lemmas for looking through apparently dependent functions

#### [Scott Morrison (Aug 06 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949748):
Ah, I see!

#### [Mario Carneiro (Aug 06 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949806):
Also, looking at the coercion in your example, it is in fact a dependent function:
```
instance {F G : C ↝ D} : has_coe_to_fun (F ⟹ G) :=
{ F   := λ α, Π X : C, (F +> X) ⟶ (G +> X),
  coe := λ α, α.components }
```
so why is this legitimate in this case?

#### [Sebastian Ullrich (Aug 06 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949818):
@**Mario Carneiro** I think so? https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/src/library/tactic/simplify.cpp#L739-L740 `simp` is the reason `[congr]` was introduced, afaik

#### [Scott Morrison (Aug 06 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949820):
The problem is that for particular values of `α`, that dependent function might `dsimp` to a non-dependent function.

#### [Mario Carneiro (Aug 06 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130949862):
I thought `[congr]` was used for `calc`

#### [Sebastian Ullrich (Aug 06 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130950017):
I'm not aware of `calc` using anything other than `[trans]`

#### [Scott Morrison (Aug 06 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130950538):
Are there any places I can look to find `@[congr]` used in conjunction with `simp`? I'm finding the C++ code pretty hard going.

#### [Scott Morrison (Aug 06 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130950675):
I guess I just found @**Gabriel Ebner**'s example at https://github.com/leanprover/lean/commit/6bd3fe24493c1748c8cfd778f63a3b832c6e6ba7#diff-db6c06d0649a66f8bbfc76e59b15cef2, but I'm still not sure what's going on. :-)

#### [Scott Morrison (Aug 06 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130951668):
Okay, I am for now failing to work out how to use @[congr] to help `simp` work better, or to write my own `simp'` that uses `ext_simplify_core`. I'm happy to continue investigating both options, and very happy if someone else does this. :-)

#### [Scott Morrison (Aug 06 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130951718):
In the meantime, could I propose, @**Johannes Hölzl** and @**Mario Carneiro**, that in my category theory PR we defer the issue of adding coercions for functors acting on objects, and not consider that an obstacle for merging this PR?

If we can solve the issue here, of course I would love to add these coercions. In the meantime, it is not very expensive to write out the coercions, or have notations for them. I would really like to get this PR done, without breaking the possibility of good automation.

#### [Mario Carneiro (Aug 06 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130951764):
Damn! I figured out what congr lemma to use, but lean doesn't accept it :/
```

@[congr] theorem NaturalTransformation.components_congr
  {F G : C ↝ D} {α β : F ⟹ G} (h : α = β) (X) : α.components X = β.components X :=
congr_fun (congr_arg coe_fn h) _
-- ok, generated automatically

@[congr] theorem NaturalTransformation.coe_congr
  {F G : C ↝ D} {α β : F ⟹ G} (h : α = β) (X) : α X = β X :=
congr_fun (congr_arg coe_fn h) _
-- invalid congruence lemma, 'NaturalTransformation.coe_congr' the left-hand-side of the congruence
-- resulting type must be of the form (coe_fn x_1 ... x_n), where each x_i is a distinct variable or a sort
```

#### [Mario Carneiro (Aug 06 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130951827):
even worse, the error is garbage because it didn't parse the statement correctly

#### [Mario Carneiro (Aug 06 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130951879):
notice that `congr` fails on this proof for completely the wrong reason:
```
theorem NaturalTransformation.coe_congr
  {F G : C ↝ D} {α β : F ⟹ G} (h : α = β) (X) : α X = β X :=
by do {
  tgt ← target,
  (lhs, rhs) ← match_eq tgt,
  guard lhs.is_app,
  clemma ← mk_specialized_congr_lemma lhs,
  trace clemma.type,
  apply_eq_congr_core tgt }
-- invalid apply tactic, failed to unify
--   ⇑α X = ⇑β X
-- with
--   ⇑?m_2 = ⇑?m_2
```

#### [Mario Carneiro (Aug 06 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130952264):
For the purpose of this PR, how about adding the coercions, but add a simp lemma that unfolds the coercions and make simp lemmas that don't use the coercions. That way users can use the coercions but they won't interfere with `simp`

#### [Mario Carneiro (Aug 06 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130952475):
@**Sebastian Ullrich** I think the coe_fn typeclass needs to be fixed so that lean knows it's a pi type:
```
class has_coe_to_fun (a : Sort u) : Sort (max u (v+1) (w+1)) :=
(dom : a → Sort v) (F : ∀ a, dom a → Sort w) (coe : Π x y, F x y)
```
I tried this modification in my local copy and it seems to work fine, but of course this requires a modification to core. Also related is an issue brought up by Floris a long time ago - `has_coe_to_sort` doesn't actually require that the target type is a sort. It should read:
```
class has_coe_to_sort (a : Sort u) : Type (max u v) :=
(coe : a → Sort v)
```
Any chance of at least getting these into lean 4?

#### [Scott Morrison (Aug 06 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130952782):
Okay, I will try out that approach. You're right that it will probably work. The only downside is that `simp` will produce 'ugly' output that looks different from what the humans are used to.

#### [Mario Carneiro (Aug 06 2018 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130952921):
of course it already does this enough that we have techniques like "use `simp` terminally" and "use `simpa`" to mitigate this problem

#### [Scott Morrison (Aug 06 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130953261):
Okay. So now I'm left with the question of how much _I_ should use the coercion in the library development.

#### [Scott Morrison (Aug 06 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130953269):
I'm inclined to barely use it! That is, provide the coercion, and a simp lemma that unfolds it, but otherwise ignore it.

#### [Scott Morrison (Aug 06 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130953275):
Is that okay? Or is that making life unpleasant for a user?

#### [Scott Morrison (Aug 06 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130953318):
The alternative is to carefully go through, introducing use of the coercion everywhere except in simp lemmas, I guess.

#### [Mario Carneiro (Aug 06 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130953809):
I think you should handle it like `sub`. Write lemmas using it, but also add simp lemma versions of the theorems when applicable

#### [Mario Carneiro (Aug 06 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130953855):
these should be one liners or restatements

#### [Mario Carneiro (Aug 06 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130953858):
the user will want to use coercions whenever possible, so there should be lemmas supporting this

#### [Mario Carneiro (Aug 06 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp inside expressions with coe_to_fun sometimes fails/near/130953864):
besides, I haven't lost hope of an automation solution to this, we're talking about a workaround here

