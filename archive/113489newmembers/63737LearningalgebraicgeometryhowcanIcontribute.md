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
<p>Hi everyone! A friend sent me a link to <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>'s answer on the "What are perfectoid spaces?" MO question, which is how I got here. I'm learning algebraic geometry right now. More to the point, I have some experience using Agda and Idris (but not Lean).</p>
<p>I would enjoy helping to formalise material related to what I'm learning; how can I help?</p>

#### [ Kevin Buzzard (Sep 02 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214551):
<p>Well, someone needs to prove that the integral closure of a subring is a subring :-)</p>

#### [ Kenny Lau (Sep 02 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214554):
<p>what the hell, <span class="user-mention" data-user-id="128083">@Soham Chowdhury</span></p>

#### [ Kevin Buzzard (Sep 02 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214594):
<p>Here are some projects which the community thinks are accessible:  <a href="https://github.com/leanprover-community/mathlib/wiki/Potential-projects" target="_blank" title="https://github.com/leanprover-community/mathlib/wiki/Potential-projects">https://github.com/leanprover-community/mathlib/wiki/Potential-projects</a></p>

#### [ Soham Chowdhury (Sep 02 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214597):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> is it ... possible I know you?</p>

#### [ Kenny Lau (Sep 02 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214604):
<p>guess who sent you that link</p>

#### [ Soham Chowdhury (Sep 02 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214651):
<p>Oh haha</p>
<blockquote>
<p>Well, someone needs to prove that the integral closure of a subring is a subring :-)</p>
</blockquote>
<p>That sounds like something I can do!</p>

#### [ Kevin Buzzard (Sep 02 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214652):
<p>Here is a challenging project which would teach you a bunch about Lean: prove that Hom(X,Spec(R)) = Hom(R,O_X(X)).</p>

#### [ Kenny Lau (Sep 02 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214656):
<blockquote>
<p>Here is a challenging project which would teach you a bunch about Lean: prove that Hom(X,Spec(R)) = Hom(R,O_X(X)).</p>
</blockquote>
<p>yeah, that...</p>

#### [ Kevin Buzzard (Sep 02 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214665):
<p>Anthony Bordg also sent me an email saying he might be interested in doing this. As I'm sure you'll know from Idris, there's a big difference between learning alg geom from a book and actually telling Lean about it.</p>

#### [ Kevin Buzzard (Sep 02 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214666):
<p>What exactly are you learning?</p>

#### [ Soham Chowdhury (Sep 02 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214761):
<p>Chapter 5 of Vakil's FOAG right now, so I don't know all that much :)</p>

#### [ Soham Chowdhury (Sep 02 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214762):
<p>But basic commutative algebra sounds like something I could get started on.</p>

#### [ Kevin Buzzard (Sep 02 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214812):
<p>Several people have been asking what they could work on. Of course embarking on a project like proving a standard algebra theorem with a new theorem prover (and then asking a gazillion questions here) is a really good way to learn how to use the theorem prover, but I am currently slightly worried that whenever someone who knows any algebra asks what they could do, I reply with basically the same reply.</p>

#### [ Kevin Buzzard (Sep 02 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214820):
<p>As far as comm alg goes, we have localisation of rings, a PR for tensor products, a definition of Noetherian rings and modules but 0 theorems (other than the fact that the two usual definitions are equivalent), and enough group theory to make doing basic commutative algebra feasible.</p>

#### [ Soham Chowdhury (Sep 02 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214872):
<p>I guess even if someone "beats me to" one of these problems, I'm sure the payoff from becoming comfortable with Lean will make it that much easier to work on harder things like, e.g. the Hom(X, Spec R) theorem you mentioned.</p>

#### [ Kevin Buzzard (Sep 02 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214874):
<p>Lean has affine schemes but not projective schemes, so you're a little ahead ;-)</p>

#### [ Kevin Buzzard (Sep 02 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214921):
<p>However they're not in mathlib, they're in a stacks project repo on my github <a href="https://github.com/kbuzzard/lean-stacks-project" target="_blank" title="https://github.com/kbuzzard/lean-stacks-project">https://github.com/kbuzzard/lean-stacks-project</a> which I wrote to learn Lean, so this code sometimes leaves some things to be desired...</p>

#### [ Soham Chowdhury (Sep 02 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214971):
<p>Is the definition of Noetherian modules in mathlib <code>master</code>? I can't seem to find it there.</p>

#### [ Kevin Buzzard (Sep 02 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133214978):
<p>I watched it be born but I don't know where it is. It was only created on Wednesday.</p>

#### [ Mario Carneiro (Sep 02 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133215018):
<p>it is in a branch on the community fork</p>

#### [ Kevin Buzzard (Sep 02 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133215023):
<p><a href="https://github.com/leanprover-community/mathlib/search?q=noetherian&amp;unscoped_q=noetherian" target="_blank" title="https://github.com/leanprover-community/mathlib/search?q=noetherian&amp;unscoped_q=noetherian">https://github.com/leanprover-community/mathlib/search?q=noetherian&amp;unscoped_q=noetherian</a> doesn't find it</p>

#### [ Kevin Buzzard (Sep 02 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133215031):
<p><a href="https://github.com/leanprover-community/mathlib/commit/ef5c110626b0197118299071a98ed98e1aead287" target="_blank" title="https://github.com/leanprover-community/mathlib/commit/ef5c110626b0197118299071a98ed98e1aead287">https://github.com/leanprover-community/mathlib/commit/ef5c110626b0197118299071a98ed98e1aead287</a></p>

#### [ Soham Chowdhury (Sep 02 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133215039):
<p>I believe GitHub search only looks in <code>master</code>.</p>

#### [ Kevin Buzzard (Sep 02 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133215098):
<p>I believe that too, now. We next need that submodules and quotient modules of Noetherian modules are Noetherian. This should be easy if we have some basic facts about there being a natural injection from the submodules of <code>M/N</code> to the submodules of <code>M</code> -- is this in mathlib? <span class="user-mention" data-user-id="110064">@Kenny Lau</span> Is this something like Proposition 1.1 of A-M?</p>

#### [ Kevin Buzzard (Sep 02 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133215139):
<p>oh, that's only for rings. OK so here's a concrete thing we need: order-preserving bijection between submodules of M/N and submodules of M containing N.</p>

#### [ Kevin Buzzard (Sep 02 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133215140):
<p>Is that there already? Does anyone know? I don't remember seeing it.</p>

#### [ Kenny Lau (Sep 02 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133215344):
<p>looks like a Galois correspondence to me</p>

#### [ Soham Chowdhury (Sep 02 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133218718):
<p>I'm going to check back here if (rather, when) I have questions. Thanks for the pointers.</p>

#### [ Patrick Massot (Sep 02 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133219598):
<p><span class="user-mention" data-user-id="128083">@Soham Chowdhury</span> do you know where to start? (hint: the answer is <a href="https://leanprover.github.io/theorem_proving_in_lean/" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/">https://leanprover.github.io/theorem_proving_in_lean/</a>).</p>

#### [ Johan Commelin (Sep 03 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Learning%20algebraic%20geometry%3B%20how%20can%20I%20contribute%3F/near/133239139):
<p>Also see this thread in Zulip: <a href="#narrow/stream/116395-maths/subject/noetherian.20modules" title="#narrow/stream/116395-maths/subject/noetherian.20modules">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/noetherian.20modules</a> (You might need to enable the "maths" stream somewhere in your settings; but I thought this was done by default nowadays.)</p>


{% endraw %}
