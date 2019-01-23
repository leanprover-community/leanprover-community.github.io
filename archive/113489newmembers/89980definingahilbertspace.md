---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/89980definingahilbertspace.html
---

## Stream: [new members](index.html)
### Topic: [defining a hilbert space](89980definingahilbertspace.html)

---


{% raw %}
#### [ Joseph Corneli (Jul 31 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130645249):
Hi, this looks like something that might be near the edge of what's possible to define right now; would a more experienced person be able to give me some guidance?

> "A Hilbert space H is a real or complex inner product space that is also a complete metric space with respect to the distance function induced by the inner product."

If this is within the range of what's possible to define maybe it's a good exercise -- but as a newbie I'd still appreciate some help!

To begin with, can we define an "[inner product space](https://en.wikipedia.org/wiki/Inner_product_space)" using `prod_module.lean`?  That file talks about "Left injection function for the inner product" (resp., right injection).  But the code doesn't seem to have much in common with my idea of an "inner product," however.

On to the next step, `metric_space.lean` mentions "completeness" but the class `complete_space` is defined in `uniform_space.lean`; I guess we can get completeness from the generalisation; how would we insist upon completeness "with respect to the distance function"?

My guess is that the components are not ready "off the shelf" but still are within reach.  Would this be a worthwhile project to tackle?   If not, is there another topic that is more easily within reach?

#### [ Johan Commelin (Jul 31 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130645351):
Hmmm, I fear it is quite hard. @**Patrick Massot** has been struggling with normed spaces for a long time.

#### [ Kenny Lau (Jul 31 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130645376):
the definition is just a bunch of axioms

#### [ Johan Commelin (Jul 31 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130645392):
Right.

#### [ Patrick Massot (Jul 31 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646185):
metric spaces have a canonical uniform space structure, so completeness is defined for them as well

#### [ Patrick Massot (Jul 31 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646189):
I think you can easily define Hilbert spaces

#### [ Kevin Buzzard (Jul 31 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646196):
Yes, the definition is not hard at all. It's proving the basic properties where you'll start to learn what Lean can and cannot do easily. @**Andreas Swerdlow** , a first year undergraduate at Imperial College, already formalised Hilbert spaces here: https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/inner_product_spaces/basic.lean

#### [ Patrick Massot (Jul 31 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646206):
Note that I struggle to get a norm on R^n, not to define normed spaces (at least not anymore)

#### [ Kenny Lau (Jul 31 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646208):
but maybe you're Kevin Buzzard and only care about the definition :P

#### [ Kevin Buzzard (Jul 31 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646233):
If you have any lemmas which you'd like proved, let Andreas know Kenny!

#### [ Patrick Massot (Jul 31 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646255):
https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/inner_product_spaces/basic.lean#L655 is not correct

#### [ Patrick Massot (Jul 31 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646332):
it does not impose any relation between the uniform structure and the inner product

#### [ Kevin Buzzard (Jul 31 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646335):
Maybe he's not finished yet :-)

#### [ Joseph Corneli (Jul 31 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130648269):
Thanks for the answers and discussion.

#### [ Andreas Swerdlow (Aug 01 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130708575):
```quote
it does not impose any relation between the uniform structure and the inner product
```
Hi Patrick,

I see the problem with my definition, but after looking through the definition of a complete space in lean, I realised I don't know enough to fix it.  Do you have any suggestions?

#### [ Johan Commelin (Aug 01 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130709091):
After `class hilbert_space (V : Type u) extends herm_inner_product_space V, complete_space V` you should have one or more fields that demand compatibility between the inner product space and the complete space.

#### [ Kevin Buzzard (Aug 01 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130713865):
I'm in the same room as Andreas but haven't thought about how Lean does these things. I guess he's defined an inner product so I know about that. But the definition of `complete_space` involves Cauchy filters. I would imagine that there are right and wrong ways to do this. Oh -- do we just demand that the topology induced by the metric on `V` ($$d(x,y)=||y-x||$$) equals the topology which `complete_space` is using? Andreas -- can you make any sense of what I'm saying?

#### [ Johan Commelin (Aug 01 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130713913):
Hmm, but I guess they have to be def.eq. Because of :diamonds:

#### [ Kevin Buzzard (Aug 01 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130714094):
Only if there's some sort of inbuilt instance going from `herm_inner_product_space` to `topological_space` right?

#### [ Johan Commelin (Aug 01 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130714208):
Right, but I suppose that we do want instances for that.

#### [ Andreas Swerdlow (Aug 01 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130714256):
I've proved that the inner product induces the natural metric

#### [ Johan Commelin (Aug 01 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130714269):
Yes, but proofs are not enough.

#### [ Johan Commelin (Aug 01 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130714280):
Alas..., this is not mathematics. And beyond my pay-grade.

#### [ Kevin Buzzard (Aug 01 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130715205):
The issue I think is that there is no "natural metric", if I've understood things correctly. You wrote `class hilbert_space (V : Type u) extends herm_inner_product_space V, complete_space V` -- so this says "there's some inner product on V -- this is an assumption -- we don't know any more about it" and "there's some topology on V that makes V complete -- this is an assumption -- we don't know any more about it", so there are now perhaps two topologies on V if I've understood correctly what these typeclasses are.

#### [ Joseph Corneli (Aug 01 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130715968):
According to a comment in `uniform_space.lean`, "A uniform space is complete if every Cauchy filter converges." Would it not be necessary to show the latter fact?  I see three equivalent Bourbakian conditions (in the case of metric spaces) mentioned on page 8 of https://arxiv.org/pdf/1802.08521.pdf, referring to Bourbaki, General Topology, II3.3, Def. 3.  Looks like heavy going.

#### [ Johannes Hölzl (Aug 01 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130716250):
this is the definition of completeness
```lean
class complete_space (α : Type u) [uniform_space α] : Prop :=
(complete : ∀{f:filter α}, cauchy f → ∃x, f ≤ nhds x)
```
Which says that `[complete_space A]` is defined to be that each Cauchy filter converges.

#### [ Joseph Corneli (Aug 01 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130716885):
Yep, I'm of the view that this must be derived from Andreas's  assertions about Hermitian inner product space.  Without that condition it sounds like he has what's called a "pre-Hilbert space" *"An (incomplete) space with an inner product is called a pre-Hilbert space, since its completion with respect to the norm induced by the inner product is a Hilbert space."*

#### [ Joseph Corneli (Aug 01 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130717776):
Though I guess the point is that the condition of completeness is precisely what cannot be shown in general, otherwise there would not be such a thing as pre-Hilbert spaces.  So, to round out `inner_product_space/basic.lean` it would be good to have an *example* of a Hilbert space.

#### [ Kevin Buzzard (Aug 01 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130718011):
So I don't quite know the best way of doing this. Andreas has defined an instance from his `herm_inner_product_space` to metric spaces, and hence to topological space. So now how to define a class Hilbert space? Should he extend `hern_inner_product_space` and then add precisely the axioms needed to prove `complete_space` -- I mean -- rewrite them all again in full? Just cutting and pasting from `#print complete_space`? And then he can make an instance from `Hilbert_space` to `complete_space`? I guess there's also the other approach -- he could have it extend `complete_space` and then write down precisely the axioms of an inner product space that aren't there already -- eew --- and then he'd have to supply a proof that the topology defined by the norm equals the original topology. Is this how to think about things? The first approach is the correct one, right?

#### [ Gabriel Ebner (Aug 01 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130718081):
> add precisely the axioms needed to prove complete_space

That's just the one line Johannes posted.

#### [ Kevin Buzzard (Aug 01 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130719157):
Got it :-) I didn't see Johannes' post -- too much going on! Thanks all!

#### [ Kevin Buzzard (Aug 01 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130719242):
https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/92b9d48860f0f68de78ccdd3c103335d9b55d5c8/src/inner_product_spaces/basic.lean#L669

#### [ Kevin Buzzard (Aug 01 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130719243):
Think we got it

#### [ Joseph Corneli (Aug 01 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130721333):
To test it out can we now prove, e.g., that "The real numbers R^n with <v,u> the vector dot product of v and u" forms a Hilbert space?

#### [ Kevin Buzzard (Aug 01 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130721998):
That's going to need a whole lot of lemmas

#### [ Kevin Buzzard (Aug 01 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130722018):
...which are probably there already.

#### [ Kevin Buzzard (Aug 01 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130722123):
...actually maybe they're not all in mathlib. You'll need things like if n sequences all tend to zero then their sum tends to zero, you'll need that if a_n tends to zero and 0 <= b_n <= a_n then b_n tends to zero etc. This sort of stuff is not really mathlib's strong point at this stage.

#### [ Reid Barton (Aug 01 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130722355):
Maybe try n = 1 first...

#### [ Kevin Buzzard (Aug 01 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130722518):
...and then prove that a direct sum of two Hilbert spaces is a Hilbert space...

#### [ Andreas Swerdlow (Aug 01 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130722847):
I need to rewrite the definition of ```herm_inner_product_space``` so that it works over any subfield of the complex numbers. At the moment you can only prove that C^n is a Hilbert space

#### [ Joseph Corneli (Aug 01 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130723051):
No L^2 functions as yet?

#### [ Joseph Corneli (Aug 01 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130723247):
Anyway I do think an example, say C, would be great to include in the file.  Some test-driven development would be useful  if you're going to generalise!  If it works for C but fails for R, that would be interesting.

#### [ Patrick Massot (Aug 01 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130735854):
I'm sorry I didn't help earlier, I was on the road all afternoon. Your definition is still not correct. You still have an inner product and a uniform space with no relation whatsoever.

#### [ Patrick Massot (Aug 01 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130735888):
Did you look at https://github.com/leanprover/mathlib/pull/208?

#### [ Patrick Massot (Aug 01 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130736158):
The way this problem is handled is really weird for mathematicians. In https://github.com/leanprover/mathlib/pull/208/files#diff-81ed9f450352da041af7e0c731a22cdbR10 a normed group gather the attributes of a commutative additive group and a metric space, together with a function `norm` and an axiom saying that the distance of the metric space comes from the norm. Note that the `extends` keyword automatically creates an instance deriving a metric space from a normed group.

#### [ Patrick Massot (Aug 01 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130736345):
The weirdest comes next. A metric space is also defined in the kind of way, it bundles what you think should be there together with a uniform space structure and an axiom saying the uniform space structure equals what you would define from a structure. And a uniform space structure is defined in turn as extending both a topological structure and what you would call a uniform structure, together with an axiom relating both worlds.

#### [ Patrick Massot (Aug 01 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130736482):
The reason for this contrived setup is kind of subtle, it's meant to ensure that some stuff are definitionally equal, not only provably equal. It doesn't prevent us from using these structures, because there are various tricks (custom constructors or mechanisms to give default values to some fields) which hide them from us when building instances.

#### [ Patrick Massot (Aug 01 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130736544):
But really the problem with your current definition if much more basic: you don't enforce any relation between the norm and the topology

#### [ Patrick Massot (Aug 01 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130736627):
If you are serious about bringing Hilbert spaces to Lean, it would probably make more sense to pester @**Johannes Hölzl** until he either merges my norms PR or ditches it and rolls his own, and then you could try to build Hilbert spaces on top of it.

#### [ Simon Hudon (Aug 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130736917):
The other alternative is to work off of @**Patrick Massot** 's branch of mathlib

#### [ Kevin Buzzard (Aug 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130736929):
Patrick I think we're OK -- line 666 is the relation. It's my fault -- I linked to the wrong line. The definition is above where I linked -- sorry. Do you think we're OK?

#### [ Simon Hudon (Aug 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130736932):
... taking the risk that @**Johannes Hölzl** will request changes and that you'll have to adapt your definitions to reflect them

#### [ Patrick Massot (Aug 01 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130737271):
Line 666 is a relation between the uniform structure and the topology it generates, it has nothing to do with the norm

#### [ Kevin Buzzard (Aug 01 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130738460):
I am not so sure. `Hilbert_space V` extends `herm_inner_product_space V`. There's an instance sending `herm_inner_product_space V` to `topological_space V` [not that you can easily spot this -- it's somewhere else in this huge file]. I think that the `is_open` on line 666 refers to this topological space structure. I quite agree that if we had a topology generated by the uniform structure we'd be in trouble and this is exactly why we extend `uniform_space.core V` and not `uniform_space V`. Did I convince you yet?

#### [ Kevin Buzzard (Aug 01 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130738520):
The instance is in line 613 and it's noncomputable because Andreas had to take the square root of $$(v,v)$$ and square root is noncomputable!

#### [ Mario Carneiro (Aug 01 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130738615):
if there are two active topologies on the structure, it should be an axiom or theorem that they are equal

#### [ Mario Carneiro (Aug 01 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130738688):
although in this case I think you can actually get a uniform space from the inner product

#### [ Mario Carneiro (Aug 01 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130738699):
noncomputability of a uniform space structure means nothing since it is not data

#### [ Patrick Massot (Aug 01 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130738818):
I just realized that we don't talk about the same version

#### [ Patrick Massot (Aug 01 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130738827):
I cloned your repo, and there were several commits on those files in the mean time

#### [ Patrick Massot (Aug 01 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130738857):
In particular I didn't look at that instance on line 613 which is currently commented out

#### [ Kevin Buzzard (Aug 01 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130739715):
Oh! :-)

#### [ Kevin Buzzard (Aug 01 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130739904):
We specifically avoided two topologies on the structure, I believe. This was exactly the problem which Patrick pointed out the first time around. Yes, we get a uniform space structure from the inner product -- that's exactly what we do now. Andreas extends uniform_space.core and then we make an instance of the uniform space using the topology coming from the norm plus an axiom that it agrees with the topology which comes from the uniform space. I am in the middle of doing something else right now but I assume there is no instance which gives a topology from a uniform_space.core -- I'm assuming that that's precisely the point of the structure, it's like a distrib.

#### [ Mario Carneiro (Aug 01 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130739993):
You probably shouldn't use `uniform_space.core` in this case

#### [ Mario Carneiro (Aug 01 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130740044):
you already have a topology coming from somewhere else, so use that in `uniform_space` and prove the equality axiom rather than letting `uniform_space.core` fill it in for you

#### [ Kevin Buzzard (Aug 01 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130740761):
V is just a vector space -- the only metric/topology we have on it is coming from the norm. All we want to do is to say that the metric is complete. We have no uniform structure or anything. I don't want to do uniform anything -- I just want to say that the metric space is complete. The only reason we're extending uniform_space.core is that this is the only way I know how to say this in Lean! What am I missing?

#### [ Mario Carneiro (Aug 01 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130741388):
if it has a norm then it extends `normed_vector_space`, with the attendant norm, metric, uniform space and topology

#### [ Mario Carneiro (Aug 01 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130741406):
the "agreement" here with the inner product says $$(v, v) = \|v\|^2$$

#### [ Patrick Massot (Aug 01 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130741409):
Sorry, I was interrupted by a phone call

#### [ Patrick Massot (Aug 01 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130741454):
What Mario says is why I suggested you build upon my normed space stuff

#### [ Mario Carneiro (Aug 01 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130741461):
(or something like it - is this a real inner product space or a more general kind?)

#### [ Patrick Massot (Aug 01 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130741709):
Also, try at the end of your file: 
```lean
variables (V : Type) (H : Hilbert_space V)
example : H.to_core.to_topological_space = uniform_space.to_topological_space V := rfl
```
seeing this fail is a bad omen

#### [ Simon Hudon (Aug 01 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130741898):
You're so superstitious!

#### [ Kevin Buzzard (Aug 01 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130741905):
This file has changed since I understood it ;-)

#### [ Patrick Massot (Aug 01 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130742139):
```quote
 you'll need that if a_n tends to zero and 0 <= b_n <= a_n then b_n tends to zero etc. This sort of stuff is not really mathlib's strong point at this stage.
```
That one is in mathlib

#### [ Patrick Massot (Aug 01 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130742165):
https://github.com/leanprover/mathlib/blob/29639b31a9808f601fa434aeed0f5756f040f0e8/analysis/topology/topological_structures.lean#L434

#### [ Mario Carneiro (Aug 01 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130742168):
also completeness is defined in terms of filters not sequences

#### [ Andreas Swerdlow (Aug 02 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130768355):
```quote
Also, try at the end of your file: 
```lean
variables (V : Type) (H : Hilbert_space V)
example : H.to_core.to_topological_space = uniform_space.to_topological_space V := rfl
```
seeing this fail is a bad omen
```
Just tried this and it fails

#### [ Kevin Buzzard (Aug 02 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130768700):
This sounds related to Mario's comment. We do not care one bit about the uniform space structure. Here is the actual question. Let M be a metric space. How do I make the assertion in Lean that M is complete? And the meta-question is why this isn't a darn sight easier than it is (the answer to this possibly being "it's because of diamonds and the type class inference system not really being designed for this sort of thing"). At the minute we make M an instance a class of uniform_space.core and then add an axiom that the open sets of M are equal to the open sets of the uniformity. What's the correct way to do it? Note that Andreas is a 1st year undergrad and is just doing this to learn the theory and to learn Lean, this just an educational experiment at this point rather than a project to get Hilbert spaces into mathlib.

#### [ Johan Commelin (Aug 02 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130768984):
```quote
Note that Andreas is a 1st year undergrad and is just doing this to learn the theory and to learn Lean, this just an educational experiment at this point rather than a project to get Hilbert spaces into mathlib.
```
Kudos! :octopus: Your UG's are amazing Kevin!

#### [ Kevin Buzzard (Aug 02 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130769069):
They're producing so much stuff that I find it difficult to keep track of it all. Every few hours I pull https://github.com/ImperialCollegeLondon/xena-UROP-2018/ and there's more stuff; it's got to the stage where there aren't enough hours in the day to look at it all. If anyone wants to review any of the code there then feel free :-)

#### [ Johan Commelin (Aug 02 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130769206):
```quote
Excluding merges, 16 authors have pushed 84 commits to master and 83 commits to all branches. On master, 37 files have changed and there have been 5,920 additions and 1,071 deletions.  -- quote from github, insights
```
That's over the last week!

#### [ Joseph Corneli (Aug 02 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130771212):
With latest version of the file I get an error: `invalid import: norm_space`.  Am I missing a dependency?  There's a file `src/inner_product_spaces/norm_spaces` (no `.lean`).  Renaming the file and adjusting the import line as follows, the error goes away:

```lean
import linear_algebra.basic algebra.field inner_product_spaces.norm_space data.complex.basic data.real.basic analysis.metric_space analysis.topology.uniform_space
```

 @**Andreas Swerdlow**  is this roughly what's intended?

#### [ Kevin Buzzard (Aug 02 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130771225):
Apologies for this. When I was involved yesterday afternoon it was all working fine but there have been some commits since then and I've not had the time to look at it all.

#### [ Patrick Massot (Aug 02 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130771650):
I also needed to modify this yesterday to get it to compile. I know this UROP thing is very free form, but maybe you could encourage commits which compile (I'm not talking about sorry, this is a different question)

#### [ Andreas Swerdlow (Aug 02 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130771710):
@**Joseph Corneli**  Yes sorry, am currently working on a version of the file that is saved on my hard drive and just copied over without thinking. That is the correct import.

#### [ Joseph Corneli (Aug 02 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130772322):
Another small suggestion would be a doc string for the main `class` in `basic.lean`:
```lean
/--
`herm_inner_product_space` defined such the inner product of two vectors is a value in ℂ.
This definition would have to be modified to work for any field of scalars.
-/
```

#### [ Kevin Buzzard (Aug 02 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130772943):
@**Andreas Swerdlow** I have located @**Minh Hieu Le (Kai)**  -- he's sitting opposite me right now :-)


{% endraw %}
