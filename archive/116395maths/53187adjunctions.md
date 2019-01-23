---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/53187adjunctions.html
---

## Stream: [maths](index.html)
### Topic: [adjunctions](53187adjunctions.html)

---


{% raw %}
#### [ Johan Commelin (Nov 07 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146960106):
I feel like it is time we get adjoint functors. We now have `map` and `comap` for over-categories. They form an adjoint pair, and this would allow us to prove useful stuff. Has anyone given thought to implementing adjunctions in Lean? Are there any traps that should be avoided?

#### [ Kenny Lau (Nov 07 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146964831):
and then refactor galois connection :p

#### [ Johan Commelin (Nov 07 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146964958):
Right. Are you interested in taking a look at the bottom of `sheaf.lean` on the `sheaf` branch? It is getting a big mess. As soon as we want to apply category theory to concrete stuff thing become rather unpleasant...

#### [ Patrick Massot (Nov 07 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146965246):
I don't like reading "As soon as we want to apply category theory to concrete stuff thing become rather unpleasant..." :sad:

#### [ Johan Commelin (Nov 07 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146965311):
I agree... and it is probably just that I'm not skilled enough in Lean.

#### [ Johan Commelin (Nov 07 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146967027):
It feels like `category_theory` is a monad: You can bind yourself into it. But you really shouldn't try to crawl out of it.

#### [ Johan Commelin (Nov 07 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146967111):
I think it is hopeless that we will be able to rewrite along equivalences of categories, right?

#### [ Johan Commelin (Nov 07 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146967150):
If `X` is a topological space, and `U` is an open subset of `X`, then `over U` is canonically equivalent to `opens U`. Is there any hope at all that I can teach Lean how to use this fact?

#### [ Johan Commelin (Nov 07 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146967222):
(Without 100 lines of scaffolding to show that I can transfer everything I want along my canonical equivalence.)

#### [ Johan Commelin (Nov 07 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146967920):
In this case it is even an isomorphism of categories. I'm not sure if that helps.

#### [ Kevin Buzzard (Nov 07 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/146970541):
```quote
I think it is hopeless that we will be able to rewrite along equivalences of categories, right?
```
rofl how about we rewrite along isomorphisms of groups first!

#### [ Scott Morrison (Nov 07 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147252668):
:up:

#### [ Reid Barton (Nov 08 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147322759):
```quote
I feel like it is time we get adjoint functors. We now have `map` and `comap` for over-categories. They form an adjoint pair, and this would allow us to prove useful stuff. Has anyone given thought to implementing adjunctions in Lean? Are there any traps that should be avoided?
```
I have defined adjunctions a couple of times, including at https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/category_theory/adjunctions.lean (see also https://github.com/rwbarton/lean-homotopy-theory/blob/lean-3.4.1/src/category_theory/preserves_colimits.lean). But I haven't needed to push the theory very far yet, so I'm not sure about traps.

#### [ Reid Barton (Nov 08 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147322876):
One thing which is a bit annoying is to state the naturality of the isomorphism Hom(FX, Y) = Hom(X, GY) for an adjunction F : C -> D, G : D -> C.
If C and D have different morphism universes then where is this isomorphism happening...?

#### [ Johan Commelin (Nov 08 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147328898):
Probably in `max v_1 v_2`...

#### [ Johan Commelin (Nov 08 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147328931):
Maybe we can have an `adjunctions` branch where you push your stuff and we (Scott, you, me, maybe others) can play around with it till we think something is ready for merging.

#### [ Johan Commelin (Nov 08 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147328996):
For example, we could then merge that branch into the `sheaf` branch, and stress test it on that example.

#### [ Scott Morrison (Nov 08 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147333368):
When I've played with adjunctions I've settled on just putting everything in the same universe level.

#### [ Scott Morrison (Nov 08 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147333380):
Would this make us sad?

#### [ Reid Barton (Nov 08 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147335341):
I'm not sure. It might be fine, especially if we have a good interface for lifting a category to a bigger universe.

#### [ Kevin Buzzard (Nov 09 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147356768):
I know that the philosophy is to be maximally universe polymorphic. But when I wrote schemes originally I spent almost my entire time working in one universe, just to see what happened, and I never ran into any problems (other than Mario telling me I should stop -- I mean I didn't run into any mathematical problems). Reading SGA the other day I see that Grothendieck also was happy with just one universe for a lot of the time. If being maximally universe polymorphic is causing problems then I might venture to suggest that being maximally universe polymorphic might simply not be that good an idea when working with categories.

#### [ Johan Commelin (Nov 09 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147357592):
I do think that a lot of our universe annotations could then go away. And the errors related to universe issues are also quite nasty and annoying. I agree with @**Reid Barton** that we would need a good way to turn lift a category to a higher universe, and I have no idea how hard this is.
@**Scott Morrison|110087** What do you think? How much of the universe issues are maths-problems, and how much of it is just *users fighting Lean*?

#### [ Scott Morrison (Nov 10 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147411657):
I don't think we've had any universe problem in a long while in the category_theory development. I think the current setup, where you often have to say `XXX.{u v}`, so Lean knows which morphism universe level you intend, is mildly annoying. The current setup is a minimal envelope around supporting `category.{v v}` and `category.{v+1 v}`, which is all that ever turns up in practice. Any time more than one category is involved, and there is a potential problem with mismatching universe levels, my instinct is to put everything at the same universe level. (i.e., just like Grothendieck, we work in a single universe, called `v`, except that we also have `u`, which we think of as either being `v` or `v+1` for small or large categories).

#### [ Scott Morrison (Nov 10 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147411706):
If that ever causes problems, then we'll announce we've learnt something, and deal with it, but for now I see no need to deal with mixed-universe level adjunctions, etc.

#### [ Kevin Buzzard (Nov 10 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147411924):
I guess Grothendieck fixed one universe u, and then talked about u-categories and u-small categories, which are these two cases.

#### [ Scott Morrison (Nov 10 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147412697):
We would suffer quite a bit by specialising to only u-categories and u-small categories, because we'd have to duplicate lots of theorems. Having `category.{u v}` lets us state theorems in both cases uniformly with not-that-much suffering, and we just remember that all the other values of `u` are not particularly relevant.

#### [ Kevin Buzzard (Nov 10 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147425039):
Yes, I'm now starting to understand the philosophy much better

#### [ Reid Barton (Nov 12 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147503855):
Status update on adjunctions: I managed to get as far as proving that right adjoints preserve limits and that any functor C -> D with C small and D cocomplete induces an adjunction (like the geometric realization/Sing adjunction).

#### [ Reid Barton (Nov 12 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147503862):
The code still needs some cleaning up, but I'll try to push it to community tomorrow

#### [ Johan Commelin (Nov 12 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147509015):
@**Reid Barton** That sounds fantastic! I'm looking forward to seeing the code.

#### [ Reid Barton (Nov 12 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147548648):
https://github.com/leanprover-community/mathlib/tree/adjunctions

#### [ Johan Commelin (Nov 12 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147548937):
Cool!

#### [ Reid Barton (Nov 12 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147549367):
I'm still not sure about the best way to deal with natural isomorphisms. Sometimes I want to compose natural isomorphisms together, in which case I want to view the isomorphism and its naturality as a single object, but often I also want to just work objectwise, and check naturality as needed later

#### [ Reid Barton (Nov 12 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147549474):
I'm looking at this proof on paper: "$$\mathrm{Hom}(\tilde F (y c), d) = \mathrm{Hom}(y c, F^* d) = F^* d(c) = \mathrm{Hom}(F c, d)$$ and so there is a natural isomorphism $$F c \to \tilde F (y c)$$"

#### [ Reid Barton (Nov 12 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147549477):
and trying to figure out how to explain it to Lean

#### [ Johan Commelin (Nov 12 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147549682):
`apply yoneda_lemma; obviously` ??? :lol:

#### [ Reid Barton (Nov 12 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147553765):
@**Scott Morrison|110087** I left a bit of a mess in `limits.lean` regarding `is_limit.equiv`/`is_limit.of_equiv` and the colimit versions. I found it's often easier to just work with the `equiv` type, rather than `iso` and especially `iso` between natural transformations. In particular, `is_limit.of_equiv` is nontrivially (at least in Lean) harder to use than `is_colimit.of_equiv`--for `is_limit.of_equiv` you have to produce an inverse as a natural transformation, while the fact that it's natural is actually automatic.

#### [ Reid Barton (Nov 12 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147553773):
This should get sorted out somehow--maybe having both `equiv` and `iso` versions

#### [ Scott Morrison (Nov 12 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554813):
@**Reid Barton**, isn't this what `nat_iso.of_components` is for?

#### [ Scott Morrison (Nov 12 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554871):
You specify an iso in each component, and check naturality in just one direction.

#### [ Scott Morrison (Nov 12 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554885):
Perhaps there should be a companion that let's you check naturality in the other direction instead.

#### [ Reid Barton (Nov 12 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554886):
oh, I didn't see that

#### [ Scott Morrison (Nov 12 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554900):
Sorry, I really should write some docs. :-(

#### [ Reid Barton (Nov 12 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554902):
but anyways, I shouldn't need to check naturality in either direction

#### [ Scott Morrison (Nov 12 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554907):
Ah, why is that?

#### [ Reid Barton (Nov 12 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554951):
Well, because... I actually want to use something like `is_limit.of_extensions_iso`

#### [ Reid Barton (Nov 12 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147554969):
but `nat_iso.of_components` doesn't produce an `is_iso`

#### [ Reid Barton (Nov 12 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555016):
The point is just that the thing which is supposed to be `is_iso` is already known to be natural

#### [ Scott Morrison (Nov 12 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555021):
ah!

#### [ Scott Morrison (Nov 12 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555026):
okay, sorry, I missed that

#### [ Scott Morrison (Nov 12 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555051):
so we need is_iso.of_nat_trans, which takes an input an `F \natt G`,  and and is_iso for each component?

#### [ Scott Morrison (Nov 12 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555185):
Regarding your
> I'm looking at this proof on paper: "$$\mathrm{Hom}(\tilde F (y c), d) = \mathrm{Hom}(y c, F^* d) = F^* d(c) = \mathrm{Hom}(F c, d)$$ and so there is a natural isomorphism $$F c \to \tilde F (y c)$$"

It seems we'd want to write:
```
apply nat_iso.of_components, -- giving us two goals; an iso in each component, and naturality of the forward direction,
{ intro X,
  apply yoneda.ext,
  <<<calc block goes here, doing the Hom set calculation>>> },
obviously -- to deal with naturality
```

#### [ Scott Morrison (Nov 12 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555241):
I think a calc block should work fine with a string of isos.

#### [ Scott Morrison (Nov 12 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555247):
Because there compositions of isos is marked with `[trans]`.

#### [ Reid Barton (Nov 12 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555262):
There are actually two naturalities(?) involved: in c and in d

#### [ Reid Barton (Nov 12 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555280):
One of them gets consumed by `yoneda.ext`, the other to show the resulting transformation is natural in `c`

#### [ Scott Morrison (Nov 12 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555303):
oh, of course

#### [ Scott Morrison (Nov 12 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555361):
so after the `calc` block we'd have another `obviously` to discharge the naturality goal that `yoneda.ext` creates?

#### [ Scott Morrison (Nov 12 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555382):
I guess `yoneda.ext` and `nat_iso.of_components` could both have `obviously` as an autoparam...

#### [ Reid Barton (Nov 12 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555473):
Gotta run for a bit :running:

#### [ Scott Morrison (Nov 12 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147555483):
but that probably makes no sense; auto_param in a open argument of an applied function isn't going to help, because it should run until later...

#### [ Reid Barton (Nov 13 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147566939):
@**Scott Morrison|110087** We need that Globular integration already https://github.com/leanprover-community/mathlib/blob/adjunctions/category_theory/adjunction.lean#L156

#### [ Scott Morrison (Nov 13 2018 at 05:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147568567):
Yeah, I was wishing for globular yesterday as well. I ended up writing a page long rewrite proof, corresponding to a commutative diagram built out of two hexagons and two squares (but interminable rewriting along category.assoc to actually use it), corresponding to a string diagram in which you just had to pull some cups and caps past each other. (This was for composition of monoidal functors.)

#### [ Reid Barton (Nov 15 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147715738):
I can't believe this resulted in a statement I could actually prove
```lean
    dsimp [canonical_diagram.cocone, canonical_diagram.to_original, canonical_diagram,
      canonical_diagram.colimit_cocone, id_iso_yoneda_extension_yoneda,
      adjunction.nat_iso_equiv, adjunction.nat_trans_equiv,
      equiv.refl, equiv.symm, equiv.trans, iso.hom_equiv_of_isos,
      adjunction.mate, adjunction.nat_equiv, adjunction.nat_equiv',
      adjunction.hom_equiv, adjunction.id, adjunction.adjunction_of_equiv_left,
      adjunction.adjunction_of_equiv, adjunction.left_adjoint_of_equiv,
      yoneda_extension_adj, yoneda_extension_e,
      equiv.subtype_equiv_subtype, equiv.subtype_equiv_of_subtype, equiv.Pi_congr_right,
      equiv.arrow_congr,
      is_colimit.equiv,
      restricted_yoneda, yoneda_extension, yoneda_extension_obj,
      restricted_yoneda_yoneda_iso_id,
      nat_iso.of_components, iso_of_equiv, yoneda_equiv],
```

#### [ Kevin Buzzard (Nov 15 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147715886):
I look at that and I can see why category theory has a reputation in some quarters of just being a bunch of trivialities...

#### [ Scott Morrison (Nov 15 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147716433):
Sounds like more rfl lemmas were needed.

#### [ Reid Barton (Nov 17 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147853440):
@**Scott Morrison|110087** did you do a second force push to the adjunctions branch, or am I imagining things?

#### [ Scott Morrison (Nov 17 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147853442):
Oh, maybe I did. Sorry, did I mess things up? :-(

#### [ Reid Barton (Nov 17 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147853526):
No not really, but give me a heads up if you do a force push in the future, as it's easier to deal with if I know about it earlier

#### [ Reid Barton (Nov 17 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147853596):
I managed to prove that the category of colimit-preserving functors Set^C^op -> D is equivalent to the category of functors C -> D

#### [ Reid Barton (Nov 17 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147853606):
for D cocomplete of course

#### [ Reid Barton (Nov 17 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147853610):
though I'm not particularly happy with the proof yet

#### [ Reid Barton (Nov 17 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147853633):
It turns out there are a lot of statements to check there...

#### [ Reid Barton (Nov 17 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/147853740):
I guess I also proved the "adjoint functor theorem" for such functors, along the way

#### [ Johan Commelin (Nov 26 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/148386153):
@**Reid Barton** Shouldn't the `left_triangle` and `right_triangle` fields in adjunction get `obviously` auto_param? (I can testify that `obviously` will prove them in the case of `comap f` and `map f` between `presheaf X` and `presheaf Y`.

#### [ Johan Commelin (Nov 26 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/148386577):
This is really slick:
```lean
def adj : adjunction (comap f) (map f) :=
{ unit   := unit f,
  counit := counit f,
  left_triangle  := by tidy,
  right_triangle := by tidy }

instance comap.preserves_colimits : preserves_colimits (comap f) :=
adjunction.left_adjoint_preserves_colimits (adj f)
```

#### [ Reid Barton (Nov 26 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/148386603):
I suppose, though I think that defining adjunctions in terms of the unit and counit was actually the wrong idea in the first place

#### [ Johan Commelin (Nov 26 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/148389931):
@**Reid Barton**  Does that mean that I shouldn't try to apply this on my sheaf branch?

#### [ Reid Barton (Nov 26 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/148394873):
Using the adjunctions branch as-is should be fine for now--I don't expect you will need to make major changes later. And more users of the code is good for trying out different designs.

#### [ Johan Commelin (Jan 17 2019 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155331480):
I've been experimenting a bit with adjunctions. Here is a little teaser:
```lean
def discrete : Type u ⥤ Top.{u} :=
{ obj := λ X, ⟨X, ⊤⟩,
  map := λ X Y f, ⟨f, continuous_top⟩ }

def trivial : Type u ⥤ Top.{u} :=
{ obj := λ X, ⟨X, ⊥⟩,
  map := λ X Y f, ⟨f, continuous_bot⟩ }

def adj₁ : adjunction discrete forget :=
{ hom_equiv := λ X Y,
  { to_fun := λ f, f,
    inv_fun := λ f, ⟨f, continuous_top⟩,
    left_inv := by tidy,
    right_inv := by tidy },
  unit := { app := λ X, id },
  counit := { app := λ X, ⟨id, continuous_top⟩ } }

def adj₂ : adjunction forget trivial :=
{ hom_equiv := λ X Y,
  { to_fun := λ f, ⟨f, continuous_bot⟩,
    inv_fun := λ f, f,
    left_inv := by tidy,
    right_inv := by tidy },
  unit := { app := λ X, ⟨id, continuous_bot⟩ },
  counit := { app := λ X, id } }
```

#### [ Johan Commelin (Jan 17 2019 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155331490):
Code can be found on the `adjunctions-2` branch.

#### [ Johan Commelin (Jan 17 2019 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155331619):
Observations made by Reid:
 * It is nice if we can have adjunctions between functors `F : C => D` and `G : D => C` where `C` and `D` don't need to live in the same universe.
 * We should learn from the `metric_space` hierarchy, and add redundant data in our definitions, with conditions that they are compatible.

#### [ Johan Commelin (Jan 17 2019 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155331719):
So now there are 3 ways to define an adjunction (with the help of `obviously` :smiley:).
 1. Like I did above: you specify `hom_equiv`, `unit` and `counit`.
 2. You only give `hom_equiv`.
 3. You only give `unit` and `counit`.
Here are two helper structures:
```lean
structure adjunction.core_hom_equiv (F : C ⥤ D) (G : D ⥤ C) :=
(hom_equiv : Π (X Y), (F.obj X ⟶ Y) ≃ (X ⟶ G.obj Y))
(hom_equiv_naturality_left' : Π {X' X Y} (f : X' ⟶ X) (g : F.obj X ⟶ Y),
  (hom_equiv X' Y) (F.map f ≫ g) = f ≫ (hom_equiv X Y) g . obviously)
(hom_equiv_naturality_right' : Π {X Y Y'} (f : F.obj X ⟶ Y) (g : Y ⟶ Y'),
  (hom_equiv X Y') (f ≫ g) = (hom_equiv X Y) f ≫ G.map g . obviously)
```
and
```lean
structure adjunction.core_unit_counit (F : C ⥤ D) (G : D ⥤ C) :=
(unit : functor.id C ⟹ F.comp G)
(counit : G.comp F ⟹ functor.id D)
(left_triangle' : (whisker_right unit F).vcomp (whisker_left F counit) = nat_trans.id _ . obviously)
(right_triangle' : (whisker_left G unit).vcomp (whisker_right counit G) = nat_trans.id _ . obviously)
```

#### [ Johan Commelin (Jan 17 2019 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155331737):
We then have
```lean
/--
`adjunction F G` represents the data of an adjunction between two functors
`F : C ⥤ D` and `G : D ⥤ C`. `F` is the left adjoint and `G` is the right adjoint.
-/
structure adjunction (F : C ⥤ D) (G : D ⥤ C) extends
  (adjunction.core_hom_equiv F G), (adjunction.core_unit_counit F G) :=
(unit_hom_equiv : Π {X}, unit.app X = (hom_equiv _ _).to_fun (𝟙 (F.obj X)) . obviously)
(counit_hom_equiv : Π {Y}, counit.app Y = (hom_equiv _ _).inv_fun (𝟙 (G.obj Y)) . obviously)
```

#### [ Johan Commelin (Jan 17 2019 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155331794):
And finally
```lean
def of_core_hom_equiv (adj : core_hom_equiv F G) : adjunction F G := -- see github for the code
def of_core_unit_counit (adj : core_unit_counit F G) : adjunction F G := -- see github for the code
```

#### [ Patrick Massot (Jan 17 2019 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155344034):
It looks very nice, except that it could look much nicer. Did you miss https://github.com/leanprover/lean/commit/95fa4cfb0a8774570d67bb231c1ab088a94e12bb#diff-50f7eff1a2547545a820cbbeee3a0b6eL15 ?

#### [ Johan Commelin (Jan 17 2019 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155344144):
Yes, I guess we should quickly make a PR that uses the correct functor symbol

#### [ Johan Commelin (Jan 17 2019 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155356649):
There is one drawback that I currently see with my approach. If the categories `C` and `D` do live in the same universe, then we can extract an isomorphism between the two Hom-bifunctors from the adjunction. We can also define an adjunction given such a natural isomorphism `i`. But the extracted isomorphism will not be defeq to `i`.

#### [ Johan Commelin (Jan 17 2019 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/155356679):
I do not see how to fix this if we also want to keep the option of adjunctions for different universe levels.

#### [ Johan Commelin (Jan 22 2019 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156608839):
Here is a slightly non-trivial example of a Lean checked adjunction:
```lean
section
open mv_polynomial
local attribute [instance, priority 0] subtype.fintype set_fintype classical.prop_decidable

noncomputable def polynomial : Type u ⥤ CommRing.{u} :=
{ obj := λ α, ⟨mv_polynomial α ℤ, by apply_instance⟩,
  map := λ α β f, ⟨eval₂ C (X ∘ f), by apply_instance⟩,
  map_id' := λ α, subtype.ext.mpr $ funext $ eval₂_eta,
  map_comp' := λ α β γ f g, subtype.ext.mpr $ funext $ λ p,
  by apply mv_polynomial.induction_on p; intros;
    simp only [*, eval₂_add, eval₂_mul, eval₂_C, eval₂_X, comp_val,
      eq_self_iff_true, function.comp_app, types_comp] at * }

@[simp] lemma polynomial_obj_α {α : Type u} :
  (polynomial.obj α).α = mv_polynomial α ℤ := rfl

@[simp] lemma polynomial_map_val {α β : Type u} {f : α → β} :
  (polynomial.map f).val = eval₂ C (X ∘ f) := rfl

noncomputable def adj : adjunction polynomial (forget : CommRing ⥤ Type u) :=
adjunction.mk_of_hom_equiv _ _
{ hom_equiv := λ α R,
  { to_fun := λ f, f ∘ X,
    inv_fun := λ f, ⟨eval₂ int.cast f, by apply_instance⟩,
    left_inv := λ f, subtype.ext.mpr $ funext $ λ p,
    begin
      have H0 := λ n, (congr (int.eq_cast' (f.val ∘ C)) (rfl : n = n)).symm,
      have H1 := λ p₁ p₂, (@is_ring_hom.map_add _ _ _ _ f.val f.2 p₁ p₂).symm,
      have H2 := λ p₁ p₂, (@is_ring_hom.map_mul _ _ _ _ f.val f.2 p₁ p₂).symm,
      apply mv_polynomial.induction_on p; intros;
      simp only [*, eval₂_add, eval₂_mul, eval₂_C, eval₂_X,
        eq_self_iff_true, function.comp_app, hom_coe_app] at *
    end,
    right_inv := by tidy },
  hom_equiv_naturality_left_symm' := λ X' X Y f g, subtype.ext.mpr $ funext $ λ p,
  begin
    apply mv_polynomial.induction_on p; intros;
    simp only [*, eval₂_mul, eval₂_add, eval₂_C, eval₂_X,
      comp_val, equiv.coe_fn_symm_mk, hom_coe_app, polynomial_map_val,
      eq_self_iff_true, function.comp_app, add_right_inj, types_comp] at *
  end }

end
```

#### [ Johan Commelin (Jan 22 2019 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156608907):
For some reason this code is slower than I would have hoped. And as you can see there is quite a bit of `mv_polynomial.induction_on p`, so I think there are some lemmas that could be factored out...

#### [ Reid Barton (Jan 22 2019 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156608934):
When I was working on adjunctions I gave up on precisely this because everything was so slow

#### [ Johan Commelin (Jan 22 2019 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609025):
Somehow that doesn't feel like a good sign.

#### [ Reid Barton (Jan 22 2019 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609062):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/my_polynomial.20performance/near/147887874

#### [ Johan Commelin (Jan 22 2019 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609169):
Aah, I see.

#### [ Johan Commelin (Jan 22 2019 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609366):
I just pushed.

#### [ Patrick Massot (Jan 22 2019 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609404):
Is this `obviously` being slow of `mv_polynomial`?

#### [ Johan Commelin (Jan 22 2019 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609443):
```
rings.lean:115:18: information

parsing took 41.6ms
rings.lean:115:18: information

elaboration of adj took 15.2s
rings.lean:115:18: information

type checking of adj took 18.7ms
rings.lean:115:18: information

decl post-processing of adj took 17.5ms
```

#### [ Johan Commelin (Jan 22 2019 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609454):
No, I think it's `mv_polynomial`

#### [ Johan Commelin (Jan 22 2019 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609524):
Also:
```
rings.lean:100:18: information

parsing took 7.51ms
rings.lean:100:18: information

elaboration of polynomial took 4.11s
rings.lean:100:18: information

type checking of polynomial took 15.8ms
rings.lean:100:18: information

decl post-processing of polynomial took 15.3ms
```

#### [ Johan Commelin (Jan 22 2019 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609545):
And there is no `obviously` in
```lean
noncomputable def polynomial : Type u ⥤ CommRing.{u} :=
{ obj := λ α, ⟨mv_polynomial α ℤ, by apply_instance⟩,
  map := λ α β f, ⟨eval₂ C (X ∘ f), by apply_instance⟩,
  map_id' := λ α, subtype.ext.mpr $ funext $ eval₂_eta,
  map_comp' := λ α β γ f g, subtype.ext.mpr $ funext $ λ p,
  by apply mv_polynomial.induction_on p; intros;
    simp only [*, eval₂_add, eval₂_mul, eval₂_C, eval₂_X, comp_val,
      eq_self_iff_true, function.comp_app, types_comp] at * }
```

#### [ Johan Commelin (Jan 22 2019 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609647):
@**Johannes Hölzl** @**Kenny Lau** @**Mario Carneiro** Is there anything that can be done here? I guess lots of the stuff that we plan on doing will depend on `mv_polynomial`. All the number theory that Kevin and Sander are interested in will need it.

#### [ Patrick Massot (Jan 22 2019 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609654):
What happens if you sorry the last proof?

#### [ Johan Commelin (Jan 22 2019 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609771):
Then it drops from 4s to 1s.

#### [ Kenny Lau (Jan 22 2019 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609780):
Stuff involving mv_polynomial and polynomial have been known to be slow.

#### [ Kenny Lau (Jan 22 2019 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609783):
I don't think @**Mario Carneiro** knows how to fix it.

#### [ Johan Commelin (Jan 22 2019 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156609862):
@**Patrick Massot** It spends 638ms in the second `by apply_instance`.

#### [ Johan Commelin (Jan 22 2019 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610033):
The last `begin`-`end` block in `adj` takes 10 seconds :scream:

#### [ Reid Barton (Jan 22 2019 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610251):
do you really need to `simp at *`?

#### [ Johan Commelin (Jan 22 2019 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610303):
Yes, some of the goals need that.

#### [ Reid Barton (Jan 22 2019 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610418):
I mean maybe you can do something more than `simp` but less than `at *`

#### [ Reid Barton (Jan 22 2019 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610450):
e.g. explicitly say where to simp

#### [ Johan Commelin (Jan 22 2019 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610592):
Aah, ok. But the context is very small, and I guess `simp` will fail quickly on atomic hypotheses...

#### [ Johan Commelin (Jan 22 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610713):
Also, the places where I want to simplify are introduced by `intros`, and what gets intro'd depends on the goal.

#### [ Johan Commelin (Jan 22 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610722):
The induction step generates 3 goals.

#### [ Johan Commelin (Jan 22 2019 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/adjunctions/near/156610749):
So if I want to be explicit in the `simp`-part, I need to tackle the 3 goals separately...


{% endraw %}
