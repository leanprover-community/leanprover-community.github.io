---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54886functorialitytactic.html
---

## [general](index.html)
### [functoriality tactic](54886functorialitytactic.html)

#### [Reid Barton (Sep 08 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133540754):
I wonder how hard it would be to write a tactic which takes an expression which is supposed to be the object mapping part of a functor, and tries to guess the morphism mapping part.

#### [Reid Barton (Sep 08 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133540817):
If the language for writing the object mapping part is sufficiently restricted, it should be doable, I think. Concretely I'm thinking of stuff like lambdas and applications of known functors and bifunctors

#### [Reid Barton (Sep 08 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133540878):
Something like a little type checker for a "directed type theory" language I guess

#### [Reid Barton (Sep 08 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133540900):
I'm imagining it would work by induction on the structure of the object-mapping expression.
GHC has a built-in feature which is kind of like this, incidentally (`deriving Functor`)

#### [Kevin Buzzard (Sep 08 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133541004):
It's an interesting question, because this tactic must be somehow inbuilt into mathematicians -- for the kinds of categories they talk about (even ones where the objects are filtered vector spaces with a nilpotent endomorphism or whatever) it is often the case that the morphisms in the category are defined when introducing the category but the morphisms are barely ever mentioned when defining functors.

#### [Reid Barton (Sep 08 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133541093):
And we say things like "the functor $$A \mapsto \mathrm{Hom}(FA, Z)$$" (for some functor F and object Z) without bothering to spell out the action on morphisms all the time

#### [Reid Barton (Sep 08 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133541110):
So, I'd like to be able to infer the functor-ness of `λ A, F A ⟶ Z`, for example.

#### [Reid Barton (Sep 08 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133541177):
Currently I can express it as `F.comp (yoneda Z)` or something opaque like that

#### [Reid Barton (Sep 08 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133541292):
I'm pretty sure the way we do this is just type checking except we also have to keep track of whether variables appear in a positive or negative (= covariant or contravariant) position.

#### [Reid Barton (Sep 08 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133541429):
$$\mathrm{colim}_{j \in J} \mathrm{lim}_{i \in I} F(i, j)$$ was a real-world example of this. To even make sense of this we need to know that $$\mathrm{lim}_{i \in I} F(i, j)$$ is functorial in $$j$$.

#### [Reid Barton (Sep 08 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133541474):
If you had a binder notation for (co)limits which also could infer the functoriality then you could literally write `colim (j : J), lim (i : I), F (i, j)`

#### [Mario Carneiro (Sep 08 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133542353):
You could do this via a custom pexpr parser

#### [Reid Barton (Sep 08 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133542416):
In :four_leaf_clover: or today?

#### [Mario Carneiro (Sep 08 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133542425):
today, I think

#### [Mario Carneiro (Sep 08 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133542431):
e.g. `def my_hom := by ccc \lam x:C, \<x, x\>`

#### [Reid Barton (Sep 08 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133542437):
Oh, like as an argument to a tactic. Yes

#### [Mario Carneiro (Sep 08 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133542449):
It has to be valid leanish syntax, but I don't think the names have to resolve or anything, you can just inspect the syntax

#### [Reid Barton (Sep 08 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133542476):
So to clarify, by "parser" you mean I get an actual already-parsed `pexpr`, then I do whatever processing I want with it to produce something else

#### [Reid Barton (Sep 08 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133542570):
that is, the tactic will receive `expr.lam .....`

#### [Reid Barton (Sep 08 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133542673):
Can I write notation like ``notation `fun` e := by ccc e``, or is it too late by then?

#### [Reid Barton (Sep 08 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133542734):
Or I guess there are things called macros?

#### [Reid Barton (Sep 08 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133542902):
Another idea is to use an auto param like
```lean
variables {C D : Type} [small_category C] [small_category D]
def mk_fun (f : C → D) (map : Π (a b : C), (a ⟶ b) → (f a ⟶ f b) . guess_functor) : functor C D :=
```
and then have the tactic process the goal, but then I guess it can only get an elaborated expr?

#### [Reid Barton (Sep 08 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133542984):
It would probably be least confusing if the action on objects was exactly the provided expression, anyways.

#### [Reid Barton (Sep 08 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133543123):
`ccc` is a bit different but also an interesting idea. You could imagine many variants (cartesian categories, monoidal categories, symmetric monoidal categories etc.)

#### [Reid Barton (Sep 08 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133543323):
Like in a monoidal (only) category you would be allowed to write `\lam <<a, b>, c>, <a, <b, c>>` but not `\lam <a, b>, <b, a>`.

#### [Reid Barton (Sep 08 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133543337):
With a cartesian category you can also duplicate and discard variables.

#### [Reid Barton (Sep 08 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133544989):
I want to write something like this but it doesn't work. How can I get an `expr` representing `f` to pass into `go`?
```lean
meta def go : pexpr → tactic pexpr
| (expr.var 0) := return (expr.var 0)
| e := return e

meta def guess_functor_core : pexpr → tactic pexpr
| (expr.lam var _ t body) := do
    map_body ← go body,
    return ``(λ _ _ f, %%body)
| e := return e
```

#### [Reid Barton (Sep 08 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133545122):
I guess this was already asked at https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/creating.20lambda.20without.20tactic

#### [Reid Barton (Sep 08 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133546868):
```lean
def myfun : C ↝ C := by guess_functor (λ x, F (F x))
#print myfun
│ def myfun : Π {C : Type} [_inst_1 : small_category C] {F : C ⥤ C}, C ⥤ C :=
│ λ {C : Type} [_inst_1 : small_category C] {F : C ⥤ C},
│   {obj := λ (x : C), ⇑F (⇑F x),
│    map' := λ (X Y : C) (f : X ⟶ Y), functor.map F (functor.map F f),
│    map_id' := _,
│    map_comp' := _}
```

#### [Mario Carneiro (Sep 08 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133552385):
that works?

#### [Mario Carneiro (Sep 08 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133552432):
I was expecting the output to be more like `F >> F`

#### [Scott Morrison (Sep 08 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133557295):
That's pretty cool! Can we play with it?

#### [Scott Morrison (Sep 08 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133557301):
Inspired by that, I wrote a pretty dumb `fyn` (short for "follow your nose") tactic, that tries to build morphisms out of what it has at hand.

#### [Scott Morrison (Sep 08 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133557342):
It is just `solve_by_elim` also using:
```
[ `category_theory.category.id, 
  `category_theory.functor.map, 
  `category_theory.nat_trans.app, 
  `category_theory.category.comp ]
```

#### [Scott Morrison (Sep 08 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133557348):
With that I can get the construction of the yoneda functor down to:
```
def yoneda : C ⥤ ((Cᵒᵖ) ⥤ (Type v₁)) := 
{ obj := λ X, { obj := λ Y : C, Y ⟶ X } }
```

#### [Scott Morrison (Sep 08 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133557355):
down from
```
def yoneda : C ⥤ ((Cᵒᵖ) ⥤ (Type v₁)) := 
{ obj := λ X, { obj := λ Y : C, Y ⟶ X,
                map' := λ Y Y' f g, f ≫ g },
  map' := λ X X' f, { app := λ Y g, g ≫ f } }
```

#### [Scott Morrison (Sep 08 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133557489):
which is itself down from
```
def yoneda : C ⥤ ((Cᵒᵖ) ⥤ (Type v₁)) := 
{ obj := λ X, { obj := λ Y : C, Y ⟶ X,
                map' := λ Y Y' f g, f ≫ g,
                map_comp' := begin intros X_1 Y Z f g, ext1, dsimp at *, erw [category.assoc] end,
                map_id' := begin intros X_1, ext1, dsimp at *, erw [category.id_comp] end },
  map' := λ X X' f, { app := λ Y g, g ≫ f,
                      naturality' := begin intros X_1 Y f_1, ext1, dsimp at *, simp at * end },
  map_comp' := begin intros X Y Z f g, ext1, ext1, dsimp at *, simp at * end,
  map_id'   := begin intros X, ext1, ext1, dsimp at *, simp at * end }
```
before `obviously`. :-)

#### [Johan Commelin (Sep 08 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133557712):
That's really awesome. I like!

#### [Reid Barton (Sep 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133560247):
Sure, here it is: https://gist.github.com/rwbarton/46f3352f7a4b84bd75c7c335efd74bb9
I'm sure that almost everything about this is wrong, and it fails on almost any more complicated example.
Currently it only supports one outer layer of lambda, so it wouldn't work for `yoneda` yet. I did add products though which sometimes work.

#### [Reid Barton (Sep 08 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133560344):
One concern I had with a tactic like this is that because it produces data, not a proof, it's important that the exact form of the output be predictable. That's why I thought some kind of induction on the expression might be preferable to a tactic which just tries to repeatedly apply things. It's possible you could get the same predictability from the latter approach too, though.

#### [Reid Barton (Sep 08 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133561161):
@**Scott Morrison**, then also consider
```lean
notation `ƛ` binders `, ` r:(scoped f, { category_theory.functor . obj := f }) := r
```

#### [Scott Morrison (Sep 08 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133562061):
```def yoneda : C ⥤ ((Cᵒᵖ) ⥤ (Type v₁)) := ƛ X, ƛ Y : C, Y ⟶ X```

#### [Scott Morrison (Sep 08 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133562063):
This is getting a little silly. :-)

#### [Reid Barton (Sep 08 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133562079):
is that `: C` needed because the variable comes from `Cᵒᵖ`?

#### [Scott Morrison (Sep 08 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133562081):
I can't omit the `: C` after the `Y`, or my `construct_morphism` gets confuseds.

#### [Reid Barton (Sep 08 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133562084):
how about `ƛ X, ƛ Y, (X, Y)`?

#### [Scott Morrison (Sep 08 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133562086):
What do you mean?

#### [Reid Barton (Sep 08 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133562141):
I mean it's a functor C -> D -> C x D, can your tactic support it? If so is the type annotation on Y required?

#### [Reid Barton (Sep 08 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133562190):
Also, I'm curious what happens if you try `ƛ x, x ⟶ x`

#### [Reid Barton (Sep 08 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133562248):
Slightly less silly notation idea is `\lam'`

#### [Scott Morrison (Sep 08 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133563447):
```def foo : C ⥤ (D ⥤ (C × D)) := ƛ X, ƛ Y, (X, Y)```

#### [Kevin Buzzard (Sep 08 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/functoriality tactic/near/133565802):
The fact that the Yoneda definition now looks like that is in some sense indicative of how little content is involved in any of the checks -- the content is in the idea that the functor exists rather than the verification that it does. I don't think it's silly at all really, I think that in some sense all that is left in the code is the idea, and a machine is doing the rest -- which is what machines are supposed to do. There are plenty of "follow your nose" definitions and theorems in mathematics. I started noticing this when I introduced the following technique into my teaching: I would state a theorem (e.g. "if a_n tends to a and b_n tends to b then (a_n + b_n) tends to a+b") and during the proof I would highlight the *idea* in the proof, which in this case is "epsilon / 2 not epsilon". I would encourage students not to learn the proof but to learn the idea, and to let the rest of the proof flow naturally. That's what's happening here -- it turns out that there are no ideas in the checks, the idea is the map on objects, and that is now all that's left.

