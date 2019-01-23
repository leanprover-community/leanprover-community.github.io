---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/35751transportforever.html
---

## Stream: [maths](index.html)
### Topic: [transport forever](35751transportforever.html)

---


{% raw %}
#### [ Patrick Massot (Oct 10 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135547994):
Today I tried to setup transport of structure along equiv, since @**Mario Carneiro** wanted to see (part of) what we would like to be automated. It can be seen at https://gist.github.com/PatrickMassot/9c5246efe8d1fd4f26c21cbf2ac99ff8 First I'd like to know if the beginning looks reasonnable. The answer is almost certainly not since I'm stuck when I try to go to rings at the bottom. This file is autonomous, it should fail reliably with any recentish version of mathlib.

#### [ Patrick Massot (Oct 10 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135548014):
Of course this is needed for the ring completions project, which is needed for the perfectoid project

#### [ Patrick Massot (Oct 10 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135548345):
I should say why this is only part of what Kevin always asks for. Here we start with some structure on a type and want to transport it along a given equiv, so that the equiv becomes an isomorphism in the relevant category. The next step is to assume we have an isomorphism in a category and transport various statements (like Kevin's exact sequences).

#### [ Patrick Massot (Oct 10 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135548838):
Let me recall the context of the ring completion project. We start with a topological ring `α`. We get a topological ring structure on `separation_quotient α` in https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L279. We get a topological ring structure on the completion of a separated topological ring at https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L1205 (oops, this is only a `comm_ring` instance, but the topological axioms should be easy). And  we have https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L747 : `completion (separation_quotient α) ≃ completion α` along which we want to transport the topological ring structure.

#### [ Johan Commelin (Oct 10 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135556061):
Nice start @**Patrick Massot**! It's also a bit sad that it is breaking down for rings.

#### [ Patrick Massot (Oct 10 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561185):
Don't loose hope Johan, Mario will save us.

#### [ Mario Carneiro (Oct 10 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561760):
As you point out, there are two slightly different senses of "transport of structure" being used here. One, which seemed to be Kevin's main point, is a theorem such as "if R ~= S are isomorphic rings and R is artinian then S is artinian", and this has a possibility of being addressed by `transfer`. The other has the form "Given an equiv A ~= B of sets, and a ring structure on A, there is an induced ring structure on B" which is what you seem to be demonstrating in the gist.

#### [ Patrick Massot (Oct 10 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561778):
yes

#### [ Patrick Massot (Oct 10 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561836):
In my use case I first want to transport the structure over an equiv and then transport properties

#### [ Mario Carneiro (Oct 10 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561849):
One reason I wouldn't want to just jump in with that kind of tactic is that most of those theorems generalize to a weaker structure than equiv

#### [ Patrick Massot (Oct 10 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561854):
And my equiv is actually a uniform space equiv so completeness would be transported for instance

#### [ Mario Carneiro (Oct 10 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561875):
For example you might just have an injection into a subring of a ring

#### [ Mario Carneiro (Oct 10 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561899):
or it might not even be an injection but there is a coherence property

#### [ Patrick Massot (Oct 10 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561902):
Maybe it's too early for a tactic here. As you wrote, we first need to see a couple of handcrafted examples in order to understand what we want

#### [ Patrick Massot (Oct 10 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561982):
Do you think the ring thing can be done with that starting point? I'm not sure whether I should try to have local instances, or maybe use `haveI` in the constructions...

#### [ Mario Carneiro (Oct 10 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562025):
I also have no applications of your kind of transport of structure

#### [ Patrick Massot (Oct 10 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562043):
what?

#### [ Mario Carneiro (Oct 10 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562090):
the "A is a ring so B is a ring" kind

#### [ Patrick Massot (Oct 10 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562094):
I wrote very precisely what immediate application I have

#### [ Patrick Massot (Oct 10 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562106):
In this thread, right before Johan's message

#### [ Mario Carneiro (Oct 10 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562141):
the problem is that just transporting the whole structure won't work

#### [ Mario Carneiro (Oct 10 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562155):
you will end up with yet another copy of the uniform structure

#### [ Patrick Massot (Oct 10 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562236):
A uniform structure *and* a compatible ring structure, and a universal property, that's exactly what I want

#### [ Mario Carneiro (Oct 10 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562282):
So what is the setting exactly for this theorem? `completion (separation_quotient α) ≃ completion α`

#### [ Patrick Massot (Oct 10 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562344):
https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L747

#### [ Patrick Massot (Oct 10 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562349):
any uniform space structure on any type

#### [ Mario Carneiro (Oct 10 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562378):
so where are the rings coming from

#### [ Patrick Massot (Oct 10 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562459):
I don't know what to write that is not copy-pasting my message before Johan's message

#### [ Johan Commelin (Oct 10 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562511):
```quote
Let me recall the context of the ring completion project. We start with a topological ring `α`. We get a topological ring structure on `separation_quotient α` in https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L279. We get a topological ring structure on the completion of a separated topological ring at https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L1205 (oops, this is only a `comm_ring` instance, but the topological axioms should be easy). And  we have https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L747 : `completion (separation_quotient α) ≃ completion α` along which we want to transport the topological ring structure.
```
Voila. I did it.

#### [ Mario Carneiro (Oct 10 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562576):
explain the last sentence. Which side has the ring, and why doesn't the other side have one?

#### [ Patrick Massot (Oct 10 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562604):
Left hand side has the ring

#### [ Patrick Massot (Oct 10 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562615):
Because `separation_quotient α` is separated

#### [ Patrick Massot (Oct 10 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562634):
This is the content of the second sentence

#### [ Mario Carneiro (Oct 10 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562813):
I don't get it. Is this `completion (separation_quotient α) ≃ completion α` in fact (in math) a uniform ring isomorphism?

#### [ Mario Carneiro (Oct 10 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562826):
If so, why isn't `completion α` already separated?

#### [ Patrick Massot (Oct 10 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562828):
A posteriori yes

#### [ Patrick Massot (Oct 10 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562856):
`completion α` is separated, but `α` isn't

#### [ Mario Carneiro (Oct 10 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562875):
what goes wrong in the `ring (completion α)` instance if you drop the `separated α` property?

#### [ Patrick Massot (Oct 10 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563061):
The map `coe : α -> completion α` is no longer injective

#### [ Mario Carneiro (Oct 10 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563201):
does injectivity get used somewhere?

#### [ Patrick Massot (Oct 10 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563225):
It is currently used in the proof everywhere, but maybe there is another proof. Johannes wrote that proof.

#### [ Patrick Massot (Oct 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563266):
So I didn't think hard about it

#### [ Mario Carneiro (Oct 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563276):
but again a posteriori it seems like it is actually injective

#### [ Mario Carneiro (Oct 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563283):
or else you wouldn't have that equiv

#### [ Patrick Massot (Oct 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563284):
No

#### [ Patrick Massot (Oct 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563289):
it's not injective

#### [ Patrick Massot (Oct 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563305):
`coe : α -> completion α` is injective if and only if `α` is separated

#### [ Patrick Massot (Oct 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563316):
`separation_quotient α -> completion (separation_quotient α)` is injective

#### [ Mario Carneiro (Oct 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563320):
ah, ok

#### [ Patrick Massot (Oct 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563321):
because `separation_quotient α` is separated

#### [ Mario Carneiro (Oct 10 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563370):
Do the definitions of `has_one` and `has_mul` at least work without `separated`?

#### [ Patrick Massot (Oct 10 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563397):
Probably

#### [ Patrick Massot (Oct 10 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563402):
maybe not actually

#### [ Patrick Massot (Oct 10 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563424):
sorry

#### [ Patrick Massot (Oct 10 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563463):
You can define mul

#### [ Patrick Massot (Oct 10 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563466):
the issue is continuity

#### [ Mario Carneiro (Oct 10 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563544):
I'm checking this branch out, 1 sec

#### [ Mario Carneiro (Oct 10 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563584):
anyway, my intuition is that you don't want to use transfer of structure like this. You should already be able to define the structure a priori, and you want to show that the equivalence respects the structure that is already there

#### [ Patrick Massot (Oct 10 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563659):
In need to transport something along this equiv though

#### [ Mario Carneiro (Oct 10 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563662):
In particular, if we did transfer of structure your way, we would end up with two ring structures on `completion (separation_quotient A)`

#### [ Patrick Massot (Oct 10 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563689):
I'm ready to trow away any ring structure which is not compatible with the uniform structure

#### [ Mario Carneiro (Oct 10 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563749):
I would guess the two ring structures are equal, but as we know that's not good enough for lean

#### [ Patrick Massot (Oct 10 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563873):
maths on a computer are so complicated...

#### [ Mario Carneiro (Oct 10 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565503):
Oh, this is evil: https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L263-L273

#### [ Mario Carneiro (Oct 10 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565530):
I'm starting to see why you get heq goals

#### [ Patrick Massot (Oct 10 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565593):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/heq.20hell.20again/near/135479776

#### [ Patrick Massot (Oct 10 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565596):
I already confessed

#### [ Patrick Massot (Oct 10 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565687):
And I blame Danish thefts

#### [ Mario Carneiro (Oct 10 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565707):
I think we need to be less constructive with our quotient constructions

#### [ Mario Carneiro (Oct 10 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565730):
the quotient ring construction for example should apply to any quotient map, not just the canonical one

#### [ Chris Hughes (Oct 10 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565737):
What's evil about it?

#### [ Patrick Massot (Oct 10 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565743):
constructive is evil

#### [ Mario Carneiro (Oct 10 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565745):
Type equality is evil

#### [ Patrick Massot (Oct 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565830):
Actually I tried to redeem with the next lemma

#### [ Mario Carneiro (Oct 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565858):
`eq_mpr_heq`?

#### [ Patrick Massot (Oct 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565859):
or previous lemma

#### [ Mario Carneiro (Oct 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565876):
the instance?

#### [ Patrick Massot (Oct 10 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565889):
I have one lemma saying the quotients are equal but the other one says the setoids are equal

#### [ Chris Hughes (Oct 10 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565899):
```quote
the quotient ring construction for example should apply to any quotient map, not just the canonical one
```
Do you mean so it would be easy to prove things about quotient rings that aren't constructed using `quotient`, like `zmod`, or `complex` using theorems about quotient rings?

#### [ Patrick Massot (Oct 10 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565949):
I mean https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L255-L261

#### [ Mario Carneiro (Oct 10 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565965):
right

#### [ Mario Carneiro (Oct 10 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565991):
as long as it acts like a quotient you should have quotient ring construction, quotient topology, etc

#### [ Patrick Massot (Oct 10 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566883):
```quote
as long as it acts like a quotient you should have quotient ring construction, quotient topology, etc
```
Is this something I'm meant to understand and convert into action, or was this you thinking aloud?

#### [ Mario Carneiro (Oct 10 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566901):
I don't really expect you to do anything on that front, it's mostly the fault of `quotient_ring` and such

#### [ Mario Carneiro (Oct 10 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566962):
in the short term you might try to avoid casting between types but still unfold the fact that it is a quotient

#### [ Patrick Massot (Oct 10 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566972):
This quotient ring stuff seems tricky to get right. I was already refactored once

#### [ Mario Carneiro (Oct 10 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566984):
indeed it's been refactored again

#### [ Mario Carneiro (Oct 10 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566993):
(module refactor touched this too)

#### [ Patrick Massot (Oct 10 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567002):
I hope this completion stuff will help you get the refactor right

#### [ Patrick Massot (Oct 10 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567198):
@**Kevin Buzzard** this conversation suggests that the perfectoid project is waiting for module refactor also on the ring completion side

#### [ Patrick Massot (Oct 10 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567217):
unless we find a way to finish that ring completion thing using evil lemmas and fake transport of structure

#### [ Kevin Buzzard (Oct 10 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567220):
One thing that really spurs me on with this whole thing is that as we try to do a different kind of mathematics to the kind that is typically done in a theorem prover, we run into issues which computer scientists seem to be able to solve. I am constantly feeling like both sides somehow benefit.

#### [ Kevin Buzzard (Oct 10 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567284):
I did this once (cutting corners) with schemes, and now look at that project.

#### [ Kevin Buzzard (Oct 10 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567295):
I say we do it right this time, however long it takes.

#### [ Patrick Massot (Oct 10 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567303):
Yes, this is exactly what I was thinking

#### [ Kevin Buzzard (Oct 10 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567311):
I'm not that busy in January...

#### [ Patrick Massot (Oct 10 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567348):
Yeah, too bad we have orthogonal teaching schedules this year

#### [ Patrick Massot (Oct 10 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567464):
Mario, could we still have `congr'` trying to discharge goals using `proof_irrel` and `proof_irrel_heq` in order to cover my evil actions?

#### [ Patrick Massot (Oct 19 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136137596):
About transport of structure, Assia pointed out to me https://hal.inria.fr/hal-01559073 It seems it's actually relevant, despite the univalent stuff

#### [ Patrick Massot (Oct 19 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136137628):
I notice that it helps publishing CS papers to promise stuff for free. It seems most papers titles in this area contain this promise.

#### [ Andrew Ashworth (Oct 19 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136138635):
Everybody loves free things! This is a good paper, I linked it previously in the "hott for newbies" thread, and Mario made a few comments.

#### [ Rudi Grinberg (Oct 20 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136146880):
Where is this thread? The search is failing me.

#### [ Bryan Gin-ge Chen (Oct 20 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136146954):
It's [here](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/what.20is.20wrong.20with.20HoTT/near/135265404).

#### [ Bryan Gin-ge Chen (Oct 20 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136147013):
As a side note, I've found that by default, searching Zulip doesn't turn up results from before I joined the server. However, it does if I additionally include "stream:general" or "stream:maths", etc.

#### [ Patrick Massot (Oct 20 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136162441):
```quote
Everybody loves free things! This is a good paper, I linked it previously in the "hott for newbies" thread, and Mario made a few comments.
```
Thanks! I was sure it had been mentioned, I even told @**Assia Mahboubi** but I couldn't find it.


{% endraw %}
