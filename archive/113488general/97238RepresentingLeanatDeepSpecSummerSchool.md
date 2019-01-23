---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/97238RepresentingLeanatDeepSpecSummerSchool.html
---

## Stream: [general](index.html)
### Topic: [Representing Lean at DeepSpec Summer School](97238RepresentingLeanatDeepSpecSummerSchool.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 07 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129267892):
I've been invited to give a talk about Lean tactics at the upcoming DeepSpec summer school. It's a 5-10 minute talk that other participants do as well. I'd like to walk the audience through the writing of a tactic that I can contrast with Coq tactics. I thought of presenting tactics like `refine_struct` but it plays a lot with the internals and I'm not sure that a non-Lean-user would see the point. 

Now I'm thinking of presenting `tauto`. Yesterday I added the closure over symmetric relations before `tauto` starts so that when it sees `¬ a = b` and `b = a` in the assumptions, it can finish the goal right away. It would be an interesting contrast to Coq because I use a table of expressions for that closure. I can't begin to imagine how you'd do that in Ltac

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 07 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129267907):
What do you guys think? @**Mario Carneiro** , @**Scott Morrison** , @**Andrew Ashworth** , @**Johannes Hölzl**, @**Sean Leather**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 07 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129267986):
5-10 minutes talk?!?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 07 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129267993):
It's good that your name is not too long

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 07 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129267995):
Hahaha! :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 07 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129268039):
I'm thinking of shortening it to gain some time. What do you think of Sim-Hud?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 07 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129268050):
Also good that you work with Lean instead of Isabelle, it's much faster to say

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 07 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129268053):
CS conferences are really crazy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 07 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129268054):
To be fair, it's a summer  school

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 07 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129269349):
```quote
To be fair, it's a summer  school
```
Which means you get 20-30 minute talks instead of 60 or 90...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 07 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129269934):
There is something even more mysterious: if you can explain how to write Lean tactics in 5-10 minutes, when didn't you teach all of us?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 07 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270092):
Darn! The cat is out of the bag now!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 07 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270098):
Of course I can make anyone proficient in 5 minutes. I just don't like you guys :stuck_out_tongue_closed_eyes:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 07 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270140):
I think in 5 minutes, the best I can do is a sales pitch

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 07 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270148):
In mathematics, do people leave talks understanding the proof or merely wanting to read the paper?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 07 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270149):
With some luck they won't have time to ask what "disruptive proof assistant" means

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 07 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270152):
They leave talks wanting to have coffee

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 07 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270191):
and cakes if available

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 07 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270325):
Small world

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 07 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270338):
When the participants ask for cake, do they get cake or only a proof that cake exists somewhere?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 07 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270415):
They get a contradiction if they assume no cake exists. I guess Kenny wouldn't call that a proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 07 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270458):
But Kenny gets handed a recipe to make cake. Sure, it's convincing but it tastes like paper

