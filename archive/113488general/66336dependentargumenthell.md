---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66336dependentargumenthell.html
---

## Stream: [general](index.html)
### Topic: [dependent argument hell](66336dependentargumenthell.html)

---

#### [Scott Morrison (Sep 12 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771753):
I seem to have backed myself into a corner, and I don't understand how to escape. I would really appreciate some help, as it feels like this problem is an instance of one that will become more and more severe as we do more advanced maths.

#### [Scott Morrison (Sep 12 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771756):
I've been working on morphisms of presheaves.

#### [Scott Morrison (Sep 12 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771768):
These are "bundled" presheaves, so they consist of a topological space, along with a functor from the category of open sets (morphisms are subsets) to some other category.

#### [Scott Morrison (Sep 12 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771812):
A morphism of presheaves `(X, O_X) \hom (Y, O_Y)` consists of a pair: a function `f : X \hom Y`, which is just a continuous map, and

#### [Scott Morrison (Sep 12 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771817):
a "comorphism", which is a natural transformation from `O_Y \to f_* O_X`.

#### [Scott Morrison (Sep 12 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771858):
The point here is that you can push forward a presheaf on X to presheaf on Y, along a continuous map (take an open set of Y, pull it back via f, then evaluate the presheaf on it).

#### [Scott Morrison (Sep 12 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771924):
Now, I want to define the identity presheaf morphism, and I want to define compositions of presheaf morphisms, and check they satisfy the right properties.

#### [Scott Morrison (Sep 12 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771965):
Yesterday I managed to do this, but both the constructions and the proofs were very ugly.

#### [Scott Morrison (Sep 12 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133771976):
Today I've made another attempt, where the constructions are quite a bit better, and the proofs look like they should be easy but get stuck at the last hurdle, when we should just be cancelling off identity morphisms and saying we're done.

#### [Scott Morrison (Sep 12 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772022):
The code is at <https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/V_pre.lean>.

#### [Scott Morrison (Sep 12 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772037):
The particular problem I reach is the proof of `comp_id'` in constructing `instance : category (Presheaf.{u v} C) := ...`.

#### [Scott Morrison (Sep 12 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772085):
Just before the `sorry`, the goal is
```
C : Type u,
𝒞 : category C,
X Y : Presheaf C,
f : Presheaf_hom X Y,
X_1 : open_set ((Y.X).α)
⊢ functor.map (Y.𝒪) (𝟙 X_1) ≫
      ⇑(f.c) (⇑(map_open_set (𝟙 (Y.X))) X_1) ≫
        functor.map (X.𝒪) (functor.map (map_open_set (f.f)) (𝟙 (⇑(map_open_set (𝟙 (Y.X))) X_1))) =
    ⇑(f.c) X_1
```

#### [Scott Morrison (Sep 12 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772095):
And this should be perfectly manageable. The left hand side is a composition of three morphisms, and we should begin by observing the first and third are actually identity morphisms, since they are explicitly some functor applied to some identity morphism.

#### [Scott Morrison (Sep 12 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772100):
In particular we should be able to rewrite `functor.map (Y.𝒪) (𝟙 X_1) ` into `𝟙 (Y.𝒪 X_1) `

#### [Scott Morrison (Sep 12 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772102):
However `simp` fails.

#### [Reid Barton (Sep 12 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772147):
Yeah I've had this happen too. In that case the problem was some implicit argument was not `X_1` but only something defeq to it, and `simp` didn't like that.

#### [Reid Barton (Sep 12 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772150):
In my case `dsimp, simp` worked, but it doesn't look like that will help you judging from the two preceding lines

#### [Scott Morrison (Sep 12 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772154):
Trying the rewrite by hand, with increasing desperation:
```
rw [category_theory.functor.map_id]
rw [category_theory.functor.map_id Y.𝒪 X_1]

#### [Scott Morrison (Sep 12 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772161):
`rw [category_theory.functor.map_id Y.𝒪 X_1] {md:=semireducible}`

#### [Scott Morrison (Sep 12 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772164):
all fail.

#### [Reid Barton (Sep 12 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772165):
`erw`?

#### [Scott Morrison (Sep 12 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772166):
`erw` is just the same as `{md:=semireducible}`

#### [Scott Morrison (Sep 12 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772167):
(I'd usually use `erw` but didn't want to scare anyone. :-)

#### [Scott Morrison (Sep 12 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772210):
Reid is exactly right that the problem is an implicit argument.

#### [Scott Morrison (Sep 12 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772211):
Let's look at that, turning on `set_option pp.implict true` and inspecting the goal again.

#### [Scott Morrison (Sep 12 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772226):
The whole thing is a bit long, but the bit that corresponds to `functor.map (Y.𝒪) (𝟙 X_1)` is
```
@functor.map
        (@open_set (@bundled.α topological_space (@Presheaf.X C 𝒞 Y))
           (examples.topological_space (@Presheaf.X C 𝒞 Y)))
        (@open_set.open_sets (@bundled.α topological_space (@Presheaf.X C 𝒞 Y))
           (examples.topological_space (@Presheaf.X C 𝒞 Y)))
        C
        𝒞
        (@Presheaf.𝒪 C 𝒞 Y)
        X_1
        (⇑(@map_open_set (@Presheaf.X C 𝒞 Y) (@Presheaf.X C 𝒞 Y) (𝟙 (@Presheaf.X C 𝒞 Y))) X_1)
        (𝟙 X_1)
```

#### [Scott Morrison (Sep 12 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772266):
We can see the problem at the end there: the last three arguments are meant to consist of two objects, and a hom between them.

#### [Scott Morrison (Sep 12 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772271):
However we've got `X_1`,  `(⇑(@map_open_set (@Presheaf.X C 𝒞 Y) (@Presheaf.X C 𝒞 Y) (𝟙 (@Presheaf.X C 𝒞 Y))) X_1)`, and `(𝟙 X_1)`.

#### [Reid Barton (Sep 12 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772280):
Something like `id ⁻¹' X_1`, I guess?

#### [Scott Morrison (Sep 12 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772281):
We really want that second object to just be `X_1` again.

#### [Reid Barton (Sep 12 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772283):
is what that long thing is

#### [Scott Morrison (Sep 12 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772285):
If we `dsimp  [map_open_set]` we see:

#### [Scott Morrison (Sep 12 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772329):
```(@open_set.mk (@bundled.α topological_space (@Presheaf.X C 𝒞 Y))
           (examples.topological_space (@Presheaf.X C 𝒞 Y))
           (@subtype.val
                (@bundled.α topological_space (@Presheaf.X C 𝒞 Y) →
                 @bundled.α topological_space (@Presheaf.X C 𝒞 Y))
                (@continuous (@bundled.α topological_space (@Presheaf.X C 𝒞 Y))
                   (@bundled.α topological_space (@Presheaf.X C 𝒞 Y))
                   (@bundled.str topological_space (@Presheaf.X C 𝒞 Y))
                   (@bundled.str topological_space (@Presheaf.X C 𝒞 Y)))
                (𝟙 (@Presheaf.X C 𝒞 Y)) ⁻¹'
              @open_set.s (@bundled.α topological_space (@Presheaf.X C 𝒞 Y))
                (examples.topological_space (@Presheaf.X C 𝒞 Y))
                X_1)
           _)```

#### [Scott Morrison (Sep 12 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772338):
Which sadly is not definitely equal to `X_1`, although we can prove it is equal.

#### [Reid Barton (Sep 12 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772385):
oh no

#### [Scott Morrison (Sep 12 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772386):
In fact, we have a lemma prepared just for this!

#### [Reid Barton (Sep 12 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772390):
wait then

#### [Scott Morrison (Sep 12 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772394):
```
@[simp] def map_open_set_id_obj (X : Top) (U : open_set X.α) : map_open_set (𝟙 X) U = U :=
begin dsimp [map_open_set], cases U, congr, end
```

#### [Scott Morrison (Sep 12 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772412):
And `rw [map_open_set_id_obj]` says ...

#### [Scott Morrison (Sep 12 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772414):
`failed`

#### [Reid Barton (Sep 12 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772417):
I'm confused

#### [Reid Barton (Sep 12 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772420):
Doesn't this mean your goal is ill-typed?

#### [Scott Morrison (Sep 12 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772421):
(And `erw` is no better, nor does it seem that using `conv` to zoom in on it helps.)

#### [Scott Morrison (Sep 12 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772464):
That's what appears to be happening, I agree.

#### [Scott Morrison (Sep 12 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772467):
So how did Lean let me get this far?

#### [Reid Barton (Sep 12 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772468):
I had that happen too once, but I didn't understand how it happened, but it's almost certainly unrelated.

#### [Scott Morrison (Sep 12 2018 at 03:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772479):
I do have a note a few lines earlier in my code `It's hard to believe this typechecks!`

#### [Scott Morrison (Sep 12 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772519):
```
structure Presheaf_hom (F G : Presheaf.{u v} C) :=
(f : F.X ⟶ G.X)
(c : G.𝒪 ⟹ ((map_open_set f) ⋙ F.𝒪))

namespace Presheaf_hom
def id (F : Presheaf.{u v} C) : Presheaf_hom F F :=
{ f := 𝟙 F.X,
  c := begin apply nat_trans.vcomp, swap, apply whisker_on_right (map_open_set_id _).inv, apply (functor.id_comp _ _ _).inv end
}

def comp {F G H : Presheaf.{u v} C} (α : Presheaf_hom F G) (β : Presheaf_hom G H) : Presheaf_hom F H :=
{ f := α.f ≫ β.f,
  c := β.c ⊟ (whisker_on_left (map_open_set β.f) α.c), -- It's hard to believe this typechecks!
}
end Presheaf_hom
```

#### [Scott Morrison (Sep 12 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772525):
In particular, I have to jump through some hoops to construct the natural transformation for `id`.

#### [Scott Morrison (Sep 12 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772531):
But Lean appears to be happy with me just writing the "obvious" answer for `comp`.

#### [Reid Barton (Sep 12 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772542):
I found composition/associativity things are often easier than identity/unitality things

#### [Scott Morrison (Sep 12 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772591):
(... in real life as well as Lean, for me!)

#### [Scott Morrison (Sep 12 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772599):
(identities are strange and confusing in higher dimensions!)

#### [Reid Barton (Sep 12 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772671):
how hard would it be to find the first place the goal becomes ill-typed?
Is the goal before the last `simp` comprehensible?

#### [Scott Morrison (Sep 12 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772673):
The only avenues I can work out are:
1) Go back and work out where this "ill-typed, or at least hard-to-see-its-well-typed" expression first appears, and then "do something different".
2) Work out how to "fix" implicit arguments.

#### [Scott Morrison (Sep 12 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772717):
(This is an example, by the way, of a situation it would be nice to have a good term inspector, where you can toggle on and off implicit arguments for subtrees.)

#### [Reid Barton (Sep 12 2018 at 03:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772767):
Given that the implicit argument is not even defeq to the right thing, I think 2 isn't applicable in this case.
It looks to me like you hit a bug in Lean (which is probably not in the kernel, since it is only the goal which is ill-typed, but still very frustrating).

#### [Scott Morrison (Sep 12 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772769):
Oooh, I maybe found a way around it.

#### [Scott Morrison (Sep 12 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772777):
It's just a matter of `dsimp`ing expressions in a different order, so somehow it's not at all a principled solution.

#### [Scott Morrison (Sep 12 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772821):
Oh, no, the problem is there a step or two later. I was just doing something by hand that `simp` was doing anyway.

#### [Scott Morrison (Sep 12 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772822):
:-(

#### [Reid Barton (Sep 12 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772935):
I'm kind of surprised that the result of the tactic passes typechecking, even with `sorry` there

#### [Scott Morrison (Sep 12 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133772995):
Shall I try for a proof of false? :-)

#### [Reid Barton (Sep 12 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773004):
Unfortunately I doubt you can prove false from a term which is ill-typed but only in that one of the type arguments is definitionally wrong (but propositionally correct)

#### [Scott Morrison (Sep 12 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773005):
Okay... this is bizarre, but `cases X_1` seems to break the impasse.

#### [Reid Barton (Sep 12 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773006):
that's not surprising

#### [Scott Morrison (Sep 12 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773008):
Why is that?

#### [Reid Barton (Sep 12 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773051):
same reason why you used `cases U` to prove `map_open_set_id_obj`

#### [Reid Barton (Sep 12 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773055):
basically you have an equality that looks like <x.1, _> = x

#### [Scott Morrison (Sep 12 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773056):
Okay, and there's a (horrible) proof:
```
  comp_id' := λ X Y f, --sorry,
    begin 
      ext,
      -- we check the functions first
      dsimp [Presheaf_hom.id, Presheaf_hom.comp], 
      simp,
      -- and now the comorphisms
      dsimp [Presheaf_hom.id, Presheaf_hom.comp], 
      simp,
      ext,
      dsimp [whisker_on_right, whiskering_on_right, whisker_on_left, whiskering_on_left],
      dsimp [map_open_set],
      simp,
      erw [category_theory.functor.map_id],
      simp,
      cases X_1,
      simp,
      apply congr_fun,
      simp,
    end,
```

#### [Reid Barton (Sep 12 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773062):
where x is a variable, and so they can never be definitionally equal. Buf after `cases x`, it's okay

#### [Scott Morrison (Sep 12 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773063):
I see.

#### [Reid Barton (Sep 12 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773064):
when you do comp, both sides look like <_, _>

#### [Reid Barton (Sep 12 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773065):
and that's why comp is easier

#### [Reid Barton (Sep 12 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773107):
This still feels weird to me, but I've seen it a few times

#### [Scott Morrison (Sep 12 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773113):
So maybe the summary from today is:
> avoid `cases` when constructing stuff, because then you'll have horrible `X.rec` expressions to deal with later, but
> remember to try `cases` when an implicit argument looks wrong!

#### [Reid Barton (Sep 12 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773166):
Well, in general when you need to prove `(blah.mk _ _) = X`, it will require doing cases on X

#### [Reid Barton (Sep 12 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773170):
I still think something very fishy is going on with your original code

#### [Scott Morrison (Sep 12 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773173):
Sure. The problem here was that it wasn't at all obvious to me that this was what was going on.

#### [Mario Carneiro (Sep 12 2018 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773227):
The file you linked references `category_theory.examples.topological_spaces` but I can't find it in the repo

#### [Scott Morrison (Sep 12 2018 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773228):
That's in mathlib

#### [Scott Morrison (Sep 12 2018 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773229):
:-)

#### [Reid Barton (Sep 12 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773271):
I just finished building your repo locally so I can take a look

#### [Scott Morrison (Sep 12 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773278):
And just to confound you, Mario, lean-category-theory is currently pointing at a branch of mathlib on `community`, in which that file has been modified. :-)

#### [Reid Barton (Sep 12 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773287):
Anyways the situation you were in ought to have been impossible. If `x : t` and `x : t'` then `t` and `t'` should be definitionally equal. Not just propositionally equal.

#### [Reid Barton (Sep 12 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773288):
At least, as far as I understand.

#### [Scott Morrison (Sep 12 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773290):
yes.

#### [Mario Carneiro (Sep 12 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773291):
oh wow, mathlib category theory has grown quite a bit since I last checked

#### [Mario Carneiro (Sep 12 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773444):
```
-- Do I dare define `open_set` as a functor from Top to CAT? I don't like CAT.

def map_open_set
  {X Y : Top} (f : X ⟶ Y) : open_set Y.α ⥤ open_set X.α :=
```
Why is it a functor to CAT? It looks like `open_set` should be a (contravariant) functor from `Top` to `Type`

#### [Scott Morrison (Sep 12 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773453):
For each topological space X, we get the category of open sets and inclusions.

#### [Reid Barton (Sep 12 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773493):
The ill-typed goal I encountered involved Lean getting confused about the difference between `quot` and `quotient`, and so I had a goal involving some types of the form `quot s a` where `s` was a setoid, which I had trouble producing

#### [Mario Carneiro (Sep 12 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773568):
Okay, I think I'm starting to piece this together. There is an unnamed function `comap f U` (where `f` is a bundled continuous function and `U` is an `open_set`) which is the object part of `map_open_set`

#### [Mario Carneiro (Sep 12 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773575):
And what is true is that `map_open_set (𝟙 X) U = comap (𝟙 X) U`, which is isomorphic to `U`

#### [Mario Carneiro (Sep 12 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773613):
so you have a classic two-category problem

#### [Scott Morrison (Sep 12 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773625):
I don't know this classic. :-)

#### [Reid Barton (Sep 12 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773626):
I think Mario means 2-category?

#### [Mario Carneiro (Sep 12 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773628):
You have to worry about coherences since it's not an equality

#### [Scott Morrison (Sep 12 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773629):
Oh, okay! :-)

#### [Scott Morrison (Sep 12 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773666):
Yes.

#### [Reid Barton (Sep 12 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773667):
Like, the Top -> Cat thing could be only a pseudofunctor

#### [Mario Carneiro (Sep 12 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773672):
As Kevin learned a while ago, a propositional equality should not ever be treated as equality in a category, only isomorphism

#### [Mario Carneiro (Sep 12 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773673):
objects are either defeq or isomorphic

#### [Scott Morrison (Sep 12 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773674):
but where am I abusing that here?

#### [Mario Carneiro (Sep 12 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773684):
```
-- These next two are desperate attempts to solve problems below.
@[simp] def map_open_set_id_obj (X : Top) (U : open_set X.α) : map_open_set (𝟙 X) U = U :=
begin dsimp [map_open_set], cases U, congr, end
@[simp] def map_open_set_id (X : Top) : map_open_set (𝟙 X) ≅ functor.id (open_set X.α) := 
```
this is bad news

#### [Mario Carneiro (Sep 12 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773691):
this equality should be turned into an iso, given a name, and explicitly reasoned with

#### [Scott Morrison (Sep 12 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773692):
It's the first one that is evil

#### [Scott Morrison (Sep 12 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773694):
and I don't use it

#### [Scott Morrison (Sep 12 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773736):
the second one is fine, isn't it?

#### [Reid Barton (Sep 12 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773743):
the type looks fine, but now I am confused about the implementation

#### [Mario Carneiro (Sep 12 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773744):
I think? I can't parse it

#### [Scott Morrison (Sep 12 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773745):
I just pushed an update

#### [Mario Carneiro (Sep 12 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773746):
`map_open_set (𝟙 X)` is a functor, so what does `≅` mean here?

#### [Scott Morrison (Sep 12 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773748):
that has the working proof, and doesn't have the evil `map_open_set_id_obj`

#### [Scott Morrison (Sep 12 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773786):
iso is automatically natural isomorphism

#### [Scott Morrison (Sep 12 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773791):
sweet sweet typeclass magic finds the category of functors between two fixed categories

#### [Reid Barton (Sep 12 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773792):
isomorphism in the functor category

#### [Scott Morrison (Sep 12 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773793):
and correctly interprets iso

#### [Mario Carneiro (Sep 12 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773796):
and that doesn't have any 2-category mess in it?

#### [Scott Morrison (Sep 12 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773799):
no -- for a fixed pair of categories C and D

#### [Scott Morrison (Sep 12 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773804):
functors and natural transformations between them are a perfectly honest 1-category

#### [Scott Morrison (Sep 12 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773806):
(indeed, the prototypical example)

#### [Reid Barton (Sep 12 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773899):
Oh man this is confusing.

#### [Mario Carneiro (Sep 12 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773901):
so where did you get that bad application from? `functor.map (Y.𝒪) (𝟙 X_1)`

#### [Reid Barton (Sep 12 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773903):
I noticed that both of these worked, and was confused.
```lean
  { app := λ U, show map_open_set (𝟙 X) U ⟶ U, from 𝟙 U },
  { app := λ U, show U ⟶ U, from 𝟙 U },
```

#### [Reid Barton (Sep 12 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773910):
Even though we know `map_open_set (𝟙 X) U = U` is not a definitional equality

#### [Mario Carneiro (Sep 12 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773911):
hah, it's because the hom destructs it

#### [Reid Barton (Sep 12 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773913):
right

#### [Scott Morrison (Sep 12 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773916):
Yeah, and I think this is where the "bad" application is coming from.

#### [Scott Morrison (Sep 12 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773956):
Can you explain what "the hom destructs it" means?

#### [Reid Barton (Sep 12 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773962):
```lean
instance : has_subset (open_set α) :=
{ subset := λ U V, U.s ⊆ V.s }
```

#### [Reid Barton (Sep 12 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773970):
this is what defines the partial order, and therefore the hom types

#### [Scott Morrison (Sep 12 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133773972):
oh ...

#### [Reid Barton (Sep 12 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774013):
it's not true that `map_open_set (𝟙 X) U = U` definitionally, but it is true that `(map_open_set (𝟙 X) U).s = U.s` because (contrary to my initial guess) `preimage id` is definitionally the identity

#### [Scott Morrison (Sep 12 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774014):
I see.

#### [Reid Barton (Sep 12 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774017):
Oh, wait...

#### [Reid Barton (Sep 12 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774022):
So maybe that weird goal was correctly typed, after all

#### [Scott Morrison (Sep 12 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774023):
Yeah.

#### [Scott Morrison (Sep 12 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774028):
And I could have replaced my evil lemma with

#### [Scott Morrison (Sep 12 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774071):
```
@[simp] def map_open_set_id_obj (X : Top) (U : open_set X.α) : (map_open_set (𝟙 X) U).s = U.s := rfl
```

#### [Scott Morrison (Sep 12 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774072):
and perhaps had it work...

#### [Scott Morrison (Sep 12 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774082):
Hmm,. you can indeed prove that via `rfl`, but I can't get it to help.

#### [Scott Morrison (Sep 12 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774124):
ah, I have to remove the dsimp [map_open_set], perhaps

#### [Mario Carneiro (Sep 12 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774125):
Scott, I'm trying to get your repo. How do you update everything with leanpkg?

#### [Scott Morrison (Sep 12 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774127):
`leanpkg build`?

#### [Scott Morrison (Sep 12 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774129):
It should notice if you don't have the right dependencies already in `_target`.

#### [Mario Carneiro (Sep 12 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774130):
I get version mismatch error

#### [Scott Morrison (Sep 12 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774136):
ah... Is your lean provided by elan?

#### [Scott Morrison (Sep 12 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774137):
This repo is set to use nightly-2018-06-21

#### [Scott Morrison (Sep 12 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774139):
but I think it should be safe to change that in leanpkg.toml file

#### [Scott Morrison (Sep 12 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774140):
What is the "official recommendation" these days?

#### [Mario Carneiro (Sep 12 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774179):
I've been using 3.4.1 even though a few bugfixes have come in

#### [Scott Morrison (Sep 12 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774185):
Since my student Keeley started forking Lean I've switched to using elan and don't notice these problems. :-)

#### [Mario Carneiro (Sep 12 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774188):
that's good to hear. You should write a tutorial :)

#### [Reid Barton (Sep 12 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774233):
for elan?

#### [Scott Morrison (Sep 12 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774234):
I really should borrow a windows machine, and write a tutorial for running elan on windows.

#### [Scott Morrison (Sep 12 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774365):
Ducking out for lunch. Thanks very much for the discussion today!

#### [Mario Carneiro (Sep 12 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774471):
Aha, I found some 2-categoricity:
```
structure Presheaf_hom (F G : Presheaf.{u v} C) :=
(f : F.X ⟶ G.X)
(c : G.𝒪 ⟹ ((map_open_set f) ⋙ F.𝒪))
```
Since `Presheaf_hom` has a component which is a functor, proving equality of homs is going to involve equality of objects

#### [Mario Carneiro (Sep 12 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774631):
I guess that can't really be avoided, but since `G.𝒪` is a functor out of a skeletal category (a partial order category), it suffices to prove isomorphism instead of equality

#### [Mario Carneiro (Sep 12 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133774739):
```
@[extensionality] lemma ext {F G : Presheaf.{u v} C} (α β : Presheaf_hom F G)
  (w : α.f = β.f) (h : α.c == β.c)
  : α = β :=
```
the `heq` here is evil. You should state some kind of composite equality here

#### [Scott Morrison (Sep 12 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775001):
Hi @**Mario Carneiro**, actually that component `Preasheaf_hom.c` is a natural transformation, not a functor, so equality is non-evil.

#### [Scott Morrison (Sep 12 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775042):
I agree that the `ext` lemma is evil. I will replace that.

#### [Mario Carneiro (Sep 12 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775051):
equality of natural transformations is not evil, equality of natural transformations in different categories is

#### [Scott Morrison (Sep 12 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775062):
Oh, so you're saying specifically the `heq` is evil.

#### [Scott Morrison (Sep 12 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775075):
I don't think we'll ever to to say anything about equalities of objects, however.

#### [Mario Carneiro (Sep 12 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775136):
I think I found the culprit. `map_open_sets` is a 2-categorical thing, since it takes homs to functors. This means that congruence says that equality of homs maps to natural iso of functors

#### [Mario Carneiro (Sep 12 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775143):
And this is the iso you should reference in the definition of `ext`

#### [Scott Morrison (Sep 12 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775147):
I'm filling in 
```
def map_open_set_iso {X Y : Top} (f g : X ⟶ Y) (h : f = g) : map_open_set f ≅ map_open_set g := {
  
}
```

#### [Scott Morrison (Sep 12 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133775148):
right now

#### [Kevin Buzzard (Sep 12 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133781152):
This is a terrifying thread to wake up to. It reminds me of when I couldn't prove anything about real numbers because there was no norm_num. But instead of a beginner struggling to prove math-trivial things because of a lack of tools, it's experts and tool-makers having problems with something that looks math-trivial

#### [Kevin Buzzard (Sep 12 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133781442):
I actually stopped thinking about pushing the perfectoid repo forward towards the definition of an adic space because this funky category showed up, Patrick was doing completions (which were also needed) and I knew someone had to do integral closures (which were also needed) so I went back to those and thought I'd wait a bit to see what the category experts thought about this category V_pre which had shown up "in the wild". I want to argue that we don't *need* V_pre, it's just a convenient container and I thought it would be a good test case. I could instead just make a new structure modelling the objects and muddle on from there and it would no doubt be fine at least as far as the ultimate goal is concerned, which is a definition.

#### [Mario Carneiro (Sep 12 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133781575):
I think this thread is Scott having an epiphany similar to the one that prompted that blog post https://mathematicswithoutapologies.wordpress.com/2018/09/11/guest-post-by-kevin-buzzard/

#### [Mario Carneiro (Sep 12 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133781606):
I think it boils down to "equalities of types are evil"

#### [Kevin Buzzard (Sep 12 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133784114):
As I'm sure you realise, that comment (it was only supposed to be a comment!) was very much informed by the comments you made when I was having that big meltdown about equality a few months ago ("Kevin, stop trolling!").

#### [Kevin Buzzard (Sep 12 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133784227):
A summer student, Ned Summers, was doing some 4th year category theory example sheet questions (using Scott's library as a dependency) and ran into these sorts of problems, and this time I was better equipped. Chris (who freely admits he knows nothing about category theory) had suggested some casts which had caused trouble for Ned, and I diagnosed the problem as exactly the same sort of thing: Ned had two objects X and Y and a proof that they were equal, and was doing exactly what a mathematican would do -- treating Hom(X,Z) as equal to Hom(Y,Z) etc etc. Equality in type theory is more delicate than that. Of course this doesn't change the fact that we are right, and your definition is rubbish -- but it's what we've got to work with ;-)

#### [Kenny Lau (Sep 12 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133784234):
> A summer student, Ned Summers

#### [Kevin Buzzard (Sep 12 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133784295):
They've almost all gone now. Ned stopped on Friday. Only about three left. I am going to spend all day writing documentation and basic questions. Yesterday I said "we want ten basic examples and ten basic questions about metaprogramming" -- today I'm (hopefully) going to write ten basic examples and ten basic questions about set membership.

#### [Kevin Buzzard (Sep 12 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133784364):
I asked a question on this chat probably last Wed or Thurs about how to generate "the identity morphism" between two objects which were provably equal, and Reid answered very quickly with some function called something like `iso_of_eq` which generated the data from the proof; it was because of my schemes meltdown that I had understood that this was what was missing.

#### [Chris Hughes (Sep 12 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133786353):
I didn't suggest the use of `eq.rec`. My instinct would be that `eq.rec` for data should be avoided if at all possible

#### [Kevin Buzzard (Sep 12 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133788910):
Maybe I got the wrong impression from Ned :-)

#### [Scott Morrison (Sep 12 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133794864):
Thanks to some help from Mario and Reid, it is well sorted out now!

#### [Scott Morrison (Sep 12 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133794955):
While I agree that I was making mistakes (being "evil") when I shouldn't have been, and the code is nicer as a result of today's exorcism, the fundamental cause of being stuck was something a bit different. I really need to catch up on sleep now, so I won't explain it now. :-)

#### [Scott Morrison (Sep 12 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133794972):
The upshot is that <https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/presheaves.lean> contains the definition of bundled presheaves (i.e. a topological space and a presheaf on it), and the right notion of morphisms between these, and indeed the category structure.

#### [Scott Morrison (Sep 12 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133794979):
It's certainly not all of `V_pre`, but it's the categorical theoretic core.

#### [Patrick Massot (Sep 12 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133794986):
Yeah, "Lean does no magic" ™ but sometimes a good exorcism session is needed

#### [Scott Morrison (Sep 12 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133795036):
Hopefully from this point on it is just adding bells and whistles (that stalk needs to be local, these valuations need to be jiggered by the whatsit).

#### [Scott Morrison (Sep 12 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133795050):
Happily, the category of presheaves is actually pretty easy to PR now. I only have one dependency, about whiskering, and that looks easy to clean up. So this may be in mathlib soon.

#### [Kenny Lau (Sep 12 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133837710):
> to reduce an `eq.rec` you need the major premise to become `refl` somehow

> that usually means finding the appropriate equality in the context and generalizing it until one side is a variable, and then `subst`, which is to say use `eq.rec` in the proof term

[Mario Carneiro, 16/04/2018 04:39:04 (UTC)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/so.20what.20is.20eq.2Erec.3F/near/125134372)

#### [Kenny Lau (Sep 12 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133837740):
underrated comment

#### [Kenny Lau (Sep 12 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133842645):
wow I had an `eq.rec` in my goal and it took me nearly 2 hours to destruct it

#### [Reid Barton (Sep 12 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133845614):
sounds about right

#### [Scott Morrison (Sep 13 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133856278):
I feel like `eq.rec` is such a disaster that we need special VS Code plugin support: a little zulip box that pops up, with a message: "Help me, Mario!" ready to be sent...

#### [Kenny Lau (Sep 13 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133866974):
ok so eq.rec isn't really the problem. The problem is sometimes you can't just rewrite something with an equality `a = b` because that something depends on `a` and `b` being those expressions. And the solution is to generalize `a` in all places in which that expression occurs, and then `subst` that equality

#### [Kenny Lau (Sep 13 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133866988):
sometimes you can't just generalize `a`, but you have to generalize a lot of things

#### [Kenny Lau (Sep 13 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133866989):
a strategy is to generalize all proofs first (`set_option pp.proofs true`), because that will always work because of proof irrelevance

#### [Scott Morrison (Sep 14 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent%20argument%20hell/near/133947991):
Slowly making progress here. This now compiles:
```
def stalks_local (F : Presheaf.{u+1 u} TopRing) : Type u :=
Π x : F, local_ring (((TopRing.forget_to_CommRing).map_presheaf F).stalk_at x)

def V_pre_pre := Σ (F : Presheaf.{u+1 u} TopRing), stalks_local F

example : category.{u+1 u} V_pre_pre := by unfold V_pre_pre; apply_instance
```

