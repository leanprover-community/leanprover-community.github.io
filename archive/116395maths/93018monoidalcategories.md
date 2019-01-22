---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/93018monoidalcategories.html
---

## [maths](index.html)
### [monoidal categories](93018monoidalcategories.html)

#### [Scott Morrison (Nov 07 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915123):
@**Michael Jendrusch** has recently started work on monoidal categories again. (Yay!)

#### [Scott Morrison (Nov 07 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915139):
I've been looking at what he's written, and I want to resume my rant about how terrible coercions are, as a result.

#### [Scott Morrison (Nov 07 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915148):
He's defined monoidal categories, and I think these are uncontroversial.

#### [Scott Morrison (Nov 07 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915151):
https://github.com/mjendrusch/monoidal-categories-reboot/blob/master/src/monoidal_categories_reboot/monoidal_category.lean

#### [Mario Carneiro (Nov 07 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915158):
so many axioms...

#### [Scott Morrison (Nov 07 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915160):
However when he gets to monoidal functors the horrors caused by coercions start to creep out...

#### [Scott Morrison (Nov 07 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915162):
Ah -- maybe I should address that first.

#### [Scott Morrison (Nov 07 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915165):
You might have said:

#### [Scott Morrison (Nov 07 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915211):
surely a monoidal category should be described as a category `C` equipped with a functor `C \times C \func C`, satisfying ...

#### [Scott Morrison (Nov 07 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915216):
(this will certainly reduce the number of axioms, at least slightly, because various things are wrapped up in functoriality)

#### [Scott Morrison (Nov 07 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915225):
However... implementation details forced on us by Lean make this a bad idea (as I discovered when I did monoidal categories previously)

#### [Mario Carneiro (Nov 07 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915228):
hopefully you prove the equivalence though?

#### [Scott Morrison (Nov 07 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915274):
Yes, it's easy (and Michael started doing it) to show afterwards that these things assemble into functors, and natural transformations, and so on.

#### [Scott Morrison (Nov 07 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915297):
The problem with making tensor product a functor first of all is that it becomes really painful to implement notation `X \otimes Y` and `f \otimes' g`.

#### [Mario Carneiro (Nov 07 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915307):
what's the issue?

#### [Scott Morrison (Nov 07 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915348):
You end up having to define as auxiliary lemmas curried versions of the functor of objects, but even then the elaborator often really struggles.

#### [Scott Morrison (Nov 07 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915363):
(Sorry, it's been a year or so since I last fought with this issue... give me a moment.)

#### [Mario Carneiro (Nov 07 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915369):
Can you make it a curried functor instead?

#### [Mario Carneiro (Nov 07 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915376):
cat being a CCC and all

#### [Scott Morrison (Nov 07 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915434):
You could make it a curried functor, but I don't think it would help. If T was your tensor product functor, you still couldn't write `T X Y` and have the elaborator successfully introduce both coercions.

#### [Scott Morrison (Nov 07 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915471):
Neither `T (X, Y)`, if `T : C \times C \func C`, or `T X Y`, if `T : C \func (C \func C)` will elaborate reliably. (In fact, I think they won't ever elaborate.)

#### [Mario Carneiro (Nov 07 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915479):
that's sad...

#### [Scott Morrison (Nov 07 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915532):
You can see examples of this all over my (no-longer-compiling) earlier attempt at monoidal categories.

#### [Mario Carneiro (Nov 07 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915535):
What about an infix functor application operator?

#### [Mario Carneiro (Nov 07 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915540):
like `<$>` for `functor`

#### [Scott Morrison (Nov 07 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915549):
```
@[ematch] definition interchange (f : U ⟶ V) (g : V ⟶ W) (h : X ⟶ Y) (k : Y ⟶ Z) :
  (f ≫ g) ⊗ (h ≫ k) = (f ⊗ h) ≫ (g ⊗ k) :=
  @Functor.functoriality (C × C) _ C _ (tensor C) ⟨U, X⟩ ⟨V, Y⟩ ⟨W, Z⟩ ⟨f, h⟩ ⟨g, k⟩
```
should really just be proved by `(tensor  C).map_comp (f, h) (g,k)`, but instead we need to use @, and specify way too many implicit arguments.

#### [Scott Morrison (Nov 07 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915556):
Yes --- so this is what I had long ago.

#### [Scott Morrison (Nov 07 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915560):
I had `+>` for obj, and `&>` for map, although I really don't care what the symbols are.

#### [Scott Morrison (Nov 07 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915564):
I would _love_ to move back to this model, which would let us get rid of lots of coercions.

#### [Mario Carneiro (Nov 07 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915612):
I've heard this story before, and I don't disagree with you

#### [Mario Carneiro (Nov 07 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915628):
I really want coercions to work, and in principle they could, but lean's coercion model is not extensible enough

#### [Mario Carneiro (Nov 07 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915646):
it should be a parser extension rather than being tied to `coe` in core

#### [Scott Morrison (Nov 07 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915652):
If we were in a situation where modifying the coercion mechanism was on the table, I would absolutely support struggling on with coercions, essentially to gain data about what we really want.

#### [Scott Morrison (Nov 07 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915697):
But I'm not sure whether :four_leaf_clover: gives us this prospect, or not.

#### [Mario Carneiro (Nov 07 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915706):
I think it might, at least it should not be far from the areas under development

#### [Scott Morrison (Nov 07 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915710):
If my fighting with coercions is not significantly likely to result in better coercions later, I just want the suffering to go away. :-)

#### [Mario Carneiro (Nov 07 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915724):
the fact that simp doesn't work under coercions is something we might be able to fix in lean 3

#### [Scott Morrison (Nov 07 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915727):
I haven't even started explaining the difficulties coercions are causing in the design of `monoidal_functor`... :-)

#### [Mario Carneiro (Nov 07 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915773):
right, sorry to derail your story. carry on

#### [Scott Morrison (Nov 07 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915790):
Essentially: if we want `monoidal_functor` to extend `functor`, we need new coercions so we can still write `F X`, when `F` is a monoidal functor. Now however none of the lemmas involving `F X` will apply when `F` is a monoidal functor, because the coercion won't be the right one.

#### [Scott Morrison (Nov 07 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915792):
So we'll have to reproduce all the lemmas...

#### [Scott Morrison (Nov 07 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915795):
And we'll have to do this again for `braided_functor`, and then again for `additive_functor`, and then again for ...

#### [Mario Carneiro (Nov 07 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915834):
wait, what's a monoidal functor now

#### [Mario Carneiro (Nov 07 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915847):
oh https://github.com/mjendrusch/monoidal-categories-reboot/blob/master/src/monoidal_categories_reboot/monoidal_functor.lean

#### [Scott Morrison (Nov 07 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915848):
monoidal functor doesn't exist yet, beyond Michael's first cut at https://github.com/mjendrusch/monoidal-categories-reboot/blob/master/src/monoidal_categories_reboot/monoidal_functor.lean

#### [Scott Morrison (Nov 07 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915853):
and you can see at the bottom of that file the problems waiting for us as soon as we define composition of monoidal functors.

#### [Mario Carneiro (Nov 07 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915944):
What's the alternative?

#### [Scott Morrison (Nov 07 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915954):
well, if all the coercions were gone, our problems would mostly disappear.

#### [Mario Carneiro (Nov 07 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146915997):
if the coercions were gone, it wouldn't typecheck. Are you writing explicit functions now?

#### [Scott Morrison (Nov 07 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916000):
Instead of having `functor.map'`, the structure field, which doesn't use the coercion, and `functor.map`, the same, as a lemma written using the coercion, we'd just have the structure field.

#### [Mario Carneiro (Nov 07 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916006):
`F.to_functor.map f`?

#### [Scott Morrison (Nov 07 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916008):
So we wouldn't have to define a new version of `map` for monoidal functors, so all the lemmas about `functor.map` would still apply

#### [Scott Morrison (Nov 07 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916009):
Yes.

#### [Scott Morrison (Nov 07 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916020):
But you wouldn't have to write the `.to_functor` explicitly.

#### [Mario Carneiro (Nov 07 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916022):
?

#### [Mario Carneiro (Nov 07 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916025):
what's the magic sauce you are using in place of coercions

#### [Scott Morrison (Nov 07 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916029):
Am I wrong? I thought that's how the extension mechanism works -- you can refer directly to the fields of the parent structure.

#### [Mario Carneiro (Nov 07 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916074):
It depends on whether you are using the old structures or new

#### [Scott Morrison (Nov 07 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916076):
new

#### [Scott Morrison (Nov 07 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916082):
but this certainly works, I just double checked :-)

#### [Mario Carneiro (Nov 07 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916094):
Is the `to_functor` in the pp.all term?

#### [Scott Morrison (Nov 07 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916287):
Yes

#### [Scott Morrison (Nov 07 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916297):
The `to_functor` is in fact there even without `pp.all`. You just don't need to write it.

#### [Scott Morrison (Nov 07 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916427):
As far as I can see the parser is doing this. There's no `monoidal_functor.obj` field at all,  but you can nevertheless write `F.obj X` when `F` is a monoidal functor, and when you pp the resulting term it shows as `F.to_functor.obj X`.

#### [Scott Morrison (Nov 07 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916445):
The essential problem is that because of coercions, we have all this duplication: `functor` has both `map'` and `map`, and `map_comp'` and `map_comp`, etc.

#### [Scott Morrison (Nov 07 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916452):
Every time we extend functor (or anything similar), we will need to reproduce all this duplication again.

#### [Mario Carneiro (Nov 07 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916502):
hm, this is parser magic we can't duplicate

#### [Reid Barton (Nov 07 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916655):
Sorry, so to go back to the start, if we forgot about coercions entirely, is there still an issue with defining the tensor product to be a functor from C x C to C?

#### [Scott Morrison (Nov 07 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916709):
I think there still is.

#### [Scott Morrison (Nov 07 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916711):
The basic question is how to implement `X \otimes Y`.

#### [Reid Barton (Nov 07 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916717):
`T.app (X, Y)`?

#### [Scott Morrison (Nov 07 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916719):
You mean `T.obj (X, Y)`?

#### [Reid Barton (Nov 07 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916720):
er, `T.obj`

#### [Reid Barton (Nov 07 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916765):
I can see that writing down the functors which the associator is supposed to be a natural isomorphism between is going to be ugly

#### [Scott Morrison (Nov 07 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916767):
The problem there is that for reasons I don't totally understand, even having the pair construction in there gums up the elaborator.

#### [Reid Barton (Nov 07 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916768):
hm

#### [Scott Morrison (Nov 07 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916773):
My old monoidal-categories repository didn't use any coercions.

#### [Scott Morrison (Nov 07 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916780):
(unfortunately I don't have a compiling version of it anymore...)

#### [Scott Morrison (Nov 07 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916812):
But I found myself having to use
```
-- Convenience methods which take two arguments, rather than a pair. (This seems to often help the elaborator avoid getting stuck on `prod.mk`.)
definition tensorObjects (X Y : C) : C := (tensor C) +> (X, Y)

infixr ` ⊗ `:80 := tensorObjects -- type as \otimes
```

#### [Reid Barton (Nov 07 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916854):
Another question: how about using isos for the associator/unitors instead of four fields each?

#### [Reid Barton (Nov 07 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916855):
I imagine you thought of that already

#### [Scott Morrison (Nov 07 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916857):
but then there's an extra layer of folding and unfolding `tensorObjects`

#### [Scott Morrison (Nov 07 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916860):
Actually, the question of using isos is a good one.

#### [Scott Morrison (Nov 07 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916862):
and I'm not sure that I did think about it carefully.

#### [Scott Morrison (Nov 07 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916903):
I suspect I wrote my initial monoidal categories library before I'd actually ironed out a usable implementation of isomorphisms....

#### [Scott Morrison (Nov 07 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916908):
@**Michael Jendrusch**, next time you're around, how about we try this idea out: using isomorphisms as the fields for associators and unitors, rather than the four separate fields?

#### [Reid Barton (Nov 07 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146916961):
Also: no bicategories?? :upside_down:

#### [Reid Barton (Nov 07 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146917029):
I kind of want to formalize (bi)limits in bicategories, since I feel the literature on them is kind of spotty.

#### [Reid Barton (Nov 07 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146918446):
but, I might want to do it less if it is going to look like https://ncatlab.org/nlab/show/bicategory#detailedDefn. How would I even know that I got the definition correct?

#### [Scott Morrison (Nov 07 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146922053):
@**Reid Barton**, I've been considering trying to talk @**Michael Jendrusch** into doing bicategories. :-) I would like them, too.

#### [Scott Morrison (Nov 07 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146922071):
But I think it makes sense to sort out the issues we're having here first, and if they are all solvable it might be a cheap rewrite to generalise...

#### [Scott Morrison (Nov 07 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146922130):
@**Michael Jendrusch**, I just added two new commits that package associators, unitors, and tensorators as isos. I think it is nicer.

#### [Johan Commelin (Nov 07 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146924968):
Yesterday one of my colleagues walked in to have a quick look at the workshop. He is working on derivators and such stuff. He explained how we might want to use multicategories for this. But I'm not sure how much work it would be to set up all the basics. He said it would help us get rid of the pentagon axiom in some sense. But I'm not sure if it means that the carpet won't fit in another corner... (is this an English idiom?).
@**Scott Morrison|110087** Are you familiar with this multicategorical approach?

#### [Michael Jendrusch (Nov 07 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146925211):
```quote
@**Michael Jendrusch**, I just added two new commits that package associators, unitors, and tensorators as isos. I think it is nicer.
```
It's merged! I would kind of like to have bicategories, too, but this looks painful (https://ncatlab.org/nlab/show/bicategory#detailedDefn).

#### [Michael Jendrusch (Nov 07 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146925412):
On another note, making `µ` an iso in the definition of a monoidal functor makes that a _strict_ monoidal functor according to nLab, where I would also want _lax_ monoidal functors. Maybe we can define a _lax_ monoidal functor and then extend it to a _strict_ monoidal functor?

#### [Scott Morrison (Nov 07 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146926349):
Ah, it's  a little subtle. If you want lax monoidal functors, then I want oplax ones (this is a serious request, actually: <https://arxiv.org/abs/1701.00567>. So if we want to do it via inheritance we'll be dealing with a diamond.

#### [Scott Morrison (Nov 07 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146926350):
But I agree it's desirable.

#### [Scott Morrison (Nov 07 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146926357):
(But you certainly can't use the name monoidal functor if you mean a lax one. :-)

#### [Scott Morrison (Nov 07 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146926559):
Regarding multicategories --- I'm not opposed to someone also introducing these, but I'm pretty confident it's all blind men describing an elephant. Now if we want to talk about disklike categories <https://arxiv.org/pdf/1108.5386.pdf>, then we'd be cooking with gas.

#### [Reid Barton (Nov 07 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/146964187):
Actually, maybe bicategories won't be that bad at all. Shouldn't it just be a matter of asking for `Pi a b. category (C a b)`, then adding a bunch of type indices everywhere in the definition of monoidal category?

#### [Scott Morrison (Nov 07 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/147252547):
Yes, that sounds right. It's a pity you can't mix `variables` syntax with structures; you could almost leave out all those extra type indices!

#### [Michael Jendrusch (Nov 08 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/147289125):
```quote
Ah, it's  a little subtle. If you want lax monoidal functors, then I want oplax ones (this is a serious request, actually: <https://arxiv.org/abs/1701.00567>. So if we want to do it via inheritance we'll be dealing with a diamond.
```
It seems that a lot of things in category theory result in diamonds when using inheritance (e.g. with strict monoidal categories). Is there another standard way of treating this without inheritance, and what are the actual problems one gets with diamonds in Lean?

#### [Michael Jendrusch (Nov 08 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/147297174):
would it make sense to try and work around inheritance (and thus diamonds) by not having a classes `lax_monoidal_functor`, `oplax_monoidal_functor` both inheriting from functor (and getting a diamond from defining `monoidal_functor` as inheriting from both), instead opting to have `functor_is_lax_monoidal`, `functor_is_oplax_monoidal` together with an instance `functor_is_monoidal` for every functor which is both lax and oplax, like this?

```lean

class functor_is_lax_monoidal
  (C : Type u) [monoidal_category.{u v} C]
  (D : Type u') [monoidal_category.{u' v'} D]
  (F : C ⥤ D) :=
-- definition of lax monoidal functor here.

class functor_is_oplax_monoidal
  (C : Type u) [monoidal_category.{u v} C]
  (D : Type u') [monoidal_category.{u' v'} D]
  (F : C ⥤ D) :=
-- definition of oplax monoidal functor here.

class functor_is_monoidal
  (C : Type u) [monoidal_category.{u v} C]
  (D : Type u') [monoidal_category.{u' v'} D]
  (F : C ⥤ D) :=
-- definition of monoidal functor here.

instance lax_and_oplax
  (C : Type u) [monoidal_category.{u v} C]
  (D : Type u') [monoidal_category.{u' v'} D]
  (F : C ⥤ D) [functor_is_lax_monoidal C D F] [functor_is_oplax_monoidal C D F] :
  functor_is_monoidal C D F := by obviously
```

#### [Scott Morrison (Nov 08 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/147333122):
This is an interesting approach; I wonder if we should re-explore making `functor` a typeclass right from the beginning.

#### [Scott Morrison (Nov 08 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/147333145):
My concern is that `functor_is_monoidal` carries data (the tensorator), so it's a little scary making it a typeclass.

#### [Scott Morrison (Nov 08 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/147333211):
However in my experience it's extremely rare that one considers two different tensorators for the same functor. (Although not _never_)

#### [Scott Morrison (Nov 08 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/147333229):
But if we're going to carry this data in a typeclass, why aren't we carrying the data of `functor.map` in a typeclass?

#### [Scott Morrison (Nov 08 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/147333256):
I have tried this, ..., but it was a long time ago and I don't really remember why I didn't like it then.

#### [Scott Morrison (Nov 10 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/monoidal categories/near/147448765):
@**Michael Jendrusch**, I started adding the monoidal structure on any category with products, that should subsume your initial example of `Type u`. It's not there yet, but I think it's a fun test of our limits library to make sure this is doable with no more effort than in the `Type u` case.

