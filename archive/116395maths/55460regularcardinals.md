---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/55460regularcardinals.html
---

## [maths](index.html)
### [regular cardinals](55460regularcardinals.html)

#### [Reid Barton (Sep 08 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133571077):
@**Mario Carneiro** I want to show that if $$\kappa$$ is a regular cardinal, then the sum of fewer than $$\kappa$$ cardinals smaller than $$\kappa$$ is less than $$\kappa$$. Is there an easy way to do this from what's already there about regular cardinals?

#### [Mario Carneiro (Sep 09 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133585985):
@**Reid Barton** added

#### [Kevin Buzzard (Sep 09 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133586025):
```quote
@**Mario Carneiro** I want to show that if $$\kappa$$ is a regular cardinal, then the sum of fewer than $$\kappa$$ cardinals smaller than $$\kappa$$ is less than $$\kappa$$. Is there an easy way to do this from what's already there about regular cardinals?
```
yeah, you can ask Mario to do it

#### [Kenny Lau (Sep 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133586031):
Do strong inaccessible cardinals exist in Lean?

#### [Mario Carneiro (Sep 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133586033):
The answer was basically "yes, once you prove a few more basic facts"

#### [Kevin Buzzard (Sep 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133586035):
That's not even right because that's not what you did -- you can mention it when Mario is within earshot is what I meant to say

#### [Kevin Buzzard (Sep 09 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133586087):
How close is `Type 1` from being one of these large cardinals?

#### [Kevin Buzzard (Sep 09 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133586090):
If alpha is a type, is homs from alpha to bool still the same type? No, we went up a level in the universe hierarchy, right?

#### [Kenny Lau (Sep 09 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133586096):
It's still the same type. Grothendieck universe is closed under power set

#### [Mario Carneiro (Sep 09 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133586099):
@**Kenny Lau** yes, `is_inacessible` means strongly inaccessible

#### [Mario Carneiro (Sep 09 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133586163):
@**Kevin Buzzard** Yes, `univ_inaccessible` asserts that a universe cardinal is inaccessible

#### [Kenny Lau (Sep 09 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133586167):
```lean
/- Lean's foundations prove the existence of ω many inaccessible
   cardinals -/
theorem univ_inaccessible : is_inaccessible (univ.{u v}) :=
is_inaccessible.mk
  (by simpa using lift_lt_univ' omega)
  (by simp)
  (λ c h, begin
    rcases lt_univ'.1 h with ⟨c, rfl⟩,
    rw ← lift_two_power.{u (max (u+1) v)},
    apply lift_lt_univ'
  end)
```

#### [Kenny Lau (Sep 09 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133586169):
cool!

#### [Kevin Buzzard (Sep 09 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133586235):
I never remember the difference between all these large cardinal axioms and I've never thought about how they interact with type theory either. I'm not sure that "normal mathematicians" care about them (in set theory or in type theory).

#### [Kevin Buzzard (Sep 09 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133586239):
(by which I mean geometers topologists analysts number theorists algebraists etc)

#### [Reid Barton (Sep 09 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133602032):
Thanks Mario! I see you also added a bunch of other statements that I was looking for while trying to figure out how to prove this.
I'm really grateful that so much cardinal arithmetic is already in mathlib--if I hadn't seen that we already had regular cardinals I probably wouldn't have started down this road towards locally presentable categories.

#### [Reid Barton (Sep 09 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133602168):
Kevin I've only ever needed regular and inaccessible cardinals. Regular cardinals are just what I wrote above, the union of a small family of small sets is again small, where "small" means cardinality $$< \kappa$$. It's useful for controlling a construction by transfinite induction up to $$\kappa$$. If we replace $$< \kappa$$ with $$\le \kappa$$ then this condition would automatically be satisfied, so every successor cardinal is regular. So regularity is not really a "largeness" condition but rather a way to rule out certain cardinals we don't like, the first example being $$\aleph_\omega = \aleph_0 + \aleph_1 + \aleph_2 + \cdots$$.

Inaccessible cardinals also have the same property with "product" in place of "union", and they are the cardinalities of Grothendieck universes, so you could say they bound the cardinality of *any* construction.

#### [Reid Barton (Sep 09 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133604572):
By the way, is it intentional that `cardinal.mk` is not `protected`? I don't really mind at the moment, but it is a little odd to see just `mk` in my goals. If there's going to be a non-`protected` name for taking the cardinality of a type, maybe something like `card` would be better.
(I think this came up earlier, when people were looking for functions named `mk` which were not `protected`, for some reason.)

#### [Kevin Buzzard (Sep 09 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133604671):
I think I once grepped through all of mathlib looking for unprotected `mk`s and that was the only one, and at the time people said it was an error but I didn't know enough about how PR's etc worked to be able to fix it.

#### [Kevin Buzzard (Sep 09 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133605106):
That's not true, it was another function not `mk`. I can't find the thread now though; might have been on gitter.

#### [Kevin Buzzard (Sep 09 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133609354):
Why do you need it? I used to think this stuff was really cool when I was a graduate student but then I realised that it never seems to actually be any use in my area

#### [Kevin Buzzard (Sep 09 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133609462):
[phone posting stuff three times]

#### [Reid Barton (Sep 09 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133609699):
One place you need the notion of regular cardinal is in the small object argument, which is a generalization of the kind of argument where you approximate a space $$X$$ by building up a cell complex where at each stage, you attach a cell $$\partial D^n \to D^n$$ for every way to map $$\partial D^n$$ to your complex so far and every way to extend it to a map $$D^n \to X$$. More generally, we could do this for any *set* of "cell" maps in any (let's say cocomplete) category. We're going to repeat this $$\kappa$$ times and in the end, we're going to want to know that any map from the domain of one of our cell maps to the end result factors through the thing we produced at stage $$\alpha$$ for some $$\alpha < \kappa$$.

#### [Reid Barton (Sep 09 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133609755):
To conclude this, we need two things.
* The domains of the cell maps are $$\kappa$$-presentable, so homs out of them commute with $$\kappa$$-filtered colimits. This is a kind of smallness condition. For example, if a set $$S$$ has cardinality less than $$\kappa$$, then a map from $$S$$ into a $$\kappa$$-filtered colimit factors through some object in the colimit.
* The ordered set of ordinals less than $$\kappa$$ is $$\kappa$$-filtered -- this is saying that $$\kappa$$ is a regular cardinal.

#### [Reid Barton (Sep 09 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133609778):
Why do we need actual regular cardinals bigger than $$\omega$$? Probably hard to give an example off-hand.

#### [Kevin Buzzard (Sep 09 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133609948):
I see. Thanks. So I guess even using transfinite induction is somehow beyond what I ever seen in practice in my area. Do you only need transfinite induction because you're trying to work with random categories?

#### [Reid Barton (Sep 09 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133610023):
No, there are actual "applied" settings like constructing localizations with respect to homology theories, where it's not easy to bound the cardinals that show up, or at least the ones which appear are bigger than $$\omega$$.

#### [Kevin Buzzard (Sep 09 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133610042):
Wow, that is what topology has become?

#### [Reid Barton (Sep 09 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133610097):
Homotopy theorists study spaces one prime at a time, didn't you know? :)

#### [Kevin Buzzard (Sep 09 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133610099):
So are there actual set-theoretic problems if you try to set this stuff up in ZFC? (in the sense that you can't actually do it?)

#### [Reid Barton (Sep 09 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133610102):
No, because there's lots of regular cardinals.

#### [Kevin Buzzard (Sep 09 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133610113):
Oh so you only need regular, not some crazy inaccessibles.

#### [Reid Barton (Sep 09 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133610128):
Yes. You could probably get by without explicitly using the notion and just taking successor cardinals in various places, but it's nicer to keep track of what you actually need.

#### [Reid Barton (Sep 09 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133610310):
That said, it is of course nice to set up the theory to work with "random" categories, or at least ones which are controlled in some sense by an arbitrary regular cardinal $$\kappa$$ (these are the locally presentable categories), and so you end up with this regular cardinal assumption baked in from the start. I'm expecting to find out exactly where it is and isn't used :)

#### [Reid Barton (Sep 09 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133612459):
In fact it would do no real damage to the theory to just replace "regular cardinal" by "successor cardinal" everywhere, particularly in view of the fact that any limit cardinal that you can "write down" (like $$\aleph_\omega$$) cannot be regular. The point is just that "regular cardinal" (sum of fewer than $$\kappa$$ cardinals below $$\kappa$$ is smaller than $$\kappa$$) is the actual property you need to make the theory work.

#### [Mario Carneiro (Sep 09 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133621586):
I'm worried that this is not the usual way we handle "size issues" in lean. Do you have an example where replacing kappa-somethings with somethings everywhere causes problems?

#### [Reid Barton (Sep 09 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133623381):
So one of the themes in this area is that we have certain constructions in which we'd like to form large (co)limits and/or do transfinite induction over all ordinals. We cannot do these constructions in ZFC and so we prove somewhat complicated theorems to show that we can replace the needed (co)limits/transfinite inductions by small ones. But, even if we assume the existence of universes so that we could perform the construction in a higher universe, we would still want to know that the resulting object belongs to the original universe when it does.

#### [Mario Carneiro (Sep 09 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133623392):
Right, in type theory the "size issue" manifests as making sure your construction is still in `Type u` given that your inputs are in `Type u`

#### [Mario Carneiro (Sep 09 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133623396):
But we don't do transfinite induction very often in type theory; the substitute is the use of a complicated inductive type

#### [Mario Carneiro (Sep 09 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133623440):
which is why I think having a regular cardinal may not be as useful as you think

#### [Reid Barton (Sep 09 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133623441):
Maybe the simplest example would be something like this. If you have a poset with least upper bounds for any subset, then it has a maximum element which you can obtain by taking the least upper bound of everything. But in category theory, we cannot obtain a terminal object in Set by taking the colimit of the identity diagram Set -> Set. I mean it is the colimit, but we do not know a priori that it exists because we only know that we can form colimits of small diagrams and Set itself is a large category.

#### [Mario Carneiro (Sep 09 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133623496):
Right, we can only take a colimit of a type in Type u

#### [Mario Carneiro (Sep 09 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133623510):
but where do regular cardinals enter the picture?

#### [Reid Barton (Sep 09 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133623626):
So, (obviously this is way overkill for this particular problem but) you can pick a regular cardinal $$\kappa$$, define what it means for a set to be "$$\kappa$$-compact" (in this case just that its cardinality is less than $$\kappa$$), show there is only a set of isomorphism classes of $$\kappa$$-compact sets (in this case, all the cardinalities less than $$\kappa$$), and pick one member from each class and form the full subcategory on those and form the colimit of that *small* diagram. Then you do more work to show that the colimit  is a terminal object not just as seen by $$\kappa$$-compact sets, but as seen by every set.

#### [Reid Barton (Sep 09 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133623701):
This also works in the category of models of any algebraic theory--here $$\kappa$$ has to be chosen larger than the arity of any operation in the theory

#### [Reid Barton (Sep 09 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133623817):
I agree that the kinds of constructions that you can do in Set by this method overlap with what you can do directly with inductive types in type theory. In this language the fact that you can form the initial fixed point of a strictly positive functor comes down to the fact that it preserves $$\kappa$$-filtered colimits for some $$\kappa$$ (which has to be bigger than the cardinalities of any types which appear as "exponents" in the functor)

#### [Reid Barton (Sep 09 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133623828):
Then you can form the fixed point by transfinite composition up to $$\kappa$$ and the fact that the functor commutes with the $$\kappa$$-filtered colimit you just wrote down is what tells you that you got a fixed point.

#### [Reid Barton (Sep 09 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133623843):
I don't see how this helps me if I want to do some arbitrary transfinite composition construction in the category of simplicial rings or whatever, though.

#### [Reid Barton (Sep 09 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133623894):
I actually am very curious when I do get to transfinite composition constructions what you have to say about representing them in Lean, because it seems like the kind of thing that Lean would be good at in some non-obvious (to me) way.

#### [Mario Carneiro (Sep 09 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624002):
```quote
So, (obviously this is way overkill for this particular problem but) you can pick a regular cardinal $$\kappa$$, define what it means for a set to be "$$\kappa$$-compact" (in this case just that its cardinality is less than $$\kappa$$), show there is only a set of isomorphism classes of $$\kappa$$-compact sets (in this case, all the cardinalities less than $$\kappa$$), and pick one member from each class and form the full subcategory on those and form the colimit of that *small* diagram. Then you do more work to show that the colimit  is a terminal object not just as seen by $$\kappa$$-compact sets, but as seen by every set.
```
Okay, so here is how I think you would do this in types: We know that we can take a colimit over any set (aka thing in `Type u`), or possibly any set satisfying some condition that is easy to satisfy. This substitutes for all the work up to the last sentence. Then we obtain an approximate colimit of Set, and we now need to show that there is some choice of type that makes the approximation a true colimit. This will require some particular "size argument" specific to the problem, but often involves constructing an inductive type larger than everything in sight

#### [Reid Barton (Sep 09 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624003):
A less trivial (but basically still the same) theorem is the adjoint functor theorem for locally presentable categories: any functor between locally presentable categories which preserves colimits has a right adjoint

#### [Reid Barton (Sep 09 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624060):
Right so the size argument is specific to the problem, but it's not specific to the choice of locally presentable category (in this case I picked Set, but it could have been Ring or whatever).

#### [Mario Carneiro (Sep 09 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624063):
what is a locally presentable category?

#### [Reid Barton (Sep 09 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624066):
And to make that size argument in general, you need to talk about cardinals

#### [Mario Carneiro (Sep 09 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624068):
You can talk about types instead

#### [Mario Carneiro (Sep 09 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624074):
of course types are cardinals of themselves

#### [Mario Carneiro (Sep 09 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624075):
so you can use type variables as proxies for cardinal numbers

#### [Reid Barton (Sep 09 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624076):
There are a bunch of equivalent formulations, but we can say that it's the category of models of an essentially algebraic theory (which means the operations might have equality preconditions, like the composition in a category).

#### [Reid Barton (Sep 09 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624128):
There's no restriction on the number or arity of the operations, except that everything involved must be a set

#### [Mario Carneiro (Sep 09 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624184):
that seems messy to work with

#### [Reid Barton (Sep 09 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624199):
Another one is: a category which is cocomplete and for some $$\kappa$$, it has a set of $$\kappa$$-compact objects which generate the whole category under $$\kappa$$-filtered colimits

#### [Mario Carneiro (Sep 09 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624248):
I'm reading that on nlab now, and now I need to figure out what $$\kappa$$-compact and $$\kappa$$-filtered colimit mean

#### [Reid Barton (Sep 09 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624253):
I can give you three equivalent definitions in Lean :)

#### [Reid Barton (Sep 09 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624255):
For $$\kappa$$-filtered categories, that is

#### [Reid Barton (Sep 09 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624316):
I guess it's kind of hard to explain how $$\kappa$$-filtered colimits arise except that they give a good theory of $$\kappa$$-compact objects.
If you want, you can substitute $$\kappa$$-directed which is a bit simpler technically.

#### [Mario Carneiro (Sep 09 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624368):
Maybe you can tell me what goes wrong if $$\kappa$$ is not a regular cardinal?

#### [Reid Barton (Sep 09 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624383):
Well it's no longer true that a $$\kappa$$-small colimit of $$\kappa$$-compact objects is $$\kappa$$-compact (because in Set, this is basically the fact I asked you for).

#### [Mario Carneiro (Sep 09 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624433):
Is there an inductive closure condition that would ensure this works?

#### [Reid Barton (Sep 09 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624435):
You might want to take a quick look at https://ncatlab.org/nlab/show/arity+class

#### [Reid Barton (Sep 09 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624446):
Actually, maybe I misunderstood but that page may be somehow relevant.

#### [Reid Barton (Sep 09 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624450):
I think you want to build up the class of $$\kappa$$-compact objects in some inductive fashion?

#### [Reid Barton (Sep 09 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624493):
Or, there is another description again of locally presentable categories.

#### [Mario Carneiro (Sep 09 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624494):
You start from some initial objects, and want to close it to a suitably large cardinal

#### [Reid Barton (Sep 09 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624498):
Start with $$\kappa$$ and a *small* category which admits $$\kappa$$-small colimits.

#### [Reid Barton (Sep 09 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624506):
Then, you can "freely adjoin" all $$\kappa$$-filtered colimits and this gives you a general locally $$\kappa$$-presentable category.

#### [Mario Carneiro (Sep 09 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624514):
Although I don't think "regular cardinal" is an inductive condition

#### [Reid Barton (Sep 09 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624579):
Actually in some of these cases, you can say exactly what goes wrong if you don't assume $$\kappa$$ is regular.
Typically you get the same notion as if you had replaced $$\kappa$$ by its cofinality.

#### [Reid Barton (Sep 09 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624585):
So, a regular cardinal $$\kappa$$ is really "standing in" for the class of all cardinals of cofinality $$\kappa$$, from this point of view

#### [Reid Barton (Sep 09 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624656):
But it's better to work only with regular ones, because for example a locally $$\kappa$$-presentable category is also locally $$\lambda$$-presentable for $$\kappa \le \lambda$$, but if you were to ignore the condition that $$\lambda$$ be regular, then it might no longer be true (because the cofinality of $$\lambda$$ could be less than $$\kappa$$).

#### [Reid Barton (Sep 09 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624792):
In the end, the point is really that it's a large class of categories in which you can do a large class of constructions in a uniform way (once you know this parameter $$\kappa$$).

#### [Reid Barton (Sep 09 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624889):
And a lot of the constructions involve this somewhat involved reasoning about cardinalities, so it's worth it to not have to do them more than once

#### [Reid Barton (Sep 09 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624895):
For example, the construction of free objects

#### [Reid Barton (Sep 09 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133624968):
I guess one other point is that to build a free object as an inductive type, you need Lean to be able to see syntactically that the functor involved is strictly positive.

#### [Reid Barton (Sep 09 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133625020):
But to do the same construction even in Set using this regular cardinal kind of machinery, you only have to prove a theorem about how it commutes with sufficiently highly filtered colimits

#### [Mario Carneiro (Sep 09 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133625027):
I think there is usually a way to make this work by writing the functor differently

#### [Mario Carneiro (Sep 09 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133625042):
I have no sense of how easy "you only have to prove a theorem about how it commutes with sufficiently highly filtered colimits" is

#### [Reid Barton (Sep 09 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133625101):
Sure, but proving a theorem is more flexible than having to produce something that satisfies a judgment. And you can abstract over an accessible functor, but you can't abstract over a strictly positive type constructor.

#### [Mario Carneiro (Sep 09 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133625150):
But you can usually write something that is obviously positive but not obviously the same as your functor

#### [Mario Carneiro (Sep 09 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133625162):
and then the theorem is shifted to proving this equality

#### [Reid Barton (Sep 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133625231):
Well it depends on what the functor is of course :)
For FX = X^S, proving that F commutes with $$\kappa$$-filtered colimits -- or we can take $$\kappa$$-directed colimits for simplicity -- is checking that if $$I$$ is a $$\kappa$$-directed poset and for each $$s \in S$$, we have an element in some $$A_{i(s)}$$, then we can map them all into some common $$A_{i'}$$ -- and this is the definition of $$\kappa$$-directed for $$\kappa > |S|$$.

#### [Reid Barton (Sep 09 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133625237):
What if my functor is something like FX = the set of unordered pairs of elements of X?

#### [Reid Barton (Sep 09 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133625257):
Anyways I think the ability to abstract over "an accessible functor" is the more interesting thing

#### [Reid Barton (Sep 09 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133625488):
Just to give you a taste, in the theory of model categories all this machinery is used heavily. One of the most important ways to construct model categories is https://ncatlab.org/nlab/show/combinatorial+model+category#SmithTheorem and if you just look at the hypotheses it should give you some sense of how this stuff gets used. It's actually quite difficult to construct any interesting examples of model categories, so this is a major result.

#### [Reid Barton (Sep 09 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/regular%20cardinals/near/133625739):
(My secret plan is to formalize the proof of this theorem.)

