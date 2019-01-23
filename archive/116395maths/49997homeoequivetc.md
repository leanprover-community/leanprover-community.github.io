---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/49997homeoequivetc.html
---

## Stream: [maths](index.html)
### Topic: [homeo equiv etc.](49997homeoequivetc.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 03 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124593811):
A more specific version of https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/structure.20vs.20class/near/124574243 (it may be easier to understand my problem by looking at code) is https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/support.lean#L188 where I'm clearly very stupidly trying to Lean some trivial lemma. I'm completely tangled in coercions and type classes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 03 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124593836):
I need two version of `supp` because I don't know how to have only one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 03 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124593899):
Then we have a classical `rw` failure on line 193 (always the same thing, `rw` itself doesn't do some kind of elaboration or reduction that is needed, and I still can't quite point out what)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 03 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124593923):
Then I  would like line 196 to be unnecessary (with the ugly ` (g.to_equiv).inv_fun` never appearing)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 03 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124593970):
And finally the computation which should be easy (but still the core of the proof) and cannot do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 03 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124593994):
I'd like to know whether the full setup is broken from the beginning or I only need a couple a carefully crafted simp lemmas to hide this mess (and prove stuff).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 03 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124594355):
cons_inj tells me about the lists being equal. Oops wrong topic.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688060):
I can see this topic has not much success. Maybe the context is too complicated because of topology. But I really think this will come up in other places. The question is: how to do group theory with groups of transformations? As long as you don't need to use the inverse of a transformation, you can easily  functions and composition of function. But what about inverses? Say I'm working with permutations of a type (not necessarily encoded as `perm` in current mathlib). I define the support of a permutation f as the complement supp f of the fixed point set (no topology here). I want to prove supp gfg⁻¹ = g(supp f). And ideally I would really like f, g and g⁻¹ to live in a type endowed with a group structure, because I have other group theoretic stuff to do. What encoding should I use? How to then talk about the image of a subset as in g(supp f)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688263):
I got as far as cutting and pasting a 230 line file and then realising I didn't have the imports

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688289):
You define `suppp f` to be `supp f`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688345):
If you want to directly play with code it's much faster to git clone

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688349):
Yes, that definition is part of the problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688354):
I couldn't avoid it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688432):
It's part of coercion/extension hell

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688448):
`supp` is defined on functions from `X` to `X`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688450):
homeos have coercions to functions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688494):
but it's not enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688499):
try to replace `suppp` by `supp` in the statement following that def and it won't type check

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688514):
But it's probably easier to solve the problem as I described it today than to add the topology layer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688561):
It's just too hard to make it work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688568):
I have mathlib not compiling.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688569):
make what work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688572):
I just pushed a version compatible with latest Lean nightly and mathlib head

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688579):
(only handling a renamed lemma)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688725):
Now I have errors in commutators.lean and groups.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688738):
those are old stuff irrelevant here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688742):
they are not updated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688745):
(this repo is my garbage repo, I'm sorry)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688748):
Everything imported in `support.lean` is ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688757):
OK it now compiles. What's the question?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688762):
Not that I'm likely to be able to answer it...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688811):
How do you sort out the mess with `supp` vs `suppp`, `fundamental` vs `fundamental''`, how to remove the sorries in the proof of `supp_conj`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 05 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688881):
```lean
open equiv
variables {α : Type*}

lemma mul_apply (a b : perm α) (x : α) : (a * b) x = (a (b x)) := rfl

@[simp] lemma one_apply (x : α) : (1 : perm α) x = x := rfl

def support (a : perm α) : set α := {x : α | a x ≠ x}

example (f g : perm α) : support (g * f * g⁻¹) = set.image g (support f) :=
set.ext $ λ y, ⟨λ h : _ ≠ _, ⟨g⁻¹ y, λ h₁, by
  rw [mul_apply, mul_apply, h₁, ← mul_apply, mul_inv_self] at h;
  exact h rfl,
show (g * g⁻¹) y = y,by rw mul_inv_self; refl⟩, 
λ ⟨x, (hx : _ ≠ _ ∧ _)⟩, show _ ≠ _, from
begin 
  rw [mul_apply, ← hx.2, ← mul_apply, ← mul_apply, mul_assoc, inv_mul_self, mul_one, mul_apply], 
  assume h,
  rw (equiv.bijective g).1 h at hx,
  exact hx.1 rfl
end⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 05 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124688971):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 05 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689034):
I proved a bit of stuff about permutations a few months ago.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689045):
Thank you very much. Now I need to rewrite it in full tactic mode to see how it could help

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689055):
The issue is that you are using coe everywhere?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689076):
What do you mean using coe everywhere?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689123):
I need homeomorphisms to be able to act as functions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689124):
So yes, they coerce to functions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689126):
Is the reason the rw doesn't work on line 193 that you are pushing type class inference too hard?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689186):
I have no idea

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689188):
Clearly there is something I'm doing wrong

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689194):
I only want to learn how to do it right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689259):
```
ambiguous overload, possible interpretations
  right_inverse
  function.right_inverse 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689274):
where do you see that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689278):
when I write `#check right_inverse`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689281):
I don't know how to check types of objects in the middle of Lean code.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689282):
@**Chris Hughes** don't you have a version of your proof before obfuscation?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689287):
Is there an easy way to do that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689288):
This is something I wonder all the time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689291):
it seems the answer is no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689294):
You'd wonder it more if you were reading someone else's code...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689413):
So what is ` (g.to_equiv).to_fun`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 05 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689414):
The reason this topic didn't get much discussion is because you basically said "there is something wrong, check out my code base and find the error"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689418):
he said lots of things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689420):
maybe there were lots of errors :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689421):
Could you at least post the error message?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689430):
(s)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689431):
There is no error message. I can't prove stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689432):
Because I'm clearly going against Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689436):
Are you being anti-idiomatic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689437):
Not writing idiomatic Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689479):
exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 05 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689487):
what? I am not in a position to see what you are talking about unless you say it here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689505):
If you want to get to the bottom of the reason rewrite fails on line 193 you should write a MWE. But I know this isn't your real question.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 05 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689522):
```quote
@**Chris Hughes** don't you have a version of your proof before obfuscation?
```
That's how I wrote it first time. I shouldn't have opened the `perm` namespace, so if it didn't work that's probably why.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689526):
@**Mario Carneiro** Is there a way of checking the type of a term in the middle of a tactic proof?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689530):
I tried to describe my problems in https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/structure.20vs.20class/near/124574243 without code, and then I posted link to my actual code. Then I tried to describe a simplified problem. I don't what I could do better to ask for help

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689571):
i.e. I can't check it outside the begin/end block because the term is only constructed within the block

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689572):
I'm honestly asking

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689582):
So what is ` (g.to_equiv).to_fun`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689588):
It's the function underlying the homeomorphism g

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689592):
for `g : homeo X X`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689595):
But it goes through two conversions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689601):
First to `equiv X X` and then to `X -> X`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689602):
When you write `g '' ...`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689604):
what do you think happens there?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689607):
That's mathlib notation for image of a subset

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689647):
Lean does figure out the coercions here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689649):
`set.image` so it takes a function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689653):
and which function does it take?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689678):
Is there some coe directly from homeo to the function?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689681):
`(g.to_equiv).to_fun`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689684):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689685):
That's what it uses?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689691):
`instance : has_coe_to_fun (homeo α β) := ⟨_, λ f, f.to_fun⟩`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689695):
is defined in `homeos.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689723):
It's indeed the same as `(g.to_equiv).to_fun`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689742):
This is a funny error message then:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689744):
```
rewrite tactic failed, did not find instance of the pattern in the target expression
  (g.to_equiv).to_fun '' {a : X | (λ (x : X), f x ≠ x) a}
state:
X : Type,
_inst_3 : topological_space X,
f g : homeo X X
⊢ {x : X | conj g f x ≠ x} = g '' {x : X | f x ≠ x} 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689756):
Is it definitionally the same?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 05 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689771):
rw doesn't do definitionally equal things.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689776):
oh yeah

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689779):
that's the second time I've forgotten that this week

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689785):
```lean
variable (g: homeo X X)
example : (g : X → X) = g.to_equiv.to_fun := rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689829):
Chris points out the problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689831):
Yes, I understand this is the problem with the rewrite

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689833):
definitionally equivalent is not enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689838):
But I'd like to know the proper way of either not having this problem or workaround it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689850):
without doing this `swap, exact ...` thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 05 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689854):
Never use `( g.to_equiv).to_fun`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689863):
I don't write this myself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 05 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689868):
I usually use `show` otherwise.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689872):
it only appears in goals and error messages

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689928):
What is this `λ h : _ ≠ _,` dark magic?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689929):
I had problems with coercions when I was doing schemes so I just stopped using them completely

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689930):
and wrote everything out in full

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689933):
How do you do it in tactic mode?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689935):
show works in tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689952):
Kevin, how would you do group theory with permutations of a Type without coercions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689958):
` show _ ≠ _ ` :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124689962):
You both need elements of the group to act on points and to have inverses

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690007):
Re: `_ ≠ _` he does this in place of `intro`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690009):
I'm just saying that you just write the coercions explicitly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690013):
That was what I did when I got sick of getting type class inference to work. I just wrote down everything myself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690085):
There must be a better way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690100):
In real world you would never need to distinguish the element of a group of transformation from themselves like this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690118):
the real world doesn't use dependent type theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690122):
it uses one piece of notation to mean more than one thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690129):
and we're so used to that, that this world can be kind of annoying sometimes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690167):
with their silly pedantic fussing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690176):
```
show {x : X | conj g f x ≠ x} = g.to_equiv.to_fun '' {x : X | f x ≠ x},
rw aux_1 g.right_inv,
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690178):
works for 193 ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690265):
I don't understand what `show` does here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690267):
Usually I need to supply a proof after `show`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690273):
it rewrites the goal into a definitionally equivalent form

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690277):
If the goal is X, then `show X,` does nothing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690280):
if the goal is definitionally equal to X, it changes the goal to X

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690287):
I can see it's doing that here. But what's the link with `show` I usually use?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690291):
which I guess is in term mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690293):
I don't know, this is the only show I use

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690294):
tactic mode is the bomb

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690370):
I use `show` in arguments to `rw` and `simp` for easy stuff I don't want to state and name using `have` beforehand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690467):
Line 190: `lemma  supp_conj (f g : homeo X X) : supp (conj g f : homeo X X) = g '' supp f :=` works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690530):
i.e. I removed `suppp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690543):
Very interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690545):
You are using `f` and `g` to mean two different things, and it guessed you wanted the map not the homeo here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690553):
the second suppp could just be removed, but the first one had to be persuaded

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690561):
Probably because `perm X` is also a group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690627):
and Lean doesn't know the group structure on `homeo X X` is induced as a subgroup of `perm X`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690659):
```quote
Then I  would like line 196 to be unnecessary (with the ugly ` (g.to_equiv).inv_fun` never appearing)
```
I don't understand this one. Is there another name for `g.to_equiv.inv_fun`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690712):
It's `g⁻¹`!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690856):
You can put `show {x : X | conj g f x ≠ x} = {b : X | f (g⁻¹ b) ≠ g⁻¹ b}` on line 196 if you like...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690867):
but you are complaining about the congr?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690884):
You want to prove two sets are equal and you don't want to use congr then funext?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124690933):
No I don't complain about congr and funext

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691006):
I don't complain at all actually, I try to learn

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691011):
I mean I complain that I'm not yet learned

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691014):
but I don't complain to anybody but me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691037):
I really don't understand Chris's proof at all

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691080):
I can't translate it into tactic mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691084):
Hence I cannot understand it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691093):
I have a really hard time imagining people actually thinking like this (without first writing the tactic proof and then obfuscate it in term mode)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691107):
I do believe you Chris, but my imagination is failing me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691169):
Your comments before the computation seem a bit superficial to me, in the sense that I would not care about any of them myself if they came up in my Lean work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691173):
But the computation is a more serious matter.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691188):
The computation is the actual proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691198):
everything before the computation is distraction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691262):
oh wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691271):
the computation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691277):
you write Prop = Prop?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691280):
There's no other way?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691283):
yes I write Prop = Prop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691287):
Maybe iff would be better with props

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691305):
That's because we see sets as map from X to  Prop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691316):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691372):
So the goal is really Prop = Prop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691379):
eew

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691384):
because we use funext to get rid of X here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691387):
Ok so your question really is something else

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691394):
But of course on paper I would write iff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691400):
You want to show `{x | p x} = {x | q x}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691406):
x is in this set iff .. iff .. iff ... done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691409):
I don't think you should use congr and then funext

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691420):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691423):
iff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691429):
Remember `{x | p x}` is only syntactic sugar for `p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691433):
sure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691441):
but there are lemmas like sets X and Y are equal iff X subseteq Y and Y subseteq X

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691480):
or whatever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 05 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691493):
`set.ext` is what you're talking about

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691494):
Sure, but here I can prove (on paper) direct equality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691503):
But you can't prove any of your intermediate steps!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691510):
So surely this is an indication that trying to prove p x = q x is a bad idea

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691585):
I would use set.ext instead of congr, funext

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691590):
and then try the calc with iff's

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691592):
indeed `apply set.ext` transforms the goal to iff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691606):
But my sorry where there because I couldn't use `rw`, not because I was proving `p x = q x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691686):
So what happens if you use set.ext and then try to push the calc through? I can't pass the `rw show  ∀ b, (g.to_equiv).inv_fun b = g⁻¹ b, from  λ b, rfl,` line

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691689):
because I don't really know what's going on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691752):
I don't understand what you don't know

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691755):
I have never seen congr_n in my life

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691758):
I don't know what all this rw show business is all about

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691762):
how is that different to just show

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691771):
can you just write it for me?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691786):
`congr_n 1` is like `congr` but stops after one step instead of recursing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691837):
how do you get from not X iff not Y to X iff Y?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691841):
if the goal is `f (a + b) = f (c + d)` and you `congr_n 1`, the new goal will be `a+b = c+d`. With `congr` it would become two random goals  like `a=c` and `b = d`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691847):
In this case `f` is `not`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 05 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691922):
By the way, I don't know how to get rid of these `not` once I go to iff instead of =

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691924):
not_iff_not.2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691942):
but there's a catch...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691945):
` ⊢ decidable (f (g⁻¹ x) = g⁻¹ x) `

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691946):
so I hope you are only interested in decidable topological spaces...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691947):
;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 05 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691985):
It's funny, as you saw with Adam, most people with a cs background start out in term mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 05 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124691993):
most people with a maths background think lambda is a real number

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 05 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692004):
I think it's simply familiarity with functional programming concepts

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 05 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692026):
Once you spend enough time looking at term mode statements they really do become more understandable 🙂

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692030):
I just found it using `find`!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692079):
`#find (¬ _ ↔ ¬ _) ↔ (_ ↔ _)` does work!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692081):
:tada: @**Sebastian Ullrich**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692096):
I found it by guessing what it was called ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692100):
Now what is this `decidable` crap? I have `noncomputable theory
local attribute [instance] classical.prop_decidable` on top of my file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692101):
Even the iff's need some work. I'm beginning to think you were better off with =. but I have to go now, childcare calls

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692146):
Why isn't it enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692156):
I need to sleep actually, I have a train to catch at an insane time tomorrow to go and give a talk about fuzzy maths in Köln

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692190):
and why this `decidable` stuff didn't come up in my `=` instead of iff stuff?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692239):
Anyway, thank you very much for your help, and thank Chris to

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692343):
I have enough food for thought on the train

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692361):
Except that I would like to understand how to tell Lean I really don't care about the `decidable` metaphysics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124692389):
@**Mario Carneiro** is there a global command to say everything should be assumed to have decidable equality?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124693410):
Is your problem simply that g is not an element of perm X? What happens if you define fp to be the permutation underlying f and gp for g, then use lemmas about groups acting on sets?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124693620):
All those iff statements are going to follow from standard lemmas about groups acting on sets. I have no idea if they're there already but that is surely the way to finish the job. Groups acting on sets should be in mathlib (I don't know if it's there already) and then all the lemmas should be proved in the same file and then you just apply them and you're home

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 06 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124702399):
> is there a global command to say everything should be assumed to have decidable equality? 

`local attribute [instance] classical.prop_decidable` should do that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124703691):
Hum. It turns out I can indeed use `apply_instance` in both cases. This is the first time I need this tactic in a context where I'm not using `example` to check whether an instance is working

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124703700):
Do you understand why ` apply not_iff_not.2,` can spawn those goals without trying `apply_instance`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 06 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124703801):
What's the context?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 06 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124703841):
Also, you should probably use `not_congr` instead, which doesn't have those extra assumptions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 06 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124703844):
I'm currently working on doing what I can with your file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 06 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124703849):
I don't think `aux_1` is true without assuming `f` and `g` are two-sided inverses

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 06 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124703851):
```
lemma aux_1 {α : Type*} {β : Type*} {f : α → β} {g : β → α}
  (h₁ : function.left_inverse g f) (h₂ : function.right_inverse g f)
  (p : α → Prop) : f '' {a : α | p a} = {b : β | p (g b)} :=
set.ext $ λ b, mem_image_iff_of_inverse h₁ h₂
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 06 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124703946):
This works for supp_conj:
```
lemma supp_conj (f g : homeo X X) : supp (conj g f : homeo X X) = g '' supp f :=
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 06 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705045):
Here's a proof of supp_conj:
```
-- should be in equiv.lean
theorem equiv.left_inverse (f : α ≃ β) : left_inverse f.symm f := f.left_inv

theorem equiv.right_inverse (f : α ≃ β) : function.right_inverse f.symm f := f.right_inv

-- should be in homeos.lean
theorem homeo.left_inverse (f : homeo α β) : left_inverse f.symm f := f.left_inv

theorem homeo.right_inverse (f : homeo α β) : function.right_inverse f.symm f := f.right_inv

theorem homeo.bijective (f : homeo α β) : bijective f := f.to_equiv.bijective

@[simp] theorem aut_mul_val (f g : homeo α α) (x) : (f * g) x = f (g x) :=
homeo.comp_val _ _ _

@[simp] theorem aut_one_val (x) : (1 : homeo α α) x = x := rfl

@[simp] theorem aut_inv (f : homeo α α) : f⁻¹ = f.symm := rfl

lemma supp_conj (f g : homeo X X) : supp (conj g f : homeo X X) = g '' supp f :=
begin
  unfold supp,
  rw homeo.image_closure,
  congr_n 1,
  apply set.ext (λ x, _),
  rw mem_image_iff_of_inverse g.left_inverse g.right_inverse,
  apply not_congr,
  dsimp [conj],
  exact calc
     (g * f * g⁻¹) x = x
        ↔ g⁻¹ (g (f (g⁻¹ x))) = g⁻¹ x : by simp [(g⁻¹).bijective.1.eq_iff]
    ... ↔ (f (g⁻¹ x)) = g⁻¹ x : by rw [← aut_mul_val, mul_left_inv]; simp
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705433):
A million thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705440):
This looks very nice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705459):
Right now I'm at the train station typing on my phone but I'll try this on the train

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705561):
Question about stuff you indicated as belonging to homeos.lean: are those restatements needed because of modeling mistakes I made or is it normal? I don't mind having them but I try to understand how to do things right.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 06 2018 at 07:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705616):
It is normal. Since you have a `coe_fn` instance for homeo, the coercion there is not written by composing other coercions so you have to restate theorems about the underlying function if you want them as simp lemmas or projections

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 06 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705667):
I put all the stuff together and PR'd it to your repo: https://github.com/PatrickMassot/lean-scratchpad/pull/1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705762):
Should I remove this coercion and have a coercion to equiv?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 06 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705770):
I think it is okay, especially if you expect it will get a lot of use. Otherwise the arrows can pile up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705945):
Ok. Thank you very much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 06 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124705948):
I even managed to merge using the crappy train station wifi

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 06 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124706045):
let me know if you want an explanation on something I did there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124714183):
```quote
I tried to describe my problems in https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/structure.20vs.20class/near/124574243 without code, and then I posted link to my actual code. Then I tried to describe a simplified problem. I don't what I could do better to ask for help
```
Write a MWE. I am much more inclined to look at code if I can just cut and paste it and it works first time. Git cloning and then downloading a new mathlib and building everything was a PITA and I couldn't possibly answer a question of the form "why does line 193 not work" without doing all that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124714242):
```quote
I even managed to merge using the crappy train station wifi
```
git is great for that isn't it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 06 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124714355):
```quote
Should I remove this coercion and have a coercion to equiv?
```
It seemed to me that one problem was you had coes from homeo to perm, from perm to fun and from homeo to fun. You had set it up so that the two maps from homeo to fun were definitionally equal (and if they weren't it would surely have been a nightmare) but even with definitional equality this didn't help with rw. @**Mario Carneiro** Can there be some version of rw which takes definitonal equality into account? i.e. "the user said rw (proof of X = Y) and I can't find X in the goal so I'll now start trying to find some term in the goal which is definitionally equal to X"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 06 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/homeo%20equiv%20etc./near/124714443):
I've read `erw` does that, but I've never managed to use it.

