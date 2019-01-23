---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/24026Categorytheory.html
---

## Stream: [maths](index.html)
### Topic: [Category theory](24026Categorytheory.html)

---

#### [Kenny Lau (Apr 01 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124502143):
https://github.com/kckennylau/category-theory/blob/master/src/adjunction_examples.lean

#### [Kenny Lau (Apr 02 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124520998):
```
@[reducible] def Set.Prod_Hom (B : Type u) : adjunction examples.Set examples.Set :=
adjunction.make _ _
  (examples.Set.product_functor B)
  (examples.Set.Hom_functor_right B)
  (λ A C f x, f x.1 x.2)
  (λ A C f x y, f (x, y))
  (λ A₁ A₂ C₁ C₂ f g t, rfl)
  (λ A₁ A₂ C₁ C₂ f g t, rfl)
  (λ A C f, funext $ λ ⟨t₁, t₂⟩, rfl)
  (λ A C f, rfl)

#### [Kenny Lau (Apr 02 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124520999):
so natural

#### [Kenny Lau (Apr 02 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124521485):
```
@[reducible] def Top_Set : adjunction examples.Top examples.Set :=
adjunction.free_forgetful _
  examples.Top.discrete
  examples.Top.forgetful
  (λ S T f, ⟨f, continuous_top⟩)
  (λ S T f, f.1)
  (λ T₁ T₂ S₁ S₂ f g t z, rfl)
  (λ T₁ T₂ S₁ S₂ f g t, subtype.eq rfl)
  (λ S T f, subtype.eq rfl)
  (λ S T f, rfl)

@[reducible] def Set_Top : adjunction examples.Set examples.Top :=
adjunction.make _ _
  examples.Top.forgetful
  examples.Top.indiscrete
  (λ S T f, f.1)
  (λ S T f, ⟨f, continuous_bot⟩)
  (λ T₁ T₂ S₁ S₂ f g t, subtype.eq rfl)
  (λ T₁ T₂ S₁ S₂ f g t, rfl)
  (λ S T f, rfl)
  (λ S T f, subtype.eq rfl)

#### [Kenny Lau (Apr 02 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124521487):
that moment when they're adjoint to each other

#### [Kenny Lau (Apr 07 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124769998):
for a set S, denoting by L(S) the transitive closure of S, we see that for any transitive set T with S ⊆ T, then L(S) ⊆ T

#### [Kenny Lau (Apr 07 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124769999):
I wonder if this is the left adjoint of some forgetful functor

#### [Kenny Lau (Apr 07 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124770041):
well, working in the category of sets with inclusion as morphism, we see that Hom_Trans(L(S),T) = Hom_Set(S,R(T)), where Trans is the category of transitive sets

#### [Kevin Buzzard (Apr 07 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124771927):
What does this even mean? What is a transitive set?

#### [Kenny Lau (Apr 07 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124771967):
A set X is transitive if for every x and y such that x∈y∈X, we have x∈X

#### [Kenny Lau (Apr 07 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124771978):
if the transitive closure is indeed a left adjoint, then we get right-exactness for free

#### [Kevin Buzzard (Apr 07 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772086):
Eew. I think I saw that notion in undergraduate set theory nearly 30 years ago, and I'm not sure I've seen it since. Maybe I saw it in the context of ordinals, which is something else I've not seen since.

#### [Kevin Buzzard (Apr 07 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772191):
Are you making an assertion here? What is R(T)?

#### [Kenny Lau (Apr 07 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772193):
the forgetful functor that forgets the fact that T is transitive

#### [Kevin Buzzard (Apr 07 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772194):
Is what you write true?

#### [Kenny Lau (Apr 07 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772195):
I believe so

#### [Kevin Buzzard (Apr 07 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772234):
If S and T are both transitive, then you're asserting that the transitive maps from S to T are the same as the maps from S to T then?

#### [Kenny Lau (Apr 07 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772235):
yes, since here the morphisms are just inclusions, so there is only one morphism per pair of sets

#### [Kevin Buzzard (Apr 07 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772241):
What does Hom_Set mean then?

#### [Kenny Lau (Apr 07 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772243):
oh, inclusion

#### [Kevin Buzzard (Apr 07 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772287):
Do you have a question?

#### [Kenny Lau (Apr 07 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772288):
is my belief right

#### [Kevin Buzzard (Apr 07 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772327):
What does Hom_Trans mean?

#### [Kenny Lau (Apr 07 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772328):
subcategory

#### [Kevin Buzzard (Apr 07 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772329):
I don't know what anything means. It feels like you have made these categories up.

#### [Kevin Buzzard (Apr 07 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772331):
It also seems that you are just as capable of writing down a proof of your assertion as I am. Why not check it in Lean? ;-)

#### [Kenny Lau (Apr 07 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772336):
because to hell with the category of sets in Lean

#### [Kevin Buzzard (Apr 07 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772338):
What does Hom_Trans mean?

#### [Kenny Lau (Apr 07 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772339):
the inclusion in the category of transitive sets

#### [Kevin Buzzard (Apr 07 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772340):
So at most one map between two sets?

#### [Kenny Lau (Apr 07 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772378):
yes

#### [Kevin Buzzard (Apr 07 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772387):
" we see that for any transitive set T with S ⊆ T, then L(S) ⊆ T ". Is that your question?

#### [Kenny Lau (Apr 07 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772388):
well that's the UMP of transitive closure

#### [Kenny Lau (Apr 07 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772389):
which should be right

#### [Kevin Buzzard (Apr 07 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772398):
But what is your question if it is not precisely that statement?

#### [Kenny Lau (Apr 07 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772399):
no idea

#### [Kevin Buzzard (Apr 07 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772400):
We might be done then :-)

#### [Kenny Lau (Apr 07 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/124772437):
interesting

#### [Reid Barton (Sep 01 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133190899):
Scott I guess I'll keep you updated on what I'm doing by sending pastebin links for now.

#### [Reid Barton (Sep 01 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133190905):
https://pastebin.com/WmdNgPdx is limits and colimits in types (nice and easy) and small and filtered categories (also easy).

#### [Reid Barton (Sep 01 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133190955):
Next I plan to try to show that small limits commute with filtered colimits

#### [Reid Barton (Sep 01 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133190963):
Probably I won't finish that in the next few days.

#### [Scott Morrison (Sep 02 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133193621):
Thanks, Reid, that patch has been applied!

#### [Reid Barton (Sep 02 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133219652):
I defined the limit functor but the proofs aren't as concise as they should be, especially map_id'.
https://pastebin.com/QDM9H7TX

#### [Reid Barton (Sep 02 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133219672):
Scott -- maybe the simp lemmas could be set up so that map_id' can be proved by obviously?
map_comp' is more complicated, since you have to use associativity (backwards)

#### [Scott Morrison (Sep 03 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133230162):
@**Reid Barton**, in fact I already had this, obscurely hidden in `universal/complete/default.lean`, with slightly different proofs. I've incorporated some changes from yours, but left my proofs for now. Curiously, `obviously` does just fine for `map_comp'`, but fails on `map_id'` because for some reason `simp` won't apply `limit.lift_π`.

#### [Scott Morrison (Sep 03 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/133230214):
I guess it was hiding in that directory because I wrote it for the sake of https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/universal/complete/functor_category.lean, a still incomplete proof that C \lea D has limits if D does.

#### [Kenny Lau (Oct 20 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136174097):
@**Scott Morrison|110087** Will you change some of the mathlib files to use category theory?

#### [Kenny Lau (Oct 20 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136174143):
what's the plan for category theory?

#### [Scott Morrison (Oct 20 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136174176):
I think at first, not much. Things like `has_products CommRing` can first live under `category_theory/`, as we get used to them.

#### [Kenny Lau (Oct 20 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136174189):
will they gradually assimilate into the main mathlib library?

#### [Scott Morrison (Oct 20 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136174190):
Eventually such facts should move out to their natural homes, immediately following where the underlying lemmas are actually proved.

#### [Kenny Lau (Oct 20 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136174193):
nice

#### [Scott Morrison (Oct 20 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136174205):
I suspect in the long run a lot of files will want to import `category_theory.isomorphism`, to avoid having to define their own custom version of `equiv` for the structure at hand.

#### [Kenny Lau (Nov 02 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136987135):
@**Scott Morrison|110087** The new module will be:
```lean
class module (α : out_param $ Type u) (β : Type v) [out_param $ ring α]
  [add_comm_group β] extends semimodule α β
```
How will your category theory library deal with this?

#### [Scott Morrison (Nov 02 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136992913):
Mostly users will just want the category of R-modules for some fixed R. After you've fixed the ring this is no more or less scary than bundling any other algebraic typeclass, I think.

#### [Kenny Lau (Nov 02 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136994837):
@**Scott Morrison|110087** I don't see how `bundle` can solve this

#### [Scott Morrison (Nov 02 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136994962):
Oh, I didn't imply that we should use `bundled`. It's only intended for the simplest cases.

#### [Scott Morrison (Nov 02 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136995172):
But `structure Module (a : Type) [ring a] := (b : Type) (m : module a b)`, is presumably fine.

#### [Scott Morrison (Nov 02 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136995228):
Maybe you haven't actually said what you're concerned about?

#### [Kenny Lau (Nov 02 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136995271):
well you forgot the add_comm_group

#### [Kenny Lau (Nov 02 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136995293):
and actually that's all I'm concerned about

#### [Scott Morrison (Nov 02 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136995418):
So `structure Module (a : Type) [ring a] := (b : Type) (g : add_comm_group b) (m : module a b)`...?

#### [Kenny Lau (Nov 02 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136995910):
I'm not really sure how all of this works, because last time in my own category repo, I was wrestling with sigma

#### [Scott Morrison (Nov 02 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136996578):
Yeah, I think just building custom structures, and then a few lemmas that peel back out the typeclasses as needed, is easiest.

#### [Scott Morrison (Nov 02 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/136996598):
I'll make a few more examples.

#### [Kenny Lau (Nov 02 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137000581):
thanks

#### [Kenny Lau (Nov 02 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137066926):
@**Scott Morrison|110087** is `bundled category` a category? If not, what's the proper name?

#### [Johan Commelin (Nov 02 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137078410):
I have a natural transformation `a` from `F` to `G`, and Lean is looking for a natural transformation from `G.op` to `F.op`. So I would like to provide `a.op` but this is not defined yet. What is the natural place to add this definition? In `opposites.lean` or in `natural_transformation.lean`?

#### [Reid Barton (Nov 02 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137078733):
I think it makes sense to keep `category`/`functor`/`natural_transformation` "at the bottom" and so put `a.op` in `opposites` like `F.op`

#### [Johan Commelin (Nov 02 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137079047):
Ok... fine with me. I could also imagine `opposites` being pretty "fundamental".

#### [Kenny Lau (Nov 02 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137079230):
It would be quite interesting if we know that functors form a category but not that categories form a category...

#### [Kenny Lau (Nov 02 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137079231):
I've searched all the files

#### [Mario Carneiro (Nov 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137079297):
the problem is that categories form a 2-category

#### [Mario Carneiro (Nov 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137079305):
so "categories form a category" is true but mostly useless

#### [Reid Barton (Nov 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137079310):
Categories also form a perfectly good category, we just don't have it yet

#### [Johan Commelin (Nov 02 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137079773):
Ok, I'm testing out a heresy:
```lean
def cocone (F : J ⥤ C) := cone F.op
```
The first problem I hit is that for `c : cocone F` the tip of the cocone `c.X` is now an object of `C\op` instead of `C`. Can this somehow be fixed? I would rather just write `f : c.X \hom X` instead of
```lean
f : @category.hom C _ c.X X
```

#### [Reid Barton (Nov 02 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137080246):
I actually have this problem in ordinary informal math as well: it's hard to talk about both C and C^op at the same time.
Sometimes I write things like $$\overline{A}$$ for the object of C^op corresponding to the object $$A$$ of C, but I'm not really fond of it.

#### [Kenny Lau (Nov 02 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137080336):
"ordinary informal math" = category

#### [Johan Commelin (Nov 02 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137080436):
Sure, so we could write `X.op` for such objects. But this problem is different. With my definition `c.X` lives in `C^op` by definition. But I'dd rather have it live in `C`... And somehow just writing `f : (c.X : C) \hom X` doesn't cut it....

#### [Johan Commelin (Nov 02 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137080457):
Hmmm... I have to run. See y'all later.

#### [Reid Barton (Nov 02 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137081858):
Perhaps we could have `unop : C\op \to C`?

#### [Kenny Lau (Nov 02 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137082098):
or maybe an equivalence of categories `C\op\op \cong C`?

#### [Kenny Lau (Nov 02 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137083573):
```lean
import algebra.module
import category_theory.examples.rings category_theory.opposites

universes u v w

variables (R : Type u) [ring R]

class Module (M : Type v) extends add_comm_group M, module R M

def Module.is_linear_map {M N : Type v} [Module R M] [Module R N] (f : M → N) : Prop :=
is_linear_map f

open category_theory category_theory.examples

instance Module.concrete_category : concrete_category (@Module.is_linear_map R _) :=
⟨λ _ _, by constructor; intros; refl,
λ _ _ _ _ _ _ _ _ hf hg, by cases hf; cases hg; constructor; intros; simp only [(∘), *]⟩

@[reducible] def Mod := bundled (Module R)

@[reducible] def Cat := bundled category

instance : category Cat :=
{ hom := λ C D, @category_theory.functor C.1 C.2 D.1 D.2,
  id := λ C, @functor.id C.1 C.2,
  comp := λ C D E, @category_theory.functor.comp C.1 C.2 D.1 D.2 E.1 E.2,
  id_comp' := λ C D f, by cases f; refl,
  comp_id' := λ C D f, by cases f; refl }

def Mod : Ringᵒᵖ ⥤ Cat :=
{ obj := λ R, bundled.mk _ (Mod R.1),
  map' := λ R S φ, concrete_functor (begin end) (begin end) }
```

#### [Reid Barton (Nov 02 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084172):
This looks good, but then the real test is whether it's convenient to use objects of `Mod R` as modules and vice versa, and the same for `Cat`

#### [Reid Barton (Nov 02 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084272):
At a minimum you want the instance that gets you the `Module` back out from `x : Mod R`

#### [Reid Barton (Nov 02 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084280):
analogous to `instance (x : Ring) : ring x := x.str`

#### [Kenny Lau (Nov 02 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084285):
that's just interface

#### [Kenny Lau (Nov 02 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084287):
anyone can write an interface

#### [Reid Barton (Nov 02 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084348):
anyone can define `Cat`, too

#### [Reid Barton (Nov 02 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084357):
Finding a good interface is the important thing

#### [Chris Hughes (Nov 02 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084372):
Interfaces are hard.

#### [Kenny Lau (Nov 02 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137084448):
I think `opposite` can have a better interface

#### [Kenny Lau (Nov 02 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087104):
@**Scott Morrison|110087** how should we define an additive category?

#### [Scott Morrison (Nov 02 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087138):
ugh, yeah, defining enriched categories may take a lot of work to do in general. :-(

#### [Scott Morrison (Nov 02 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087180):
If you _just_ want additive categories (which is very reasonable, later we can retrofit them as special cases of enriched categories)

#### [Scott Morrison (Nov 02 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087225):
then I don't think it's too bad

#### [Kenny Lau (Nov 02 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087236):
ok, then how?

#### [Scott Morrison (Nov 02 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087237):
Just have a new typeclass `[additive_category C]`, with fields `hom_abelian : add_comm_group (X \hom Y)` and `comp_bilinear : ...`

#### [Scott Morrison (Nov 02 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087239):
and then some `defs` that create instances from these fields

#### [Kenny Lau (Nov 02 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087261):
can we instead declare it as a functor from the Hom category to the Ab category

#### [Kenny Lau (Nov 02 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087302):
such that some triangle commutes

#### [Kenny Lau (Nov 02 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087316):
I guess Hom isn't a category

#### [Scott Morrison (Nov 02 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087321):
yeah, I'm not sure what you mean

#### [Kenny Lau (Nov 02 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087339):
there must be a way to do this category-theoretically...

#### [Scott Morrison (Nov 02 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087358):
Well... I think often it's better to have the definitions "explicit" and then have lemmas saying "you can interpret this in categorical terms"

#### [Kenny Lau (Nov 02 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087367):
sure

#### [Scott Morrison (Nov 02 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087368):
In particular, for monoidal categories (or 2-categories), which I really want to get back to,

#### [Scott Morrison (Nov 02 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087421):
it turns out to be a really bad idea to say that a monoidal category is a category equipped with a functor (C x C) \func C, such that ...

#### [Kenny Lau (Nov 02 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087436):
why isn't Lean ready for a category theory library?

#### [Scott Morrison (Nov 02 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087445):
and instead you should do everything grossly: a function `tensorObjects`, a function `tensorMorphisms`, and then have a lemma saying these form that functor

#### [Scott Morrison (Nov 02 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087481):
This sounds like a really bad idea, but the way lean's notation system and elaborator work, you run into endless misery making the functor the "primary" description of the tensor product.

#### [Scott Morrison (Nov 02 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087484):
It's very unfortunate. :-(

#### [Scott Morrison (Nov 02 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137087555):
> why isn't Lean ready for a category theory library?

Speaking to mathematicians, Lean, like every other ITP system, is not ready to do mathematics in. :-)

Lean is terrible, just less terrible than all the others!

#### [Reid Barton (Nov 03 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137088959):
I don't know whether this would be easier or harder, but you don't actually need monoidal categories to do enriched categories; you could enrich in a multicategory instead

#### [Kevin Buzzard (Nov 03 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137089207):
I've found it quite good fun doing abstract maths in Lean. I've not used categories though. But stuff like commutative algebra seems to come out nicely.

#### [Kenny Lau (Nov 03 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137089255):
right, until the module thing came along

#### [Chris Hughes (Nov 03 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137089369):
Lean is often good at abstract stuff. I think maybe abstract usually means it has to be done on paper more formally, because there's less real world intuition.

#### [Scott Morrison (Nov 03 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137103458):
> But stuff like commutative algebra seems to come out nicely.

Stockholm syndrome. :-)

#### [Reid Barton (Nov 05 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137177771):
Scott, are you attached to the name `category_theory.embedding`?
How about `fully_faithful`?

#### [Reid Barton (Nov 05 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137177843):
`embedding` is ambiguous, I feel. Someone may think it implies "injective on objects" for example. The nlab gives a variety of definitions.

#### [Reid Barton (Nov 05 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137177890):
(Also it collides with the top-level `embedding` of topological spaces, which is not `category_theory`'s fault but it did cause some extremely confusing behavior during one of my lean-homotopy-theory mathlib version bumps.)

#### [Scott Morrison (Nov 05 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/137179986):
Yes, we should definitely change this.

#### [Johan Commelin (Nov 05 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815330):
@**Scott Morrison|110087** Do you have any idea why this would fail?
```lean
failed to synthesize type class instance for
X : Type u₁,
𝒳 : category X,
U : X,
f : covering_family U,
p : f.index × f.index
⊢ category (Xᵒᵖ ⥤ Type v₁)
```

#### [Scott Morrison (Nov 05 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815457):
either you're missing the import, or something is weird with universe levels?

#### [Johan Commelin (Nov 05 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815502):
I have
```lean
def presheaf := Xᵒᵖ ⥤ C

variables {X} {C}

instance : category (presheaf X C) := by unfold presheaf; apply_instance
```
in the same file.

#### [Scott Morrison (Nov 05 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815626):
Turn on pp.universes?

#### [Johan Commelin (Nov 05 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815660):
I'll try that. I also see
```
[class_instances] (0) ?x_0 : category (Xᵒᵖ ⥤ Type v₁) := @functor.category ?x_40 ?x_41 ?x_42 ?x_43
failed is_def_eq
```
in the trace.

#### [Johan Commelin (Nov 05 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815837):
Ok, that gave me
```lean
failed to synthesize type class instance for
X : Type u₁,
𝒳 : category.{u₁ v₁} X,
U : X,
f : covering_family.{u₁ v₁} U,
p : f.index × f.index
⊢ category.{(max u₁ (v₁+1)) v₁} (Xᵒᵖ ⥤ Type v₁)
```

#### [Johan Commelin (Nov 05 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815842):
Maybe I don't understand universes well enough...

#### [Johan Commelin (Nov 05 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815850):
Should that last `v_1` be a `v_1 + 1`?

#### [Reid Barton (Nov 05 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815950):
I think it should be `max u_1 v_1`, if I calculated right

#### [Reid Barton (Nov 05 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815980):
Ah, Scott was kind enough to write out the universe parameters in `instance functor.category`.

#### [Reid Barton (Nov 05 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146815996):
My guess: perhaps you are doing something where you actually need `X` to be a small category?

#### [Reid Barton (Nov 05 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816055):
it's hard to say what to do without knowing where that goal is coming from

#### [Johan Commelin (Nov 05 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816060):
But in `yoneda` Scott is doing the same thing as I'm doing. Now I'm really confused.
```lean
variables (C : Type u₁) [𝒞 : category.{u₁ v₁} C]
include 𝒞

def yoneda : C ⥤ ((Cᵒᵖ) ⥤ (Type v₁)) :=
```

#### [Reid Barton (Nov 05 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816089):
Sure you can write down `X\op \func Type v_1`, but it might not have `v_1`-small hom sets.

#### [Reid Barton (Nov 05 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816155):
Which is what your goal is asking for

#### [Mario Carneiro (Nov 05 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816217):
how big are the homsets of the functor category?

#### [Scott Morrison (Nov 05 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816296):
```
variables (C : Type u₁) [𝒞 : category.{u₁ v₁} C] (D : Type u₂) [𝒟 : category.{u₂ v₂} D]
include 𝒞 𝒟

instance functor.category :
  category.{(max u₁ v₁ u₂ v₂) (max u₁ v₂)} (C ⥤ D) :=
```

#### [Scott Morrison (Nov 05 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816308):
I wrote the universe levels explicitly in the definition, as documentation for just these moments. :-)

#### [Johan Commelin (Nov 05 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816354):
Thanks! I'm probably dense, but I'm still confused why Scott could write what he wrote for `yoneda`, and now I want to apply it and Lean complains...

#### [Scott Morrison (Nov 05 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816417):
The danger is always the `u1` appearing the morphism universe level.

#### [Reid Barton (Nov 05 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816437):
Apply what how? What is the actual math?

#### [Scott Morrison (Nov 05 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816449):
So in Yoneda, we don't care about the universe level of the morphisms in the resulting category.

#### [Scott Morrison (Nov 05 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816456):
But you _do_ care.

#### [Scott Morrison (Nov 05 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816472):
You need a category  `category.{(max u₁ (v₁+1)) v₁} (Xᵒᵖ ⥤ Type v₁)`

#### [Johan Commelin (Nov 05 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816490):
Ooops... I crashed the machine I was logged into...

#### [Johan Commelin (Nov 05 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816497):
I was working on the `sheaf` branch.

#### [Johan Commelin (Nov 05 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816561):
https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/sheaf.lean#L41

#### [Scott Morrison (Nov 05 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816588):
But with `category.{u1 v1} X`, you're going to find `Xop \func Type v1` only has a category structure with

#### [Scott Morrison (Nov 05 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816603):
objects in universe `max u1 (v1+1)` (which is fine)

#### [Scott Morrison (Nov 05 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816619):
and morphisms in universe `max u1 v1`

#### [Scott Morrison (Nov 05 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816623):
which breaks your constraint

#### [Johan Commelin (Nov 05 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816683):
I see. So now I should convince Lean that it should be looking for a more relaxed constraint...

#### [Johan Commelin (Nov 05 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146816844):
First need to build mathlib on a new machine. (What is the emoji for compiling?)

#### [Johan Commelin (Nov 05 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817011):
I propose :fencing: for compiling because of https://www.xkcd.com/303/

#### [Reid Barton (Nov 05 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817352):
I guess this is one of the points where one uses universes in a more serious way

#### [Mario Carneiro (Nov 05 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817488):
is this what representable functors are for?

#### [Reid Barton (Nov 05 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817526):
In math one could just pass to a universe in which X is a small category

#### [Kevin Buzzard (Nov 05 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817571):
```quote
is this what representable functors are for?
```
They're used in the Fermat's Last Theorem proof to produce rings out of thin air.

#### [Reid Barton (Nov 05 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817863):
I think your options are
* Assume `X` is a `small_category.{v_1}`
* Have `sieve` take values in presheaves valued in `Type (max u_1 v_1)`
* Redesign limits so that you can talk about the limit of a `w`-sized diagram in a `category.{u v}` (but I don't think this sounds like a good idea)

#### [Reid Barton (Nov 05 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817945):
The first two are both versions of the math "just pick a universe in which X looks small", and it's a matter of where you want to put that shift of universe

#### [Kevin Buzzard (Nov 05 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817951):
The fpqc topology has some issues with large limits. @**Johan Commelin** are you planning on writing something sufficently general to deal with the fpqc topology?

#### [Johan Commelin (Nov 05 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817961):
Yes.

#### [Johan Commelin (Nov 05 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817974):
I want to do sheaves in the biggest generality possible.

#### [Kevin Buzzard (Nov 05 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817983):
Conrad would argue that the fpqc topology "does not exist"

#### [Johan Commelin (Nov 05 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817984):
I think I'll go for option 2.

#### [Reid Barton (Nov 05 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146817988):
Are they actual issues or just issues for people who don't believe in universes?

#### [Kevin Buzzard (Nov 05 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818048):
I don't fully understand the issues

#### [Johan Commelin (Nov 05 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818056):
I think a little bit of both. You need to do resizing at some point. Like we were discussing `kappa`-small stuff a while ago.

#### [Reid Barton (Nov 05 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818087):
I think if you express any topology other than the Zariski one naturally in Lean it will have the same issues as the fpqc topology--otherwise you will need to manually replace your category with an essentially equivalent small one

#### [Kevin Buzzard (Nov 05 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818088):
I do understand that the issue with an fpqc cover is that you can't make a set of all fpqc covers

#### [Kevin Buzzard (Nov 05 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818107):
I'm not sure this is accurate Reid

#### [Kevin Buzzard (Nov 05 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818172):
With the etale topology there is in some formal sense not a set of etale covers

#### [Kevin Buzzard (Nov 05 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818174):
but there is a set of etale covers such that every etale cover is isomorphic to a cover in your set

#### [Kevin Buzzard (Nov 05 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818187):
with fpqc the problem is genuinely worse

#### [Kevin Buzzard (Nov 05 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818188):
because an arbitrary morphism of fields is fpqc

#### [Kevin Buzzard (Nov 05 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818203):
so there is not even a set of isomorphism classes of etale covers of spec(field)

#### [Kevin Buzzard (Nov 05 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818256):
I don't know whether thinking about things in a more universey way makes these two problems become the same

#### [Kevin Buzzard (Nov 05 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818305):
but in ZFC I've always had the impression that they were not the same

#### [Reid Barton (Nov 05 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818326):
Right, that is what I mean--you would not be able to define etale covers as just "a scheme with an etale map to X", because that will live in a too large universe--you need to manually replace the category with an equivalent small one with some kind of cardinality argument

#### [Kevin Buzzard (Nov 05 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818343):
right

#### [Kevin Buzzard (Nov 05 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818352):
but you can't do that for fpqc

#### [Reid Barton (Nov 05 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818363):
right

#### [Reid Barton (Nov 05 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818411):
so there are two kinds of issues which could arise then

#### [Reid Barton (Nov 05 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818486):
one is if you don't accept the universe axiom, then you can't talk about such large collections like the category of sheaves for the fpqc topology on X at all

#### [Kevin Buzzard (Nov 05 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818510):
I believe Conrad is strictly ZFC so rejects the fpqc topology

#### [Reid Barton (Nov 05 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818514):
but that's not an issue if you do accept universes

#### [Scott Morrison (Nov 05 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818575):
@**Johan Commelin** I pushed my (inconclusive) changes to the sheaf branch. Now my dog insists on a walk (in the rain).

#### [Reid Barton (Nov 05 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146818580):
but then a second issue which might come up is: you need to take a limit of sets or something, but because the indexing diagram of the limit is large it could take you outside the category you called Set. And that is a real issue even if you believe in universes

#### [Johan Commelin (Nov 05 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146819009):
@**Scott Morrison|110087** Thanks! I'll take a look!

#### [Kevin Buzzard (Nov 05 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146819201):
Looking through old emails I've exchanged with Conrad on the fpqc matter, he basically says "fppf is enough for everything, and anyone who wants to work with fpqc -- well, that's their problem, and they can work out the details for themselves"

#### [Reid Barton (Nov 05 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146819571):
Another possible approach is https://ncatlab.org/nlab/show/small+presheaf

#### [Reid Barton (Nov 05 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146819792):
I think you can also think of this as like Ind, but with no restriction on the indexing diagrams you allow

#### [Reid Barton (Nov 05 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146819837):
However I don't know whether this is useful for applications in algebraic geometry

#### [Reid Barton (Nov 05 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146819848):
https://ncatlab.org/nlab/show/large+site is a not particularly encouraging page

#### [Johan Commelin (Nov 05 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820504):
@**Reid Barton** Hmmzz, I'm not really making any progress...

#### [Reid Barton (Nov 05 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820515):
I expect you will have other problems, too :slight_smile:

#### [Johan Commelin (Nov 05 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820521):
/me is not designed to think about universe issues...

#### [Johan Commelin (Nov 05 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820597):
What do you think is the best solution for now? Making `X` small?

#### [Reid Barton (Nov 05 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820648):
certainly easiest for the time being

#### [Reid Barton (Nov 05 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820668):
and you don't really lose any generality

#### [Johan Commelin (Nov 05 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820672):
Ok, then I'll leave the headaches for the sheaves refactor that Mario will work on next summer (-;

#### [Reid Barton (Nov 05 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820747):
I think your next problem was going to be: you have some coproducts indexed on a `Type v_1`, but now the morphism size is `max u_1 v_1`

#### [Reid Barton (Nov 05 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146820750):
so you would need to add some `ulift` to align them

#### [Johan Commelin (Nov 05 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821056):
You're completely right.

#### [Johan Commelin (Nov 05 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821111):
So I want my indexing type to be *small* small

#### [Johan Commelin (Nov 05 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821132):
In which universe should the indexing type of a covering family live?

#### [Johan Commelin (Nov 05 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821143):
`max u_1 v_1`?

#### [Reid Barton (Nov 05 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821152):
I thought you were going to make X small instead

#### [Reid Barton (Nov 05 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821157):
so u_1 = v_1

#### [Reid Barton (Nov 05 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821163):
if not, then I'm not sure

#### [Johan Commelin (Nov 05 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821344):
Yes, I am going to do that. So then I should just take `u_1`, right?

#### [Reid Barton (Nov 05 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821455):
Whatever the universe level of X is. It seems we tend to call it `v` in `category_theory`

#### [Reid Barton (Nov 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146821697):
Well, or `u`

#### [Johan Commelin (Nov 05 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146823630):
@**Scott Morrison|110087** Wouldn't it be useful to have `has_pullbacks_of_has_limits` be an instance in general?

#### [Scott Morrison (Nov 05 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146823698):
I'm afraid of doing that before we know that the pullbacks thus produced are "nice enough".

#### [Johan Commelin (Nov 05 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146823713):
Ok, I see.

#### [Scott Morrison (Nov 05 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146823719):
I suspect that you'll only want that instance "in desperation", when you don't have access to a construction of pullbacks that is defeq to something easier to work with than the general limit.

#### [Johan Commelin (Nov 05 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146823743):
Hmmm, ok

#### [Johan Commelin (Nov 05 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146823759):
So now I've made two small edits to `sheaf`.

#### [Johan Commelin (Nov 05 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146823819):
Do you have a minute to look at the errors that remain? I'm very bad at fighting these universe issues.

#### [Scott Morrison (Nov 05 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824066):
hah, we've been duplicating effort :-)

#### [Johan Commelin (Nov 05 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824201):
Well, I didn't do much...

#### [Johan Commelin (Nov 05 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824312):
Do you think the library is ready for this? Or am I making too big a jump?

#### [Scott Morrison (Nov 05 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824367):
We're almost there. :-)

#### [Scott Morrison (Nov 05 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824419):
And this is exactly the sort of stress testing of limits that we need.

#### [Scott Morrison (Nov 05 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824431):
I committed a little, but it's still badly broken, and I have to get the kids to school/me to work.

#### [Johan Commelin (Nov 05 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824449):
Sure, those are more important than silly sheaves (-;

#### [Johan Commelin (Nov 05 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824459):
See you later

#### [Kevin Buzzard (Nov 05 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824782):
I've just been reading SGA4 in the bath

#### [Kevin Buzzard (Nov 05 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824788):
As you do

#### [Kevin Buzzard (Nov 05 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824860):
And very early on when talking about limits and colimits

#### [Kevin Buzzard (Nov 05 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824888):
They assume that the diagram is u-small

#### [Kevin Buzzard (Nov 05 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824928):
ie isomorphic to an element of the universe u

#### [Kevin Buzzard (Nov 05 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824964):
Their categories are u-categories

#### [Kevin Buzzard (Nov 05 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146824981):
Ie hom sets are all in u

#### [Kevin Buzzard (Nov 05 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146825039):
But the limits are over u-small diagrams consistently

#### [Kevin Buzzard (Nov 05 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146825391):
Example theorem : the category of u-abelian groups has u-limits. This *means* that you take the category  whose objects are abelian groups in some universe, and then take a limit but only over a category which is itself an *element* of u

#### [Reid Barton (Nov 05 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146825626):
That's essentially our setup too, see https://github.com/leanprover-community/mathlib/blob/limits-others-new/category_theory/limits/limits.lean#L21-L22

#### [Johan Commelin (Nov 05 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146826137):
@**Scott Morrison|110087** In things like `coequalizer.desc` should the argument `w` get an auto_param `obviously`?

#### [Scott Morrison (Nov 05 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146826530):
Yes, that seems plausible.

#### [Johan Commelin (Nov 05 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146826939):
@**Scott Morrison|110087** I just pushed some more silly stuff. Didn't make fundamental progress.

#### [Johan Commelin (Nov 06 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146850316):
@**Scott Morrison|110087** I don't think `functor.const` should be in `cones`. It is more fundamental. Should this be moved to `functor` or something?

#### [Scott Morrison (Nov 06 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/146851045):
Sounds good.

#### [Reid Barton (Nov 10 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147440403):
@**Johan Commelin** did you ever find a setup for typing the functor arrow in emacs?

#### [Johan Commelin (Nov 10 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147442348):
Nah, haven't looked into it yet. Sorry. Maybe some other emacs user can tell us how to fix this. @**Sebastian Ullrich** ?

#### [Gabriel Ebner (Nov 10 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147442884):
The input abbreviations for emacs are defined here: https://github.com/leanprover/lean-mode/blob/9d6b8471e2044310b4cd7cd3213b1fc8f78ec499/lean-input.el#L407  It should be straightforward to submit a PR adding the new arrows (you might also want to add Scott's calligraphic symbols).

#### [Gabriel Ebner (Nov 10 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147443005):
These are the relevant changes in the vscode extension:
`\McB`, etc. https://github.com/leanprover/vscode-lean/commit/46ef6b277f4b90ef440730e3b2f73f9381aa08b0#diff-7c2385f0b8db521fe81e3d20489e5f12
`\bbA`, etc. https://github.com/leanprover/vscode-lean/commit/0080ed0f7c80b199abf31212a7eb9356d3cbc896#diff-7c2385f0b8db521fe81e3d20489e5f12
`\functor` https://github.com/leanprover/vscode-lean/commit/d3988d9fae1ab4a7e4785486a08c5eddcd33c575#diff-7c2385f0b8db521fe81e3d20489e5f12

#### [Gabriel Ebner (Nov 10 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147443017):
In the long term, we might want to have a common source for these abbreviations that is shared by the editor extensions.

#### [Johan Commelin (Nov 10 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147443021):
@**Gabriel Ebner** Thanks a lot for the links! Once I find some time, I hope to add a PR.

#### [Johan Commelin (Nov 15 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147739528):
Do we know that composition of functors is associative? I can't find it...

#### [Reid Barton (Nov 15 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147739654):
I don't think so, but it is true by defeq at least

#### [Johan Commelin (Nov 15 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147739865):
I see. So I guess this should be added sooner rather than later.

#### [Scott Morrison (Nov 15 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147768822):
It's in `lean-category-theory`, under `functor_categories/isomorphisms.lean`.

#### [Scott Morrison (Nov 15 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147768830):
At least -- it constructs the equality as a natural isomorphism.

#### [Scott Morrison (Nov 15 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147768858):
I thought it would be good to also prove the the unitors and associator for functors satisfy the triangles and pentagon equations, but didn't do that.

#### [Scott Morrison (Nov 15 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147772079):
@**Johan Commelin**, it turned out this was easy to do, so there's a new PR adding unitors and associators for functors, as well as checking the pentagon and triangle. (These will be necessary one day when we want an example of a 2-category!)

#### [Johan Commelin (Nov 16 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147797409):
@**Scott Morrison|110087** @**Reid Barton**  I have a question about yoneda. I find the `yoneda.lean` file a bit confusing. Is there an easy way to extract that `F.obj U` is canonically the same as `yoneda.obj  ⟹ F`, where `U : X` and `F : presheaf X`? Or is this something that we have to add to this file?

#### [Reid Barton (Nov 16 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147797624):
In the adjunctions branch I just sort of ignored most of the contents of `yoneda.lean` and added an `equiv` which I could actually understand

#### [Reid Barton (Nov 16 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147797631):
though I feel this approach isn't ideal either

#### [Johan Commelin (Nov 16 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147802724):
@**Scott Morrison|110087** I don't think this is in your Yoneda file in an equivalent form, is it?
```lean
@[simp] lemma yoneda_sections (U : X) (F : presheaf X) :
(yoneda.obj U ⟹ F) ≅ F.obj U :=
{ hom := show (yoneda.obj U ⟹ F) → (F.obj U), from λ α, α.app U (𝟙 U),
  inv := show F.obj U → yoneda.obj U ⟹ F, from λ s,
  { app := λ V, show _ → F.obj V, from λ i, F.map i s,
    naturality' := λ V₁ V₂ i, by tidy; erw F.map_comp; tidy },
  hom_inv_id' :=
  begin
    ext α V i,
    tidy {trace_result := tt},
    have := congr (α.naturality i),
    dsimp at this,
    erw ←(this rfl),
    simp
  end,
  inv_hom_id' := by tidy; erw F.map_id; tidy }
```
That `hom_inv_id'` is particularly nasty. Would `tidy` + `rewrite_search` be able to deal with that?

#### [Scott Morrison (Nov 16 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147803013):
No, we've already got this. This iso is just a component of the natural isomorphism produced in `yoneda_lemma`.

#### [Scott Morrison (Nov 16 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147803015):
```
@[simp] lemma yoneda_sections (X : C) (F : Cᵒᵖ ⥤ Type v₁) : (yoneda.obj X ⟹ F) ≅ ulift.{u₁} (F.obj X) :=
nat_iso.app (yoneda_lemma C) (X, F)
```

#### [Scott Morrison (Nov 16 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147803018):
should do it.

#### [Scott Morrison (Nov 16 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147803027):
If you're already working in a small category you can remove the `ulift`.

#### [Scott Morrison (Nov 16 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147803088):
`yoneda_lemma` is the natural isomorphism between the two functors starting with `(X, F)`. You can either embed `X` into presheafs, via the yoneda embedding, and then take hom, or you can just evaluate `F` on `X`.

#### [Scott Morrison (Nov 16 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147803312):
And
```
omit 𝒞
def ulift_trivial (V : Type u₁) : ulift.{u₁} V ≅ V := by tidy

@[simp] def yoneda_sections_small {C : Type u₁} [small_category C] (X : C) (F : Cᵒᵖ ⥤ Type u₁) : (yoneda.obj X ⟹ F) ≅ F.obj X :=
nat_iso.app (yoneda_lemma C) (X, F) ≪≫ ulift_trivial _
```
gives you the version you want, for small categories.

#### [Scott Morrison (Nov 16 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147803314):
Shall I just push this as a separate PR?

#### [Scott Morrison (Nov 16 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147803361):
Sorry, it was an obvious omission in writing `yoneda.lean`, just writing out the main result in components.

#### [Scott Morrison (Nov 16 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147804444):
This is available at https://github.com/leanprover/mathlib/pull/480.

#### [Scott Morrison (Nov 16 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147804449):
It depends on the limits PR, because it's not worth backporting, but you're welcome to merge into the `sheaf` branch.

#### [Johan Commelin (Nov 16 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147827210):
@**Scott Morrison|110087** Ok cool! I kept on struggling with that product category. But this looks really nice!

#### [Johan Commelin (Nov 17 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147868545):
@**Scott Morrison|110087** Is `iso_of_is_iso` missing in the library?

#### [Scott Morrison (Nov 17 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147868567):
Yes, lots of iso stuff is missing, that I've just been discovering now. :-)

#### [Scott Morrison (Nov 17 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147868569):
I've been filling it in the monoidal categories repository, which is where I need it immediately.

#### [Scott Morrison (Nov 17 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147868576):
Is it holding you up? I can make yet another PR to mathlib with some improvements to the `iso` and `is_iso` interface.

#### [Johan Commelin (Nov 17 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147868625):
```lean
def iso_of_is_iso {X Y : C} {f : X ⟶ Y} (h : is_iso f) : X ≅ Y :=
{ hom := f,
  ..h}
```
That's whay I have at the top of my file now.

#### [Scott Morrison (Nov 17 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147868668):
Ok, if that's keeping you afloat for now, I'll finish up a few things before making a "fixing isos" PR. It turns out there are at least a dozen other things missing too. :-)

#### [Scott Morrison (Nov 17 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147868676):
As I'm sure Mario has told us many times before, you actually have to use this stuff!

#### [Johan Commelin (Nov 17 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147869737):
@**Scott Morrison|110087** I just pushed a whole bunch of stuff to the `sheaf` branch. If you want more data points for how stuff is used...

#### [Johan Commelin (Nov 17 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/147869739):
I'm gathering stuff that should move elsewhere at the top of the file. If it fits into PRs that you are preparing, please take it.

#### [David Michael Roberts (Nov 21 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148077160):
```quote
I do understand that the issue with an fpqc cover is that you can't make a set of all fpqc covers
```
 The issue is that there is not even a set of fpqc covers whose elements refine all possible fpqc covers, whereas for fppf and coarser this is true, even when there's not a set of isomorphism classes of covers. This is a genuine problem, and there is a model of ZF whose category of sets forms a large site with this 'feature' (with covers=surjective functions).

#### [David Michael Roberts (Nov 21 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148077261):
One can of course consider whether a given presheaf is a fpqc sheaf or not, but forget trying to fpcq-sheafify in general. The hypotheses of the general adjoint functor theorem are not satisfied, so one cannot construct the left adjoint to Sh_fpqc(Aff) --> PreSh(Aff).

#### [Johan Commelin (Nov 27 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148639830):
I currently have
```lean
@[simp] lemma map_left_id : map_left R (nat_trans.id L) ≅ functor.id _ :=
{ hom :=
  { app := λ X, { left := 𝟙 _, right := 𝟙 _ } },
  inv :=
  { app := λ X, { left := 𝟙 _, right := 𝟙 _ } } }
```
but that is a worthless simp-lemma because of `≅`. I think that in fact equality should hold:
```lean
@[simp] lemma map_left_id' : map_left R (nat_trans.id L) = functor.id _ := sorry
```
But I have no idea how to prove that two terms of a structure are equal. Is it true that they are equal if all their fields are equal? Is this somewhere in mathlib?

#### [Reid Barton (Nov 27 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640013):
This is generally what extensionality lemmas do... but you're probably going to have a bad time working with equality of functors

#### [Reid Barton (Nov 27 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640081):
what's `map_left`?

#### [Reid Barton (Nov 27 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640129):
Never mind, I figured it out from one of your other messages

#### [Patrick Massot (Nov 27 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640189):
Not sure it will help, but your question looks like the classic:
```lean
structure johan :=
(a : ℕ)
(aone : a = 1)

lemma johan.ext (X Y : johan) (h : X.a = Y.a) : X = Y :=
begin
  cases X, 
  cases Y,
  congr ; assumption
end
```

#### [Patrick Massot (Nov 27 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640204):
sorry about the silly example, but I wanted a structure including at least one data and one proof field

#### [Johan Commelin (Nov 27 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640336):
@**Patrick Massot** Thanks, I should have thought about `cases`.

#### [Reid Barton (Nov 27 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640349):
I think what you have now is the best way

#### [Johan Commelin (Nov 27 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640352):
@**Reid Barton** Well, but working with natural isomorphisms is also a massive pain atm.

#### [Reid Barton (Nov 27 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640456):
I guarantee it is not as bad as rewriting morphisms across equalities of objects and then trying to reason about the result

#### [Patrick Massot (Nov 27 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148640556):
We should really setup a FAQ somewhere

#### [Johan Commelin (Nov 27 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148662831):
@**Scott Morrison|110087** I have no idea if this makes any sense, but I regularly get errors like these:
```lean
type mismatch at application
  colimit.pre_map (comma.fst yoneda (functor.of_obj X) ⋙ F) ((comma.map_right_id' yoneda (functor.of_obj X)).hom)
term
  (comma.map_right_id' yoneda (functor.of_obj X)).hom
has type
  comma.map_right yoneda (𝟙 (functor.of_obj X)) ⟶ functor.id (comma yoneda (functor.of_obj X)) : Type (max
        (max ? v)
        v
        ?)
but is expected to have type
  ?m_3 ⟹ ?m_4 : Type v
```
Would it help to just get rid of the notation `⟹`, and always speak of natural transformations as homs in the functor category?

#### [Johan Commelin (Nov 27 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148662863):
Or is this a stupid universe issue again? (I just realise there are annoying `?` in the error...)

#### [Johan Commelin (Nov 27 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148662980):
Ok, never mind. It's a universe issue.

#### [Kenny Lau (Nov 27 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148664964):
@**Johan Commelin** how do you get that many colours

#### [Johan Commelin (Nov 27 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148665094):
I had `less` syntax, instead of `lean` :upside_down: @**Kenny Lau**

#### [Scott Morrison (Nov 27 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148666324):
```quote
I guarantee it is not as bad as rewriting morphisms across equalities of objects and then trying to reason about the result
```
 Yes. This. Please don't prove equalities between functors, you are just setting yourself up for suffering.

#### [Reid Barton (Nov 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148670683):
```quote
Would it help to just get rid of the notation `⟹`, and always speak of natural transformations as homs in the functor category?
```
I have actually wondered about this too, after a few minor annoyances involving the difference between `nat_trans.vcomp` and `category.comp`.

#### [Reid Barton (Nov 27 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148670713):
It's hard to predict which one you will get once you start talking about colimits in categories of presheaves, as Johan has probably also experienced.

#### [Reid Barton (Nov 27 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148671054):
It might be a rather invasive change though, or even not workable for some reason

#### [Scott Morrison (Nov 27 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148673378):
I've experienced the same pain, but haven't tried removing `⟹`. It seems a reasonable experiment, however.

#### [Johan Commelin (Nov 28 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148696347):
I don't like the idea of setting myself up for suffering.

#### [Johan Commelin (Nov 28 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148696378):
But I'm suffering hard at the moment.

#### [Johan Commelin (Nov 28 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148696393):
After all `functor.id ⋙ F` is not defeq to `F`, and so we need some natural isomorphisms, and I just get the general feeling that we are walking headfirst into nasty 2-categorical territory.

#### [Johan Commelin (Nov 28 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148696399):
Because, say what you like, but Lean isn't very good at working with the canonical natural isomorphism between `functor.id ⋙ F` and `F`.

#### [Johan Commelin (Nov 28 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148696451):
I've got the following context:
```lean
C : Type v,
𝒞 : small_category C,
D : Type u,
𝒟 : category D,
F : C ⥤ D,
_inst_1 : has_colimits D,
X : presheaf C
⊢ colimit.pre (comma.fst yoneda (functor.of_obj X) ⋙ F) (comma.map_right yoneda (𝟙 (functor.of_obj X))) =
    𝟙 (colimit (comma.fst yoneda (functor.of_obj X) ⋙ F))
```
This might look a bit daunting, but `(comma.map_right yoneda (𝟙 (functor.of_obj X)))` is naturally isomorphic to `functor.id _`

#### [Johan Commelin (Nov 28 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148696511):
@**Scott Morrison|110087** I'm really lost here. The maths is trivial. But Lean is fighting back hard.

#### [Scott Morrison (Nov 28 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148696896):
Want to point me to a file and a commit?

#### [Johan Commelin (Nov 28 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697034):
@**Scott Morrison|110087** https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/presheaf.lean#L69

#### [Johan Commelin (Nov 28 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697048):
Maybe I still don't know how to let the library do the heavy lifting for me...

#### [Scott Morrison (Nov 28 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697316):
woah, checking out that branch is like stepping into the future. adjunctions, cocompletions, groupoids, oh my.

#### [Johan Commelin (Nov 28 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697393):
Well, most of that is by Reid.

#### [Johan Commelin (Nov 28 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697415):
Or I should say: all of *that* is by Reid.

#### [Scott Morrison (Nov 28 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697497):
Can we not call functors `f`, when they could perfectly well be `F`?

#### [Scott Morrison (Nov 28 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697542):
Also, I feel you're slightly overusing variables. Things like `map` and `map'` should have the variable `F : C \func D` visible right there at the definition.

#### [Scott Morrison (Nov 28 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697554):
variables are great for implicit arguments, or even the primary argument if they are the sole primary argument for 20 definitions in a row...

#### [Johan Commelin (Nov 28 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697568):
Sure. I was using `F` for presheaves, but I decided that maybe I shouldn't yet do that.

#### [Johan Commelin (Nov 28 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697647):
Anyway, you shouldn't look too much at the `sheaf.lean` file. It will need a major rewrite once I have working presheaves.

#### [Scott Morrison (Nov 28 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697740):
Lots of stuff doesn't compile?

#### [Scott Morrison (Nov 28 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697742):
In the imports of presheaf.lean

#### [Johan Commelin (Nov 28 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697786):
Hmmm... I thought those were fine... but maybe stuff broke.

#### [Scott Morrison (Nov 28 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697789):
e.g. limits/limits.lean and adjunctions.lean

#### [Johan Commelin (Nov 28 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697815):
adjunctions probably don't compile

#### [Johan Commelin (Nov 28 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697822):
limits should work, but maybe it broke after I merged in Reid's branch

#### [Scott Morrison (Nov 28 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697824):
Ok, I see the thing you probably need, which is naturality in the second argument of colimit.pre

#### [Scott Morrison (Nov 28 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697831):
I can try to provide you that, and you can try to get stuff to compile :-)

#### [Johan Commelin (Nov 28 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697896):
Ok, so I have `colimit.pre_map`

#### [Scott Morrison (Nov 28 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697904):
yes, but that's naturality in the first argument, which isn't what you need

#### [Johan Commelin (Nov 28 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697907):
But I guess we need to upgrade `pre` into a functor?

#### [Scott Morrison (Nov 28 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697911):
unfortunately I think that might need to wait for 2-categories, I'm not sure. :-)

#### [Johan Commelin (Nov 28 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697919):
Right... but it is where this stuff is sucking us into, not?

#### [Scott Morrison (Nov 28 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697960):
I'm actually not sure where I should do this work. The main `limits` branch is now a bit stranded, as Reid has been pulling stuff out into separate PRs.

#### [Scott Morrison (Nov 28 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697966):
Doing work on the limits branch now may get orphaned, I'm not sure.

#### [Johan Commelin (Nov 28 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697980):
Maybe dump it into `sheafy_preamble`

#### [Johan Commelin (Nov 28 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148697995):
I've been using that file to collect all sorts of facts that I need.

#### [Scott Morrison (Nov 28 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698006):
Yeah, I'm worried about that getting orphaned too. :-)

#### [Scott Morrison (Nov 28 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698050):
We're playing a bit fast and loose with our branches at the moment.

#### [Johan Commelin (Nov 28 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698056):
Very much.

#### [Johan Commelin (Nov 28 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698093):
So what exactly is the statement that you are trying to prove?

#### [Scott Morrison (Nov 28 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698100):
@**Reid Barton**, I'd really like to straighten out the limits branches a bit. What is the best way to "rebase" (possibly by hand) everything remaining on top of `limits-2`? Is this a bad thing to want to do?

#### [Scott Morrison (Nov 28 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698145):
No idea :-) I hadn't even started.

#### [Scott Morrison (Nov 28 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698181):
Say we have a natural transformation a : E \natt E'.

#### [Scott Morrison (Nov 28 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698235):
colim.map (a >>> F) gives a map from colim (E >>> F) to colim (E' >>> F)

#### [Scott Morrison (Nov 28 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698250):
presumably the triangle, obtained by mapping both of those to colim F via colim.pre, commutes?

#### [Scott Morrison (Nov 28 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698274):
So then if a is invertible, we have `colim.pre F E = colim.map (a^{-1} >>> F) >> colim.pre F E' >> colim.map (a >>> F)`.

#### [Scott Morrison (Nov 28 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698318):
and hopefully now if E' is the identity, as in your case, everything quickly simplifies from there

#### [Johan Commelin (Nov 28 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698343):
So `pre_map` is saying that this triangle commutes.

#### [Scott Morrison (Nov 28 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698410):
No. `pre_map` is about changing the functor `F`, not the functor `E`.

#### [Johan Commelin (Nov 28 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698416):
But if `E' = functor.id _` it still doesn't simplify, because `functor.id _ >>> F` is not `F`. For example `colimit.pre F (functor.id _) = \b1 (colimit F)` does not typecheck :sad:

#### [Scott Morrison (Nov 28 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698417):
I've just been looking at the history of the `sheaf` branch.

#### [Johan Commelin (Nov 28 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698433):
@**Scott Morrison|110087** I think you are confusing `map_pre` and `pre_map`.

#### [Scott Morrison (Nov 28 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698437):
And ... you're up shit creek without a paddle. :-)

#### [Johan Commelin (Nov 28 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698441):
`pre_map` is something I added. It is in `sheafy_preamble.lean`

#### [Scott Morrison (Nov 28 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698445):
Getting `sheaf` back on top of master after `limits-2` is merged is going to suck.

#### [Johan Commelin (Nov 28 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698488):
@**Scott Morrison|110087** I will probably just copy-paste stuff into a new branch...

#### [Scott Morrison (Nov 28 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698489):
I'm looking at
```
lemma colimit.pre_map {K : Type v} [small_category K] [has_colimits_of_shape K C] (E : K ⥤ J) :
  colimit.pre F E ≫ colim.map α = colim.map (whisker_left E α) ≫ colimit.pre G E :=
by ext; rw [←assoc, colimit.ι_pre, colim.ι_map, ←assoc, colim.ι_map, assoc, colimit.ι_pre]; refl
```
in `limits-2`.

#### [Scott Morrison (Nov 28 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698507):
I see. But yes, your `pre_map` is what we need. :-)

#### [Johan Commelin (Nov 28 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698523):
Aaahrg... so the names have changed...

#### [Johan Commelin (Nov 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698565):
What is called `pre_map` in `limits-2` used to be `map_pre` on your old limits branch.

#### [Johan Commelin (Nov 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698572):
Ok, so in `presheaf.lean` you can see that I already `erw`d the `pre_map`-thingy.

#### [Scott Morrison (Nov 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698574):
I see. :-) Reid must have fixed it. :-) As I said, up a creek! :-)

#### [Scott Morrison (Nov 28 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698581):
Well, I can't see that, because nothing compiles. :-)

#### [Scott Morrison (Nov 28 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698603):
So, you need to keep the `colim.map` in there for the unitor.

#### [Johan Commelin (Nov 28 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698613):
Sorry, I need to run to a seminar...

#### [Johan Commelin (Nov 28 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698663):
And I'm sorry that stuff doens't compile. I still have some sort of interactive VScode when I work on this...

#### [Johan Commelin (Nov 28 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698669):
Maybe I should just wait till limits are merged, and then start from scratch.

#### [Scott Morrison (Nov 28 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698678):
You just want to know that
```
colimit.pre F (functor.id _) = colimit.map (left_unitor F)
```
(that's not meant to be real code).

#### [Scott Morrison (Nov 28 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148698746):
Okay, in any case, keep bugging me about this. I'd both like to help, and like to see the resolution. I think it's going to be fine. :-)

#### [Johan Commelin (Nov 28 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148704306):
@**Scott Morrison|110087** Thanks for all your comments. I'll see if I can make any progress.

#### [Reid Barton (Nov 28 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148708825):
Oh yeah, I noticed all the `limit.` lemmas had names of the form `limit.foo_bar` if the left-hand side looked like `limit.foo ... >> limit.bar ...`, and so I reversed the components of all the names of the corresponding `colimit` lemmas because they have the composition on the left-hand side in the other order.

#### [Reid Barton (Nov 28 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148708855):
Actually I just copied and pasted the limit lemmas to make colimit versions, I ignored whatever was there before (which I think was not a full set of matching lemmas)

#### [Johan Commelin (Nov 28 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148709058):
@**Scott Morrison|110087** I fixed a bunch of compile issues, which we due to `functor.const` being picked from the wrong namespace (even though `category_theory` seems to be open). I really hope Lean 4 will kick a lot of these things out of the root namespace, because these conflicts are quite annoying.

#### [Reid Barton (Nov 28 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148709086):
Yeah I encountered that same `functor.const` issue too, not sure what caused it to crop up suddenly

#### [Keeley Hoek (Nov 28 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148709263):
Does @[priority] affect that kind of resolution?

#### [Reid Barton (Nov 28 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148710423):
I can try to produce a rebased version of my `adjunctions` branch, that shouldn't take too long.

#### [Reid Barton (Nov 28 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148712087):
It looks like Johan has mostly just been working on one file, so probably easiest to just copy the `sheaf` branch into a new branch indeed

#### [Reid Barton (Nov 28 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148712367):
Oh, also the specific shape limit stuff isn't in `limits-2` yet. I do have a copy that at least builds on top of `limits-2` though, so I can push that somewhere as a temporary measure for you, Johan

#### [Johan Commelin (Nov 28 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148712439):
Ooh, don't worry too much about this

#### [Johan Commelin (Nov 28 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148712447):
I think it's best to fix it after `limits-2` is merged.

#### [Reid Barton (Nov 28 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148712710):
Ah, fair enough. I'll hold off on these things then

#### [Johan Commelin (Nov 28 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148720854):
I'm very confused about https://github.com/leanprover-community/mathlib/blob/sheaf/category_theory/commas.lean#L155-L156
I thought I understood `rfl` by now. But apparently this is not `rfl`. If someone can explain this mystery, I would be very grateful.

#### [Gabriel Ebner (Nov 28 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148721486):
`map_right_id'` should be a `def`.  Theorems don't unfold (except for special circumstances / options).

#### [Johan Commelin (Nov 28 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148721547):
Aaah, it should certainly be a `def`. Let me try again.

#### [Johan Commelin (Nov 28 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148721603):
@**Gabriel Ebner** Cool! Now it works.

#### [Kevin Buzzard (Nov 28 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148727291):
Computer scientists have such weird ideas about what a theorem is :-)

#### [Johan Commelin (Nov 28 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148728262):
@**Scott Morrison|110087** @**Reid Barton** I suggest we replace `of_obj` with `of.obj` after defining
```lean
namespace functor
variables {C : Type u} [𝒞 : category.{u v} C]
include 𝒞

def of : C ⥤ (punit ⥤ C) := const punit

namespace of
@[simp] lemma obj_obj (X : C) : (of.obj X).obj = λ _, X := rfl
@[simp] lemma obj_map (X : C) : (of.obj X).map = λ _ _ _, 𝟙 X := rfl
@[simp] lemma map_app {X Y : C} (f : X ⟶ Y) : (of.map f).app = λ _, f := rfl
end of

end functor
```
Is that ok?

#### [Reid Barton (Nov 28 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148728479):
Yes, that seems sensible

#### [Reid Barton (Nov 28 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148748886):
```quote
@**Scott Morrison|110087** I fixed a bunch of compile issues, which we due to `functor.const` being picked from the wrong namespace (even though `category_theory` seems to be open). I really hope Lean 4 will kick a lot of these things out of the root namespace, because these conflicts are quite annoying.
```
If someone could track this down, it would be super helpful. I'm not sure what changed here.

#### [Johan Commelin (Nov 30 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148861225):
@**Reid Barton** @**Scott Morrison|110087** Do you think we need something like this? I find it extremely annoying that Lean refuses some of my morphisms because the come from an opposite category. I understand why Lean complains, but getting it to accept the arrow is extremely annoying. This might help...
```lean
namespace category.hom
variables {C : Type u} [𝒞 : category.{u v} C]
include 𝒞

def op {X Y : C} (f : X ⟶ Y) : @category.hom _ category_theory.opposite Y X := f
def deop {X Y : Cᵒᵖ} (f : X ⟶ Y) : @category.hom _ 𝒞 Y X := f

@[simp] lemma op_deop {X Y : C} (f : X ⟶ Y) : f.op.deop = f := rfl
@[simp] lemma deop_op {X Y : Cᵒᵖ} (f : X ⟶ Y) : f.deop.op = f := rfl

end category.hom
```

#### [Scott Morrison (Dec 01 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/148898413):
This sounds fine to me. I agree dealing with opposites is gross. :-(

#### [Johan Commelin (Dec 03 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150778353):
@**Reid Barton** Have you had similar experiences? What is your opinion on my proposed solution?

#### [Scott Morrison (Dec 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150835179):
Hi @**Johan Commelin**, I am experimenting with making `op` irreducible, and thus _requiring_ the use of `op` or `deop` (and corresponding `op_obj` and `deop_obj` on objects).

#### [Scott Morrison (Dec 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150835194):
It is slightly grosser, but I think we've all discovered that too much can go mysteriously wrong with the current implementation of opposites.

#### [Johan Commelin (Dec 04 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150835467):
@**Scott Morrison|110087** Aah, that sounds like a good idea!

#### [Johan Commelin (Dec 04 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150835496):
I hadn't thought about making it irreducible. Those boundaries are useful, but I'm not yet aware of how to make the system help us.

#### [Johan Commelin (Dec 04 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150835503):
So yes, I think it is very good if we have to be explicit about `op`ing and `deop`ing.

#### [Scott Morrison (Dec 04 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150840492):
#510

#### [Johan Commelin (Dec 04 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150841470):
@**Scott Morrison|110087** Looks good to me. I do wonder if we can remove the `_obj` suffix to make things a bit shorter. We could rename the existing `op` to `op_cat`.

#### [Johan Commelin (Dec 04 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/150841491):
I think this is a good PR, but I regret that a lot of stuff is also becoming somewhat uglier.

#### [Kevin Buzzard (Dec 11 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151459647):
@**Ramon Fernandez Mir** is making me engage with the category theory stuff! Is there a name for this map: `(λ f r, f r : (FF.obj x ⟶ FF.obj y) → (FF.obj x → FF.obj y)) `? I'm changing a long arrow to a short one. The target of the functor FF is the category `CommRing`, so I want to take an abstract element of the hom set and actually produce the ring hom. There's a coercion that does it magically, but I actually have a set of abstract homs and want a set of concrete homs and I have to feed `set.image` something.

#### [Johan Commelin (Dec 11 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151461302):
@**Kevin Buzzard** Could you provide slightly more context? I typically get away without doing anything.

#### [Kevin Buzzard (Dec 11 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151461833):
We had a functor `FF` from a small category `J` to `CommRing` and two objects `x` and `y` of `J`, and we wanted the set of maps from $$FF(x)$$ to $$FF(y)$$ coming from `J`.

#### [Johan Commelin (Dec 11 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151461946):
I see, and `FF.obj x \hom FF.obj y` is a subtype, but you want a set?

#### [Johan Commelin (Dec 11 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151461981):
Is that correct? If so, I think `subtype.val` would be the function you are looking for.

#### [Johan Commelin (Dec 11 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151461995):
I don't know by heart how `CommRing` is defined.

#### [Kevin Buzzard (Dec 11 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151462204):
I'm trying to get from `category_theory.category.hom R S` to `R -> S`

#### [Kevin Buzzard (Dec 11 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151462333):
I can just evaluate a term of type `category_theory.category.hom R S` at `r` and get `s : S`

#### [Kevin Buzzard (Dec 11 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151462431):
but I was wondering what the name of the coercion was, because I needed to refer to the map itself when doing something else.

#### [Johan Commelin (Dec 11 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151465278):
@**Kevin Buzzard** On line 90 of `category.lean` you can find
```lean
{ hom   := λa b, subtype (hom a.2 b.2),
```
(This is in the instance of `concrete_category` --> `category`.) So the map you want is called `subtype.val`.

#### [Reid Barton (Dec 11 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151467554):
I think there is (or should be?) some more high-level name for this, like `forget`

#### [Johan Commelin (Dec 11 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151469130):
@**Kevin Buzzard** That's right. As Reid mentioned, there is a `forget`ful functor. You will have to
```lean
import category_theory.types
```

#### [Reid Barton (Dec 11 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151469476):
Ah that's where it is

#### [Reid Barton (Dec 14 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151755507):
@**Kevin Buzzard** did you end up using `forget`? I'm inclined to make its "C" argument implicit, would that help or hurt you?

#### [Kevin Buzzard (Dec 14 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151758445):
I didn't do anything. I was talking about it with Ramon at our last meeting and haven't thought about it since

#### [Kevin Buzzard (Dec 14 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/151758486):
I am completely snowed under with teaching and reference writing

#### [Ramon Fernandez Mir (Dec 23 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Category%20theory/near/152438280):
@**Reid Barton** sorry I just saw this. I was playing with that code a few days ago and I didn't manage to make it work with forget. What is the "C" argument meant to be?

