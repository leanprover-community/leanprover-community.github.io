---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85628CategorytheoryPR.html
---

## [general](index.html)
### [Category theory PR](85628CategorytheoryPR.html)

#### [Scott Morrison (Aug 07 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131024775):
Hi @**Mario Carneiro**, I didn’t understand your suggestion to use “`functor.id` (protected)”. What is “protected”?

#### [Scott Morrison (Aug 07 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131025217):
Worked it out.

#### [Mario Carneiro (Aug 07 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026124):
Hm, I see that you renamed the identity functor to `category.identity` and the identity natural transformation to `functor.identity`. I assume you did that so that you can use projection notation, but I think it's more confusing than is worth it. What do the mathematicians here think?

#### [Scott Morrison (Aug 07 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026681):
Oh, I'm not at all attached to projection notation here: I'd guessed that was what you'd tell me to do!

#### [Scott Morrison (Aug 07 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026746):
As far as I'm concerned I would be happy with any of:
`C.identity`, `Functor.id C`, `Functor.identity C`, or `1 : C ↝ C`.

#### [Scott Morrison (Aug 07 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026756):
(I know how to arrange for any of those, just want to know what is preferred.)

#### [Johan Commelin (Aug 07 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026820):
My order of preference would be 4,1,3,2

#### [Mario Carneiro (Aug 07 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026879):
Johan, Would you prefer to see `1 X` or `functor.id C X` in a goal printout talking about the identity functor applied to an object `X`?

#### [Mario Carneiro (Aug 07 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026883):
(this isn't a rhetorical question)

#### [Scott Morrison (Aug 07 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026887):
@**Mario Carneiro**, I'm confused why we would want to put `protected` on the definition of the identity functor. What is the motivation there? It seems if we're going to hide that, we should also hide the lemmas about it.

#### [Scott Morrison (Aug 07 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026890):
@**Mario Carneiro**, seeing that comparison, I really dislike `1 X`!

#### [Mario Carneiro (Aug 07 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026923):
because `id` is already a global definition, and we don't want to interfere with that

#### [Scott Morrison (Aug 07 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026931):
How about `functor.identity C`?

#### [Mario Carneiro (Aug 07 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026932):
plus there are like 5 different `id`s going around and I'd like to know which is which

#### [Scott Morrison (Aug 07 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026933):
No need to collide with the global `id`

#### [Scott Morrison (Aug 07 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026935):
or the `category.id`

#### [Scott Morrison (Aug 07 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026936):
... :-)

#### [Mario Carneiro (Aug 07 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026949):
the name collision is deliberate though, it's a consistent naming scheme

#### [Scott Morrison (Aug 07 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026955):
In fact, I now really dislike the `has_one` instances for both `C ↝ C` and `F ↝ F`, and want to remove both.

#### [Mario Carneiro (Aug 07 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131026995):
I'm surprised this bothers you given that we already have `𝟙 X`

#### [Scott Morrison (Aug 07 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027003):
Okay... so `functor.id C`, `nat_trans.id F`, and the only use of the symbol 1 will be `𝟙 X`.

#### [Mario Carneiro (Aug 07 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027012):
I'm okay with that

#### [Mario Carneiro (Aug 07 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027021):
the protection is not needed for the theorems since they usually have more specific names that don't collide with core

#### [Mario Carneiro (Aug 07 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027067):
they are still namespaced in `functor` though so you will need to use the prefix unless you have opened it

#### [Johan Commelin (Aug 07 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027091):
```quote
Johan, Would you prefer to see `1 X` or `functor.id C X` in a goal printout talking about the identity functor applied to an object `X`?
```
I think I would prefer something like that `id_ C` or `1_ C`.

#### [Mario Carneiro (Aug 07 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027096):
How about using local notations for that?

#### [Johan Commelin (Aug 07 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027100):
That might work.

#### [Mario Carneiro (Aug 07 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027141):
You probably don't need the `C` most of the time either

#### [Johan Commelin (Aug 07 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027144):
Yes, but it might help to remind you of which cat you're working with.

#### [Mario Carneiro (Aug 07 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027148):
Well if it shows up as `1_ X` then it's inferrable from context

#### [Johan Commelin (Aug 07 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027156):
I might think that is the identity morphism of X

#### [Mario Carneiro (Aug 07 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027160):
that's the *completely different* `𝟙 X` :P

#### [Scott Morrison (Aug 07 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027162):
Yeah, I think we want to make expressions that look even vaguely like `1 X` unambiguous

#### [Scott Morrison (Aug 07 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027207):
and my preference is that the only similar looking expressions are `𝟙 X`, the identity morphism on `X`.

#### [Scott Morrison (Aug 07 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027211):
If only there was a triple struck 1

#### [Mario Carneiro (Aug 07 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027212):
I keep being reminded of `equiv.refl` as the only notation for the identity equiv

#### [Johan Commelin (Aug 07 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027220):
Hmm, I prefer `𝟙 C`

#### [Johan Commelin (Aug 07 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027229):
If we have `𝟙 X` already.

#### [Mario Carneiro (Aug 07 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027232):
I think that will be a thing too

#### [Johan Commelin (Aug 07 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027233):
After all, it is the identity morphism on `C` in `Cat`.

#### [Johan Commelin (Aug 07 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027238):
Aah, and they will be defeq, but we can't have only one definition?

#### [Scott Morrison (Aug 07 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027284):
Yeah... that's a bit of a sore point. `Cat` is of course a 2-category, and thinking of it as a 1-category by just ignoring the top level invites trouble.

#### [Mario Carneiro (Aug 07 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027304):
so that means `𝟙 C` is not (or will be) defeq to `functor.id C`?

#### [Mario Carneiro (Aug 07 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027310):
or does `𝟙 C` just not typecheck?

#### [Scott Morrison (Aug 07 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027356):
At present it just doesn't typecheck

#### [Scott Morrison (Aug 07 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131027360):
Let me investigate this point for a few minutes.

#### [Scott Morrison (Aug 07 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028385):
Arranging for `𝟙 C` to typecheck may not be impossible, but it will take quite a bit of work which hasn't otherwise been necessary, so I'd like to kick that back to some TODO list. :-)

#### [Johan Commelin (Aug 07 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028392):
Sure, I'm completely fine with that (-;

#### [Scott Morrison (Aug 07 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028441):
For now you just write `functor.id C` when you want the identity functor.

#### [Johan Commelin (Aug 07 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028442):
Sounds like we might want `has_id` notation.

#### [Johan Commelin (Aug 07 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028454):
And then all sorts of things can be instances of `has_id`, and you can write a doublestroke 1 in front of them.

#### [Mario Carneiro (Aug 07 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028460):
and what would the type of `generic.id` be?

#### [Johan Commelin (Aug 07 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028465):
What's that?

#### [Mario Carneiro (Aug 07 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028471):
if you have a typeclass, you have to decide in advance what the type of the thing is

#### [Johan Commelin (Aug 07 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028511):
You are talking with a "cargo cult Leaner"

#### [Johan Commelin (Aug 07 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028520):
So, you mean the type of `has_id`?

#### [Mario Carneiro (Aug 07 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028530):
well, `has_id` will be a class that contains an identity operation, and that identity operation will have some type

#### [Johan Commelin (Aug 07 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028534):
Aah, I see.

#### [Johan Commelin (Aug 07 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028538):
Yeah... depends...

#### [Johan Commelin (Aug 07 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028546):
And it depends a bit too much to be a dependent type.

#### [Mario Carneiro (Aug 07 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028593):
I suspect this will be a sticking point in any such plans

#### [Mario Carneiro (Aug 07 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131028605):
category theory just has too much overloading here to make sense of it

#### [Mario Carneiro (Aug 07 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131036160):
Congratulations to Scott for his perseverance in improving this PR for mathlib and even going back to change his library, which could not have been an easy task.

#### [Scott Morrison (Aug 07 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131037342):
Phew... I think I've rewritten everything about 4 times now. It does keep getting less bad as a result, whatever that signifies. :-)

#### [Mario Carneiro (Aug 07 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131037460):
now that we've got the basic definitions, how about the less basic ones? :D

#### [Scott Morrison (Aug 07 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131037525):
Don't worry, there's a `category_theory_2` branch ready to turn into a PR. :-)

#### [Scott Morrison (Aug 07 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131037530):
I'm just having to google how rebasing works!

#### [Scott Morrison (Aug 07 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131038016):
okay... rebasing is still confusing me, but there's a second PR now!

#### [Johan Commelin (Aug 07 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131038508):
Cool! Awesome! Congratulations!

#### [Kevin Buzzard (Aug 07 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131040791):
Oh the first PR has been merged! Fabulous!

#### [Scott Morrison (Aug 08 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131100523):
Hi @**Reid Barton** sometime soon we should  do some coordination to combine the category theory development you've been doing in your homotopy theory repo with mine.

#### [Patrick Massot (Aug 08 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Category%20theory%20PR/near/131100538):
This should definitely be one of our small groups in Orsay (although you can start online of course).

