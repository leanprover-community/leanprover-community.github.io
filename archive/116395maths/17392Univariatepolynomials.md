---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/17392Univariatepolynomials.html
---

## Stream: [maths](index.html)
### Topic: [Univariate polynomials](17392Univariatepolynomials.html)

---


{% raw %}
#### [ Kevin Buzzard (May 03 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058586):
Here's another "canonical isomorphism" question. Johannes has implemented multivariate polynomials with variables in some index type sigma.

#### [ Kevin Buzzard (May 03 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058599):
But the univariate theory (polynomials in one variable) is special

#### [ Kevin Buzzard (May 03 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058621):
there are more theorems, for example; over a field these things form a Euclidean domain and a principal ideal domain etc

#### [ Kevin Buzzard (May 03 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058631):
so there is probably an argument for developing the theory of polynomials in one variable further.

#### [ Kevin Buzzard (May 03 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058638):
But one doesn't want to reprove everything

#### [ Kevin Buzzard (May 03 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058689):
and for polynomials in one variable, Johannes' definition becomes `(unit -> nat) ->_0 alpha`

#### [ Kevin Buzzard (May 03 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058693):
and `unit -> nat` is just canonically isomorphic to nat

#### [ Kevin Buzzard (May 03 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058734):
so now we have a sort-of insane way of setting up univariate polys

#### [ Kevin Buzzard (May 03 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058744):
and a sensible way

#### [ Kevin Buzzard (May 03 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058793):
and one would imagine that the sensible way, nat ->_0 alpha, was the thing to use

#### [ Kevin Buzzard (May 03 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058799):
but one wants to import all Johannes' work for free, like definitions and the proof that polynomials form a ring etc

#### [ Kevin Buzzard (May 03 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058801):
so one first notes that there's an equiv between nat and (unit -> nat)

#### [ Kevin Buzzard (May 03 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058808):
and then one wants to pull all of Johannes' definitions and theorems through this equiv

#### [ Kevin Buzzard (May 03 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058877):
but currently in Lean this seems hard. Is that right?

#### [ Kevin Buzzard (May 03 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058980):
I see. And this takes us back to exactly what we were thinking about a few days ago

#### [ Kevin Buzzard (May 03 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058981):
whether ring is transportable

#### [ Kevin Buzzard (May 03 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058985):
(and it should be)

#### [ Mario Carneiro (May 03 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059273):
The short answer is yes, this is hard, but really it doesn't quite characterize the problem so well. We don't *want* to transfer the ring structure of `(unit -> nat) ->_0 alpha` to `nat ->_0 alpha` in the "naive way" because this would make all the operations filter through the equivalence which would make them hard to use

#### [ Mario Carneiro (May 03 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059350):
(not to mention inefficient, not sure if we are deciding to care about this here)

#### [ Kevin Buzzard (May 03 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059372):
So if we need univariate polys

#### [ Kevin Buzzard (May 03 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059391):
is the best idea currently just to re-implement them? :-/

#### [ Mario Carneiro (May 03 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059411):
we would want instead to define the operations specially for univariate polys, but prove that the canonical equiv is a ring homomorphism and use that to prove that the other structure is a ring

#### [ Mario Carneiro (May 03 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059474):
this is basically what `transfer` is intended to do

#### [ Mario Carneiro (May 03 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059492):
You should check out `num` a bit to see how the process can work

#### [ Mario Carneiro (May 03 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059536):
I define operations on `num` that act like corresponding operations on `nat`, prove that the map from `nat` to `num` preserves the operations, and use that to prove that `num` is a `decidable_linear_ordered_semiring` or whatever

#### [ Johan Commelin (May 03 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059543):
Can't we have some `meta` code that automatically generates all the theorems and proof, given the `equiv`, so that it does the reimplementation for us? Together with transport statements that link the new implementation to the old one...

#### [ Kevin Buzzard (May 03 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059579):
This approach is "better" than the one used to transfer proofs from multiplicative groups to additive groups, right?

#### [ Mario Carneiro (May 03 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059588):
That's `transfer`

#### [ Kevin Buzzard (May 03 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059591):
Because there the two types are themselves equivalent in a strong sense

#### [ Kevin Buzzard (May 03 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059616):
so you can literally translate a proof that a group with multiplication as group law has some property, to the same proof that a group with addition as group law has some analogous property

#### [ Kevin Buzzard (May 03 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059644):
but here unit -> nat is a different type to nat

#### [ Mario Carneiro (May 03 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059694):
In some sense the equiv from `add_group` to `group` is "cheap"

#### [ Mario Carneiro (May 03 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059719):
and the underlying carrier types are defeq, which helps a lot

#### [ Kevin Buzzard (May 03 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059726):
and so the argument somehow relies on the fact that Johannes didn't do anything funny with his unit -> nat type which we can't also do with the nat type

#### [ Mario Carneiro (May 03 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059793):
For more general equivalences, `equiv` does the job

#### [ Mario Carneiro (May 03 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059797):
the argument doesn't rely on anything more

#### [ Mario Carneiro (May 03 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059808):
(but you do have to prove that the equiv respects the operations)

#### [ Kevin Buzzard (May 03 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059835):
Stupid question

#### [ Kevin Buzzard (May 03 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059844):
what is an example of something you can do in type theory for unit -> nat which you can't do for nat

#### [ Kevin Buzzard (May 03 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059852):
I can't make that rigorous

#### [ Mario Carneiro (May 03 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059855):
they are equiv, so nothing?

#### [ Mario Carneiro (May 03 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059918):
In PL theory they are a bit different, since one is like a delayed computation and the other is a value, but I assume you are ignoring this distinction

#### [ Kevin Buzzard (May 03 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059927):
yes

#### [ Kevin Buzzard (May 03 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059948):
If equiv commutes with everything in dependent type theory

#### [ Kevin Buzzard (May 03 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059956):
why isn't this transportable stuff just standard and built in?

#### [ Kevin Buzzard (May 03 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059967):
Is it in Coq?

#### [ Mario Carneiro (May 03 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059977):
Of course it doesn't commute with everything, but you can always lift operations by pre/post composing with it

#### [ Kevin Buzzard (May 03 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059987):
right

#### [ Kevin Buzzard (May 03 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059996):
and if you go from X to Y and then back to X you will have the identity

#### [ Mario Carneiro (May 03 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060061):
you will have propositionally the identity, it's (probably) not defeq

#### [ Kevin Buzzard (May 03 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060069):
oh boy

#### [ Mario Carneiro (May 03 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060073):
that means that you may need to cast stuff across the equality

#### [ Kevin Buzzard (May 03 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060084):
but can a computer construct the proof if it's not defeq?

#### [ Mario Carneiro (May 03 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060087):
and those casts build up and get more complicated

#### [ Mario Carneiro (May 03 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060115):
the proof is given, it's an equiv so that's part of the structure

#### [ Johan Commelin (May 03 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060181):
Ouch, so this is going to break us up if we are somewhere deep down in the guts of formalising the proof of the Weil conjectures

#### [ Johan Commelin (May 03 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060195):
Because you exceed `max_transfers` which was set to `1000` or something...

#### [ Mario Carneiro (May 03 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060212):
just try to have a better way to say stuff than transferring some other statement when casts get involved

#### [ Johan Commelin (May 03 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060217):
(Maybe I am blatantly displaying my ignorance...)

#### [ Mario Carneiro (May 03 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060227):
mostly avoid too many dependent types

#### [ Kevin Buzzard (May 03 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060234):
we don't care that the proofs can get complicated because they are irrelevant

#### [ Mario Carneiro (May 03 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060237):
I'm talking about terms

#### [ Kevin Buzzard (May 03 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060241):
right

#### [ Kevin Buzzard (May 03 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060283):
if I want to define affine 1-space

#### [ Kevin Buzzard (May 03 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060288):
`Spec(R[x])`

#### [ Kevin Buzzard (May 03 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060295):
then in the definition of e.g. the local ring at some point

#### [ Kevin Buzzard (May 03 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060296):
there will be casts everywhere

#### [ Kevin Buzzard (May 03 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060299):
it will be unreadable

#### [ Johan Commelin (May 03 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060301):
Mario, I am a bit afraid that this is not so easy to avoid... or the formalisation might become way more difficult then they "maths" proof

#### [ Mario Carneiro (May 03 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060311):
It's all about modularity

#### [ Mario Carneiro (May 03 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060317):
just break stuff up into bite sized chunks and it's all doable

#### [ Kevin Buzzard (May 03 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060318):
Is this the reason that all the big type theory proofs of maths theorems are proofs about objects like finite groups rather than locally Noetherian schemes?

#### [ Kevin Buzzard (May 03 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060325):
problems pile up

#### [ Kevin Buzzard (May 03 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060364):
and it's difficult to make them go away

#### [ Johan Commelin (May 03 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060371):
Ok, then I misunderstood you. I thought that if you started combining these "modules" then some evil synergy would multiply their "badness of casts"

#### [ Mario Carneiro (May 03 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060386):
Just have solid abstraction layers, as long as the informal math doesn't get notationally horrible the formal horribleness is bounded

#### [ Johan Commelin (May 03 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060396):
Ok, I really hope so.

#### [ Mario Carneiro (May 03 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060405):
The multiplying badness of casts happens when you try to do it in general over the whole theory

#### [ Johan Commelin (May 03 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060451):
If Kevin is meeting all these problems in the definition of an affine scheme... then we want 1) all sorts of properties of morphisms of schemes, 2) topos theory, 3) derived categories, 4) etale cohomology, 5)... etc etc

#### [ Mario Carneiro (May 03 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060452):
i.e. you write some tactic that just plows through the whole system to transfer any term across some equiv

#### [ Johan Commelin (May 03 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060453):
before you can even sensibly formulate the Weil conjectures

#### [ Mario Carneiro (May 03 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060467):
these kinds of tactics care nothing for abstraction

#### [ Johan Commelin (May 03 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060472):
Hmmm, I'm still confused...

#### [ Johan Commelin (May 03 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060531):
Do you think that in the end we can have automation help us with these transfers, and still have the modularity? Or does the automation mean that it will "plow through the system"?

#### [ Kevin Buzzard (May 03 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060538):
When I started reading proofs in mathlib

#### [ Kevin Buzzard (May 03 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060552):
I was really confused why people would create a new structure and then instantly write functions giving access to the things used to construct the structure

#### [ Kevin Buzzard (May 03 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060554):
but

#### [ Kevin Buzzard (May 03 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060558):
it's all part

#### [ Kevin Buzzard (May 03 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060563):
of a solid abstraction layer

#### [ Johan Commelin (May 03 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060576):
Hmm, that's a good example. A "mathematician" wouldn't (want) to do that.

#### [ Johan Commelin (May 03 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060619):
Again, couldn't some automation do that for us?

#### [ Kevin Buzzard (May 03 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060623):
Getting the code to run fast is not our problem :-)

#### [ Mario Carneiro (May 03 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060635):
In theory, but it probably would need lots of tweaks

#### [ Kevin Buzzard (May 03 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060637):
You just wait for either the CS people to write better tactics or for the engineers to write faster chips

#### [ Johan Commelin (May 03 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060639):
If I write `structure` then Lean should immediately add those boilerplate things...

#### [ Kevin Buzzard (May 03 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060651):
Sometimes the access to the constructor has a different name to the constructor

#### [ Kevin Buzzard (May 03 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060657):
that happens with the proofs in equiv IIRC

#### [ Mario Carneiro (May 03 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060663):
If you look closely you will notice that the "boilerplate" often differs in minor details like use of notation, binding explicitness,...

#### [ Mario Carneiro (May 03 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060679):
The `structure` command already tries its best to give you theorems the way you want

#### [ Mario Carneiro (May 03 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060733):
but it's using heuristics, and sometimes we want it different in a particular case

#### [ Johan Commelin (May 03 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060736):
Yeah, I've seen that. So maybe we "mathematicians" should just learn to be more precise. (But we don't buy that mathematics isn't precise enough...)

#### [ Mario Carneiro (May 03 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060767):
It's like how there are (natural language) grammar rules, but also exceptions

#### [ Kevin Buzzard (May 03 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060771):
`equiv.apply_inverse_apply`

#### [ Kevin Buzzard (May 03 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060816):
There's a solid abstraction layer in action

#### [ Kevin Buzzard (May 03 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126061032):
```lean
import data.equiv 
example (X Y : Type) (e : equiv X Y) : e.apply_inverse_apply = e.right_inv := rfl
```

#### [ Kevin Buzzard (May 04 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126068166):
How about writing a `regex` which will replace all `(sigma ->_0 nat)` with `(nat)` and then make it all work again?

#### [ Kevin Buzzard (May 04 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126068171):
that sounds like an interesting challenge

#### [ Mario Carneiro (May 04 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126075513):
That sounds like it should wait for lean 4, when the parser is exposed to lean code

#### [ Johan Commelin (May 04 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126083049):
But we could just do an actual copy-paste-search-replace, right? The only thing that would remain is some theorems that say the result is isomorphic to what you started with.

#### [ Kevin Buzzard (May 05 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126116550):
https://github.com/johoelzl/mason-stother/blob/e6e1eb353d3dbea93571f761b408bc4900472179/poly_over_field.lean#L138

#### [ Kevin Buzzard (May 05 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126116566):
Johannes or his coauthor implemented polys in 1 variable already

#### [ Johan Commelin (May 05 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126149005):
Wow, there's already quite a lot there!

#### [ Scott Morrison (May 07 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126195259):
I'm not too up on univariate polynomials in Lean yet. Does anyone know if we have: 
"evaluation of `p : Z[x]` at `x : R` is a ring homomorphism from `Z[x]` to `R`"?

#### [ Johan Commelin (May 07 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126202825):
@**Scott Morrison** Voila, but multivariate: https://github.com/leanprover/mathlib/blob/master/linear_algebra/multivariate_polynomial.lean#L171-L173

#### [ Johan Commelin (May 07 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126202875):
Ok, and they haven't made it a ring homomorphism, but they show that it is additive and multiplicative...

#### [ Patrick Massot (May 07 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126204324):
@**Johannes Hölzl** what is the status of https://github.com/johoelzl/mason-stother? I guess JWageM is your student or something like this? Will this be in mathlib at some point?

#### [ Johannes Hölzl (May 07 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126204480):
Yes, @**Jens Wagemaker** is currently writing his Bachelor thesis on Mason-Stother. The theory itself is finished, and now he is writing the thesis itself. When this is finished we will port most parts of the developed theory to mathlib. Most parts, as we assume that polynomials over a field form a unique factorization domain, so everything from there on will need to wait until this is done. And there is quiet some divergence between the mathlib version Jens used and the current one, so there is some merging to be done.

#### [ Patrick Massot (May 07 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126204489):
I think someone did Euclidean domains recently

#### [ Patrick Massot (May 07 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126204491):
https://github.com/leanprover/mathlib/blob/d5c73c0b372d1181ca386e3264497e2c56077d93/algebra/euclidean_domain.lean

#### [ Patrick Massot (May 07 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126204534):
So it shouldn't be too hard to get UFD for polynomials with one variable over a field

#### [ Johannes Hölzl (May 07 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126204536):
No, it shouldn't be hard. Just needs to be done.

#### [ Johan Commelin (May 08 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126250080):
It seems to me that maybe `eval` should take its arguments in the opposite order. Then one can curry it, and get a (semi)-ring homomorphism.

#### [ Johan Commelin (May 08 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126250085):
Does that make sense?

#### [ Johan Commelin (May 08 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126253365):
Here is a commit that swaps the order of the arguments, and also proves that `eval f` is a ring homomorphism:
https://github.com/jcommelin/mathlib/commit/b0d0ca6d2892c902c5feffdfa58d3e3be2b013b2

#### [ Scott Morrison (May 08 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254364):
Looks promising!

#### [ Johannes Hölzl (May 08 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254544):
@**Johan Commelin** chaning the argument order of `eval` is a good idea. But is there a reason why you changed the applications from `p.eval f` to `eval f p`? Even with the changed order the `p.eval f` syntax should work. Lean figures out that `p` is a polynomial and looks up `mv_polynomial.eval`, inserting `p` at the appropriate place.

#### [ Johan Commelin (May 08 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254565):
Ok cool!

#### [ Johan Commelin (May 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254567):
I didn't know that

#### [ Johan Commelin (May 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254573):
But then, maybe I actually prefer `f.eval (p+q)` etc...

#### [ Johan Commelin (May 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254574):
What do you think of that?

#### [ Johan Commelin (May 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254576):
And then `f.eval` becomes a ring hom

#### [ Johan Commelin (May 08 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254633):
Aah, but that won't work, I guess... because then it doens't know where to find `eval`

#### [ Johan Commelin (May 08 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254634):
Right?

#### [ Johan Commelin (May 08 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254638):
There is some namespacing-magic going on, and that is why `p.eval` does work?

#### [ Johan Commelin (May 08 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254644):
/me is still learning new things every minute

#### [ Johan Commelin (May 08 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254816):
@**Johannes Hölzl** I think I prefer the `eval f p` notation. Even better would be some sort of `eval_f p`.

#### [ Johan Commelin (May 08 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254826):
Also, as a mathematician I always write `f` for polynomials, and `p` or `x` for the map `\sigma \to \alpha`. So that was pretty confusing (-;

#### [ Johannes Hölzl (May 08 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254914):
Well I would write `f` for the polynomial function (i.e. a function which can be represented as a polynomial) but I write `p`, `q` etc for the syntactic object.

#### [ Johan Commelin (May 08 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254978):
Yeah, I get that. (I only work with the syntactic objects... not the functions.)

#### [ Johannes Hölzl (May 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126255021):
Also, `f.eval p` doesn't work as `f` is in the function space, which AFAIK doesn't work with this syntax mechanism.

#### [ Johannes Hölzl (May 08 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126255032):
I prefer `p.eval f` as `eval` is a very generic name, and we will surely have multiple instances in different namespaces. `p.eval` makes it clear that we are referring to the polynomial one.

#### [ Johannes Hölzl (May 08 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126255034):
It is not necessary in `mv_polynomial`, but might be in other cases.

#### [ Johan Commelin (May 08 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126255170):
Ok, whichever you prefer. Should I change it and PR it?

#### [ Johannes Hölzl (May 08 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126255387):
Yeah, just change it back how it was before.

#### [ Johan Commelin (May 08 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126255866):
Oh my, it looks like I overdid it: https://github.com/jcommelin/mathlib/commit/2f63d86718e9e00ea55f67cb22f0f306fe8fcde3

#### [ Johannes Hölzl (May 08 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126258142):
why do you remove `eval_zero`?

#### [ Johan Commelin (May 08 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126259831):
Because it follows from `eval_C`...

#### [ Johannes Hölzl (May 08 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126260018):
But the simplifier doesn't see that `0 = C 0`! This is the reason for `eval_zero`: it is a `@[simp]` rule.

#### [ Johan Commelin (May 08 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126260363):
Hmmm, my bad...

#### [ Johan Commelin (May 08 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126260364):
I'll fix it

#### [ Johan Commelin (May 08 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126260507):
https://github.com/jcommelin/mathlib/commit/fa1710d88ff007cd947645136dd6c8986028430d
Voila


{% endraw %}
