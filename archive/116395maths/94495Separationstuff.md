---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/94495Separationstuff.html
---

## Stream: [maths](index.html)
### Topic: [Separation stuff](94495Separationstuff.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134237694):
@**Johannes Hölzl** I'm working on uniform spaces again, and I have a couple of question. 
* First, at https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_space.lean#L638-L640 the comment mentions two possible definitions of T1 spaces. Am I right to think the equivalence of those definitions is not in mathlib?
* Bourbaki defines separated uniform spaces as uniform spaces whose underlying topology is T2. You define them in terms of the separation relation, and prove the underlying topological space is T2. But you don't prove the converse implication, do you?
* When trying to prove the converse implication on paper, I get that T1 underlying topology is enough. Is this fishy? Or is it only that topologies coming from uniform structures are special and T1 implies T2 (and regular)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 19 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134239354):
T1 implies T2 for uniform spaces should be the same epsilon/2 as shows metric spaces are T2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 19 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134239449):
Uh, on my phone and apparently can't form complete sentences but I guess you understand what I mean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134239563):
Indeed it looks very plausible, but I wanted to check with our local expert before starting to Lean it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134240553):
I now have a really detailed paper proof of the fact that the group uniform structure on the completion of a group is the same as the completion of the group uniform structure. I have about 15 lemmas to state and prove in Lean. I'm really afraid because lots of them involve different uniform structures on the same type, and I don't know how to fight the type class resolution system here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134253310):
Ok, I decided to start with a lemma which is independent of all the group theory stuff and openly involves different uniform structures on the same type. 
```lean
import analysis.topology.uniform_space
open set

variables {α : Type*} {β : Type*}

lemma uniform_continuous_id_of_emb [uniform_space α] (u u' : uniform_space β) (top : u.to_topological_space = u'.to_topological_space)
  {e : α → β} (ue : @uniform_embedding _ _ _ u e) (dense : ∀x, x ∈ closure (range e))
  (h : @uniform_continuous _ _ _ u' e) :  u ≤ u' :=
begin
  let e₀ := (ue.dense_embedding dense).extend e,
  
  sorry
end
```
As expected, lots of @/_ flying around. First surprise: how does Lean accepts the `dense` hypothesis? Where does it get a topology on beta? I was expecting to need to need @ here, pick at random from `u` to `u'` and then use the `topo` hypothesis in the proof. And then Lean complains when I define `e₀`: `synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized u' inferred u`. Here I want to use uniform structure `u`. How can I proceed?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259187):
Any hint about this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259425):
first observation: in `dense`, the type class instances find somehow `u'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259461):
For some reasons it also uses non-type class parameters...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259548):
Yes, this is what confuses me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259575):
the type class inference will use `u` if you swap `u'` and `u`. then `u` will be used in `dense`, and `e₀` works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259585):
but this is surely not reliable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259601):
Of course square brackets are meant to indicate how these arguments will be supplied when applying the lemma. But somehow I thought they also indicated what to put in the type class system for immediate use in following arguments

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259626):
I thought about swapping, but I wanted a robust solution

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259705):
And , while you're here, this thread starts with three questions for you...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259709):
to have it robust you need to use the `@...` notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259913):
My son requires me, you have some extra thinking time :smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259939):
1) heh, the comment is the wrong way around. All we have specifically for T1 is the three theorem below the `class`.  So AFAIR: no this equivalence is not in mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259948):
```lean
import analysis.topology.uniform_space
open set

variables {α : Type*} {β : Type*}

--set_option trace.class_instances true
lemma uniform_continuous_id_of_emb (u : uniform_space β) 
 : false :=
begin
  have u' : uniform_space β := by apply_instance, -- works??
--  have : u = u' := rfl, -- fails??
  sorry
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134259975):
this is horrible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260041):
2) no the converse is not proved

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260187):
3) Reid's comment makes sense to me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 19 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260195):
@**Kevin Buzzard** you used have instead of let.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260216):
thank goodness for that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260225):
and not for the first time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260341):
@**Patrick Massot**  do you work with: **I. M. James: Topologies and Uniformities**? This is what I used to formalize most of uniform spaces.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260347):
```lean
import analysis.topology.uniform_space
open set

variables {α : Type*} {β : Type*}

lemma uniform_continuous_id_of_emb [uniform_space α] (u u' : uniform_space β) 
 : false :=
begin
  let βtop : topological_space β := by apply_instance, -- ??
  have : βtop = @uniform_space.to_topological_space β u' := rfl,
  sorry
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260400):
So as Johannes says, type class inference picks up `u'` and it's not clear why

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260910):
```quote
How can I proceed?
```
Well we now see the problem; type class inference succeeds when it shouldn't, so...

```lean
import analysis.topology.uniform_space
open set

variables {α : Type*} {β : Type*}

lemma uniform_continuous_id_of_emb [uniform_space α] (u u' : uniform_space β) (top : u.to_topological_space = u'.to_topological_space)
  {e : α → β} (ue : @uniform_embedding _ _ _ u e) (dense : ∀x, x ∈ @closure β (u.to_topological_space) (range e))
  (h : @uniform_continuous _ _ _ u' e) :  u ≤ u' :=
begin
  let e₀ := @dense_embedding.extend _ β β _ (u.to_topological_space) e (u'.to_topological_space)
    (@uniform_embedding.dense_embedding _ _ _ u _ ue dense) e,

  sorry
end
```

I don't know what you're complaining about :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260981):
Did you steel Scott's monitor?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 19 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260988):
Those lines are way too long. :rolling_on_the_floor_laughing:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134260990):
Here is a possible workaround: use beta and gamma with an equiv, let u be the uniform structure on beta and u' on gamma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261001):
```quote
Those lines are way too long. :rolling_on_the_floor_laughing:
```
I even halved the longest one!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261022):
and then you won't get the problems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261028):
and you can just push forward and pull back the uniformities.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261100):
This might actually work. But of course the question still remains as to how type class inference is stealing your uniformities. This is very funny. It's *exactly* the opposite of the complaint most of my student have -- "I can see it in the local context, how come Lean doesn't know why R is a ring?"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261241):
ah yes, when you move the parameters `u` and `u'` to the right side of `:`, then it doesn't work anymore:
```lean
lemma uniform_continuous_id_of_emb [uniform_space α] :
  ∀(u u' : uniform_space β) (top : u.to_topological_space = u'.to_topological_space)
  {e : α → β} (ue : @uniform_embedding _ _ _ u e)
  (dense : ∀x, x ∈ closure (range e)) -- fails here
  (h : @uniform_continuous _ _ _ u' e), u ≤ u' := ...
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261338):
So when Leo said only stuff to the left of the colon could be used for type class inference, I didn't realise he meant that even stuff which we didn't want to use would get used...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261347):
Is this just for uniform spaces or does everything do this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261357):
I guess everything?!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261372):
maybe only things which are marked as `@[class]`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261392):
```lean
lemma test (α : Type) (u : ring α) : false :=
begin
  let v : ring α := by apply_instance,
  -- who knew that this worked??
  have : u = v := rfl,
  sorry 
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261407):
Is this a bug??

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 19 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261471):
I'm confused, why is this a surprise

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 19 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261498):
you asked for an instance, it found one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261505):
Patrick, even though Johannes has pointed out a fix, the more I think about the gamma trick the more I think you should consider it seriously. Then you can just use type class inference for beta with u and gamma with u', and deduce the actual thing you want afterwards with a minimal amount of `@`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261512):
I just had absolutely no idea that it would look there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 19 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261523):
isn't that where it normally looks?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261535):
I thought there was the square bracket stuff and the round bracket stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261541):
and it only looked in the square bracket stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 19 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261591):
Ah, I see. The square bracket only affects users of the theorem, it doesn't matter what you mark it when it's in the context

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 19 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261614):
the only thing that matters inside the theorem is whether the head constant is a `@[class]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261627):
I see!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261666):
Hm, this is also news to me!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261709):
In which case Patrick I think this is an even bigger indication that you should just work with two different types and maps between them, and in the application make the types the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261780):
Hopefully this solves some blockages higher up the chain of problems as well. I didn't know things worked like this, and presumably Patrick didn't either -- but I do remember him saying that he could not actually solve some problems with type classes because he could not direct his instances in the right direction. This will hopefully clear a lot of stuff up.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261857):
I also think it is a good idea to use two types and a uniform equivalence between them. The annoying this is: this may force you to prove for a lot of constants, that they are invariant under equivalences

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261869):
I guess the reason many users didn't notice this is simply because it is very rare to actually have two terms of type `foo X` with `foo` a class, which you actually want to be distinct; usually users are wrestling to prove that they are the equal, not the other way around.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261902):
yes, type classes work so well, exactly for this reason: if you assume two different structures, you usually have two different types

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134261948):
```quote
I also think it is a good idea to use two types and a uniform equivalence between them. The annoying this is: this may force you to prove for a lot of constants, that they are invariant under equivalences
```
@**Simon Hudon** This is back to transport de structure. Deligne emphasized this concept in his IAS lecture last week.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134262036):
Patrick is about to need the fact that if he has `h : equiv X Y` and a topological space structure on X, then all topology-like theorems he proves for X should have an analogue for Y obtained by mapping and co-mapping along h.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134262303):
we need to extensions of `equiv`: `continuous_equiv` and `uniform_equiv`. We also assume a topological structure on `Y` (it may be the one induced by `h`, but this shouldn't be necessary def-equal)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 19 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134262810):
isn't `continuous_equiv` just `homeo`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134262868):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134263238):
I feel like we have taken a big step forward here though. My solution with long lines would have been hell and Patrick was complaining some time ago that he could not control his instances. I realised the other reason that this phenomenon was not well known -- if you have a term whose type is a class, 99% of the time you put it in square brackets in the statement of a theorem or definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134263651):
I'm back. Thanks everybody for your work on this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134263681):
I'm not sure I'm buying the two types solutions. The problem is that I'm not intersted in this lemma in isolation, it's a tiny step in a much bigger proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134263692):
So I'll actually need to apply this lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 19 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134264311):
@**Kevin Buzzard**: @**Johannes Hölzl** keeps pointing out that `transport` overlaps with his `transfer` machinery. I think it would be worth checking if `transfer` solves your problems right out of the box.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134264380):
it doesn't solve them right out of the box. It still requires quite some infrastructure. But I think it is less work to extend `transfer` than to implement a `transport`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134265117):
I would like to hear much more about what is going on here. I don't know what either of these words are. Are they tactics? I remember having a lot of fun working towards `transport`. Maybe we have an actual use case here. Presumably Johannes in his message above has pinpointed exactly what we need in this situation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134265223):
Patrick if you try and prove the lemma using just one beta then you have an @ nightmare. If you prove it using beta and gamma then you have a different problem which might be easily solvable and furthermore your lemma will be a more general result. You can get the lemma you want by applying the more general one in the case beta = gamma and then you are only in @ hell for a few lines

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134265278):
I think this is a very important topic, so I'll probably try a couple of solutions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134265294):
I still need to know how I can use my "same topology hypothesis" to deduce that the range of e is dense for for topologies

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134265322):
This is very much like how transport de structure works in Galois theory. You first do it with an isomorphism X = Y and then apply it with X=Y but the isomorphism not equal to the identity and you deduce something which might look like a nontrivial computation with no work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Sep 19 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134265376):
`transfer` is a tactic, used in core lean to prove various properties of integers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134265497):
Kevin, you heard about it in Orsay

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134265731):
Oh I remember! I hadn't put two and two together.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134266139):
This fight against @ is epic. Did I tell you I forgot to assume both uniformities on β are complete and separated?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134266198):
I tried to cut my proof into so many tiny lemmas that I forgot to copy-paste a couple of assumptions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134266574):
`set_option pp.all true` is my only ally

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134266643):
`rewrite tactic failed, motive is not type correct nested exception message: check failed, application type mismatch (use 'set_option trace.check true' for additional details)` is my enemy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134266705):
Now I am confused about why something which transfers proofs from N x N to Z can help. I think I need to think about how transfer actually works. But with the beta gamma approach there are no @s at all and you can just use type class inference as usual.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134266720):
In fact I would be tempted to see how much you can do with beta not assumed equal to gamma and not ever prove anything with beta = gamma unless you absolutely have to.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134266778):
You can try to prove the lemma if you want (without forgetting to assume both structures on target are complete and separated)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134266850):
`transfer` doesn't require an equivalence, just a relation and proofs about terms related terms. That's how proofs about `Z` can be reduced to proofs about `N x N`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267045):
I guess I would need to know the maths statement and proof...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267138):
Here is the real world story (using A and B instead of greek letters for typing convenience). We have A with a fixed uniform structure, and B with two complete separated uniform structure u and u', which induce the same topology on B. We have e : A to B which is a uniform embedding into (B, u) with dense image. We assume e is uniformly continuous from A to (B, u'). Hence it can be extended by continuity to some uniformly continuous e0 from (B, u) to (B, u'). Since e0 \circ e = e, we learn the e0 is the identity on the image of e. But the later is dense, so by continuity, e0 = Id. So we learned that Id is uniformly continuous from (B, u) to (B, u'), QED.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267191):
As is often the case, the paper I have in front of me contains only an annotated commutative diagram.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267273):
Can we work on this together at cocalc (possibly at different times)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267286):
or is it easier just to spam the chat with gists?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267302):
Here my full Lean so far:
```lean
import analysis.topology.uniform_space

open set
variables {α : Type*} {β : Type*}

def unif_emb {α : Type*} {β : Type*} (u_α : uniform_space α) (u_β : uniform_space β) (f : α → β) : Prop :=
uniform_embedding f

def unif_cont {α : Type*} {β : Type*} (u_α : uniform_space α) (u_β : uniform_space β) (f : α → β) : Prop :=
uniform_continuous f

def top (u : uniform_space α):= u.to_topological_space 

def complete (u : uniform_space α) := complete_space α

def hausdorff (u : uniform_space α) := separated α

set_option pp.all true
lemma uniform_continuous_id_of_emb [uα : uniform_space α] (u' u : uniform_space β) 
  [cu : complete u] [hu : hausdorff u] [cu' : complete u'] [hu' : hausdorff u'] (htop : top u = top u')
  {e : α → β} (ue : unif_emb uα u e) (dense : ∀x, x ∈ closure (range e))
  (h : unif_cont uα u' e) :  u ≤ u' :=
begin
  let e₀ := (ue.dense_embedding dense).extend e,
  haveI : separated β := hu, 
  have : unif_cont u u' e₀,
  { dsimp [unif_cont, e₀],
    have := @uniform_continuous_uniformly_extend β α β u uα u' e ue dense e h cu' hu',
    dsimp [top] at htop,
    
    sorry },
  
  sorry
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267307):
I am trying to help my daughter with biology homework, clean the kitchen, eat some dinner and prove a lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267315):
A CoCalc effort would probably be fun

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267377):
As you can see, I tried to hide a bunch of @ in new definitions which simply change binders

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267413):
The bad side is we need `dsimp` then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 19 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267624):
That real world proof looks applicable where the types are different. The only tricky bit is "generating the same topology", but I think this just means that the equiv is a quotient map (in the topological sense)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267625):
The relevant part of state is then
```lean
this :
  @uniform_continuous.{u_2 u_2} β β u u'
    (@dense_embedding.extend.{u_1 u_2 u_2} α β β (@uniform_space.to_topological_space.{u_1} α uα)
       (@uniform_space.to_topological_space.{u_2} β u)
       e
       (@uniform_space.to_topological_space.{u_2} β u')
       (@uniform_embedding.dense_embedding.{u_1 u_2} α β uα u e ue dense)
       e),
htop :
  @eq.{u_2+1} (topological_space.{u_2} β) (@uniform_space.to_topological_space.{u_2} β u)
    (@uniform_space.to_topological_space.{u_2} β u')
⊢ @uniform_continuous.{u_2 u_2} β β u u'
    (@dense_embedding.extend.{u_1 u_2 u_2} α β β (@uniform_space.to_topological_space.{u_1} α uα)
       (@uniform_space.to_topological_space.{u_2} β u)
       e
       (@uniform_space.to_topological_space.{u_2} β u)
       (@uniform_embedding.dense_embedding.{u_1 u_2} α β uα u e ue dense)
       e)
```
So it looks like `rwa htop at this` should close the goal, but I get a that nasty error instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267727):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267732):
Here is the version which is written in what I believe is the correct generality (using A and B and C instead of greek letters for typing convenience). We have A, B, C uniform spaces, with B and C uniform and complete, and a homeo j : B -> C.  We have e : A to B which is a uniform embedding into B with dense image. We assume j circ e is uniformly continuous from A to C. Hence it can be extended by continuity to some uniformly continuous j' from B to C. Since j = j' on e(A), j = j' and hence j is uniformly continuous from B to C, QED *without a single @*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267846):
I'll try to prove that tomorrow, but I fear this is only pushing the pain to the moment I will need to apply the lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 19 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267863):
we need the theorem that `id` is uniformly continuous from `u` to `u'` iff `u <= u'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 19 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267879):
that is the only part that really needs `@` work, and the proof is trivial using `map_id` on filters

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267939):
Sure, we need this id stuff.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134267956):
But I don't understand the next sentence

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268016):
And I don't understand why rewrite doesn't work in my attempt.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268122):
uniform continuity works on pairs of function, i.e. you need to prove `(λx:α×α, (x.1, x.2)) = id`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268196):
and then unfold `uniform_continuity` and rewrite with this equality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268304):
Sure, but this is completely orthogonal to my problem, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268321):
I'm far away from having that id is uniformly continuous here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268507):
Do we have homeomorphisms in the strong sense of a continuous equiv with a continuous inverse?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268530):
no :(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268631):
https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/homeos.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268639):
Would you like to get this in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268698):
I need to go sleeping, but don't hesitate to unblock this. I hope I could then imitate the solution in many other such lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134268794):
Patrick here is the statement with beta ne gamma:
```lean
lemma uniform_continuous_id_of_emb' [uα : uniform_space α] [uniform_space β] [uniform_space γ]
  [complete_space β] [separated β] [complete_space γ] [separated γ] (j : equiv β γ) -- need cts
  {e : α → β} (ue : uniform_embedding e) (dense : ∀x, x ∈ closure (range e))
  (h : uniform_continuous (j ∘ e)) :  uniform_continuous j := sorry
```
I had to use none of your five binder-changing defs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269048):
Weird! My rewrite now works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269054):
I wanted to try one more time. I have no idea what changed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269137):
Thanks Kevin. I'll definitely try this road tomorrow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 19 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269145):
But, as I wrote earlier, I think it's important enough that I try several things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269235):
wait, does the statement hold at all?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269249):
How do you want to prove it? (ah, reading your previous description)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269434):
```lean
  have : unif_cont u u' e₀,
  { dsimp [unif_cont, e₀],
    have := @uniform_continuous_uniformly_extend β α β u uα u' e ue dense e h cu' hu',
    dsimp [top] at htop,
    rwa [htop] {occs := occurrences.pos [2]} },
```
the have can be proved fixing the occurence. I guess the `e₀ = id` proof doesn't mention any uniformities?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269643):
Oh -- I should add that my formalisation is not quite correct because the `equiv` should be a `homeo`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269735):
Hmm, we seem to need the theorem that `id` is uniformly continuous from `u` to `u'` iff `u <= u'`. But I would rather prove a statement that an equiv is uniformly continuous iff some pushforward of a uniformity is `<=` the other one. Is this already in Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134269997):
this holds by definitional equality. EDIT: no, it doesn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134270448):
```lean
def unif_cont {α : Type*} {β : Type*} (u_α : uniform_space α) (u_β : uniform_space β) (f : α → β) : Prop :=
uniform_continuous f
```
Is this OK if alpha = beta? I'm not so sure. I think type class inference chooses the same uniform structure twice. @**Patrick Massot** I think there's a bug here. Thoughts anyone?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134270861):
```lean
lemma uniform_continuous_iff {α β} [uα : uniform_space α] [uβ : uniform_space β] (f : α → β):
  uniform_continuous f ↔ uβ.comap f ≤ uα :=
filter.map_le_iff_le_comap
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 19 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134271113):
@**Kevin Buzzard** the content of `unif_cont` is fully elaborated. The elaborator doesn't do a type class search when it is used in `uniform_continuous_id_of_emb`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134271209):
Oh I see. So it's Ok.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134271228):
As you can see, I am still coming to terms with my new knowledge about how typeclass inference works. Patrick -- sorry -- it's Ok.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134271543):
Patrick's version --
```lean
lemma uniform_continuous_id_of_emb [uα : uniform_space α] (u' u : uniform_space β)
  [cu : complete u] [hu : hausdorff u] [cu' : complete u'] [hu' : hausdorff u'] (htop : top u = top u')
  {e : α → β} (ue : unif_emb uα u e) (dense : ∀x, x ∈ closure (range e))
  (h : unif_cont uα u' e) :  u ≤ u' :=
```
Should the conclusion be `u' <= u`? I'm not an expert in uniform spaces.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 19 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134271658):
I ask because Patrick seemed to be saying that the conclusion was that id was continuous from u to u', and Johannes seems to want to conclude from this that `u' <= u`. But this could easily be some situation where `<=` is defined as `>=` for some people (as far as I know)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134272056):
There is no `uniform_space.comap_id` :-(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134274017):
gaargh there seems to be no `ext`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134274344):
`⊢ u' = uniform_space.comap id u'`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134275140):
```quote
```lean
  have : unif_cont u u' e₀,
  { dsimp [unif_cont, e₀],
    have := @uniform_continuous_uniformly_extend β α β u uα u' e ue dense e h cu' hu',
    dsimp [top] at htop,
    rwa [htop] {occs := occurrences.pos [2]} },
```
```
With the gamma version it's just

```lean
  let e₀ := (ue.dense_embedding dense).extend (j ∘ e),
  have : uniform_continuous e₀,
  { dsimp [unif_cont, e₀],
    exact uniform_continuous_uniformly_extend ue dense h,
  },
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134275198):
Everything is easier this way, switching to gamma is a no-brainer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134275275):
```lean
import analysis.topology.uniform_space

open set
variables {α : Type*} {β : Type*} {γ : Type*}

lemma uniform_continuous_id_of_emb' [uniform_space α] [uniform_space β] [uniform_space γ]
  [complete_space β] [separated β] [complete_space γ] [separated γ] (j : equiv β γ) -- need continuity assumption
  {e : α → β} (ue : uniform_embedding e) (dense : ∀x, x ∈ closure (range e))
  (h : uniform_continuous (j ∘ e)) : uniform_continuous j := 
begin
  let e₀ := (ue.dense_embedding dense).extend (j ∘ e),
  have : uniform_continuous e₀,
  { dsimp [e₀],
    exact uniform_continuous_uniformly_extend ue dense h,
  },
  sorry -- I need that j is a homeo and this isn't in the assumptions
end
```
but it's bedtime now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134275281):
and we need to say that `j` is a homeo not just an equiv.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134275359):
```lean
lemma uniform_continuous_iff {α β} [uα : uniform_space α] [uβ : uniform_space β] (f : α → β):
  uniform_continuous f ↔ uβ.comap f ≤ uα :=
filter.map_le_iff_le_comap

def unif_emb {α : Type*} {β : Type*} (u_α : uniform_space α) (u_β : uniform_space β) (f : α → β) : Prop :=
uniform_embedding f

def unif_cont {α : Type*} {β : Type*} (u_α : uniform_space α) (u_β : uniform_space β) (f : α → β) : Prop :=
uniform_continuous f

def top (u : uniform_space α):= u.to_topological_space

def complete (u : uniform_space α) := complete_space α

def hausdorff (u : uniform_space α) := separated α

lemma uniform_continuous_id_of_emb [uα : uniform_space α] (u' u : uniform_space β)
  [cu : complete u] [hu : hausdorff u] [cu' : complete u'] [hu' : hausdorff u'] (htop : top u = top u')
  {e : α → β} (ue : unif_emb uα u e) (dense : ∀x, x ∈ closure (range e))
  (h : unif_cont uα u' e) :  u' ≤ u :=
begin
  have H : unif_cont u u' id := @uniform_continuous_id_of_emb' α β β uα u u' cu hu cu' hu' (equiv.refl β) e ue dense h,
  unfold unif_cont at H,
  rw uniform_continuous_iff at H,
  convert H,
  -- ⊢ u' = uniform_space.comap id u'
  -- should be trivial?
  sorry
end 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134275590):
`  have : uniform_continuous e₀ :=
    uniform_continuous_uniformly_extend ue dense h,`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291887):
Indeed it seems the following is missing:
```lean
lemma id_prod : (λ (p : α × α), (p.1, p.2)) = id :=
by ext ; simp

attribute [extensionality] uniform_space_eq

lemma uniform_space_comap_id {α : Type*} : uniform_space.comap (id : α → α) = id :=
begin
  ext u,
  dsimp [uniform_space.comap],
  rw [id_prod, filter.comap_id]
end
```
The first one is strange, but I couldn't find it @**Johannes Hölzl** any thought?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291938):
Should we add this to mathlib? make the first one a simp lemma?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 20 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291941):
you mean `id_prod`? I don't think we have it yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291947):
Yes, id_prod

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291951):
I feel like a child collecting football cards again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291955):
great excitement when we discover a new basic lemma we don't have

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291967):
simp or not simp?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 20 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291968):
I guess we will never run out of basic lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 20 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291971):
currently I'm in favor of not simp

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291975):
I ran out of football cards once; I remember the joy of getting the last one. Bryan Flynn, Leeds United.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 20 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134291976):
I don't think we have a lot of eta-rule like these in the simp-set. And it might get confusing. But then this rule is quiet nice...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134292015):
But I thought we would ultimately find that every basic lemma is either easy or has a tactic-free and simple proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134292016):
What about tagging uniform_space_eq?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 20 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134292107):
yes, `uniform_space_eq` should be tagged with `@[extensionality]`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134292424):
Ok, I first PR'ed id_prod, then I'll do the other two

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 20 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134292533):
just waiting for Travis

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316246):
Quick update on this topic: mathlib got https://github.com/leanprover/mathlib/commit/d0f1b21a9df64f48a8d28203bf292eb80e05a6da and https://github.com/leanprover/mathlib/commit/1da8cc51854c2e75f456878b195b162dc8dbb130 then I added https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/homeos.lean to the perfectoid project (I think I still don't whether mathlib wants it). We can then write the two versions of the lemma (following my real life sketch and Kevin's Lean  start) as:
```lean
open set
variables {α : Type*} {β : Type*} {γ : Type*}

lemma uniform_continuous_id_of_emb' [uniform_space α] [uniform_space β] [uniform_space γ]
  [complete_space β] [separated β] [complete_space γ] [separated γ] (j : homeo β γ)
  {e : α → β} (ue : uniform_embedding e) (dense : ∀x, x ∈ closure (range e))
  (h : uniform_continuous (j ∘ e)) : uniform_continuous j :=
begin
  let e₀ := (ue.dense_embedding dense).extend (j ∘ e),
  have uc_e₀ : uniform_continuous e₀,
  { dsimp [e₀],
    exact uniform_continuous_uniformly_extend ue dense h },
  convert uc_e₀,
  ext b,
  have closed : is_closed {b : β | j b = e₀ b} := (is_closed_eq j.fun_con uc_e₀.continuous),
  have dense' : closure (range e) = univ, by rwa eq_univ_iff_forall,
  apply is_closed_property dense' closed (λ a, eq.symm $ uniformly_extend_of_emb ue dense h)
end

def unif_emb {α : Type*} {β : Type*} (u_α : uniform_space α) (u_β : uniform_space β) (f : α → β) : Prop :=
uniform_embedding f

def unif_cont {α : Type*} {β : Type*} (u_α : uniform_space α) (u_β : uniform_space β) (f : α → β) : Prop :=
uniform_continuous f

def top (u : uniform_space α):= u.to_topological_space

def complete (u : uniform_space α) := complete_space α

def hausdorff (u : uniform_space α) := separated α

lemma uniform_continuous_id_of_emb [uα : uniform_space α] (u' u : uniform_space β)
  [cu : complete u] [hu : hausdorff u] [cu' : complete u'] [hu' : hausdorff u'] (htop : top u = top u')
  {e : α → β} (ue : unif_emb uα u e) (dense : ∀x, x ∈ closure (range e))
  (h : unif_cont uα u' e) :  u' ≤ u :=
begin
  let iduu' : @homeo β β (top u) (top u') :=
  { to_fun := id,
    inv_fun := id,
    left_inv := λ x, rfl,
    right_inv := λ x, rfl,
    fun_con := by rw ←htop; exact continuous_id,
    inv_con := by rw ←htop; exact continuous_id },

  rw show e = iduu' ∘ e, by refl at h,
  have H := @uniform_continuous_id_of_emb' α β β uα u u' cu hu cu' hu' iduu' e ue dense h,

  rw uniform_continuous_iff at H,
  convert H,
  rw show (iduu' : β → β) = id, by refl,
  simp [uniform_space_comap_id]
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316471):
Of course the first proof has no @, we are not fighting mathlib here. The second one is not too bad in my opinion. The statement is clean, because of the "rebinded" definitions, which cost nothing in the proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316535):
The main @ thing is the definition of the identity seen as a homeo between different topologies, which costs two slightly awkwards `rw show ..., by refl`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316601):
What do you guys think about all this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316684):
I think the identity homeo should be a theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316753):
Stating what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316771):
just like the theorem that identity is continuous iff the topologies are le, the identity is a homeo iff the topologies are eq

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316811):
This bundled definition of a homeo doesn't seem so nice when it comes to stating that some map is a homeo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316836):
this is true. Maybe settle for one direction, the one you proved

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316920):
The reverse direction says that if `f : homeo A A T1 T2` and `f x = x` for all `x`, then `T1 = T2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316930):
So it would be a `def`, not a `lemma`, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134316939):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317018):
After all this refactoring, I would ask whether you really need `uniform_continuous_id_of_emb` though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317045):
we treated it as the endgame but maybe you can avoid le on uniformities to begin with

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317110):
I was wondering the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317111):
Of course this is also a legitimate question. But this thread is also used as an exercise in type class hell survival.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317153):
Patrick's original question was whether the completion of a top group "equalled" (in a mathematician-like way) the completion of the underlying uniform space. But these two completions are just two different types so you could instead ask if they are uniform-equiv, not that this exists.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317201):
On the other hand Johannes, if I recall correctly, put a bunch of stuff in `topological_space.lean` about different topologies on the same space...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317202):
What do you mean "different types"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317249):
Isn't there one "complete-a-group" function which completes a group and spits out one type, and one "complete-a-uniform-space" function which completes a uniform space and spits out a second type? And we think of them as "equal" but they're two different types. That's all I mean, and you know all this already.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317315):
I was wondering if you ever needed to compare two uniformities on the same type, but I don't know the full story

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317340):
No, there is a complete a uniform space structure, an instance saying that the result has a uniform structure, and there are instances saying that abelian top groups are uniform spaces, and that the completion of a group is a top group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317355):
The full story is still at https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L124

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317382):
and https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/group_completion.lean#L118 of course (maybe with tiny differences)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317454):
So we really have two uniform space structures on the same type. But of course I wonder whether I could cook up more functions to hide things to the type class system

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317655):
So should that line 124 even make sense?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317662):
That's what I'm thinking

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317668):
Given some top group H

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317670):
there is an associated uniform space which is also H

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317685):
but then isn't there `topological_add_group.completion H` (one type) and `uniform_space.completion H` (a different type)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317756):
And then maybe you prove a theorem saying that two uniform structures are the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317768):
I guess there is a single (uniform) completion operation which additionally has the property that it lifts topological group structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317774):
right, but should it be like that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317777):
should the theorem be that there's a uniform space equiv?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317778):
Obviously `topological_group` should have a uniform component so that this can be by defeq

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317847):
```quote
Obviously `topological_group` should have a uniform component
```
This is when it gets silly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317853):
The theorem that is sorried there has mathematical content, it won't become trivial

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317857):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317866):
So I don't know what Mario wants to see defeq

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317867):
of course, the content is shifted to the definition of the topological group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317879):
Is there no way of making all this sensible?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317884):
There are zero cases where you want a topological group with a uniform structure that doesn't agree with it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317890):
It's like the product of metric spaces example, but it's even better, because we don't even have to take a product.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317894):
Except for non-commutative groups where there are two choices

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317895):
rofl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317944):
Left uniformity and right uniformity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317945):
two different uniformities giving the same topology, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317950):
sure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317959):
Let's cross that bridge when we come to it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317960):
I assumed everything was commutative because I aimed for addition in rings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317964):
and it was complicated enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317967):
I want to end up in a situation where there are no diamonds. Is this possible?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317977):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317978):
Given a uniform space I want to be able to complete it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317982):
I don't mind seeing the uniform structure as part of the abelian top group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317985):
I assume you mean the diamonds commute by defeq

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134317987):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318005):
What I was thinking is that the group completion should have a different name.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318006):
But I don't see how this will help when proving the actual theorem, even if this proof is now part of the construction of the top group instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318053):
this is not supposed to help proving the theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318059):
yes I was just wondering about how to make the theorem part of the infrastructure. Is this just clear to both of you?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318060):
I mean help in the Lean sense, not maths sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318076):
Nothing is clear to me here (except the proof I see on paper in front of me)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318084):
I want to give the top group completion a different name, make it a different type to the uniform space completion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318110):
hmm but it still has to be a top group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318113):
It will make that `same_uniformity` theorem true by defeq, so you won't have to muck about with rewriting instance arguments

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318165):
But it's true that the theorem still has to be proved, and it is an equality of uniformities

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318169):
top groups and uniform spaces -- they are going to be classes, right? Let's make that assumption

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318172):
yes, are they not already?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318173):
And there's always going to be an instance from top group to uniform space, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318174):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318184):
but it may be generated by `extends`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318198):
?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318208):
and will a top group definitely have a uniformity component?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318215):
so the instance is a forgetful functor?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318219):
If `class top_group extends uniform_space`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318222):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318225):
But with the completion construction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318230):
you can insert the theorem into the construction, can you not?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318236):
yes, that's the idea

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318239):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318313):
so the top group completion *must* have the "uniform space generated by the top group structure" uniform space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318321):
So the gain would be when I wanted to use the `same_uniformity` theorem, in https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/group_completion.lean#L161 not when I want to prove it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318401):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318406):
sounds very good

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318411):
I think I'm there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318434):
Kevin, do you want to know why we need this theorem? It's easy to explain

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318451):
Mario, the trouble is I tried to do this "top_group extends uniform space" trick after the Orsay meeting but couldn't handle everything that broke when I started

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318512):
I can see for maths reasons why we want to prove the two uniformities are equal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318529):
What I was thinking about was how all this could play well with the type class system.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318544):
That is exactly why I changed your beta,beta to beta,gamma, because then the theorem you were struggling on suddenly seemed much easier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318545):
ok, we're on the same page

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318717):
but if topological_group extends uniform_space (I don't know if it does or if it should) then we have to be careful, but it sounds like it's OK. I guess it doesn't matter whether it extends or not -- you probably still want an instance. Eew. Is top group -> uniform space -> top space defeq to top group -> top space?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318744):
Yes, I made sure this is true back in June

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318765):
It's ridiculous that this sort of thing is important. I think the system is not quite fit for purpose.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318790):
https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L353

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318805):
I'm with Chris. He had trouble with two instances which were provably equivalent but not defeq. There should be a way to make this work by brandishing a theorem at the type class inference system and saying "use this if stuck"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318890):
```quote
just like the theorem that identity is continuous iff the topologies are le
```
Do we actually have this theorem in mathlib? I can't find it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318891):
It would be wonderful if the default setting was "if it's a class, then you will have one instance and that's the end of it. If there are two instances, then you had better supply the proof that they're the same"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134318900):
and you had to explicitly switch this off.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134319419):
Let's try to use the existing Lean. @**Mario Carneiro** what do you suggest I should do? Should I try to refactor everything about commutative additive top groups? Should I start with `class topological_abelian_group (α : Type u) extends uniform_space α, add_comm_group α`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134319450):
and then prove an instance converting this to the existing topological group classes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 20 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134320701):
he'll make you call it `topological_add_comm_group`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134321783):
I'm okay with saying `top` instead of `topological`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134321834):
exactly because you want to stack adjectives like this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134324250):
What about my question?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134325399):
I hate to answer a question like that with yes, but yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134325445):
then again, I think @**Johannes Hölzl** had a part in the original formulation so maybe he should say something here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 20 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134325826):
```quote
I hate to answer a question like that with yes, but yes
```
What would you prefer?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 20 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134326342):
what you said: a class `top_add_comm_group` that extends `uniform_space` and `add_comm_group`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 21 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134377971):
I tried various things today, but clearly I'm not doing it right. Recall I defined the Hausdorff completion functor in https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/master/src/for_mathlib/completion.lean I also defined a uniform structure on commutative topological groups in https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/master/src/for_mathlib/topological_structures.lean#L109, and wanted to get a group completion functor. For this it seems we need closer integration of topological groups and uniform structures. I made a first attempt at https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/e44b49e7bd9f77f59246f725cc38bf879c2af50f/src/for_mathlib/top_groups.lean There I have an axiom relating a uniform structure and a group structure, but the uniform structure is a parameter. There are only two sorries in that file, and the completion stuff is available right from the beginning, seemingly without diamond issue. However I'd like a way to produce a `top_add_comm_group` from a topological space structure and a group structure, building the uniform space structure automatically using a version of my previous unbundled work. I don't see how to do that. Then I tried https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/master/src/for_mathlib/top_groups.lean where the only parameter of `top_add_comm_group` is the carrier type. But then I had to setup much more wrapping around my completion stuff, and https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/master/src/for_mathlib/top_groups.lean#L45 completely fails. I really need help from @**Johannes Hölzl**  or @**Mario Carneiro** in order to now which attempt (if any) goes in the right direction.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 21 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134391084):
I'm taking a look at it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 22 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134432236):
Do you need `topological_add_group` in your definition of `top_add_comm_group`? Shouldn't `topological_add_group` be derived from `unif_group`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 22 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134434646):
You're probably right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 22 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134434933):
I forked your repo: https://github.com/johoelzl/lean-perfectoid-spaces

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 22 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134434980):
So in `top_groups` you need to prove that the group is a group, and then that the uniformity fits

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 22 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134435010):
first we need to show that `-` and `+` are (uniform) continuous, and reduce to `-`, `+` on `G` under `to_completion`. Then we can proof the group properties by the embedding along `to_completion`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 22 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134435042):
is this what you expected or do you want something different?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 22 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134435676):
I want to be able to manipulate topological groups and their completions. The mathematical story is extremely clear, and I already formalized large parts of it, but they don't want to fit together. Have you seen my two recent attempts? There are successive commits. The older attempts are in neighboring files. Would you like me to LaTeX the math story?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 22 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134435734):
I think LaTeX is not yet necessary. But what kind of manipulations do you want to make?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 22 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134435834):
The same thing we want from the beginning: a completion functor, left adjoint to the inclusion of complete hausdorff group into all topological groups. That's all!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 22 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134435843):
We do have it for uniform space, in my `completion.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 22 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134435897):
hm, this is a little bit too far for me. but you are currently stuck in proving that the completion of a topological group (with the induced uniformity) is again a group. This is what I see in `top_groups`. is this correct?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 22 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134435910):
or did you just `sorry` this part, because you wanted to see how this way works for later proofs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 22 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134436031):
The key fact is we start with a completion which is a universal solution to the problem of factoring maps into complete hausdorff spaces:
* https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L51
* https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L132
* https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L157
* https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L171
Then the action of the completion functor on maps comes for free: https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L144

When moving to topological groups, we want all those maps to be group morphisms. It looks like extending operation by continuity and running the same abstract non-sense will do it without any work. But when you think about how to prove that `completion.map f` is a group morphisms you see you need commutation of the two constructions (from top group to uniform space and from uniform space to completion)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 22 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134436032):
so what I propose is:
* we get obviously that `group_completion G` is a complete, separated uniformity (and everything we know about them). This is a couple of instances.
* then we proof that it is a `group`. This requires some work, we need to lift the group operations and show that they are uniform and invariant under coerion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 22 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134436086):
I did all that in my first attempt in https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/topological_structures.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 22 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134436096):
But then the last instance fail completely because of the diamond issue, and even sorrying an equality of uniform structures didn't help because I couldn't manage rewriting instances

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 22 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134436140):
I'm sorry I need to take care of my family. But in any case I don't think this problem can be solved without investing some time into reading my various attempts

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 22 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134436141):
Thank you very much for trying to help me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 22 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134436154):
I am of course actively interested in making all this work so let me know if I can help somehow.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 22 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134446757):
So it turns out that `top_add_comm_group` is equivalent to `uniform_add_group`. From `uniform_add_group` we can derive `uniformity = comap (λx:α×α, x.2 - x.1) (nhds (0:α))`.

so the only complicated lift is the group structure itself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 24 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134515389):
@**Johannes Hölzl** I see you made some progress in your fork. Are you still working on this? Or do you think I should try to copy your work and try to proceed?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 24 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134515432):
I didn't continue on this yet. But I want to continue today

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134515457):
In particular, does it mean you think that the definition of `top_add_comm_group` is the correct starting point, and wrapping the completion stuff in `group_completion` is the right thing to do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 24 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134515513):
Ok, great. I'll wait and see then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 24 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134515522):
But I think I will take a look again at your `completion` branch in `leanprover-community`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 24 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134515619):
I think `top_add_comm_group` is not necessary. I think `uniform_add_group` can also be used instead of it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 24 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134515669):
But if you want you can finish the proofs in `top_groups.lean`. In the meantime I look at your `completion` branch and try to bring it up to current `mathlib` and see how I want to merge it. What do you think about this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134515861):
I still don't understand what is `uniform_add_group` This notion doesn't exist in real world maths, and it seems equivalent to topological groups, at least in the communtative case. What's the point?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 24 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134516035):
The difference is just that `topological_add_group` doesn't know about its uniformity. So I called the type class which requires the uniformity `uniform_add_group`. We can change `topological_add_group` to require an uniform space, and change the axiom to assume that `-` is uniformly continuous.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 24 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134516077):
The difference to `top_add_comm_group` will be that `topological_add_group` is still unbundled.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 24 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134516170):
I don't understand. What is unbundled?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 24 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134516284):
Okay, **bundled** is not the right word in this context. What I mean is that `topological_add_group` has the topology and the group structure as **parameter**. `top_add_group` has it as the uniformity and its group as fields in its structure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 24 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134516888):
I'm sorry this conversation is not smoother, but my youngest daughter is sick, and I have to take care of her

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 24 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134516966):
The point of the "bundled" version was to try to make sure the work of proving the uniform structure compatibility in group completions would be hidden in the instance building, and would never be an issue afterwards

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 24 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134517026):
But of course this version needs a constructor which only takes group law axioms, a topology and a bunch of continuity proofs, in the same way as a metric space can be constructed from a distance without providing a uniformity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 24 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134517460):
I will see how much of the actual construction can be hidden. Also, note that I will rebase your `completions` branch in `leanprover-community` after lunch. I hope you don't have any local changes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 24 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134517551):
It's a bit of a mess that this work is somewhat split between this mathlib branch and the prefectoid repository, but I think the only substantial difference is the new `top_groups.lean` in the perfectoid repository, so you can work on the community mathlib branch

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 24 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134522077):
I worked a bit, see https://github.com/johoelzl/lean-perfectoid-spaces/compare/master...PatrickMassot:master I unsorried the `add_comm_group` structure by porting my previous work. Hopefully this could save you some time. This required adding a couple of lemmas first. I tried to follow the mathlib convention in naming `group_completion.continuous_add` and `group_completion.continuous_add'` but I noticed you didn't. Also, I shortened the name since it's all in the `group_completion` namespace, but since the purely topological `continuous_add` is in root namespace, it's a but of a mess. Hopefully all this will be much simpler in the end

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 24 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134522483):
Thanks! I'm currently reorganizing `uniform_space.lean` and move the separated quotient type and `Cauchy` to `completions.lean`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 24 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134522579):
Great!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 24 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134522595):
I'm very excited and grateful to get some help here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 24 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134524646):
Also note that the proofs in https://github.com/johoelzl/lean-perfectoid-spaces/blob/fa721c6aa863c79b22ce463358c2b616c413e38c/src/for_mathlib/top_groups.lean#L194 are not as abstract as we'd like them to be. Ideally they would all follow from things like https://github.com/leanprover-community/mathlib/blob/a5da4d5acccc9910d921cfadb2c8e4cce59e1d80/analysis/topology/completion.lean#L726. So all topological argument would ultimately be in https://github.com/leanprover-community/mathlib/blob/a5da4d5acccc9910d921cfadb2c8e4cce59e1d80/analysis/topology/completion.lean#L552, as they should be. But the trouble is that group axioms in mathlib are stated as equalities between elements, instead of functions. So a lot of packing and unpacking would be required. I hesitated to setup all this, with a new group structure constructor inspired by [universal algebra](https://en.wikipedia.org/wiki/Universal_algebra) but I preferred to move on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 25 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134615079):
@**Patrick Massot** I moved now most of the completion stiff to its own lean theory `analysis.topology.completion`. I added the group completion instances to the `completion` type itself. I guess this makes sense.
the only thing missing is a nice setup for topological groups, where one only needs to define the zero nighbourhood and get a topological group, or where one proofs that we have a topological group and get the uniformity. This is currently in `analysis/topology/topological_groups` but needs to be restructured.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134619925):
Thanks @**Johannes Hölzl** It all looks nice, except that I still don't know what we are talking about. What is this theory of `uniform_add_group`? Is this meant to be only an intermediate definition? Is the missing piece the piece were you make connection with topological groups as they are defined in math books?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134620301):
Also, I'm confused about when the diamond problem will return to hit us. The fact that the group uniform structure on the completion of a group is the completion of the group uniform structure is a non-empty mathematical content. In my approach it seemed necessary in order to get a functorial group completion. Where will this be needed in your way of building the theory?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 25 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134620397):
`uniform_add_group` is a technical device. I don't want to force each appearance of a topological group to be a uniform space. That's why it is split into a `topological_add_group` (topology + group) and `uniform_add_group` (uniformity + group). We know also that we can derive a canonical uniform space for a topological group, but this is not setup as a type class instance.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 25 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134620466):
What is exactly the diamond? We have `add_group (completion A)` and `uniform_space (completion A)`. Both have currently only one way to construct them. What are the alternatives?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134620573):
`topological_add_group.to_uniform_space (completion A) = completion (topological_add_group.to_uniform_space A)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134620584):
That's a non-empty mathematical result

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 25 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134620608):
but `topological_add_group.to_uniform_space` is currently not in our type class hierarchy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134620712):
I don't understand why this theorem can be avoided while constructing the completion functor for commutative topological groups

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134620730):
It's independent of the discussion of have instances or def

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 25 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134621075):
With `uniformity_eq_comap_nhds_zero` (https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/topological_structures.lean#L276) it should be easy to prove this. In the one direction this is how we define the uniformity, in the other direction we have a `uniform_add_group` and can use `uniformity_eq_comap_nhds_zero`.

But maybe I misunderstand the problem. I will try to prove this diamond tomorrow.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134621323):
Ok, thank you very much. I would really love to see the finished thing (including the link with topological groups). I hope I'll be able to learn something from this, since I spend quite a lot of time thinking about more naive (ie. straight from maths books) approaches

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134625736):
Indeed `uniformity_eq_comap_nhds_zero` looks like a characterization of the uniform structure that could be very important. The first step of the proof looks like it has nothing to do with groups:
```lean
lemma johannes_lemma {α : Type*} [uniform_space α] : ∀ {s : set (α×α)} {f : α → α → α},
  uniform_continuous (λp:α×α, f p.1 p.2) → s ∈ (@uniformity α _).sets →
  ∃ u ∈ (@uniformity α _).sets, ∀a b c, (a, b) ∈ u → (f a c, f b c) ∈ s :=
begin
  assume s f hf hs,
  rw [uniform_continuous, uniformity_prod_eq_prod, tendsto_map'_iff, (∘)] at hf,
  rcases mem_map_sets_iff.1 (hf hs) with ⟨t, ht, hts⟩, clear hf,
  rcases mem_prod_iff.1 ht with ⟨u, hu, v, hv, huvt⟩, clear ht,
  refine ⟨u, hu, assume a b c hab, hts $ (mem_image _ _ _).2 ⟨⟨⟨a, b⟩, ⟨c, c⟩⟩, huvt ⟨_, _⟩, _⟩⟩,
  exact hab,
  exact refl_mem_uniformity hv,
  refl
end
```
I don't know what would be a better mathlib name.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134625920):
Better statement:
```lean
lemma johannes_lemma {α : Type*} [uniform_space α] {β : Type*} [uniform_space β]
: ∀ {s : set (β × β)} {f : α → α → β},
  uniform_continuous (λ p : α × α, f p.1 p.2) → s ∈ (@uniformity β _).sets →
  ∃ u ∈ (@uniformity α _).sets, ∀a b c, (a, b) ∈ u → (f a c, f b c) ∈ s :=
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134625951):
And I don't change any character from the proof! I love that. Usually when we wrote in real world math: "the same proof shows that..." it's a polite lie

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626147):
Of course we can also write this as:
```lean
lemma johannes_lemma {α : Type*} [uniform_space α] {β : Type*} [uniform_space β] {f : α → α → β}
: uniform_continuous (λ p : α × α, f p.1 p.2) → ∀ {s : set (β × β)}, s ∈ (@uniformity β _).sets →
  ∃ u ∈ (@uniformity α _).sets, ∀a b c, (a, b) ∈ u → (f a c, f b c) ∈ s
```
Isn't it an `iff` then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 25 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626187):
I'm trying to process the "better statement". Is it essentially saying that if $$f : A \times A \to B$$ is uniformly continuous, then so is $$f(-, c) : A \to B$$ for any $$c \in A$$?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626239):
I'm also trying to process it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626262):
But I don't think it means what you wrote

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626280):
but you may be right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 25 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626303):
Oh no I am not right.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 25 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626314):
I see. I had the quantifier involving $$c$$ in the wrong place.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626333):
Yeah, it's a tricky statement

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134626410):
Still there is an asymmetry between the two A factors, so it's probably not an iff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134627274):
Anyway, this lemma, in its latest version allows to reduce the crucial proof to:
```lean
lemma uniformity_eq_comap_nhds_zero : uniformity = comap (λx:α×α, x.2 - x.1) (nhds (0:α)) :=
begin
  rw [nhds_eq_comap_uniformity, filter.comap_comap_comp],
  refine le_antisymm (filter.map_le_iff_le_comap.1 _) _ ; intros s hs,
  { rcases johannes_lemma uniform_continuous_sub' hs with ⟨t, ht, hts⟩,
    refine mem_map.2 (mem_sets_of_superset ht _),
    rintros ⟨a, b⟩,
    simpa [subset_def] using hts a b a },
  { rcases johannes_lemma uniform_continuous_add' hs with ⟨t, ht, hts⟩,
    refine ⟨_, ht, _⟩,
    rintros ⟨a, b⟩, simpa [subset_def] using hts 0 (b - a) a }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134627304):
And I still don't understand the magic trick that seems to have removed the diamond issue (I mean removed from the maths discussion, I'm not even talking about Lean). I guess I'll see it when everything will be in place.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134627409):
I also don't understand at all https://github.com/leanprover-community/mathlib/commit/85b19e23d45f14a210d0b7491c66477d0c560c9a Why did you remove all this? It contains a lot of maths that don't appear anywhere else

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 26 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134652519):
Urgs, I removed the wrong file.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 26 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134697940):
@**Johannes Hölzl** Did you try to go from `topological_add_group` to the completion and still get everything?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 26 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134698069):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 26 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134698176):
Mario did you just respond to a question asked on the wrong topic with an answer posted on the wrong stream

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 26 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134698232):
yes. yes I did.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 26 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134698240):
This topic was only distantly related to separation stuff anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 26 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134698271):
Somehow, deep down, I guess we miss Gitter's mess

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 26 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134698719):
The stuff about group topologies generated from a neighborhood filter around zero will probably be very convenient for the perfectoid project, which  uses adic topology

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 26 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134699310):
I didn't work yet on the diamond, I got side tracked by the topological space construction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 26 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134699347):
Ok, I understand.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 27 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Separation%20stuff/near/134731658):
I added now `topological_add_comm_group.to_uniform_space_eq`. It doesn't look to be directly a diamond. The reason is the following:
For `completion α` to be a group, we already need to know that `α` has a uniform space, and that the group structure is compatible with this uniformity (i.e. `uniform_add_group`).

A diamond would mean we have `group_to_uniform ∘ completion = completion ∘group_to_uniform`. But `completion` doesn't work on groups without the uniformity. So we actually have `group_to_uniform ∘ completion ∘group_to_uniform = completion ∘group_to_uniform`. Now it is enough to prove `group_to_uniform ∘ G = G`, where `G` is already a group with compatible uniformity.

