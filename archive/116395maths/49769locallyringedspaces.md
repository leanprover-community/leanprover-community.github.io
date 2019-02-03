---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/49769locallyringedspaces.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [locally ringed spaces](https://leanprover-community.github.io/archive/116395maths/49769locallyringedspaces.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Sep 01 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133171105):
<p>In <a href="https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/locally_ringed.lean" target="_blank" title="https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/locally_ringed.lean"><code>lean-category-theory</code></a> I've added a definition of <code>locally_ringed_space</code>.</p>

#### [ Scott Morrison (Sep 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133171115):
<div class="codehilite"><pre><span></span>def structure_sheaf := sheaf.{v+1 v} α Ring

structure ringed_space :=
(𝒪 : structure_sheaf α)

structure locally_ringed_space extends ringed_space α :=
(locality : ∀ x : α, local_ring (stalk_at.{v+1 v} 𝒪 x).1)
</pre></div>

#### [ Scott Morrison (Sep 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133171148):
<p>and that seems to work (without even many sorries in earlier files :-)</p>

#### [ Scott Morrison (Sep 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133171149):
<p>But there's quite a bit of work to do in order to actually construct examples.</p>

#### [ Patrick Massot (Sep 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133171150):
<p>Yeah! Let's do that instead of trying to prove 2 is not a square in Z and get depressed</p>

#### [ Scott Morrison (Sep 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133171151):
<p>I thought I should try to do the sheaf of cts functions on a topological space.</p>

#### [ Scott Morrison (Sep 01 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133171156):
<p>Unfortunately there are going to be some difficulties.</p>

#### [ Scott Morrison (Sep 01 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133171180):
<p>In particular, at the moment <code>stalk_at</code> is just defined by:</p>
<div class="codehilite"><pre><span></span>def stalk_at (F : sheaf α V) (x : α) : V :=
colimit (F.near x)
</pre></div>

#### [ Scott Morrison (Sep 01 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133171203):
<p>Unfortunately general colimits of rings are pretty gross. My plan had been to construct coequalizers and coproducts in CommRing,</p>

#### [ Scott Morrison (Sep 01 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133171208):
<p>and then use general machinery to get colimits.</p>

#### [ Scott Morrison (Sep 01 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133171213):
<p>However if you do that, it's going to be very hard to show that a stalk of the structure sheaf is actually germs of continuous functions at that point.</p>

#### [ Scott Morrison (Sep 01 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133171271):
<p>I think I'll need to change <code>colimit</code> in the definition of <code>stalk_at</code> to <code>directed_colimit</code> (or <code>filtered_colimit</code>?), show that the poset of neighbourhood of <code>x</code> is actually directed, and then separately give a formula for directed colimits of commutative rings.</p>

#### [ Scott Morrison (Sep 01 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133171322):
<p>That formula for directed colimits, when applied to the sheaf of continuous functions, should look exactly like germs.</p>

#### [ Scott Morrison (Sep 01 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133171386):
<p>But if someone wants to do parts of this:</p>
<ul>
<li>define filtered categories, and filtered colimits</li>
<li>construct instances of <code>has_coproducts</code>, <code>has_coequalizers</code>, and/or <code>has_filtered_limits</code> for <code>Ring</code></li>
<li>show that continuous functions from a topological space to a topological ring forms a topological ring</li>
<li>define germs of continuous functions</li>
<li>show that germs are a local ring<br>
then it will get done faster. :-)</li>
</ul>

#### [ Patrick Massot (Sep 01 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133172131):
<p>I'd love to work on all that, but I really think I should focus on completions of rings, otherwise the perfectoid project will be really stuck</p>

#### [ Reid Barton (Sep 01 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133173786):
<p>I definitely plan to define at least filtered categories and colimits</p>

#### [ Scott Morrison (Sep 01 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133174627):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>, great! I just made a primitive first cut at filtered categories, and shows that inhabited directed posets are filtered.</p>

#### [ Scott Morrison (Sep 01 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133174638):
<p>I was going to start trying to define filtered limits in <code>Ring</code>, but I think jetlag has caught up with me.</p>

#### [ Reid Barton (Sep 01 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133174783):
<p>I'm currently on a train anyways, but is there a branch somewhere where I can follow along with the limits etc.?</p>

#### [ Scott Morrison (Sep 01 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133174852):
<p>It's all happening in <code>master</code> of <code>lean-category-theory</code></p>

#### [ Scott Morrison (Sep 01 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133174856):
<p>Although I'm committing less often because I'm trying to be better and checking that it compiles before pushing :-)</p>

#### [ Reid Barton (Sep 01 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133175067):
<p>Ah yes, I see it.</p>

#### [ Reid Barton (Sep 01 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133175080):
<p>Yes, that's a nice thing to do when you have users :)</p>

#### [ Reid Barton (Sep 01 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/locally%20ringed%20spaces/near/133175086):
<p>Though maybe I could just work in a branch of your library for now</p>


{% endraw %}
