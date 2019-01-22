---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91089structurevsclass.html
---

## [general](index.html)
### [structure vs class](91089structurevsclass.html)

#### [Kenny Lau (Apr 02 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124512218):
The age-old question: when to use `structure` and when to use `class`?

#### [Kevin Buzzard (Apr 02 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124523699):
You have to step back and decide whether you want a global, unique instance or not.

#### [Kenny Lau (Apr 03 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558513):
```
universes u v

variables (G : Type u) [group G] (X : Type v)

class group_action : Type (max u v) :=
(fn : G → X → X)
(one : ∀ x, fn 1 x = x)
(mul : ∀ g h x, fn (g * h) x = fn g (fn h x))

#### [Kenny Lau (Apr 03 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558514):
should this be a `class` or a `structure`?

#### [Mario Carneiro (Apr 03 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558557):
A class, I would think, if you want that notation to work

#### [Mario Carneiro (Apr 03 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558565):
You may also be able to make one of the two type arguments an `out_param`. Would you say that one (kind of) uniquely determines the other?

#### [Kenny Lau (Apr 03 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558605):
```quote
A class, I would think, if you want that notation to work
```
I also think so, but then the following becomes awkward, since it suggests that I can synthesize more than one group actions:
```
protected def trivial : group_action G S :=
⟨λ g, id, λ x, rfl, λ g h x, rfl⟩

#### [Kenny Lau (Apr 03 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558607):
```quote
You may also be able to make one of the two type arguments an `out_param`. Would you say that one (kind of) uniquely determines the other?
```
a `module` is just an R-action right, so maybe we can use the same strategy

#### [Kenny Lau (Apr 03 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558608):
although the set has an abelian group structure

#### [Kenny Lau (Apr 03 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558615):
I don't know in this case, what do you think?

#### [Mario Carneiro (Apr 03 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558618):
Of course there are multiple group actions in actuality, but probably you want to focus on just one in a given context. Maybe using `local instance`?

#### [Kenny Lau (Apr 03 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124558662):
I actually just want to state it, so maybe `def` is fine

#### [Patrick Massot (Apr 03 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561840):
```quote
```lean
universes u v

variables (G : Type u) [group G] (X : Type v)

class group_action : Type (max u v) :=
(fn : G → X → X)
(one : ∀ x, fn 1 x = x)
(mul : ∀ g h x, fn (g * h) x = fn g (fn h x))
```
```
Why not
```lean
structure  action (G : Type*) [group G] (α : Type*) :=
(map : G → equiv.perm α)
(homo : is_group_hom map)

```

#### [Kenny Lau (Apr 03 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561884):
because.

#### [Kenny Lau (Apr 03 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561886):
because stating it more abstractly makes it less useful

#### [Kenny Lau (Apr 03 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561889):
conciseness c’est pas tous

#### [Patrick Massot (Apr 03 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561902):
See also https://github.com/PatrickMassot/lean-scratchpad/blob/master/subgroups.lean for related random stuff

#### [Patrick Massot (Apr 03 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561946):
Using group homomorphism should give you access to lemmas you'll need to reprove with your less abstract definition

#### [Mario Carneiro (Apr 03 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561951):
you want to restate them anyway though

#### [Mario Carneiro (Apr 03 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561993):
I think that kenny's version more accurately represents the data content, which is a single function G -> X -> X satisfying some properties, rather than a function to a pair of functions

#### [Mario Carneiro (Apr 03 2018 at 07:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124561996):
of course you want your version stated as lemmas, and then all those theorems become available in the end anyway

#### [Patrick Massot (Apr 03 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124562198):
Mathematically the accurate representation of content if certainly mine. About Lean usability I don't know of course

#### [Mario Carneiro (Apr 03 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124562574):
they are certainly equivalent, but the data content is different. It's like the difference between representing the integers by an integer, or by a pair of an integer and its negative. The representations are equivalent, but one has some additional redundancy

#### [Kenny Lau (Apr 03 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124562588):
let’s all just represent nat by Pi X, X->(X->X)->X

#### [Patrick Massot (Apr 03 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574243):
Ok, I think I understand the confusion: we are talking about two separate issues. My claim is that the mathematically meaningful and redundancy free point of view is to define a group action as a group homomorphism. It seems you are discussing the redundancy in your definition of `perm X`. Now I'm even more confused. A long time ago you told I should build homeomorphisms on top of equiv. Since then I've been suffering through two levels of coercions (`homeo` to `equiv` to `function`). And I have loads of attempted proofs where I'm stuck with expression mixing multiplication in the group `homeo X X` and composition of `equiv` and composition of  functions, which are all the same but I never know how to tell Lean.  And a few days ago you proved this `f '' (-s) = - f '' s` by throwing away `equiv` and use `function.bijective`, so this is the second time in a couple of days where you seem to avoid `equiv`. I would appreciate any clue about what I should be doing with my groups of homeomorphisms.

#### [Kenny Lau (Apr 03 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574254):
@**Patrick Massot** How would you state a G-Set homomorphism in your definition of G-Set? In mine, f:X->Y is a homomorphism if f(gx)=gf(x)

#### [Patrick Massot (Apr 03 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574430):
I don't understand your question. If ρ_X : G → perm X and ρ_Y : G → perm Y are two G-action then f : X → Y is a G-morphism if, for all g, f ∘ ρ_X(g) = ρ_Y(g) ∘ f

#### [Kenny Lau (Apr 03 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574442):
interesting

#### [Patrick Massot (Apr 03 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574443):
Of course you could phrase this in terms of natural transformations

#### [Kenny Lau (Apr 03 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574445):
I can see a commutative diagram inside :P

#### [Patrick Massot (Apr 03 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574447):
If you want Mario to run away

#### [Kenny Lau (Apr 03 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574448):
oh really

#### [Patrick Massot (Apr 03 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574455):
Sure

#### [Kenny Lau (Apr 03 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574458):
could you enlighten me?

#### [Kenny Lau (Apr 03 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574468):
and I feel like I've seen this in group rep

#### [Patrick Massot (Apr 03 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574540):
But what I was advocating is an intermediate point of view, not going all the way to using categories to define group actions

#### [Kenny Lau (Apr 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574579):
I am writing a category theory repo

#### [Kenny Lau (Apr 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574581):
so it is helpful to me

#### [Kenny Lau (Apr 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574584):
https://github.com/kckennylau/category-theory

#### [Kenny Lau (Apr 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574586):
in fact I'm proving that the forgetful functor GSet->Set has right adjoint

#### [Patrick Massot (Apr 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574591):
A group is a category with one object, and morphisms given by the group element

#### [Patrick Massot (Apr 03 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574601):
then a G-set is simply a functor from G to Set

#### [Kenny Lau (Apr 03 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574603):
but it would be a fun fact to prove that that functor thing is isomorphic to the GSet in the category of categories

#### [Kenny Lau (Apr 03 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574611):
aha, so it's the slice category

#### [Patrick Massot (Apr 03 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574612):
And a morphism of G-set is a morphism in this category

#### [Patrick Massot (Apr 03 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574617):
hence a natural transformation

#### [Kenny Lau (Apr 03 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574621):
very interesting

#### [Patrick Massot (Apr 03 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574657):
It's meant to be the very first exercise you do after reading the definition of a natural transformation

#### [Kenny Lau (Apr 03 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574667):
where do you learn category theory?

#### [Patrick Massot (Apr 03 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574668):
Are you talkin to Scott about this repo?

#### [Kenny Lau (Apr 03 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574671):
I'm not; he hasn't replied to my message

#### [Kenny Lau (Apr 03 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574676):
I don't think I've seen him here for a while

#### [Patrick Massot (Apr 03 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574689):
He was probably captured by real life

#### [Patrick Massot (Apr 03 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574694):
This happened to me during the last couple of weeks

#### [Patrick Massot (Apr 03 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574741):
And actually students will probably invade my office soon, and I'll have to let you do your category theory exercises

#### [Kenny Lau (Apr 03 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124574747):
alright

#### [Kevin Buzzard (Apr 03 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124578652):
```quote
I don't think I've seen him here for a while
```
Scott is on holiday at the minute.

#### [Scott Morrison (Apr 04 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599463):
I am back, but actual maths has captured my attention for a moment --- a collaborator is here this week.

#### [Kenny Lau (Apr 04 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599466):
omg you're back

#### [Scott Morrison (Apr 04 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599523):
I am definitely still working on getting my category theory library reading for a PR, but there is still some work to do, which I haven't been finding a lot of time for.

#### [Kenny Lau (Apr 04 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599529):
hope you don't mind the fact that i'm creating another

#### [Scott Morrison (Apr 04 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599532):
No, not at all.

#### [Scott Morrison (Apr 04 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599537):
If you would like to join forces, however, I would be very happy.

#### [Kenny Lau (Apr 04 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599545):
sure

#### [Scott Morrison (Apr 04 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599549):
I think it is good to have different eyes and different opinions on projects.

#### [Scott Morrison (Apr 04 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599554):
I think my focus for category theory for a while will be not adding new material, but rather getting the basics PR'd into mathlib.

#### [Scott Morrison (Apr 04 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599558):
If you would like to add material, however, that is certainly fine.

#### [Scott Morrison (Apr 04 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599601):
Also, if you have comments and criticisms of the basics, I'm very happy to hear them concurrently with preparing to PR.

#### [Kenny Lau (Apr 04 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599609):
have you looked at mine?

#### [Scott Morrison (Apr 04 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599610):
I'm happy to just give you commit access on the repository if you'd like, or I'll merge PRs as they come.

#### [Scott Morrison (Apr 04 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599614):
Looking at yours is on my todo list, but Lean is not getting to the top of the todo list again until next week.

#### [Kenny Lau (Apr 04 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599615):
well you would need to fix your repo first, I heard it doesn't work well with the latest mathlib

#### [Scott Morrison (Apr 04 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599627):
It was working after the "monad merge" on Lean, and the subsequent update to Lean. I will check again in a moment. Hopefully it is okay, however.

#### [Scott Morrison (Apr 04 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124599949):
Besides irrelevant problems in mathlib, lean-category-theory builds fine against the HEAD of Lean at the moment.

#### [Kevin Buzzard (Apr 04 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124616405):
Kenny's top priority at the minute is revising for mechanics, but let me give a huge +1 to the idea of you two collaborating on category theory. Kenny seems to understand all the standard category theoretic notions well now, and has a bunch of examples in his head, so whilst he might not yet be at the stage of doing infinity-1 categories or whatever, he will almost certainly have more time to work on categories in the near future (e.g. after his mechanics exam in mid-May)

#### [Kenny Lau (Apr 04 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124616411):
right, there's mechanics

#### [Kevin Buzzard (Apr 04 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124616413):
And I am doing my schemes library by proving lots of things about sheaves and presheaves of types, and then writing ad hoc extensions to sheaves of rings

#### [Kevin Buzzard (Apr 04 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124616422):
and the sooner I can do sheaves of objects the better

#### [Patrick Massot (Apr 04 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124616865):
Exams are in mid-May and they are already revising?

#### [Patrick Massot (Apr 04 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124616867):
That's even more amazing than first year students using Lean!

#### [Kenny Lau (Apr 04 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124616918):
"they are already revising", more like "they are already being told to revise"

#### [Patrick Massot (Apr 04 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124617037):
This afternoon I will attend a talk whose title is: "Perfectoid spaces and us"

#### [Patrick Massot (Apr 04 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124617046):
for a general mathematical audience

#### [Kenny Lau (Apr 04 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124617047):
by thomas hales?

#### [Patrick Massot (Apr 04 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124617050):
Did you make any progress in formalizing perfectoid spaces

#### [Kenny Lau (Apr 04 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124617055):
aucun

#### [Patrick Massot (Apr 04 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124617056):
No, by Ariane Mézard

#### [Kevin Buzzard (Apr 04 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124627096):
Our progress so far is a new empty repository, and Kenny wrote some stuff about valuations and then found he didn't have push access.

#### [Kevin Buzzard (Apr 04 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124627162):
I think that claiming that we "did" schemes but not even being able to construct one example is not such a great advertisement, so when I write Lean code I typically try and fix this problem. We are nearly there. I broke the problem down into three parts; part (3) is basically done, part (1) Chris Hughes has nearly finished and part (2) should be easy (and I will start on it soon, hopefully). When we can prove that an affine scheme is a scheme I will get back to perfectoid spaces.

#### [Kevin Buzzard (Apr 04 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124627166):
```quote
by thomas hales?
```
Kenny, I don't think Tom Hales knows too much about perfectoid spaces.

#### [Patrick Massot (Apr 04 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124633933):
I was sitting next to Fontaine during that talk and, according to him, Ariane also doesn't know much about perfectoid spaces.

#### [Patrick Massot (Apr 04 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124633945):
Which probably means we are lucky Mézard gave this talk instead of Fontaine :smile:

#### [Patrick Massot (Apr 04 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124633959):
Also, I didn't tell Fontaine about schemes without example

#### [Patrick Massot (Apr 04 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124633963):
But I confess I told this story to François Charles a couple of days ago

#### [Patrick Massot (Apr 04 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124634012):
He agrees the fact that affine schemes are schemes is not trivial, but still disapproves having defined schemes with no example

#### [Patrick Massot (Apr 04 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124634029):
During that inauguration thing I also got the opportunity of chatting a bit with Christine Paulin (the dean of my university, who was involved in the theoretical foundations of Coq).

#### [Patrick Massot (Apr 04 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124634194):
Then a colleague asked me why I was talking to her, and I may have found one new recruit for Lean

#### [Kevin Buzzard (Apr 04 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124638886):
```quote
Which probably means we are lucky Mézard gave this talk instead of Fontaine :smile:
```
Anyone who wants to hear Fontaine's opinion can just read his Sem Bourbaki :-)

#### [Patrick Massot (Apr 04 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124642522):
I once opened this Bourbaki seminar and decided it was not written for me :wink:

#### [Patrick Massot (Apr 04 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20vs%20class/near/124642590):
But, to be honest, I don't think Fontaine would say the Bourbaki I wrote about flexibility of contact structures in higher dimensions was written for him.

