---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39323Computationallyirrelevantproofs.html
---

## Stream: [general](index.html)
### Topic: [Computationally irrelevant proofs](39323Computationallyirrelevantproofs.html)

---


{% raw %}
#### [ AHan (Jan 04 2019 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154428282):
<p>Is there any tactics for handling program containing computationally irrelevant proof?<br>
Sometimes it's annoying that the non-trivial proof been replace by <code>_</code>...</p>

#### [ Johan Commelin (Jan 04 2019 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154428517):
<p>All proofs are irrelevant.</p>

#### [ Johan Commelin (Jan 04 2019 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154428527):
<p>That's a design choice.</p>

#### [ Johan Commelin (Jan 04 2019 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154428543):
<p>You shouldn't ever have to care about them again.</p>

#### [ Kenny Lau (Jan 04 2019 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154428601):
<p><code>set_option pp.proofs true</code></p>

#### [ AHan (Jan 04 2019 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154429152):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>  Why shouldn't I have to care about them again ? <br>
I mean what if I can proof my goal with just unfold definitions of some functions, but they're hided by <code>_</code>?</p>

#### [ AHan (Jan 04 2019 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154429205):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span>  Thanks this is exactly what i'm looking for !</p>

#### [ Mario Carneiro (Jan 04 2019 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154429544):
<p>The reason they are hidden is because it doesn't matter what is there; all proofs are definitionally equal (so if you unify with a term which has a different proof in that slot it doesn't matter), and proofs are computationally irrelevant (they do not affect control flow in any way) and they are literally thrown away by the VM.</p>

#### [ Mario Carneiro (Jan 04 2019 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154429587):
<p>if you can prove your goal only by unfolding definitions, then probably <code>rfl</code> or similar will finish the job</p>

#### [ AHan (Jan 04 2019 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154430687):
<p>Thanks for the explanation!</p>

#### [ petercommand (Jan 05 2019 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154464288):
<p>is there any rw tactic to deal with programs containing computationally irrelevant proofs? like, sometimes I want to rewrite a subterm in a goal, but  the type  of the computationally irrelevant proof depends on that subterm</p>

#### [ petercommand (Jan 05 2019 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154464297):
<p>and that makes it really annoying to manually rewrite that particular subterm</p>

#### [ petercommand (Jan 05 2019 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154464343):
<p>I would very much want a tactic to deal with this :3</p>

#### [ petercommand (Jan 05 2019 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154464356):
<p>like, a tactic that can rewrite the type of the proof simutaneously</p>

#### [ petercommand (Jan 05 2019 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154464407):
<p>(and the type of the terms of the type of the proof etc)</p>

#### [ Chris Hughes (Jan 05 2019 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154465158):
<p>There is <code>subst</code>, but that isn't too powerful at the moment.</p>

#### [ Mario Carneiro (Jan 05 2019 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154465872):
<p><code>simp</code> will do this, but probably not in the full generality you expect</p>

#### [ Mario Carneiro (Jan 05 2019 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154465873):
<p>the full problem is actually quite hard</p>

#### [ Mario Carneiro (Jan 05 2019 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154465880):
<p>but it is because of things like this that I try to avoid partial functions</p>

#### [ Mario Carneiro (Jan 05 2019 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154465883):
<p>there are a variety of tricks for totalizing functions so that there is no proof argument in the way</p>

#### [ Kenny Lau (Jan 05 2019 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154466144):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> does that include using <code>epsilon</code> instead of <code>some</code>?</p>

#### [ Mario Carneiro (Jan 05 2019 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154466359):
<p>I usually just pair <code>some</code> with an if statement</p>

#### [ Mario Carneiro (Jan 05 2019 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154466537):
<p>There are other options too, you aren't necessarily removing the proof argument. You could push the proof into the domain, making it a subtype domain like <code>finset</code>, or you could push it into the codomain producing an <code>roption</code> function</p>

#### [ Kevin Buzzard (Jan 05 2019 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154470598):
<p>This conversation is too abstract for me. Can someone post some examples of what people are saying should be avoided?</p>

#### [ Chris Hughes (Jan 05 2019 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154470962):
<p>Stuff like <code>log : Π z : ℂ, z ≠ 0 → ℂ </code> because then if I have <code>log x hx</code> in my goal and <code>x = y</code> it's hard to rewrite.</p>

#### [ Patrick Massot (Jan 05 2019 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154471014):
<p>Teaser: my talk in Amsterdam will feature this discussion on some example</p>

#### [ Kevin Buzzard (Jan 05 2019 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154471076):
<p>Oh yes, you can't rewrite because hx isn't a proof of the right thing. Thanks.</p>

#### [ Kevin Buzzard (Jan 05 2019 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154471078):
<p>The CS guys should just fix this</p>

#### [ Kevin Buzzard (Jan 05 2019 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154471130):
<p>It's a problem with their system. They shouldn't be working around it. We should be making maths the way mathematicians do it, not moaning about things like this. Why can't it be fixed? Can it be fixed in Lean 4?</p>

#### [ Patrick Massot (Jan 05 2019 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154471182):
<p>It seems the general case is hard for good reasons. But I agree Lean should have tactics that try heuristic or special cases</p>

#### [ Chris Hughes (Jan 05 2019 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154471192):
<p>I get the sense that it might be much easier to make something that works 95% of the time, and the last 5% is super hard.</p>

#### [ Scott Morrison (Jan 06 2019 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154499678):
<p>"Perfect is the enemy of good" has never been more appropriate!</p>

#### [ Kenny Lau (Jan 06 2019 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154509503):
<p>maybe write a tactic to do it</p>

#### [ Kevin Buzzard (Jan 06 2019 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154520838):
<p>I don't understand what's difficult here, but I'm sure there is something difficult because I'm aware that this issue comes up now and again</p>

#### [ Kevin Buzzard (Jan 06 2019 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154520840):
<p>It feels the same as the "replace this ring with this isomorphic ring" issue</p>

#### [ petercommand (Jan 07 2019 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154551482):
<blockquote>
<p>It feels the same as the "replace this ring with this isomorphic ring" issue</p>
</blockquote>
<p>I would think that "replace this ring with this isomorphic ring" would be even harder than substituting propositionally equal term</p>

#### [ petercommand (Jan 07 2019 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154551494):
<p>since two isomorphic rings are not necessarily propositionally equal</p>

#### [ Kevin Buzzard (Jan 07 2019 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154552001):
<p>Right! Mathematicians have a code of honour where we only do things to rings which would work if you replaced the ring with an isomorphic one</p>

#### [ Kenny Lau (Jan 07 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154554248):
<p>so you mean functors</p>

#### [ Joe Hendrix (Jan 11 2019 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154941811):
<p>To resurrect this a bit, has there been a tactic that just introduces casts as needed?   In the log example, with <code>log : Π z : ℂ, z ≠ 0 → ℂ</code>, if you have the term <code>log x h</code> and equality<code>e: x = y</code>, the tactic could rewrite <code>log x h</code> to <code>log y (eq.rec h e)</code>.    I've tried this on an ad-hoc basis and sometimes run into problems later dealing with terms like <code>(eq.rec h e)</code>, but perhaps a tactic could systematically rewrite through rec.</p>

#### [ Chris Hughes (Jan 11 2019 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154942122):
<p><code>subst</code> already does this but only for local constants. Apparently the problem is very hard in general.</p>

#### [ Mario Carneiro (Jan 11 2019 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Computationally%20irrelevant%20proofs/near/154948114):
<p>You can often get <code>simp</code> to do this, or <code>conv</code>, because they use congruence lemmas for rewriting</p>


{% endraw %}
