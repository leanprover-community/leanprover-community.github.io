---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/05512Transferhomomorphism.html
---

## Stream: [maths](index.html)
### Topic: [Transfer homomorphism](05512Transferhomomorphism.html)

---


{% raw %}
#### [ Kenny Lau (Jun 15 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127678):
<p>Let G be a group and H a subgroup of finite index. Then, pick a set-theoretic section s:G/H-&gt;G where G/H is the right cosets. Then, the transfer homomorphism G^ab -&gt; H^ab is defined by sending [[g]] to prod[x in G/H] s(x) g s(xg)^-1.</p>

#### [ Kenny Lau (Jun 15 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127688):
<p>The wonderful thing about this homomorphism is that it is independent of the section s</p>

#### [ Kenny Lau (Jun 15 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127734):
<p>but this also means that I will be lifting arbitrarily many quotients.</p>

#### [ Kenny Lau (Jun 15 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127738):
<p>How should I do that?</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127753):
<p>using choice</p>

#### [ Kenny Lau (Jun 15 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127757):
<p>but it will be noncomputable</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127765):
<p>obviously</p>

#### [ Kenny Lau (Jun 15 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127769):
<p>can I make it computable?</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127773):
<p>nothing about what you said sounds remotely computable</p>

#### [ Kenny Lau (Jun 15 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127776):
<p>it seems computable to me</p>

#### [ Kenny Lau (Jun 15 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127781):
<p>the map is independent of s</p>

#### [ Kenny Lau (Jun 15 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127784):
<p>there is only finitely many choices to make</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127789):
<p>How do you even know such a function <code>s</code> exists?</p>

#### [ Kenny Lau (Jun 15 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127833):
<p>you don't need the function s. you just need to lift finitely many quotients</p>

#### [ Kenny Lau (Jun 15 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127837):
<p>obviously s is noncomputable</p>

#### [ Kenny Lau (Jun 15 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127839):
<p>but the transfer homomorphism should be computable</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127843):
<p>How is G^ab defined</p>

#### [ Kenny Lau (Jun 15 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127847):
<p>G quotient G commutator</p>

#### [ Kenny Lau (Jun 15 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127851):
<p>G/[G,G]</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127866):
<p>And in what sense is G/H finite</p>

#### [ Kenny Lau (Jun 15 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127881):
<p>in the sense that H is a finite-index subgroup of G</p>

#### [ Kenny Lau (Jun 15 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127885):
<p>so G/H is a fintype</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127954):
<p>I mean, how are you expressing "finite index"</p>

#### [ Kenny Lau (Jun 15 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127956):
<p>[fintype G/H]</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127976):
<p>And how do you construct a section?</p>

#### [ Kenny Lau (Jun 15 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127978):
<p>I don't</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127979):
<p>Any section at all</p>

#### [ Kenny Lau (Jun 15 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128127982):
<p>section is noncomputable</p>

#### [ Kenny Lau (Jun 15 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128022):
<p>but the transfer homomorphism is independent of section</p>

#### [ Kenny Lau (Jun 15 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128025):
<p>so I need finitely many lifts</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128034):
<p>Even ignoring the lifts</p>

#### [ Kenny Lau (Jun 15 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128046):
<p>I can't construct any section computably</p>

#### [ Kenny Lau (Jun 15 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128053):
<p>if that's what you mean</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128081):
<p>I think I see what you mean with iterating lifts, that might be possible</p>

#### [ Kenny Lau (Jun 15 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128113):
<p>hmm</p>

#### [ Kenny Lau (Jun 15 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128118):
<p>but it will be very hard</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128119):
<p>But you will have to redo the work of <code>finset.pi</code></p>

#### [ Kenny Lau (Jun 15 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128120):
<p>each element of the product is not well-defined</p>

#### [ Kenny Lau (Jun 15 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128123):
<p>it is the product itself which is well-defined</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128127):
<p>You have a single quotient in the output</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128148):
<p>or even a <code>trunc</code>, if you express the section property in a subtype</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128197):
<p>Do you have decidable equality on G/H?</p>

#### [ Kenny Lau (Jun 15 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128202):
<p>is that necessary?</p>

#### [ Kenny Lau (Jun 15 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128210):
<p>I feel that it is already computable</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128212):
<p>it comes up in the construction of the functions</p>

#### [ Kenny Lau (Jun 15 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128247):
<p>how would you do it?</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128310):
<p>I am reminded of a discussion with <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> about generalizing the quotient axioms to allow for indexed families of quotients</p>

#### [ Kenny Lau (Jun 15 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128314):
<p>but everything is finite here</p>

#### [ Kenny Lau (Jun 15 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128321):
<p>the axioms should be enough</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128324):
<p>But it's provable in the finite case, and that's what I would prove</p>

#### [ Kenny Lau (Jun 15 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128328):
<p>hmm</p>

#### [ Kenny Lau (Jun 15 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128330):
<p>this is very hard</p>

#### [ Kenny Lau (Jun 15 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128332):
<p>can I even do this in 3 days</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128339):
<p>It's less than 100 lines for sure</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128430):
<p>Also, decidable equality is definitely necessary for constructing sections</p>

#### [ Kenny Lau (Jun 15 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128439):
<p>I don't want to construct any section</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128445):
<p>You do, that's the whole point</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128453):
<p>You are lifting stuff from a quotient but that's not so important</p>

#### [ Kenny Lau (Jun 15 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128510):
<p>hmm</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128520):
<p>Are you suggesting that there is a way to define the transfer that avoids reference to any section?</p>

#### [ Kenny Lau (Jun 15 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128525):
<p>If I do a product indexed by a fintype do I need decidable equality?</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128530):
<p>I assume you have to make coordinated choices in order to define the sums</p>

#### [ Kenny Lau (Jun 15 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128535):
<p>but everything is finite</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128620):
<p>No, products of elements in a commutative group over a finset does not require decidable_eq</p>

#### [ Kenny Lau (Jun 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128626):
<p>then why do I need it now</p>

#### [ Kenny Lau (Jun 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128629):
<p>even if the choice is coordinated</p>

#### [ Kenny Lau (Jun 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128631):
<p>it's still finite</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128637):
<p>to define the section that coordinates the choices</p>

#### [ Kenny Lau (Jun 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128642):
<p>but everything is well-defined</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128690):
<p>How are you going to remember your finitely many choices if not with a function? And how is that function indexed?</p>

#### [ Kenny Lau (Jun 15 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128694):
<p>isn't it the philosophy of quotient that if your choices are well-defined then you are computable?</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128703):
<p>That's not the problem</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128708):
<p>You want a function G/H -&gt; G</p>

#### [ Kenny Lau (Jun 15 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128717):
<p>list.rec is computable</p>

#### [ Kenny Lau (Jun 15 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128718):
<p>multiset.rec is computable</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128719):
<p>that means distinguishing elements of G/H when they are sent to different members of G</p>

#### [ Kenny Lau (Jun 15 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128721):
<p>finset.rec is computable</p>

#### [ Kenny Lau (Jun 15 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128128806):
<p>hmm</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128129541):
<p>Here's a way to state the section property without groups:</p>
<div class="codehilite"><pre><span></span>def choices {ι : Type*} [fintype ι] {α : ι → Type*} (R : ∀ i, α i → α i → Prop)
    (f : ∀ i, quot (R i)) : quot (λ (a b : Π i, α i), ∀ i, R i (a i) (b i)) := sorry
</pre></div>

#### [ Kenny Lau (Jun 15 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128129595):
<p>I only have one quotient though</p>

#### [ Kenny Lau (Jun 15 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128129601):
<p>it's just G/H</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128129610):
<p>That doesn't make too much of a difference</p>

#### [ Mario Carneiro (Jun 15 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128129673):
<p>The point here is the interchanging of pi and quot</p>

#### [ Kenny Lau (Jun 15 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128129683):
<p>I see</p>

#### [ Mario Carneiro (Jun 15 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128129782):
<p>It seems reasonable to have that function as a computable axiom, this is what Gabriel and I discussed</p>

#### [ Kenny Lau (Jun 15 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128129786):
<p>I see</p>

#### [ Mario Carneiro (Jun 15 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128129787):
<p>because it has an obvious VM interpretation</p>

#### [ Kenny Lau (Jun 15 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128129793):
<p>but is it provable?</p>

#### [ Mario Carneiro (Jun 15 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128129794):
<p>but you can only prove it for I finite</p>

#### [ Mario Carneiro (Jun 15 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128129806):
<p>and even then I believe it implies decidable equality of I</p>

#### [ Kevin Buzzard (Jun 15 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128130433):
<p>Kenny, if you are under time constraints, why not just make it noncomputable, make sure everything else is done, and come back to it later if you have time?</p>

#### [ Mario Carneiro (Jun 15 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128130542):
<p>I will look into this theorem, and report back if I can prove it. Feel free to assume it</p>

#### [ Reid Barton (Jun 15 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128130568):
<p>This version is not quite right though, because for example one of the <code>R i</code> could be the empty relation, and then the "product relation" is also empty</p>

#### [ Reid Barton (Jun 15 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128130653):
<p>You need to assume the <code>R i</code> are at least reflexive, or build the "product relation" differently, like the Cartesian product of graphs</p>

#### [ Mario Carneiro (Jun 15 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128130733):
<p>That's fine, <code>quot</code> implicitly takes the equivalence closure of the given relation</p>

#### [ Mario Carneiro (Jun 15 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128130750):
<p><code>quotient</code> is the variant that explicitly assumes the relation is an equivalence already</p>

#### [ Reid Barton (Jun 15 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128130797):
<p>But, say, <code>R 1</code> might be nontrivial, while <code>R 2</code> is empty, and then <code>λ (a b : Π i, α i), ∀ i, R i (a i) (b i)</code> is empty, so we haven't made any identifications in <code>\a 1 \x \a 2</code></p>

#### [ Reid Barton (Jun 15 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128130830):
<p>then we'd have a map <code>quot (R 1) \to \a 1</code>. Or is that okay?</p>

#### [ Mario Carneiro (Jun 15 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128130903):
<p>I see, yes that's bad</p>

#### [ Mario Carneiro (Jun 15 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128130919):
<p>So maybe just replace<code>quot</code> with <code>quotient</code> everywhere</p>

#### [ Mario Carneiro (Jun 15 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128130929):
<p>although then I have to show that the pi of equivalences is an equivalence</p>

#### [ Mario Carneiro (Jun 15 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128131542):
<p>Here's the noncomputable version:</p>
<div class="codehilite"><pre><span></span>instance pi_setoid {ι : Type*} {α : ι → Type*} [∀ i, setoid (α i)] : setoid (Π i, α i) :=
{ r := λ a b, ∀ i, a i ≈ b i,
  iseqv := ⟨
    λ a i, setoid.refl _,
    λ a b h i, setoid.symm (h _),
    λ a b c h₁ h₂ i, setoid.trans (h₁ _) (h₂ _)⟩ }

noncomputable def quotient.choice {ι : Type*} {α : ι → Type*} [S : ∀ i, setoid (α i)]
  (f : ∀ i, quotient (S i)) : @quotient (Π i, α i) (by apply_instance) :=
⟦λ i, (f i).out⟧

theorem quotient.choice_eq {ι : Type*} {α : ι → Type*} [∀ i, setoid (α i)]
  (f : ∀ i, α i) : quotient.choice (λ i, ⟦f i⟧) = ⟦f⟧ :=
quotient.sound $ λ i, quotient.mk_out _
</pre></div>

#### [ Mario Carneiro (Jun 15 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128136633):
<blockquote>
<p>Let G be a group and H a subgroup of finite index. Then, pick a set-theoretic section s:G/H-&gt;G where G/H is the right cosets. Then, the transfer homomorphism G^ab -&gt; H^ab is defined by sending [[g]] to prod[x in G/H] s(x) g s(xg)^-1.</p>
</blockquote>
<p>Shouldn't there be a [[]] in the definition there somewhere?</p>

#### [ Kenny Lau (Jun 15 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128136644):
<p>by sending [[g]] to [[prod[x in G/H] s(x) g s(xg)^-1]].</p>

#### [ Mario Carneiro (Jun 15 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128136655):
<p>Does <code>[[g h]] = [[g]][[h]]</code>?</p>

#### [ Kenny Lau (Jun 15 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128136663):
<p>yes</p>

#### [ Mario Carneiro (Jun 15 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128136679):
<p>Then don't the <code>s(x)</code> parts cancel?</p>

#### [ Kenny Lau (Jun 15 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128136684):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Mario Carneiro (Jun 15 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128136736):
<p><code>[[prod[x in G/H] s(x) g s(xg)^-1]] = (prod[x in G/H] [[s(x)]]) (prod[x in G/H] [[g]]) (prod[x in G/H] [[s(xg)]]^-1)</code></p>

#### [ Mario Carneiro (Jun 15 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128136747):
<p>and <code>prod[x in G/H] [[s(xg)]]^-1 = prod[x in G/H] [[s(x)]]^-1</code> by reindexing</p>

#### [ Kenny Lau (Jun 15 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128136748):
<p>oh you can't do that, g is not in H</p>

#### [ Kenny Lau (Jun 15 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128136762):
<p>s(x) g s(xg)^-1 is in H</p>

#### [ Mario Carneiro (Jun 15 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128136768):
<p>I know, but they should still be equal as members of G</p>

#### [ Kenny Lau (Jun 15 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128136779):
<p>no, because H^ab is H/[H,H]</p>

#### [ Mario Carneiro (Jun 15 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128137621):
<p>Okay, I think I have something close to a proof that decidable_eq of the coset relation is necessary. Suppose you know <code>fintype G/H</code>. Ignoring quotients for a moment, thinking "computationally", this is essentially a list of elements of G which chooses exactly one element of every coset (or, if you prefer, a bijection (not an equiv) from fin n to G/H). Now that looks like the section we want, but the problem is the computation of s(xg) that we need later. The function x |-&gt; xg is a permutation of G/H which corresponds to a permutation of the list s, but computationally it's not that easy since if we take our representative s(x) and multiply by g we get s(x)g, which is in the same coset as s(xg) but is not usually the same. So we need a way of searching our list s to find the value that is in the same coset as s(x)g, and there is no way to do this from the given data.</p>

#### [ Kenny Lau (Jun 15 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128141785):
<p>I see. Then I'll just come up with a section noncomputably then.</p>

#### [ Mario Carneiro (Jun 15 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128141854):
<p>Here's the computable version of that theorem:</p>
<div class="codehilite"><pre><span></span>def quotient.fin_choice_aux {ι : Type*} [decidable_eq ι]
  {α : ι → Type*} [S : ∀ i, setoid (α i)] :
  ∀ (l : list ι), (∀ i ∈ l, quotient (S i)) → @quotient (Π i ∈ l, α i) (by apply_instance)
| []     f := ⟦λ i, false.elim⟧
| (i::l) f := begin
  refine quotient.lift_on₂ (f i (list.mem_cons_self _ _))
    (quotient.fin_choice_aux l (λ j h, f j (list.mem_cons_of_mem _ h)))
    _ _,
  exact λ a l, ⟦λ j h,
    if e : j = i then by rw e; exact a else
    l _ (h.resolve_left e)⟧,
  refine λ a₁ l₁ a₂ l₂ h₁ h₂, quotient.sound (λ j h, _),
  by_cases e : j = i; simp [e],
  { subst j, exact h₁ },
  { exact h₂ _ _ }
end

theorem quotient.fin_choice_aux_eq {ι : Type*} [decidable_eq ι]
  {α : ι → Type*} [S : ∀ i, setoid (α i)] :
  ∀ (l : list ι) (f : ∀ i ∈ l, α i), quotient.fin_choice_aux l (λ i h, ⟦f i h⟧) = ⟦f⟧
| []     f := quotient.sound (λ i h, h.elim)
| (i::l) f := begin
  simp [quotient.fin_choice_aux, quotient.fin_choice_aux_eq l],
  refine quotient.sound (λ j h, _),
  by_cases e : j = i; simp [e],
  subst j, refl
end

def quotient.fin_choice {ι : Type*} [fintype ι] [decidable_eq ι]
  {α : ι → Type*} [S : ∀ i, setoid (α i)]
  (f : ∀ i, quotient (S i)) : @quotient (Π i, α i) (by apply_instance) :=
quotient.lift_on (@quotient.rec_on _ _ (λ l : multiset ι,
    @quotient (Π i ∈ l, α i) (by apply_instance))
    finset.univ.1
    (λ l, quotient.fin_choice_aux l (λ i _, f i))
    (λ a b h, begin
      have := λ a, quotient.fin_choice_aux_eq a (λ i h, quotient.out (f i)),
      simp [quotient.out_eq] at this,
      simp [this],
      let g := λ a:multiset ι, ⟦λ (i : ι) (h : i ∈ a), quotient.out (f i)⟧,
      refine eq_of_heq ((eq_rec_heq _ _).trans (_ : g a == g b)),
      congr&#39; 1, exact quotient.sound h,
    end))
  (λ f, ⟦λ i, f i (finset.mem_univ _)⟧)
  (λ a b h, quotient.sound $ λ i, h _ _)


theorem quotient.fin_choice_eq {ι : Type*} [fintype ι] [decidable_eq ι]
  {α : ι → Type*} [∀ i, setoid (α i)]
  (f : ∀ i, α i) : quotient.fin_choice (λ i, ⟦f i⟧) = ⟦f⟧ :=
begin
  let q, swap, change quotient.lift_on q _ _ = _,
  have : q = ⟦λ i h, f i⟧,
  { dsimp [q],
    exact quotient.induction_on
      (@finset.univ ι _).1 (λ l, quotient.fin_choice_aux_eq _ _) },
  simp [this], exact setoid.refl _
end
</pre></div>

#### [ Kenny Lau (Jun 15 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128141861):
<p>:o</p>

#### [ Kevin Buzzard (Jun 16 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Transfer%20homomorphism/near/128164386):
<p>Canceling s -- [[]] is being used for both the map G-&gt;Gab and H-&gt;Hab so they don't cancel. Spending the weekend in a field without much internet so don't expect too much from me until sun pm</p>


{% endraw %}
