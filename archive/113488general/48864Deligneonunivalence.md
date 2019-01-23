---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48864Deligneonunivalence.html
---

## Stream: [general](index.html)
### Topic: [Deligne on univalence](48864Deligneonunivalence.html)

---

#### [Johan Commelin (Sep 09 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Deligne%20on%20univalence/near/133618998):
http://www.math.ias.edu/calendar/event/138368/1536679800/1536683400

#### [Johan Commelin (Sep 09 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Deligne%20on%20univalence/near/133619046):
For those who don't know Deligne: he is a giant, a hero, archetype of the arithmetic geometer, one of the few ancients that is still with us...

#### [Johan Commelin (Sep 09 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Deligne%20on%20univalence/near/133619056):
M. Harris on this abstract: https://mathematicswithoutapologies.wordpress.com/2018/09/09/univalent-foundations-and-mathematical-practice/

#### [Bryan Gin-ge Chen (Sep 12 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Deligne%20on%20univalence/near/133840719):
[Here's a link to a video of Deligne's talk](https://video.ias.edu/VoevodskyMemConf-2018/0911-PierreDeligne); the other talks for Voevodsky's memorial conference are being uploaded [here](https://video.ias.edu/vladimir).

#### [Johan Commelin (Sep 13 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Deligne%20on%20univalence/near/133860739):
Cool! Thanks for posting this. I couldn't find them.

#### [Kevin Buzzard (Sep 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Deligne%20on%20univalence/near/133868555):
@**Reid Barton** @**Scott Morrison** do either of you have any thoughts on the question Deligne raises in the last 4 or so minutes of the talk, about homotopy groups of sphere?

#### [Reid Barton (Sep 13 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Deligne%20on%20univalence/near/133892924):
I think it's related to the following broad question which I have thought a little bit about.
In homotopy type theory, types have some built-in homotopy structure of course--we can define $$S^n$$ and even do some non-trivial calculations like $$\pi_3(S^2) = \mathbb{Z}/2$$.
On the other hand, inside homotopy type theory we also have a "non-homotopy" type theoretic "universe"--the 0-types, which we can treat as sets. Assuming some classical axioms perhaps, we could then redo classical homotopy theory: we can build the theory of topological spaces, continuous maps, the real numbers, homotopies, spheres, etc., exactly like we do it here in Lean. Alternatively we could pick another model for homotopy theory like simplicial sets, and redo the whole theory classically, and prove in the classical way that simplicial sets and topological spaces define the same homotopy theory.

#### [Reid Barton (Sep 13 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Deligne%20on%20univalence/near/133893246):
What I don't know how to do is to compare the "classical" homotopy theory (built up from sets by topological spaces or simplicial sets or whatever) with the "internal" one which is somehow directly defined using types to represent homotopy types. I'm not even talking about how to prove a theorem that the homotopy theories are equivalent in some sense. I don't know how to define any map in either direction between classical spaces and types-as-homotopy-types.
All I really know how to do is: for any particular finite cell complex, I can write it down as a classical object, and I can also write it down as a higher inductive type, and declare that the correspondence is supposed to send one to the other.

#### [Reid Barton (Sep 13 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Deligne%20on%20univalence/near/133893324):
I don't know how to take an arbitrary simplicial set and write down a corresponding higher inductive type, since I'd need to use infinitely many different constructors to represent the $$n$$-cells for each $$n \ge 0$$.

#### [Reid Barton (Sep 13 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Deligne%20on%20univalence/near/133893557):
If you *could* do this functorially, then you could address Deligne's question. Represent $$\alpha \in \pi_{n+k}(S^n)$$ as a map between some simplicial sets which have the homotopy types of $$S^{n+k}$$ and $$S^n$$. Then, applying this correspondence, you should obtain a map between some types which are equivalent to the internal homotopy types $$S^{n+k}$$ and $$S^n$$. Then precomposition with this map can be identified with a map from the $$n$$-fold loop space of any type $$A$$ to the $$(n+k)$$-fold loop space of $$A$$.

#### [Mario Carneiro (Sep 13 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Deligne%20on%20univalence/near/133893618):
> What I don't know how to do is to compare the "classical" homotopy theory (built up from sets by topological spaces or simplicial sets or whatever) with the "internal" one which is somehow directly defined using types to represent homotopy types. I'm not even talking about how to prove a theorem that the homotopy theories are equivalent in some sense. I don't know how to define any map in either direction between classical spaces and types-as-homotopy-types.

It is questions like this that have prompted the development of "cohesive type theory", which adds a modality called "shape" that converts between a homotopy type and the set that encodes it

#### [Mario Carneiro (Sep 13 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Deligne%20on%20univalence/near/133893637):
I think Mike Shulman is the main force behind it

#### [Mario Carneiro (Sep 13 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Deligne%20on%20univalence/near/133893681):
In standard HoTT I think you can only talk about the correspondence metatheoretically

#### [Patrick Massot (Sep 13 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Deligne%20on%20univalence/near/133894083):
```quote
In homotopy type theory, types have some built-in homotopy structure of course--we can define $$S^n$$ and even do some non-trivial calculations like $$\pi_3(S^2) = \mathbb{Z}/2$$.
```
If that's true in HoTT, I don't want to be part of it

#### [Reid Barton (Sep 13 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Deligne%20on%20univalence/near/133894154):
oops! off by one error

#### [Reid Barton (Sep 13 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Deligne%20on%20univalence/near/133895052):
```quote
> What I don't know how to do is to compare the "classical" homotopy theory (built up from sets by topological spaces or simplicial sets or whatever) with the "internal" one which is somehow directly defined using types to represent homotopy types. I'm not even talking about how to prove a theorem that the homotopy theories are equivalent in some sense. I don't know how to define any map in either direction between classical spaces and types-as-homotopy-types.

It is questions like this that have prompted the development of "cohesive type theory", which adds a modality called "shape" that converts between a homotopy type and the set that encodes it
```
Thanks. I found https://arxiv.org/pdf/1509.07584.pdf which is indeed relevant.

#### [Reid Barton (Sep 13 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Deligne%20on%20univalence/near/133896509):
This talk of topological $$\mathbb{S}^1$$ and homotopy $$S^1$$ reminds me of motivic homotopy theory $$\mathbb{G}_m$$ and $$S^1$$

