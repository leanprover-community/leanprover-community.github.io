---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/24083separatedquotient.html
---

## Stream: [maths](index.html)
### Topic: [separated quotient](24083separatedquotient.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 30 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134934490):
@**Johannes Hölzl** why https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L185 is not an instance?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 30 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134934537):
Oh! Why this completeness assumption?!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 30 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134934585):
I love doing that with Lean: I removed the assumption and the proof still compiles!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 30 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134935104):
yeah should be instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 30 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134935220):
Yeah for removing assumptions. You remove them in real life and then have to understand the proof all over again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 30 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134935260):
exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 30 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134935707):
I just noticed while reviewing my work that this unneeded assumption is simply copy-paste from the previous lemma (where it *is* needed).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 30 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134935788):
Anyway, @**Johannes Hölzl** please have a look at https://github.com/leanprover-community/mathlib/commit/cfb60c52739921a0a9b36bbe2a73400dc2fc372a

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 30 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134935833):
The nonempty quotient stuff will have to move to its proper place but I don't have courage right now (it means recompiling all mathlib since the proper place is very low in the tree).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 30 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134935851):
Kevin: this commit is still work towards ring completions. It's preparation for the isomorphism from `completion (separation_quotient a)` to `completion a`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 30 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134935907):
We're getting really close. We may have ring completion tomorrow if I can hide from my secretary and from the head of my department. But first I need to sleep.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134954357):
@**Johannes Hölzl** I just noticed that some lemmas from my versions of uniform spaces completions didn't make it through your refactoring. In particular https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L266-L267 and https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L274 (I realized I forgot the analogue of the last one for the separation quotient yesterday). Is it on purpose? From a categorical point of view they are crucial.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134955431):
sorry, both got lost. I will add them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957496):
It's ok, I can add them back

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957792):
Just to make sure: Johannes, are you working on this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957884):
Not yet, I wanted to start now. Do you have some changes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957928):
No, I was about to start :smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957931):
I'll let you do this, and work on the next steps

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957949):
okay

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957952):
Did you pull what I did yesterday?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957962):
One thing I will also change: remove `is_ideal'`. I don't think it is necessary.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957966):
yes, i just pulled

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134957973):
Fine. I was worried that nobody reacted to this `is_ideal'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134958024):
But I hope the topology proof won't become ugly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134958110):
I hope so, too. That's why I plan to remove it again. If it gets ugly I will add a "constructor" function for `is_ideal` instead of the additional structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134958121):
Ok, great. I'll stop asking questions and let you work then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964418):
So I restructured a little bit and replaced the proof for `is_ideal (closure _)`, by adding nicer rules for membership in `closure`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964465):
I see you pushed while I was writing a link to the previous version :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964571):
Hehe good. I guess you want to work now on the ring completion without assuming Hausdorff?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964596):
Yes, and then you'll have the pleasure to refactor it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964669):
No problem. I'm sure it will be in a good state!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964686):
I'm a bit sad that the proof of `ideal_closure` is no unrecognizable for mathematicians

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964708):
I don't know why you and Mario don't like equalities between functions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964765):
It's really going against main stream mathematics to replace function equality with elements equality everywhere

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964766):
No I'm confused. I think it is much more readable than before. We state what kind of steps we proof (is it the zero, add, or mul case) and we say how we proof the membership in the `closure`. Before it was just a sequence of tactics, not mentioning which case is proved.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964783):
Category theory tells us that elements are confusing, only arrows matter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964857):
I agree that stating which case we are proving is nice. What I'm talking about is hiding that the proof key is `image_closure_subset_closure_image`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964869):
that you've hidden in `mem_closure`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134964887):
also that name is much harder to find than image_closure_subset_closure_image

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134966165):
why is it harder to find? You ask, "is there anything to prove membership in `closure`" then you find it. if you ask: is there anything w.r.t. subset of closure you don't find it. But both are valid. Your proof might be more categorical. But only halfway, you proof something about subsets, not about arrows. You still use `closure_mono`, instead of arguing about an mono-homomorphism into another type.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134966222):
`closure` is very set based, so for me it doesn't make sense to argue about arrows.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134970528):
```quote
No problem. I'm sure it will be in a good state!
```
@**Johannes Hölzl** it's your turn: https://github.com/leanprover-community/mathlib/commit/b0592fe97e74ef4e9af8158052d30053914d639b

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134970540):
I'm sure you'll find better names :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134975072):
I find these conversations very interesting. Patrick is absolutely right from a mathematical point of view. Grothendieck stressed that the arrows were more important than the objects. People talked about geometric objects being smooth but Grothendieck argued that the correct definition was that of a map being smooth, and an object being smooth just meant that the map from this object to the one point set was smooth. On the other hand Johannes thinks about mathematics in a completely different way. Do people properly understand how Grothendieck's ideas should influence type theory?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134989929):
Hum, I built a ring structure on the separation quotient of a topological ring, but forgot to prove that it's a *topological* ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134989951):
I'll need that projection on a quotient group is open

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134989996):
Do we have open maps in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 01 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134990070):
Don't think so, there's `embedding_open` I think which says that an embedding of an open subspace is an open map, but just spelled out explicitly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134990159):
I'm not sure how to get back the fact that addition on a group quotient group is defined by `quotient.lift`. Should I `dunfold` until I see it or is there a better way?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 01 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991135):
use `show`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991253):
`dsimp` could also help.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991543):
I'm completely lost in our maze of quotient structures. Do we have the quotient of a commutative additive group by a subgroup? Is it related in anyway with quotient rings? Or should I be doing topological modules?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991736):
`quotient_add_group.add_group` (https://github.com/leanprover/mathlib/blob/master/group_theory/quotient_group.lean#L46)
is for normal subgroups, but as far as I understand a normal subgroup is just a subgroup in the commutative case?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991739):
yes, every group is normal in this case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991843):
so you can use `quotient_add_group`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991886):
Ah there is also `quotient_add_group.add_comm_group` it is just not setup as an `instance`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991969):
What about https://github.com/leanprover/mathlib/blob/master/group_theory/quotient_group.lean#L53?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134991981):
It looks good but I haven't managed to use it yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134992188):
Yes, that's it, but the multiplicative version. Afterwards the additive version is derived (line 63). But for the additive version the instance attribute is missing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134992244):
Oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134992526):
Now it seems to work without the attribute, strange...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134992763):
maybe its somewhere else?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134992978):
I need to stop for today, but at least I have some statement:
```lean
import analysis.topology.topological_structures

variables {α : Type*} [add_comm_group α] [topological_space α]

instance [topological_add_group α] (N : set α) [is_add_subgroup N]: topological_space (quotient_add_group.quotient N) :=
by dunfold quotient_add_group.quotient ; apply_instance

instance [topological_add_group α] (N : set α) [is_add_subgroup N]: topological_add_group (quotient_add_group.quotient N) :=
{ continuous_add := sorry,
  continuous_neg := sorry}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/134993038):
I wasn't able to get to the point where I can simply use continuity of lifts of continuous functions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 02 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135019838):
@**Patrick Massot**  fyi, I rebased the branch. So pull the new branch before continuing on it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135113983):
I tried to return to this topological quotient group, but I still have no idea how to unfold the definition of addition on the quotient. It uses a mysterious `quotient.lift_on2'` that I can't reach, even using change. The MWE is:
```lean
import analysis.topology.topological_structures
import group_theory.quotient_group

variables {α : Type*} [add_comm_group α] [topological_space α]
  [topological_add_group α] (N : set α) [is_add_subgroup N]

instance [topological_add_group α] (N : set α) [is_add_subgroup N]: topological_space (quotient_add_group.quotient N) :=
by dunfold quotient_add_group.quotient ; apply_instance

instance : topological_add_group (quotient_add_group.quotient N) :=
{ continuous_add := sorry,
  continuous_neg := sorry}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 03 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135114738):
@**Patrick Massot** Do you have a strategy in mind?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 03 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135114755):
Which ingredients would you want to apply?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 03 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135114869):
My guess would be that you first need to turn the addition into a map `quot × quot → quot`, then identify `quot × quot` with an appropriate quotient. And then apply some lemma about the universal property of quotients and continuous maps

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 03 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135114874):
Of course this is very vague...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 03 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135115571):
So, `quotient.lift_on2'` is just  `quotient.lift_on2` using a implicit parameter instead of a type class parameter. If this helps...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 03 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135118401):
I think the math strategy is to start with a commutative square involving the multiplication $$G \times G \to G$$ and the multiplication $$G/H \times G/H \to G/H$$. Right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 03 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135118531):
Where the vertical maps are $$q \times q$$ and $$q$$ where $$q : G \to G/H$$ is the quotient map. I think the fact that that square commutes is a definitional equality (for each pair $$(g_1, g_2) \in G \times G$$). So you should not have to unfold the definition of the product in $$G/H$$ if that is correct.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 03 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135118773):
@**Patrick Massot** the fact that `quotient_group.mk` is a `group_hom` should mean that you don't need to unfold mul. The proof that it is a `group_hom` is just `rfl` anyway, so everything's definitionally equal to what you want it to be.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 03 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135119108):
The point is that the multiplication on the quotient is ultimately defined in terms of `quot.lift`, and `quot.lift` applied to something made from `quot.mk` reduces.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 03 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135119477):
Ok, so first of all we need to know that the quotient map is ctu. Is this already there?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 03 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135120140):
Assuming "ctu" = continuous then `continuous_quot_mk`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 03 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135120393):
By the way, this one is not simply a formal consequence of the universal property of the quotient, because the product of two quotient maps is not in general a quotient map (although in this case I guess it probably is)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 03 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135120428):
For `continuous_neg`, you can argue along those lines.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135124484):
Sorry, I was away. Indeed the quotient projection is continuous, and addition is continuous, so I want to use https://github.com/leanprover/mathlib/blob/c1f9f2e2977c0f6cb1cfd949bee8c3817cce0489/analysis/topology/continuity.lean#L811 applied to quotient.mk \circ addition. My problem is to get Lean to swallow that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135124910):
oh maybe I misunderstood. Do you mean I could use https://github.com/leanprover/mathlib/blob/c1f9f2e2977c0f6cb1cfd949bee8c3817cce0489/analysis/topology/continuity.lean#L383?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135124969):
lemma quotient_map.continuous_iff {f : α → β} {g : β → γ} (hf : quotient_map f) : continuous g ↔ continuous (g ∘ f)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135125165):
I'm waiting for mathlib to compile...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 03 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135125502):
Is `continuous_quot_mk` the right `quot_mk`? I see no mention of groups anywhere around it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135125527):
The topology on the quotient group is the quotient topology (I hope)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 03 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135127345):
You can't use `continuous_quotient_lift` or `quotient_map.continuous_iff` because $$G/H \times G/H$$ is not (obviously) a quotient of $$G \times G$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 03 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135127429):
I thought you were doing the proof which goes like: $$q$$ is an open map (because $$q^{-1}(q(U))$$ is a union of translates of $$U$$, hence open), so $$q \times q$$ is an open map, and then you can check that the preimage of an open subset of $$G/H$$ under multiplication is again open by chasing around the square

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135127544):
Indeed this is what I wanted to do the other day (I even asked whether we have a definition of open maps in mathlib) and then I forgot what I was doing...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135127598):
But I guess the map from $$G \times G$$ to $$G/H \times G/H$$ should still be a quotient map

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135127616):
I need to think on paper

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135128893):
I decided that every proof will need to first prove that $$G \to G/H$$ is open anyway.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135128980):
why do I feel like I've proved that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135128997):
I'd be very interested

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129011):
Do you remember if this is in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129246):
```lean
def topological_group.coinduced {α : Type u} {β : Type v}
  [t : topological_group α] [group β]
  (f : α → β) [is_group_hom f] (hf1 : function.surjective f)
  (hf2 : ∀ S, is_open S → is_open (f ⁻¹' (f '' S))) :
  topological_group β :=
```
`hf2` seems to say that it is an open map

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129261):
```lean
instance quotient_group.topological_group (G : Type u)
  [topological_group G] (N : set G) [normal_subgroup N] :
  topological_group (left_cosets N) :=
by letI := left_rel N; from
topological_group.coinduced quotient.mk quotient.exists_rep (λ S hs,
have (⋃ x : {x // ⟦x⟧ = 1}, (λ y, x.1 * y) ⁻¹' S)
    = quotient.mk ⁻¹' (quotient.mk '' S),
  from set.ext $ λ z,
  ⟨λ ⟨S, ⟨⟨g, h1⟩, rfl⟩, h2⟩, ⟨g * z, h2,
    by rw [is_group_hom.mul quotient.mk, h1, one_mul];
    from quotient_group.is_group_hom _⟩,
  λ ⟨g, h1, h2⟩, ⟨_, ⟨⟨g * z⁻¹,
    by rw [is_group_hom.mul quotient.mk, h2, is_group_hom.inv quotient.mk, mul_inv_self];
    repeat { from quotient_group.is_group_hom _ }⟩, rfl⟩,
    by simp [h1]⟩⟩,
this ▸ is_open_Union $ λ x : {x // ⟦x⟧ = 1},
continuous_mul continuous_const continuous_id _ hs)
```
so this consistutes a proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129329):
https://github.com/kckennylau/local-langlands-abelian/blob/master/src/topological_group.lean#L205-L221

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129383):
@**Patrick Massot** is this what you want?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129407):
it looks very much like what I want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129453):
nice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129455):
I mean the statement of course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129475):
I mean, it's not hard to prove

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129481):
the proof...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129505):
a first year could learn that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129530):
the math proof is easy yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129603):
reading a term mode proof is hard (for me)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129613):
this proof is 3 months old btw

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129722):
I will need to redo it in my context and state intermediate lemmas for reuse anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129734):
but it's still helpful to have one full proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129752):
ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129831):
thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135129991):
Did you think about PRing stuff from this repo?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 03 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135130001):
maybe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 03 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135130577):
Remember your work is lost if you don't PR it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 04 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135155155):
The first key thing we need from Kenny's repo is algebraic closure, and it's not in there yet. Kenny is waiting for module refactoring because the argument needs loads of ideals over loads of rings.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 04 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135155166):
After that we need to take a level-headed look at how much is appropriate for mathlib and how much really just a wacky independent project

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 04 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/separated%20quotient/near/135155170):
(and I don't know what the conclusion will be)


{% endraw %}
