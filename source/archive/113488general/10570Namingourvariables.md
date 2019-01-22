---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10570Namingourvariables.html
---

## [general](index.html)
### [Naming our variables](10570Namingourvariables.html)

#### [Kenny Lau (Apr 07 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124741274):
```quote
For consistency, please change your upper case type names to `α, β, γ` etc.
```
https://github.com/leanprover/mathlib/pull/89#discussion_r179398893

#### [Kenny Lau (Apr 07 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124741277):
@**Kevin Buzzard** :)

#### [Kevin Buzzard (Apr 07 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124742233):
I am skeptical about this approach being always the best idea. Rings are called R in mathematics, groups are called G and so on. Schemes are called S and their structure sheaves are called $$\mathcal{O}_S$$. They're all types.

#### [Kevin Buzzard (Apr 07 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124742238):
That was supposed to be a calliagraphic O

#### [Kenny Lau (Apr 07 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124742239):
I triggered the right person :P

#### [Kevin Buzzard (Apr 07 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124742289):
My index sets are called things like alpha, beta, because they are just random types so I stick to the conventions.

#### [Kenny Lau (Apr 07 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124742292):
what happened to iota

#### [Kevin Buzzard (Apr 07 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124742297):
But for readability isn't it better to have math objects called what mathematicians call them?

#### [Kevin Buzzard (Apr 07 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124742298):
i.e. depends on the typeclass

#### [Simon Hudon (Apr 07 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124743335):
@**Kevin Buzzard** I'd be tempted to agree with you on groups and rings but I'm also hesitant to add any exception to style rules. The more exceptions there are, the harder they are to understand, enforce and agree to. I guess the next question is: what would be a good reason to create an exception?

#### [Simon Hudon (Apr 07 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124743443):
Not answering my own question yet ... I can think of good reasons to not call type variables `R` or `G`. Being a ring or a group is not necessarily all that they are. If they conform to independent structures, which one should dictate the name?

#### [Simon Hudon (Apr 07 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124743518):
I think the reason for naming them `R` or `G` is somewhat undermined by the fact that the information is already conveyed by `[group α]`

#### [Kevin Buzzard (Apr 07 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124756586):
I want to argue that mathematicians have solved these problems. I am currently writing a bunch of stuff about topological spaces and I call my topological spaces X and Y, because this is what mathematicians tend to call them, but if I had a topological ring I would call it R, because this is what mathematicians tend to call them. I would definitely never call any of them alpha.

#### [Kevin Buzzard (Apr 07 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124756627):
Given that many mathematical objects are types, it seems like a very strange rule to demand that they're all called alpha etc. Isn't this analogous to someone saying "OK so in this code, everything that is a variable needs to be called standard variable names like x,y,z etc"? [regardless of what they're doing]

#### [Kevin Buzzard (Apr 07 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124756629):
If we weren't using type class inference and things like groups, rings etc were their own specialised types then nobody would bat an eyelid if groups were all called G

#### [Mario Carneiro (Apr 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124756678):
I think it is just like that though. For me, when writing lean code the "sort of thing" the type represents seems less important since it's not being directly associated to the notations and such like it is in math. (Instead, the typeclass parameters do all the heavy lifting here.) From what I can tell, the current convention is to use `G H` etc for `Group`s, but still to use greek letters for unbundled group-types.

#### [Mario Carneiro (Apr 07 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124756679):
It's just that `Group` hasn't needed to play a big role (yet) in mathlib, so you don't see it much

#### [Kenny Lau (Apr 07 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758522):
@**Kevin Buzzard** what will happen if I call a group alpha and a ring beta in the m1p2 test?

#### [Kenny Lau (Apr 07 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758523):
I mean, alpha[beta] doesn’t look so bad as a group ring does it

#### [Kevin Buzzard (Apr 07 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758560):
Just don't get me started.

#### [Kevin Buzzard (Apr 07 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758563):
I'm trying to prove an affine scheme is a scheme

#### [Kevin Buzzard (Apr 07 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758564):
Lean has notational irrelevance

#### [Kevin Buzzard (Apr 07 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758565):
so notation is irrelevant

#### [Kenny Lau (Apr 07 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758613):
it’s my PR; of course i will get you started

#### [Kenny Lau (Apr 07 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758621):
let alpha be a real number... let beta be a sequence with limit to gamma

#### [Mario Carneiro (Apr 07 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758622):
now *that's* a bridge too far

#### [Mario Carneiro (Apr 07 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758661):
I kid, but in the lean convention only things of type `Type` are greek letters

#### [Kevin Buzzard (Apr 07 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758940):
My gut instinct is to be completely happy with _restrictions_ of this form -- "we use alpha to be something of type Type so don't use it to be anything else"

#### [Kevin Buzzard (Apr 07 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758942):
because mathematicians typically have more than one notation for things

#### [Kevin Buzzard (Apr 07 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758943):
e.g. if you told me I couldn't use G for groups because mathlib conventions were that G was always for rings

#### [Kevin Buzzard (Apr 07 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758945):
then I would just use H for groups

#### [Kevin Buzzard (Apr 07 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20our%20variables/near/124758948):
so that sort of rule is easy to abide by

