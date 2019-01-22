---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/97723modulerefactoring.html
---

## [general](index.html)
### [module refactoring](97723modulerefactoring.html)

#### [Mario Carneiro (Sep 21 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134359525):
I'm a bit late for my birthday deadline, but I have enough of the refactoring done that I'm ready to get feedback on it. See [leanprover-community/module](https://github.com/leanprover/mathlib/compare/master...leanprover-community:module). Remarks:

* The main contributions here are the complete bundling of `linear_map` and `submodule`. In fact both of these were already present in mathlib, but making them primary makes everything go so much smoother.
* The structure of `submodule` and its category-theory-like interactions with `linear_map` are emphasized heavily. In particular, `submodule` is a complete lattice, `map` and `comap` are galois connections, there are tons of theorems about the map of an inf or the comap of fst and so on.
* The amount of duality here is staggering. I guess someone who is category theory minded will tell me that Mod is its own opposite category or some such thing, but it really shows in the equational theory. Even stuff like `inl` being dual to `fst` causes some nice properties, and some stuff plays even nicer than on Set like `prod p q ⊔ prod p' q' = prod (p ⊔ p') (q ⊔ q')`.
* Injectivity and surjectivity of linear maps is expressed through `ker` and `range` (should I call it `im`?), and even `linear_independent` and `basis` can be expressed using properties of the `lc.total` function.

On the whole, I'm feeling really good about the results, and the proofs are much cleaner.

#### [Johan Commelin (Sep 21 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134359600):
This is really cool! And yes, please call use `im` :lol:

#### [Mario Carneiro (Sep 21 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134359655):
The name `range` is of course borrowed from terminology on `set`. I would rather not confuse with `image` which is `map` here

#### [Mario Carneiro (Sep 21 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134359741):
`map f p` is the submodule `f[p]` where `p` is a submodule, and `range f = map f \top = f[univ]` which was previously called `im` on linear maps

#### [Mario Carneiro (Sep 21 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134359814):
What is the common name for the coproduct pairing function? I called it [`copair`](https://github.com/leanprover-community/mathlib/blob/45f72059515083a0ae74567432dfc7853f791235/linear_algebra/basic.lean#L113-L114) since `pair` is used for the product pairing operation

#### [Kenny Lau (Sep 21 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134360028):
but it's the same...

#### [Johan Commelin (Sep 21 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134360049):
I think @**Scott Morrison|110087**  and @**Reid Barton** have the most experience with such decisions

#### [Johannes Hölzl (Sep 21 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134363426):
this is really nice!

#### [Patrick Massot (Sep 21 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134364133):
Mario, could you explain how all this solves the trouble we had with instance loops and multiple possible base rings?

#### [Kevin Buzzard (Sep 21 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134370222):
I got caught up with something else this morning but later on today, when I have Lean time, I will just merge the patch and see how Hilbert basis goes with it. Does it compile sorry-free?

#### [Reid Barton (Sep 21 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134370418):
`copair`/`pair` seems as good as anything else.
Normally we just write an arrow $$A \oplus B \to C$$ and let the reader do the boring work of figuring out what map we are actually talking about.

#### [Kenny Lau (Sep 21 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134370446):
how about product or coproduct as a bifunctor?

#### [Mario Carneiro (Sep 21 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134388143):
@**Patrick Massot**  This doesn't address that issue, although it prepares the way a bit. I anticipate that this should be a comparatively simple change, but I didn't want the two refactorings to interact so I'm going to start on it as soon as this is done.

#### [Mario Carneiro (Sep 21 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134388211):
@**Kevin Buzzard** It's not yet building. I finished the main linear algebra files, but I haven't finished up the cleanup of uses outside linear algebra. (There are no sorries, it just breaks.)

#### [Johannes Hölzl (Sep 21 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134388442):
@**Mario Carneiro** by the way: the introduction of `coe` rewrites broke some proofs in `set_theory/ordinal` and `cofinality`. I fixed this, but you might want to do a different fix

#### [Mario Carneiro (Sep 21 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134389089):
yeah, apologies for pushing stuff last night that broke things; my computer was running very slow and I was lacking feedback on whether my fixes worked

#### [Johannes Hölzl (Sep 21 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134389417):
No problem. But I'm not sure if these are the intended changes. I didn't look too deep how these new simp rules are supposed to work.

#### [Mario Carneiro (Sep 21 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134389493):
The idea is that `coe` will infer transitive instances, but since simp rules are only written on single coercions they won't fire on these composite instances. So we unfold them to multiple coe arrows first

#### [Mario Carneiro (Sep 21 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134389521):
I don't think I realized this until lately, but lean will also infer transitive instances for `coe` + `coe_fn` and `coe` + `coe_sort`, and since the instances are different there are more simp lemmas associated to these

#### [Mario Carneiro (Sep 21 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134389602):
I think the breakage is because some simp LHSs were written with composite instances, which now break because simp normal form doesn't have any composite instances. The fix is to make sure simp LHSs have multiple coercion in these cases

#### [Patrick Massot (Sep 21 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134390066):
Ok, I'm less confused then (about modules, I'm still 100% confused about topological groups). I couldn't understand how those changes could help with the lost ring issue

#### [Chris Hughes (Sep 21 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134390560):
Is it worth bundling ideals and subgroups as well?

#### [Johannes Hölzl (Sep 21 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134391051):
I think we should replace ideals by submodules, so yes we want to have them bundled. I'm not sure about subgroups. We surely want a bundled version, but maybe still an unbundled one too

#### [Kevin Buzzard (Sep 21 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134392526):
Johannes -- the idea about ideals was that submodule R M makes sense for varying R and M, but ideal R = submodule R R so only one input is needed.

#### [Chris Hughes (Sep 21 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134392890):
But I think you want lattice and semiring on ideals as well, so you need bundles for that.

#### [Mario Carneiro (Sep 21 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134396604):
I am of the opinion that `subgroup` and other such algebraic classes should also be bundled; almost all of the lattice structure theorems done here hold for anything that fits the structure of a universal algebra. `ideal R := submodule R R` can be defined as reducible so that all the theorems about submodules still apply.

#### [Mario Carneiro (Sep 21 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134396657):
What are some examples where you think not having `is_sub*` will cause problems?

#### [Johan Commelin (Sep 21 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134403252):
```quote
`ideal R := submodule R R` can be defined as reducible so that all the theorems about submodules still apply.
```
@**Mario Carneiro**  I thought you said in Orsay that you couldn't think of any reason why a definition should be reducible. Has that changed? If so, can you explain?

#### [Kevin Buzzard (Sep 22 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134412301):
If I open polynomial.lean (which I need for Hilbert basis) I just get 1000 errors. I think I would be happier to give feedback by trying to write Lean code and then getting stuck or finding things easier than before and reporting back. I find it hard to theorise about changes that I may not fully understand.

#### [Mario Carneiro (Sep 22 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134414013):
Yeah, sorry about that. Mostly you can just open and read `algebra.module` and `linear_algebra.basic` for now. I'll let you know when it's really done (by pushing it to `master`, unless someone objects)

#### [Mario Carneiro (Sep 22 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134414027):
I just didn't want to get too far afield with a change this sweeping without some input

#### [Mario Carneiro (Sep 22 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134414217):
@**Johan Commelin** That's a fair point. There are three options here: (1) nonreducible def (2) reducible def (3) notation. In Orsay I argued that either (1) or (3) suffices in most cases where you think you want (2).

In this case, I don't think it matters too much, although (1) will require copying some instances like the `complete_lattice` instance, and possibly some theorems. Doing this would make the cleanest separation, allowing us to present a solid API for ideals that doesn't talk about modules half the time. (2) and (3) will entail some amount of API leakage here, moreso with (3) since it is `submodule R R` that will appear in all your statements. 

The downsides of reducible defs (inconsistent handling in rw and simp) don't really apply when the def is a type since you don't usually do rewrites on a type, you just force it to be defeq to something else.

#### [Mario Carneiro (Sep 28 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134781266):
This is a change I haven't implemented, but I'm considering it and want to get some feedback. Maybe a basis should be an injective function from some type into the module, i.e. the "basis" is really the range of this function, and the function gets to pick its indexing type. The reason is because we often tend to use a basis as an index for a sum, or as the domain of the free vector space to which to express isomorphism, or as the set whose cardinality is the dimension of the space - all of these roles are better accommodated by having an algebra of indexing types (which we already have courtesy of DTT) where measuring cardinality and indexing is more natural. (Also, it allows a basis to carry computational content, which isn't super important but indicates that this might be moving in the right direction.)

#### [Reid Barton (Sep 28 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134781707):
From a mathematical perspective this change is very natural. We often write things like "let {b_1, ..., b_n} be a basis of V" but usually (whether we are aware of it or not) we really mean we are working with an indexed collection b_i, i.e., a function {1, ..., n} -> V.

#### [Reid Barton (Sep 28 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134781777):
It's easy to say things which are false if taken literally in the "set style". For example: {x, y} is a linearly independent set in a vector space if and only if there do not exist nonzero a, b such that ax + by = 0. Well, not if x = y!

#### [Reid Barton (Sep 28 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134781792):
On the other hand there are occasionally times when you genuinely need to work with subsets because you want to use the order structure and/or know that the collection of all possible bases is small, for example when proving that every vector space has a basis

#### [Mario Carneiro (Sep 28 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134781797):
I think the statement about every vector space has a basis will explicitly use subsets

#### [Reid Barton (Sep 28 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134781842):
I think the function approach is not really restrictive then anyways. You just say "a subset such that the inclusion is a basis".

#### [Mario Carneiro (Sep 28 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134781853):
i.e. every vector space has a basis where the function is the subtype coercion and the indexing set is a subtype of the vector space

#### [Reid Barton (Sep 28 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134781855):
(By the way, injectivity of the function is a consequence of being a basis, not a precondition.)

#### [Mario Carneiro (Sep 28 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134781869):
I agree, I think under most circumstances you should be able to prove injectivity, except in trivial cases and in those cases you probably don't want to impose it additionally

#### [Mario Carneiro (Sep 28 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134781913):
(bases over the zero ring are weird)

#### [Reid Barton (Sep 28 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134781932):
Hmm... yes

#### [Mario Carneiro (Sep 28 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134781956):
speaking of which... `unit` should be a ring

#### [Mario Carneiro (Sep 28 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134781998):
it would fit nicely with the ring instance for products and Pis

#### [Reid Barton (Sep 28 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134782068):
The nlab definition of basis is: A basis of a free R-module M (possibly a vector space, see basis of a vector space) is a linear isomorphism $$B\colon M \to \oplus_{i\in I}R$$ to a direct sum of copies of the ring R, regarded as a module over itself.

#### [Reid Barton (Sep 28 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134782086):
I think this kind of property is more important than "for all i /= j, b_i /= b_j"

#### [Reid Barton (Sep 28 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134782104):
... if you find yourself having to make some decision regarding the zero ring

#### [Reid Barton (Sep 28 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134782355):
Yes okay, now I see you were saying the same thing regarding definition of bases over the zero ring

#### [Mario Carneiro (Sep 28 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134783593):
so what does this say about linearly independent sets?

#### [Mario Carneiro (Sep 28 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134783641):
I guess these should also be indexed

#### [Johan Commelin (Sep 28 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134785061):
```quote
speaking of which... `unit` should be a ring
```
```lean
instance : comm_ring unit := by tidy
```

#### [Johan Commelin (Sep 28 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134785183):
Good luck golfing that...

#### [Johan Commelin (Sep 28 2018 at 03:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134785315):
I'm pretty sure that `tidy` will also prove for you that it is the terminal object in `Ring` and `CRing`

#### [Kevin Buzzard (Sep 28 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/134807675):
I must confess I was surprised when I first saw that in Lean a basis was a subset. Mulling over this, I realised that it was because I was used to teaching students about bases of *finite-dimensional* vector spaces -- and this is not a conversation about bases, this is also a conversation about the concepts of linear independence and spanning -- and in these cases it seems more convenient when developing the theory to be considering lists of elements rather than subsets (so order matters, and repeats are OK). For a dumb example, consider the zero ring `R`. Then `R^3=R` and hence I want `[0,0,0]` to be a basis for `R`, which it is. This is the only case where bases can have repeated elements and also the only case where bases can have different cardinalities. A less pathological example is that if a basis of a fdvs is a list then a linear map is a matrix, rather than some weird concept of a matrix where we don't mind permuting the rows and columns which we'd get for sets. My students did a bunch of stuff involving this over the summer -- linear maps = matrices and so on -- and although their code is probably not mathlib-ready it would not surprise me if they had worked out some good useful and correct statements.

The only situation I know where subsets are better than maps from a type is in the Zorn proof that every vector space has a basis. But this result is in some sense a bit of a novelty, my impression is that working mathematicians very rarely think about infinite-dimensional vector spaces with no extra structure at all, and if there is extra structure (a topology or whatever) then the abstract notion of a basis is usually not what we want anyway (c.f. "basis" of a Hilbert space = lin ind subset with dense span).

#### [Johan Commelin (Oct 04 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135187101):
If we are refactoring modules... would it make sense to rename `span` to `generate`? It would be more in line with all the other forms of `generate`...

#### [Mario Carneiro (Oct 04 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135193289):
I was actually thinking about going the other way :)

#### [Mario Carneiro (Oct 04 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135193368):
specifically as relates to other "closure" operations e.g. subgroup closure and normal closure

#### [Mario Carneiro (Oct 04 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135193424):
For set-of-set operations like `filter` and `topology` I prefer `generate`, but maybe that's not principled enough

#### [Mario Carneiro (Oct 04 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135193452):
I agree some uniformity of naming would be a good thing

#### [Johan Commelin (Oct 04 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135193845):
Ok, I don't really care which one gets chosen :lol:

#### [Mario Carneiro (Oct 08 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135377864):
So I've got to working on `ideal` now, and I have come to realize that ideal theory is not simply a specialization of submodule theory. It's obvious in hindsight, but as a category the homs are different - a ring hom is not a linear map, and a linear map is not a ring hom

#### [Mario Carneiro (Oct 08 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135377912):
So this means that things like `map` and `comap` don't work the same way on rings

#### [Mario Carneiro (Oct 08 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135377924):
In particular I don't even think there is a notion of `ideal.map` unless you assume the map is surjective

#### [Mario Carneiro (Oct 08 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135378146):
Is there a way to make sense of a ring-changing hom from (R,M) to (R',M') modules?

#### [Scott Morrison (Oct 08 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135378473):
Perhaps there's a notion of a map (R,M) to (R',M') as a linear map f : M to M', and a ring hom g : R' to R (note this is backwards), satisfying g(r') m = r' f(m).

#### [Scott Morrison (Oct 08 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135378476):
I'm not sure it's particularly useful.

#### [Mario Carneiro (Oct 08 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135378488):
yeah I was thinking the ring part might end up contravariant

#### [Mario Carneiro (Oct 08 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135378490):
so I guess this does not generalize ring homs as maps (R,R) -> (R', R')

#### [Johan Commelin (Oct 08 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135378925):
```quote
Is there a way to make sense of a ring-changing hom from (R,M) to (R',M') modules?
```
@**Mario Carneiro** What exactly do you mean with this question?

#### [Mario Carneiro (Oct 08 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135378968):
I wonder if there is a common generalization of ring homs, (R,R) -> (R', R') and linear maps (R,M) -> (R, M')

#### [Mario Carneiro (Oct 08 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135378976):
is there a category theory operation for taking a "total space" over the categories R-Mod where R is an object in the category Ring?

#### [Johan Commelin (Oct 08 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135378980):
Sure.

#### [Johan Commelin (Oct 08 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135378985):
That's a fibered category

#### [Johan Commelin (Oct 08 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135378994):
And this one is one of the first examples

#### [Johan Commelin (Oct 08 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379047):
A map `(R,M) → (R',M')` is a pair `R → R'` + `R' \otimes_R M → M'`. (Or do I need commutativity for that tensor product?)

#### [Johan Commelin (Oct 08 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379051):
Yes, I do.

#### [Johan Commelin (Oct 08 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379052):
This doesn't work for arbitrary `R → R'`.

#### [Johan Commelin (Oct 08 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379094):
@**Mario Carneiro** Were you planning on doing left- right- and two-sided-ideals?

#### [Johan Commelin (Oct 08 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379097):
Or only ideals in comm_rings?

#### [Mario Carneiro (Oct 08 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379102):
Just comm ring ideals, since that's what's there now

#### [Johan Commelin (Oct 08 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379107):
Ok, so for comm_ring modules you get this really nice fibered category `Mod`.

#### [Johan Commelin (Oct 08 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379109):
Is that what you were looking for?

#### [Johan Commelin (Oct 08 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379113):
Note that by adjunction you can also just give a map `M → M'` that is `R`-linear

#### [Mario Carneiro (Oct 08 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379128):
> `R' \otimes_R M`

what is this

#### [Johan Commelin (Oct 08 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379153):
Tensor product

#### [Johan Commelin (Oct 08 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379154):
turning `M` into an `R'`-module

#### [Mario Carneiro (Oct 08 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379155):
so R' is viewed as a R-module here?

#### [Johan Commelin (Oct 08 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379156):
Yes

#### [Mario Carneiro (Oct 08 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379164):
oh, there's an interesting construction we don't have

#### [Johan Commelin (Oct 08 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379166):
Which one?

#### [Mario Carneiro (Oct 08 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379169):
a ring hom `R -> R'` yields a R-module structure on `R'`

#### [Johan Commelin (Oct 08 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379173):
You mean the forgetful functor?

#### [Johan Commelin (Oct 08 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379176):
From `R'`-mod to `R`-mod?

#### [Mario Carneiro (Oct 08 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379216):
It's not forgetful, right?

#### [Johan Commelin (Oct 08 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379218):
Not really

#### [Mario Carneiro (Oct 08 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379219):
The hom could be anything

#### [Johan Commelin (Oct 08 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379222):
I still think of it as "forgetting"

#### [Johan Commelin (Oct 08 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379229):
We have `R` is an `R`-mod

#### [Johan Commelin (Oct 08 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379233):
So if you chain that to the "forget" instance, you have what you want.

#### [Mario Carneiro (Oct 08 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379239):
I don't follow

#### [Johan Commelin (Oct 08 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379242):
I tried adding "forget" about 3 months ago, and I ran into trouble.

#### [Mario Carneiro (Oct 08 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379244):
what forget instance?

#### [Johan Commelin (Oct 08 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379248):
But maybe with the refactor, you can now do it.

#### [Johan Commelin (Oct 08 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379249):
I mean `R'` is an `R'`-mod + every `R'`-mod is an `R`-mod.

#### [Johan Commelin (Oct 08 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379273):
I want your instance to be broken into 2 steps.

#### [Johan Commelin (Oct 08 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379301):
```quote
what forget instance?
```
The "forgetful" functor instance

#### [Mario Carneiro (Oct 08 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379302):
> every R'-mod is an R-mod

This one requires an explicit ring hom input

#### [Johan Commelin (Oct 08 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379308):
Hmmm, it does... unless we turn `R'` into an algebra

#### [Johan Commelin (Oct 08 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379310):
over `R`

#### [Mario Carneiro (Oct 08 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379318):
ah, we don't have anything like that yet

#### [Mario Carneiro (Oct 08 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379369):
I needed assoc algebras around this time in metamath, now I forget why

#### [Mario Carneiro (Oct 08 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379428):
Ah - multivariate polynomials are the free assoc algebra

#### [Johan Commelin (Oct 08 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379457):
The ones we have are also commutative

#### [Johan Commelin (Oct 08 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379496):
At some point we might want non-commutative polynomials as well

#### [Mario Carneiro (Oct 08 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379511):
I have never touched noncomm polynomials, but I guess it's not so hard with the group ring construction

#### [Mario Carneiro (Oct 08 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379514):
... + free monoid construction which we already have

#### [Johan Commelin (Oct 08 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379515):
So, could we have `f^* M'`?

#### [Mario Carneiro (Oct 08 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379555):
I think so, what does that mean?

#### [Johan Commelin (Oct 08 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379556):
where `f` is a ring hom `R → R'` and `M'` is an `R'`-mod

#### [Johan Commelin (Oct 08 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379559):
So `f^*` is the functor `R'-mod → R-mod`

#### [Mario Carneiro (Oct 08 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379565):
ah, okay so this is the contravariant thing that scott mentioned

#### [Johan Commelin (Oct 08 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379567):
Right, and it is adjoint to tensoring.

#### [Johan Commelin (Oct 08 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379568):
Which is covariant

#### [Johan Commelin (Oct 08 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379570):
no, that's bullcrap

#### [Johan Commelin (Oct 08 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379571):
I'm brainfarting

#### [Johan Commelin (Oct 08 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379609):
tensor is adjoint to hom

#### [Johan Commelin (Oct 08 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135379614):
Lol. So you get to choose: either you use `f^*` which is contravariant. Or you use tensor products, and you get something covariant, but "harder to parse".

#### [Johan Commelin (Oct 08 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135383276):
@**Mario Carneiro** How would all this abstract nonsense help with:
```quote
So I've got to working on `ideal` now, and I have come to realize that ideal theory is not simply a specialization of submodule theory. It's obvious in hindsight, but as a category the homs are different - a ring hom is not a linear map, and a linear map is not a ring hom
```

#### [Kenny Lau (Oct 08 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135383285):
And nobody here has pointed out that extensions of ideals exist, c.f. Atiyah-Macdonald P.9

#### [Kenny Lau (Oct 08 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135383328):
```quote
In particular I don't even think there is a notion of `ideal.map` unless you assume the map is surjective
```
if f:A->B is a ring hom and L is an ideal in A then L^e is the ideal generated by f(L)

#### [Kenny Lau (Oct 08 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135383339):
[2018-10-08.png](/user_uploads/3121/OAIFV_UuuBZXylsyoLFs_sUK/2018-10-08.png)

#### [Mario Carneiro (Oct 08 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135383404):
yeah, okay that's a better idea

#### [Mario Carneiro (Oct 08 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135383408):
just close the resulting set under ideal operations

#### [Johan Commelin (Oct 08 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135383456):
@**Mario Carneiro** Do you have some sort of todo list of what remains for this refactor?

#### [Mario Carneiro (Oct 08 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135383458):
@**Johan Commelin** It's just some idle speculation on my part, I don't really have any concrete implementation ideas

#### [Mario Carneiro (Oct 08 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135383464):
I'm currently in "tying up loose ends" mode in the refactor, I don't want to introduce new things

#### [Johan Commelin (Oct 08 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135383467):
Great!

#### [Mario Carneiro (Oct 08 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135383470):
it's already behind schedule too much

#### [Mario Carneiro (Oct 08 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135383513):
although it has made several other projects come to the fore, which I will probably have to start working on after I'm done

#### [Mario Carneiro (Oct 08 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135383515):
foremost of which is the multiple scalar field thing

#### [Johan Commelin (Oct 08 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135383519):
After you are done, I think `faster` should be the first thing on your list. :lol:

#### [Mario Carneiro (Oct 08 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135383522):
I'm actually working on that ATM

#### [Johan Commelin (Oct 08 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135383525):
Wonderful! Thanks for doing that!

#### [Kevin Buzzard (Oct 08 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135384515):
Here are some thoughts. The fundamental notion in algebraic geometry is an "f-map" -- see 6.21.7 in [the stacks project](https://stacks.math.columbia.edu/tag/008C). Lemma 6.21.8 shows that this is a natural idea. Although it's dressed up in a geometric language, this is something related to the conversation here. The notion of an f-map shows up in the definition of a morphism of ringed spaces in [definition 6.21](https://stacks.math.columbia.edu/tag/0090). In the discussion just below 6.26.3 [here](https://stacks.math.columbia.edu/tag/0094) we see the notion of an f-map of sheaves of modules. Note in particular in that discussion that the f-maps from G to F are in canonical bijection with two other hom sets, one involving only sheaves on X and one involving only sheaves on Y.

Now of course all this needs a lot of unravelling, and the way to unravel is to ask how what de Jong writes translates into the case of affine schemes, which are just commutative rings in disguise. If I got it right, then he says to focus on the following idea: if $$f:A\to B$$ is a map of rings and if $$G$$ is an $$A$$-module and $$F$$ a $$B$$-module, an $$f$$-map $$G\to F$$ is simply an $$A$$-module homomorphism from $$G$$ to $$F$$, and the observation is that such maps naturally biject with the $$B$$-module homomorphisms from $$G\otimes_AB$$ to $$F$$. I think this is different to what Scott suggests -- he went the other way.

#### [Kevin Buzzard (Oct 08 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135384772):
```quote
I wonder if there is a common generalization of ring homs, (R,R) -> (R', R') and linear maps (R,M) -> (R, M')
```
I think $$f$$-maps give this. An $$f$$-map $$(R,M)\to (R',M')$$ is a ring map $$R\to R'$$ and an $$R$$-module map $$M\to M'$$ (note I'm constantly using this trick of, the moment I have a ring map $$R\to R'$$, considering all $$R'$$-modules as $$R$$-modules). If $$R\to R'$$ is the identity then this is just an $$R$$-module homomorphism, and an *example* of an $$f$$-map $$(R,R)\to(R',R')$$ is given by $$(f,f)$$, but given $$f:R\to R'$$ there are $$f$$-maps $$(R,R)\to (R',R')$$ which are not $$(f,f)$$.

#### [Kevin Buzzard (Oct 08 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385018):
OK so Johan has isolated exactly the same idea, but somehow it seems that he has come from a completely different viewpoint (I don't know what a fibred category is). Regarding commutative v non-commutative, I think it's a good idea to push commutative here. Someone impressed on me decades ago that one should not think of commutative ring theory as a special case of non-commutative ring theory but regard them as completely different areas. I don't know anything about research into non-commutative ring theory, but commutative ring theory is very much alive and kicking -- e.g. ideas from the theory of perfectoid spaces were used here https://arxiv.org/abs/1608.08882 to resolve a the direct summand conjecture. Commutative algebra is the foundation of modern algebraic geometry and I have always been of the opinion (even before I knew anything about formal proof verification software) that books like Atiyah--Macdonald and Matsumura (both standard commutative algebra textbooks) somehow "operated close to the axioms" whilst still being of great modern interest. If we want to push Lean as a tool for algebraic geometry, which it one day might become, then there's no harm focussing on commutative algebra. When someone eventually decides to do some basic representation theory of finite groups we might have to plough through basics of semisimple algebras but that is somehow a completely different project.

#### [Johan Commelin (Oct 08 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385035):
@**Kevin Buzzard** A fibered category is the thing that underlies a stack.

#### [Johan Commelin (Oct 08 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385039):
Basically it abstracts $$f$$-maps

#### [Kevin Buzzard (Oct 08 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385344):
```quote
> every R'-mod is an R-mod

This one requires an explicit ring hom input
```
Patrick mentioned recently that sometimes it's best to concentrate on the morphisms, not the objects. In alg geom we even see it in the name -- an $$f$$-map is a construction which depends on a map $$f$$ of rings. In fact Johan is saying all the right things, I need to get up much earlier to get ahead of him. Given $$f:R\to R'$$ there are then adjoint functors $$(R-mod)\to(R'-mod)$$ and $$(R'-mod)\to(R-mod)$$ and hopefully Kenny proved enough about universal property of tensor products to show that these are adjoints. I think that Scott's punt went in the wrong direction. There is a time when you get maps one way and the other way, but that's when you go back to schemes.

#### [Johan Commelin (Oct 08 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385406):
```quote
In fact Johan is saying all the right things, I need to get up much earlier to get ahead of him. 
```
I've got a 2-year old daughter. You can't win.

#### [Johan Commelin (Oct 08 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385439):
Well, what I think that Scott meant that `f → f^*` is contravariant.

#### [Kevin Buzzard (Oct 08 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385440):
Kenny's construction is something else though. If $$L$$ is an ideal of $$A$$ then $$L^e$$, the pushforward ideal, is less well-behaved. $$L^e$$ is the image of $$L\otimes_AB$$ (the canonical thing when it comes to modules) under the natural map from this guy to $$B$$ corresponding by adjointness to the map $$L\to B$$. So it might satisfy some universal property for ideals, but probably not for modules.

#### [Kevin Buzzard (Oct 08 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385492):
OK I think that's all I have to say and I think that most of it had been said already, but at least I caught up.

#### [Johan Commelin (Oct 08 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385493):
For ideals it will probably give you a Galois connection. Here! I said it. Without checking.

#### [Mario Carneiro (Oct 08 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385562):
But I guess $$L^e$$ is the best you can do when you have a ring hom A->B and an ideal L?

#### [Johan Commelin (Oct 08 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385574):
If you want an ideal of `B`, yes.

#### [Johan Commelin (Oct 08 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385584):
Otherwise, you could just tensor, and treat it as a module.

#### [Mario Carneiro (Oct 08 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385586):
Is this a thing we can currently do?

#### [Johan Commelin (Oct 08 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385590):
What?

#### [Mario Carneiro (Oct 08 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385592):
tensoring like that

#### [Johan Commelin (Oct 08 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385594):
I guess almost

#### [Johan Commelin (Oct 08 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385634):
@**Kenny Lau** Did you include extension of scalars in your work on tensor products?

#### [Johan Commelin (Oct 08 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385647):
@**Mario Carneiro** Given what we have, it shouldn't be too hard

#### [Kenny Lau (Oct 08 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135385977):
I don’t think I did.

#### [Kevin Buzzard (Oct 08 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135386823):
Oh I see. The issue is that if $$M$$ is an $$A$$-module and $$B$$ is an $$A$$-algebra (and hence an $$A$$-module) then $$M\otimes_AB$$ is not just an $$A$$-module but a $$B$$-module.

#### [Johan Commelin (Oct 08 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135386914):
Right, we don't have something like that atm

#### [Johan Commelin (Oct 08 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135386928):
But it shouldn't be hard to put a `B`-mod structure on the tensor product.

#### [Johan Commelin (Oct 08 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135387004):
I don't know if it should "extend" the `A`-mod structure, in the sense that if you "restrict" scalars you get an `A`-mod that is defeq to what you started with.

#### [Patrick Massot (Oct 08 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/135421783):
```quote
foremost of which is the multiple scalar field thing
```
I'm completely lost: I thought this module refactor was mostly about multiple scalars

#### [Kenny Lau (Oct 23 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136304439):
How's it going? @**Mario Carneiro**

#### [Mario Carneiro (Oct 23 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136306139):
waiting on my school work to decrease in intensity

#### [Mario Carneiro (Oct 23 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136306145):
hopefully I should be able to find some time for it this week

#### [Kenny Lau (Nov 01 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136911662):
https://github.com/leanprover-community/mathlib/commits/module

#### [Kenny Lau (Nov 01 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136911664):
@**Mario Carneiro** is there anything we can help with?

#### [Mario Carneiro (Nov 01 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136912060):
Possibly... I'm just short on time these days. The main work is done, I think, but a bunch of files still need to be updated

#### [Kenny Lau (Nov 01 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136912064):
what can we do?

#### [Kenny Lau (Nov 01 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136912067):
should I fix the errors?

#### [Mario Carneiro (Nov 01 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136912068):
go in there and make the red squiggles go away

#### [Kenny Lau (Nov 01 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136912116):
roger that

#### [Mario Carneiro (Nov 01 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136912204):
Don't get too attached to anything that you write there, I'll probably have a look through all the files anyway, but it will be a lot easier if it's not already broken

#### [Kenny Lau (Nov 01 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136919089):
@**Mario Carneiro** there are things that you deleted and things that depend on them, right

#### [Kenny Lau (Nov 01 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136919093):
I'll just leave those untouched

#### [Mario Carneiro (Nov 01 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136919165):
like what? I think all deleted files have equivalents

#### [Kenny Lau (Nov 01 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136919191):
like the order embedding of submodules of submodules, and the prime ideal, and the trivial ideal

#### [Kenny Lau (Nov 01 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136919263):
and also this:
```lean
@[simp] theorem Union_set_of_directed {ι} (hι : nonempty ι)
  (S : ι → submodule α β)
  (H : ∀ i j, ∃ k, S i ≤ S k ∧ S j ≤ S k) :
  ((supr S : submodule α β) : set β) = ⋃ i, S i :=
```

#### [Mario Carneiro (Nov 01 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136919265):
prime ideals are still there

#### [Mario Carneiro (Nov 01 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136919287):
search for that, it moved somewhere else

#### [Mario Carneiro (Nov 01 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136919297):
I think it is Union_coe now

#### [Kenny Lau (Nov 01 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136919305):
`prime_ideal` doesn't give me anything

#### [Kenny Lau (Nov 01 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136919307):
and i wouldn't search for `prime`

#### [Mario Carneiro (Nov 01 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136919355):
the trivial ideal is bottom

#### [Kenny Lau (Nov 01 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136919360):
ok I searched for `prime` and I found it

#### [Kenny Lau (Nov 01 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136925189):
@**Mario Carneiro** what about the embedding “submodules of N” -> “submodules of M” where N is a submodule of M?

#### [Mario Carneiro (Nov 01 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136928650):
I think that's `map N.subtype` or `map_subtype.order_iso`

#### [Kenny Lau (Nov 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136942283):
@**Mario Carneiro** I've pushed a partial fix

#### [Kenny Lau (Nov 01 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136942285):
I'll see what more I can do

#### [Kenny Lau (Nov 02 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136986811):
@**Mario Carneiro** for principal ideal domains, the situation is that `{x | a ∣ x}` is a set not an ideal, so these definitions are a bit troublesome:
```lean
class is_principal_ideal [comm_ring α] (S : set α) : Prop :=
(principal : ∃ a : α, S = {x | a ∣ x})

class principal_ideal_domain (α : Type*) extends integral_domain α :=
(principal : ∀ (S : ideal α), is_principal_ideal (S : set α))
```

#### [Kenny Lau (Nov 02 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/136986813):
what should I do?

#### [Kenny Lau (Nov 02 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137008240):
@**Mario Carneiro** [`ideal.quotient.eq`](https://github.com/leanprover/mathlib/blob/master/ring_theory/ideals.lean#L140) is missing

#### [Kenny Lau (Nov 02 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137008271):
(and `submodule.quotient.eq` doesn't count)

#### [Kenny Lau (Nov 02 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137064504):
Successfully reduced to 4 errors. Pushed.

#### [Mario Carneiro (Nov 02 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137076716):
the ideal `{x | a ∣ x}` is now spelled `span {a}`

#### [Kenny Lau (Nov 02 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079093):
@**Mario Carneiro** by "now" do you mean "I've changed that in my private copy" or "I should change that and then push it"?

#### [Mario Carneiro (Nov 02 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079105):
I mean in the module branch that's how it is currently used

#### [Mario Carneiro (Nov 02 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079113):
so if you find it elsewhere you should use that

#### [Kenny Lau (Nov 02 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079114):
so it's the latter?

#### [Kenny Lau (Nov 02 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079118):
ok

#### [Mario Carneiro (Nov 02 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079137):
is_principal_ideal should be a property of S : ideal

#### [Kenny Lau (Nov 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079292):
and what is to become of `ideal.quotient.eq`? @**Mario Carneiro**

#### [Mario Carneiro (Nov 02 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079358):
what does `quotient_ring` look like now?

#### [Kenny Lau (Nov 02 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079414):
it looks like `ideal.quotient` now

#### [Kenny Lau (Nov 02 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079430):
we have `ideal.quotient.mk := submodule.quotient.mk` and we have `submodule.quotient,eq`

#### [Kenny Lau (Nov 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079446):
but not `ideal.quotient.eq`

#### [Mario Carneiro (Nov 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079455):
oh sure, you can state `ideal.quotient.eq`

#### [Kenny Lau (Nov 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079458):
ok

#### [Mario Carneiro (Nov 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079464):
it's just a defeq copy paste job

#### [Kenny Lau (Nov 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079476):
I just thought I wouldn't add things without first asking you

#### [Mario Carneiro (Nov 02 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079481):
I have not added all theorems from submodules to ideals, I intended to add them as needed

#### [Mario Carneiro (Nov 02 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079549):
you can often just use the submodule version directly, but it is slightly less ergonomic

#### [Kenny Lau (Nov 02 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137079650):
I agree (with the latter statement)

#### [Kenny Lau (Nov 02 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137084347):
```lean
lemma mem_span_singleton {x y : α} :
  x ∈ span ({y} : set α) ↔ ∃ a, a * y = x :=
```

#### [Kenny Lau (Nov 02 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137084351):
@**Mario Carneiro** can I change this to use dvd?

#### [Mario Carneiro (Nov 02 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137084382):
maybe make another theorem

#### [Kenny Lau (Nov 02 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137084453):
but nobody uses that theorem

#### [Kenny Lau (Nov 02 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137084455):
you added that theorem yourself

#### [Kenny Lau (Nov 02 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137085654):
```lean
lemma is_maximal_of_irreducible {p : α} (hp : irreducible p) :
  is_maximal (span ({p} : set α)) :=
```
Should this be an instance?

#### [Mario Carneiro (Nov 02 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137085959):
oh I see, it's copy pasted from the analogous theorem on submodule, where you can't use dvd

#### [Mario Carneiro (Nov 02 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137086049):
as for that last one - probably not. Things like `irreducible` and `maximal` and `nat.prime` are forming a new kind of idiom, where the predicate is a `class` but most of the theorems use it like normal assumptions

#### [Mario Carneiro (Nov 02 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137086099):
This is primarily intended to support the few cases where you have to use typeclass inference, like in Z/nZ is a field

#### [Kevin Buzzard (Nov 03 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137089370):
I want there to be an "is_an_integer" predicate on eg rat to save me from coercions.

#### [Kenny Lau (Nov 03 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137089440):
@**Kevin Buzzard** wrong thread?

#### [Kevin Buzzard (Nov 03 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137089490):
Isn't that a predicate which is a class?

#### [Kenny Lau (Nov 03 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137089518):
oh well this is going off track

#### [Chris Hughes (Nov 03 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137089626):
Why is it a class?

#### [Mario Carneiro (Nov 03 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137089816):
I don't just mean a predicate that is a class, we have plenty of those like `first_countable X`. I mean predicates that are classes that we use without instance brackets in most theorems

#### [Kenny Lau (Nov 03 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137090743):
I feel like there is not enough transparency with the module refactoring, so I've decided to write something about it.

Major changes made:

- `semimodule α β` and `module α β` and `vector_space α β` now take one more argument, that `β` is an `add_comm_group`, i.e. before making an instance of a module, you need to prove that it's an abelian group first.
- vector space is no longer over a field, but a discrete field.
- The idiom for making an instance `module α β` (after proving that `β` is an abelian group) is `module.of_core { smul := sorry, smul_add  := sorry, add_smul := sorry, mul_smul := sorry, one_smul := sorry }`.
- `is_linear_map` and `linear_map` are now both structures, and they are independent, meaning that `linear_map` is no longer defined as `subtype is_linear_map`. The idiom for making `linear_map` from `is_linear_map` is `is_linear_map.mk' (f : M -> N) (sorry : is_linear_map f)`, and the idiom for making `is_linear_map` from `linear_map` is `f.is_linear` (i.e. `linear_map.is_linear f`).
- `is_linear_map.add` etc no longer exist. instead, you can now add two linear maps together, etc.
- the class`is_submodule` is gone, replaced by the structure `submodule` which contains a carrier, i.e. if `N : submodule R M` then `N.carrier` is a type. And there is an instance `module R N` in the same situation.
- similarly, the class `is_ideal` is gone, replaced by the structure `ideal`, which also contains a carrier.
- endomorphism ring and general linear group are defined.
- submodules form a complete lattice. the trivial ideal is now idiomatically the bottom element, and the universal ideal the top element.
- `linear_algebra/quotient_module.lean` is deleted, and it's now `submodule.quotient` (so if `N : submodule R M` then `submodule R N.quotient`) Similarly, `quotient_ring.quotient` is replaced by `ideal.quotient`. The canonical map from `N` to `N.quotient` is `submodule.quotient.mk`, and the canonical map from the ideal `I` to `I.quotient` is `ideal.quotient.mk I`.
- `linear_equiv` is now based on a linear map and an equiv, and the difference being that now you need to prove that the inverse is also linear, and there is currently no interface to get around that.
- Everything you want to know about linear independence and basis is now in the newly created file `linear_algebra/basis.lean`.
- Everything you want to know about linear combinations is now in the newly created file `linear_algebra/lc.lean`.
- `linear_algebra/linear_map_module.lean` and `linear_algebra/prod_module.lean` and `linear_algebra/quotient_module.lean` and `linear_algebra/submodule.lean` and `linear_algebra/subtype_module.lean` are deleted (with their contents placed elsewhere).

#### [Mario Carneiro (Nov 03 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137090764):
Ha, this was my secret plan all along

#### [Kenny Lau (Nov 03 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137090808):
I think one would prefer transparency

#### [Mario Carneiro (Nov 03 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137090810):
now that kenny had to read the stuff he knows what changed

#### [Mario Carneiro (Nov 03 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137090817):
and can write a nice summary for us

#### [Kenny Lau (Nov 03 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137090822):
lol

#### [Mario Carneiro (Nov 03 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137090864):
A remark on `module.of_core`: it's only intended for use when you aren't proving it's a semimodule first

#### [Mario Carneiro (Nov 03 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137090910):
like if you don't care about semimodules

#### [Kenny Lau (Nov 03 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137090954):
I'm sure Kevin doesn't

#### [Mario Carneiro (Nov 03 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137090961):
By the way, `is_linear_map` is a late addition. I'm hoping it will not be needed much at all, but it's useful to have as a mixin occasionally

#### [Kenny Lau (Nov 03 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137091015):
one would have to refactor `tensor_product` to get rid of all the dependencies thereto, I believe

#### [Mario Carneiro (Nov 03 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137091016):
I really want `linear_map` to be the primary one

#### [Mario Carneiro (Nov 03 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137091023):
oh, I may have done that already

#### [Kenny Lau (Nov 03 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137091025):
not entirely

#### [Mario Carneiro (Nov 03 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137091026):
shoot, I have an unsaved file in vscode

#### [Kenny Lau (Nov 03 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137091030):
lol

#### [Mario Carneiro (Nov 03 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137091130):
re: interface for linear_equiv, you don't need to prove the inverse is linear, that's not in the structure

#### [Mario Carneiro (Nov 03 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137091149):
it's just the union (pushout?) of linear_map and equiv

#### [Kenny Lau (Nov 03 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137091304):
oh, right

#### [Kenny Lau (Nov 03 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137091863):
@**Mario Carneiro** are you going to push your file?

#### [Mario Carneiro (Nov 03 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137092023):
oh wait, looks like I already pushed most of it

#### [Mario Carneiro (Nov 03 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137092026):
you already had the important stuff

#### [Kenny Lau (Nov 03 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137092090):
but tensor product still depends on is_linear_map right?

#### [Kenny Lau (Nov 03 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137092235):
```lean
protected def id : R ⊗ M ≃ₗ M :=
{ inv_fun := (⊗ₜ) 1,
  left_inv := lift.ext
    (linear_map.is_linear $ linear_map.comp (is_linear_map.mk' _ $ (bilinear _ _).linear_right 1) (lift _ _))
    linear_map.id.is_linear
    (λ x y, by simp; rw [← tmul_smul, ← smul_tmul, smul_eq_mul, mul_one]),
  right_inv := λ m, by simp,
  .. (lift (λ c x, c • x)
    ⟨λ m, linear_map.is_linear (linear_map.smul_right linear_map.id m),
    λ r, linear_map.is_linear (r • linear_map.id)⟩ : R ⊗ M →ₗ M) }
```

#### [Kenny Lau (Nov 03 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137092236):
I don't think anyone wants to see this

#### [Mario Carneiro (Nov 03 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137092333):
what is your objection exactly?

#### [Kenny Lau (Nov 03 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137092419):
1. the linear map needs to be put after `..`; 2. lack of `is_linear_map.comp` and the fact that `lift.ext` and most of the things in `tensor_product` depend on `is_linear_map` make proofs very long and cumbersome

#### [Mario Carneiro (Nov 03 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137093199):
I've only done the first half of that file, so some things may still need to be hashed out

#### [Mario Carneiro (Nov 03 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137093203):
`lift.ext` should take linear maps as input

#### [Mario Carneiro (Nov 03 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137093273):
You shouldn't feel bound to the current way statements of theorems are written, that's what refactoring is about

#### [Mario Carneiro (Nov 03 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137093296):
Ideally, this construction should be easy, just cobbling together functions we already know are linear

#### [Mario Carneiro (Nov 03 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137093354):
I think we need another constructor for is_bilinear_map, or is_linear_map, that takes a linear function and asks you to prove equality to the target function

#### [Mario Carneiro (Nov 03 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137093401):
which corresponds to the alternate definition `def is_linear_map (f : β → γ) := ∃ g : β →ₗ γ, ∀ x, f x = g x`

#### [Kenny Lau (Nov 03 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096037):
```quote
`lift.ext` should take linear maps as input
```
I don't think that will work, because there are things that need to be proved to be linear

#### [Kenny Lau (Nov 03 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096098):
do you think I should change `is_bilinear_map` to `bilinear_map`?

#### [Mario Carneiro (Nov 03 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096203):
Huh? `lift.ext` takes two functions and proofs that they are linear

#### [Mario Carneiro (Nov 03 2018 at 03:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096204):
that can always be contracted to a function taking a `linear_map` arg

#### [Mario Carneiro (Nov 03 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096254):
I thought about it, but do the set of all bilinear maps have a nice structure like linear maps? Like can you add them and such

#### [Kenny Lau (Nov 03 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096331):
yes

#### [Kenny Lau (Nov 03 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096332):
they're even a module

#### [Kenny Lau (Nov 03 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096371):
they're as nice as linear maps

#### [Kenny Lau (Nov 03 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096374):
(because of the universal property of tensor product :P)

#### [Mario Carneiro (Nov 03 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096836):
well okay then

#### [Mario Carneiro (Nov 03 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096849):
I think `bilinear_map` still needs to reference `is_linear_map` though

#### [Kenny Lau (Nov 03 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096851):
```lean
@[reducible] def bilinear_map := M →ₗ N →ₗ P
```

#### [Kenny Lau (Nov 03 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096852):
how about this

#### [Mario Carneiro (Nov 03 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096854):
oh! does that work?

#### [Kenny Lau (Nov 03 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096856):
I'm experimenting with it now

#### [Mario Carneiro (Nov 03 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096859):
is Mod(R) a CCC?

#### [Kenny Lau (Nov 03 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096898):
CCC?

#### [Mario Carneiro (Nov 03 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096899):
cartesian closed category

#### [Mario Carneiro (Nov 03 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096900):
i.e. that thing means what you want it to

#### [Kenny Lau (Nov 03 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096901):
yes

#### [Kenny Lau (Nov 03 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096910):
actually I don't know

#### [Kenny Lau (Nov 03 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096913):
I just know that Hom(M tensor N, P) = Hom(M, Hom(N, P))

#### [Kenny Lau (Nov 03 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096914):
so (- tensor N) is right adjoint to Hom(N, -)

#### [Mario Carneiro (Nov 03 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096923):
that looks a lot like the universal property of the exponential

#### [Mario Carneiro (Nov 03 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137096963):
Hom(N,P) there is actually an object of the category

#### [Kenny Lau (Nov 03 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137097797):
```lean
import group_theory.free_abelian_group
import linear_algebra.basic tactic.squeeze

variables (R : Type*) [comm_ring R]
variables (M : Type*) (N : Type*) (P : Type*) {Q : Type*}
variables [add_comm_group M] [add_comm_group N] [add_comm_group P] [add_comm_group Q]
variables [module R M] [module R N] [module R P] [module R Q]
include R

@[reducible] def bilinear_map := M →ₗ N →ₗ P

variables {R M N P}

namespace bilinear_map
variables {M N P Q}

section mk
variable (f : M → N → P)
variable (H1 : ∀ m₁ m₂ n, f (m₁ + m₂) n = f m₁ n + f m₂ n)
variable (H2 : ∀ c m n, f (c • m) n = c • f m n)
variable (H3 : ∀ m n₁ n₂, f m (n₁ + n₂) = f m n₁ + f m n₂)
variable (H4 : ∀ c m n, f m (c • n) = c • f m n)

def bilinear_map.mk :
  bilinear_map R M N P :=
⟨λ m, ⟨f m, H3 m, λ c, H4 c m⟩,
λ m₁ m₂, linear_map.ext $ H1 m₁ m₂,
λ c m, linear_map.ext $ H2 c m⟩

theorem bilinear_map.mk_apply (m : M) (n : N) :
  bilinear_map.mk f H1 H2 H3 H4 m n = f m n := rfl

end mk

variables (f : bilinear_map R M N P)

def comm : bilinear_map R N M P :=
bilinear_map.mk (λ n m, f m n)
  (λ n₁ n₂ m, (f m).map_add _ _)
  (λ c n m, (f m).map_smul _ _)
  (λ n m₁ m₂, by rw f.map_add; refl)
  (λ c n m, by rw f.map_smul; refl)

@[simp] theorem comm_apply (m : M) (n : N) : f.comm n m = f m n := rfl

def left (y : N) : M →ₗ P := f.comm y
def right (x : M) : N →ₗ P := f x

@[simp] theorem left_apply (x : M) (y : N) : f.left y x = f x y := rfl
@[simp] theorem right_apply (x : M) (y : N) : f.right x y = f x y := rfl

theorem zero_left (y) : f 0 y = 0 := (f.left y).map_zero
theorem zero_right (x) : f x 0 = 0 := (f.right x).map_zero

theorem neg_left (x y) : f (-x) y = -f x y := (f.left y).map_neg _
theorem neg_right (x y) : f x (-y) = -f x y := (f.right x).map_neg _

theorem add_left (x₁ x₂ y) : f (x₁ + x₂) y = f x₁ y + f x₂ y := (f.left y).map_add _ _
theorem add_right (x y₁ y₂) : f x (y₁ + y₂) = f x y₁ + f x y₂ := (f.right x).map_add _ _

theorem smul_left (r x y) : f (r • x) y = r • f x y := (f.left y).map_smul _ _
theorem smul_right (r x y) : f x (r • y) = r • f x y := (f.right x).map_smul _ _

def comp₁ (g : Q →ₗ M) : bilinear_map R Q N P :=
linear_map.comp f g

@[simp] theorem comp₁_apply (g : Q →ₗ M) (q : Q) (n : N) :
  f.comp₁ g q n = f (g q) n := rfl

def comp₂ (g : Q →ₗ N) : bilinear_map R M Q P :=
linear_map.comp ⟨λ x, linear_map.comp x g, λ _ _, rfl, λ _ _, rfl⟩ f

@[simp] theorem comp₂_apply (g : Q →ₗ N) (m : M) (q : Q) :
  f.comp₂ g m q = f m (g q) := rfl

def comp₃ (g : P →ₗ Q) : bilinear_map R M N Q :=
linear_map.comp ⟨g.comp, λ x y, linear_map.ext $ λ n, g.map_add _ _,
  λ c x, linear_map.ext $ λ n, g.map_smul _ _⟩ f

@[simp] theorem comp₃_apply (g : P →ₗ Q) (m : M) (n : N) :
  f.comp₃ g m n = g (f m n) := rfl

end bilinear_map
```

#### [Kenny Lau (Nov 03 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137097798):
looking good

#### [Mario Carneiro (Nov 03 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137097901):
maybe I'm spoiled, but I would hope that there was a direct way to get `comm`

#### [Mario Carneiro (Nov 03 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137097902):
maybe it requires the tensor product though

#### [Mario Carneiro (Nov 03 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137097943):
I guess it is equivalent to saying that `left` is a linear map

#### [Mario Carneiro (Nov 03 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137098004):
If `apply : M -> (M ->l N) ->l N` was linear we would have it

#### [Kenny Lau (Nov 03 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137098005):
and if `comp` was also linear.. :P

#### [Mario Carneiro (Nov 03 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137098051):
yeah, there should be a principled way to do this using CCCs

#### [Kenny Lau (Nov 03 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137098052):
but that would be too category-theoretical for our purposes

#### [Mario Carneiro (Nov 03 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137098057):
I mean with the categories unfolded away

#### [Mario Carneiro (Nov 03 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137098062):
We know that CCCs interpret lambda calculus, so literally anything you can write down that is type correct will be linear

#### [Mario Carneiro (Nov 03 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137098104):
we just need the right building blocks to get everything else

#### [Kenny Lau (Nov 03 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137098106):
but we also know that lambda calculus is generated by abstraction and application?

#### [Mario Carneiro (Nov 03 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137098113):
yes

#### [Kenny Lau (Nov 03 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137098114):
but abstraction isn't a linear map?

#### [Mario Carneiro (Nov 03 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137098116):
That's `apply`

#### [Kenny Lau (Nov 03 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137098159):
so what's the conclusion?

#### [Mario Carneiro (Nov 03 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137098162):
er, no - abstraction is the UMP of apply

#### [Mario Carneiro (Nov 03 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137098170):
it works because the families we are considering are themselves linear in their free variables

#### [Mario Carneiro (Nov 03 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137098173):
so you get a "lambda" like operator

#### [Mario Carneiro (Nov 03 2018 at 04:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137098216):
In this context we wouldn't actually be able to write down lambda, because we have "the wrong lambda", it isn't linear because we don't have the right notion of family for the category

#### [Mario Carneiro (Nov 03 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137098221):
but we can run any lambda term through the CCC translation to get a term using only CCC primitives, and we can prove these are all linear

#### [Johan Commelin (Nov 03 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137103669):
I really like where this is going! Keep up the good work!

#### [Kevin Buzzard (Nov 03 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137104926):
Yes many thanks Kenny for trying to get the show back on the road. Does this stuff compile yet? Is it worth going back to Hilbert basis theorem yet?

#### [Kenny Lau (Nov 03 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137110271):
Fixed

#### [Kenny Lau (Nov 03 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137110475):
@**Mario Carneiro** what's the next step?

#### [Mario Carneiro (Nov 03 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137110481):
is it compiling now?

#### [Kenny Lau (Nov 03 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137110485):
yes

#### [Mario Carneiro (Nov 03 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137110524):
sweet

#### [Mario Carneiro (Nov 03 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137110532):
unfortunately I still need to finish and review it myself, so it's in the queue with the other PRs now

#### [Mario Carneiro (Nov 03 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137110546):
If things go well I will have time this weekend for it

#### [Kenny Lau (Nov 03 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137110590):
nice

#### [Mario Carneiro (Nov 03 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137110591):
but if you see any other ways to improve it, add more theorems etc, now's the time

#### [Mario Carneiro (Nov 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137110605):
the CCC laws seem like a good place to start

#### [Mario Carneiro (Nov 03 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137110608):
prove that `curry : (A X B -> C) -> (A -> B -> C)` is a linear map

#### [Mario Carneiro (Nov 03 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137110655):
an equiv, even

#### [Kenny Lau (Nov 03 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137110661):
ok

#### [Kenny Lau (Nov 03 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137110702):
I don't think that's true

#### [Mario Carneiro (Nov 03 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137110907):
put `l` everywhere

#### [Mario Carneiro (Nov 03 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137110908):
that's homs in the category

#### [Kenny Lau (Nov 03 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137110950):
it's `(M tensor N) -> P` equiv `M -> (N -> P)`

#### [Kenny Lau (Nov 03 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111063):
```
1. (M ⊗ N) ⊗ P -> M ⊗ (N ⊗ P)
2. (M ⊗ N) -> P -> M ⊗ (N ⊗ P)
3. P -> (M ⊗ N) -> M ⊗ (N ⊗ P)
4. P -> M -> N -> M ⊗ (N ⊗ P)
5. M -> P -> N -> M ⊗ (N ⊗ P)
6. M -> N -> P -> M ⊗ (N ⊗ P)
7. M -> N ⊗ P -> M ⊗ (N ⊗ P)
````

#### [Mario Carneiro (Nov 03 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111403):
yes

#### [Mario Carneiro (Nov 03 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111408):
linear equiv I assume

#### [Mario Carneiro (Nov 03 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111419):
But I chose that one specifically because it's one of the CCC primitives

#### [Johan Commelin (Nov 03 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111422):
*canonical* linear equiv, even... :grinning_face_with_smiling_eyes:

#### [Mario Carneiro (Nov 03 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111473):
`apply` is another: `(M -> N) X M -> N`

#### [Mario Carneiro (Nov 03 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111476):
it's trivial with that equiv though

#### [Mario Carneiro (Nov 03 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111486):
I think the hom adjunction is equivalent to a few terms that you can compose

#### [Mario Carneiro (Nov 03 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111490):
like apply and curry

#### [Mario Carneiro (Nov 03 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111532):
do we have everything we need for the tensor product to be a product?

#### [Mario Carneiro (Nov 03 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111538):
Is it also the coproduct?

#### [Johan Commelin (Nov 03 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111546):
Nope

#### [Johan Commelin (Nov 03 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111550):
Coproduct is the direct sum, which is also the product

#### [Johan Commelin (Nov 03 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111594):
Tensor product is in fact the coproduct in the category of commutative rings

#### [Kevin Buzzard (Nov 03 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111617):
Yes but for modules over a commutative ring it's a different story. You can see something funny is going on because there aren't natural maps from M to M tensor N or from M tensor N to M

#### [Kevin Buzzard (Nov 03 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111643):
Other than the zero map

#### [Mario Carneiro (Nov 03 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111668):
wait what?

#### [Mario Carneiro (Nov 03 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137111674):
this is a funny product indeed

#### [Kenny Lau (Nov 03 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137112176):
```
1. (M ⊗ N) ⊗ P -> M ⊗ (N ⊗ P)
2. (M ⊗ N) -> P -> M ⊗ (N ⊗ P)
3. M -> N -> P -> M ⊗ (N ⊗ P)
4. M -> N ⊗ P -> M ⊗ (N ⊗ P)

#### [Kenny Lau (Nov 03 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137112714):
`(N ≃ₗ P) -> ((M →ₗ N) ≃ₗ (M →ₗ P))`

#### [Johan Commelin (Nov 03 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137112878):
Are you listing the things that you are currently proving?

#### [Mario Carneiro (Nov 03 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137113439):
I think he's just enumerating type correct statements and looking for inhabited types?

#### [Johan Commelin (Nov 03 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137113487):
Do we have `dual`?

#### [Johan Commelin (Nov 03 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137113493):
Because `M.dual \otimes N = Hom(M,N)` might be an interesting statement...

#### [Kenny Lau (Nov 03 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137113504):
that's just `M ->L R`

#### [Kenny Lau (Nov 03 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137113549):
and what you said is only true for M finitely dimensional vector space

#### [Johan Commelin (Nov 03 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137113551):
Of course, but it is a useful concept.

#### [Johan Commelin (Nov 03 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137113555):
I'm probably missing some hypotheses...

#### [Mario Carneiro (Nov 03 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137113557):
don't let truth get in the way of beauty

#### [Kenny Lau (Nov 03 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114111):
```lean
protected def assoc : (M ⊗ N) ⊗ P ≃ₗ M ⊗ (N ⊗ P) :=
linear_equiv.of_linear
  (lift $ lift $ comp (unlift' _ _ _ _) $ unlift id)
  (lift $ comp (lift' _ _ _ _) $ unlift $ unlift id)
  (lift.ext' $ linear_map.ext $ λ m, lift.ext' $ bilinear_map.ext $ λ n p,
    by repeat { rw lift.tmul <|> rw comp₃_apply <|> rw comp_apply <|> rw mk_apply <|>
        rw lift'_apply <|> rw comm'_apply <|> rw unlift_apply <|> rw unlift'_apply <|> rw id_apply })
  (lift.ext' $ comm_inj $ linear_map.ext $ λ p, lift.ext' $ bilinear_map.ext $ λ m n,
    by repeat { rw lift.tmul <|> rw comp₃_apply <|> rw comp_apply <|> rw comm_apply <|> rw mk_apply <|>
        rw lift'_apply <|> rw comm'_apply <|> rw unlift_apply <|> rw unlift'_apply <|> rw id_apply })
```

#### [Johan Commelin (Nov 03 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114113):
@**Kenny Lau** How far are we from defining the category of commutative `R`-algebras?

#### [Kenny Lau (Nov 03 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114114):
oh well

#### [Kenny Lau (Nov 03 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114116):
what's the concrete version of your question?

#### [Johan Commelin (Nov 03 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114155):
Flat ring homs

#### [Kenny Lau (Nov 03 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114159):
```lean
@[reducible] def bilinear_map := M →ₗ N →ₗ P
```

#### [Kenny Lau (Nov 03 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114160):
should we just remove `bilinear_map` entirely?

#### [Johan Commelin (Nov 03 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114169):
I think we can leave it out till people start complaining.

#### [Johan Commelin (Nov 03 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114173):
I would encourage everyone to use linear maps out of the tensor product.

#### [Johan Commelin (Nov 03 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114231):
Anyway, I would be really happy if we have flat ring homs. Especially if it is readable, instead of the obfuscated kludge that we sometimes see... I think flat ring homs can be a good test case to see if mathlib is ready for the 25 other properties of ring homs that algebraic geometry depends upon.

#### [Kenny Lau (Nov 03 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114271):
what are the 25 other properties?

#### [Kenny Lau (Nov 03 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114278):
```lean
def map (f : M →ₗ P) (g : N →ₗ Q) : M ⊗ N →ₗ P ⊗ Q :=
lift $ comp₁ (comp₂ (mk _ _ _) g) f
```
man my interface is really good

#### [Johan Commelin (Nov 03 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114317):
https://stacks.math.columbia.edu/tag/02WE most of these have an equivalent for rings

#### [Kenny Lau (Nov 03 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114408):
```lean
def map (f : M →ₗ P) (g : N →ₗ Q) : M ⊗ N →ₗ P ⊗ Q :=
lift $ comp₁ (comp₂ (mk _ _ _) g) f

@[simp] theorem map_tmul (f : M →ₗ P) (g : N →ₗ Q) (m : M) (n : N) :
  map f g (m ⊗ₜ n) = f m ⊗ₜ g n :=
rfl
```
how on earth is this `rfl`

#### [Mario Carneiro (Nov 03 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114472):
of course it is, it's a quotient

#### [Kenny Lau (Nov 03 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114480):
well then why isn't this `rfl`:
```lean
@[simp] lemma lift.tmul (x y) :
  lift f (x ⊗ₜ y) = f x y :=
```

#### [Kenny Lau (Nov 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114580):
```lean
@[simp] lemma lift.tmul (x y) :
  lift f (x ⊗ₜ y) = f x y :=
zero_add _
```

#### [Kenny Lau (Nov 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114583):
I guess that's why

#### [Mario Carneiro (Nov 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114587):
where'd that come from?

#### [Kenny Lau (Nov 03 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114639):
the free group

#### [Chris Hughes (Nov 03 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114640):
```quote
```lean
@[simp] lemma lift.tmul (x y) :
  lift f (x ⊗ₜ y) = f x y :=
zero_add _
```
```
I love proofs like this.

#### [Mario Carneiro (Nov 03 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114643):
`free_abelian_group.lift` also isn't `rfl`

#### [Kenny Lau (Nov 03 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114655):
right

#### [Kenny Lau (Nov 03 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114656):
it's zero_add as well

#### [Mario Carneiro (Nov 03 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114700):
but why? It's built out of pieces that are rfl

#### [Mario Carneiro (Nov 03 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114702):
is it `free_group.to_group`?

#### [Mario Carneiro (Nov 03 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114716):
ah yes

#### [Mario Carneiro (Nov 03 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114756):
```
def to_group.aux : list (α × bool) → β :=
λ L, list.prod $ L.map $ λ x, cond x.2 (f x.1) (f x.1)⁻¹

def to_group : free_group α → β :=
quot.lift (to_group.aux f) $ λ L₁ L₂ H, red.step.to_group H
```

#### [Mario Carneiro (Nov 03 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114760):
```
@[simp] lemma to_group.of {x} : to_group f (of x) = f x :=
one_mul _
```

#### [Kenny Lau (Nov 03 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114810):
so it's all in `list.prod`

#### [Kenny Lau (Nov 03 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114879):
under which semantics is `by simp; simp only [linear_equiv.apply_symm_apply]` supposed to work where `by simp [linear_equiv.apply_symm_apply]` fails?

#### [Mario Carneiro (Nov 03 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114881):
lol, now this has got me thinking about rewriting `free_group` again

#### [Mario Carneiro (Nov 03 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114931):
one way to get the right defeqs here is to have the actual definition of `free_group` be the quotient of expressions in the language of groups with the group laws, and then prove that this is isomorphic to lists

#### [Kenny Lau (Nov 03 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114932):
and how would one implement "expressions"?

#### [Mario Carneiro (Nov 03 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114933):
expressions in the language of groups means trees

#### [Mario Carneiro (Nov 03 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114935):
you just have a symbol for one and inv and mul

#### [Mario Carneiro (Nov 03 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114977):
and the basis elements

#### [Mario Carneiro (Nov 03 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114979):
and you get trees

#### [Kenny Lau (Nov 03 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114980):
and what do you mean by tree?

#### [Mario Carneiro (Nov 03 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114987):
```
inductive group_expr (A) : Type
| one : group_expr
| inv : group_expr -> group_expr
| mul : group_expr -> group_expr -> group_expr

#### [Kenny Lau (Nov 03 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137114999):
aha

#### [Kenny Lau (Nov 03 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115007):
how would that help?

#### [Mario Carneiro (Nov 03 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115008):
if you define this as  an inductive, and define the relations as a quotient, you will get really nice defeq

#### [Mario Carneiro (Nov 03 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115051):
`lift (x * y) = lift x * lift y`, `lift 1 = 1`, `lift x = f x`

#### [Kenny Lau (Nov 03 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115052):
I don't see how this is different from redefining `list.prod` so that `list.prod [f]` is definitionally equivalent to `f`?

#### [Kenny Lau (Nov 03 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115054):
oh

#### [Kenny Lau (Nov 03 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115056):
fair enough

#### [Johan Commelin (Nov 03 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115068):
```quote
one way to get the right defeqs here is to have the actual definition of `free_group` be the quotient of expressions in the language of groups with the group laws, and then prove that this is isomorphic to lists
```
Wait... in the other thread you said we shouldn't focus on getting all the right defeqs... :sad:

#### [Mario Carneiro (Nov 03 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115069):
lol

#### [Mario Carneiro (Nov 03 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115071):
sometimes it matters

#### [Mario Carneiro (Nov 03 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115081):
The reason quotient types exist is because of defeqs

#### [Mario Carneiro (Nov 03 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115116):
otherwise we would just use sets of sets

#### [Johan Commelin (Nov 03 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115127):
/me doesn't follow... noob alert...

#### [Mario Carneiro (Nov 03 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115130):
there is no way to build quotient types like lean's without an axiom

#### [Mario Carneiro (Nov 03 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115169):
we can get something provably isomorphic, but it won't have the defeq on lift

#### [Johan Commelin (Nov 03 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115173):
I probably haven't experience the pain of working without lean's quotient types... what is wrong with sets of sets?

#### [Mario Carneiro (Nov 03 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115182):
It allows you to define functions that have a certain behavior by definition on the basis elements

#### [Mario Carneiro (Nov 03 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115224):
You can live without defeq, in set theory they do this

#### [Kenny Lau (Nov 03 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115225):
@**Mario Carneiro** so, are you going to do it, or do you intend me to do it? :P

#### [Mario Carneiro (Nov 03 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115226):
but it is nice to have for computational purposes

#### [Mario Carneiro (Nov 03 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115235):
I think I have enough major projects to do :) Like Johan says, it's not essential

#### [Kenny Lau (Nov 03 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115237):
ok

#### [Mario Carneiro (Nov 03 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115239):
but if it interests you, feel free

#### [Johan Commelin (Nov 03 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115242):
I encourage both of you to first get this merged into mathlib before embarking on new projects...

#### [Johan Commelin (Nov 03 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115287):
(or expanding the scope of this refactor)

#### [Kenny Lau (Nov 03 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115306):
ok I pushed the tensor product

#### [Kenny Lau (Nov 03 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115308):
@**Mario Carneiro** should we PR it now?

#### [Mario Carneiro (Nov 03 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115350):
sure, that will give it more exposure

#### [Kenny Lau (Nov 03 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115356):
more exposure to what?

#### [Mario Carneiro (Nov 03 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115365):
people with ideas

#### [Mario Carneiro (Nov 03 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115406):
or who like to read about new things on github

#### [Mario Carneiro (Nov 03 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115409):
obviously I'm already aware of this PR, and I will merge it when ready

#### [Kenny Lau (Nov 03 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115420):
and when is it ready?

#### [Mario Carneiro (Nov 03 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115514):
when I am satisfied with all the changes? It was unfinished when I last reviewed it

#### [Mario Carneiro (Nov 03 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137115519):
thank you for fixing the bugs, but some things still take time

#### [Patrick Massot (Nov 03 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137120657):
Thank you very much @**Kenny Lau** for the documentation effort (and help with actual Lean)! Should we already copy that to [docs/theories/linear_algebra](https://github.com/leanprover/mathlib/blob/master/docs/theories/linear_algebra.md) or could it still change?

#### [Kenny Lau (Nov 03 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137120659):
It could still change

#### [Patrick Massot (Nov 03 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137120699):
Ok. It would be very useful if you could update it when it will stabilize, so that we'll be able to incorporate it to the docs

#### [Kenny Lau (Nov 03 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137130652):
@**Mario Carneiro** ok I pushed the refactored `free_group.lean`

#### [Kenny Lau (Nov 03 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137130654):
(it won't build now; I'll fix the errors if you like the new `free_group`)

#### [Kenny Lau (Nov 03 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137131106):
also, I don't understand why it is ok that `linear_map` doesn't take the ring as an argument

#### [Kenny Lau (Nov 03 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137131918):
ok I put the free group in [a new branch](https://github.com/leanprover-community/mathlib/tree/module-with-free-group) and resetted the PR'ed branch

#### [Kevin Buzzard (Nov 04 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166041):
So I thought I'd try and get the hang of modules in Lean. Is this construction somewhere in the module branch:

```lean
import linear_algebra.basic

example (R S : Type) [comm_ring R] [comm_ring S] (f : R → S) [is_ring_hom f] (M : Type)
  [add_comm_group M] (HM : module S M) : module R M := sorry
```
?

#### [Kevin Buzzard (Nov 04 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166228):
Idly trying to prove it myself:
```lean
import linear_algebra.basic

example (R S : Type) [comm_ring R] [comm_ring S] (f : R → S) [is_ring_hom f] (M : Type)
  [add_comm_group M] [HM : module S M] : module R M :=
{ smul_add := sorry,
  add_smul := sorry,
  mul_smul := sorry,
  one_smul := sorry,
  zero_smul := sorry,
  smul_zero := sorry
}
/-

failed to synthesize type class instance for
R S : Type,
_inst_1 : comm_ring R,
_inst_2 : comm_ring S,
f : R → S,
_inst_3 : is_ring_hom f,
M : Type,
_inst_4 : add_comm_group M,
HM : module S M
⊢ has_scalar R M

-/
```

#### [Chris Hughes (Nov 04 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166337):
It's a new structure. Don't you just have to define a `has_scalar` instance first?

#### [Kevin Buzzard (Nov 04 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166359):
```lean
import linear_algebra.basic

instance has_scalar_of_ring_hom (R S : Type) [comm_ring R] [comm_ring S] (f : R → S) [is_ring_hom f] (M : Type) [has_scalar S M] :
has_scalar R M := {
  smul := λ r m, (f r) • m
}

example (R S : Type) [comm_ring R] [comm_ring S] (f : R → S) [is_ring_hom f] (M : Type)
  [add_comm_group M] [HM : module S M] : module R M :=
{ smul_add := sorry,
  add_smul := sorry,
  mul_smul := sorry,
  one_smul := sorry,
  zero_smul := sorry,
  smul_zero := sorry
}
-- maximum class-instance resolution depth has been reached
```

My question is whether this is already in the module refactoring, which I think was to a certain extent inspired by the fact that this used to be hard to do

#### [Chris Hughes (Nov 04 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166407):
I don't think type class inference knows how to infer `f`. Try making the first things a def, and then giving `to_has_scalar` or whatever explicitly. Thinking about it, I don't think the second thing can be an instance with the current setup either.

#### [Kevin Buzzard (Nov 04 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166579):
Oh this is exactly one of those situations where I don't know how to put something into the type class inference machine because I'm in term mode.

#### [Chris Hughes (Nov 04 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166582):
`by haveI := _; exact _`

#### [Kevin Buzzard (Nov 04 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166634):
```lean
import linear_algebra.basic

def has_scalar_of_ring_hom (R S : Type) [comm_ring R] [comm_ring S] (f : R → S) [is_ring_hom f] (M : Type) [has_scalar S M] :
has_scalar R M := {
  smul := λ r m, (f r) • m
}

example (R S : Type) [comm_ring R] [comm_ring S] (f : R → S) [is_ring_hom f] (M : Type)
  [add_comm_group M] [HM : module S M] : module R M :=
  begin haveI := has_scalar_of_ring_hom R S f M,
  exact 
{ smul_add := sorry,
  add_smul := sorry,
  mul_smul := sorry,
  one_smul := sorry,
  zero_smul := sorry,
  smul_zero := sorry
}
end
```

#### [Kevin Buzzard (Nov 04 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166635):
no errors :D

#### [Kevin Buzzard (Nov 04 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166642):
so I have to go into tactic mode to put something into the type class inference machine?

#### [Chris Hughes (Nov 04 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166648):
I think so.

#### [Chris Hughes (Nov 04 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166690):
This should also work I think.
```lean
example (R S : Type) [comm_ring R] [comm_ring S] (f : R → S) [is_ring_hom f] (M : Type)
  [add_comm_group M] [HM : module S M] : module R M :=
{ to_has_scalar := has_scalar_of_ring_hom R S f M, 
  smul_add := sorry,
  add_smul := sorry,
  mul_smul := sorry,
  one_smul := sorry,
  zero_smul := sorry,
  smul_zero := sorry }
end
```

#### [Kevin Buzzard (Nov 04 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166812):
Now I have problems with two smuls. @**Kenny Lau** Is this done already? I don't want to waste my time if it's already there, but this is exactly what I have always needed for Hilbert basis.

#### [Chris Hughes (Nov 04 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166821):
I would wait until after module refactorign

#### [Kenny Lau (Nov 04 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166822):
the right thing to do is just say smul := sorry, right

#### [Kenny Lau (Nov 04 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166823):
no, this hasn’t been done

#### [Kevin Buzzard (Nov 04 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166867):
I thought module refactoring had happened

#### [Kenny Lau (Nov 04 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166871):
you should also read my summary of the changes, this is mentioned there

#### [Kenny Lau (Nov 04 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166872):
and also you should use module.of_core

#### [Kenny Lau (Nov 04 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166873):
and also you should use module.of_core

#### [Kevin Buzzard (Nov 04 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166874):
I thought I had read your summary of the changes :-/

#### [Kevin Buzzard (Nov 04 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137166884):
Chris your version is better:
```lean
example (R S : Type) [comm_ring R] [comm_ring S] (f : R → S) [is_ring_hom f] (M : Type)
  [add_comm_group M] [HM : module S M] : module R M :=
{ to_has_scalar := has_scalar_of_ring_hom R S f M,
  smul_add := λ r x y,smul_add (f r) x y, -- works
  add_smul := sorry,
  mul_smul := sorry,
  one_smul := sorry,
  zero_smul := sorry,
  smul_zero := sorry }

example (R S : Type) [comm_ring R] [comm_ring S] (f : R → S) [is_ring_hom f] (M : Type)
  [add_comm_group M] [HM : module S M] : module R M :=
by haveI := has_scalar_of_ring_hom R S f M;
  exact 
{ smul_add := λ r x y, smul_add (f r) x y, -- fails
  add_smul := sorry,
  mul_smul := sorry,
  one_smul := sorry,
  zero_smul := sorry,
  smul_zero := sorry
}
```

#### [Kevin Buzzard (Nov 04 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137167005):
I see. I think Kenny is pointing out that by "The idiom for making an instance module α β (after proving that β is an abelian group) is module.of_core" he means the strong statement that end users should actually never make modules directly. Is that right Kenny? I still need an instance of `module R M` though -- how do I get it?

#### [Kevin Buzzard (Nov 04 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137167057):
```lean
example (R S : Type) [comm_ring R] [comm_ring S] (f : R → S) [is_ring_hom f] (M : Type)
  [add_comm_group M] [HM : module S M] : module R M := module.of_core {
    smul := sorry,
    smul_add := sorry,
    add_smul := sorry,
    mul_smul := sorry,
    one_smul := sorry
  }
```
Maybe I'm on the right lines now

#### [Kenny Lau (Nov 04 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137167070):
right

#### [Kevin Buzzard (Nov 04 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137167310):
```lean
    add_smul := λ r s m, -- (is_ring_hom.map_add f).symm ▸ (add_smul (f r) (f s) m), -- stupid triangle never works for me
      begin show f (r + s) • m = f r • m + f s • m, rw is_ring_hom.map_add f, exact add_smul (f r) (f s) m,end,
```

#### [Kenny Lau (Nov 04 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137167371):
i think you are missing two arguments

#### [Kevin Buzzard (Nov 04 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137167450):
```lean
import linear_algebra.basic

example (R S : Type) [comm_ring R] [comm_ring S] (f : R → S) [is_ring_hom f] (M : Type)
  [add_comm_group M] [HM : module S M] : module R M := module.of_core {
    smul := λ r m, (f r) • m,
    smul_add := λ r, smul_add $ f r,
    add_smul := λ r s m, -- (is_ring_hom.map_add f).symm ▸ (add_smul (f r) (f s) m), -- stupid triangle never works for me
      begin show f (r + s) • m = f r • m + f s • m, rw is_ring_hom.map_add f, exact add_smul (f r) (f s) m,end,
    mul_smul := λ r s m, begin show f (r * s) • m = f r • (f s • m), rw is_ring_hom.map_mul f, exact mul_smul (f r) (f s) m,end,
    one_smul := λ m, begin show f 1 • m = m, rw is_ring_hom.map_one f, exact one_smul m, end
  }
```
Still haven't lost my touch ;-) [ugh]

#### [Kevin Buzzard (Nov 04 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137167457):
well so far I got 0% of the way through proving Hilbert basis, but at least I learnt not to use `module`

#### [Kevin Buzzard (Nov 04 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137167736):
Does this completely fundamental fact have a name?

Current version:

```lean
import linear_algebra.basic

instance module_of_module_of_ring_hom {R : Type*} [ring R] {S : Type*} [ring S] (f : R → S) [is_ring_hom f] {M : Type*}
  [add_comm_group M] [HM : module S M] : module R M := module.of_core {
    smul := λ r m, (f r) • m,
    smul_add := λ r, smul_add $ f r,
    add_smul := λ r s m, -- (@is_ring_hom.map_add _ _ _ _ f _ r s) ▸ (add_smul (f r) (f s) m), -- stupid triangle never works for me
      begin show f (r + s) • m = f r • m + f s • m, rw is_ring_hom.map_add f, exact add_smul (f r) (f s) m,end,
    mul_smul := λ r s m, begin show f (r * s) • m = f r • (f s • m), rw is_ring_hom.map_mul f, exact mul_smul (f r) (f s) m,end,
    one_smul := λ m, begin show f 1 • m = m, rw is_ring_hom.map_one f, exact one_smul m, end
  }
```

#### [Kevin Buzzard (Nov 04 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137167788):
rw doesn't do unfolding (i.e. if I tell it `rw H` with `H : X = Y` and `X` isn't directly in view, it won't start unfolding things in an attempt to find `X`, even if something immediately unfolds to give `X`). Is the same true for the stupid triangle?

#### [Chris Hughes (Nov 04 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137167790):
Yes. What about `erw`

#### [Kevin Buzzard (Nov 04 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137167798):
I still seem to need the `show` for `add_smul`.

#### [Kevin Buzzard (Nov 04 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137167925):
`    add_smul := λ r s m, (((@is_ring_hom.map_add _ _ _ _ f _ r s).symm ▸ (add_smul (f r) (f s) m)) :  f (r + s) • m = f r • m + f s • m),`

#### [Kevin Buzzard (Nov 04 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137167926):
longer than the tactic proof ;-)

#### [Johan Commelin (Nov 04 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137167940):
It ought to be `by tidy`.

#### [Kevin Buzzard (Nov 04 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137167986):
does `tidy` know to try a theorem called `add_smul` when proving something called `add_smul`?

#### [Johan Commelin (Nov 04 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137167991):
Only if it is a simp-lemma

#### [Johan Commelin (Nov 04 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137168005):
But maybe, once backwords reasoning is merged, this could realistically done by `tidy`.

#### [Kevin Buzzard (Nov 04 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137168971):
Will this instance ever trigger?

#### [Chris Hughes (Nov 04 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137170222):
I doubt it. It will have to find a ring hom out of nowhere.

#### [Kenny Lau (Nov 04 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137170360):
maybe we should make ring_hom just like linear_map

#### [David Michael Roberts (Nov 04 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/137171588):
```quote
is Mod(R) a CCC?
```
No, because the monoidal structure is not cartesian. What you want is https://ncatlab.org/nlab/show/closed+monoidal+category

#### [Kenny Lau (Nov 05 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145302840):
(deleted)

#### [Kenny Lau (Nov 05 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145302841):
(deleted)

#### [Mario Carneiro (Nov 05 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145303310):
okay, my other obligations are done, so I'm working on finishing the refactoring tonight

#### [Kenny Lau (Nov 05 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145303430):
```lean
import data.polynomial

local attribute [instance, priority 1] classical.prop_decidable

universes u v w

open polynomial

theorem leading_term_aux {R} [nonzero_comm_ring R] {f g : polynomial R} (Hle : nat_degree f ≤ nat_degree g)
  (Hf : f ≠ 0) (Hg : g ≠ 0) (Hh : leading_coeff f + leading_coeff g ≠ 0) :
leading_coeff (f * X ^ (nat_degree g - nat_degree f) + g) = leading_coeff f + leading_coeff g :=
sorry

def ideal.leading_coeff {R : Type u} [nonzero_comm_ring R] (I : ideal (polynomial R)) : ideal R :=
{ carrier := leading_coeff '' I,
  zero := ⟨0, I.zero_mem, rfl⟩,
  add := λ a b ⟨f, hf1, hf2⟩ ⟨g, hg1, hg2⟩, sorry/-begin
    by_cases h0 : a + b = 0, rw h0, exact ⟨0, I.zero_mem, rfl⟩,
    by_cases hf : f = 0, rw [← hf2, ← hg2, hf, leading_coeff_zero, zero_add], exact ⟨g, hg1, rfl⟩,
    by_cases hg : g = 0, rw [← hf2, ← hg2, hg, leading_coeff_zero, add_zero], exact ⟨f, hf1, rfl⟩,
    cases le_total (nat_degree f) (nat_degree g) with hd hd, -- can't get WLOG to work
    { refine ⟨f * X ^ (nat_degree g - nat_degree f) + g,
        I.add_mem (I.mul_mem_right hf1) hg1, _⟩,
      have := leading_term_aux hd hf hg (by rwa [hf2, hg2]),
      rwa [hf2, hg2] at this },
    { refine ⟨g * X ^ (nat_degree g - nat_degree f) + f,
        I.add_mem (I.mul_mem_right hg1) hf1, _⟩,
      have := leading_term_aux hd hg hf (by rwa [hf2, hg2, add_comm]),
      rwa [hf2, hg2] at this }
  end-/,
  smul := λ c a ⟨f, hf1, hf2⟩, begin
    by_cases hcr : c • a = 0, rw hcr, exact ⟨0, I.zero_mem, rfl⟩,
    refine ⟨C c * f, I.mul_mem_left hf1, _⟩,
    have : leading_coeff (C c) * leading_coeff f ≠ 0,
    { rwa [leading_coeff_C, hf2, ← smul_eq_mul] },
    rw [leading_coeff_mul' this, leading_coeff_C, hf2, smul_eq_mul]
  end }
```

#### [Kenny Lau (Nov 05 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145303431):
@**Mario Carneiro** why does this time out?

#### [Mario Carneiro (Nov 05 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145303491):
polynomials have had problems with long elaboration in the past

#### [Mario Carneiro (Nov 05 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145303494):
check that it isn't doing any crazy typeclass searches?

#### [Kenny Lau (Nov 05 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145303620):
it's searching for `has_one nat` and `has_add nat` like a billion times

#### [Mario Carneiro (Nov 05 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145303719):
still profiling (slow business, of course) but it looks like the second block takes much longer than the first

#### [Kenny Lau (Nov 05 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145303725):
oh, thanks

#### [Kenny Lau (Nov 05 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145303733):
@**Kevin Buzzard** should I push what I have in my kmb_hilbert_basis?

#### [Mario Carneiro (Nov 05 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145303748):
it takes 3.5 seconds with the sorry in, which is bad but not that bad so I guess you are worried about the commented out bit

#### [Kenny Lau (Nov 05 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145303805):
but why does `polynomial` have long elaboration time?

#### [Mario Carneiro (Nov 05 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145304062):
If I replace the last `rwa` in the second block with `rw`, the final state is:
```
...
this : leading_coeff (g * X ^ (nat_degree f - nat_degree g) + f) = b + a
⊢ leading_coeff (g * X ^ (nat_degree g - nat_degree f) + f) = a + b
```
I'm not sure how assumption is supposed to close that

#### [Kenny Lau (Nov 05 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145304145):
ah

#### [Mario Carneiro (Nov 05 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145304160):
it's probably taking forever unfolding all the things to see if those are actually the same

#### [Kenny Lau (Nov 05 2018 at 08:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145304269):
should I add two submodules together?

#### [Kenny Lau (Nov 05 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145304491):
```lean
import algebra.module

universes u v

variables {R : Type u} [ring R]
variables {M : Type v} [add_comm_group M] [module R M]

instance submodule.has_add' : has_add (submodule R M) :=
⟨λ N₁ N₂, {
  carrier := { z | ∃ (x ∈ N₁) (y ∈ N₂), x + y = z },
  zero := ⟨0, N₁.zero_mem, 0, N₂.zero_mem, add_zero _⟩,
  add := λ z₁ z₂ ⟨x₁, hx₁, y₁, hy₁, hz₁⟩ ⟨x₂, hx₂, y₂, hy₂, hz₂⟩,
    ⟨x₁ + x₂, N₁.add_mem hx₁ hx₂, y₁ + y₂, N₂.add_mem hy₁ hy₂,
    by rw [← hz₁, ← hz₂, add_assoc, add_left_comm x₂, ← add_assoc]⟩,
  smul := λ c z ⟨x, hx, y, hy, hz⟩,
    ⟨c • x, N₁.smul_mem c hx, c • y, N₂.smul_mem c hy,
    by rw [← hz, smul_add]⟩ }⟩
```

#### [Mario Carneiro (Nov 05 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145304533):
isn't this `\sup`?

#### [Kenny Lau (Nov 05 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145304534):
oh

#### [Kenny Lau (Nov 05 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145304535):
lol

#### [Mario Carneiro (Nov 05 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/145304565):
I realize that ring theorists prefer the notations $$A + B$$ and $$A\cap B$$ to $$A\vee B$$ and $$A\wedge B$$, but I think we should go for more notational uniformity

#### [Kenny Lau (Nov 05 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146784108):
oh, `coeff_is_linear` uses `is_linear_map`, should I refactor that? @**Mario Carneiro**

#### [Kenny Lau (Nov 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146784560):
```lean
def map_mk (I J : ideal α) : ideal I.quotient :=
{ carrier := mk I '' J,
  zero := ⟨0, J.zero_mem, rfl⟩,
  add := by rintro _ _ ⟨x, hx, rfl⟩ ⟨y, hy, rfl⟩;
    exact ⟨x + y, J.add_mem hx hy, rfl⟩,
  smul := by rintro ⟨c⟩ _ ⟨x, hx, rfl⟩;
    exact ⟨c * x, J.mul_mem_left hx, rfl⟩ }
```
I think we can generalize this @**Mario Carneiro**

#### [Mario Carneiro (Nov 05 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146784575):
to what?

#### [Mario Carneiro (Nov 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146784617):
yes on `coeff` btw, you may need a second function though

#### [Kenny Lau (Nov 05 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146785589):
@**Mario Carneiro** and how far away are we from the refactoring?

#### [Mario Carneiro (Nov 05 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146785630):
plan is to finish it today; I am currently rejiggering some stuff with `is_unit` and `nonunits` prompted by some of Rob's applications

#### [Kenny Lau (Nov 05 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146786349):
are you working on a separate branch or a private repo or something? i.e. should I just push to that branch?

#### [Mario Carneiro (Nov 05 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146786408):
I'm working locally, feel free to keep committing to the `module` branch and I'll merge when I push

#### [Kenny Lau (Nov 05 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146786420):
do you want to push your work to the community branches?

#### [Kevin Buzzard (Nov 05 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146786436):
Kenny and I are just chatting on Skype

#### [Kevin Buzzard (Nov 05 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146786437):
For Hilbert basis

#### [Kevin Buzzard (Nov 05 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146786489):
one perhaps needs that there's some inclusion of lattices -- if R -> S is a ring hom and M is an S-module

#### [Kevin Buzzard (Nov 05 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146786501):
then there's an order preserving injection from the lattice of sub-S-modules to the lattice of sub-R-modules

#### [Mario Carneiro (Nov 05 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146786568):
okay, it's broken tho

#### [Kevin Buzzard (Nov 05 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146786582):
A sub-R-module is just a sub-f(R)-module where f(R) is the subring of S

#### [Kevin Buzzard (Nov 05 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146786605):
If R -> S is an injection with M an S-module then there's an injection from the sub-S-modules to the sub-R-modules

#### [Kevin Buzzard (Nov 05 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146786657):
If R -> S is a surjection and M is an R-module then the submodule of M consisting of stuff which is annihiliated by the kernel of R->S is an S-module

#### [Kevin Buzzard (Nov 05 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146786709):
and that way you get an injection from sub-S-modules to sub-R-modules

#### [Kenny Lau (Nov 05 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146787850):
```lean
import data.polynomial

universe u

variables {R : Type u} [comm_ring R] [decidable_eq R]
variable (I : ideal (polynomial R))

def ideal.of_polynomial : submodule R (polynomial R) :=
{ carrier := (@submodule.carrier (polynomial R) (polynomial R) _ _ ring.to_module I : set (polynomial R)),
  zero := sorry, add := sorry, smul := sorry }

def ideal.of_polynomial' : submodule R (polynomial R) :=
{ carrier := (I.carrier : set (polynomial R)), -- doesn't work
  zero := sorry, add := sorry, smul := sorry }
```
@**Mario Carneiro**

#### [Mario Carneiro (Nov 05 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146787867):
it's probably guessing the wrong scalar ring here

#### [Kevin Buzzard (Nov 05 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146787870):
I thought it never had to guess anything nowadays?

#### [Mario Carneiro (Nov 05 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146787918):
that's the next thing on the list after the module refactor

#### [Kevin Buzzard (Nov 05 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146787923):
There's a _list_??

#### [Johan Commelin (Nov 05 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146787928):
I feel there is a need for module refactor 2.0 :rolling_on_the_floor_laughing:

#### [Kevin Buzzard (Nov 05 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146787930):
I never realised modules were so hard :-)

#### [Kenny Lau (Nov 05 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146787987):
yeah that's 'coz you're a mathematician

#### [Mario Carneiro (Nov 05 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146788414):
the list is my todo list, and it's on the list because people want modules to have multiple scalar rings

#### [Kevin Buzzard (Nov 05 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146788582):
I am just trying to formalise various standard results in undergraduate algebra like Hilbert basis and reporting back on what mathematicians use

#### [Mario Carneiro (Nov 05 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146794422):
@**Kenny Lau** @**Johannes Hölzl** The final draft of the module refactor is pushed

#### [Kenny Lau (Nov 05 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146794432):
so... coeff is linear?

#### [Mario Carneiro (Nov 05 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146794653):
it is now

#### [Kenny Lau (Nov 05 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146794754):
thanks

#### [Kevin Buzzard (Nov 05 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146794766):
So how do I make an S-module into an R-module if I have a ring hom $$f : R \to S$$?

#### [Kevin Buzzard (Nov 05 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146794771):
thanks too

#### [Mario Carneiro (Nov 05 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146794880):
Maybe there should be a way to put chosen ring homs in the typeclass infrastructure?

#### [Mario Carneiro (Nov 05 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146794939):
Otherwise you just have to introduce it locally every time

#### [Mario Carneiro (Nov 05 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146794957):
I assume you aren't asking how to define the R-module structure, that's not difficult at all

#### [Johan Commelin (Nov 05 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146795078):
```quote
Maybe there should be a way to put chosen ring homs in the typeclass infrastructure?
```
I think we could also try using a structure `algebra`.

#### [Kevin Buzzard (Nov 05 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146795319):
```quote
I assume you aren't asking how to define the R-module structure, that's not difficult at all
```
Right -- I'm asking for the idiomatic way to do it.

#### [Johannes Hölzl (Nov 05 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146796014):
@**Mario Carneiro**  why  is it now a mixing, i.e. why is the group structure not part of modules anymore?

#### [Mario Carneiro (Nov 05 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146796108):
Because the parent coercion `module R M => add_comm_group M` was causing much of the module typeclass issues

#### [Mario Carneiro (Nov 05 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146796123):
plus if `R` becomes not an `out_param` then it won't even work

#### [Johannes Hölzl (Nov 05 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146802129):
the module PR looks very good to me

#### [Johan Commelin (Nov 05 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146804978):
It's merged :tada: :thumbs_up: :octopus:

#### [Johannes Hölzl (Nov 05 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/module refactoring/near/146804983):
COMMIT 1000

