---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74681tacticforsettheoretictrivialities.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [tactic for set-theoretic trivialities](https://leanprover-community.github.io/archive/113488general/74681tacticforsettheoretictrivialities.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (May 21 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866089):
<p>I am beginning to tire of goals of the form <code>Ua ∩ Ub ∩ Uc ⊆ Ua ∩ Ub ∩ (Ua ∩ Uc)</code></p>

#### [ Kevin Buzzard (May 21 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866091):
<p>Is there a tactic which solves them?</p>

#### [ Kevin Buzzard (May 21 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866093):
<p>[these are sets]</p>

#### [ Kevin Buzzard (May 21 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866107):
<p>[let me stress that I can solve them, it's just the novelty is wearing off]</p>

#### [ Andrew Ashworth (May 21 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866109):
<p><code>by finish</code>?</p>

#### [ Kevin Buzzard (May 21 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866116):
<p>didn't work for me for this one</p>

#### [ Kevin Buzzard (May 21 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866165):
<p>cc and simp don't work either</p>

#### [ Kevin Buzzard (May 21 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866176):
<p>[Prediction : in about 8 hours Scott wakes up and remarks that one of his secret tactics does the job immediately]</p>

#### [ Kenny Lau (May 21 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866279):
<p><code>solve_by_elim</code>?</p>

#### [ Kevin Buzzard (May 21 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866331):
<p>Note that any such tactic will have to deal with the fact that <code>exact ⟨Ha,Hb,⟨Ha,Hc⟩⟩</code> is not a proof of <code>y ∈ Ua ∩ Ub ∩ (Ua ∩ Uc)</code> because of stupid left associativity of \cap</p>

#### [ Kevin Buzzard (May 21 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866342):
<p><code>solve_by_elim</code> doesn't work</p>

#### [ Mario Carneiro (May 21 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866351):
<p>I think <code>finish</code> was intended to work on those goals</p>

#### [ Mario Carneiro (May 21 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866401):
<p>but you may need to use its options</p>

#### [ Mario Carneiro (May 21 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866429):
<div class="codehilite"><pre><span></span>example {α} (Ua Ub Uc : set α) : Ua ∩ Ub ∩ Uc ⊆ Ua ∩ Ub ∩ (Ua ∩ Uc) :=
by simp [set.subset_def] {contextual := tt}
</pre></div>

#### [ Andrew Ashworth (May 21 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866528):
<p>it reminds me I don't know what <code>finish</code> solves. Does it work on any boolean algebra?</p>

#### [ Patrick Massot (May 21 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866532):
<p><code>by finish[set.subset_def]</code> also works</p>

#### [ Mario Carneiro (May 21 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866533):
<p>it works on the boolean algebra of propositions...</p>

#### [ Mario Carneiro (May 21 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866539):
<p>that's why <code>subset_def</code> is needed here</p>

#### [ Kenny Lau (May 21 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866767):
<p>people just bloody abusing <code>finish</code></p>

#### [ Kevin Buzzard (May 21 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866773):
<p>We're too classical for you</p>

#### [ Kevin Buzzard (May 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866779):
<p>Do you think it's true in constructive maths?</p>

#### [ Kevin Buzzard (May 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866780):
<p>I would have no idea :-)</p>

#### [ Kenny Lau (May 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866782):
<p>of course it is</p>

#### [ Kevin Buzzard (May 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866783):
<p>:-)</p>

#### [ Kenny Lau (May 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866784):
<p>they're literally the same set</p>

#### [ Kevin Buzzard (May 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866786):
<p>yeah but you never know with this constructive maths thing</p>

#### [ Patrick Massot (May 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866787):
<p>Using <code>finish</code> does not only finishes the goal. It also conveys the meaning that the goal is now something we don't want to discuss at all</p>

#### [ Kevin Buzzard (May 21 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866789):
<p>I mean not not P is literally the same as P, right?</p>

#### [ Kenny Lau (May 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866830):
<p><em>t r i g g e r e d</em></p>

#### [ Kevin Buzzard (May 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866833):
<p>Shouldn't you be revising for mechanics?</p>

#### [ Kenny Lau (May 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866836):
<p>I see that you're proving mul_add</p>

#### [ Kenny Lau (May 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866838):
<p>can't you prove that the two sets are equal instead?</p>

#### [ Patrick Massot (May 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866839):
<p>Shouldn't you be marking?</p>

#### [ Kenny Lau (May 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866840):
<p>I think equality is eaiser to prove</p>

#### [ Kenny Lau (May 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866842):
<blockquote>
<p>Shouldn't you be marking?</p>
</blockquote>
<p>oooooooh</p>

#### [ Kevin Buzzard (May 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866843):
<p>I've just proved something is a ring!</p>

#### [ Kevin Buzzard (May 21 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866848):
<p>I'm sitting on the tube platform at South Ken, completely elated</p>

#### [ Kevin Buzzard (May 21 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866853):
<p>[:= v happy]</p>

#### [ Kevin Buzzard (May 21 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866855):
<p>Now if only someone had proved that a product of rings was a ring</p>

#### [ Kevin Buzzard (May 21 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866886):
<p>oh wait</p>

#### [ Kevin Buzzard (May 21 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866904):
<p>I think O_X(U) is a ring!</p>

#### [ Kevin Buzzard (May 21 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866905):
<p>I still have to prove restriction is a ring homomorphism though</p>

#### [ Kevin Buzzard (May 21 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866906):
<p>I will save that for after some marking</p>

#### [ Kevin Buzzard (May 21 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866918):
<p>What I am actually pleased about is that I seriously engaged with quotient types for the first time in my life, and I have come out alive</p>

#### [ Kevin Buzzard (May 21 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866962):
<p>Why is quot.lift called that?</p>

#### [ Kevin Buzzard (May 21 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866964):
<p>It's the opposite of a lift, the way things are set up in my brain</p>

#### [ Kevin Buzzard (May 21 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866965):
<p>It's a descent</p>

#### [ Patrick Massot (May 21 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866966):
<p>I remember being puzzled by this terminology while reading TPIL</p>

#### [ Kevin Buzzard (May 21 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866973):
<p>I think that this observation was genuinely something which added to my confusion when looking at quotient type stuff</p>

#### [ Kevin Buzzard (May 21 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866975):
<p>This name was not at all intuitive for me</p>

#### [ Patrick Massot (May 21 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866976):
<p>Obviously</p>

#### [ Kevin Buzzard (May 21 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866983):
<p>Is this a CS thing Patrick?</p>

#### [ Patrick Massot (May 21 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866984):
<p>No idea</p>

#### [ Patrick Massot (May 21 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126866985):
<p>Just crazyness if you ask me</p>

#### [ Kevin Buzzard (May 21 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126867031):
<p>Anyway, we live and learn, and I've certainly learnt something over the last couple of days. Thanks to everyone that helped. I genuinely feel like a better Leaner.</p>

#### [ Sean Leather (May 21 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20set-theoretic%20trivialities/near/126867301):
<p><del>Leaner</del>Lea(r)ner</p>


{% endraw %}
