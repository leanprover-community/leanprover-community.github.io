---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/17392Univariatepolynomials.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Univariate polynomials](https://leanprover-community.github.io/archive/116395maths/17392Univariatepolynomials.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (May 03 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058586):
<p>Here's another "canonical isomorphism" question. Johannes has implemented multivariate polynomials with variables in some index type sigma.</p>

#### [ Kevin Buzzard (May 03 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058599):
<p>But the univariate theory (polynomials in one variable) is special</p>

#### [ Kevin Buzzard (May 03 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058621):
<p>there are more theorems, for example; over a field these things form a Euclidean domain and a principal ideal domain etc</p>

#### [ Kevin Buzzard (May 03 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058631):
<p>so there is probably an argument for developing the theory of polynomials in one variable further.</p>

#### [ Kevin Buzzard (May 03 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058638):
<p>But one doesn't want to reprove everything</p>

#### [ Kevin Buzzard (May 03 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058689):
<p>and for polynomials in one variable, Johannes' definition becomes <code>(unit -&gt; nat) -&gt;_0 alpha</code></p>

#### [ Kevin Buzzard (May 03 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058693):
<p>and <code>unit -&gt; nat</code> is just canonically isomorphic to nat</p>

#### [ Kevin Buzzard (May 03 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058734):
<p>so now we have a sort-of insane way of setting up univariate polys</p>

#### [ Kevin Buzzard (May 03 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058744):
<p>and a sensible way</p>

#### [ Kevin Buzzard (May 03 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058793):
<p>and one would imagine that the sensible way, nat -&gt;_0 alpha, was the thing to use</p>

#### [ Kevin Buzzard (May 03 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058799):
<p>but one wants to import all Johannes' work for free, like definitions and the proof that polynomials form a ring etc</p>

#### [ Kevin Buzzard (May 03 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058801):
<p>so one first notes that there's an equiv between nat and (unit -&gt; nat)</p>

#### [ Kevin Buzzard (May 03 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058808):
<p>and then one wants to pull all of Johannes' definitions and theorems through this equiv</p>

#### [ Kevin Buzzard (May 03 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058877):
<p>but currently in Lean this seems hard. Is that right?</p>

#### [ Kevin Buzzard (May 03 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058980):
<p>I see. And this takes us back to exactly what we were thinking about a few days ago</p>

#### [ Kevin Buzzard (May 03 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058981):
<p>whether ring is transportable</p>

#### [ Kevin Buzzard (May 03 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126058985):
<p>(and it should be)</p>

#### [ Mario Carneiro (May 03 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059273):
<p>The short answer is yes, this is hard, but really it doesn't quite characterize the problem so well. We don't <em>want</em> to transfer the ring structure of <code>(unit -&gt; nat) -&gt;_0 alpha</code> to <code>nat -&gt;_0 alpha</code> in the "naive way" because this would make all the operations filter through the equivalence which would make them hard to use</p>

#### [ Mario Carneiro (May 03 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059350):
<p>(not to mention inefficient, not sure if we are deciding to care about this here)</p>

#### [ Kevin Buzzard (May 03 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059372):
<p>So if we need univariate polys</p>

#### [ Kevin Buzzard (May 03 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059391):
<p>is the best idea currently just to re-implement them? :-/</p>

#### [ Mario Carneiro (May 03 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059411):
<p>we would want instead to define the operations specially for univariate polys, but prove that the canonical equiv is a ring homomorphism and use that to prove that the other structure is a ring</p>

#### [ Mario Carneiro (May 03 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059474):
<p>this is basically what <code>transfer</code> is intended to do</p>

#### [ Mario Carneiro (May 03 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059492):
<p>You should check out <code>num</code> a bit to see how the process can work</p>

#### [ Mario Carneiro (May 03 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059536):
<p>I define operations on <code>num</code> that act like corresponding operations on <code>nat</code>, prove that the map from <code>nat</code> to <code>num</code> preserves the operations, and use that to prove that <code>num</code> is a <code>decidable_linear_ordered_semiring</code> or whatever</p>

#### [ Johan Commelin (May 03 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059543):
<p>Can't we have some <code>meta</code> code that automatically generates all the theorems and proof, given the <code>equiv</code>, so that it does the reimplementation for us? Together with transport statements that link the new implementation to the old one...</p>

#### [ Kevin Buzzard (May 03 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059579):
<p>This approach is "better" than the one used to transfer proofs from multiplicative groups to additive groups, right?</p>

#### [ Mario Carneiro (May 03 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059588):
<p>That's <code>transfer</code></p>

#### [ Kevin Buzzard (May 03 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059591):
<p>Because there the two types are themselves equivalent in a strong sense</p>

#### [ Kevin Buzzard (May 03 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059616):
<p>so you can literally translate a proof that a group with multiplication as group law has some property, to the same proof that a group with addition as group law has some analogous property</p>

#### [ Kevin Buzzard (May 03 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059644):
<p>but here unit -&gt; nat is a different type to nat</p>

#### [ Mario Carneiro (May 03 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059694):
<p>In some sense the equiv from <code>add_group</code> to <code>group</code> is "cheap"</p>

#### [ Mario Carneiro (May 03 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059719):
<p>and the underlying carrier types are defeq, which helps a lot</p>

#### [ Kevin Buzzard (May 03 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059726):
<p>and so the argument somehow relies on the fact that Johannes didn't do anything funny with his unit -&gt; nat type which we can't also do with the nat type</p>

#### [ Mario Carneiro (May 03 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059793):
<p>For more general equivalences, <code>equiv</code> does the job</p>

#### [ Mario Carneiro (May 03 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059797):
<p>the argument doesn't rely on anything more</p>

#### [ Mario Carneiro (May 03 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059808):
<p>(but you do have to prove that the equiv respects the operations)</p>

#### [ Kevin Buzzard (May 03 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059835):
<p>Stupid question</p>

#### [ Kevin Buzzard (May 03 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059844):
<p>what is an example of something you can do in type theory for unit -&gt; nat which you can't do for nat</p>

#### [ Kevin Buzzard (May 03 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059852):
<p>I can't make that rigorous</p>

#### [ Mario Carneiro (May 03 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059855):
<p>they are equiv, so nothing?</p>

#### [ Mario Carneiro (May 03 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059918):
<p>In PL theory they are a bit different, since one is like a delayed computation and the other is a value, but I assume you are ignoring this distinction</p>

#### [ Kevin Buzzard (May 03 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059927):
<p>yes</p>

#### [ Kevin Buzzard (May 03 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059948):
<p>If equiv commutes with everything in dependent type theory</p>

#### [ Kevin Buzzard (May 03 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059956):
<p>why isn't this transportable stuff just standard and built in?</p>

#### [ Kevin Buzzard (May 03 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059967):
<p>Is it in Coq?</p>

#### [ Mario Carneiro (May 03 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059977):
<p>Of course it doesn't commute with everything, but you can always lift operations by pre/post composing with it</p>

#### [ Kevin Buzzard (May 03 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059987):
<p>right</p>

#### [ Kevin Buzzard (May 03 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126059996):
<p>and if you go from X to Y and then back to X you will have the identity</p>

#### [ Mario Carneiro (May 03 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060061):
<p>you will have propositionally the identity, it's (probably) not defeq</p>

#### [ Kevin Buzzard (May 03 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060069):
<p>oh boy</p>

#### [ Mario Carneiro (May 03 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060073):
<p>that means that you may need to cast stuff across the equality</p>

#### [ Kevin Buzzard (May 03 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060084):
<p>but can a computer construct the proof if it's not defeq?</p>

#### [ Mario Carneiro (May 03 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060087):
<p>and those casts build up and get more complicated</p>

#### [ Mario Carneiro (May 03 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060115):
<p>the proof is given, it's an equiv so that's part of the structure</p>

#### [ Johan Commelin (May 03 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060181):
<p>Ouch, so this is going to break us up if we are somewhere deep down in the guts of formalising the proof of the Weil conjectures</p>

#### [ Johan Commelin (May 03 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060195):
<p>Because you exceed <code>max_transfers</code> which was set to <code>1000</code> or something...</p>

#### [ Mario Carneiro (May 03 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060212):
<p>just try to have a better way to say stuff than transferring some other statement when casts get involved</p>

#### [ Johan Commelin (May 03 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060217):
<p>(Maybe I am blatantly displaying my ignorance...)</p>

#### [ Mario Carneiro (May 03 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060227):
<p>mostly avoid too many dependent types</p>

#### [ Kevin Buzzard (May 03 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060234):
<p>we don't care that the proofs can get complicated because they are irrelevant</p>

#### [ Mario Carneiro (May 03 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060237):
<p>I'm talking about terms</p>

#### [ Kevin Buzzard (May 03 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060241):
<p>right</p>

#### [ Kevin Buzzard (May 03 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060283):
<p>if I want to define affine 1-space</p>

#### [ Kevin Buzzard (May 03 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060288):
<p><code>Spec(R[x])</code></p>

#### [ Kevin Buzzard (May 03 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060295):
<p>then in the definition of e.g. the local ring at some point</p>

#### [ Kevin Buzzard (May 03 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060296):
<p>there will be casts everywhere</p>

#### [ Kevin Buzzard (May 03 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060299):
<p>it will be unreadable</p>

#### [ Johan Commelin (May 03 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060301):
<p>Mario, I am a bit afraid that this is not so easy to avoid... or the formalisation might become way more difficult then they "maths" proof</p>

#### [ Mario Carneiro (May 03 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060311):
<p>It's all about modularity</p>

#### [ Mario Carneiro (May 03 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060317):
<p>just break stuff up into bite sized chunks and it's all doable</p>

#### [ Kevin Buzzard (May 03 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060318):
<p>Is this the reason that all the big type theory proofs of maths theorems are proofs about objects like finite groups rather than locally Noetherian schemes?</p>

#### [ Kevin Buzzard (May 03 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060325):
<p>problems pile up</p>

#### [ Kevin Buzzard (May 03 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060364):
<p>and it's difficult to make them go away</p>

#### [ Johan Commelin (May 03 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060371):
<p>Ok, then I misunderstood you. I thought that if you started combining these "modules" then some evil synergy would multiply their "badness of casts"</p>

#### [ Mario Carneiro (May 03 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060386):
<p>Just have solid abstraction layers, as long as the informal math doesn't get notationally horrible the formal horribleness is bounded</p>

#### [ Johan Commelin (May 03 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060396):
<p>Ok, I really hope so.</p>

#### [ Mario Carneiro (May 03 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060405):
<p>The multiplying badness of casts happens when you try to do it in general over the whole theory</p>

#### [ Johan Commelin (May 03 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060451):
<p>If Kevin is meeting all these problems in the definition of an affine scheme... then we want 1) all sorts of properties of morphisms of schemes, 2) topos theory, 3) derived categories, 4) etale cohomology, 5)... etc etc</p>

#### [ Mario Carneiro (May 03 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060452):
<p>i.e. you write some tactic that just plows through the whole system to transfer any term across some equiv</p>

#### [ Johan Commelin (May 03 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060453):
<p>before you can even sensibly formulate the Weil conjectures</p>

#### [ Mario Carneiro (May 03 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060467):
<p>these kinds of tactics care nothing for abstraction</p>

#### [ Johan Commelin (May 03 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060472):
<p>Hmmm, I'm still confused...</p>

#### [ Johan Commelin (May 03 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060531):
<p>Do you think that in the end we can have automation help us with these transfers, and still have the modularity? Or does the automation mean that it will "plow through the system"?</p>

#### [ Kevin Buzzard (May 03 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060538):
<p>When I started reading proofs in mathlib</p>

#### [ Kevin Buzzard (May 03 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060552):
<p>I was really confused why people would create a new structure and then instantly write functions giving access to the things used to construct the structure</p>

#### [ Kevin Buzzard (May 03 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060554):
<p>but</p>

#### [ Kevin Buzzard (May 03 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060558):
<p>it's all part</p>

#### [ Kevin Buzzard (May 03 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060563):
<p>of a solid abstraction layer</p>

#### [ Johan Commelin (May 03 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060576):
<p>Hmm, that's a good example. A "mathematician" wouldn't (want) to do that.</p>

#### [ Johan Commelin (May 03 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060619):
<p>Again, couldn't some automation do that for us?</p>

#### [ Kevin Buzzard (May 03 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060623):
<p>Getting the code to run fast is not our problem :-)</p>

#### [ Mario Carneiro (May 03 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060635):
<p>In theory, but it probably would need lots of tweaks</p>

#### [ Kevin Buzzard (May 03 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060637):
<p>You just wait for either the CS people to write better tactics or for the engineers to write faster chips</p>

#### [ Johan Commelin (May 03 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060639):
<p>If I write <code>structure</code> then Lean should immediately add those boilerplate things...</p>

#### [ Kevin Buzzard (May 03 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060651):
<p>Sometimes the access to the constructor has a different name to the constructor</p>

#### [ Kevin Buzzard (May 03 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060657):
<p>that happens with the proofs in equiv IIRC</p>

#### [ Mario Carneiro (May 03 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060663):
<p>If you look closely you will notice that the "boilerplate" often differs in minor details like use of notation, binding explicitness,...</p>

#### [ Mario Carneiro (May 03 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060679):
<p>The <code>structure</code> command already tries its best to give you theorems the way you want</p>

#### [ Mario Carneiro (May 03 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060733):
<p>but it's using heuristics, and sometimes we want it different in a particular case</p>

#### [ Johan Commelin (May 03 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060736):
<p>Yeah, I've seen that. So maybe we "mathematicians" should just learn to be more precise. (But we don't buy that mathematics isn't precise enough...)</p>

#### [ Mario Carneiro (May 03 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060767):
<p>It's like how there are (natural language) grammar rules, but also exceptions</p>

#### [ Kevin Buzzard (May 03 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060771):
<p><code>equiv.apply_inverse_apply</code></p>

#### [ Kevin Buzzard (May 03 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126060816):
<p>There's a solid abstraction layer in action</p>

#### [ Kevin Buzzard (May 03 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126061032):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">X</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="n">e</span><span class="bp">.</span><span class="n">apply_inverse_apply</span> <span class="bp">=</span> <span class="n">e</span><span class="bp">.</span><span class="n">right_inv</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Kevin Buzzard (May 04 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126068166):
<p>How about writing a <code>regex</code> which will replace all <code>(sigma -&gt;_0 nat)</code> with <code>(nat)</code> and then make it all work again?</p>

#### [ Kevin Buzzard (May 04 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126068171):
<p>that sounds like an interesting challenge</p>

#### [ Mario Carneiro (May 04 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126075513):
<p>That sounds like it should wait for lean 4, when the parser is exposed to lean code</p>

#### [ Johan Commelin (May 04 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126083049):
<p>But we could just do an actual copy-paste-search-replace, right? The only thing that would remain is some theorems that say the result is isomorphic to what you started with.</p>

#### [ Kevin Buzzard (May 05 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126116550):
<p><a href="https://github.com/johoelzl/mason-stother/blob/e6e1eb353d3dbea93571f761b408bc4900472179/poly_over_field.lean#L138" target="_blank" title="https://github.com/johoelzl/mason-stother/blob/e6e1eb353d3dbea93571f761b408bc4900472179/poly_over_field.lean#L138">https://github.com/johoelzl/mason-stother/blob/e6e1eb353d3dbea93571f761b408bc4900472179/poly_over_field.lean#L138</a></p>

#### [ Kevin Buzzard (May 05 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126116566):
<p>Johannes or his coauthor implemented polys in 1 variable already</p>

#### [ Johan Commelin (May 05 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126149005):
<p>Wow, there's already quite a lot there!</p>

#### [ Scott Morrison (May 07 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126195259):
<p>I'm not too up on univariate polynomials in Lean yet. Does anyone know if we have: <br>
"evaluation of <code>p : Z[x]</code> at <code>x : R</code> is a ring homomorphism from <code>Z[x]</code> to <code>R</code>"?</p>

#### [ Johan Commelin (May 07 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126202825):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> Voila, but multivariate: <a href="https://github.com/leanprover/mathlib/blob/master/linear_algebra/multivariate_polynomial.lean#L171-L173" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/linear_algebra/multivariate_polynomial.lean#L171-L173">https://github.com/leanprover/mathlib/blob/master/linear_algebra/multivariate_polynomial.lean#L171-L173</a></p>

#### [ Johan Commelin (May 07 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126202875):
<p>Ok, and they haven't made it a ring homomorphism, but they show that it is additive and multiplicative...</p>

#### [ Patrick Massot (May 07 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126204324):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> what is the status of <a href="https://github.com/johoelzl/mason-stother" target="_blank" title="https://github.com/johoelzl/mason-stother">https://github.com/johoelzl/mason-stother</a>? I guess JWageM is your student or something like this? Will this be in mathlib at some point?</p>

#### [ Johannes Hölzl (May 07 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126204480):
<p>Yes, <span class="user-mention" data-user-id="111160">@Jens Wagemaker</span> is currently writing his Bachelor thesis on Mason-Stother. The theory itself is finished, and now he is writing the thesis itself. When this is finished we will port most parts of the developed theory to mathlib. Most parts, as we assume that polynomials over a field form a unique factorization domain, so everything from there on will need to wait until this is done. And there is quiet some divergence between the mathlib version Jens used and the current one, so there is some merging to be done.</p>

#### [ Patrick Massot (May 07 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126204489):
<p>I think someone did Euclidean domains recently</p>

#### [ Patrick Massot (May 07 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126204491):
<p><a href="https://github.com/leanprover/mathlib/blob/d5c73c0b372d1181ca386e3264497e2c56077d93/algebra/euclidean_domain.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/d5c73c0b372d1181ca386e3264497e2c56077d93/algebra/euclidean_domain.lean">https://github.com/leanprover/mathlib/blob/d5c73c0b372d1181ca386e3264497e2c56077d93/algebra/euclidean_domain.lean</a></p>

#### [ Patrick Massot (May 07 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126204534):
<p>So it shouldn't be too hard to get UFD for polynomials with one variable over a field</p>

#### [ Johannes Hölzl (May 07 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126204536):
<p>No, it shouldn't be hard. Just needs to be done.</p>

#### [ Johan Commelin (May 08 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126250080):
<p>It seems to me that maybe <code>eval</code> should take its arguments in the opposite order. Then one can curry it, and get a (semi)-ring homomorphism.</p>

#### [ Johan Commelin (May 08 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126250085):
<p>Does that make sense?</p>

#### [ Johan Commelin (May 08 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126253365):
<p>Here is a commit that swaps the order of the arguments, and also proves that <code>eval f</code> is a ring homomorphism:<br>
<a href="https://github.com/jcommelin/mathlib/commit/b0d0ca6d2892c902c5feffdfa58d3e3be2b013b2" target="_blank" title="https://github.com/jcommelin/mathlib/commit/b0d0ca6d2892c902c5feffdfa58d3e3be2b013b2">https://github.com/jcommelin/mathlib/commit/b0d0ca6d2892c902c5feffdfa58d3e3be2b013b2</a></p>

#### [ Scott Morrison (May 08 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254364):
<p>Looks promising!</p>

#### [ Johannes Hölzl (May 08 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254544):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> chaning the argument order of <code>eval</code> is a good idea. But is there a reason why you changed the applications from <code>p.eval f</code> to <code>eval f p</code>? Even with the changed order the <code>p.eval f</code> syntax should work. Lean figures out that <code>p</code> is a polynomial and looks up <code>mv_polynomial.eval</code>, inserting <code>p</code> at the appropriate place.</p>

#### [ Johan Commelin (May 08 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254565):
<p>Ok cool!</p>

#### [ Johan Commelin (May 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254567):
<p>I didn't know that</p>

#### [ Johan Commelin (May 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254573):
<p>But then, maybe I actually prefer <code>f.eval (p+q)</code> etc...</p>

#### [ Johan Commelin (May 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254574):
<p>What do you think of that?</p>

#### [ Johan Commelin (May 08 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254576):
<p>And then <code>f.eval</code> becomes a ring hom</p>

#### [ Johan Commelin (May 08 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254633):
<p>Aah, but that won't work, I guess... because then it doens't know where to find <code>eval</code></p>

#### [ Johan Commelin (May 08 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254634):
<p>Right?</p>

#### [ Johan Commelin (May 08 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254638):
<p>There is some namespacing-magic going on, and that is why <code>p.eval</code> does work?</p>

#### [ Johan Commelin (May 08 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254644):
<p>/me is still learning new things every minute</p>

#### [ Johan Commelin (May 08 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254816):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I think I prefer the <code>eval f p</code> notation. Even better would be some sort of <code>eval_f p</code>.</p>

#### [ Johan Commelin (May 08 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254826):
<p>Also, as a mathematician I always write <code>f</code> for polynomials, and <code>p</code> or <code>x</code> for the map <code>\sigma \to \alpha</code>. So that was pretty confusing (-;</p>

#### [ Johannes Hölzl (May 08 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254914):
<p>Well I would write <code>f</code> for the polynomial function (i.e. a function which can be represented as a polynomial) but I write <code>p</code>, <code>q</code> etc for the syntactic object.</p>

#### [ Johan Commelin (May 08 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126254978):
<p>Yeah, I get that. (I only work with the syntactic objects... not the functions.)</p>

#### [ Johannes Hölzl (May 08 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126255021):
<p>Also, <code>f.eval p</code> doesn't work as <code>f</code> is in the function space, which AFAIK doesn't work with this syntax mechanism.</p>

#### [ Johannes Hölzl (May 08 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126255032):
<p>I prefer <code>p.eval f</code> as <code>eval</code> is a very generic name, and we will surely have multiple instances in different namespaces. <code>p.eval</code> makes it clear that we are referring to the polynomial one.</p>

#### [ Johannes Hölzl (May 08 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126255034):
<p>It is not necessary in <code>mv_polynomial</code>, but might be in other cases.</p>

#### [ Johan Commelin (May 08 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126255170):
<p>Ok, whichever you prefer. Should I change it and PR it?</p>

#### [ Johannes Hölzl (May 08 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126255387):
<p>Yeah, just change it back how it was before.</p>

#### [ Johan Commelin (May 08 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126255866):
<p>Oh my, it looks like I overdid it: <a href="https://github.com/jcommelin/mathlib/commit/2f63d86718e9e00ea55f67cb22f0f306fe8fcde3" target="_blank" title="https://github.com/jcommelin/mathlib/commit/2f63d86718e9e00ea55f67cb22f0f306fe8fcde3">https://github.com/jcommelin/mathlib/commit/2f63d86718e9e00ea55f67cb22f0f306fe8fcde3</a></p>

#### [ Johannes Hölzl (May 08 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126258142):
<p>why do you remove <code>eval_zero</code>?</p>

#### [ Johan Commelin (May 08 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126259831):
<p>Because it follows from <code>eval_C</code>...</p>

#### [ Johannes Hölzl (May 08 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126260018):
<p>But the simplifier doesn't see that <code>0 = C 0</code>! This is the reason for <code>eval_zero</code>: it is a <code>@[simp]</code> rule.</p>

#### [ Johan Commelin (May 08 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126260363):
<p>Hmmm, my bad...</p>

#### [ Johan Commelin (May 08 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126260364):
<p>I'll fix it</p>

#### [ Johan Commelin (May 08 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Univariate%20polynomials/near/126260507):
<p><a href="https://github.com/jcommelin/mathlib/commit/fa1710d88ff007cd947645136dd6c8986028430d" target="_blank" title="https://github.com/jcommelin/mathlib/commit/fa1710d88ff007cd947645136dd6c8986028430d">https://github.com/jcommelin/mathlib/commit/fa1710d88ff007cd947645136dd6c8986028430d</a><br>
Voila</p>


{% endraw %}
