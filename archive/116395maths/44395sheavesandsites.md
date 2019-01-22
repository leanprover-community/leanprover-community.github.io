---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/44395sheavesandsites.html
---

## [maths](index.html)
### [sheaves and sites](44395sheavesandsites.html)

#### [Johan Commelin (Nov 08 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147299236):
Lol, I'm quite sure that the definition of `coverage` is wrong. I should demand that the collection of covers contains the singletons `{id : U ⟶ U}` for every `U : X`.

#### [Johan Commelin (Nov 08 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147299259):
If I'm right, this is also missing on nLab.

#### [Johan Commelin (Nov 12 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147532006):
I retract this. There is a comment on nLab pointing out that you don't need to demand that identity morphisms cover. It doesn't change your category of sheaves.

#### [Kenny Lau (Nov 12 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147532080):
did you say nlab...

#### [Kenny Lau (Nov 12 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147532144):
man you've gone too far...

#### [Johan Commelin (Nov 12 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147545193):
`opens X` is now a site!
https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheaf.lean#L245

#### [Johan Commelin (Nov 12 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147545202):
This is one of the ugliest proofs I've written in a long time.

#### [Johan Commelin (Nov 12 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147545468):
Also, I would like to get some feedback on the definition of the `covers` for `opens X`. This is the actual data that goes into a `site`. The rest doesn't matter, because it's only proofs. (They should of course be faster then what I have now.)
Basically, there are at least three (equivalent) ways to specify the data of `covers`:
1) `covers := λ U Us, U.val = ⨆u∈Us, (u:over _).left.val` — take the union in `set X`
2) `covers := λ U Us, U = ⨆u∈Us, (u:over _).left` — take the "union" in `opens X`
3) `covers := λ U Us, U = limits.sigma (λ u∈Us, (u:over _))` — take the "union" as a colimit in the category `over U`
Do people already see reasons to choose/discard one of these options?

#### [Johan Commelin (Nov 12 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147545537):
I currently have option (2). But maybe option (3) is actually better, even though it is high-brow; because it would tie in better to all the facts that we (will) have about functors/limits/etc...

#### [Reid Barton (Nov 12 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147547765):
I wonder whether using actual families (instead of `set` everywhere) would make your life easier

#### [Reid Barton (Nov 12 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147547907):
Maybe this isn't actually causing any difficulty

#### [Johan Commelin (Nov 12 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147548610):
Hmm, I had that before, and it actually became harder... also, you run into more universe issues, I think.

#### [Johan Commelin (Nov 13 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576521):
`sheaf.lean` is now `sorry`-free. In particular, I have defined the site on a basis of a topology.

#### [Kevin Buzzard (Nov 13 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576576):
@**Ramon Fernandez Mir** you might be interested in this. @**Johan Commelin** where is this work? Is it on github?

#### [Johan Commelin (Nov 13 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576586):
My todo-list:

* Clean up the proofs
* Prove that continuous functions to some space `T` form a sheaf on `X`
* Generalise to sheaves with values in `C` (e.g., `C = CommRing` or `Ab`)
* Define stalks
* Build an API around everything

#### [Johan Commelin (Nov 13 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576593):
https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheaf.lean

#### [Johan Commelin (Nov 13 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576745):
@**Scott Morrison|110087** Would you mind testing your most powerful version of `obviously` on (parts) of the proofs at the bottom of `sheaf.lean`? As you can see I'm mostly doing what `tidy` would do, except that I sprinkle an occasional `rw` into the mix.

#### [Johan Commelin (Nov 13 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576748):
(If you have time for this...)

#### [Scott Morrison (Nov 13 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576890):
Hi @**Johan Commelin** , we should combine/adapt the stuff I wrote on bundled presheaves at some point, with a category structure based on:
```
structure Presheaf :=
(X : Top.{v})
(𝒪 : (opens X)ᵒᵖ ⥤ C)

structure Presheaf_hom (F G : Presheaf.{u v} C) :=
(f : F.X ⟶ G.X)
(c : G.𝒪 ⟹ ((opens.map f).op ⋙ F.𝒪))
```

#### [Scott Morrison (Nov 13 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576895):
Am I right that you haven't got this yet?

#### [Scott Morrison (Nov 13 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147576897):
I think most of the other stuff I'd done previously on sheaves is all obsolete by your recent progress.

#### [Johan Commelin (Nov 13 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147577022):
(I don't have stalks yet :lol:)

#### [Johan Commelin (Nov 13 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147577025):
Why would you want the bundled presheaves?

#### [Johan Commelin (Nov 13 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147577047):
To define morphisms of ringed spaces?

#### [Johan Commelin (Nov 13 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147577051):
I think I would first do that unbundled.

#### [Johan Commelin (Nov 13 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147577899):
Hmmm, I just realised that I don't even know what it means to be a sheaf with values in `C` when working on an arbitrary site.
I can make sense of it
* if the site has pullbacks, or
* if `C` is *concrete* in the sense that it comes with a forgetful functor to `Type`.

#### [Johan Commelin (Nov 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147578584):
@**Mario Carneiro** Do you have any tips on what the right "go-for-it" route would be in this case?

#### [Johan Commelin (Nov 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147578592):
We want sheaves of rings.
There are 23 definitions that are all math-equivalent.

#### [Harry Gindi (Nov 13 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580288):
There's no way to do it as a ring object in sheaves?

#### [Johan Commelin (Nov 13 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580305):
That is one of the 23 possibilities (-;

#### [Johan Commelin (Nov 13 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580313):
But then you need to connect it to all the useful things that we know already about rings.

#### [Johan Commelin (Nov 13 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580320):
This is math-trivial, of course

#### [Harry Gindi (Nov 13 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580363):
A lot of them aren't true for sheafy rings

#### [Johan Commelin (Nov 13 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580367):
But now you actually need to justify it to a computer.

#### [Johan Commelin (Nov 13 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580381):
Sure, but there is an extremely large bunch of trivialities that are true

#### [Harry Gindi (Nov 13 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580399):
Is there any way to work with sheaves directly as nonclassical types?

#### [Harry Gindi (Nov 13 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580463):
so that all of the theorems for rings that don't use classical assertions hold?

#### [Johan Commelin (Nov 13 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580575):
What exactly do you mean?

#### [Johan Commelin (Nov 13 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580580):
Working internally in some topos?

#### [Johan Commelin (Nov 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580598):
Or you want to lift all constructive results into every topos?

#### [Johan Commelin (Nov 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580615):
Nothing like that currently exists. And pulling it off would be quite a non-trivial project.

#### [Harry Gindi (Nov 13 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580710):
Yeah, I agree

#### [Johan Commelin (Nov 13 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580756):
@**Scott Morrison|110087** Do you think the current definition of `sheaf` is ok?
```lean
def sheaf (X : Type u) [𝒳 : site.{u} X] :=
{ F : presheaf X (Type u) // nonempty (site.sheaf_condition F) }
```
I need the ugly `nonempty` because `is.iso` is not a `Prop`. What is the correct Lean-idiom for this?

#### [Scott Morrison (Nov 13 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580770):
Why not just use a sigma type?

#### [Scott Morrison (Nov 13 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580779):
The category of presheaves will not care about the evidence you provide

#### [Johan Commelin (Nov 13 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580780):
I want to use `full_subcategory`

#### [Johan Commelin (Nov 13 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580787):
But maybe I shouldn't?

#### [Scott Morrison (Nov 13 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580792):
so use `sigma_category`, which I think hasn't landed in mathlib

#### [Scott Morrison (Nov 13 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580795):
but is the same idea, it just ignores the extra data

#### [Scott Morrison (Nov 13 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580839):
If you think about it, this is a perfectly sensible thing to do categorically:

#### [Johan Commelin (Nov 13 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580842):
Ok... I see. Which branch do I need to merge into `sheaf` to do that?

#### [Johan Commelin (Nov 13 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580848):
Yeah, the idea is obvious. I just didn't want to roll my own tooling.

#### [Scott Morrison (Nov 13 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580850):
you can have something that acts as a full subcategory, but actually makes many copies of the objects that you're keeping, according to the different ways to witness that you want them ...

#### [Johan Commelin (Nov 13 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580854):
/me is lazy...

#### [Scott Morrison (Nov 13 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580860):
I think it's only in `lean-category-theory`

#### [Scott Morrison (Nov 13 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580862):
so it's not just merging a branch

#### [Johan Commelin (Nov 13 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580876):
Aaah, then I'll leave a TODO above the current definition.

#### [Harry Gindi (Nov 13 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580886):
Is there documentation for what a sigma-category is?

#### [Scott Morrison (Nov 13 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580896):
Copy and paste
```
instance sigma_category (Z : C → Type w₁) : category.{(max u₁ w₁) v₁} (Σ X : C, Z X) := 
{ hom  := λ X Y, X.1 ⟶ Y.1,
  id   := λ X, 𝟙 X.1,
  comp := λ _ _ _ f g, f ≫ g }

def sigma_category_inclusion (Z : C → Type u₁) : (Σ X : C, Z X) ⥤ C := 
{ obj := λ X, X.1,
  map' := λ _ _ f, f }

instance full_σ        (Z : C → Type u₁) : full    (sigma_category_inclusion Z)    := by obviously
instance faithful_σ    (Z : C → Type u₁) : faithful (sigma_category_inclusion Z)   := by obviously
```

#### [Scott Morrison (Nov 13 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580925):
into full_subcategory.lean?

#### [Harry Gindi (Nov 13 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147580958):
does it have a non-type-theoretic analogue?

#### [Johan Commelin (Nov 13 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581050):
Sure, but I don't know if it actually occurs.

#### [Scott Morrison (Nov 13 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581091):
Sure. Say you have a set of objects C, and a function f : C \to Set. Make a new category with objects (X, Y), where Y is in f(X), and whose morphisms (X, Y) to (X', Y') are just the C-morphisms from X to X'.

#### [Johan Commelin (Nov 13 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581094):
It would be like taking the category of groups with all functions as morphisms

#### [Scott Morrison (Nov 13 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581095):
Does it have a name?

#### [Scott Morrison (Nov 13 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581105):
It just makes f(X) many copies of the object X.

#### [Harry Gindi (Nov 13 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581171):
it looks like it's related to the 'anafunctor' version of a subcategory?

#### [Johan Commelin (Nov 13 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581204):
@**Harry Gindi** Here is a math question that I don't know the answer to. In what generality do people speak of sheaves on a site $$X$$ with values in a category $$C$$?
What assumptions do I need to make on $$X$$ and/or $$C$$? Is there some grand theory that unifies everything?

#### [Harry Gindi (Nov 13 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581290):
people sometimes say "sheaves of X" in all kinds of cases, but it only makes sense when X is a subcategory of algebras for some algebraic theory rel set

#### [Johan Commelin (Nov 13 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581304):
Well, if the site $$X$$ has pullbacks, then I guess the sheaf condition makes sense in every category $$C$$ with equalizers, right?

#### [Harry Gindi (Nov 13 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581351):
yes, but it is usually the wrong thing

#### [Johan Commelin (Nov 13 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581356):
Ok, so it works but is useless.

#### [Harry Gindi (Nov 13 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581368):
I think so, yes

#### [Johan Commelin (Nov 13 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581438):
Ok, I'll have to think a bit about how to move this forward. I'm not sure if I'm ready for defining all the stuff related to algebraic theories.

#### [Harry Gindi (Nov 13 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581522):
It might make more sense if you could relativize algebraic stuff to like parameterized types?

#### [Harry Gindi (Nov 13 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581530):
I don't know, it's really alien to me

#### [Harry Gindi (Nov 13 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581550):
probably the easiest way is as you said

#### [Harry Gindi (Nov 13 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581604):
when the category is concrete, being a sheaf with values in C is the same thing as asking that the underlying sheaf of sets is a sheaf

#### [Harry Gindi (Nov 13 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581646):
I don't know how well that works with e.g. a sheaf of complexes

#### [Harry Gindi (Nov 13 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581741):
which is like the most important application of sheafy stuff in alg. geom, I think

#### [Scott Morrison (Nov 13 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581744):
You have to be pretty careful with this statement. It's not just "concrete" (e.g. topological rings have a faithful functor to Set) You also need that the forgetful functor is continuous and reflects isos.

#### [Scott Morrison (Nov 13 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581830):
At some point I wrote down the statement, but never attempted to prove it:
```
variables {V : Type (u+1)} [𝒱 : large_category V] [has_products.{u+1 u} V] (ℱ : V ⥤ (Type u))
          [faithful ℱ] [category_theory.limits.preserves_limits ℱ] [reflects_isos ℱ]
include 𝒱

-- This is a good project!
def sheaf.of_sheaf_of_types
  (presheaf : (opens X)ᵒᵖ ⥤ V)
  (underlying_is_sheaf : is_sheaf (presheaf ⋙ ℱ)) : is_sheaf presheaf := sorry

```

#### [Scott Morrison (Nov 13 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581858):
(This won't be compatible with Johan's version of presheaves and sheaves, of course.)

#### [Harry Gindi (Nov 13 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581877):
I wonder if a good way to do this is with internal objects in a topos after all

#### [Harry Gindi (Nov 13 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581886):
then you could try to follow Hakim's thesis

#### [Johan Commelin (Nov 13 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581986):
I challenge you to try it :smiley:

#### [Harry Gindi (Nov 13 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147581991):
I don't understand how you can say something like categories of nonclassical types satisfyinf Giraud's axioms are categories of sheaves on a site

#### [Johan Commelin (Nov 13 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582038):
What do you mean?

#### [Harry Gindi (Nov 13 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582050):
like, we might want to work internally to some Grothendieck topos

#### [Harry Gindi (Nov 13 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582065):
and the objects there would hopefully be of type "type"

#### [Johan Commelin (Nov 13 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582066):
Sure. And `Type` is equivalent to sheaves on `unit`

#### [Johan Commelin (Nov 13 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582076):
No, for an arbitrary topos the type of the objects wouldn't be `Type`

#### [Johan Commelin (Nov 13 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582123):
They would be of type `X`, where `X` is your topos.

#### [Harry Gindi (Nov 13 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582126):
then how can you transfer results from type type to type sheafy type

#### [Johan Commelin (Nov 13 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582129):
And so you have to develop all of type theory internal to topoi. And this hasn't been done yet in Lean. And I don't think it has been done in any theorem prover.

#### [Johan Commelin (Nov 13 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582142):
To do that "transfer" you would have to build quite a bit of machinery.

#### [Harry Gindi (Nov 13 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582145):
exactly, it looks daunting

#### [Johan Commelin (Nov 13 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582151):
Very daunting

#### [Johan Commelin (Nov 13 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582160):
It would take Mario a whole summer, I'm afraid.

#### [Harry Gindi (Nov 13 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582218):
one way to do it, maybe, would be to try to prove that any nonclassical theorem in type type holds when you substitute type X for type type when X is a topos?

#### [Harry Gindi (Nov 13 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582233):
it's not easy

#### [Harry Gindi (Nov 13 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582320):
It would probably be highly rewarding in terms of work saved

#### [Harry Gindi (Nov 13 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147582598):
I should probably look in e.g. the elephant to see if there is a statement of such a theorem

#### [Mario Carneiro (Nov 13 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147583484):
I'm afraid I have no idea about the math in this area

#### [Mario Carneiro (Nov 13 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147583499):
I'm not sure how much of it is important to the modeling question

#### [Mario Carneiro (Nov 13 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147583644):
```quote
Hmmm, I just realised that I don't even know what it means to be a sheaf with values in `C` when working on an arbitrary site.
I can make sense of it
* if the site has pullbacks, or
* if `C` is *concrete* in the sense that it comes with a forgetful functor to `Type`.
```
 Are these two definitions related to each other? Harry says this is not the right notion in some categories?

#### [Mario Carneiro (Nov 13 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147583678):
If there is a reasonable categorical interpretation of the sheaf operations or what not then that seems like a good place to start

#### [Mario Carneiro (Nov 13 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147583745):
but it sounds like a "sheaf of rings" is not a sheaf over `Ring` as I would hope, but rather a ring object in sheaves... unfortunately I don't know any way of relating rings and ring objects in a suitably algorithmic way

#### [Mario Carneiro (Nov 13 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147583842):
that is, you can define a group object, ring object etc but nothing about these definitions will connect them to the usual algebraic classes, and there won't be a general procedure for inputting a universal algebra and getting a predicate in category theory language

#### [Mario Carneiro (Nov 13 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147583872):
and "internalization" is not something we can currently do in a nice way, although maybe a tactic could do it in the future

#### [Johan Commelin (Nov 13 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147585448):
@**Mario Carneiro** Thanks for your input. I think Harry is saying that it would be best to go for the option with *concrete* categories, and Scott already gave a mockup of the statement.

#### [Johan Commelin (Nov 13 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147585465):
You are right that a sheaf of rings is a ring object in sheaves. (At least that is one way to define it.)

#### [Harry Gindi (Nov 13 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147585780):
I asked a colleague of mine who specializes in topos theory (and has lots of experience with Lean, but the HOTT branch)

#### [Harry Gindi (Nov 13 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147585838):
oh yeah, he's here, Jonas

#### [Harry Gindi (Nov 13 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147585865):
@**Jonas Frey**

#### [Johan Commelin (Nov 13 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147586499):
I imagine that a bunch of these problems would go away when using HoTT + univalence

#### [Harry Gindi (Nov 13 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589162):
@**Mario Carneiro** I was saying that the notion of a sheaf with values in a category that isn't 'algebraic' in some sense is bad

#### [Mario Carneiro (Nov 13 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589170):
so what does "algebraic" mean here?

#### [Harry Gindi (Nov 13 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589185):
admits a finite limit sketch over set, I believe

#### [Mario Carneiro (Nov 13 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589194):
like what are some simple examples?

#### [Harry Gindi (Nov 13 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589196):
sheaves of categories are bad, for example

#### [Mario Carneiro (Nov 13 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589202):
I'm not really sure what the applications are here, what kinds of sheaves are good?

#### [Harry Gindi (Nov 13 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589247):
the right notion for a sheaf of categories has additional coherence conditions (cocycle conditions) that make them stacks

#### [Mario Carneiro (Nov 13 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589258):
but I presume these don't come up in the usual cases for some reason?

#### [Harry Gindi (Nov 13 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589259):
good categories for sheaves: groups, rings, abgroups, things of that nature

#### [Harry Gindi (Nov 13 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589270):
yeah, basically

#### [Mario Carneiro (Nov 13 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589330):
So is the "data" of a sheaf all present in an arbitrary category?

#### [Mario Carneiro (Nov 13 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589340):
or does pullbacks suffice?

#### [Mario Carneiro (Nov 13 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589364):
and somehow in a "good" category these operations have additional properties that make it work

#### [Harry Gindi (Nov 13 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589374):
(deleted)

#### [Harry Gindi (Nov 13 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589430):
sorry, all products

#### [Harry Gindi (Nov 13 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589438):
because you can have infinite covering families

#### [Mario Carneiro (Nov 13 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589448):
I think the easy route would be to define what a sheaf is in an arbitrary category with the constructions needed in the definition itself, and then add appropriate regularity conditions for the theorems (or just prove the theorems in particular categories when needed)

#### [Mario Carneiro (Nov 13 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589497):
I would imagine that it will be easy to retrofit the theorems with more generality as needed

#### [Harry Gindi (Nov 13 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589498):
Scott's version works better than that

#### [Harry Gindi (Nov 13 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589514):
it hits all of the ones we care about

#### [Mario Carneiro (Nov 13 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589516):
I'm not sure how well "concrete categories" in the literal sense of functors to Type work in lean

#### [Mario Carneiro (Nov 13 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589536):
Scott can say better than me

#### [Harry Gindi (Nov 13 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589604):
the key feature of sheaves and presheaves is exactly that they are set-valued and the sheaf condition says something about sets

#### [Harry Gindi (Nov 13 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589691):
having a continuous conservative functor to sets is always satisfied when the category is monadic over sets

#### [Kevin Buzzard (Nov 13 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589726):
In the perfectoid project we need sheaves of topological rings

#### [Harry Gindi (Nov 13 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589741):
hmm, how are those even defined?

#### [Harry Gindi (Nov 13 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589793):
that was exactly the example Scott said would be problematic (topological groups)

#### [Kevin Buzzard (Nov 13 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589800):
well we only need them on topological spaces, so I think there are no technical issues...

#### [Harry Gindi (Nov 13 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589829):
Are they pro-rings like completions?

#### [Harry Gindi (Nov 13 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589933):
Can I see where these are defined in ordinary mathematical language?

#### [Kevin Buzzard (Nov 13 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147589942):
Actually there might be some topological issue. Wait a minute, I'll dig up a reference

#### [Kevin Buzzard (Nov 13 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590004):
https://www2.math.uni-paderborn.de/fileadmin/Mathematik/People/wedhorn/Lehre/AdicSpaces.pdf  remark 8.19 on p80

#### [Kevin Buzzard (Nov 13 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590030):
The map from F(U) to the stuff in prod_i F(U_i) which agree on overlaps needs to be a homeo rather than just continuous

#### [Kevin Buzzard (Nov 13 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590087):
I think that this is probably exactly the sheaf axiom for top rings

#### [Harry Gindi (Nov 13 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590088):
Yeah, I think you could get away with this because they're adic rings

#### [Kevin Buzzard (Nov 13 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590092):
I am not sure this has anything to do with it

#### [Kevin Buzzard (Nov 13 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590112):
I think that the point is that to check that a presheaf of top rings is a sheaf, it does not suffice to check that the underlying presheaf of rings is a sheaf

#### [Kevin Buzzard (Nov 13 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590123):
there is epsilon more to it than this.

#### [Harry Gindi (Nov 13 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590125):
well, continuous maps between adic rings are the natural transformations between pro-objects

#### [Kevin Buzzard (Nov 13 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590130):
These rings are not adic rings in general

#### [Harry Gindi (Nov 13 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590170):
ah

#### [Kevin Buzzard (Nov 13 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590189):
They are what used to be called "f-adic", which is _not_ "adic + ...", it's "has a subring which is adic + ..."

#### [Harry Gindi (Nov 13 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590197):
mhm

#### [Kevin Buzzard (Nov 13 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590202):
They're now called Huber rings

#### [Kevin Buzzard (Nov 13 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590220):
(terminology due to Scholze)

#### [Mario Carneiro (Nov 13 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590238):
When I said concrete categories in the literal sense I was comparing to categories that are built on actual sets and functions

#### [Harry Gindi (Nov 13 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590242):
yeah, this looks like a special situation that isn't usually covered in the classical theory, I think

#### [Mario Carneiro (Nov 13 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590282):
in which case the forgetful functor is implicit

#### [Mario Carneiro (Nov 13 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590317):
there is quite a lot you can do with concrete categories built like this

#### [Harry Gindi (Nov 13 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590355):
in that case, Kevin, maybe the answer is to do a common generalization that covers the usual situation and the one for perfectoid spaces.

#### [Harry Gindi (Nov 13 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590421):
There are also simplicial sheaves, which have a separate homotopy-theoretic component

#### [Harry Gindi (Nov 13 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590456):
but that way lies madness

#### [Harry Gindi (Nov 13 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147590545):
and you'd end up trying to do everything in this article: https://ncatlab.org/nlab/show/model+structure+on+simplicial+presheaves#injectiveprojective__localglobal__presheavessheaves

#### [Johan Commelin (Nov 13 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591580):
@**Mario Carneiro** I hope the following code is parseable
```lean
T : Top,
U : opens X,
Us : covering_family U,
this : Π (u : over U), u ∈ Us → (opens.to_Top.obj (u.left) ⟶ T)
⊢ opens.to_Top.obj (⨆ (u : over U) (H : u ∈ Us), u.left) ⟶ T
```
Do you know if we have any stuff in topology that would help here?

#### [Johan Commelin (Nov 13 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591673):
What this is saying is: I have a bunch of functions to `T` defined on `u`s that cover `U`. Now I want to build a function `U` to `T`.

#### [Johan Commelin (Nov 13 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591691):
Of course we need that they agree on overlaps. This is hidden in my context, but it looks ugly, so I didn't paste it.

#### [Johan Commelin (Nov 13 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591712):
Ok, so here is a more precise question: how do I check continuity locally?

#### [Mario Carneiro (Nov 13 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591776):
as with opens, I think you want a covering_family U to be a type

#### [Harry Gindi (Nov 13 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591791):
Can sieves make life easier?

#### [Harry Gindi (Nov 13 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591847):
because then you might just prove that every covering family determines a sieve

#### [Mario Carneiro (Nov 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591941):
why do sheaf and sieve and stack and site all sound so similar? the alliteration is killing me

#### [Johan Commelin (Nov 13 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147591998):
```quote
because then you might just prove that every covering family determines a sieve
```
 I am already using sieves.

#### [Harry Gindi (Nov 13 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592041):
ah, I see, that's good. Much easier to state the sheaf condition that way!

#### [Johan Commelin (Nov 13 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592046):
Mario, I was quite happy with `covering_family` being a set. But maybe it should be a type.

#### [Johan Commelin (Nov 13 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592069):
```quote
ah, I see, that's good. Much easier to state the sheaf condition that way!
```
 Sure, but now I need to actually prove that something is a sheaf :scream:

#### [Mario Carneiro (Nov 13 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592196):
that statement parses, but it isn't provable without stuff about compatibility

#### [Harry Gindi (Nov 13 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592207):
test case: Every representable is a sheaf wrt the topology generated by universal epimorphic families?

#### [Johan Commelin (Nov 13 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592302):
@**Mario Carneiro** Hence my more precise question...

#### [Johan Commelin (Nov 13 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592369):
@**Harry Gindi** Indeed. I'm proving that continuous functions `X → T` form a sheaf on `X`, for a given `T`.

#### [Johan Commelin (Nov 13 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592388):
So it is not as general as your test case.

#### [Harry Gindi (Nov 13 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592452):
I guess then you'd first have to define universal epimorphic families 😛

#### [Johan Commelin (Nov 13 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592469):
Feel free to join in :joy_cat:

#### [Harry Gindi (Nov 13 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592486):
Talk is cheap, that's why I do it so often

#### [Kenny Lau (Nov 13 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592586):
let's just define the spectrum of a ring fist

#### [Kenny Lau (Nov 13 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592590):
(sorry, I'm a more concrete guy)

#### [Johan Commelin (Nov 13 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592607):
I'm working on it Kenny. I'm trying to define ringed spaces.

#### [Harry Gindi (Nov 13 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592667):
Hom_CRing(R, -): Ring->Set; where's my big novelty check

#### [Johan Commelin (Nov 13 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592724):
Harry, one of the first things you learn when working with provers is that there are lots of definitions that are math-trivially equivalent. But proving that they are equivalent in Lean is often very hard.

#### [Johan Commelin (Nov 13 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592742):
I'm quite sure that there is value in defining a functor from `Ring^op` to `LRS`.

#### [Harry Gindi (Nov 13 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147592797):
I know, I'm being silly. This definition I just gave is meaningless even outside a theorem prover

#### [Harry Gindi (Nov 13 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147593491):
Just saw this on MathOverflow, could be a useful guide: https://rawgit.com/iblech/internal-methods/master/notes.pdf

#### [Harry Gindi (Nov 13 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147593526):
especially if you decide to go down the internal logic route

#### [Reid Barton (Nov 13 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594050):
@**Johan Commelin**, not sure how much progress you made on your gluing continuous functions question, but step 1 is to just construct the glued function even as a function, i.e., disregarding the topology of X, and then check that the glued function actually restricts to the original guys

#### [Reid Barton (Nov 13 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594103):
then step 2 would be to check continuity, possibly you can use `continuous_subtype_nhds_cover` for this

#### [Reid Barton (Nov 13 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594119):
You might find https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/homotopy_theory/topological_spaces/inter_union.lean a useful guide though there I was only interested in the case of two (closed) subsets

#### [Johan Commelin (Nov 13 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594216):
Ok, thanks for the tips.

#### [Reid Barton (Nov 13 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594217):
Step 1 will require `choice`

#### [Johan Commelin (Nov 13 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594225):
I'm currently trying to build a function.

#### [Johan Commelin (Nov 13 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594238):
And I haven't come to the point yet where I need choice. But I think I'm close

#### [Patrick Massot (Nov 13 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594245):
I think this was already discussed here, with a student of Kevin

#### [Patrick Massot (Nov 13 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594486):
https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/Topology.20-.20Beginner/near/130051069

#### [Kevin Buzzard (Nov 13 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594545):
@**Luca Gerolla**  wanted to define a continuous function on a closed interval [0,1] by glueing continuous functions on [0,1/2] and [1/2,1]

#### [Patrick Massot (Nov 13 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594557):
exactly

#### [Patrick Massot (Nov 13 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594564):
hopefully this is what I linked to

#### [Harry Gindi (Nov 13 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594583):
I can't get that link to work on mobile

#### [Johan Commelin (Nov 13 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594681):
Thanks @**Patrick Massot**, your memory is better than mine.

#### [Reid Barton (Nov 13 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594772):
I realize that maybe it's not very obvious what the module I linked to is doing--it's showing that for $$A_0$$, $$A_1$$ closed subsets of a space X, there is a pushout square in Top involving $$A_0 \cap A_1$$, $$A_0$$, $$A_1$$, $$A_0 \cup A_1$$. For open subsets you would use the other lemma from topology I mentioned, and then it's the same as checking the sheaf condition I guess.

#### [Harry Gindi (Nov 13 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594850):
@**Reid Barton** you have to use AC to construct glued maps?

#### [Harry Gindi (Nov 13 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594873):
that's surprising to me

#### [Harry Gindi (Nov 13 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594918):
or is this "choice" different from the axiom of choice?

#### [Reid Barton (Nov 13 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594921):
You could construct a glued map on the quotient type (the disjoint union of the subsets) modulo (points with the same image in X) without choice

#### [Reid Barton (Nov 13 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594980):
Ah, it is a bit different from the axiom of choice

#### [Reid Barton (Nov 13 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147594988):
In Lean, basically, `choice` = nonconstructive

#### [Harry Gindi (Nov 13 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595010):
so how do intuitionists glue maps?

#### [Reid Barton (Nov 13 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595116):
You need `choice` to go from "for each x there exists a y such that ..." to a function mapping x to the corresponding y, even if you know that the corresponding y is also unique. So in that sense it's not exactly analogous to the axiom of choice in ZFC

#### [Reid Barton (Nov 13 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595178):
I don't know. I guess you could try to replace "subset of X" by "map to X whose fibers are subsingletons", but I don't know how far you would get with that.

#### [Johan Commelin (Nov 13 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595313):
I think I want my covers to be defined as `U = colimit u \in Us`. Then this sort of problems would go away.

#### [Reid Barton (Nov 13 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595319):
I have this picture in my mind of $$A_0 \times \{0\} \cup (A_0 \cap A_1) \times [0, 1] \cup A_1 \times \{1\}$$ projecting to $$A_0 \cup A_1 \subset X$$, and not admitting a continuous section over $$A_0 \cup A_1$$. Don't know if it means anything though.

#### [Mario Carneiro (Nov 13 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595430):
I think I gave a proof that gluing in arbitrary topological spaces requires choice using roughly that example

#### [Reid Barton (Nov 13 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595436):
@**Mario Carneiro** had a nice example arguing that you really need something noncomputable to glue functions which is ... right.

#### [Mario Carneiro (Nov 13 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595494):
where by "choice" I mean unique choice

#### [Mario Carneiro (Nov 13 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595558):
lean doesn't really distinguish between AC, unique choice and LEM

#### [Mario Carneiro (Nov 13 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595575):
they all follow from the same axiom

#### [Harry Gindi (Nov 13 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147595737):
Can you glue maps of locales without choice?

#### [Ramon Fernandez Mir (Nov 13 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596063):
I've actually been looking into it. It's in the sheaf branch on the community mathlib.

#### [Johan Commelin (Nov 13 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596097):
So now I have this goal:
```lean
(⨆ (u : {x // x ∈ Us}), (u.val).left) = ⨆ (u : over U) (H : u ∈ Us), u.left
```
@**Mario Carneiro** will say: "I told you that `covering_family U` should be a type." But it's not (at the moment). How do I solve silly goals like this?

#### [Johan Commelin (Nov 13 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596117):
@**Ramon Fernandez Mir** Good to see you!

#### [Mario Carneiro (Nov 13 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596119):
There is a rewrite rule for this

#### [Johan Commelin (Nov 13 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596132):
I want `rewrite_search`...

#### [Mario Carneiro (Nov 13 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596236):
`supr_subtype`

#### [Luca Gerolla (Nov 13 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596268):
```quote
@**Luca Gerolla**  wanted to define a continuous function on a closed interval [0,1] by glueing continuous functions on [0,1/2] and [1/2,1]
```
 Indeed, I was dealing with continuous functions on two closed sets $$ V, U$$ (where $$U, V$$ cover the overall domain $$X$$) agreeing on their intersection $$ U \cap  V$$  and I needed to construct a continuous function $$ X \to Y $$. The code (mainly done by Mario and Kevin) is at https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Material/pasting_lemma.lean. 
Although dealing with a general covering I don't know if it can be of any help.

#### [Kenny Lau (Nov 13 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596340):
@**Luca Gerolla** wrong thread?

#### [Mario Carneiro (Nov 13 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596355):
I don't think so

#### [Kenny Lau (Nov 13 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596373):
what's Luca doing on an nlab thread...

#### [Johan Commelin (Nov 13 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596381):
He's on a thread about gluing functions.

#### [Kenny Lau (Nov 13 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596382):
`\cap` $$\cap$$

#### [Johan Commelin (Nov 13 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596387):
His post is about gluing functions.

#### [Luca Gerolla (Nov 13 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147596829):
Also continous_if (from mathlib - topology.continuity) turned out  very useful when I had just and ite function. 
Look forward to seeing the solution to this more general pasting :)

#### [Johan Commelin (Nov 13 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147598973):
@**Scott Morrison|110087** Here is something that I find a bit annoying to do. I'm trying to prove that the following functor preserves colimits:
```lean
def to_Top : opens X ⥤ Top :=
{ obj := λ U,
          { α := U.val,
            str := subtype.topological_space },
  map := λ U V i, ⟨λ x, ⟨x.1, (plift.down (ulift.down i)) x.2⟩,
    (embedding.continuous_iff embedding_subtype_val).mpr continuous_subtype_val ⟩ }
```
Here is what I have so far:
```lean
def to_Top.preserves_colimits : preserves_colimits (@to_Top X _) :=
{ preserves := λ J _ K c hc,
  { desc := λ s, _ } }
```
The local context is now:
```lean
X : Type u,
_inst_1 : topological_space X,
J : Type u,
_x : small_category J,
K : J ⥤ opens X,
c : limits.cocone K,
hc : limits.is_colimit c,
s : limits.cocone (K ⋙ to_Top)
⊢ (functor.map_cocone to_Top c).X ⟶ s.X
```
The annoying thing is the pair `c, hc`. I would much rather work with `hc : has_colimit K` and `c : colimit K`. Because then I can use facts about how this colimit is defined. Of course I can build a unique isomorphism between the `c` that I got from Lean and the one that I'm interested in. But I wonder if it would make sense to change the setup a bit...

#### [Johan Commelin (Nov 13 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599173):
I've pushed all that I have so far. Now I need to start packing to catch a train.

#### [Johan Commelin (Nov 13 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599192):
If anyone has good ideas, or wants to refactor this, please go ahead!

#### [Johan Commelin (Nov 13 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599215):
I'm just trying to push this category stuff to the limit (no pun intended)

#### [Reid Barton (Nov 13 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599555):
I think we can just add a lemma for that.
You're saying you want to prove: if F : C -> D and C already `has_colimits`, then to prove F preserves colimits it suffices to consider the ones provided by the `has_colimits` instance.

#### [Johan Commelin (Nov 13 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599626):
Yes, but why not just always condider the one provided by `has_colimit K`, where `K` is a diagram.

#### [Patrick Massot (Nov 13 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599634):
```quote
I'm just trying to push this category stuff to the limit (no pun intended)
```
 When we'll have that `to_dual` tactic, you'll be able to pull this category stuff to the colimit without any extra effort!

#### [Reid Barton (Nov 13 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599670):
Because the concept of preserving colimits doesn't depend on a choice of colimits

#### [Johan Commelin (Nov 13 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599690):
I see... you're probably right. I don't yet fully grasp the details of the API

#### [Johan Commelin (Nov 13 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147599771):
But your suggested lemma would also fix this problem.

#### [Kevin Buzzard (Nov 13 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147601888):
@**Johan Commelin** @**Kenny Lau** -- @**Ramon Fernandez Mir** asks me exactly what you are going to be doing regarding Spec of a ring. Ramon is supposed to be completely refactoring the scheme project as part of his MSc thesis; I got him to look at locally ringed spaces but now these are done modulo the assertion that the category of rings has all colimits. Then Kenny mentioned Spec -- I think it would just be less nervy for us if we knew exactly what you guys were planning on doing and what Ramon can do (he has written thousands of lines of Coq code but is new to Lean). Currently we need that colimits exist in the category of commutative rings, and that the spectrum of a ring is a locally ringed space (which of course is a lot of work, even though it's in some sense done already). The first step towards this is that the spectrum of a ring has a presheaf of rings on the basis of open sets $$D(f)$$. Shall I tell him to do this or will someone else do it by the weekend? It would be good if we could work together on this (although of course there is plenty plenty to do -- e.g. this Gamma Spec adjointness is a goal I have in mind for Ramon, something Johan suggested months ago -- and products of schemes is another thing).

#### [Kevin Buzzard (Nov 13 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147602049):
Of course I know all of this is already done in the schemes project -- the point is that we want to do it as a test of the category theory stuff; in the past we did it all "by hand".

#### [Kevin Buzzard (Nov 13 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147604152):
I think I know how to prove that colimits exist in the category of commutative rings -- can I get Ramon to do this or @**Kenny Lau** are you likely do just randomly do this at some point in the next few days?

#### [Kevin Buzzard (Nov 13 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147604211):
It will be quite a good stress test of Johannes' multivariable polynomial work I think.

#### [Johan Commelin (Nov 13 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611121):
@**Kevin Buzzard** Yes, collaboration is good. I have no intention to "mow away the grass" before Ramon's feet.
Here is a question for you: do you intend to make things mathlib-ready? Is the endgoal a PR to mathlib?

My goal is to get a theory of sheaves that is ready for the perfectoid project.

#### [Johan Commelin (Nov 13 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611202):
Concerning colimits in CommRing: do all of them exist? Or only the directed ones?

#### [Kevin Buzzard (Nov 13 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611234):
I convinced myself this afternoon that they all existed

#### [Johan Commelin (Nov 13 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611284):
Sheaves of rings seems to be a bit of an issue. I'm not yet sure how to define them. Once we have those, I'll leave it up to Ramon to define LRS. I will not touch `Spec` or anything close to it (-;

#### [Reid Barton (Nov 13 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611297):
They do all exist

#### [Johan Commelin (Nov 13 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611305):
I do intend to define stalks. So I might get close to LRS...

#### [Kevin Buzzard (Nov 13 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611313):
via some big standard universal construction -- given a diagram in CommRing, let T0 be the polynomial ring over Z with variables the disjoint union of all the rings in the diagram, and then quotient out by the relations making all of the canonical maps ring homs

#### [Johan Commelin (Nov 13 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611342):
I would not mind at all if Ramon works on a branch of community mathlib and regularly pull and pushes to the `sheaf` branch.

#### [Kevin Buzzard (Nov 13 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611388):
The "bad" news is that this all seems to be some special case of some big theory due to Lawvere and we could spend forever formalising that instead

#### [Kevin Buzzard (Nov 13 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611425):
(existence of limits and colimits in some big gneerality for some algebraic categories or something)

#### [Johan Commelin (Nov 13 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611521):
Right. So we just do rings by hand first. Like you did schemes by hand first. This seems to be what Mario would tell us to do anyway.

#### [Kevin Buzzard (Nov 13 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611540):
Right -- so @**Kenny Lau** are you happy if @**Ramon Fernandez Mir** proves existence of colimits in the category of commutative rings?

#### [Kevin Buzzard (Nov 13 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611550):
In a relatively "hands-on" way, not using Lawvere anything

#### [Johan Commelin (Nov 13 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611586):
Be aware that Scott already has some general machinery in this direction. I guess you only need coproducts and coequalisers.

#### [Kevin Buzzard (Nov 13 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611712):
I am not 100% sure whether this makes life any easier in this case

#### [Kevin Buzzard (Nov 13 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611817):
in the sense that now instead of making one gigantic commutative polynomial ring in a huge set of variables and quotienting out by an ideal generated by terms of two types and then proving something about it, you'll have to build two such rings and prove something about each of them.

#### [Johan Commelin (Nov 13 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147611967):
It would be useful to know that coproducts are defeq to tensor products, I assume...

#### [Kevin Buzzard (Nov 13 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147612367):
funny isn't it. For products and subobjects you feel like you've made progress. But colimits are quotients so it's always going to be a pain I think. I don't even really understand what the coproduct of an arbitrary set of rings looks like -- it seems to be some sort of direct limit of finite tensor products -- but of course we haven't built direct limits yet so there's a danger of going round in circles here.

#### [Kevin Buzzard (Nov 13 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147612491):
```quote
Here is a question for you: do you intend to make things mathlib-ready? Is the endgoal a PR to mathlib?
```
 I don't even know if Mario would be interested in hosting schemes (and I've not asked) -- my goal is to take the crappy code which I wrote so I could learn how to write Lean code, and replace it with code which is sufficiently respectable to get a publication. I've not thought about mathlib at all.

#### [Johan Commelin (Nov 13 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613037):
I think there are two options:
* either stuff like this goes into mathlib,
* or the Lean community comes up with a good strategy to have decentralised libraries that work together nicely as dependencies of other projects.

#### [Mario Carneiro (Nov 13 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613059):
The construction you sketched is clearly a composition of two constructions, why not formalize that?

#### [Johan Commelin (Nov 13 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613110):
@**Mario Carneiro** Do you want schemes in mathlib?

#### [Mario Carneiro (Nov 13 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613114):
I want polished code in mathlib

#### [Johan Commelin (Nov 13 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613127):
Do you want polished schemes in mathlib?

#### [Mario Carneiro (Nov 13 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613141):
sure, if that interests yous

#### [Mario Carneiro (Nov 13 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613160):
there seem to be a lot of intermediate steps though

#### [Johan Commelin (Nov 13 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613162):
It interests mes and about 65% of all Field medalists.

#### [Johan Commelin (Nov 13 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613239):
There's a lot of intermediate steps because I'm trying to write reusable code.

#### [Reid Barton (Nov 13 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147613596):
I'm not sure which construction Mario is referring to

#### [Mario Carneiro (Nov 13 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147615817):
```quote
via some big standard universal construction -- given a diagram in CommRing, let T0 be the polynomial ring over Z with variables the disjoint union of all the rings in the diagram, and then quotient out by the relations making all of the canonical maps ring homs
```

#### [Mario Carneiro (Nov 13 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147615855):
we already have the first part, and the second part should generalize to "given a bunch of functions(?) make them all ring homs"

#### [Scott Morrison (Nov 13 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147624123):
I think, unfortunately, that eventually we will want to do all the varieties of colimits in CommRing separately.

#### [Scott Morrison (Nov 13 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147624194):
We should do the general colimit, we should also do the filtered colimit (which is much easier), we should do coproducts, we should do binary coproducts. General nonsense says you don't need to prove any comparison theorems relating these, happily.

#### [Scott Morrison (Nov 13 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147624227):
Later, various bits of general machinery about algebraic categories will give us the filtered colimits "for free"

#### [Scott Morrison (Nov 13 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147624240):
but someone should do the construction in CommRing first as a warmup.

#### [Scott Morrison (Nov 13 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147624259):
I don't know the Lawvere stuff; maybe later there's some generality that gives us all colimits in CommRing too?

#### [Kevin Buzzard (Nov 13 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147625299):
Ok so Ramon and I will take on the task of general colimits. I'm a bit unsure about whether working in this generality will actually cause problems when we want to prove that the stalks for an affine scheme are local, but let's wait and see!

#### [Scott Morrison (Nov 13 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147629404):
Are you sure you don't want to do filtered colimits first, @**Kevin Buzzard**? They are both easier to construct, and more useful! (Because they're all that's needed for stalks, and will make arguments about stalks easier.)

#### [Kevin Buzzard (Nov 13 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630367):
The way Johan or you had set up locally ringed spaces relied on the fact that CommRing had colimits

#### [Kevin Buzzard (Nov 13 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630421):
I don't know what a filtered colimit is. I know what a directed set is. Is it sort-of the same thing?

#### [Kevin Buzzard (Nov 13 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630462):
aah I now know that a filtered colimit is a categorification of a directed set

#### [Kevin Buzzard (Nov 13 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630538):
So I guess I don't know where to stop here. Why not just do colimits over a directed partial order? They are both easier to construct, and more useful! (Because they're all that's needed for stalks, and will make arguments about stalks easier.)

#### [Kevin Buzzard (Nov 13 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630555):
And Kenny did them already :P

#### [Reid Barton (Nov 13 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630640):
Well, filtered is the right level of generality for the fact that you can compute the colimit in Set

#### [Kevin Buzzard (Nov 13 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630661):
but colimits in Set are completely different to colimits in CommRing

#### [Kevin Buzzard (Nov 13 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630669):
or am I misunderstanding? (presumably)

#### [Reid Barton (Nov 13 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630680):
General ones are, but filtered ones are not

#### [Kevin Buzzard (Nov 13 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630685):
Oh I see!

#### [Scott Morrison (Nov 13 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630803):
I will add filtered colimits (in the simplest sense, not Reid's kappa-filtered ones) to the limits branch shortly. (Just the definition!)

#### [Scott Morrison (Nov 13 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630858):
@**Johan Commelin**, Johannes asked me to rebase the limits branch; prepare for trouble. :-)

#### [Kevin Buzzard (Nov 13 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630866):
So @**Ramon Fernandez Mir** would be interested in this. People seem to be suggesting that the definition here https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/presheaves/locally_ringed.lean which uses arbitrary colimits is not wise?

#### [Scott Morrison (Nov 13 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630872):
Yes

#### [Scott Morrison (Nov 13 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630878):
That isn't wise. :-)

#### [Kevin Buzzard (Nov 13 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630892):
and instead of `stalk_at` one should use something else?

#### [Scott Morrison (Nov 13 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630907):
I think `stalk_at` will be exactly the same

#### [Scott Morrison (Nov 13 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630960):
We'll just change the typeclass provided, from `has_colimits` to `has_filtered_colimits`

#### [Kevin Buzzard (Nov 13 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630966):
I see. And that doesn't break anything else?

#### [Kevin Buzzard (Nov 13 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630973):
When teaching is finished I'm going to be cloning this repo finally

#### [Scott Morrison (Nov 13 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630980):
Magic will then notice that the category of open sets containing x is filtered, and so use the `has_filtered_colimits` instance,

#### [Kevin Buzzard (Nov 13 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147630984):
at the minute cloning it would lead me astray

#### [Scott Morrison (Nov 13 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631004):
which will provide an nice construction of the colimit (as a quotient of a disjoint union, just like in Set), rather than the huge one in terms of tensor products.

#### [Kevin Buzzard (Nov 13 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631007):
Would magic work for sheaves on a basis? For sheaves on a site?

#### [Scott Morrison (Nov 13 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631014):
That I don't know.

#### [Kevin Buzzard (Nov 13 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631032):
I had never seen the construction of a colimit in CommRing until today, when I figured it out for myself. I did not use tensor products. What trick did I miss?

#### [Kevin Buzzard (Nov 13 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631053):
I just made a polynomial ring over Z with variables the disjoint union of all the rings in the diagram

#### [Kevin Buzzard (Nov 13 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631056):
and then quotiented

#### [Kevin Buzzard (Nov 13 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631112):
I understand that for two rings a coproduct is the tensor product

#### [Kevin Buzzard (Nov 13 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631119):
but I couldn't see how this generalised to infinitely many rings

#### [Kevin Buzzard (Nov 13 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631132):
it seemed to be a direct limit of tensor produts, but to make direct limits you  want to take coproducts again

#### [Scott Morrison (Nov 13 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631157):
oh, okay, maybe I didn't think very hard about the infinite diagram case, either :-)

#### [Scott Morrison (Nov 13 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631173):
(I had never thought about any of this (nor knew what a site was, etc) until Lean came along. :-)

#### [Reid Barton (Nov 13 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631237):
Well... it's the filtered colimit of all the ways to take a coproduct of finitely many of the rings

#### [Reid Barton (Nov 13 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631238):
and filtered colimits are easy

#### [Kevin Buzzard (Nov 13 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631245):
Is there a general story?

#### [Reid Barton (Nov 13 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631246):
That said, the construction you gave is the simplest one and it has essentially nothing to do with rings in particular

#### [Kevin Buzzard (Nov 13 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631256):
Reducing a general colimit to a filtered colimit?

#### [Kevin Buzzard (Nov 13 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631348):
I still don't know whether we should just stick to filtered (0,1)-categories

#### [Kevin Buzzard (Nov 13 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631363):
i.e. directed sets (I should stop looking at nlab)

#### [Kevin Buzzard (Nov 13 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631372):
Oh, Reid's argument perhaps resolves this -- if it works over set then take it

#### [Reid Barton (Nov 13 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631433):
Directed colimits will be somewhat easier notationally and you don't need them unless you want stalks for some site which is not itself a poset. I think.

#### [Kevin Buzzard (Nov 13 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631440):
I think the etale site is the simplest example of this that I know

#### [Reid Barton (Nov 13 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631441):
Er, don't need filtered colimits unless ..., of course.

#### [Kevin Buzzard (Nov 13 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631458):
and next year when we're doing etale cohomology we'll need etale sites

#### [Reid Barton (Nov 13 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631469):
I think it is safe to assume that by the time we want to do etale cohomology we will have filtered colimits of rings

#### [Reid Barton (Nov 13 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147631531):
You can actually build filtered colimits from directed ones, so it doesn't lose any great generality to work with directed ones for some purposes

#### [Kevin Buzzard (Nov 14 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147633659):
```quote
Magic will then notice that the category of open sets containing x is filtered, and so use the `has_filtered_colimits` instance,
```
 There's something I can't get to add up here. Say there's a `has_colimits` instance and also a simpler `has_filtered_colimits` instance. Now let's say I'm trying to take a colimit and it happens to be filtered. If Lean uses the `has_colimits` instance then the colimit will be constructed in one way, but if Magic notices that the colimit is filtered then it could construct it using the simpler filtered colimit construction. The two constructions will give canonically isomorphic, but probably not defeq, objects, and doesn't this give rise to a diamond?

#### [Scott Morrison (Nov 14 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147638007):
I have to admit I don't know how bad a problem this is going to be!

#### [Reid Barton (Nov 14 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147638987):
You also don't necessarily *have* to put your filtered colimits into the type class system. You can just define and use them directly.

#### [Harry Gindi (Nov 14 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147640447):
the general statement comes from the theory of locally presentable categories

#### [Harry Gindi (Nov 14 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147640571):
every object can be given as a filtered colimit of finite pushouts of compact (i.e. finitely (resp Kappa)-presentable) objects, iirc the statement correctly

#### [Harry Gindi (Nov 14 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147640591):
and iirc CRing has only a single generator, Z[x]

#### [Harry Gindi (Nov 14 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147640677):
You don't need to work with Lawvere theories to do this stuff, you might be fine doing the locPres machinery and then proving algebraic categories you care about are LocPres

#### [Harry Gindi (Nov 14 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147640684):
standard reference is Adamek-Rosicky

#### [Harry Gindi (Nov 14 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147640760):
It seems a lot less complicated than doing Lawvere theories generally

#### [Harry Gindi (Nov 14 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147640896):
The general argument is useful in other places, iirc. Grothendieck first used this style of argument in the Tohoku paper

#### [Harry Gindi (Nov 14 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147640956):
proving that the category of abelian sheaves has enough injectives, but I forget the details

#### [Johan Commelin (Nov 14 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147649975):
@**Kevin Buzzard** Maybe we should change the definition of `stalk` a tiny little bit, and write `filtered_colimit` instead of `colimit`. That would take care of your issue, I think.

#### [Kevin Buzzard (Nov 14 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147650968):
This is a diamond-like issue but one level up. With diamonds you might end up with two objects which are equal but the proof isn't rfl. Here the objects are not even equal, merely canonically isomorphic

#### [Johan Commelin (Nov 14 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147652970):
I see what you mean. And I think this is showing that the current type class system might not be a good fit for categorical stuff (wait till we want to do higher-categorical stuff...). But maybe we can just ignore the issue for now, and hope  that Lean 4 will solve this issue before we hit serious problems.

#### [Johan Commelin (Nov 15 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147739873):
This is pretty ugly:
```lean
def extend : presheaf X C :=
{ obj := λ U, limit ((comma.fst (full_subcategory_inclusion B) (functor.of_obj U)).op ⋙ F),
  map := λ U V i,
    show (limits.limit (functor.op (comma.fst (full_subcategory_inclusion B) (functor.of_obj U)) ⋙ F) ⟶
        limits.limit (functor.op (comma.fst (full_subcategory_inclusion B) (functor.of_obj V)) ⋙ F)),
    begin
      have foo := limit.pre ((comma.fst (full_subcategory_inclusion B) (functor.of_obj U)).op ⋙ F) (extend.aux i),
      dsimp [extend.aux] at foo,
      convert foo,
      swap 3, assumption
    end }
```

#### [Reid Barton (Nov 15 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147740652):
Why isn't the `map` field just an application of `limit.pre`?

#### [Reid Barton (Nov 15 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147740706):
what goal is the last line solving?

#### [Reid Barton (Nov 15 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147741081):
My guess is that representing slice categories as comma categories is actually not a good idea in Lean, because the isomorphism (punit -> a) = a is not enough of an equality

#### [Reid Barton (Nov 15 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147741481):
Did you actually manage to prove the map_id and map_comp fields?

#### [Johan Commelin (Nov 15 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147741721):
Not yet, still working on it.

#### [Johan Commelin (Nov 15 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147741761):
Note that I'm not taking a slice category, although it almost is.

#### [Johan Commelin (Nov 15 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147741857):
This is opens in `B` that are contained in `U`, but `U` is not in `B`.

#### [Reid Barton (Nov 15 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742182):
Oh, I see

#### [Reid Barton (Nov 15 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742355):
If these are presheaves of sets, then there's an easier way to write the formula

#### [Reid Barton (Nov 15 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742375):
it's the same as the right Kan extension, right?

#### [Johan Commelin (Nov 15 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742424):
Hmmm... I think so.

#### [Johan Commelin (Nov 15 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742430):
If you want to help, please do so.

#### [Johan Commelin (Nov 15 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742437):
Lean is fighting back hard (-;

#### [Johan Commelin (Nov 15 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742454):
Maybe we should do it for a general map between sites, in that case.

#### [Reid Barton (Nov 15 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742530):
If E is the extended presheaf then we should have E(U) = Hom(yU, E) = Hom(R(yU), F) where R is the restriction of a presheaf on C to a presheaf on B

#### [Reid Barton (Nov 15 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742547):
so E is the composition y, then R, then Hom(-, F)

#### [Reid Barton (Nov 15 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742567):
Yes, that might help as well... at least for clarity

#### [Johan Commelin (Nov 15 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742652):
Ok, I think this is a nice way to do it!

#### [Johan Commelin (Nov 15 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742680):
I don't yet see why it is the same thing as in my special case

#### [Johan Commelin (Nov 15 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147742806):
Aah, `U` is the colimit of all the `Ui ∈ B` that are contained in `U`. Now pull this through `Hom(_, F)` and you get a limit.

#### [Reid Barton (Nov 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743096):
You might find it useful to borrow https://github.com/leanprover-community/mathlib/blob/adjunctions/category_theory/presheaf.lean#L85

#### [Reid Barton (Nov 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743119):
I think you will want to apply it twice

#### [Reid Barton (Nov 15 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743129):
In your setup you have a functor B -> C, right?

#### [Johan Commelin (Nov 15 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743202):
What do you mean?

#### [Johan Commelin (Nov 15 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743262):
`B` is a basis, and it has an inclusion into `opens X`.

#### [Johan Commelin (Nov 15 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743276):
I have a presheaf on `B`

#### [Reid Barton (Nov 15 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743300):
Okay so let's call `opens X` `C` for now

#### [Johan Commelin (Nov 15 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743339):
Aaah, `C` was my category of coefficients so far

#### [Reid Barton (Nov 15 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743342):
ah

#### [Johan Commelin (Nov 15 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743355):
But maybe I should stop worrying about coefficients, and only focus on `Type`.

#### [Reid Barton (Nov 15 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743373):
Well this formula won't work unless the values are in Type

#### [Johan Commelin (Nov 15 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743496):
Right, so I should forget about `C`

#### [Johan Commelin (Nov 15 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743523):
And sheaves of rings will require some extra thought

#### [Reid Barton (Nov 15 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743525):
Okay, in that case let me just use the names from the thing I linked above, so you have a functor C -> D

#### [Reid Barton (Nov 15 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743544):
If you apply `restricted_yoneda` to it, you get a functor D -> Set^C^op

#### [Reid Barton (Nov 15 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743555):
and if you apply `restricted_yoneda` to that, you get a functor Set^C^op -> Set^D^op

#### [Reid Barton (Nov 15 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743559):
and that should be the right Kan extension along the original functor

#### [Reid Barton (Nov 15 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743982):
the thing I called "Ry" earlier is another, possibly better way to write `restricted_yoneda`

#### [Johan Commelin (Nov 15 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147743992):
Sorry, as student entered my office. So I have to wait a while with this thing.

#### [Johan Commelin (Nov 15 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147746533):
@**Reid Barton** Hmmm... morphisms of sites seem to be non-trivial. I don't think I want to do them now, unless you want to join in. We would need to explain Lean this definition https://ncatlab.org/nlab/show/flat+functor#SiteValuedFunctors

#### [Reid Barton (Nov 15 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147747568):
Right... so concretely I guess your actual goal is to show that the extended presheaf is actually a sheaf?

#### [Reid Barton (Nov 15 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147747732):
You might want to pick a fact to prove, and work backwards from there

#### [Reid Barton (Nov 15 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147747750):
Otherwise you can enter a swamp of things you could formalize and choices of definitions you could make

#### [Johan Commelin (Nov 15 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147751358):
Right. I want to get an equivalence of categories between `sheaf B` and `sheaf X`. That is a concrete goal that I definitely want to reach.

#### [Johan Commelin (Nov 15 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147753284):
@**Reid Barton** So which approach would you suggest now? Maybe the one with Kan extensions is best? Because it will generalise later on?

#### [Johan Commelin (Nov 15 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147753315):
Hmmm, I'm being called for an early dinner. See you later.

#### [Johan Commelin (Nov 15 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147762987):
:rolling_on_the_floor_laughing: This error is hilarious:
```lean
type mismatch at application
  set.{u} (over.{u u} U)
term
  over.{u u} U
has type
  Type u
but is expected to have type
  Type u
```

#### [Johan Commelin (Nov 15 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147767061):
@**Reid Barton** How does this look?
```lean
def restrict : presheaf X ⥤ category_theory.presheaf B :=
{ obj := λ F, (full_subcategory_inclusion B).op ⋙ F,
  map := λ _ _ f, whisker_left _ f }

def extend : category_theory.presheaf B ⥤ presheaf X :=
{ obj := λ F, yoneda.op ⋙ restrict.op ⋙ yoneda.obj F,
  map := λ F G f, whisker_left _ $ whisker_left _ $ yoneda.map f }
```
I think you gave a very good suggestion!

#### [Johan Commelin (Nov 15 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147767734):
@**Reid Barton** I think it makes sense to merge your `presheaf.lean` with parts of my `sheaf.lean`. What would be the best approach? Should I merge your branch into mine?

#### [Johan Commelin (Nov 15 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147767788):
I would like to prove that `restrict` and `extend` form an adjunction anyway.

#### [Reid Barton (Nov 16 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/147783569):
@**Johan Commelin** Feel free to merge my branch into yours of course, though I will note that I intend to try out a redesign of adjunctions at some point

#### [Johan Commelin (Nov 20 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024110):
I'm not sure if I'm using things in the right way. I'm trying to write
```lean
let G1 := (equiv_of_iso D).trans (equiv.subtype_equiv_of_subtype.{(u+1) (u+1)} Eeq),
```
where `D : F.obj ≅ {p // horrible p}` is isomorphisms between a type and a subtype in the category `Type u` which I turn into an equiv.
I then want to replace the horrible right hand side with a subtype of something else, so I thought, lets use transitivity of `equiv` and feed it `Eeq`, which is:
```lean
Eeq : (limits.sigma.{u+1 u} (λ (Ui : {x // x ∈ c}), yoneda.{u u}.obj ((Ui.val).left)) ⟶ F) ≃
  Π (a : {x // x ∈ c}), F.obj ((a.val).left) :=
  equiv.trans.{u+1 u+1 u+1} (equiv_of_iso.{u} E)
    (equiv.Pi_congr_right.{u u+1 u+1}
       (λ (Ui : {x // x ∈ c}),
          equiv_of_iso.{u}
            (nat_iso.app.{u+1 u+1 u u} (yoneda_lemma.{u u} X) ((Ui.val).left, F) ≪≫
               ulift_trivial.{u} ((evaluation_uncurried.{u u u+1 u} Xᵒᵖ (Type u)).obj ((Ui.val).left, F))))),
```
The left hand side of `Eeq` should be exactly the type of the `p` in `{p // horrible p}`.

I get the following error:
```lean
type mismatch at application
  equiv.subtype_equiv_of_subtype.{u+1 u+1} Eeq
term
  Eeq
has type
  (limits.sigma.{u+1 u} (λ (Ui : {x // x ∈ c}), yoneda.{u u}.obj ((Ui.val).left)) ⟶ F) ≃
    Π (a : {x // x ∈ c}), F.obj ((a.val).left)
but is expected to have type
  (limits.sigma.{u+1 u} (λ (Ui : {x // x ∈ c}), yoneda.{u u}.obj ((Ui.val).left)) ⟶ F) ≃ ?m_1
```
I have tried looking at universes. I have enable `pp.all`. And I'm clueless. Any suggestions?

#### [Kevin Buzzard (Nov 20 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024274):
Is it a typeclass issue? That sometimes causes errors that look like that. Lean can't infer a typeclass and so gives up and prints an unhelpful error message

#### [Kevin Buzzard (Nov 20 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024298):
I mean equiv.subtype_equiv_of_subtype -- does it have some secret inputs that it can't find?

#### [Johan Commelin (Nov 20 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024334):
Also, why is `p` not an explicit argument in
```lean
def subtype_equiv_of_subtype {p : α → Prop} : Π (e : α ≃ β), {a : α // p a} ≃ {b : β // p (e.symm b)}
| ⟨f, g, l, r⟩ :=
  ⟨subtype.map f $ assume a ha, show p (g (f a)), by rwa [l],
   subtype.map g $ assume a ha, ha,
   assume p, by simp [map_comp, l.comp_eq_id]; rw [map_id]; refl,
   assume p, by simp [map_comp, r.comp_eq_id]; rw [map_id]; refl⟩
```

#### [Johan Commelin (Nov 20 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024344):
Well, in general it can't infer that `p`.

#### [Kevin Buzzard (Nov 20 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024349):
I'm explicitly talking about typeclasses

#### [Chris Hughes (Nov 20 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024351):
What universe is `?m_1` expected to be in?

#### [Johan Commelin (Nov 20 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024354):
`Type u`

#### [Mario Carneiro (Nov 20 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024361):
I think Johannes has a bad habit of making lots of things implicit that can't be inferred when used directly

#### [Mario Carneiro (Nov 20 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024384):
I guess that `p` is inferrable if you use it as a rewrite, or apply it to something

#### [Johan Commelin (Nov 20 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024389):
But in my case a smart elaborator should even be able to infer it, because I'm composing with another equiv.

#### [Johan Commelin (Nov 20 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024429):
Can I rewrite along `equiv`s?

#### [Mario Carneiro (Nov 20 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024432):
I think? `calc` for sure

#### [Chris Hughes (Nov 20 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024442):
Isn't `Π (a : {x // x ∈ c}), F.obj ((a.val).left)` Type (u + 1). If I'm not mistaken?

#### [Johan Commelin (Nov 20 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024445):
Hmmm, it says `rewrite tactic failed, lemma is not an equality nor a iff`

#### [Mario Carneiro (Nov 20 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024474):
hm, I guess that is probably a `// TODO(Leo)` somewhere

#### [Mario Carneiro (Nov 20 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024531):
obviously it's not high on the list of priorities

#### [Johan Commelin (Nov 20 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024534):
The `F.obj ((a.val).left)` is `Type u`, and the product is over `c : set (over U)` where `U : X` and `X : Type u`

#### [Johan Commelin (Nov 20 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024540):
I hope that doesn't bump up universes...

#### [Mario Carneiro (Nov 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024545):
that sounds fine

#### [Mario Carneiro (Nov 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024550):
you can just check, of course

#### [Chris Hughes (Nov 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024567):
If `F.obj ((a.val).left` is Type u, then `Π (a : {x // x ∈ c}), F.obj ((a.val).left)` is Type (u + 1) right?

#### [Chris Hughes (Nov 20 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024608):
No it isn't

#### [Mario Carneiro (Nov 20 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024687):
another trick you can try is `by convert` at the type mismatch

#### [Mario Carneiro (Nov 20 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024697):
it should home in on the mismatched part

#### [Johan Commelin (Nov 20 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024711):
How exactly should I do that?

#### [Mario Carneiro (Nov 20 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024771):
something like `subtype_equiv_of_subtype (by convert Eeq)` or `refine subtype_equiv_of_subtype _, convert Eeq`

#### [Johan Commelin (Nov 20 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024839):
Cool! That finds the following unsolved goal:
```lean
⊢ presheaf.category_theory.limits.has_coproducts.{u} = limits.functor_category_has_coproducts.{u+1 u}
```

#### [Johan Commelin (Nov 20 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024841):
That's progress at least.

#### [Kevin Buzzard (Nov 20 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148024861):
I am loving `convert`. I use it a lot when doing basic UG maths -- "this is basically the answer, now let's see what pieces we have to pick up"

#### [Johannes Hölzl (Nov 20 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148027986):
@**Johan Commelin**  `rw` only work with `=` (maybe also `==`, and `<->` only works due to `propext`). Rewriting with `equiv` is hard, one needs to prove that the motive (i.e. context in which the right-hand side appears) can be transported along the `equiv`. Even ignoring dependencies, parametricity is necessary as it shows that there is no `choice` involved.

#### [Johan Commelin (Nov 20 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148028093):
Right. That is about what I expected.

#### [Johannes Hölzl (Nov 20 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148028181):
To rewrite along a `equiv` we could use the `param`-branch https://github.com/leanprover-community/mathlib/commits/param and `transfer`.

#### [Johannes Hölzl (Nov 20 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148028325):
One example why it is a problem is:

We want to rewrite `e : α ≃ β` in `{a : α // p a}`, but what would be the goal? We get something like`{b : β // p (f⁻¹ b)}`. But in many cases `p` itself is also parametric, i.e. we have actually `{b : β // @p α (f⁻¹ b)}` (not really, as `p` is describing a term and not a constant, but I hope you get the idea) Now when we can try to adopt the structure of `p` s.t. `α` is completely replaced by `β`, and then `f` isn't occurring anymore

#### [Johannes Hölzl (Nov 20 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148028348):
This adoption mechanism is the kind of rewrite `transfer` is intended to do

#### [Johannes Hölzl (Nov 20 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148028353):
and `param` provides us with the necessary relations

#### [Johan Commelin (Nov 20 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148028487):
I see. But I suspect that `param` isn't yet ready for prime time.

#### [Patrick Massot (Nov 20 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148028596):
You need to ask @**Cyril Cohen** about this

#### [Cyril Cohen (Nov 20 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148028937):
@**Johannes Hölzl** @**Johan Commelin** @**Patrick Massot** `param` is not ready yet, the translation of recursors was not as straightforward as I thought.

#### [Johan Commelin (Nov 20 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148039894):
What do you do when Lean doesn't want to plug a morphism in the category `C` into your contravariant functor `F : Cᵒᵖ  ⥤ Type u`?
You use `convert`, and let `tidy` clean up the mess! :tada:
```lean
functor.map F (by convert Ui.val.hom; tidy)
```

#### [Johan Commelin (Nov 20 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148041125):
What's up, @**Kenny Lau**?

#### [Reid Barton (Nov 20 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046156):
```quote
Cool! That finds the following unsolved goal:
```lean
⊢ presheaf.category_theory.limits.has_coproducts.{u} = limits.functor_category_has_coproducts.{u+1 u}
```
```
 This is probably true by `refl`

#### [Johan Commelin (Nov 20 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046302):
```lean
invalid apply tactic, failed to unify
  presheaf.category_theory.limits.has_coproducts.{u} = limits.functor_category_has_coproducts.{u+1 u}
with
  ?m_3 = ?m_3
```

#### [Johan Commelin (Nov 20 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046325):
```lean
instance : has_coproducts.{(u+1) u} (presheaf X) := limits.has_coproducts_of_has_colimits
```

#### [Johan Commelin (Nov 20 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046374):
So, I changed that instance, and now I get
```lean
tactic failed, there are no goals to be solved
state:
no goals
```

#### [Johan Commelin (Nov 20 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046438):
Aaah, lol, that is because I should now remove the `refl`.

#### [Reid Barton (Nov 20 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046447):
Oh, I didn't notice "coproducts" rather than "colimits". Still I'm confused. What are the two instances which are not defeq, but equal by tidy?

#### [Johan Commelin (Nov 20 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046463):
No, they aren't equal by `tidy` either

#### [Reid Barton (Nov 20 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046499):
Or rather, what did you change that instance to?

#### [Reid Barton (Nov 20 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046576):
well, the right hand side of that goal I guess

#### [Johan Commelin (Nov 20 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046590):
Exactly

#### [Reid Barton (Nov 20 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046604):
But I see
```lean
instance functor_category_has_coproducts [has_coproducts.{u v} C] : has_coproducts.{(max u v) v} (K ⥤ C) :=
limits.has_coproducts_of_has_colimits
```

#### [Reid Barton (Nov 20 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046754):
... I'm really confused now

#### [Reid Barton (Nov 20 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148046922):
Ohh, maybe I get what is going on. I think all this duplication between colimit classes is biting you

#### [Reid Barton (Nov 20 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047035):
Well, I'm still not sure why that would be a problem either really

#### [Reid Barton (Nov 20 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047048):
But I still think the duplication is silly anyways

#### [Johan Commelin (Nov 20 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047066):
Which duplication do you mean exactly?

#### [Reid Barton (Nov 20 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047140):
Good question

#### [Reid Barton (Nov 20 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047155):
I was thinking of `has_colimits_of_shape` and `has_colimits` being unrelated

#### [Reid Barton (Nov 20 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047165):
But now I see there's also `has_colimits` which is also unrelated

#### [Reid Barton (Nov 20 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047176):
Gah, `has_coproducts`

#### [Reid Barton (Nov 20 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047441):
Anyways, I'm still confused by the original fact that you replaced an instance by, as far as I can tell, its definition and it changed the behavior of `refl`

#### [Johan Commelin (Nov 20 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047568):
Well, I didn't even need `refl` anymore. `convert` now took care of everything.

#### [Reid Barton (Nov 20 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047657):
because `congr`, which `convert` uses, will try closing goals with `refl` for you

#### [Johan Commelin (Nov 20 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047663):
Currently I'm trying to prove the equivalence of different formulations of the sheaf condition. Math-proof: apply Yoneda; QED. Lean-proof: :scream: :scream: :boom:

#### [Reid Barton (Nov 20 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047717):
`by convert x` should be the same as `by exact x`

#### [Johan Commelin (Nov 20 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148047745):
which apparently is not the same as `x`

#### [Reid Barton (Nov 20 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148055915):
OK, I got to the same place where you were before changing the instance.

#### [Reid Barton (Nov 20 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148055953):
It's kind of hard to understand what's going on because all the `has_blah` things are classes, which means they aren't printed except with `pp.implicit`, which also prints a bunch of other stuff I don't care about...

#### [Reid Barton (Nov 20 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148056108):
I wish you could jump from names in the goal window to their definitions...

#### [Johan Commelin (Nov 20 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148056614):
Right, we should but the "interactive" back in the goal window :grinning:

#### [Reid Barton (Nov 20 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148056956):
My conclusion is that I don't know what is wrong exactly, but all these different `has_*` need to be rethought (probably there should be far fewer of them)

#### [Reid Barton (Nov 20 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148057011):
Apparently your instances which were not the same reduce to something like the following

#### [Reid Barton (Nov 20 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148057077):
On one side, we have the colimit of a functor on a discrete category defined using the instance that says the category of types has colimits

#### [Reid Barton (Nov 20 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148057109):
On the other side, we're doing something like building a colimit cone from a coproduct thing, which in turn is built from the original colimit somehow

#### [Reid Barton (Nov 20 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148057118):
both of these constructions being nontrivial

#### [Reid Barton (Nov 20 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148057189):
so that they don't just cancel out

#### [Reid Barton (Nov 20 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148057227):
I haven't even seen this file `limits/products.lean` before

#### [Johan Commelin (Nov 20 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148065294):
Thanks for looking into this! Apparently it's trickier than I thought...

#### [Reid Barton (Nov 20 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148065317):
There are so many instances and it's hard to tell which ones are used where.

#### [Reid Barton (Nov 20 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148065430):
for example, `functor_category_has_coproducts` uses `limits.has_coproducts_of_has_colimits` which needs a `limits.has_colimits_of_shape.{u v} (discrete β)` instance. Does it come from `has_colimits_of_shape_of_has_coproducts_of_shape` or `functor_category_has_colimits_of_shape`?

#### [Reid Barton (Nov 20 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148065635):
either way, it will eventually end up at `has_coproducts_of_shape` for the original category which comes from `has_coproducts_of_shape_of_has_coproducts` which uses `has_coproducts` which comes from an unnamed instance with definition `has_coproducts_of_has_colimits` which finally comes from the one true `has_colimits` instance for Type. I think.

#### [Reid Barton (Nov 20 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148065696):
So that's how you end up with the `has_colimits` -> `has_coproducts` -> `has_colimits` double translation, which is not `refl`

#### [Johan Commelin (Nov 27 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640522):
It's really quite stupid, but I only realised yesterday that all the time I've been working with the wrong `map f : presheaf X \functor presheaf Y`.

#### [Johan Commelin (Nov 27 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640569):
We want something like this:
```lean
def map' : presheaf X ⥤ presheaf Y :=
{ obj := λ F,
  { obj := λ V, colimit ((comma.snd.{u u u u} (functor.of_obj V) f).op ⋙ F),
    map := λ V₁ V₂ j, colimit.pre ((comma.snd.{u u u u} (functor.of_obj V₂) f).op ⋙ F) (comma.map_left f $ functor.of_map j).op,
    map_id' := λ V,
    begin
      erw functor.of_map_id,
      erw colimit.pre_map,
      tidy,
    end },
  map := _ }
```
but I find it impossible to get this sorry-free.

#### [Reid Barton (Nov 27 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640594):
This is what I implemented in the `adjunctions` branch, I think?

#### [Johan Commelin (Nov 27 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640600):
This is what will give us the pullback of (pre)sheaves.

#### [Johan Commelin (Nov 27 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640608):
Aaah, did you?

#### [Johan Commelin (Nov 27 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640664):
I didn't look far enough, I'm afraid.

#### [Reid Barton (Nov 27 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640670):
I think it is `yoneda_extension (F.comp yoneda)`?

#### [Reid Barton (Nov 27 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640698):
at least, it seems to involve many of the same ingredients :)

#### [Johan Commelin (Nov 27 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640743):
In which file?

#### [Reid Barton (Nov 27 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640747):
another construction which I am not very happy about, though...

#### [Reid Barton (Nov 27 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640751):
`presheaf.lean`

#### [Johan Commelin (Nov 27 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640850):
Aaah, I see. Seems pretty non-trivial...

#### [Johan Commelin (Nov 27 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640875):
Also, why do you work with `≃` instead of `≅`. Isn't that just as "bad"?

#### [Reid Barton (Nov 27 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640886):
Yeah, I did it in a round-about way, in retrospect

#### [Reid Barton (Nov 27 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640953):
In general I use `equiv` because it actually has useful lemmas and also it can relate different universes

#### [Reid Barton (Nov 27 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640961):
though I added a couple more lemmas for `iso` in the limits PR

#### [Johan Commelin (Nov 27 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148640996):
Hmm, I feel like we should merge your `presheaf.lean` and my `sheaf.lean`. Or at least deduplicate.

#### [Reid Barton (Nov 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148641237):
I intend to take a second stab at all the adjunctions and presheaf stuff at some point, but I'm not actively working on it at the moment

#### [Johan Commelin (Nov 27 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148641294):
Ok, I'll move some stuff from my file to yours. So that `sheaf.lean` is only about sheaves.

#### [Johan Commelin (Nov 27 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148641306):
If you start working on it again, please make sure to take a look at the `sheaf` branch version of your file.

#### [Reid Barton (Nov 27 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148641624):
FWIW, my conclusion from my first attempt was that it's probably better to do all the constructions in a manifestly natural way, like Scott did in `yoneda.lean` for example, even though the result is probably pretty unreadable. Then you can add a simp lemma that explains what is actually happening on the level of objects

#### [Reid Barton (Nov 27 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148642150):
Or at least, don't have a bunch of isomorphisms with the naturality conditions stated separately. That was a big mess

#### [Johan Commelin (Nov 27 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148642474):
I see. That's what I've been trying to do. But I also got stuck.

#### [Johan Commelin (Nov 27 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148642576):
The problem with doing things in a "manifestly natural way" is that you get sucked into ever deeper/wider/higher abstractions...

#### [Reid Barton (Nov 27 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148642695):
it's true

#### [Reid Barton (Nov 27 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148643278):
And that's sort of why I backed off from my previous comment. It's not obvious how to do this "category of elements" construction functorially

#### [Reid Barton (Nov 27 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148643384):
The key is to somehow give these things usable and complete instances, so that the way to prove things about them is not to `dsimp` 100 things

#### [Reid Barton (Nov 27 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148643417):
and that's where my current version of `presheaf.lean` sort of fell apart

#### [Reid Barton (Nov 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148643508):
https://github.com/leanprover-community/mathlib/blob/adjunctions/category_theory/presheaf.lean#L310

#### [Johan Commelin (Nov 27 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148644814):
@**Reid Barton** Does this mean that you think we should avoid `adjunction.left_adjoint_of_equiv`?

#### [Johan Commelin (Nov 29 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148766980):
Yuchai! This is now sorry-free: https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/presheaf.lean#L59
But it is slower than slow! Not sure how to speed it up though. I'm chaining a bunch of rewrites. Are there strategies for speeding this up?

#### [Scott Morrison (Nov 29 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148767231):
One thing that I find often works is to work out why the `erw` are necessary. This is sometimes unrewarding, but often it is because hidden inside implicit arguments there are things that should `dsimp`, but you forgot to write the appropriate `rfl` lemmas.  Sometimes you get really lucky, and after diagnosing a problem like this you can not only change the `erw` to `rw`, but even to `dsimp`!

#### [Johan Commelin (Nov 29 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148767295):
I see. (I've stopped using `rw`, because `erw` has more powerful magic (-;)

#### [Johan Commelin (Nov 29 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148767296):
Is `dsimp` faster than `erw`?

#### [Scott Morrison (Nov 29 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148767299):
Yes.

#### [Scott Morrison (Nov 29 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148767305):
And `erw` can be slower than `rw`, in places where either work. (I think?)

#### [Scott Morrison (Nov 29 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148767352):
Well, `dsimp` can be either faster or slower than `erw`. :-) But _usually_ it seems to be faster to avoid using `erw`.

#### [Johan Commelin (Nov 29 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148767491):
@**Scott Morrison|110087** Do you think we could have a `[derive rfl-lemmas]`?

#### [Scott Morrison (Nov 29 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148767960):
I've just had a quick look at that proof, Johan, and I don't seem to be able to make much improvement. :-( There does seem to be a small problem changing between `colimit` and `colim.obj`.

#### [Johan Commelin (Nov 29 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148770849):
So here is what I imagine `derive rflsimp` (or whatever) should do: it looks at the current definition, and (as far as I thought this through, which is not that far) it does two checks:
* the definition is an "abbreviation" (like `def presheaf C := C \functor Type v`. In this case it looks up all the rflsimp lemmas that it derived for `C \functor D` and defines copies in the `presheaf` namespace.
* the definition `X` is a structure. In this case it looks up all the fields. For a field `foo` it checks whether this is a Pi-type (?) and how many arguments the Pi takes. So if `foo := λ a b c, bar(a,b,c)` then it will create the appropriate simp-lemma (proved by `rfl`) that
```lean
@[simp] lemma X.foo (x : X) (a b c : some_type) :  x.foo a b c = bar(a,b,c) := rfl
```
Of course I don't know how to write `meta`-code. And of course this is probably a very simplified picture. But I think something like this should be possible, and I think it would result in three things:
* less boilerplate (especially in the category library!)
* less broken proofs, where `tidy` doesn't work, because somewhere someone forgot to state the obvious `rfl`-simp-lemma.
* less wasted time in hunting down the brokenness of the preceding point.

#### [Johan Commelin (Nov 29 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148771232):
@**Scott Morrison|110087** Thanks for looking into speeding things up. I added a rflsimp-lemma for `colim.obj`. Do you have any clue why the first line in that proof (with the comment) didn't simplify?

#### [Scott Morrison (Nov 29 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148777570):
Nope, I couldn't work it out. The next "usual suspect" for simp not working is that the thing that needs to be `simp`ed is inside a function that looks superficially dependent but actually isn't when you think about it a bit. `simp`, which needs to build congruence lemmas to do "rewriting", can't work out what do to, but `rw` can. This is a "known problem" with `simp`, apparently.

#### [Scott Morrison (Nov 29 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148777585):
You know how to use `rewrite_search`, don't you? :-)

#### [Keeley Hoek (Nov 29 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148778422):
At some point Johan I made a thing which did this
It was a command called `rfl_lemma` I think. If you have access to rewrite_search you have access to it, too

#### [Keeley Hoek (Nov 29 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148778431):
It only worked for structures though

#### [Johan Commelin (Nov 29 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148779294):
@**Scott Morrison|110087** @**Keeley Hoek** I don't have `rewrite_search`. Do you think it is ready to be tested by others? If so, what do I need to do to get started?

#### [Keeley Hoek (Nov 29 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148782650):
You could always try it out! My understanding is that all you should have to do is add
````
lean-tidy = {git = "https://github.com/semorrison/lean-tidy", rev = "3a69d6241207f0c0758468dce666858027c54909"}
````
to your `leanpkg.toml` and run `leanpkg configure`. (I'm slightly worried though because `lean-tidy` obviously imports from `mathlib`, which you are working on... but I suspect it will work find (I think this is what Scott does to get his proofs using it).

#### [Keeley Hoek (Nov 29 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148782717):
Then import `tactic.rewrite_search`. You can try to discharge goals with the `rewrite_search` tactic, but make sure you tag lemmas it is allowed to use with `@[search]`. There is much more complicated stuff you can do (including more specific tagging), but that's a start!

#### [Johan Commelin (Nov 29 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148783201):
Thanks for the explanation!

#### [Scott Morrison (Nov 29 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148783722):
I've actually never used it inside mathlib, I'm very curious if it works.

#### [Keeley Hoek (Nov 29 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148783729):
ooh
Maybe it won't then

#### [Keeley Hoek (Nov 29 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148783739):
something about "ambiguous import xxxx"

#### [Johan Commelin (Nov 29 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148784745):
How far are we from a merge request of a (preliminary) version of `rewrite_search`?

#### [Johan Commelin (Nov 29 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148785350):
@**Keeley Hoek** @**Scott Morrison|110087** I followed the instructions and then ran `leanpkg build`. I'm getting tons of errors :stuck_out_tongue_wink:

#### [Keeley Hoek (Nov 29 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148785538):
:D

#### [Keeley Hoek (Nov 29 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148785563):
yeah, sorry
I think what you actually have to do is copy paste the lean-tidy repo over mathlib
but probably don't do that it will mess your history

#### [Johan Commelin (Nov 30 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/148857277):
@**Scott Morrison|110087** @**Keeley Hoek** I can report that adding that Lean *does not* outright refuse that repo as a dependency of mathlib. However... there's tons and tons of errors. So it's not really usable in a sense.

#### [Johan Commelin (Dec 28 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638060):
After a long period of being distracted by other work, I've returned to the sheaves and sites project. Stuff is now happening on the `sheaf-2` branch, which has less dependencies than `sheaf`.
I am currently struggling with defining a pretty non-constructive map. I have a gadget `s` which comes with a proof that I can perform a certain construction after some choice, and the result of the construction does not depend on the choice. But how do I actually do this?
```lean
def foo (c : covering_family U) (F : presheaf X) :
(matching_sections c F) ⟶ (matching_sections c.generate_sieve.val F) :=
λ s : matching_sections c F, show matching_sections c.generate_sieve.val F, from
{ val := λ V H,
  begin
    delta matching_sections at s,
    choose Ui H f using H,
    refine F.map _ (s.1 _ H),
  end,
  property := _ }
```
Here is what my goal window looks like
```lean
X : Type u,
_inst_1 : small_category X,
U : X,
c : covering_family U,
F : presheaf X,
V : over U,
s :
  {s // ∀ (Ui : over U) (H : Ui ∈ c) (Uj : over U) (H_1 : Uj ∈ c) (V : over U) (f : V ⟶ Ui) (g : V ⟶ Uj),
     F.map (f.left) (s Ui H) = F.map (g.left) (s Uj H_1)},
Ui : over U,
H : Ui ∈ c,
f : nonempty (V ⟶ Ui)
⊢ Ui.left ⟶ V.left
```
What I need to do is extract some hom `f` from `V` to `Ui` out of the current `f : nonempty (_)`. I should then be able to close the goal with `exact f.left`. But I can only eliminate into `Prop` from `nonempty`. So how should I set things up?
All of this is at https://github.com/leanprover-community/mathlib/blob/sheaf-2/category_theory/sheaf.lean#L190-L199

#### [Reid Barton (Dec 28 2018 at 07:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638676):
Are you going to need to prove the resulting construction is independent of the choice?

#### [Reid Barton (Dec 28 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638688):
The simple answer is to use choice again, in the form of `classical.choice`

#### [Reid Barton (Dec 28 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638738):
maybe the `choose` tactic could do this when the final Prop is a `nonempty`

#### [Reid Barton (Dec 28 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638740):
or you could use that `\exists blah, blah, blah, true` encoding

#### [Johan Commelin (Dec 28 2018 at 07:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638796):
So `nonempty blah` is not Lean-equivalent to the `\exists blah, blah, blah, true` encoding?

#### [Johan Commelin (Dec 28 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638804):
The `choose` tactic doesn't help... :sad:

#### [Reid Barton (Dec 28 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638807):
it's not definitionally equivalent, much as `p /\ true` isn't definitionally equivalent to `p`

#### [Johan Commelin (Dec 28 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638882):
`nonempty_of_exists` is not an iff...

#### [Reid Barton (Dec 28 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638940):
You can just use `choice f`

#### [Johan Commelin (Dec 28 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638952):
Ok, I'll try that. Too bad that `choose f` does not work.

#### [Reid Barton (Dec 28 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152638953):
Sometimes when there is going to be a lot of "can only eliminate into Prop" nonsense in a proof, I just put an `apply choice` at the start

#### [Reid Barton (Dec 28 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152639001):
or not necessarily at the start of the whole argument, but at the start of some subargument to satisfy some lemma which wants to take an actual map rather than just an existence statement

#### [Johan Commelin (Dec 28 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152642729):
Ok, that worked. But I still wonder why `choose f` didn't work. @**Patrick Massot** Any ideas why `choose` doesn't work on `nonempty`?
Here's the proof that I have now
```lean
noncomputable def foo (c : covering_family U) (F : presheaf X) :
(matching_sections c F) ⟶ (matching_sections c.generate_sieve.val F) :=
λ s : matching_sections c F, show matching_sections c.generate_sieve.val F, from
{ val := λ V H,
  begin
    delta matching_sections at s,
    choose Ui H f using H,
    refine F.map _ (s.1 _ H),
    exact (classical.choice f).left,
  end,
  property := _ }
```

#### [Kenny Lau (Dec 28 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152642813):
because `choose` is skolemization?

#### [Johan Commelin (Dec 28 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152643079):
I don't know what that means.

#### [Johan Commelin (Dec 28 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152643597):
I love the marvellous power of the underscore:
```lean
noncomputable def foo (c : covering_family U) (F : presheaf X) :
(matching_sections c F) ⟶ (matching_sections c.generate_sieve.val F) :=
λ s : matching_sections c F, show matching_sections c.generate_sieve.val F, from
{ val := λ V H,
  begin
    choose Ui H f using H,
    refine F.map _ (s.1 _ H),
    exact (classical.choice f).left,
  end,
  property :=
  begin
    intros,
    show (F.map _ ≫ F.map _) _ = (F.map _ ≫ F.map _) _,
    repeat {rw ← F.map_comp},
    exact s.property _ _ _ _ _ (_ ≫ _) (_ ≫ _)
  end }
```

#### [Johan Commelin (Dec 28 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/152667001):
I'm hitting a nasty error again (probably I'm being bitten by `choice`).
Here is the error (code follows below):
```lean
type mismatch at application
  ⟨s_val, s_property⟩.val Ui H
term
  H
has type
  Ui_1 ∈ c_1
but is expected to have type
  Ui ∈ c
types contain aliased name(s): Ui U c
remark: the tactic `dedup` can be used to rename aliases
```
Code:
```lean
def quux (c : covering_family U) :
c.matching_sections ≅ c.generate_sieve.val.matching_sections :=
{ hom := foo c,
  inv := bar c,
  hom_inv_id' :=
  begin
    ext1 F,
    ext1 s,
    apply subtype.ext.mpr,
    funext,
    convert s.property _ _ _ _ _ _ (𝟙 _),
    tidy {trace_result := tt}
  end,
  inv_hom_id' :=
  begin
    ext1 F,
    ext1 s,
    apply subtype.ext.mpr,
    funext,
    dsimp [foo, bar],
    convert s.property _ _ _ _ _ _ (𝟙 _), -- This line fails
    tidy {trace_result := tt},
  end }
```
Context, just before the `convert`:
```lean
X : Type u,
_inst_1 : small_category X,
U : X,
c : covering_family U,
F : presheaf X,
s : (matching_sections ((generate_sieve c).val)).obj F,
V : over U,
H : V ∈ (generate_sieve c).val
⊢ F.map ((classical.choice _).left) (s.val (classical.some H) _) = s.val V H
```

#### [Johan Commelin (Jan 20 2019 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/156493474):
@**Kevin Buzzard** Replying to https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What's.20new.20in.20Lean.20maths.3F/near/156491890 in this thread.
To be precise: I have no trouble at all extending a presheaf from a basis to the whole space. The problem is checking that it sends sheaves to sheaves. The difficulty is probably due to the fact that I do not have a usable API around the sheaf condition.
And I guess my sheaf condition is hard to work with right now because I'm trying to be quite general, doing sheaves on an arbitrary site.

#### [Kevin Buzzard (Jan 20 2019 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheaves%20and%20sites/near/156495585):
Oh -- the proof involves some argument on stalks which for a general site is complicated? Are there universe issues or do you only work with small sites?

