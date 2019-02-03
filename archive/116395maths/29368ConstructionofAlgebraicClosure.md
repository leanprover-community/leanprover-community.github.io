---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/29368ConstructionofAlgebraicClosure.html
---

## Stream: [maths](index.html)
### Topic: [Construction of Algebraic Closure](29368ConstructionofAlgebraicClosure.html)

---


{% raw %}
#### [ Kenny Lau (May 29 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264707):
<p>I saw many constructions of the algebraic closure of a field <strong>k</strong> using direct limit, but I have a different construction in mind:<br>
The set <strong>k-bar</strong> is { (f,n) in k[X] x N | f is irreducible and n &lt; deg f }. The n represents the n-th root of the polynomial.<br>
Addition and multiplicatoin can be defined using resultant.<br>
Is this construction valid? Would this be a better construction?</p>

#### [ Johan Commelin (May 29 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264852):
<p>Hmm, maybe I'm being silly. But how do you order the roots?</p>

#### [ Kenny Lau (May 29 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264858):
<p>I don't</p>

#### [ Johan Commelin (May 29 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264862):
<p>Ok, so how do you do addition and multiplication?</p>

#### [ Kenny Lau (May 29 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264874):
<p>For f and g, I use resultant to construct h that contains all the roots</p>

#### [ Kenny Lau (May 29 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264876):
<p>then just, you know, do the thing</p>

#### [ Kenny Lau (May 29 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264884):
<p>if f has deg m and g has deg n, then h has deg mn</p>

#### [ Kenny Lau (May 29 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264885):
<p>no this doesn't work</p>

#### [ Johan Commelin (May 29 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264932):
<p>I mean, your approach looks very constructive. But we know that you need choice for k-bar</p>

#### [ Johan Commelin (May 29 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264948):
<p>So that makes me suspicious</p>

#### [ Kenny Lau (May 29 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264979):
<p>do you need choice for the direct limit construction?</p>

#### [ Johan Commelin (May 29 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265144):
<p>Yes, you want to use Zorn to pick a maximal element</p>

#### [ Johan Commelin (May 29 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265313):
<p>Does this mean you are going to refuse the project that Kevin gave you?</p>

#### [ Kenny Lau (May 29 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265318):
<p>I think the problem is when I add 1+sqrt(2) and -sqrt(2)</p>

#### [ Kenny Lau (May 29 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265321):
<p>no, that doesn't</p>

#### [ Kenny Lau (May 29 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265337):
<p>and how do you know about the project</p>

#### [ Johan Commelin (May 29 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265356):
<p>Kevin mentioned somewhere that you were working on some algebraic stuff</p>

#### [ Johan Commelin (May 29 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265363):
<p>for a project that he gave you</p>

#### [ Johan Commelin (May 29 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265431):
<p>Anyway, I think it is very cool. I have been thinking about Galois theory. But I was daunted by defining the algebraic closure.</p>

#### [ Johan Commelin (May 29 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265438):
<p>I haven't worked with Choice yet in Lean</p>

#### [ Kenny Lau (May 29 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265446):
<p>nice</p>

#### [ Johan Commelin (May 29 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265451):
<p>But we really need Galois theory</p>

#### [ Kenny Lau (May 29 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265454):
<p>stop before you are corrupted by choice</p>

#### [ Kenny Lau (May 29 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265476):
<blockquote>
<p>I mean, your approach looks very constructive. But we know that you need choice for k-bar</p>
</blockquote>
<p>we all know that you don't need choice for F_p-bar or Q-bar or R-bar</p>

#### [ Johan Commelin (May 29 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265478):
<p>Yes, I also reject infinity (-;</p>

#### [ Kevin Buzzard (May 29 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265798):
<p>Yes you can't do add this way Kenny</p>

#### [ Kevin Buzzard (May 29 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265799):
<p>The problem is that what you are doing in your head, is this:</p>

#### [ Kevin Buzzard (May 29 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265841):
<p>if you have have two polynomials f(X) and g(X), irreducible in k[X] say</p>

#### [ Kevin Buzzard (May 29 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265843):
<p>then you are doing mathematics in the ring k[X]/(f) tensor_k k[X]/(g)</p>

#### [ Kevin Buzzard (May 29 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265847):
<p>and unfortunately this is not in general a field</p>

#### [ Kevin Buzzard (May 29 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265880):
<p>Consider the polynomials f(X)=X^3-2 and g(X)=(X+1)^3-2. Both are irredudible over Q</p>

#### [ Kevin Buzzard (May 29 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265886):
<p>You order the roots of both of them</p>

#### [ Mario Carneiro (May 29 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265888):
<p>If you do this construction, I would like to have a computable algebraic numbers construction from it</p>

#### [ Kevin Buzzard (May 29 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265897):
<p>but who is to say that if a,b,c was the first order then a-1,b-1,c-1 was the second one</p>

#### [ Kenny Lau (May 29 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265942):
<p>but we all know that Q-bar is computable</p>

#### [ Kevin Buzzard (May 29 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265948):
<p>so who can possibly tell when (root 1 of f) - (root 1 of g) is 1 or not?</p>

#### [ Kevin Buzzard (May 29 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265965):
<p>The problem is that whilst g is irreducible over Q</p>

#### [ Kevin Buzzard (May 29 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265970):
<p>it is not irreducible over the larger field Q[X]/(f)</p>

#### [ Kevin Buzzard (May 29 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265983):
<p>indeed, it factors into a linear and an irreducible quadric over this larger field</p>

#### [ Kevin Buzzard (May 29 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265988):
<p>so now all of a sudden the roots are not as indistinguishable as they used to be</p>

#### [ Assia Mahboubi (May 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274084):
<p>Hi <span class="user-mention" data-user-id="110064">@Kenny Lau</span> <a href="https://github.com/math-comp/math-comp/blob/master/mathcomp/field/countalg.v" target="_blank" title="https://github.com/math-comp/math-comp/blob/master/mathcomp/field/countalg.v">here</a> is a formalized construction of the algebraic closure of countable fields. It heavily relies on <a href="https://github.com/math-comp/math-comp/blob/master/mathcomp/field/algebraics_fundamentals.v" target="_blank" title="https://github.com/math-comp/math-comp/blob/master/mathcomp/field/algebraics_fundamentals.v">this</a>, the existence of an algebraically closed field with an   automorphism of order 2. <a href="https://github.com/math-comp/math-comp/blob/master/mathcomp/field/algC.v" target="_blank" title="https://github.com/math-comp/math-comp/blob/master/mathcomp/field/algC.v">Here</a>  is an abstract construction of algebraic numbers. I can help deciphering the statements and proofs if you're interested. But several of these files have long headers describing what's done in them.</p>

#### [ Kenny Lau (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274120):
<p>thanks</p>

#### [ Assia Mahboubi (May 29 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274182):
<p>And all this is constructive. It only relies on the fact that there is choice operator on countable types with a decidable equality. This is provable in Coq without extra axioms, but using a subtle singleton elimination argument. I do not know if the same holds in Lean.</p>

#### [ Kenny Lau (May 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274220):
<p>we don't have the axiom of unique choice in Lean, if that's what you mean</p>

#### [ Kenny Lau (May 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274231):
<p>I suppose we can look at the preimage under the bijection from N and find the minimum element</p>

#### [ Assia Mahboubi (May 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274233):
<p>No this is not what I mean, unique choice does not hold in Coq either.</p>

#### [ Kenny Lau (May 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274235):
<p>then it should still be constructive in Lean</p>

#### [ Mario Carneiro (May 29 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274326):
<p>There is a choice operator on countable types in lean</p>

#### [ Mario Carneiro (May 29 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274374):
<p><code>encodable.choose</code> in <code>data.encodable</code></p>

#### [ Patrick Massot (May 29 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274391):
<p>Noooo! Assia, please don't encourage Kenny in his constructive deviance</p>

#### [ Assia Mahboubi (May 29 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274403):
<p>Ah thanks <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, I was trying to dig into Lean to see if I could find it.</p>

#### [ Mario Carneiro (May 29 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274413):
<p>The axiomatically basic one is <code>nat.find</code></p>

#### [ Assia Mahboubi (May 29 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274688):
<p>Hi again <span class="user-mention" data-user-id="110031">@Patrick Massot</span>! Don't worry, I am just saying that for countable fields, classical proofs are constructive, in fact. I don't think that constructivism is the difficult issue here but I may well have forgotten how easy classical life is.</p>


{% endraw %}
