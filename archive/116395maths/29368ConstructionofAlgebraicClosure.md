---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/29368ConstructionofAlgebraicClosure.html
---

## [maths](index.html)
### [Construction of Algebraic Closure](29368ConstructionofAlgebraicClosure.html)

#### [Kenny Lau (May 29 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264707):
I saw many constructions of the algebraic closure of a field **k** using direct limit, but I have a different construction in mind:
The set **k-bar** is { (f,n) in k[X] x N | f is irreducible and n < deg f }. The n represents the n-th root of the polynomial.
Addition and multiplicatoin can be defined using resultant.
Is this construction valid? Would this be a better construction?

#### [Johan Commelin (May 29 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264852):
Hmm, maybe I'm being silly. But how do you order the roots?

#### [Kenny Lau (May 29 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264858):
I don't

#### [Johan Commelin (May 29 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264862):
Ok, so how do you do addition and multiplication?

#### [Kenny Lau (May 29 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264874):
For f and g, I use resultant to construct h that contains all the roots

#### [Kenny Lau (May 29 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264876):
then just, you know, do the thing

#### [Kenny Lau (May 29 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264884):
if f has deg m and g has deg n, then h has deg mn

#### [Kenny Lau (May 29 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264885):
no this doesn't work

#### [Johan Commelin (May 29 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264932):
I mean, your approach looks very constructive. But we know that you need choice for k-bar

#### [Johan Commelin (May 29 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264948):
So that makes me suspicious

#### [Kenny Lau (May 29 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127264979):
do you need choice for the direct limit construction?

#### [Johan Commelin (May 29 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265144):
Yes, you want to use Zorn to pick a maximal element

#### [Johan Commelin (May 29 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265313):
Does this mean you are going to refuse the project that Kevin gave you?

#### [Kenny Lau (May 29 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265318):
I think the problem is when I add 1+sqrt(2) and -sqrt(2)

#### [Kenny Lau (May 29 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265321):
no, that doesn't

#### [Kenny Lau (May 29 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265337):
and how do you know about the project

#### [Johan Commelin (May 29 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265356):
Kevin mentioned somewhere that you were working on some algebraic stuff

#### [Johan Commelin (May 29 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265363):
for a project that he gave you

#### [Johan Commelin (May 29 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265431):
Anyway, I think it is very cool. I have been thinking about Galois theory. But I was daunted by defining the algebraic closure.

#### [Johan Commelin (May 29 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265438):
I haven't worked with Choice yet in Lean

#### [Kenny Lau (May 29 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265446):
nice

#### [Johan Commelin (May 29 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265451):
But we really need Galois theory

#### [Kenny Lau (May 29 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265454):
stop before you are corrupted by choice

#### [Kenny Lau (May 29 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265476):
```quote
I mean, your approach looks very constructive. But we know that you need choice for k-bar
```
we all know that you don't need choice for F_p-bar or Q-bar or R-bar

#### [Johan Commelin (May 29 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265478):
Yes, I also reject infinity (-;

#### [Kevin Buzzard (May 29 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265798):
Yes you can't do add this way Kenny

#### [Kevin Buzzard (May 29 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265799):
The problem is that what you are doing in your head, is this:

#### [Kevin Buzzard (May 29 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265841):
if you have have two polynomials f(X) and g(X), irreducible in k[X] say

#### [Kevin Buzzard (May 29 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265843):
then you are doing mathematics in the ring k[X]/(f) tensor_k k[X]/(g)

#### [Kevin Buzzard (May 29 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265847):
and unfortunately this is not in general a field

#### [Kevin Buzzard (May 29 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265880):
Consider the polynomials f(X)=X^3-2 and g(X)=(X+1)^3-2. Both are irredudible over Q

#### [Kevin Buzzard (May 29 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265886):
You order the roots of both of them

#### [Mario Carneiro (May 29 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265888):
If you do this construction, I would like to have a computable algebraic numbers construction from it

#### [Kevin Buzzard (May 29 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265897):
but who is to say that if a,b,c was the first order then a-1,b-1,c-1 was the second one

#### [Kenny Lau (May 29 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265942):
but we all know that Q-bar is computable

#### [Kevin Buzzard (May 29 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265948):
so who can possibly tell when (root 1 of f) - (root 1 of g) is 1 or not?

#### [Kevin Buzzard (May 29 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265965):
The problem is that whilst g is irreducible over Q

#### [Kevin Buzzard (May 29 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265970):
it is not irreducible over the larger field Q[X]/(f)

#### [Kevin Buzzard (May 29 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265983):
indeed, it factors into a linear and an irreducible quadric over this larger field

#### [Kevin Buzzard (May 29 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127265988):
so now all of a sudden the roots are not as indistinguishable as they used to be

#### [Assia Mahboubi (May 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274084):
Hi @**Kenny Lau** [here](https://github.com/math-comp/math-comp/blob/master/mathcomp/field/countalg.v) is a formalized construction of the algebraic closure of countable fields. It heavily relies on [this](https://github.com/math-comp/math-comp/blob/master/mathcomp/field/algebraics_fundamentals.v), the existence of an algebraically closed field with an   automorphism of order 2. [Here](https://github.com/math-comp/math-comp/blob/master/mathcomp/field/algC.v)  is an abstract construction of algebraic numbers. I can help deciphering the statements and proofs if you're interested. But several of these files have long headers describing what's done in them.

#### [Kenny Lau (May 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274120):
thanks

#### [Assia Mahboubi (May 29 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274182):
And all this is constructive. It only relies on the fact that there is choice operator on countable types with a decidable equality. This is provable in Coq without extra axioms, but using a subtle singleton elimination argument. I do not know if the same holds in Lean.

#### [Kenny Lau (May 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274220):
we don't have the axiom of unique choice in Lean, if that's what you mean

#### [Kenny Lau (May 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274231):
I suppose we can look at the preimage under the bijection from N and find the minimum element

#### [Assia Mahboubi (May 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274233):
No this is not what I mean, unique choice does not hold in Coq either.

#### [Kenny Lau (May 29 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274235):
then it should still be constructive in Lean

#### [Mario Carneiro (May 29 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274326):
There is a choice operator on countable types in lean

#### [Mario Carneiro (May 29 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274374):
`encodable.choose` in `data.encodable`

#### [Patrick Massot (May 29 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274391):
Noooo! Assia, please don't encourage Kenny in his constructive deviance

#### [Assia Mahboubi (May 29 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274403):
Ah thanks @**Mario Carneiro**, I was trying to dig into Lean to see if I could find it.

#### [Mario Carneiro (May 29 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274413):
The axiomatically basic one is `nat.find`

#### [Assia Mahboubi (May 29 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Construction%20of%20Algebraic%20Closure/near/127274688):
Hi again @**Patrick Massot**! Don't worry, I am just saying that for countable fields, classical proofs are constructive, in fact. I don't think that constructivism is the difficult issue here but I may well have forgotten how easy classical life is.

