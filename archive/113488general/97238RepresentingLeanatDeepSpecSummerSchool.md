---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/97238RepresentingLeanatDeepSpecSummerSchool.html
---

## Stream: [general](index.html)
### Topic: [Representing Lean at DeepSpec Summer School](97238RepresentingLeanatDeepSpecSummerSchool.html)

---


{% raw %}
#### [ Simon Hudon (Jul 07 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129267892):
<p>I've been invited to give a talk about Lean tactics at the upcoming DeepSpec summer school. It's a 5-10 minute talk that other participants do as well. I'd like to walk the audience through the writing of a tactic that I can contrast with Coq tactics. I thought of presenting tactics like <code>refine_struct</code> but it plays a lot with the internals and I'm not sure that a non-Lean-user would see the point. </p>
<p>Now I'm thinking of presenting <code>tauto</code>. Yesterday I added the closure over symmetric relations before <code>tauto</code> starts so that when it sees <code>¬ a = b</code> and <code>b = a</code> in the assumptions, it can finish the goal right away. It would be an interesting contrast to Coq because I use a table of expressions for that closure. I can't begin to imagine how you'd do that in Ltac</p>

#### [ Simon Hudon (Jul 07 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129267907):
<p>What do you guys think? <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> , <span class="user-mention" data-user-id="110087">@Scott Morrison</span> , <span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> , <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>, <span class="user-mention" data-user-id="110045">@Sean Leather</span></p>

#### [ Patrick Massot (Jul 07 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129267986):
<p>5-10 minutes talk?!?</p>

#### [ Patrick Massot (Jul 07 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129267993):
<p>It's good that your name is not too long</p>

#### [ Simon Hudon (Jul 07 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129267995):
<p>Hahaha! :D</p>

#### [ Simon Hudon (Jul 07 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129268039):
<p>I'm thinking of shortening it to gain some time. What do you think of Sim-Hud?</p>

#### [ Patrick Massot (Jul 07 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129268050):
<p>Also good that you work with Lean instead of Isabelle, it's much faster to say</p>

#### [ Patrick Massot (Jul 07 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129268053):
<p>CS conferences are really crazy</p>

#### [ Simon Hudon (Jul 07 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129268054):
<p>To be fair, it's a summer  school</p>

#### [ Johan Commelin (Jul 07 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129269349):
<blockquote>
<p>To be fair, it's a summer  school</p>
</blockquote>
<p>Which means you get 20-30 minute talks instead of 60 or 90...</p>

#### [ Patrick Massot (Jul 07 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129269934):
<p>There is something even more mysterious: if you can explain how to write Lean tactics in 5-10 minutes, when didn't you teach all of us?</p>

#### [ Simon Hudon (Jul 07 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270092):
<p>Darn! The cat is out of the bag now!</p>

#### [ Simon Hudon (Jul 07 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270098):
<p>Of course I can make anyone proficient in 5 minutes. I just don't like you guys <span class="emoji emoji-1f61d" title="stuck out tongue closed eyes">:stuck_out_tongue_closed_eyes:</span></p>

#### [ Simon Hudon (Jul 07 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270140):
<p>I think in 5 minutes, the best I can do is a sales pitch</p>

#### [ Simon Hudon (Jul 07 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270148):
<p>In mathematics, do people leave talks understanding the proof or merely wanting to read the paper?</p>

#### [ Patrick Massot (Jul 07 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270149):
<p>With some luck they won't have time to ask what "disruptive proof assistant" means</p>

#### [ Patrick Massot (Jul 07 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270152):
<p>They leave talks wanting to have coffee</p>

#### [ Patrick Massot (Jul 07 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270191):
<p>and cakes if available</p>

#### [ Simon Hudon (Jul 07 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270325):
<p>Small world</p>

#### [ Simon Hudon (Jul 07 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270338):
<p>When the participants ask for cake, do they get cake or only a proof that cake exists somewhere?</p>

#### [ Patrick Massot (Jul 07 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270415):
<p>They get a contradiction if they assume no cake exists. I guess Kenny wouldn't call that a proof.</p>

#### [ Simon Hudon (Jul 07 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Representing%20Lean%20at%20DeepSpec%20Summer%20School/near/129270458):
<p>But Kenny gets handed a recipe to make cake. Sure, it's convincing but it tastes like paper</p>


{% endraw %}
