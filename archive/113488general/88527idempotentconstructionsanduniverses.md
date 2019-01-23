---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88527idempotentconstructionsanduniverses.html
---

## Stream: [general](index.html)
### Topic: [idempotent constructions and universes](88527idempotentconstructionsanduniverses.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135671325):
I think there might be general theory behind this. I will just start with an example:
There is this thing called a *topos*. It shows up in geometry, topology, and also logic. It is the natural category theoretic places where a *sheaf* lives. If you have a topological space `X`, you can form `Sh(X)`: the category of all sheaves on `X`. This is the prototypical example of a topos. It turns out that topological spaces are to restrictive, we need to categorify them, what you get is *sites*: a category `C` together with a *Grothendieck topology* on `C`. Every Grothendieck topos is (by definition) the category of sheaves on some site.
Now here is a cool thing: every topos can be equipped with a *canonical topology*. This means that we can talk about sheaves on a topos. In particular we can form `Sh(Sh(X))`.
It turns out that you don't get anything new if you do this. Except, there is a catch, your universe levels increase. Mathematicians fight their way around this by fixing some `κ` and looking at the topos of `κ`-small sheaves, so that they can stay in the same universe, etc... I am afraid that we cannot escape this issue. (This has nothing to do with willing to work with universes or not. We just *really* don't want "idempotent" operations to bump up universe levels.)
In Lean we have the notion of `fintype`. Is it easy to speak about `ĸ`-small types? Is there a good systematic way to attack problems like this?
Related places where this shows up:
- algebraic closures
- valuation spectrum (to make this "idempotent" you probably have to take the ring of functions on `Spv`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135673434):
Locally presentable categories are a related idea (and a Grothendieck topos is in particular a locally presentable category). A locally $$\kappa$$-presentable category $$C$$ is (among other characterizations) the category of those presheaves on a (small) category $$A$$ which take a designated collection of $$\kappa$$-small cocones in $$A$$ to limit cones in Set. Then it turns out that we can take $$A$$ to be $$C_\kappa$$, the full subcategory of all $$\kappa$$-presentable objects of $$C$$, at least after replacing this by an equivalent small category, together with the collection of all $$\kappa$$-small colimits in $$C_\kappa$$.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135673511):
And you are Leanifying this kind of stuff, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135673531):
My intention is just to formalize $$\kappa$$-smallness as
```lean
variables {α : Type u} (κ : cardinal.{u}) (h : cardinal.mk α < κ)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135673583):
and it seems to be working okay, for example, I mostly proved that $$\kappa$$-filtered colimits can be reduced to $$\kappa$$-directed colimits, which involves a somewhat complicated construction and a bunch of simple cardinality estimates

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135673777):
@**Reid Barton** But do you also have code to turn this into categories that don't increase the universe level?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135673791):
Or is this what you mean with "after replacing this by an equivalent small category"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135673978):
Right, good question. I haven't gotten that far yet but at some point the question will be how to replace something which we know as mathematicians is small or essentially small (like the collection of $$\kappa$$-presentable objects) with something which actually lives in the original universe `u`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674004):
Let me try to think what the simplest example of such a question is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674120):
Right, I think you just rephrased in 3 lines what took me about 30 lines :upside_down:  :thumbs_up:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674180):
I guess a typical example is: given a category C, show there is only a `Type u` of isomorphism classes of diagrams K -> C where K is $$\kappa$$-small and whose image belongs to a specified *set* (i.e., another `Type u`) of objects of C.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674215):
The obvious attempt `structure my_thing := (K : Type u) [small_category K] (F : functor K C) ...` fails immediately because we cannot put a `Type u` in there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674238):
This isn't the simplest example but I think it has most of the interesting ingredients.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674371):
Simpler examples would be things like: prove there is only a set of isomorphism classes of $$\kappa$$-small categories K, or even prove that there is only a set of isomorphism classes of $$\kappa$$-small sets.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674447):
Prove that there is only a set of $$\kappa$$-small algebraic field extensions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674476):
If I understand it correctly, you can just define $$\bar K$$ with Zorn, after you know that fact.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674494):
And it won't have to live in a higher universe.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674536):
But I think we want some kind of general method or bag of tricks for building these up, rather than just doing them all as one-off constructions. But that probably begins by doing the simplest cases as one-off constructions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674588):
Right... that's the kind of thing I'dd like to find out in this thread.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675036):
Okay so let's break your claim down in mind-numbing detail. There is a category of field extensions of K, which I guess is relevant because the conclusion is "every [...] field extension of K is isomorphic [over K] to one selected from [some type]".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675075):
It has a forgetful functor to Set. We're interested in the field extensions whose underlying set is $$\kappa$$-small and which satisfy some other property (algebraic over K) whose details don't matter here I think.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675137):
Well, algebraic implies $$\kappa$$-small.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675164):
If $$\kappa$$ is bigger than the cardinality of the ground field.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675186):
I guess we should say a category C is essentially small when there's an equivalence D -> C with `D : Type u` a small category

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675201):
Oh true, but then the rest of the argument goes through the fact that the extensions we care about are $$\kappa$$-small, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675251):
Yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675292):
So, the subcategory of Set on the $$\kappa$$-small sets is essentially small. This must be some primitive ingredient because it is tied closely to the notion of cardinality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675298):
and surely we can just prove it directly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675343):
Then, we want to argue like: a set can only be made into a field in a set's worth of ways

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675359):
that is just the statement that `discrete_field` has type `Type u -> Type u`, I guess

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675387):
Or here, you could just substitute `algebraic_extension_of k : Type u -> Type u` and then be done with the whole argument at the end of this step.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675565):
So I suppose the missing piece is something like: if F : C' -> C is a functor and the fibers of F.obj are small then the preimage of an essentially small subcategory of C is an essentially small subcategory of C'

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675582):
Well, I didn't state that quite right (that statement is false)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675615):
for this F also needs to be an isofibration, i.e. if FX' = X and X -> Y is an isomorphism in C then it lifts to at least one isomorphism X' -> Y' in C'

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675691):
(aka "transport of structure")

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675886):
I guess I never thought about the fact that this is required. But I think it really is. After all, you *could* define a field extension of K in the same way but then say that the only maps between field extensions are identity maps (not even isomorphisms) and then even though there is only a set of ways to equip each set with a field extension structure, it's no longer true that every $$\kappa$$-small field extension is isomorphic to one from a set of representatives.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135676375):
I think what's going on here is:
1. The pullback of an equivalence D -> C by an isofibration C' -> C is an equivalence D' -> C'. ("The canonical model category structure on Cat is right proper.")
2. We can choose the pullback D' here to belong to Type u. This isn't a general fact about pullbacks because C' belongs to Type (u+1). Instead it is some statement about the way pullbacks interact with `bundled` categories.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677129):
Right. This is looking good. The only problem is that it will take some time to convince Lean of this :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677326):
So I suppose we can hide all the category theory language maybe.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677428):
For each cardinal `k : cardinal.{u}`, there's a type `R k : Type u` and a function `U : R k -> Type u` with the property that every type of cardinality < k is `equiv` to `U r` for some `r : R k`. (`R k` = representatives of isomorphism classes of sets of size < k.) In fact, `R k` is just `k.out` or something.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677528):
Right. Did you just reduce the problem to "transport of structure"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677544):
Then we can define a new structure
```lean
structure kappa_small_algebraic_extension (K : Type u) [discrete_field K] :=
(r : R k)
(str : algebraic_extension_of K (U r))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677609):
and we will need transport of structure to show that every $$\kappa$$-small algebraic extension is "isomorphic" to one that comes from `kappa_small_algebraic_extension`, yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677620):
but then the point is that `kappa_small_algebraic_extension K` is also a `Type u`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677629):
Exactly. That is really nice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677651):
This would allow us to do universe resizing (is this what it is called) for the valuation spectrum, for algebraic closures, etc...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677704):
We probably still want "constructions" in the end. But it is nice to also have this option available.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677731):
And in the case of topoi, I think this is maybe the only option.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135678808):
Maybe we should try to actually prove the existence of algebraic closures modulo whatever field theory results we need (a composition of algebraic extensions is algebraic?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 12 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135679028):
Kenny already did some of that stuff in his LL repo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135695603):
Polynomials are currently quite hard to work with because module refactoring hasn't landed yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135696715):
@**Johan Commelin** I'm actually not sure exactly what proof you had in mind for which you need to know that there is only a set of isomorphism classes of algebraic extensions of K.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135696795):
To apply Zorn's lemma you need a poset, but the collection of algebraic extensions of K only forms a filtered diagram because there will typically be several embeddings $$F \to E$$ between two extensions $$F$$ and $$E$$.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135696807):
Actually it's not even filtered, I guess

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135696994):
http://www2.im.uj.edu.pl/actamath/PDF/30-131-132.pdf has a proof which is the kind of thing I was imagining, but it looks at fields whose underlying set is a subset of some fixed set $$S$$ containing $$K$$, so that there is a partial order defined by inclusion. (Actually the collection $$\mathcal{R}$$ defined there makes no sense as defined, since a subset $$L$$ of $$S$$ is not a field, but it can be fixed by considering pairs of a subset and a field structure on the subset, and defining the poset relation so that $$L \le L'$$ if $$L \subset L'$$ and the inclusion is a field extension.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697233):
http://www.cs.bsu.edu/~hfischer/math412/Closure.pdf seems to be a rather more careful version of the same proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697336):
a construction that needs to deal with set-theoretic issues would be very ugly if implemented, I think.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697340):
it wouldn't be natural.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697437):
I've talked here before about alternatives to cardinal bounds. The key is to find a set (type) that indexes all the relevant objects up to isomorphism

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697497):
I'm talking about the added difficulty and unnaturality when proving the universal properties

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697504):
These things are usually best done on a case by case basis though, which complicates matters

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697532):
Unfortunately, there's nothing that can be done about this Kenny. The perfect system would allow you to just write down these types over an impredicative universe so you get the right universal property, but that's inconsistent

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697597):
The fact that in some particular case you can do it without an impredicative universe is a nontrivial fact that must be proved

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697603):
of course there's something that can be done. That isn't the only construction of algebraic closure. The one that I know has no universe issues.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697621):
The key is picking the right indexing type, like I said

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697630):
if you do it right you don't have universe issues

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697785):
Kenny what is your proof of existence of algebraic closure?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697844):
There's another one where you sort of adjoin roots of all polynomials at once and then use the existence of maximal ideals to form a quotient which is a field

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697905):
Kenny has thought about algebraic closure quite a bit and I'd be interested to hear his response. He did embark upon a construction some weeks ago but had problems using polynomials. I cannot remember the specific issue but I think that we got confirmation from Mario that the issues would be fixed by the module refactoring.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697949):
I am pretty sure that Kenny was going to adjoin all polynomials at once and use the existence of maximal ideals. However there is then the issue that this new field L is only guaranteed to contain all roots of polynomials with coefficients in the original field K.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697951):
@**Reid Barton** So is the idea that every element of the algebraic closure is expressible as a root of some polynomial over the base field?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 12 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697952):
Yes, I read some notes by someone with the initials "KMB" about this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697957):
There are then two ways of proceeding. One is to iterate this construction countably infinitely often and to take a direct limit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698001):
and the other is to work harder and prove that L is algebraically closed anyway.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698014):
But the natural way of doing the latter is I guess via the theory of integral closures.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698018):
I would be inclined to go for the "work harder" route

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698025):
since it keeps the complexity of the object itself down

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698026):
me too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698030):
[and for integral closures you need Hilbert basis and for that you need the module refactoring]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698055):
I need this big lemma that for any polynomial f, there is a separable polynomial h and integer n such that f(x) = h(x^(p^n)), where p is the characteristic of the field (p=1 for Q)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698110):
Now you are talking about separable closure maybe?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698122):
no...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698132):
the proof that L is algebraically closed anyway is to consider M the maximally purely inseparable subextension

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698144):
wait so Q is characteristic 1 now?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698146):
The advantage of doing separable closure would be that you could then state the abelian local Langlands conjectures in full and correct generality.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698156):
and show that every polynomial f in M still has a root in L (by considering f^(p^n) for a large n and observing that (x+y)^p = x^p+y^p so eventually you get a polynomial f^(p^n) in K which has a root in L by construction)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698245):
and then show that every polynomial f in M splits in L, which requires Primitive Element Theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698273):
What is wrong with the proof I'm about to sketch for the fact that L is alg closed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698387):
Say M/L is a finite field extension. Say degree > 1 for a contradiction. Choose m in M not L. Consider the min poly p(x) of m. Its coefficients generate a finite extension K' of K. Now K'(m) is a finite extension of K, so m has a min poly over K. But we already added the roots of all the polys with coefficients in K.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698441):
I only added one root

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698449):
Is this a serious issue?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698466):
I see what you mean though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698503):
also I can shorten "Say M/L is a finite field extension. Say degree > 1 for a contradiction. Choose m in M not L. Consider the min poly p(x) of m" to "consider an irred. poly. p in L[X]"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698564):
Yes, I was just spelling it out because your comment made me wonder where my mistake was.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698569):
So we are reduced to showing that L is normal or something like that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698606):
I still don't see why K'(m) is a finite extension of K

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698674):
oh that's just because K'/K was generated by finitely many elements of L over K and L/K is algebraic.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698692):
ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698695):
Do you need the theory of integral extensions here? Sum of two elements integral over K is integral over K?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698778):
Honestly this code should be waiting until after the module refactoring :-/

