---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/28653dontknowhowto.html
---

## [new members](index.html)
### [don't know how to](28653dontknowhowto.html)

#### [Etienne Laurin (Aug 04 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/130864937):
Hi! I'm a C++ developer in Dublin. I'm trying to learn Lean by doing some exercises.
```lean
variables {T : Type} {A B : T → Prop}
lemma t₁ : (∃ x, A x) → ∃ x, (A x ∨ B x) := λ ⟨x, p⟩, ⟨x, or.inl p⟩
lemma t₂ : (∃ x, A x) ∨ (∃ x, B x) → ∃ x, (A x ∨ B x) :=
    λ h, h.cases_on (λ ⟨x, p⟩, ⟨x, or.inl p⟩) (λ ⟨x, p⟩, ⟨x, or.inr p⟩)
```
t₁ works but t₂ fails with "don't know how to synthesize placeholder". How can I get Lean to tell me what/where this placeholder is? Is there something better than or.cases_on that I could be using?

#### [Mario Carneiro (Aug 04 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/130865206):
There is a known issue with using projection notation in conjunction with `@[elab_as_eliminator]` definitions like `or.cases_on`. You can fix the proof by either not using projection notation, i.e. `or.cases_on h` instead of `h.cases_on`, or by using `h.elim` instead (which is basically the same as `or.cases_on` without the weird elaborator marking)

#### [Etienne Laurin (Aug 04 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/130865584):
Thanks!

#### [Kevin Buzzard (Aug 04 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/130865651):
How can you tell `or.cases_on` is tagged `@[elab_as_eliminator]`? `#print or.cases_on` only tells me it's `@[reducible]`

#### [Mario Carneiro (Aug 04 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/130865788):
Hm, that's interesting. `T.rec`, `T.rec_on`, and `T.cases_on` are automatically generated for every inductive type and are always treated as if they have `elab_as_eliminator` enabled, although you are right that there is no explicit indication of such. You can test it by making a copy of `or.cases_on` with exactly the definition `#print` says, and the lemma will typecheck; then if you add `elab_as_eliminator` you get exactly the same errors

#### [Kevin Buzzard (Aug 04 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/130865850):
`example : @or.cases_on = @or.elim := rfl`, and they're both there, so they must be different somehow ;-) It's how the elaborator elaborates them.

#### [Mario Carneiro (Aug 04 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/130865947):
you should be aware that that's not the best way to check that two definitions are the same according to lean, that is only up to defeq which ignores annotations and bindings, as well as unifying universes

#### [Mario Carneiro (Aug 04 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/130866021):
Also, strange as it may sound I'm pretty sure there are duplicate definitions (completely identical) in lean. Often this has to do with renaming

#### [Edward Ayers (Aug 08 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131118119):
I got this to work with 
`λ h, or.cases_on h (λ ⟨x, p⟩, ⟨x, or.inl p⟩) (λ ⟨x, p⟩, ⟨x, or.inr p⟩)`

#### [Edward Ayers (Aug 08 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131118228):
Can someone explain what the "synthesize placeholder" error actually means? It is by far the most common error I get and I currently get rid of it by making random transformations to the source until it goes away

#### [Mario Carneiro (Aug 08 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131118304):
it means the proof is unfinished

#### [Edward Ayers (Aug 08 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131118316):
proof that the term typechecks?

#### [Mario Carneiro (Aug 08 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131118320):
lean is saying "there is a missing part of the proof and I don't know how to fill it in"

#### [Mario Carneiro (Aug 08 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131118344):
No, the term itself is the proof

#### [Edward Ayers (Aug 08 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131118347):
I often get it where the goal that it is trying to prove is `Type ?`. What should I do then?

#### [Mario Carneiro (Aug 08 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131118365):
That means there is a missing type somewhere

#### [Mario Carneiro (Aug 08 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131118414):
for example, looking at the term you just gave without any other context, I can't figure out the type of `h`

#### [Mario Carneiro (Aug 08 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131118422):
I know it is an `or` of something but I don't know what

#### [Mario Carneiro (Aug 08 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131118427):
so if I were lean I would say "couldn't synth placeholder `|- Type ?`"

#### [Edward Ayers (Aug 08 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119049):
Ok let me paste some code where I can't figure out what it wants
I put this file in `mathlib/category_theory/scratch.lean`
```
import .category
import .functor
universes u1 u2 v1 v2

namespace category_theory
    section 
        variables 
            {C : Type u1} [𝒞 : category.{u1 v1} C] 
            {D : Type u2} [𝒟 : category.{u2 v2} D]
        include 𝒞 𝒟
        def t : Π (a b c : D) (p : a = b) (x : a ⟶ c), b ⟶ c := λ a b c p x, eq.rec x p
        def t2 (F G : C ↝ D) (ob_eq : ∀ (Z : C), F Z = G Z)  (X Y : C) (f : X ⟶ Y) : (G X ⟶ F Y) 
            := t (F X) (G X) (F Y) (ob_eq X) (F.map f)
    end
end category_theory
```
And I get a synth `Type ?` error for `t` in `t2` but I can't figure out which type I am missing

#### [Reid Barton (Aug 08 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119269):
Just looking at this (haven't built recent mathlib yet), I think the problem is that `t` "depends on" `C`, because of `include 𝒞`, but there's nothing in the type of `t` which can ever determine what `C` has to be.

#### [Edward Ayers (Aug 08 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119333):
Ah, so if you are in a section and write `variables`, then all definitions in that section implicitly depend on these variables, even if they are not used in the definition?

#### [Reid Barton (Aug 08 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119335):
And so there's no reason that `t`'s `C` in the use of `t` in `t2`needs to be the same as the `C` in `t2`, so Lean can't figure out how to assign it.

#### [Reid Barton (Aug 08 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119347):
Not in general, but using `include` forces the `variable` to be included as a parameter to every subsequent definition.

#### [Edward Ayers (Aug 08 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119364):
Where can I find some docs on `include`? I find it cryptic

#### [Reid Barton (Aug 08 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119365):
So if you show the full inferred type of `t`, it should begin `t : \Pi {C : Type u1} [𝒞 : category.{u1 v1} C] ...`

#### [Reid Barton (Aug 08 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119421):
`𝒞`was included because of the `include`, and `C` was included because `𝒞` depends on it

#### [Edward Ayers (Aug 08 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119458):
If I comment out `include`, then the `\hom` arrows become errors. How would I get rid of those errors without using `include`?

#### [Edward Ayers (Aug 08 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119525):
It can't find evidence for `category D`.

#### [Reid Barton (Aug 08 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119547):
https://leanprover.github.io/theorem_proving_in_lean/tactics.html mentions `include`/`omit` in the first section. I don't remember whether it is also explained elsewhere in TPIL

#### [Reid Barton (Aug 08 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119558):
In this case, you could put `include 𝒟` between the definitions of `t` and `t2`

#### [Edward Ayers (Aug 08 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119625):
Fixed code:
```lean
import .category
import .functor
universes u1 u2 v1 v2

namespace category_theory
    section 
        variables 
            {C : Type u1} [𝒞 : category.{u1 v1} C] 
            {D : Type u2} [𝒟 : category.{u2 v2} D]
        include 𝒟
        def t : Π (a b c : D) (p : a = b) (x : a ⟶ c), b ⟶ c := λ a b c p x, eq.rec x p
        include 𝒞
        def t2 (F G : C ↝ D) (ob_eq : ∀ (Z : C), F Z = G Z)  (X Y : C) (f : X ⟶ Y) : (G X ⟶ F Y) 
            := t (F X) (G X) (F Y) (ob_eq X) (F.map f)
    end
end category_theory
```

#### [Reid Barton (Aug 08 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119700):
Normally you could just omit the names `𝒞 : ` and `𝒟 : ` and the include statements and Lean would figure out where it needs the instance variables. The fact that that doesn't work here is some combination of there being extra universe parameters involved and a bug in Lean, I think.

#### [Edward Ayers (Aug 08 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119729):
Ok but this then errors for me:
```lean
import .category
import .functor
universes u1 u2 v1 v2

namespace category_theory
    section 
        variables 
            {C : Type u1} [category.{u1 v1} C] 
            {D : Type u2} [category.{u2 v2} D]
        --include 𝒟
        def t : Π (a b c : D) (p : a = b) (x : a ⟶ c), b ⟶ c := λ a b c p x, eq.rec x p
        --include 𝒞
        def t2 (F G : C ↝ D) (ob_eq : ∀ (Z : C), F Z = G Z)  (X Y : C) (f : X ⟶ Y) : (G X ⟶ F Y) 
            := t (F X) (G X) (F Y) (ob_eq X) (F.map f)
    end
end category_theory
```

#### [Edward Ayers (Aug 08 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119748):
`kernel failed to type check declaration 't' this is usually due to a buggy tactic or a bug in the builtin elaborator`

#### [Edward Ayers (Aug 08 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119757):
cool

#### [Edward Ayers (Aug 08 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119821):
which must be why it had `𝒞 : ` in to start with, to avoid the lean bug

#### [Reid Barton (Aug 08 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119827):
Yes. The reason is either that Lean doesn't know what universe parameters to specialize `⟶` to, or that there's a bug where including the instance variable doesn't cause `C` to also get included.  I don't remember the exact details any more.
When you get that "kernel failed to type check declaration" error, it means it failed to include `C`, I think.

#### [Reid Barton (Aug 08 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119926):
Right, the workaround is that when you manually tell it to include the `category` instance, then it can correctly infer that it needs `C` too. The downside is that now you are responsible for making sure the right variables are `include`d--if you have too many then you end up with your original issue.

#### [Edward Ayers (Aug 08 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119929):
thanks so much for your help

#### [Reid Barton (Aug 08 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119952):
In general, this class of error can be tough to figure out. I don't know of a better way than thinking really hard about what Lean is trying to do and figuring out where it might be getting stuck.

#### [Reid Barton (Aug 08 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131119954):
No problem

#### [Edward Ayers (Aug 08 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131120046):
It seems like solving these errors requires intimately knowing what the elaborator is doing.  And from what I know, the elaborator is very elaborate

#### [Patrick Massot (Aug 08 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131120215):
```quote
Normally you could just omit the names `𝒞 : ` and `𝒟 : ` and the include statements and Lean would figure out where it needs the instance variables.
```
I think this is not true. To me it seems Lean will always include these statements. That explains why we sometimes see unneeded or duplicate instance arguments, even in mathlib

#### [Patrick Massot (Aug 08 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131120241):
```quote
It seems like solving these errors requires intimately knowing what the elaborator is doing.  And from what I know, the elaborator is very elaborate
```
Unfortunately and fortunately, this is all very true.

#### [Edward Ayers (Aug 08 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131120395):
It would be great if when there was an elaborator error, a textbox appeared that you could enter the missing type or proof into.

#### [Mario Carneiro (Aug 08 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131120407):
Lean will include an unnamed typeclass variable when all of its dependencies are included (usually because they are mentioned directly in the statement or are dependencies of something mentioned). Like so:
```
variables (A : Type) [group A]
example (x : A) : true := ... -- group A is included
example : true := ... -- group A is not included
```

#### [Patrick Massot (Aug 08 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131120439):
yes, this matches what I saw

#### [Reid Barton (Aug 08 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131120443):
Yes, good point @**Patrick Massot**.

#### [Mario Carneiro (Aug 08 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131120505):
Lean will never include a named typeclass variable unless it is mentioned:
```
variables (A : Type) [G : group A]
example (x : A) : true := ... -- group A is not included
example : x + x = x := ... -- group A is included
```
And an included typeclass variable is always included:
```
variables (A : Type) [G : group A]
include G
example (x : A) : true := ... -- group A is included
example : true := ... -- group A is included
```

#### [Scott Morrison (Aug 09 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/don't know how to/near/131137096):
I will add some documentation about `include` right in the `category_theory` files, specialised to the use case there.

Unfortunately `category C` has an unbound universe level, because we need to know the universe level of the morphisms, and this is not determined by the universe level of `C` itself. (This design decision is constrained by the desire to be able to write uniform code for small categories and large categories.)

When we write `variable [category.{u v} C]`, Lean is reasonably rather hesistant to use this variable, unless it is sure that `v` is the actually intended universe level. To avoid having to explicitly write this universe variable in every definition that you're hoping will make use of this `[category C]` variable, we give it a name as in `[𝒞 :  category.{u v} C]` and explicitly include it in every following declaration, via `include 𝒞`.

This then adds a danger: if you write another declaration that doesn't actually care about this category (e.g. one declaration refers to four different categories, but a subsequent one only mentions two), this typeclass variable will still be included as an argument, mucking everything up. Hence `include 𝒞` statements need to be carefully scoped with `section .... end` commands.

