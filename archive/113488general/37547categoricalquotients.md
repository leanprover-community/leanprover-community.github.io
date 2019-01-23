---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37547categoricalquotients.html
---

## Stream: [general](index.html)
### Topic: [categorical quotients](37547categoricalquotients.html)

---


{% raw %}
#### [ Scott Morrison (Apr 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870843):
Is everyone ready for a new puzzle about how to formalise things mathematicians use without thinking about? :-)

#### [ Scott Morrison (Apr 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870844):
I would like to define a notion of a "categorical quotient".

#### [ Scott Morrison (Apr 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870846):
Recall that a quotient of a type `X` by a relation `R` is a type `Y`, which is pretty much useless, _except_ that we can construct functions `Y -> Z` by giving two pieces of data:

#### [ Scott Morrison (Apr 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870847):
1. a function `f : X -> Z`, and
2. a proof that `R x x' -> (f x = f x')`.

#### [ Scott Morrison (Apr 30 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870848):
I want instead a categorical quotient of a type `X` by a relation `R`, let's call it `Q` which is useless except that we can construct functions `Q -> C`, where `C` are the objects of some category, by giving three pieces of data:

#### [ Scott Morrison (Apr 30 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870849):
1. a function `f : X -> C`,
2. for each `R x x'`, an isomorphism `φ x x' : f x ≅ f x'`, and
3. for each `x x' x''` so that `R x x'` and `R x' x''` (and so automatically `R x x''`), we have `φ x x'` composed with `φ x' x''` is equal to `φ x x''.

#### [ Scott Morrison (Apr 30 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870889):
This says: you are only allowed to make functions out of `Q` that are independent of choices of representative _up to coherent isomorphisms_.

#### [ Scott Morrison (Apr 30 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870890):
So --- how do I do this in Lean?

#### [ Scott Morrison (Apr 30 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870891):
(The point of course is hygiene: we can sometimes help make our programs more correct by only using quotient types, when that's all that's needed. Unfortunately quotient types are a bit too restrictive for what actually happens in the real world.)

#### [ Scott Morrison (Apr 30 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125870892):
(And no, it not useful in this situation to merely define functions to the isomorphism classes of objects of `C`, which is something you could do with a plain quotient and data 1-3.)

#### [ Scott Morrison (Apr 30 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125871041):
(A categorical quotient is at least as good as a quotient: you can take `C` to be a discrete category, where the only (iso)morphisms are identities, and this recovers the usually construction of function out of a quotient.)

#### [ Kevin Buzzard (Apr 30 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882176):
Is this a non-trivial problem in dependent type theory?

#### [ Kevin Buzzard (Apr 30 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882177):
Is there a chance that it is not possible to define such a quotient?

#### [ Kevin Buzzard (Apr 30 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882240):
Note that Scott's question is really flagging the difference between and equivalence relation, and `equiv`. The statement that two terms in a setoid are equivalent is a proposition. However an instance of `equiv x y` really is data, and to a mathematician sometimes that data really is important.

#### [ Mario Carneiro (Apr 30 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882310):
There is a piece missing from the specification: what property do you get from those lift functions `Q -> C`?

#### [ Johan Commelin (Apr 30 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882354):
They fit in a commutative diagram

#### [ Mario Carneiro (Apr 30 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882404):
of course, but what is it exactly?

#### [ Johan Commelin (Apr 30 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882405):
So, there is a quotient map `q : X -> Q`, and the map `g : Q -> C` that you have obtained is such that `f` is *equal* to `g \circ q`

#### [ Johan Commelin (Apr 30 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882407):
I guess that *equal* does not mean defeq but only provable equality in a set of morphisms in the category

#### [ Mario Carneiro (Apr 30 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882518):
What prevents the definition `Q := X` and `lift f := f`?

#### [ Mario Carneiro (Apr 30 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882624):
I guess in the plain quotient case you have `quot.sound : R x y -> q x = q y`, so here you want `sound : R x y -> q x ~= q y`; then presumably `transport  (lift f φ) (sound (h : R x y)) = φ x y`

#### [ Johan Commelin (Apr 30 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882764):
Wait, so now we are merging two themes? (-;

#### [ Johan Commelin (Apr 30 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882778):
But, to answer your question about `Q := X`. I should have added that the quotient map `q` should also satisfy points 2 and 3 from Scott's post.

#### [ Johan Commelin (Apr 30 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882819):
So `Q` is the universal gadget among all the data that satisfies 1, 2, and 3

#### [ Johan Commelin (Apr 30 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125882826):
Also, it does not need to exist in all situations. Its existence is a theorem that has to be proven.

#### [ Mario Carneiro (Apr 30 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883456):
How can its existence be conditional? It doesn't have a category as input, so either Lean can prove these things exist in general or not

#### [ Johan Commelin (Apr 30 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883461):
```quote
I want instead a categorical quotient of a type `X` by a relation `R`, let's call it `Q` which is useless except that we can construct functions `Q -> C`, **where `C` are the objects of some category**, by giving three pieces of data:
```
(emphasis mine)

#### [ Johan Commelin (Apr 30 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883462):
So, there is some category lurking in the background

#### [ Scott Morrison (Apr 30 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883463):
But Johan, it's not a fixed category.

#### [ Scott Morrison (Apr 30 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883464):
(I think? Maybe I'm confused about my own question. I wanted that description to hold for any category `C`.)

#### [ Johan Commelin (Apr 30 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883465):
Ok... then I'm confused

#### [ Mario Carneiro (Apr 30 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883505):
`C` plays the role of beta in `quot.lift`

#### [ Scott Morrison (Apr 30 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883509):
Yes.

#### [ Johan Commelin (Apr 30 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883515):
So, maybe Q always exists, but it is not always an object of *some category*

#### [ Johan Commelin (Apr 30 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883520):
Because it only lives in some cocompletion of *said category*

#### [ Mario Carneiro (Apr 30 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883530):
I don't think there is a requirement that `Q`be an element of `C`

#### [ Mario Carneiro (Apr 30 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883575):
It's just some type, with a function to the objects of `C`

#### [ Mario Carneiro (Apr 30 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883576):
it's the index category for a diagram in `C`

#### [ Johan Commelin (Apr 30 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883583):
Ok, got it

#### [ Mario Carneiro (Apr 30 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883625):
Hm, there's a problem interpreting `Q` as a category: what are the equivs?

#### [ Mario Carneiro (Apr 30 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883674):
If `Q` is the universal thing satisfying 1-3, then we can slot `q` in for `f`, `Q` for `C`, and `sound` for `φ` to get the properties expected of `Q` itself, but then this means that `sound x x' : q x ~= q x'` and this doesn't make any sense since `q x : Q` is not a type

#### [ Johan Commelin (Apr 30 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883724):
Ok, I'm confused again...

#### [ Johan Commelin (Apr 30 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883727):
First I thought that Scott was trying to formalise some colimit inside some category

#### [ Johan Commelin (Apr 30 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883730):
But now it seems he wants to do something more general?

#### [ Johan Commelin (Apr 30 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883776):
Scott, is this an example of what you try to achieve: taking the quotient of all groups by the relation of isomorphism?

#### [ Johan Commelin (Apr 30 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883782):
But that is not coherent, I guess

#### [ Mario Carneiro (Apr 30 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/125883785):
I suspect what Scott wants to do is not possible unless you make a lot of non-canonical choices, but I await a full specification first

#### [ Kevin Buzzard (May 02 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/126004937):
This is very much related to all this canonical stuff I'm thinking about, so I would be interested in bumping this thread. I've only seen the notion of categorical quotient in algebraic geometry, where it looks like this: https://en.wikipedia.org/wiki/Categorical_quotient

#### [ Kevin Buzzard (May 02 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/categorical%20quotients/near/126005124):
But here it's not just a relation on the object X you want to quotient, there is a group action. @**Scott Morrison** did you need something more general than this? Note that X isn't a type in the version I know, it's an object in the category.


{% endraw %}
