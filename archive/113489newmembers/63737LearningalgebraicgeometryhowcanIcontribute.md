---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/63737LearningalgebraicgeometryhowcanIcontribute.html
---

## Stream: [new members](index.html)
### Topic: [Learning algebraic geometry; how can I contribute?](63737LearningalgebraicgeometryhowcanIcontribute.html)

---


{% raw %}
#### [ Soham Chowdhury (Sep 02 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214542):
Hi everyone! A friend sent me a link to @**Kevin Buzzard**'s answer on the "What are perfectoid spaces?" MO question, which is how I got here. I'm learning algebraic geometry right now. More to the point, I have some experience using Agda and Idris (but not Lean).

I would enjoy helping to formalise material related to what I'm learning; how can I help?

#### [ Kevin Buzzard (Sep 02 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214551):
Well, someone needs to prove that the integral closure of a subring is a subring :-)

#### [ Kenny Lau (Sep 02 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214554):
what the hell, @**Soham Chowdhury**

#### [ Kevin Buzzard (Sep 02 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214594):
Here are some projects which the community thinks are accessible:  https://github.com/leanprover-community/mathlib/wiki/Potential-projects

#### [ Soham Chowdhury (Sep 02 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214597):
@**Kenny Lau** is it ... possible I know you?

#### [ Kenny Lau (Sep 02 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214604):
guess who sent you that link

#### [ Soham Chowdhury (Sep 02 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214651):
Oh haha

```quote
Well, someone needs to prove that the integral closure of a subring is a subring :-)
```
That sounds like something I can do!

#### [ Kevin Buzzard (Sep 02 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214652):
Here is a challenging project which would teach you a bunch about Lean: prove that Hom(X,Spec(R)) = Hom(R,O_X(X)).

#### [ Kenny Lau (Sep 02 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214656):
```quote
Here is a challenging project which would teach you a bunch about Lean: prove that Hom(X,Spec(R)) = Hom(R,O_X(X)).
```
yeah, that...

#### [ Kevin Buzzard (Sep 02 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214665):
Anthony Bordg also sent me an email saying he might be interested in doing this. As I'm sure you'll know from Idris, there's a big difference between learning alg geom from a book and actually telling Lean about it.

#### [ Kevin Buzzard (Sep 02 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214666):
What exactly are you learning?

#### [ Soham Chowdhury (Sep 02 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214761):
Chapter 5 of Vakil's FOAG right now, so I don't know all that much :)

#### [ Soham Chowdhury (Sep 02 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214762):
But basic commutative algebra sounds like something I could get started on.

#### [ Kevin Buzzard (Sep 02 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214812):
Several people have been asking what they could work on. Of course embarking on a project like proving a standard algebra theorem with a new theorem prover (and then asking a gazillion questions here) is a really good way to learn how to use the theorem prover, but I am currently slightly worried that whenever someone who knows any algebra asks what they could do, I reply with basically the same reply.

#### [ Kevin Buzzard (Sep 02 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214820):
As far as comm alg goes, we have localisation of rings, a PR for tensor products, a definition of Noetherian rings and modules but 0 theorems (other than the fact that the two usual definitions are equivalent), and enough group theory to make doing basic commutative algebra feasible.

#### [ Soham Chowdhury (Sep 02 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214872):
I guess even if someone "beats me to" one of these problems, I'm sure the payoff from becoming comfortable with Lean will make it that much easier to work on harder things like, e.g. the Hom(X, Spec R) theorem you mentioned.

#### [ Kevin Buzzard (Sep 02 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214874):
Lean has affine schemes but not projective schemes, so you're a little ahead ;-)

#### [ Kevin Buzzard (Sep 02 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214921):
However they're not in mathlib, they're in a stacks project repo on my github https://github.com/kbuzzard/lean-stacks-project which I wrote to learn Lean, so this code sometimes leaves some things to be desired...

#### [ Soham Chowdhury (Sep 02 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214971):
Is the definition of Noetherian modules in mathlib `master`? I can't seem to find it there.

#### [ Kevin Buzzard (Sep 02 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214978):
I watched it be born but I don't know where it is. It was only created on Wednesday.

#### [ Mario Carneiro (Sep 02 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133215018):
it is in a branch on the community fork

#### [ Kevin Buzzard (Sep 02 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133215023):
https://github.com/leanprover-community/mathlib/search?q=noetherian&unscoped_q=noetherian doesn't find it

#### [ Kevin Buzzard (Sep 02 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133215031):
https://github.com/leanprover-community/mathlib/commit/ef5c110626b0197118299071a98ed98e1aead287

#### [ Soham Chowdhury (Sep 02 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133215039):
I believe GitHub search only looks in `master`.

#### [ Kevin Buzzard (Sep 02 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133215098):
I believe that too, now. We next need that submodules and quotient modules of Noetherian modules are Noetherian. This should be easy if we have some basic facts about there being a natural injection from the submodules of `M/N` to the submodules of `M` -- is this in mathlib? @**Kenny Lau** Is this something like Proposition 1.1 of A-M?

#### [ Kevin Buzzard (Sep 02 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133215139):
oh, that's only for rings. OK so here's a concrete thing we need: order-preserving bijection between submodules of M/N and submodules of M containing N.

#### [ Kevin Buzzard (Sep 02 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133215140):
Is that there already? Does anyone know? I don't remember seeing it.

#### [ Kenny Lau (Sep 02 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133215344):
looks like a Galois correspondence to me

#### [ Soham Chowdhury (Sep 02 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133218718):
I'm going to check back here if (rather, when) I have questions. Thanks for the pointers.

#### [ Patrick Massot (Sep 02 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133219598):
@**Soham Chowdhury** do you know where to start? (hint: the answer is https://leanprover.github.io/theorem_proving_in_lean/).

#### [ Johan Commelin (Sep 03 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133239139):
Also see this thread in Zulip: https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/noetherian.20modules (You might need to enable the "maths" stream somewhere in your settings; but I thought this was done by default nowadays.)


{% endraw %}
