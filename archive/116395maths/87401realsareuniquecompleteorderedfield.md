---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/87401realsareuniquecompleteorderedfield.html
---

## Stream: [maths](index.html)
### Topic: [reals are unique complete ordered field](87401realsareuniquecompleteorderedfield.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 09 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131159069):
The reals are the unique complete ordered field up to unique isomorphism. Is this in Lean already? I thought it might be a good exercise for a student.  @**Patrick Massot** does "complete" here mean "an ordered field inherits a topology from the order, and the associated uniform space is complete"? Last week I didn't know what that even meant. Is that the same as asking that any non-empty bounded set has a least upper bound? 

I think Reid Barton once commented that because of this theorem, one should not prove theorems about the reals, one should instead prove theorems about complete ordered fields :-)

#### [ Mario Carneiro (Aug 09 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131159304):
I think there is a more useful way to characterize this property: `real.cast`

#### [ Mario Carneiro (Aug 09 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131159322):
Any complete field has a unique continuous field hom from the reals

#### [ Mario Carneiro (Aug 09 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131159398):
Also, I think we have a good bit of the infrastructure already, since it was originally used to define functions like addition on the reals by continuous extension from rat.add

#### [ Andrew Ashworth (Aug 09 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131159443):
iirc Reid mentioned that because a synthetic, axiom based real number allowed his code to run much faster

#### [ Mario Carneiro (Aug 09 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131159448):
That's often true

#### [ Mario Carneiro (Aug 09 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131159459):
concrete constructions have the drawback that lean can start unfolding them

#### [ Mario Carneiro (Aug 09 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131159852):
Here, I'll get you started:
```
def real.cast {α} [topological_space α] [division_ring α] : ℝ → α :=
dense_embedding_of_rat.extend coe
```
Can you prove that this has all the same properties as `rat.cast`? What is the analogue of `rat.eq_cast`?

#### [ Johan Commelin (Aug 09 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160061):
Mario, did you just write down a map from `real` to `rat`?

#### [ Mario Carneiro (Aug 09 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160072):
heh, I guess I did

#### [ Johan Commelin (Aug 09 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160080):
Ughh. The mathematician in me is worried, and crying, and has a huge headache. This is not a nice map, is it?

#### [ Mario Carneiro (Aug 09 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160128):
It is under more assumptions

#### [ Mario Carneiro (Aug 09 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160131):
`extend_eq` requires that the space be t2

#### [ Mario Carneiro (Aug 09 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160137):
and `tendsto_extend` needs that it is regular

#### [ Mario Carneiro (Aug 09 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160145):
I guess Q is not a regular space?

#### [ Johan Commelin (Aug 09 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160151):
But, to which `rat` does that map send `pi` or `e`?

#### [ Johan Commelin (Aug 09 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160163):
I guess we'll never know... because of computability

#### [ Mario Carneiro (Aug 09 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160171):
If the limit is not defined, it maps to an arbitrary constant in Q

#### [ Johan Commelin (Aug 09 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160229):
Right, so it is the identity on rationals and maps the rest to 57 (or 37, if you ask Kevin).

#### [ Mario Carneiro (Aug 09 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160252):
Actually it is `classical.choice (_ : nonempty Q)`

#### [ Patrick Massot (Aug 09 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160300):
Kevin: https://en.wikipedia.org/wiki/Real_number#%22The_complete_ordered_field%22

#### [ Mario Carneiro (Aug 09 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160330):
Oh, I was wrong, you need more than just regular space for it to be defined, you need this condition
```
(hf : ∀b, ∃c, tendsto f (vmap e (nhds b)) (nhds c))
```

#### [ Mario Carneiro (Aug 09 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160388):
There should be a simple assumption giving this property, but I guess you need a uniform structure

#### [ Mario Carneiro (Aug 09 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160647):
if you assume `archimedean A` and `discrete_linear_ordered_field A`, then you can prove that `rat.cast` is a dense embedding by just generalizing the existing proof `dense_embedding_of_rat`, and hence define a function like `real.cast` out of `A`

#### [ Mario Carneiro (Aug 09 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160661):
and then you have your isomorphism

#### [ Kevin Buzzard (Aug 09 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131161921):
```quote
Kevin: https://en.wikipedia.org/wiki/Real_number#%22The_complete_ordered_field%22
```
Oh thanks for this Patrick! That clears this mess up!

#### [ Patrick Massot (Aug 09 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131161973):
Remember: if it's not formalized, you don't even know what you are talking about.

#### [ Kevin Buzzard (Aug 09 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131163511):
this is a fabulous example of this! I was talking to Chris about this last week and just ended up confused. I said "did you know that the reals are the unique complete ordered field?" and he replied "don't you need some archimedean property" and I said "oh yeah, what happens if you adjoin an infinitesimal?" and it was at this point that I realised I was no longer quite sure what I was talking about.

#### [ Mario Carneiro (Aug 09 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131163998):
what is an example of a complete nonarchimedean field?

#### [ Johan Commelin (Aug 09 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164008):
Q_p

#### [ Mario Carneiro (Aug 09 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164014):
ordered field?

#### [ Johan Commelin (Aug 09 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164020):
Hmmm. Don't know about those.

#### [ Mario Carneiro (Aug 09 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164102):
In my proof sketch, you definitely need archimedean to prove dense embedding, but I think you can use completeness to prove archimedean

#### [ Johan Commelin (Aug 09 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164111):
Seems reasonable

#### [ Mario Carneiro (Aug 09 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164141):
If completeness means dedekind-complete, then the sup of N is contradictory so you get archimedean that way

#### [ Mario Carneiro (Aug 09 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164218):
but if it is only complete relative to the uniformity it's not obvious to me

#### [ Kevin Buzzard (Aug 09 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164262):
I am in the middle of something else at the minute but I convinced myself last week that you could put an order on $$\mathbb{R}(\epsilon)$$ with $$\epsilon$$ smaller than any positive real but greater than zero. Can one complete this, for some notion of completion?

#### [ Mario Carneiro (Aug 09 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164335):
wait, Q_p isn't nonarchimedean

#### [ Mario Carneiro (Aug 09 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164339):
it isn't ordered so the term doesn't apply

#### [ Kevin Buzzard (Aug 09 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164340):
It is for some definition

#### [ Rob Lewis (Aug 09 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164349):
It has a nonarchimedean norm.

#### [ Johan Commelin (Aug 09 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164361):
What the hack does "nonarchimedean" mean if even Q_p is no longer an example.... (shakes head...)

#### [ Kevin Buzzard (Aug 09 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164364):
I have a book called "nonarchimedean analysis" which defines a nonarchimedean field to be a field complete with respect to a non-trivial nonarchimedean norm.

#### [ Kevin Buzzard (Aug 09 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164399):
and a nonarchimedean norm is a function from the field to the non-negative reals satisfying F(x)=0 iff x=0, F(xy)=F(x)F(y) and F(x+y)<=max(F(x),F(y))

#### [ Kevin Buzzard (Aug 09 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164418):
and non-trivial means "not the one with F(x)=1 for x non-zero and F(0)=0"

#### [ Kevin Buzzard (Aug 09 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164493):
and complete in this context means the underlying metric space is complete with d(x,y)=F(x-y)

#### [ Mario Carneiro (Aug 09 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164500):
what does an archimedean norm have to do with the archimedean property? the definitions look completely different

#### [ Kevin Buzzard (Aug 09 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164538):
Oh sorry, I defined a nonarchimedean norm above, I'll edit

#### [ Mario Carneiro (Aug 09 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164570):
wiki says a nonarchimedean norm is one that defines an ultrametric, but I don't see what that has to do with 1+1+1+...

#### [ Kevin Buzzard (Aug 09 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164613):
A norm is F as above but with F(x+y)<=max(F(x),F(y)) weakened to F(x+y)<=F(x)+F(y)

#### [ Kevin Buzzard (Aug 09 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164623):
and a norm is defined to be archimedean if it is not nonarchimedean (seriously)

#### [ Kevin Buzzard (Aug 09 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164666):
I think the two uses of archimedean are unfortunate, and are probably just related to the fact that the reals satisfies both properties

#### [ Kevin Buzzard (Aug 09 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164681):
As Patrick says, if you haven't formalised it, you don't know what you're talking about

#### [ Mario Carneiro (Aug 09 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164726):
I want to call that an ultranorm, it makes more sense

#### [ Kevin Buzzard (Aug 09 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164750):
What would you like my book to be called?

#### [ Mario Carneiro (Aug 09 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164768):
ultra analysis?

#### [ Kevin Buzzard (Aug 09 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164786):
I think it would have sold more copies with that title

#### [ Kevin Buzzard (Aug 09 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164797):
Bosch--Guentzer--Remmert

#### [ Kevin Buzzard (Aug 09 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164810):
It's a classic. I read it from cover to cover.

#### [ Mario Carneiro (Aug 09 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164887):
anyway, which of these archimedeans is the one we care about?

#### [ Johan Commelin (Aug 09 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164899):
Number theorists care about the normy version.

#### [ Mario Carneiro (Aug 09 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164905):
I mean for uniqueness of R

#### [ Kevin Buzzard (Aug 09 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164993):
Did you see Patrick's Wikipedia link? That says something about the confusion. But the definition of an archimedean norm is, I believe, nothing to do with the uniqueness statement about the reals.

#### [ Kevin Buzzard (Aug 09 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165049):
The only role I've ever seen that "archimedean = not non-archimedean" definition play is when classifying all norms on number fields. I am honestly not sure it's used anywhere else.

#### [ Kevin Buzzard (Aug 09 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165097):
Maybe in Cassels' "Local Fields" there'a a section on archimedean norms, and it might even say that every field with an archimedean norm is a subfield of the complexes or something.

#### [ Kevin Buzzard (Aug 09 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165135):
I forget the lemma. Certainly the theorem is that the archimedean norms on a number field are all induced from embeddings into the complexes (modulo some equivalence relation on norms which is "induced metrics define the same topology")

#### [ Mario Carneiro (Aug 09 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165193):
wait, so does R have any uniqueness property that does not reference the order?

#### [ Kevin Buzzard (Aug 09 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165327):
The complexes are the unique algebraically closed field of characteristic zero and cardinality 2^aleph_0 (proof: transcendence basic; probably I'm assuming AC here). If you take an element of order 2 in Aut(complexes) then its fixed points are a field which I think is not in general isomorphic to the reals but which is quite difficult to tell apart from the reals if you don't think about the ordering.

#### [ Kevin Buzzard (Aug 09 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165373):
Hmm, maybe the fixed points do even have an ordering, perhaps it's this unboundedness of 1+1+1+... which fails in these general fields (are they called "real closed fields"?)

#### [ Mario Carneiro (Aug 09 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165374):
If you allow the topology, you should be able to get R exactly, right?

#### [ Mario Carneiro (Aug 09 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165377):
there is only one nontrivial continuous automorphism of C

#### [ Kevin Buzzard (Aug 09 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165378):
right

#### [ Kevin Buzzard (Aug 09 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165386):
but I defined it as an abstract field

#### [ Kevin Buzzard (Aug 09 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165389):
Take Q, adjoin 2^aleph_0 independent transcendental elements, and then take the alg closure

#### [ Kevin Buzzard (Aug 09 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165390):
This proves that C is isomorphic to an algebraic closure of Q_p

#### [ Kevin Buzzard (Aug 09 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165440):
and an algebraic closure of Q_p has a non-archimedean norm on it, which makes it a metric space, and this metric space is not complete, and if you complete it then you get something called C_p, which by the same argument is also isomorphic to C

#### [ Mario Carneiro (Aug 09 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165448):
isomorphic as fields?

#### [ Kevin Buzzard (Aug 09 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165450):
So there's lots of different topologies on C

#### [ Johan Commelin (Aug 09 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165456):
```quote
isomorphic as fields?
```
yes

#### [ Kevin Buzzard (Aug 09 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165457):
Yes, any two alg closed fields of char 0 and cardinality 2^aleph_0 are isomorphic

#### [ Mario Carneiro (Aug 09 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165463):
but if you want to capture "complete" from the original statement, you want a topological field structure

#### [ Kevin Buzzard (Aug 09 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165465):
Proof is "take a transcendence basis over Q, check it has size 2^aleph_0, hence your field must be iso to an alg closure of Q(X_i:i in reals)

#### [ Kevin Buzzard (Aug 09 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165522):
So if c is a random automorphism of order 2 of (alg closure of Q(X_i : i in reals)) then I think you can define an order on the fixed subfield, by x > 0 iff x is a non-zero square

#### [ Kevin Buzzard (Aug 09 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165562):
but before I say too much more I should look at the Wikipedia article on real closed fields and I'm trying to read a student's work on homotopy theory :-/

#### [ Johan Commelin (Aug 09 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165970):
I think *real closed fields* would be a really cool topic to formalise as well.

#### [ Johan Commelin (Aug 09 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165972):
There is lots of interesting logic there.

#### [ Johan Commelin (Aug 09 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131166026):
Quantifier elimination. Semialgebraic sets. https://en.wikipedia.org/wiki/Cylindrical_algebraic_decomposition

#### [ Johan Commelin (Aug 09 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131166039):
Anyway, I'm derailing this topic.

#### [ Kenny Lau (Aug 09 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131171804):
there is an order on Q_p

#### [ Kenny Lau (Aug 09 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131171889):
wait the order isn't compatible with the ring structure


{% endraw %}
