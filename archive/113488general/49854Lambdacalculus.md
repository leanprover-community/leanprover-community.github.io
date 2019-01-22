---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49854Lambdacalculus.html
---

## [general](index.html)
### [Lambda calculus](49854Lambdacalculus.html)

#### [Alexander Bentkamp (Dec 17 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152020148):
Hello,
Does anyone know of a formalization of the lambda calculus in Lean?
In particular termination of beta/eta reduction?

#### [Patrick Massot (Dec 17 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152020719):
I would have a look at https://github.com/leanprover/mathlib/tree/master/computability (but maybe this is something else)

#### [Patrick Massot (Dec 17 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152020807):
And, if it doesn't exist, maybe having a look at https://github.com/leanprover/mathlib/blob/5613d2ecc92ce8fae9555745bd94756dec61a323/group_theory/free_group.lean#L127 and https://github.com/leanprover/mathlib/blob/57194fa57e76721a517d6969ee88a6007f0722b3/logic/relation.lean#L288 could be a good idea

#### [Mario Carneiro (Dec 17 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152021502):
I don't think lambda calculus has been done, although there are several projects in the same space

#### [Mario Carneiro (Dec 17 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152021571):
I assume you are talking about simply typed lambda calculus, since of course the regular kind doesn't terminate

#### [Mario Carneiro (Dec 17 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152021611):
I believe Jeremy has a formalization of lambda calculus, although he intended it for different purposes and I don't think he proved this property

#### [Mario Carneiro (Dec 17 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152021724):
aha, here it is: https://github.com/avigad/embed/blob/master/src/exp.lean

#### [Mario Carneiro (Dec 17 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152021734):
it's not much more than the definition

#### [Mario Carneiro (Dec 17 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152021811):
I guess he never defined typechecking for lambda terms, since he was going for FOL

#### [Alexander Bentkamp (Dec 17 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152023395):
Ok, thanks for the pointers. I will think about whether I'd like to work on this then. Actually, I'd like to formalize a unification procedure for lambda-terms, but I will need a formalization of the lambda-calculus for that first :-)

#### [Kenny Lau (Dec 17 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152023686):
I might be missing something obvious here

#### [Kenny Lau (Dec 17 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152023688):
but what happened to the Y-combinator?

#### [Kenny Lau (Dec 17 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152023697):
oh, that's what "simply typed" rules out isn't it

#### [Alexander Bentkamp (Dec 17 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152023793):
Yes, I wasn't very precise. I meant simply typed lambda calculus.

#### [Wojciech Nawrocki (Dec 19 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152218893):
Hey, I'm actually working on this right now! Is there any particular formulation that you want to use? I'm trying to figure out inherently typed terms at the moment, but I have a formulation in raw terms with a typechecking procedure and a proof of progress, basically following "Software Foundations".

#### [Alexander Bentkamp (Dec 20 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152262213):
Oh, that's great! As I said, I actually would like to formalize a unification procedure for lambda-terms. So if I could build on your library once it's finished, that would be perfect. I find it hard to predict which formulation would be more suitable for this, but I guess it doesn't matter too much.

#### [Wojciech Nawrocki (Dec 20 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152263621):
It's not pretty code and definitely not suitable for a library, but I can upload it somewhere like git when I have a bit more time if that helps your project :)

#### [Wojciech Nawrocki (Dec 20 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152263723):
By the way, you mean unification of the entire term assuming some holes on one (or both?) sides, not just types, right?

#### [Alexander Bentkamp (Dec 20 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152271412):
Yes, with holes on both sides, but the holes are realized as free variables. In addition to that, there are also constant symbols. So for example, one could ask for unifiers of `f (X a) b` and `f c (Y d)`, where uppercase letters are variables and lowercase letters are constants. A unifier would be `{X ↦ λZ. c; Y ↦ λZ. b}`. The procedure is described here: https://www.sciencedirect.com/science/article/pii/0304397576900219

#### [Alexander Bentkamp (Dec 20 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152272457):
So it sounds like you don't plan / don't have time to improve your code such that it would be usable as a library?  If I decide to formalize lambda calculus myself, I will ask you again for what you've done. But currently, I tend to using Isabelle/HOL instead for this project (Oh, oh, high treason in this chat I suppose).

#### [Wojciech Nawrocki (Dec 20 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152275053):
Oh, I do hope to make it fairly readable, just not the very partial raw-term formulation, which is what I have currently, but rather the inherently-typed one which I only started on. That said, I'm using quantified type theory to support linear typing, which is more general than simply-typed lambda, but can be instantiated (I think..) to simply-typed lambda.

#### [Josh Pollock (Dec 20 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152293681):
We actually did some stlc in lean in the University of Washington's graduate PL class last fall: https://courses.cs.washington.edu/courses/cse505/17au/lec11/lean/stlc.lean

#### [Alexander Bentkamp (Dec 21 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/152324240):
Thanks! I'll have a closer look next year. Happy holidays :-)

#### [Patrick Thomas (Jan 02 2019 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/154197485):
I just started learning lambda calculus. If you don't mind explaining, I was wondering why the condition ```x2 \notin FV (e1) \/ x1 \notin FV (e)``` is not a part of the definition for ```lam_diff``` in ```is_subst```?

#### [Mario Carneiro (Jan 02 2019 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/154197511):
are you referring to a particular formalization?

#### [Patrick Thomas (Jan 02 2019 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/154197586):
Sorry, yes. The one that Josh Pollock posted a link to earlier in the thread.

#### [Mario Carneiro (Jan 02 2019 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/154197839):
I think you are right. There are variable capturing substitutions that are admitted by `is_subst`

#### [Patrick Thomas (Jan 02 2019 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/154198088):
If that is the case, would adding that condition be the simplest fix?

#### [Patrick Thomas (Jan 02 2019 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/154201289):
If I try to add connectives like ```∧``` and ```∨``` to the inductive definition, I seem to get an error of "...contains variables that are not parameters". Are these permitted in inductive definitions?

#### [Patrick Thomas (Jan 02 2019 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/154202553):
Would this work?

```lean
inductive is_subst : expr → string → expr → expr → Prop
-- (λ y . P)[ x := N ] = (λ y . P [ x := N ]) if x ≠ y and y ∉ FV (N) or x ∉ FV (P)
| lam_diff : ∀ (y : string) (P : expr) (x : string) (N : expr) (e : expr),
	x ≠ y
	→ ((¬ is_free N y) ∨ (¬ is_free P x))
	→ is_subst P x N e
	→ is_subst (expr.lam y P) x N (expr.lam y e)
```

#### [Kenny Lau (Jan 02 2019 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/154203012):
```lean
meta constant is_free : expr → string → Prop

meta inductive is_subst : expr → string → expr → expr → Prop
-- (λ y . P)[ x := N ] = (λ y . P [ x := N ]) if x ≠ y and y ∉ FV (N) or x ∉ FV (P)
| lam_diff : ∀ (y : string) (P : expr) (x : string) (N : expr) (e : expr),
    x ≠ y
    → ((¬ is_free N y) ∨ (¬ is_free P x))
    → is_subst P x N e
    → is_subst (expr.lam y sorry P sorry) x N (expr.lam y sorry e sorry)
```

#### [Kenny Lau (Jan 02 2019 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/154203014):
this works for me verbatim

#### [Patrick Thomas (Jan 02 2019 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/154203290):
Thank you. Do you think this would be a good fix for the definition?

#### [Kenny Lau (Jan 02 2019 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/154203316):
no because it has `sorry`

#### [Patrick Thomas (Jan 02 2019 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/154203407):
I'm sorry, I didn't mean verbatim, but if the definition was amended in this manner.

#### [Kenny Lau (Jan 02 2019 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/154203425):
my point is that I didn't change the part you complained about

#### [Kenny Lau (Jan 02 2019 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/154203436):
i.e. your diagnosis is not very accurate

#### [Patrick Thomas (Jan 02 2019 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/154203689):
The diagnosis about the error message or about the definition in the link that Josh posted? My post may have been confusing. I don't get error messages for the code I posted, it was changed to avoid them. I was asking if it worked to fix the definition that Josh posted.

#### [Kenny Lau (Jan 02 2019 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/154203786):
oh... context...

#### [Patrick Thomas (Jan 02 2019 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lambda calculus/near/154203800):
Sorry about that.

