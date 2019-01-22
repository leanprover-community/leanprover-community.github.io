---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/00370multiplicativefinsupp.html
---

## [maths](index.html)
### [multiplicative finsupp](00370multiplicativefinsupp.html)

#### [Johan Commelin (Jan 22 2019 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156594377):
I'm trying to stress test my adjunctions code. A natural example is `mv_polynomial` being left adjoint to `forget`. This adjunction is actually a composite of two adjunctions: the free monoid construction, and monoid rings. While trying to write these things down, I got stuck in the whole additive-multiplicative business again. So, let's forget about this motivation for now.

Has anyone ever attempted to turn `data/finsupp` into a file that supports both multiplicative and additive coefficients? Are there any expected problems? Or is this just something that has to be done by someone?

#### [Mario Carneiro (Jan 22 2019 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156594586):
use `multiplicative A` for the coefficients

#### [Johan Commelin (Jan 22 2019 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156595162):
I know I can do that. But it becomes pretty messy. And it feels to me like it defeats the purpose of the `add`/`mul` distinction.

#### [Johan Commelin (Jan 22 2019 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156595211):
All of a sudden I'm having proofs like
```lean
{ map_one := map_domain_zero, map_mul := λ _ _, map_domain_add }
```
which creates cognitive dissonance.

#### [Johan Commelin (Jan 22 2019 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156595229):
I think that if we want to use `multiplicative` (or `additive`, I don't care) we should just use it everywhere.

#### [Mario Carneiro (Jan 22 2019 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156595240):
well we did, and now you want the other one

#### [Johan Commelin (Jan 22 2019 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156595315):
No, I mean everywhere in mathlib.

#### [Mario Carneiro (Jan 22 2019 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156595320):
I have argued since day 1 that it would be much nicer to use add for group theory and forget about mul except in specialized circumstances, but mathematicians get hissy about non-commutative addition

#### [Kevin Buzzard (Jan 22 2019 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156596112):
Mathematicians definitely want both.

#### [Kevin Buzzard (Jan 22 2019 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156596116):
Non-commutative addition is the least of our worries here.

#### [Mario Carneiro (Jan 22 2019 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156596745):
If I said "all groups must use addition", what exactly would be the downside? AFAICT there are very few places where you actually need multiplicative groups besides "it looks better"

#### [Mario Carneiro (Jan 22 2019 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156596829):
by contrast it is quite common to use the group structure of additive groups embedded in rings and other things

#### [Mario Carneiro (Jan 22 2019 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156596867):
Note that a ring does not have a multiplicative group; multiplication is not a group operation. Instead there is an associated structure, the "units group", that is a group

#### [Kevin Buzzard (Jan 22 2019 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156597285):
If you said "all groups must use addition" then mathematicians would consistently be utterly confused about why the unit group of a ring had group law addition. I guess there's nothing stopping this convention -- equally, there is nothing stopping the convention that you use a little heart symbol. It's just that mathematicians would then find this stuff even harder to understand. Notation conveys meaning and notation which mathematicians have fixed on is *very* hard to change. I personally loathe the standard symbol for quadratic residues / non-residues, because it's a fraction in a bracket -- but there's very little I can do about this.

#### [Johan Commelin (Jan 22 2019 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156597691):
We have proof irrelevance. Why can't we have notation irrelevance. (I know that the current implementation via type classes makes it hard. But that just means we need a better solution.)

#### [Johan Commelin (Jan 22 2019 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156599282):
@**Mario Carneiro** I can see why you would want all groups to be additive (although adding invertible matrices feels very wrong). But with monoids you wouldn't have a clean solution, right? Every ring gives you two monoids, one for addition, the other for multiplication. I'm interested in knowing what you would do there.

#### [Kevin Buzzard (Jan 22 2019 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156615639):
I thought about this more. A mathematician has a fixed notation for a ring, so you can't change it -- it uses `+` and `*`. And a ring is a group under `+` and the units of a ring are a group under `*`, and these come up again and again, so you can't change these either :-/ And the point is that in mathematics we are capable of rewriting these group axioms from `+` to `*` seamlessly because *it is true that it works fine*, yet Lean struggles to do it seamlessly. There clearly is some sort of a problem here, but I don't think mathematicians will accept removal of `*` because it goes the wrong way. For us, the units of $$R$$ are a subset of $$R$$. This is not how it works in DTT and somehow we need a better solution :-/

#### [Johan Commelin (Jan 22 2019 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156615711):
How about `End(V)`? We'll use `\circ` instead of `*`, without blinking an eye.

#### [Reid Barton (Jan 22 2019 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156615835):
A unit is just an automorphism of a ring as a module over itself, what's the problem?

#### [Reid Barton (Jan 22 2019 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156615884):
(https://stackoverflow.com/questions/3870088/a-monad-is-just-a-monoid-in-the-category-of-endofunctors-whats-the-problem)

