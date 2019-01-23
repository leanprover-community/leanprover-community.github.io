---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/71101extendpresheaffrombasis.html
---

## Stream: [maths](index.html)
### Topic: [extend presheaf from basis](71101extendpresheaffrombasis.html)

---

#### [Johan Commelin (Oct 10 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135529957):
@**Scott Morrison|110087** Somehow this is not doing what I hoped:
```lean
import category_theory.presheaves
import category_theory.sheaves
import category_theory.limits

open category_theory
open category_theory.examples
open category_theory.limits

universes u v w

variables {X : Top.{u}}
variables {V : Type v} [𝒱 : category.{v w} V] [has_limits.{v w} V]
include 𝒱

def extend {B : set (set X)} (h : topological_space.is_topological_basis B) (F : presheaf B V) :
presheaf (open_set X) V :=
{ obj  := λ U, limit ((full_subcategory_embedding (λ U' : B, U'.1 ⊆ U)) ⋙ F),
  map' := sorry }

```

#### [Johan Commelin (Oct 10 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530007):
The embedding is complaining about universes. I don't get why.

#### [Scott Morrison (Oct 10 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530180):
@**Johan Commelin**, I'm just guessing here, but there are universe constraints in taking limits.

#### [Kevin Buzzard (Oct 10 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530263):
I don't know anything about your errors but even seeing that you're daring to write this sort of code -- "extending a presheaf from a basis might be possible" -- makes me quite excited for the future.

#### [Scott Morrison (Oct 10 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530292):
In particular, the index category is meant to be a category.{v v}, and the target category is meant to be a category.{u v}.

#### [Scott Morrison (Oct 10 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530306):
If you don't satisfy those constraints to begin with, you're going to have to ulift.

#### [Scott Morrison (Oct 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530319):
Me too, by the way --- I'm very excited to see things like this work!

#### [Johan Commelin (Oct 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530322):
But it is looking for some `Type w`. I really don't know where it is getting that from?

#### [Johan Commelin (Oct 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530326):
Do you have comma categories somewhere?

#### [Kevin Buzzard (Oct 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530327):
One thing which might be obvious to everyone already is that of course when you extend, you don't literally "extend", you define a new object on all open sets, and its values on basic open sets are isomorphic to, but not defeq to, the values taken by the old object.

#### [Johan Commelin (Oct 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530330):
I just want the category of opens contained in `U`.

#### [Johan Commelin (Oct 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530334):
Maybe you already have this somewhere...

#### [Johan Commelin (Oct 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530386):
@**Kevin Buzzard** Do you want me to include the scare-quotes in the definition :lol: ?

#### [Kevin Buzzard (Oct 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135530402):
I am just being reminded of the nightmares I had when doing sheaves by hand in the schemes project.

#### [Scott Morrison (Oct 10 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135531230):
Sorry, I will try to look at this soon. I'm working on installation instructions, still. :-)

#### [Scott Morrison (Oct 10 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135531457):
@**Johan Commelin** , is that code available somewhere? I'd like to look at the universe issue.

#### [Scott Morrison (Oct 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135531508):
(universes scare the bejeebus out of me, and I'm perpetually terrified that someone is going to discover I've still got them wrong in the category theory library)

#### [Reid Barton (Oct 10 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135531525):
You have made V a category.{v w} which means you can only form limits of size w

#### [Scott Morrison (Oct 10 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135531577):
(phew, that's Reid agreeing with me... my heart rate is dropping again. :-)

#### [Johan Commelin (Oct 10 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135532719):
Hmmm, let me take another look.
@**Scott Morrison|110087** All the code I have is what I posted above.

#### [Johan Commelin (Oct 10 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135533061):
@**Reid Barton** I still don't get what is wrong with my code.

#### [Johan Commelin (Oct 10 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135533127):
@**Scott Morrison|110087** Here is a snippet that is probably useful for `over.lean`:
```lean
section over
variables {C : Type u} [𝒞 : category.{u v} C]
include 𝒞

def over.forget (Z : C) : over Z ⥤ C :=
{ obj  := λ X, X.1,
  map' := λ X Y f, f.1 }

end over
```

#### [Scott Morrison (Oct 10 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135533245):
Thanks, I added `over.forget`.

#### [Johan Commelin (Oct 10 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135533671):
@**Scott Morrison|110087** Ok, so I should take `X : Top.{w}`. It is important that I don't take `Top.{u}`. Can you explain why?

#### [Scott Morrison (Oct 10 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135533722):
> Reid Barton: You have made V a category.{v w} which means you can only form limits of size w

#### [Johan Commelin (Oct 10 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135533800):
Ok... I don't think I care too much. It is a bit tricky to get right. I wouldn't mind if Lean just scaled everything into the right universe. But I guess that brings some tradeoff in foundations that I don't understand.

#### [Johan Commelin (Oct 10 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534835):
@**Scott Morrison|110087** May we *please* have presheaves be contravariant. My head is breaking without the `op`s.

#### [Scott Morrison (Oct 10 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534843):
no problem

#### [Scott Morrison (Oct 10 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534855):
We need to make a PR to mathlib to fix this, right?

#### [Johan Commelin (Oct 10 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534862):
No, presheaves aren't in mathlib

#### [Johan Commelin (Oct 10 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534868):
Or did you break the definition of `open_set`?

#### [Scott Morrison (Oct 10 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534920):
Yes :-)

#### [Johan Commelin (Oct 10 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534931):
Aaah, ok. Hmmz.

#### [Johan Commelin (Oct 10 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534940):
Well... yes. Then we need a PR.

#### [Scott Morrison (Oct 10 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534954):
Regarding automating the copy-and-paste: I really doubt this can work in most of my cases here, where the rewrites are occurring in auto_params for structure fields.

#### [Scott Morrison (Oct 10 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135534963):
The tactic `obviously` doesn't even appear.

#### [Johan Commelin (Oct 10 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535588):
@**Scott Morrison|110087** I'm stuck on
```lean
⊢ (U₁ ⟶ U₂) → U₂.s ⊆ U₁.s
```
After that we have extended presheaves.

#### [Johan Commelin (Oct 10 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535607):
That goal looks like very trivial. But I don't know how to extract the inclusion from the hom.

#### [Scott Morrison (Oct 10 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535652):
try `intro`, then `cases`?

#### [Johan Commelin (Oct 10 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535661):
Aah `cases`.

#### [Scott Morrison (Oct 10 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535664):
or commit something I can poke at

#### [Scott Morrison (Oct 10 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535697):
remember that hom there is probably some ulift plift gadget

#### [Scott Morrison (Oct 10 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535704):
to turn a Prop into a Type at whatever universe you're living in

#### [Johan Commelin (Oct 10 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535763):
Right, it's working now. Except that it couldn't figure out `comp'` on its own :sad:

#### [Johan Commelin (Oct 10 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135535779):
```lean
import category_theory.presheaves
import category_theory.sheaves
import category_theory.limits

open category_theory
open category_theory.examples
open category_theory.limits

universes u v w

section extend
variables {X : Top.{w}}
variables {V : Type v} [𝒱 : category.{v w} V] [has_limits.{v w} V]
include 𝒱

variables {B : set (open_set X)}
(h : topological_space.is_topological_basis ((λ U : open_set X, U.s) '' B))

def extend (F : presheaf B V) :
presheaf (open_set X) V :=
{ obj  := λ U, limit ((full_subcategory_embedding (λ U' : B, U'.1 ⊆ U)) ⋙ F),
  map' := λ U₁ U₂ ι,
    limit.lift (full_subcategory_embedding (λ (U' : ↥B), U'.val ⊆ U₂) ⋙ F)
    { X := limit (full_subcategory_embedding (λ (U' : ↥B), U'.val ⊆ U₁) ⋙ F),
      π := λ U, begin dsimp,
      refine limit.π _ ⟨U.1, set.subset.trans U.2 _⟩ ≫ _,
      { cases ι, cases ι, exact ι },
      { exact 𝟙 _ } end } }

end extend
```

#### [Scott Morrison (Oct 10 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135537106):
Perhaps giving a name to `full_subcategory_embedding ...` will make this look nicer.

#### [Scott Morrison (Oct 10 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135537134):
I'd be curious to see that goals after `tidy` on `comp'`.

#### [Scott Morrison (Oct 10 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135537207):
I wonder if we need some extra help for posets here.

#### [Johan Commelin (Oct 10 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135537749):
@**Scott Morrison|110087** Here is what I have now:
```lean
import category_theory.presheaves
import category_theory.sheaves
import category_theory.limits

open category_theory
open category_theory.examples
open category_theory.limits

universes u v w

section under_set
variables {X : Top.{v}}

def under_set (B : set (open_set X)) (U : open_set X) : set B := (λ U' : B, U'.1 ⊆ U)

variables {B : set (open_set X)} {U U₁ U₂ : open_set X}

instance : category (under_set B U) := by unfold under_set; apply_instance

variables (B) (U)

def under_set.map (ι : U₁ ⟶ U₂) : under_set B U₂ ⥤ under_set B U₁ :=
{ obj  := λ U, ⟨U.1, set.subset.trans U.2 ι.1.1⟩,
  map' := λ U U' f, f }

def under_set.embedding : under_set B U ⥤ B := full_subcategory_embedding (under_set B U)

end under_set

section extend
variables {X : Top.{v}}
variables {V : Type u} [𝒱 : category.{u v} V] [has_limits.{u v} V]
include 𝒱

variables (B : set (open_set X))
(h : topological_space.is_topological_basis ((λ U : open_set X, U.s) '' B))

def extend (F : presheaf B V) :
presheaf (open_set X) V :=
{ obj  := λ U, limit ((under_set.embedding B U) ⋙ F),
  map' := λ U₁ U₂ ι,
    limit.lift ((under_set.embedding B U₂) ⋙ F)
    { X := limit ((under_set.embedding B U₁) ⋙ F),
      π := λ U, limit.π _ ⟨U.1, set.subset.trans U.2 ι.1.1⟩ ≫ (𝟙 _)
       } }

end extend
```

#### [Johan Commelin (Oct 10 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135537756):
Goal is:
```lean
tactic failed, there are unsolved goals
state:
X : Top,
V : Type u,
𝒱 : category V,
_inst_1 : has_limits V,
B : set (open_set X),
F : presheaf {x // x ∈ B} V,
U₁ U₂ : open_set X,
ι : U₁ ≤ U₂,
j_val_val : open_set X,
j_val_property : j_val_val ∈ B,
j_property : ⟨j_val_val, j_val_property⟩ ∈ under_set B U₂,
j'_val_val : open_set X,
j'_val_property : j'_val_val ∈ B,
j'_property : ⟨j'_val_val, j'_val_property⟩ ∈ under_set B U₂,
f : j_val_val ≤ j'_val_val
⊢ limit.π (under_set.embedding B U₁ ⋙ F) ⟨⟨j_val_val, j_val_property⟩, _⟩ ≫
      functor.map F (functor.map (under_set.embedding B U₂) {down := {down := f}}) =
    limit.π (under_set.embedding B U₁ ⋙ F) ⟨⟨j'_val_val, j'_val_property⟩, _⟩
```

#### [Johan Commelin (Oct 10 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135542499):
Here is a version where the auto_param gets the job done:
```lean
def extend (F : presheaf B V) : presheaf (open_set X) V :=
{ obj  := λ U, limit ((under_set.embedding B U) ⋙ F),
  map' := λ U₁ U₂ ι,
    begin
      rw show limit (under_set.embedding B U₂ ⋙ F) = limit (under_set.map B ι ⋙ under_set.embedding B U₁ ⋙ F),
      by congr,
      exact limit.pre ((under_set.embedding B U₁) ⋙ F) (under_set.map B ι),
    end }
```

#### [Johan Commelin (Oct 10 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135542532):
I still don't like the `rw show`, but I don't know how to get rid of it.

#### [Patrick Massot (Oct 10 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135542709):
Don't we have a gentleman agreement that any use of Scott's category theory must begin with a local notation reintroducing the proper composition symbol everywhere?

#### [Johan Commelin (Oct 10 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135543280):
:lol: I didn't think about it. Sorry...

#### [Johan Commelin (Oct 10 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135546628):
And we now have:
```lean
def Γ {C : Type w₁} [category.{w₁ w₂} C] (U : C) (F : presheaf C V) : V := F.obj U

lemma extend_val {F : presheaf B V} (U : open_set X) : Γ U (extend F) = limit ((under_set.embedding B U) ⋙ F) := rfl

lemma extend_val_basic_open {F : presheaf B V} (U : B) : Γ U.1 (extend F) ≅ Γ U F :=
by rw extend_val; exact
{ hom := limit.π (under_set.embedding B (U.val) ⋙ F) ⟨U, set.subset.refl _⟩,
  inv := limit.lift (under_set.embedding B (U.val) ⋙ F)
  { X := Γ U F,
    π := λ U', F.map (ulift.up (plift.up U'.2)) } }
```

#### [Johan Commelin (Oct 10 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135546669):
That latter thing is really slow )-; But I don't see how to speed it up.

#### [Patrick Massot (Oct 10 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135546721):
Lots of proofs are provided in the background

#### [Johan Commelin (Oct 10 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135546842):
```quote
elaboration: tactic execution took 16.8s
num. allocated objects:  146
num. allocated closures: 146
16762ms   100.0%   tactic.seq
16762ms   100.0%   tactic.step
16762ms   100.0%   tactic.istep._lambda_1
16762ms   100.0%   tactic.istep
16762ms   100.0%   scope_trace
16762ms   100.0%   interaction_monad.monad._lambda_9
16759ms   100.0%   all_goals_core
16759ms   100.0%   tactic.interactive.exact
16759ms   100.0%   _private.3346078393.all_goals_core._main._lambda_2
16759ms   100.0%   tactic.all_goals
16756ms   100.0%   tactic.to_expr
    3ms     0.0%   rw_core
    3ms     0.0%   tactic.exact
    3ms     0.0%   _private.3200700535.rw_goal._lambda_4
    3ms     0.0%   _private.3200700535.rw_goal._lambda_2
    3ms     0.0%   interaction_monad.orelse'
    3ms     0.0%   tactic.rewrite_target
    3ms     0.0%   interactive.loc.apply
    3ms     0.0%   tactic.interactive.propagate_tags
    3ms     0.0%   _interaction._lambda_2
    2ms     0.0%   tactic.rewrite
    2ms     0.0%   tactic.rewrite_core
    1ms     0.0%   tactic.replace_target
    1ms     0.0%   tactic.mk_eq_mpr
```

#### [Johan Commelin (Oct 10 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135558576):
The next step would be to define sheaves on a basis, and show that their extensions are sheaves on the space.

#### [Johan Commelin (Oct 10 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135558620):
I have the vague feeling that maybe we just want a general statement about sites.

#### [Johan Commelin (Oct 10 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135558749):
@**Reid Barton** Do you know if the inclusion of a basis `B` into `open_set X` is some sort of geometric morphism?

#### [Johan Commelin (Oct 10 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135558814):
If so, then I'dd rather just start attacking the general case...

#### [Reid Barton (Oct 10 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559318):
I've never learned these topos theory words

#### [Johan Commelin (Oct 10 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559476):
It seems that the answer might be yes... so now we want topos theory in mathlib :lol:

#### [Johan Commelin (Oct 10 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559723):
@**Reid Barton** Did you ever do things with Kan extensions in your library?

#### [Reid Barton (Oct 10 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559838):
Nope, near the top of my list for post-colimits.

#### [Johan Commelin (Oct 10 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559851):
Ok... cool. How close do you think this is to being mathlib-ready?

#### [Reid Barton (Oct 10 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559913):
Which?

#### [Johan Commelin (Oct 10 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559924):
Kan extensions

#### [Reid Barton (Oct 10 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559937):
Oh, I haven't actually started on them at all yet.

#### [Johan Commelin (Oct 10 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135559940):
If Scott's limit and colimit stuff is in mathlib. Would that be a follow-up PR? Or would you need other stuff before that?

#### [Reid Barton (Oct 10 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560032):
Are you going to need general Kan extensions? Or just extending a functor on C to presheaves on C

#### [Johan Commelin (Oct 10 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560067):
The latter is good enough

#### [Reid Barton (Oct 10 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560069):
I see. We may want adjunctions, too.

#### [Johan Commelin (Oct 10 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560073):
We do

#### [Johan Commelin (Oct 10 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560089):
But I guess that will be the third PR that Scott has on his list (-;

#### [Reid Barton (Oct 10 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560110):
In order to state the characterization of Kan extension as left adjoint to restriction

#### [Reid Barton (Oct 10 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560152):
I guess we can define them without that though

#### [Reid Barton (Oct 10 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560168):
:plane: but should be back online in not too long

#### [Johan Commelin (Oct 10 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135560185):
Good luck!

#### [Patrick Massot (Oct 10 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135561537):
```quote
Nope, near the top of my list for post-colimits.
```
What about formalizing what you told us about reflective subcategory?

#### [Johan Commelin (Oct 10 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135561999):
@**Reid Barton** Hmmm, a topological basis doesn't give a site. You don't have intersections = products. So the generalisation doesn't apply. Too bad.

#### [Reid Barton (Oct 10 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135562984):
Reflective subcategories are in the same bulleted list in my notes. I forget which one is listed first :)

#### [Patrick Massot (Oct 10 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135563212):
Perfectoid spaces vote for reflexive subcategories first

#### [Kevin Buzzard (Oct 10 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135567536):
```quote
Aah `cases`.
```
You needed that for that `option` question yesterday too. It works for any inductive type.

#### [Scott Morrison (Oct 11 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135572559):
Hmm, your profiling output is not very helpful, because everything is hidden behind the `to_expr` that `exact` is calling.

#### [Scott Morrison (Oct 11 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135572563):
Is it possible to make another lemma for the `exact`?

#### [Scott Morrison (Oct 11 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135572602):
(Also, this is fabulous.)

#### [Kevin Buzzard (Oct 11 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135572927):
I've been really busy over the last couple of days -- but have you (@**Johan Commelin** ) just extended a presheaf from a basis and then shown that the restriction back to the basis is isomorphic to the original presheaf, in about 10 lines? Heh, I guess you should really have shown that the restriction was isomorphic as a presheaf on the basis to F ;-) But still -- who cares if it's slow, it's a small number of lines and that feels right to a mathematician.

#### [Reid Barton (Oct 11 2018 at 05:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135583396):
@**Johan Commelin** I finally looked at your actual code (too many missing Unicode characters on my phone to be practical) and I think you can use something called `limit.pre` or similar to simplify your `extend` even further.
If you have a diagram `X : J -> C` and a functor `F : I -> J` then you get an induced map `lim_I X -> lim_J (X \o F)` and this map is called `limit.pre`.
If you have a map `a -> b` in `C` then you get a functor `C/a -> C/b` and I think your `extend` is `limit.pre` of this functor.

#### [Johan Commelin (Oct 11 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584496):
@**Reid Barton** I'm sorry, I think you have been looking at old code. The new code already uses `limit.pre`: https://github.com/jcommelin/lean-perfectoid-spaces/blob/huber_tate/src/for_mathlib/presheaves.lean

#### [Johan Commelin (Oct 11 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584509):
It isn't as nice as I wish. I would like to get rid of the ugly `rw, congr, exact`.

#### [Reid Barton (Oct 11 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584558):
Ah, I see. I think maybe I missed the `limit.pre` in there, indeed

#### [Reid Barton (Oct 11 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584570):
I guess `convert` might be slightly better?

#### [Reid Barton (Oct 11 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584573):
change `exact` to `convert` and move it first, then see what happens?

#### [Reid Barton (Oct 11 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584578):
I'm a little confused how `congr` proved something without producing any new goals

#### [Johan Commelin (Oct 11 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584579):
@**Kevin Buzzard** Yes, I did. Isn't it delightful? But proving that the extension of a sheaf is a sheaf will be a lot harder.

#### [Johan Commelin (Oct 11 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584624):
```quote
change `exact` to `convert` and move it first, then see what happens?
```
I think that didn't work: deterministic timeout or something.

#### [Johan Commelin (Oct 11 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584627):
In some sense it was really brittle.

#### [Reid Barton (Oct 11 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584637):
Odd

#### [Johan Commelin (Oct 11 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584645):
That file doens't need anything from the perfectoid project. So if you want to hack on it, you can just copy-paste it.

#### [Johan Commelin (Oct 11 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135584814):
Of course you need Scott's libs

#### [Reid Barton (Oct 11 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135619434):
@**Johan Commelin** I was able to replace the whole `map'` field by
```lean
map' := λ U₁ U₂ ι, limit.pre ((under_set.embedding B U₁) ⋙ F) (under_set.map B ι)
```
Everything is quite slow in the editor, I believe because there are errors in the imports (stuff under `category_theory.limits`)

#### [Johan Commelin (Oct 11 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135629183):
Cool! Thanks a lot. Somehow I think I got deterministic timeouts when I tried that. Maybe it is related to the errors in the imports that you mentioned.

#### [Reid Barton (Oct 11 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135629306):
My understanding is that `lean --make` doesn't write out `.olean` files when the build was unsuccessful, which means if your imports have errors then lean in the editor will be much slower.

#### [Reid Barton (Oct 11 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135629362):
It looks like the errors are rather trivial in this case (some tactics failed because there were no goals remaining) but I didn't try to just fix them because they are in lean-category-theory

#### [Johan Commelin (Oct 12 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135659126):
Ok, now it worked for me as well.

#### [Johan Commelin (Oct 15 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135813243):
I think the following is pretty ugly:
```lean
variables {B : set (open_set X)}
variables (h : topological_space.is_topological_basis ((λ U : open_set X, U.s) '' B))
```
Does this mean that I should define `is_basis` for `B` directly? It feels like duplicating a lot of stuff. Is this the curse of bundling?

#### [Mario Carneiro (Oct 15 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135813787):
I don't understand what you are trying to do

#### [Johan Commelin (Oct 15 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135813797):
I'm trying to say that a collection of open sets is a basis. But the open sets are bundled.

#### [Mario Carneiro (Oct 15 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135813997):
I guess you can write `open_set.s` instead of the lambda

#### [Johan Commelin (Oct 15 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814020):
Ok, and would that be the *morally correct* way? Or should I "develop the theory of a basis of bundled open sets"?

#### [Mario Carneiro (Oct 15 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814069):
I'm not sure if you want the forward image or preimage yet, but I think this is what you want

#### [Johan Commelin (Oct 15 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814235):
Well, you could redefine `is_basis` for a set of opens, right? Something like
```lean
\forall U : open_set X, x : X, x ∈ U → ∃ U' ∈ B, x ∈ U' ∧ U' ⊆ U
```

#### [Mario Carneiro (Oct 15 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814375):
I would define `open_set.is_basis` using the image formulation, and then prove that version as a theorem

#### [Johan Commelin (Oct 15 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814380):
Ok, thanks.

#### [Mario Carneiro (Oct 15 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814394):
also that's not the right condition

#### [Mario Carneiro (Oct 15 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814398):
the exists is satisfied by `U`

#### [Johan Commelin (Oct 15 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814450):
No, `U` is not `∈ B`. (In general.)

#### [Mario Carneiro (Oct 15 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814452):
oh... but what about intersections?

#### [Johan Commelin (Oct 15 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814458):
What's with them?

#### [Mario Carneiro (Oct 15 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814475):
a basis should be closed under intersection (ish)

#### [Johan Commelin (Oct 15 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814486):
Oooo... maybe. I'll see when I start proving things (-;

#### [Mario Carneiro (Oct 15 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814491):
This just says B covers the space

#### [Johan Commelin (Oct 15 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814542):
It says that `B` covers every open.

#### [Mario Carneiro (Oct 15 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814567):
oh, actually I think you have the intersection property then

#### [Mario Carneiro (Oct 15 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814672):
if $$U, V \in B$$ and $$x \in U \cap V$$, then $$U\cap V$$ is open so you can find $$x\in W\in B$$ with $$W\subseteq U\cap V$$

#### [Johan Commelin (Oct 15 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135814712):
That looks good, right?

#### [Mario Carneiro (Oct 15 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135815120):
yeah

#### [Mario Carneiro (Oct 15 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135815128):
actually now I recall Kevin saying that this was the obvious definition and he was confused by mathlib's

#### [Johan Commelin (Oct 15 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135826125):
@**Mario Carneiro** Proving that the two definitions are equivalent is a major headache. I feel like we are missing an induction principle for generated topologies. But maybe it is *me* who is missing it.

#### [Johan Commelin (Oct 15 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135826813):
```lean
-- set.lean
@[reducible]
def sUnion (s : set (set α)) : set α := {t | ∃ a ∈ s, t ∈ a}
prefix `⋃₀`:110 := sUnion
```
Does this mean that we can't use `⋃₀` to take the union of `Us : set (open_set X)`? Or can/should I overload notation?

#### [Johan Commelin (Oct 15 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135827571):
I would expect that this notation is meaningful for every type that has a union-operator.

#### [Kenny Lau (Oct 15 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135828259):
try it wthout 0?

#### [Johan Commelin (Oct 15 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135828350):
That gives a weird error: `invalid expression starting at 27:51`

#### [Johan Commelin (Oct 15 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135828554):
@**Kenny Lau** How is this supposed to work? I tried
```lean
lemma is_basis_iff₁ {B : set (open_set X)} :
is_basis B ↔ ∀ {U : open_set X}, ∃ Us ⊆ set B, U = ⋃ U' ∈ Us, U' := sorry
```
Clearly this is not what Lean wants to see...

#### [Kenny Lau (Oct 15 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135828610):
you need : not \in

#### [Kenny Lau (Oct 15 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135828619):
and it’s called bUnion

#### [Johan Commelin (Oct 15 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135828914):
Right, so for this we need a lattice structure on `open_set`. Which we will need at some point anyway.

#### [Johan Commelin (Oct 15 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135837316):
@**Scott Morrison|110087** I know you are busy. Just posting this in case you have a couple of minutes where you are bored :stuck_out_tongue_wink: 
```lean
import category_theory.examples.topological_spaces
import order.lattice
import category_theory.tactics.obviously

universes u v

open category_theory
open category_theory.examples

namespace open_set
open topological_space lattice

variables {X : Top.{v}}

local attribute [back] topological_space.is_open_inter
local attribute [back] is_open_union
local attribute [back] open_set.is_open

instance : has_inter (open_set X) := 
{ inter := λ U V, ⟨ U.s ∩ V.s, by obviously ⟩ }

instance : has_union (open_set X) := 
{ union := λ U V, ⟨ U.s ∪ V.s, by obviously ⟩ }

instance : lattice (open_set X) :=
by refine {
  sup := open_set.has_union.union,
  inf := open_set.has_inter.inter,
  le_antisymm := λ U₁ U₂ _ _, by cases U₁; cases U₂; tidy,
  le_sup_left := begin intros U₁ U₂, cases U₁; cases U₂, tidy, end,
  le_sup_right := sorry,
  sup_le := sorry,
  inf_le_left := sorry,
  inf_le_right := sorry,
  le_inf := sorry,
  ..open_set.preorder }; tidy
```
What incantations do I need to get `tidy` up to speed?

#### [Johannes Hölzl (Oct 15 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135837545):
I guess you need the rules how `union` and `intersection` behave under `subset`, like `set.subset_union_left`. So try add this as `back`.

#### [Mario Carneiro (Oct 15 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135839090):
hey @**Kenny Lau**, I see a galois insertion...

#### [Reid Barton (Oct 15 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135839344):
Do we have an emoji for galois insertion

#### [Johan Commelin (Oct 15 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135839838):
Thanks, I'll try that tomorrow.

#### [Kevin Buzzard (Oct 15 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135842162):
```quote
Do we have an emoji for galois insertion
```
So we need to choose one, right? People should vote on Reid's question.

#### [Johan Commelin (Oct 16 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881584):
@**Scott Morrison|110087** I implemented Johannes suggestion. Now I have the following bunch of code:
```lean
import category_theory.examples.topological_spaces
import order.lattice
import category_theory.tactics.obviously

universes u v

open category_theory
open category_theory.examples

namespace open_set
open topological_space lattice

variables {X : Top.{v}}

local attribute [back] topological_space.is_open_inter
local attribute [back] is_open_union
local attribute [back] open_set.is_open

local attribute [back] set.subset_union_left
local attribute [back] set.subset_union_right

instance : has_inter (open_set X) :=
{ inter := λ U V, ⟨ U.s ∩ V.s, by obviously ⟩ }

instance : has_union (open_set X) :=
{ union := λ U V, ⟨ U.s ∪ V.s, by obviously ⟩ }

#print prefix open_set.has_union

local attribute [simp] open_set.has_union.equations._eqn_1

instance : lattice (open_set X) :=
by refine {
  sup := open_set.has_union.union,
  inf := open_set.has_inter.inter,
  le_antisymm := λ U₁ U₂ _ _, by cases U₁; cases U₂; tidy,
  le_sup_left := begin tidy, end,
  le_sup_right := begin intros U₁ U₂, cases U₁; cases U₂, tidy, end,
  sup_le := sorry,
  inf_le_left := sorry,
  inf_le_right := sorry,
  le_inf := sorry,
  ..open_set.preorder }; tidy
```

#### [Johan Commelin (Oct 16 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881631):
The `tidy` in the proof of `le_sup_left` leaves me with the following goal:
```lean
X : Top,
a b : open_set X,
a_1 : X.α,
a_2 : a_1 ∈ a.s
⊢ a_1 ∈ a.s ∨ a_1 ∈ b.s
```

#### [Johan Commelin (Oct 16 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881644):
Ooh wait! Does this mean that I have to mark `or.inl` with `[back!]` or something like that?

#### [Kevin Buzzard (Oct 16 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881646):
Does `@[simp] instance : has_union (open_set X)` do the same as `attribute [simp] open_set.has_union.equations._eqn_1`?

#### [Mario Carneiro (Oct 16 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881700):
or.inl is not a good `back!` lemma

#### [Johan Commelin (Oct 16 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881711):
Hmmm, why not?

#### [Mario Carneiro (Oct 16 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881757):
because it will try to prove everything by the left disjunct

#### [Johan Commelin (Oct 16 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881760):
Only if the assumptions are satisfied, right?

#### [Mario Carneiro (Oct 16 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881761):
not with the `!`

#### [Mario Carneiro (Oct 16 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881768):
I think `simp` should work

#### [Mario Carneiro (Oct 16 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881773):
because it will turn the goal into `true \/ ...` and then `true`

#### [Johan Commelin (Oct 16 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881774):
Well, it doesn't. Because `tidy` would try that.

#### [Mario Carneiro (Oct 16 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881775):
did you see if `simp * at *` works by hand?

#### [Mario Carneiro (Oct 16 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881777):
what about `simp *`?

#### [Johan Commelin (Oct 16 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881838):
Ok, that works. Is that a bug in `tidy`?

#### [Mario Carneiro (Oct 16 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881911):
or a bug in `simp * at *`

#### [Mario Carneiro (Oct 16 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881952):
wait, which is "that"

#### [Kevin Buzzard (Oct 16 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881966):
I have a very unclear idea about what all these things like `tidy` and `obviously` and `backwards_reasoning` do. It seems to me that they "all do the same thing" -- they just "try a bunch of stuff like simp and split and stuff". Does `tidy` have a sufficiently formal specification that one can ask if there is a "bug" in it? Do you actually mean "let's make `tidy` try more stuff"?

#### [Mario Carneiro (Oct 16 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135881994):
`back` has a "spec", but you are right about the others

#### [Mario Carneiro (Oct 16 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882015):
`obviously` is `tidy` + `rewrite_search`

#### [Mario Carneiro (Oct 16 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882019):
which is that graph thing that Keeley Hoek did

#### [Johan Commelin (Oct 16 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882029):
`simp *` worked. I would imagine that `tidy` should try that as well. Of course it is not a bug in the strict sense; but I meant a "bug" in the sense that it would be a nice feature to add to `tidy`.

#### [Mario Carneiro (Oct 16 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882030):
`tidy` is just a kitchen sink tactic right now, although I understand it is loosely based on the Gowers-Ganesalingam prover

#### [Johan Commelin (Oct 16 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882245):
I'm struggling with finding  a statement that type checks. I just proved that `open_set X` has a lattice structure. Now I want to take a union of a bunch of opens. What should I tell Lean to make sense of this?
```lean
lemma is_basis_iff₁ {B : set (open_set X)} :
is_basis B ↔ ∀ {U : open_set X}, ∃ Us ⊆ set B, U = ⋃ U' : Us, U' := sorry
```

#### [Johan Commelin (Oct 16 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882253):
Currently it doesn't like the `⋃` symbol.

#### [Mario Carneiro (Oct 16 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882319):
use the sup symbol

#### [Kevin Buzzard (Oct 16 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882321):
Isn't there `union` and `Union` and `bUnion` and `sUnion` or something? Usage depends on whether you're taking a union of two things, or a set of things, or a type of things etc. One of them is that big union symbol -- aren't there other notations too though? I can never remember which is which here.

#### [Mario Carneiro (Oct 16 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882324):
most of the union/inter notation is specific to `set`

#### [Mario Carneiro (Oct 16 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882364):
the generic version is `Sup` and `Inf`

#### [Johan Commelin (Oct 16 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882367):
Ok, I see. So for everything else we want to use lattice notation?

#### [Mario Carneiro (Oct 16 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882369):
yes

#### [Johan Commelin (Oct 16 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882385):
And turning something into a lattice doesn't automatically give you a `has_Sup`. Is that on purpose?
I don't know anything about lattices.

#### [Mario Carneiro (Oct 16 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882386):
> ` ∃ Us ⊆ set B, `

what should this mean?

#### [Mario Carneiro (Oct 16 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882393):
a complete lattice, not a lattice

#### [Johan Commelin (Oct 16 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882394):
That there is a bunch of basic opens such that...

#### [Mario Carneiro (Oct 16 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882398):
lattice just gives you binary sup

#### [Johan Commelin (Oct 16 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882399):
Ok, so I should prove that `open_set` is a complete lattice.

#### [Mario Carneiro (Oct 16 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882437):
yes

#### [Mario Carneiro (Oct 16 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882443):
again, galois insertion should make it easy

#### [Johan Commelin (Oct 16 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882525):
I propose :return: for galois connections and adjunctions. I don't understand the :basketball: symbol. Maybe it's because I'm Dutch :lol:

#### [Johan Commelin (Oct 16 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882544):
Ok, I have no idea what boilerplate I should write for that Galois insertion. What is the best way to find this out?

#### [Mario Carneiro (Oct 16 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882677):
you need a pair of functions with a galois connection, from the complete lattice to the type you want a complete lattice structure on, and one round trip should be the identity

#### [Kevin Buzzard (Oct 16 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882881):
The basketball was the only emoji I found which looked like anything being inserted into anything, that's all

#### [Kevin Buzzard (Oct 16 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882927):
I didn't even look for an emoji of something being connected to something

#### [Johan Commelin (Oct 16 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882938):
Ok, so one of the maps is `open_set.s` and the other is ?? the interior? Or the smallest open containing some set `S`?

#### [Mario Carneiro (Oct 16 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882948):
interior, certainly

#### [Johan Commelin (Oct 16 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135882949):
Brainfart, that doesn't even make sense. So it should be the interior.

#### [Mario Carneiro (Oct 16 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135883011):
actually I'm a bit worried you will end up the wrong way around, i.e. you will get the `u` function being injective instead of the `l` function

#### [Mario Carneiro (Oct 16 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135883021):
@**Johannes Hölzl** How do you want to do galois coinsertions?

#### [Johan Commelin (Oct 16 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135883518):
Ok, so `l = interior` and `u = open_set.s`. Is this good or bad news for our complete_lattice?

#### [Mario Carneiro (Oct 16 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135883614):
try to prove galois insertion?

#### [Johan Commelin (Oct 16 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135883814):
Oops, I switched `l` and `u`. I still find those names confusing... Ok, so it is going to be a `coinsertion`.

#### [Johan Commelin (Oct 16 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884099):
@**Mario Carneiro** Is the Galois connection enough to get the complete lattice structure? Or do I need to work out `galois_coinsertion` first? I really don't know the maths here.

#### [Mario Carneiro (Oct 16 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884124):
the insertion is important

#### [Mario Carneiro (Oct 16 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884128):
it is basically making an order embedding

#### [Mario Carneiro (Oct 16 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884134):
and you pull the relation back along that

#### [Johan Commelin (Oct 16 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884143):
You mean coinsertion?

#### [Mario Carneiro (Oct 16 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884151):
that too

#### [Johan Commelin (Oct 16 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884171):
Hmmm, I will try to dualize all the stuff about `insertion`s.

#### [Mario Carneiro (Oct 16 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884173):
it should work just as well, it will just pull a lattice from left to right instead of right to left

#### [Mario Carneiro (Oct 16 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884175):
or vice versa

#### [Mario Carneiro (Oct 16 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884179):
you know, just put co everywhere

#### [Johannes Hölzl (Oct 16 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884238):
look into how it is done for `filter`. Here I use `dual_order` to get the other way round

#### [Mario Carneiro (Oct 16 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884245):
I was just about to suggest that

#### [Johannes Hölzl (Oct 16 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884258):
```lean
def gi_generate (α : Type*) :
@galois_insertion (set (set α)) (order_dual (filter α)) _ _ filter.generate filter.sets
```

#### [Mario Carneiro (Oct 16 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884260):
but filter is dualized on only one side

#### [Mario Carneiro (Oct 16 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884275):
I guess a coinsertion is dualized on both sides

#### [Johannes Hölzl (Oct 16 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884308):
is it enough to add `order_dual` on both sides?

#### [Mario Carneiro (Oct 16 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884341):
I wonder whether we want a separate definition though since otherwise the names will be even more confusing than they already are

#### [Mario Carneiro (Oct 16 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884361):
plus `galois_coinsertion` should extend `galois_connection` with no duals

#### [Mario Carneiro (Oct 16 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884413):
do we know that `galois_connection` is self-dual?

#### [Johannes Hölzl (Oct 16 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884424):
to its symmetric form:
```lean
protected lemma dual [pα : preorder α] [pβ : preorder β]
  (l : α → β) (u : β → α) (gc : galois_connection l u) :
  @galois_connection (order_dual β) (order_dual α) _ _ u l :=
assume a b, (gc _ _).symm
```

#### [Johannes Hölzl (Oct 16 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884427):
in https://github.com/leanprover/mathlib/blob/master/order/galois_connection.lean#L160

#### [Kevin Buzzard (Oct 16 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884663):
then it should just be called `galois_nnection`

#### [Kevin Buzzard (Oct 16 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884719):
it's shorter

#### [Johan Commelin (Oct 16 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884777):
Aaahrg, all those design decisions. Is there a choice procedure for such design decisions?
I think we should make the same choice as for the `limit` vs `colimit` story in category theory.

#### [Johan Commelin (Oct 16 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884833):
So we just copy-paste all the code and dualize it. Right?

#### [Kevin Buzzard (Oct 16 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884837):
[or write a tactic which generates the code for you...]

#### [Johannes Hölzl (Oct 16 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135884873):
usually you copy all statements from the Galois insertion anyway. I don't see a problem to use a Galois insertion and `dual_order` twice. You only want to use it to get the complete lattice, afterwards you don't care anymore.

#### [Johan Commelin (Oct 16 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135887809):
Ok, now I've got
```lean
def interior (s : set X) : open_set X :=
{ s := interior s,
  is_open := is_open_interior }

def gc : galois_connection (@open_set.s X) interior :=
λ U s, ⟨λ h, interior_maximal h U.is_open, λ h, le_trans h interior_subset⟩

def gco : galois_coinsertion (@open_set.s X) interior :=
{ choice := λ s _, interior s,
  gc := gc,
  u_l_le := λ _, interior_subset,
  choice_eq := λ _ _, rfl }

instance : partial_order (open_set X) :=
{ le_antisymm := λ U₁ U₂ _ _, by cases U₁; cases U₂; tidy,
   .. open_set.preorder }

instance : complete_lattice (open_set X) := galois_coinsertion.lift_complete_lattice gco

def univ : open_set X :=
{ s := set.univ,
  is_open := is_open_univ }
```
I guess that this definition of `univ` is not correct? Should it be a theorem about `⊤` somehow?

#### [Johan Commelin (Oct 16 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135894415):
@**Johannes Hölzl** Those `order_dual`s are completely blowing up my brain. Does this look good or am I missing something?
```lean
def interior (s : set X) : open_set X :=
{ s := interior s,
  is_open := is_open_interior }

def gc : galois_connection (@open_set.s X) interior :=
λ U s, ⟨λ h, interior_maximal h U.is_open, λ h, le_trans h interior_subset⟩

def gi : @galois_insertion (order_dual _) (order_dual _) _ _ interior (@open_set.s X) :=
{ choice := λ s _, interior s,
  gc := galois_connection.dual _ _ gc,
  le_l_u := λ _, interior_subset,
  choice_eq := λ _ _, rfl }

instance : partial_order (open_set X) :=
{ le_antisymm := λ U₁ U₂ _ _, by cases U₁; cases U₂; tidy,
   .. open_set.preorder }

instance : complete_lattice (open_set X) :=
@galois_insertion.lift_complete_lattice (order_dual _) (order_dual _) _ interior (@open_set.s X) _ gi
```

#### [Johannes Hölzl (Oct 16 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135894662):
looks good to me. Is there something wrong?

#### [Johan Commelin (Oct 16 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135894967):
Yes, I'm getting the dual order.

#### [Johan Commelin (Oct 16 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135894982):
So now I need a function that takes an order, and flips it around.

#### [Johan Commelin (Oct 16 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895221):
@**Johannes Hölzl** Is there a way to unfold something only once?

#### [Johannes Hölzl (Oct 16 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895354):
hm, `rw [h] {occs := occurrences.pos [1]}` is the only thing I know

#### [Johannes Hölzl (Oct 16 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895452):
for the dual, lets take a look at filters again:
```lean
private def original_complete_lattice : complete_lattice (filter α) :=
@order_dual.lattice.complete_lattice _ (gi_generate α).lift_complete_lattice
```

#### [Johan Commelin (Oct 16 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895460):
I hacked around it like this:
```lean
instance open_set.lattice.complete_lattice.order_dual : complete_lattice (order_dual (open_set X)) :=
@galois_insertion.lift_complete_lattice (order_dual _) (order_dual _) _ interior (@open_set.s X) _ gi

lemma order_dual_order_dual {α : Type*} : order_dual (order_dual α) = α := rfl

instance : complete_lattice (open_set X) :=
begin
  have foo : complete_lattice (order_dual (order_dual (open_set X))),
  by apply_instance,
  rw order_dual_order_dual at foo,
  exact foo
end
```
@**Johannes Hölzl** I am not so sure that the coinsertions are useless. This is causing me quite some pain...

#### [Johannes Hölzl (Oct 16 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895503):
`order_dual.lattice.complete_lattice` does what you want

#### [Johannes Hölzl (Oct 16 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895514):
and it doesn't have the `rw` problem

#### [Johan Commelin (Oct 16 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895594):
@**Johannes Hölzl** I don't see how to apply it. It can only put orders on `order_dual _`, it can't go the other way.

#### [Johannes Hölzl (Oct 16 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895688):
you are sure it doesn't work? `preorder (order_dual (order_dual A)) = preorder A` should be (in your case) by definition

#### [Johannes Hölzl (Oct 16 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135895698):
can you put your theory on a gist?

#### [Johan Commelin (Oct 16 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896091):
@**Johannes Hölzl** Voila: https://gist.github.com/jcommelin/c9d04b7770f89a0fadc11aae5ca90d87
This is what I have so far.

#### [Johannes Hölzl (Oct 16 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896557):
```lean
instance : partial_order (open_set X) :=
{ le_antisymm := λ U₁ U₂ _ _, by cases U₁; cases U₂; tidy,
   .. open_set.preorder }

instance : complete_lattice (open_set X) :=
@order_dual.lattice.complete_lattice _
  (@galois_insertion.lift_complete_lattice (order_dual _) (order_dual _) _ interior (@open_set.s X) _ gi)
```
now you have the dual

#### [Johannes Hölzl (Oct 16 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896558):
is this what you want?

#### [Johan Commelin (Oct 16 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896566):
I think it is. Let me try.

#### [Johan Commelin (Oct 16 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896627):
But this still isn't proved by `rfl`:
```lean
@[simp] lemma Lub_s {Us : set (open_set X)} : (⨆ U ∈ Us, U).s = ⋃₀ (open_set.s '' Us) :=
```
And I think that with coinsertions it could have been `rfl`, right?

#### [Johannes Hölzl (Oct 16 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896694):
only if you setup `choice` correctly

#### [Johannes Hölzl (Oct 16 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896728):
and this is also with insertion a `rfl`

#### [Johannes Hölzl (Oct 16 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896788):
so, no `coinsertion` doesn't give you a rfl by default. It will only be a `rfl` when you use the proof in `choice` to construct `rfl` data. And since `insertion` and `coinsertion` are just dual, it works also with insertion.

#### [Johannes Hölzl (Oct 16 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896817):
So what you need to do:
```lean
def gi : @galois_insertion (order_dual (set X)) (order_dual (open_set X)) _ _ interior (@open_set.s X) :=
{ choice := λ s _, interior s,
  gc := galois_connection.dual _ _ gc,
  le_l_u := λ U, interior_subset,
  choice_eq := λ _ _, rfl }
```
Instead of `choice := λ s _, interior s,` you need to write something like:
`choice := λ s _, (s, proof that s is open),`

#### [Johan Commelin (Oct 16 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896890):
Huuh, but `s` isn't open.

#### [Johannes Hölzl (Oct 16 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896917):
yes it is, the `_` is actually a proof from which you can show that it is open

#### [Johannes Hölzl (Oct 16 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896964):
it says: `interior s = s`

#### [Johannes Hölzl (Oct 16 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135896994):
then you also need to adapt your `choice_eq` proof accordingly

#### [Johan Commelin (Oct 16 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135897076):
Ok, I see. I'll try to do this.

#### [Johan Commelin (Oct 16 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135897497):
@**Johannes Hölzl** Sorry, but the following still doesn't work:
```lean
have foo : (Sup Us).s = Sup (open_set.s '' Us) := rfl
```

#### [Johannes Hölzl (Oct 16 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135898099):
you should get:
```lean
have foo : (Sup Us).s = (⨆a∈Us, a.s) := rfl
```

#### [Johan Commelin (Oct 16 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135898427):
@**Johannes Hölzl** That gives me
```lean
invalid field notation, type is not of the form (C ...) where C is a constant
  a
has type
  ?m_1
```
I now have the following ugly proof myself:
```lean
@[simp] lemma Sup_s {Us : set (open_set X)} : (Sup Us).s = ⋃₀ (open_set.s '' Us) :=
by rw [@galois_connection.l_Sup _ _ _ _ (@open_set.s X) interior (gc) Us, set.sUnion_image]
```

#### [Johannes Hölzl (Oct 16 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135898448):
what about `have foo : (Sup Us).s = (⨆a∈Us, open_set.s a) := rfl`

#### [Johan Commelin (Oct 16 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135898745):
Still fails:
```lean
invalid type ascription, term has type
  ?m_2 = ?m_2
but is expected to have type
  (Sup Us).s = ⨆ (a : open_set X) (H : a ∈ Us), a.s
```

#### [Johannes Hölzl (Oct 16 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135898976):
how does your `gi` look like?

#### [Johan Commelin (Oct 16 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135899032):
```lean
def gi : @galois_insertion (order_dual (set X)) (order_dual (open_set X)) _ _ interior (@open_set.s X) :=
{ choice := λ s hs, { s := s, is_open := interior_eq_iff_open.mp $ le_antisymm interior_subset hs },
  gc := galois_connection.dual _ _ gc,
  le_l_u := λ _, interior_subset,
  choice_eq := λ s hs, le_antisymm interior_subset hs }
```

#### [Johannes Hölzl (Oct 16 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135900200):
hm
```lean
set_option pp.all true
#print open_set.lattice.complete_lattice
```
somewhere `set` gets unfolded and the `pi` instance is used. Then we get different `Sup` and `Inf`.

#### [Reid Barton (Oct 16 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135900203):
Kudos to the individual who came up with :gun: for Galois insertion btw

#### [Johan Commelin (Oct 16 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135900316):
@**Johannes Hölzl** Hmmm... I think I'm giving up on debugging this. It is too annoying. If you feel like debugging it, I haven't made much progress since my gist.

#### [Johannes Hölzl (Oct 16 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135900464):
```lean
instance : complete_lattice (open_set X) :=
@order_dual.lattice.complete_lattice _
  (@galois_insertion.lift_complete_lattice
    (order_dual (set X)) (order_dual (open_set X)) _ interior (@open_set.s X) _ gi)

lemma Sup_s {Us : set (open_set X)} : (Sup Us).s = ⨆s∈Us, open_set.s s :=
rfl
```
this works

#### [Johannes Hölzl (Oct 16 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135900784):
`(order_dual (set _))` is already enough. Then the elaborator finds the right instance, instead of the instance for `X -> Prop`

#### [Johan Commelin (Oct 16 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135900908):
Ok, so my instance is wrong... hmmzzz. Thanks for finding this bug!

#### [Alex J. Best (Oct 16 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135907294):
@**Reid Barton**  Thanks, after trying to teach myself some lean on the side and lurking here a lot without doing anything I'm glad someone found my first "contribution" as funny as I did

#### [David Michael Roberts (Oct 17 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/extend%20presheaf%20from%20basis/near/135958522):
```quote
then it should just be called `galois_nnection`
```
or a cogalois-nnection (sorry)

