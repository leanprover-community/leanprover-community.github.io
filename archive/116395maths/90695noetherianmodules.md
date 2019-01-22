---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/90695noetherianmodules.html
---

## [maths](index.html)
### [noetherian modules](90695noetherianmodules.html)

#### [Johan Commelin (Aug 31 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133118514):
What are the next steps for noetherian modules?
1. We want to prove that if `M` is noetherian, then so are all its submodules and quotients.
2. This suggests that we might quickly want `is_noetherian` to be a class.
3. To prove (1) we want to show that a linear map `M -> N` induces an order preserving map `submodule R M -> submodule R N`.

#### [Johan Commelin (Aug 31 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133118538):
The map induced map in (3) is injective if `M -> N` is an inclusion or quotient map.

#### [Johan Commelin (Aug 31 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133118680):
Is this induced map an example of (one side of) a Galois connection? And is it useful to know this?

#### [Reid Barton (Aug 31 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133118845):
There are actually three maps forming two Galois connections I think

#### [Johan Commelin (Aug 31 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133118894):
Taking image, taking inverse image, and ...?

#### [Reid Barton (Aug 31 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133118898):
Whatever the right adjoint to the inverse image is

#### [Reid Barton (Aug 31 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133118913):
The biggest submodule whose inverse image is contained in the original one

#### [Reid Barton (Aug 31 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133118914):
I guess it's not useful

#### [Johan Commelin (Aug 31 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133118961):
Right, so you have `N' \sub N`, and then you'dd take the image of `f^{-1} N' \cap M`?

#### [Johan Commelin (Aug 31 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133118970):
Scratch that, that's nonsense

#### [Reid Barton (Aug 31 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133118972):
Start with a submodule of M

#### [Johan Commelin (Aug 31 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133118973):
Right,

#### [Johan Commelin (Aug 31 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133118985):
Call it `M'`, and put `\cap M'` in my formula

#### [Reid Barton (Aug 31 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133119032):
It's those n whose inverse image is a subset of M'. I think

#### [Reid Barton (Aug 31 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133119101):
You have it for just a map of sets also.

#### [Reid Barton (Aug 31 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133119112):
It has a forall where the direct image has an exists

#### [Johannes Hölzl (Aug 31 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133119129):
Yeah, sets and filters also have this strange right adjoint to preimage. I don't know if this is useful anywhere...

#### [Reid Barton (Aug 31 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133119132):
Actually, now I think it doesn't exist for submodules

#### [Reid Barton (Aug 31 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133119136):
Because the inverse image of zero might not be zero

#### [Reid Barton (Aug 31 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133119191):
So the inverse image map doesn't preserve the empty sup

#### [Reid Barton (Aug 31 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133119199):
So it can't have a right adjoint

#### [Reid Barton (Aug 31 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133119239):
So ignore everything I said.

#### [Reid Barton (Aug 31 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133119288):
Direct and inverse image of submodules should be a Galois connection though

#### [Johan Commelin (Aug 31 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133119325):
Right, and I guess this is a general fact about subobjects in algebraic concrete categories...

#### [Johan Commelin (Aug 31 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133119344):
So it would be cool if we could either deduce it from such a general fact, or have a subtype_galois_connection tactic (-;

#### [Reid Barton (Aug 31 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133119826):
I guess we can start with the complete lattice of subobjects tactic and the span Galois insertion tactic

#### [Johannes Hölzl (Aug 31 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133119930):
A `galois_connection` tactic would be nice, but I don't see how it should work. To prove that something is free (e.g. `span`, `generator` etc) is not for free.

#### [Johan Commelin (Aug 31 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133119980):
No, I didn't mean that one. I meant the direct/inverse image connection.

#### [Johan Commelin (Aug 31 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133119990):
That one is usually just a follow-your-nose result.

#### [Reid Barton (Aug 31 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133120085):
You can take the intersection of all the subobjects which contain the given set. Basically get the complete lattice structure from the intersection instead

#### [Reid Barton (Aug 31 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133120098):
But then in a particular case, you will probably want a more explicit description of the generated subobject.

#### [Johan Commelin (Aug 31 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133120107):
Mario would say that we shouldn't automate this, but just go for it (-;

#### [Reid Barton (Aug 31 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133120164):
Does the subobject instance tactic work for R-modules? Does it understand that the structure is `module R`?

#### [Johan Commelin (Aug 31 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133120248):
this instance is already in mathlib

#### [Johan Commelin (Aug 31 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133120255):
I didn't test the tactic, because that is not yet in mathlib

#### [Johan Commelin (Aug 31 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133120260):
`linear_algebra.subtype_module`

#### [Mario Carneiro (Aug 31 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133120467):
```quote
A `galois_connection` tactic would be nice, but I don't see how it should work. To prove that something is free (e.g. `span`, `generator` etc) is not for free.
```
`span` is not free when presented in a "constructive" way, i.e. linear combinations of elements in the set, but it is free given the Moore collection axioms. A Moore collection is a set of sets that is closed under arbitrary intersection (let's call these things closed sets). This enables the definition of a closure operator that is the span (i.e. the intersection of all closed sets containing S), and then there is some work to show that this operator has a constructive interpretation using an inductive family or what have you. Any algebraically presented subobject family like `is_subgroup` or `is_submodule`, where the assumptions all say "if these things are in the subgroup then these other things are in the subgroup", is a Moore collection, and there is a formulaic proof of such.

#### [Mario Carneiro (Aug 31 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133120573):
This approach seems like a way to automate this, but it does not go via the galois connection, since that approach brings in the details of the constructive definition of span (here I mean constructive in the mathematician's sense) which are not as uniform

#### [Reid Barton (Aug 31 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133120680):
Right so there are three definitions of, say, the submodule of M generated by a set S.

#### [Reid Barton (Aug 31 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133120688):
1 is the intersection of the submodules containing S.

#### [Mario Carneiro (Aug 31 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133120743):
If a Moore collection is generated by the closure with respect to a (possibly infinite) family of finite arity operators, then it is an algebraic closure system (ACS), which has still more properties for free. Almost all of the algebraic sub-things are ACSs

#### [Reid Barton (Aug 31 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133120754):
2 is the set of elements which can be built up from S from the operations of a module, i.e., we define an inductive type of trees which are expressions in the language of R-modules.

#### [Reid Barton (Aug 31 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133120770):
3 is the one in terms of linear combinations.

#### [Mario Carneiro (Aug 31 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133120779):
(2) seems like an inductive definition that is amenable to automation in the same sense as I have suggested

#### [Reid Barton (Aug 31 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133120790):
1 and 2 are automatable. 3 is not, you have to think of something which is a good "normal form" (roughly) and then prove a special theorem.

#### [Reid Barton (Aug 31 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133121139):
I guess it probably doesn't matter much which definition we choose or whether the definitions are consistent between different kinds of structures

#### [Mario Carneiro (Aug 31 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133121298):
If we want a one-line setup of the collection, the complete lattice, the span operator and the galois connection, it would be best to take one of the uniform versions as the definition, and leave the nonuniform version as a theorem to be proven separately

#### [Reid Barton (Aug 31 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133121315):
I should look into this Moore system stuff. It sounds related to locally presentable categories (a locally finitely presentable category is the category of models of a finitary essentially algebraic theory) and there are some theorems about subobjects in them, though usually I don't care so much about those theorems.

#### [Mario Carneiro (Aug 31 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133121395):
I learned about it first through metamath, see http://us.metamath.org/mpeuni/df-mre.html and http://us.metamath.org/mpeuni/df-acs.html which have some links to references. Wikipedia doesn't seem to have anything on it

#### [Johannes Hölzl (Aug 31 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133121603):
Yeah, I should have looked into them the first time you mentioned them. I like the Examples section in https://ncatlab.org/nlab/show/Moore+closure :
> What are examples? Better to ask what isn't an example!

#### [Reid Barton (Aug 31 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133121936):
I see, so it looks a lot more general than subobjects in an algebraic theory.

#### [Mario Carneiro (Aug 31 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133122067):
oh, looks like the WP reference is https://en.wikipedia.org/wiki/Closure_operator

#### [Mario Carneiro (Aug 31 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133122126):
"finitary closure operator" in that article corresponds to what I called an ACS

#### [Scott Morrison (Sep 01 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133170533):
Does anyone know why the noetherian branch isn't compiling?

#### [Scott Morrison (Sep 01 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133170579):
@**Chris Hughes**, @**Kenny Lau**, what are the prospects of getting tensor products of commutative rings into mathlib?

#### [Kenny Lau (Sep 01 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133170588):
I wrote [half the file](https://github.com/kckennylau/Lean/blob/master/constructive_tensor_product.lean) a month ago

#### [Patrick Massot (Sep 01 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133170789):
`is_add_group_hom` is now in mathlib

#### [Patrick Massot (Sep 01 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133170840):
https://github.com/leanprover/mathlib/commit/afd1c063638d611fda65db7499ccbd7257c90870

#### [Patrick Massot (Sep 01 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133170878):
What is the current state of quotient groups by the way?

#### [Chris Hughes (Sep 01 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133171270):
Kevin's stuff got merged. There's about 100 lines of the basic facts.

#### [Scott Morrison (Sep 01 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133171274):
@**Chris Hughes** can you point me to it?

#### [Patrick Massot (Sep 01 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133171276):
I was thinking of the `left_cosets` vs `group_quotient` issue

#### [Patrick Massot (Sep 01 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133171277):
I think we have two competing versions

#### [Chris Hughes (Sep 01 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133171317):
Everything's `quotient_group.quotient` now.

#### [Patrick Massot (Sep 01 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133171323):
left_cosets disappeared?

#### [Chris Hughes (Sep 01 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133171326):
Yes.

#### [Patrick Massot (Sep 01 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133171328):
That's good news, but again something to be changed in Kenny's tensor product file

#### [Chris Hughes (Sep 01 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133171330):
but `quotient_group` includes quotient by non normal subgroups

#### [Chris Hughes (Sep 01 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133171337):
@**Scott Morrison** It's in `group_theory/quotient_group`

#### [Scott Morrison (Sep 01 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133171396):
@**Chris Hughes**, oh, oops, I thought you were talking about tensor products of rings. :-)

#### [Patrick Massot (Sep 01 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133171400):
couldn't we call this `group.quotient` instead of `quotient_group`? The later really looks like the quotient is a group

#### [Scott Morrison (Sep 01 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133171401):
@**Kenny Lau**, are you going to PR that stuff on tensor products? I'd like to be able to use it!

#### [Chris Hughes (Sep 01 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133171490):
I think `group.quotient` is a better name.

#### [Kenny Lau (Sep 01 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133176767):
```quote
@**Kenny Lau**, are you going to PR that stuff on tensor products? I'd like to be able to use it!
```
give me some time

#### [Kenny Lau (Sep 02 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133213796):
Tensor product PR: https://github.com/leanprover/mathlib/pull/303

#### [Kenny Lau (Sep 02 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133213797):
@**Scott Morrison** further feature request?

#### [Kenny Lau (Sep 02 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133213799):
@**Patrick Massot** you might be interested

#### [Patrick Massot (Sep 02 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133214450):
thanks Kenny!

#### [Patrick Massot (Sep 02 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133223691):
Kenny's tensor product is merged! I'm really super excited by the idea of mathlib taking advantage of Kenny's proving power!

#### [Kevin Buzzard (Sep 02 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133223768):
rofl I was reviewing it

#### [Kenny Lau (Sep 02 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133223774):
it's alright Kevin, I may still have things to add there anyway

#### [Kenny Lau (Sep 02 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133223784):
I may prove the dimension theorem, and then I would prove that the dimension of tensor is the product of the dimension

#### [Johannes Hölzl (Sep 02 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133223945):
@**Kevin Buzzard** was I too fast merging it? Any suggestions?

#### [Kevin Buzzard (Sep 02 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133223956):
nothing serious. I'll finish my review. I am trying to get into the habit of reviewing mathlib PRs where the mathematics relates to the perfectoid project.

#### [Kevin Buzzard (Sep 04 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133338778):
@**Mario Carneiro** just to let you know I am still working on the Noetherian branch of  community mathlib. I have a proof that subs and quotients of Noeth are Noeth but it's currently broken as I fiddle with it to try and make things more general and reasonable. I'm sure there will still be lots of work to do when I finally make the PR, hopefully tomorrow. Admin got the better of me today, that and the fact that I kept having little insights about how to do things a little better than they were done before.

#### [Kevin Buzzard (Sep 05 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/noetherian%20modules/near/133368044):
OK so I pushed the proof that a sub of a Noetherian module is Noetherian to community-mathlib, the Noetherian branch. I spent some time proving order embeddings which I could have probably avoided. I'd appreciate any feedback on the push. Am I supposed to open a PR to mathlib? I have littered my PR with comments, which of course will have to go in the end, but they're just to flag things I wasn't sure about or to explain what I was trying to do.

I also have a proof that quotients of Noetherian modules are Noetherian, but I was waiting for Chris' quotient module PR to be accepted -- I see that it was accepted an hour ago so I'll work on quotient modules later.

