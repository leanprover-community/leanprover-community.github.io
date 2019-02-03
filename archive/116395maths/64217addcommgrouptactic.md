---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/64217addcommgrouptactic.html
---

## Stream: [maths](index.html)
### Topic: [add_comm_group tactic](64217addcommgrouptactic.html)

---


{% raw %}
#### [ Patrick Massot (Aug 08 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120526):
<p>Could we get a scaled down <code>ring</code> tactic handling <code>add_comm_group</code>? My current goal is <code>φ (x', y') - φ (x, y) =   φ (x', y₁) - φ (x, y₁) + (φ (x', y') - φ (x', y₁) - (φ (x, y') - φ (x, y₁))) + (φ (x₁, y') - φ (x₁, y)) + (φ (x, y') - φ (x, y) - (φ (x₁, y') - φ (x₁, y)))</code> and I can't face proving it by hand</p>

#### [ Mario Carneiro (Aug 08 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120596):
<p>it's on the todo list</p>

#### [ Patrick Massot (Aug 08 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120597):
<p>(this is a generalization of the thing I called a <code>ring</code> bug the other day because I forgot to tell Lean rings are commutative)</p>

#### [ Kevin Buzzard (Aug 08 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120730):
<p>Why not put a ring structure on your group? ;-)</p>

#### [ Kevin Buzzard (Aug 08 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120750):
<p>I think once someone showed me a group for which they could prove that this could not be done, unfortunately.</p>

#### [ Mario Carneiro (Aug 08 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120759):
<p>I think I know how to do modules; maybe you could use that</p>

#### [ Kevin Buzzard (Aug 08 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120813):
<p>Oh yeah, Q/Z. No possibility for 1 because it would be killed by some n, but not everything is killed by n</p>

#### [ Mario Carneiro (Aug 08 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120860):
<p>any non-unital ring satisfies this criterion</p>

#### [ Mario Carneiro (Aug 08 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120979):
<p>oh, actually I think you stand to gain just a bit by using a module tactic to solve abelian group problems</p>

#### [ Patrick Massot (Aug 08 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120989):
<p>It makes me think I should try the <code>rcases_hint</code> tactic now that you pushed it</p>

#### [ Mario Carneiro (Aug 08 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131121036):
<p>since it would be able to handle <code>(m * n) . x = m . (n . x)</code> where m,n : Z</p>

#### [ Mario Carneiro (Aug 08 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131121042):
<p>but a standard abelian group tactic can't deal with Z variables</p>

#### [ Mario Carneiro (Aug 08 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131121067):
<p>You should definitely try <code>rcases_hint</code>. I wrote 200 lines of lean in one sitting and tested it once at the end, and it seemed to work</p>

#### [ Mario Carneiro (Aug 08 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131121113):
<p>...at least it's type correct</p>

#### [ Johan Commelin (Aug 08 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131121736):
<p>Unfortunately, <code>add_comm_group</code> is not the same as <code>module \Z</code></p>

#### [ Mario Carneiro (Aug 08 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131121833):
<p>that's not a significant problem for a tactic, it can supply the instance when needed</p>

#### [ Mario Carneiro (Aug 08 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131121859):
<p>speaking of which, someone should prove that instance. All the hard work is already done</p>

#### [ Patrick Massot (Aug 08 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131123895):
<p>I can't use the depth parameter</p>

#### [ Mario Carneiro (Aug 08 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131123968):
<p>The syntax is <code>rcases_hint e {depth := 4}</code> or <code>rintro_hint {depth := 4}</code></p>

#### [ Mario Carneiro (Aug 08 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131123979):
<p>the lack of delimiter between <code>e</code> and the cfg may cause a problem</p>

#### [ Patrick Massot (Aug 08 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131123982):
<p>it complains <code>e</code> is not a function</p>

#### [ Patrick Massot (Aug 08 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131123992):
<p>so yes, a delimiter may help</p>

#### [ Mario Carneiro (Aug 08 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131123998):
<p>I'm open to suggestions</p>

#### [ Mario Carneiro (Aug 08 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131124080):
<p>would <code>rcases_hint e : 4</code> be too weird?</p>

#### [ Patrick Massot (Aug 08 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131124093):
<p>it's not meant to stay in the final Lean file anyway</p>

#### [ Patrick Massot (Aug 08 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131124101):
<p>so I would say it's fine</p>

#### [ Patrick Massot (Aug 08 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131124410):
<p>What about trying to guess better names?</p>

#### [ Johan Commelin (Aug 08 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131125303):
<blockquote>
<p>speaking of which, someone should prove that instance. All the hard work is already done</p>
</blockquote>
<p>Do we want an actual <code>instance</code>, or just 2 lemmas that convert either way. I think we can't have instances both ways, right? That would blow up the type class system <span class="emoji emoji-1f4a5" title="boom">:boom:</span></p>

#### [ Mario Carneiro (Aug 08 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131125618):
<p>We already have an instance one way, the other one should just be a def</p>

#### [ Mario Carneiro (Aug 08 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131125639):
<p>I changed <code>rcases_hint</code> to <code>rcases?</code>, <code>hint</code>  takes too long to write</p>

#### [ Mario Carneiro (Aug 08 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131125657):
<p>the depth thing should be fixed</p>

#### [ Patrick Massot (Aug 08 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131131422):
<blockquote>
<p>My current goal is <code>φ (x', y') - φ (x, y) =   φ (x', y₁) - φ (x, y₁) + (φ (x', y') - φ (x', y₁) - (φ (x, y') - φ (x, y₁))) + (φ (x₁, y') - φ (x₁, y)) + (φ (x, y') - φ (x, y) - (φ (x₁, y') - φ (x₁, y)))</code> and I can't face proving it by hand</p>
</blockquote>
<p>This was the last missing piece, so I decided to try it. After about 15 minutes of misery, I found out that <code>apply eq_of_sub_eq_zero, simp</code> does the trick!</p>

#### [ Kevin Buzzard (Aug 08 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131133991):
<blockquote>
<p>Unfortunately, <code>add_comm_group</code> is not the same as <code>module \Z</code></p>
</blockquote>
<p>OK so in the perfectoid mathlib pile-up there is <code>quotient_group.lean</code>, which I wrote based on <code>quotient_module.lean</code>. But what I actually want is <code>quotient_add_group.lean</code> so I can use it to improve <code>quotient_ring.lean</code>. I see three possibilities for making <code>quotient_add_group.lean</code> : </p>
<p>(1) just copy <code>quotient_group.lean</code> changing all the <code>*</code>s to <code>+</code>s etc. </p>
<p>(2) Some sort of tactic magic</p>
<p>(3) <em>deduce</em> the results from <code>quotient_module.lean</code> using the fact that, as we mathematicians say, an abelian group "is" a <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Z</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{Z}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.68889em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Z</span></span></span></span></span>-module.</p>
<p>Which is the best idea?</p>
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Do you mind if I put our names on the top of <code>quotient_group.lean</code> (remember -- I wrote it, basically copying from <code>quotient_module.lean</code> and then you fixed up a bunch of stuff and made it better) and PR it to mathlib via the community mathlib?</p>

#### [ Patrick Massot (Aug 08 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131134156):
<p>No problem, go ahead</p>


{% endraw %}
