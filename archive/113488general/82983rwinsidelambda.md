---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/82983rwinsidelambda.html
---

## Stream: [general](index.html)
### Topic: [rw inside lambda](82983rwinsidelambda.html)

---


{% raw %}
#### [ Kenny Lau (Sep 09 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133624964):
<p>from my experience, <code>simp</code> can change things inside lambda, but <code>rw</code> cannot. Is there a way to bypass this and let <code>rw</code> change inside lambda?</p>

#### [ Mario Carneiro (Sep 09 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133624971):
<p><code>conv</code> + <code>rw</code></p>

#### [ Reid Barton (Sep 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133625661):
<p>Also see topic <a href="#narrow/stream/113488-general/subject/rw.20under.20lambda/near/126107890" title="#narrow/stream/113488-general/subject/rw.20under.20lambda/near/126107890">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/rw.20under.20lambda/near/126107890</a> and the more verbose topic <a href="#narrow/stream/113488-general/subject/Why.20can't.20.60rw.60.20look.20inside.20lambda.20expressions.3F/near/130212033" title="#narrow/stream/113488-general/subject/Why.20can't.20.60rw.60.20look.20inside.20lambda.20expressions.3F/near/130212033">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/Why.20can't.20.60rw.60.20look.20inside.20lambda.20expressions.3F/near/130212033</a></p>

#### [ Kenny Lau (Sep 10 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133640326):
<p>so exactly which tactics are avaiblale inside <code>conv</code>?</p>

#### [ Kevin Buzzard (Sep 10 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133641348):
<p>rw</p>

#### [ Kenny Lau (Sep 10 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133641426):
<p>I mean, a complete list of tactics available inside <code>conv</code></p>

#### [ Kevin Buzzard (Sep 10 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133641504):
<p>There's probably a file in core which lists them. There's to_lhs, something called something like whnf and you might want to skim Patrick's docs</p>

#### [ Kevin Buzzard (Sep 10 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133641835):
<p><a href="https://github.com/leanprover/lean/blob/master/library/init/meta/converter/interactive.lean" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/meta/converter/interactive.lean">https://github.com/leanprover/lean/blob/master/library/init/meta/converter/interactive.lean</a></p>

#### [ Kevin Buzzard (Sep 10 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133641838):
<p>Maybe that's the definitive answer</p>

#### [ Kevin Buzzard (Sep 10 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133641952):
<p>Funext, change, simp and dsimp</p>

#### [ Kevin Buzzard (Sep 10 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133642024):
<p><a href="https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md">https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md</a></p>

#### [ Kevin Buzzard (Sep 10 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133642027):
<p>Has a couple of nice tricks</p>

#### [ Kenny Lau (Sep 10 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133642625):
<p>well I would like to be able to use <code>apply/exact/refine</code> inside <code>conv</code></p>

#### [ Kenny Lau (Sep 10 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133642672):
<p><code>conv</code> inside <code>conv</code> would also be useful</p>

#### [ Kenny Lau (Sep 10 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133642676):
<p>I feel like <code>conv</code> has a lot of potential to be the most powerful tactic ever</p>

#### [ Kenny Lau (Sep 10 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133644854):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I don't understand why there's no basic tactics (i.e. <code>exact</code>) inside conv</p>

#### [ Mario Carneiro (Sep 10 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645090):
<p><code>conv</code> is a different monad from <code>tactic</code></p>

#### [ Mario Carneiro (Sep 10 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645145):
<p><code>exact</code> doesn't even make sense</p>

#### [ Kenny Lau (Sep 10 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645146):
<p>I mean, why didn't we implement exact inside conv</p>

#### [ Kenny Lau (Sep 10 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645150):
<p>conv is just a bunch of congr_arg and funext right</p>

#### [ Mario Carneiro (Sep 10 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645172):
<p>the tactic state in the conv monad is basically <code>?p : X = ?m</code> where <code>?p</code> and <code>?m</code> are to be determined</p>

#### [ Kenny Lau (Sep 10 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645178):
<p>if we have <code>a + b = c + d</code>, and I do <code>conv { to_lhs, congr, skip, }</code> then the current state is <code>a + b = a + ?m</code> right</p>

#### [ Kenny Lau (Sep 10 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645187):
<p>if I do <code>exact (sorry : b = foo b)</code> then I can tell Lean exactly that <code>?m</code> should be <code>foo b</code> right</p>

#### [ Mario Carneiro (Sep 10 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645201):
<p>by comparison to the regular tactic state which is just <code>?m : t</code></p>

#### [ Mario Carneiro (Sep 10 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645300):
<p>I think <code>update_lhs</code> does that</p>

#### [ Johan Commelin (Sep 10 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645375):
<p>I've never heard about that one. Sounds good!</p>

#### [ Johan Commelin (Sep 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645390):
<p>Can you also <em>zoom out</em> in <code>conv</code>?</p>

#### [ Johan Commelin (Sep 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645411):
<p>You zoom in with <code>congr</code> and <code>funext</code>. But I sometimes also want to zoom out again.</p>

#### [ Mario Carneiro (Sep 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645430):
<p>No, zoom out doesn't make sense</p>

#### [ Mario Carneiro (Sep 10 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645496):
<p>what is possible instead is a split lhs/rhs that produces multiple subgoals</p>

#### [ Mario Carneiro (Sep 10 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645527):
<p>also, lhs/rhs is so passe. We need rcases patterns in conv!</p>

#### [ Kenny Lau (Sep 10 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645626):
<p>what is update_lhs?</p>

#### [ Mario Carneiro (Sep 10 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645646):
<p>I guess it is not an interactive command, but it is available as a conv tactic</p>

#### [ Mario Carneiro (Sep 10 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645670):
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">update_lhs</span> <span class="o">(</span><span class="n">new_lhs</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:</span> <span class="n">conv</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">transitivity</span><span class="o">,</span>
   <span class="n">rhs</span> <span class="bp">&gt;&gt;=</span> <span class="n">unify</span> <span class="n">new_lhs</span><span class="o">,</span>
   <span class="n">exact</span> <span class="n">h</span><span class="o">,</span>
   <span class="n">t</span> <span class="err">←</span> <span class="n">target</span> <span class="bp">&gt;&gt;=</span> <span class="n">instantiate_mvars</span><span class="o">,</span>
   <span class="n">change</span> <span class="n">t</span>
</pre></div>

#### [ Johan Commelin (Sep 10 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645872):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Why would zoom out not make sense? If I drill down into a nested sum, do some <code>rw</code> there, then I would want to zoom out again and play with the sum that is 1 level up.</p>

#### [ Mario Carneiro (Sep 10 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645979):
<p>As I said, the conv monad has a state which is <code>?p : X = ?m</code>. If you zoom in then <code>?m</code> is assigned, so you can't return to it any more than you can rewind in a proof</p>

#### [ Mario Carneiro (Sep 10 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133646109):
<p>I think that <code>to_lhs</code> would make more sense as a tactic combinator, i.e. <code>to_lhs { &lt;conv&gt; }, &lt;conv&gt;</code></p>

#### [ Mario Carneiro (Sep 10 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133646119):
<p>that would allow you to return to the outer context in the second part</p>

#### [ Kenny Lau (Sep 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133646183):
<p>also if I go deep inside using <code>conv</code> then all the variables have the same name and I can't even <code>dedup</code></p>

#### [ Mario Carneiro (Sep 10 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133646218):
<p>note that <code>find</code> is actually a combinator like this inside conv, so you can use it to temporarily zoom in</p>

#### [ Mario Carneiro (Sep 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133646274):
<p>however, find patterns never work the way I want them to</p>


{% endraw %}
