---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/35751transportforever.html
---

## Stream: [maths](index.html)
### Topic: [transport forever](35751transportforever.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135547994):
Today I tried to setup transport of structure along equiv, since @**Mario Carneiro** wanted to see (part of) what we would like to be automated. It can be seen at https://gist.github.com/PatrickMassot/9c5246efe8d1fd4f26c21cbf2ac99ff8 First I'd like to know if the beginning looks reasonnable. The answer is almost certainly not since I'm stuck when I try to go to rings at the bottom. This file is autonomous, it should fail reliably with any recentish version of mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135548014):
Of course this is needed for the ring completions project, which is needed for the perfectoid project

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135548345):
I should say why this is only part of what Kevin always asks for. Here we start with some structure on a type and want to transport it along a given equiv, so that the equiv becomes an isomorphism in the relevant category. The next step is to assume we have an isomorphism in a category and transport various statements (like Kevin's exact sequences).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135548838):
Let me recall the context of the ring completion project. We start with a topological ring `α`. We get a topological ring structure on `separation_quotient α` in https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L279. We get a topological ring structure on the completion of a separated topological ring at https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L1205 (oops, this is only a `comm_ring` instance, but the topological axioms should be easy). And  we have https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L747 : `completion (separation_quotient α) ≃ completion α` along which we want to transport the topological ring structure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135556061):
Nice start @**Patrick Massot**! It's also a bit sad that it is breaking down for rings.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561185):
Don't loose hope Johan, Mario will save us.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561760):
As you point out, there are two slightly different senses of "transport of structure" being used here. One, which seemed to be Kevin's main point, is a theorem such as "if R ~= S are isomorphic rings and R is artinian then S is artinian", and this has a possibility of being addressed by `transfer`. The other has the form "Given an equiv A ~= B of sets, and a ring structure on A, there is an induced ring structure on B" which is what you seem to be demonstrating in the gist.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561778):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561836):
In my use case I first want to transport the structure over an equiv and then transport properties

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561849):
One reason I wouldn't want to just jump in with that kind of tactic is that most of those theorems generalize to a weaker structure than equiv

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561854):
And my equiv is actually a uniform space equiv so completeness would be transported for instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561875):
For example you might just have an injection into a subring of a ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561899):
or it might not even be an injection but there is a coherence property

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561902):
Maybe it's too early for a tactic here. As you wrote, we first need to see a couple of handcrafted examples in order to understand what we want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561982):
Do you think the ring thing can be done with that starting point? I'm not sure whether I should try to have local instances, or maybe use `haveI` in the constructions...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562025):
I also have no applications of your kind of transport of structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562043):
what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562090):
the "A is a ring so B is a ring" kind

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562094):
I wrote very precisely what immediate application I have

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562106):
In this thread, right before Johan's message

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562141):
the problem is that just transporting the whole structure won't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562155):
you will end up with yet another copy of the uniform structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562236):
A uniform structure *and* a compatible ring structure, and a universal property, that's exactly what I want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562282):
So what is the setting exactly for this theorem? `completion (separation_quotient α) ≃ completion α`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562344):
https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L747

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562349):
any uniform space structure on any type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562378):
so where are the rings coming from

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562459):
I don't know what to write that is not copy-pasting my message before Johan's message

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 10 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562511):
```quote
Let me recall the context of the ring completion project. We start with a topological ring `α`. We get a topological ring structure on `separation_quotient α` in https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L279. We get a topological ring structure on the completion of a separated topological ring at https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L1205 (oops, this is only a `comm_ring` instance, but the topological axioms should be easy). And  we have https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L747 : `completion (separation_quotient α) ≃ completion α` along which we want to transport the topological ring structure.
```
Voila. I did it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562576):
explain the last sentence. Which side has the ring, and why doesn't the other side have one?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562604):
Left hand side has the ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562615):
Because `separation_quotient α` is separated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562634):
This is the content of the second sentence

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562813):
I don't get it. Is this `completion (separation_quotient α) ≃ completion α` in fact (in math) a uniform ring isomorphism?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562826):
If so, why isn't `completion α` already separated?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562828):
A posteriori yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562856):
`completion α` is separated, but `α` isn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562875):
what goes wrong in the `ring (completion α)` instance if you drop the `separated α` property?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563061):
The map `coe : α -> completion α` is no longer injective

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563201):
does injectivity get used somewhere?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563225):
It is currently used in the proof everywhere, but maybe there is another proof. Johannes wrote that proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563266):
So I didn't think hard about it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563276):
but again a posteriori it seems like it is actually injective

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563283):
or else you wouldn't have that equiv

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563284):
No

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563289):
it's not injective

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563305):
`coe : α -> completion α` is injective if and only if `α` is separated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563316):
`separation_quotient α -> completion (separation_quotient α)` is injective

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563320):
ah, ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563321):
because `separation_quotient α` is separated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563370):
Do the definitions of `has_one` and `has_mul` at least work without `separated`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563397):
Probably

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563402):
maybe not actually

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563424):
sorry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563463):
You can define mul

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563466):
the issue is continuity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563544):
I'm checking this branch out, 1 sec

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563584):
anyway, my intuition is that you don't want to use transfer of structure like this. You should already be able to define the structure a priori, and you want to show that the equivalence respects the structure that is already there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563659):
In need to transport something along this equiv though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563662):
In particular, if we did transfer of structure your way, we would end up with two ring structures on `completion (separation_quotient A)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563689):
I'm ready to trow away any ring structure which is not compatible with the uniform structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563749):
I would guess the two ring structures are equal, but as we know that's not good enough for lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563873):
maths on a computer are so complicated...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565503):
Oh, this is evil: https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L263-L273

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565530):
I'm starting to see why you get heq goals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565593):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/heq.20hell.20again/near/135479776

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565596):
I already confessed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565687):
And I blame Danish thefts

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565707):
I think we need to be less constructive with our quotient constructions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565730):
the quotient ring construction for example should apply to any quotient map, not just the canonical one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 10 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565737):
What's evil about it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565743):
constructive is evil

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565745):
Type equality is evil

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565830):
Actually I tried to redeem with the next lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565858):
`eq_mpr_heq`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565859):
or previous lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565876):
the instance?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565889):
I have one lemma saying the quotients are equal but the other one says the setoids are equal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 10 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565899):
```quote
the quotient ring construction for example should apply to any quotient map, not just the canonical one
```
Do you mean so it would be easy to prove things about quotient rings that aren't constructed using `quotient`, like `zmod`, or `complex` using theorems about quotient rings?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565949):
I mean https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L255-L261

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565965):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565991):
as long as it acts like a quotient you should have quotient ring construction, quotient topology, etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566883):
```quote
as long as it acts like a quotient you should have quotient ring construction, quotient topology, etc
```
Is this something I'm meant to understand and convert into action, or was this you thinking aloud?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566901):
I don't really expect you to do anything on that front, it's mostly the fault of `quotient_ring` and such

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566962):
in the short term you might try to avoid casting between types but still unfold the fact that it is a quotient

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566972):
This quotient ring stuff seems tricky to get right. I was already refactored once

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566984):
indeed it's been refactored again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 10 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566993):
(module refactor touched this too)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567002):
I hope this completion stuff will help you get the refactor right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567198):
@**Kevin Buzzard** this conversation suggests that the perfectoid project is waiting for module refactor also on the ring completion side

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567217):
unless we find a way to finish that ring completion thing using evil lemmas and fake transport of structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 10 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567220):
One thing that really spurs me on with this whole thing is that as we try to do a different kind of mathematics to the kind that is typically done in a theorem prover, we run into issues which computer scientists seem to be able to solve. I am constantly feeling like both sides somehow benefit.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 10 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567284):
I did this once (cutting corners) with schemes, and now look at that project.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 10 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567295):
I say we do it right this time, however long it takes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567303):
Yes, this is exactly what I was thinking

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 10 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567311):
I'm not that busy in January...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567348):
Yeah, too bad we have orthogonal teaching schedules this year

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 10 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567464):
Mario, could we still have `congr'` trying to discharge goals using `proof_irrel` and `proof_irrel_heq` in order to cover my evil actions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 19 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136137596):
About transport of structure, Assia pointed out to me https://hal.inria.fr/hal-01559073 It seems it's actually relevant, despite the univalent stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 19 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136137628):
I notice that it helps publishing CS papers to promise stuff for free. It seems most papers titles in this area contain this promise.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Oct 19 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136138635):
Everybody loves free things! This is a good paper, I linked it previously in the "hott for newbies" thread, and Mario made a few comments.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rudi Grinberg (Oct 20 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136146880):
Where is this thread? The search is failing me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 20 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136146954):
It's [here](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/what.20is.20wrong.20with.20HoTT/near/135265404).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 20 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136147013):
As a side note, I've found that by default, searching Zulip doesn't turn up results from before I joined the server. However, it does if I additionally include "stream:general" or "stream:maths", etc.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 20 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136162441):
```quote
Everybody loves free things! This is a good paper, I linked it previously in the "hott for newbies" thread, and Mario made a few comments.
```
Thanks! I was sure it had been mentioned, I even told @**Assia Mahboubi** but I couldn't find it.


{% endraw %}
