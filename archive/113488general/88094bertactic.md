---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88094bertactic.html
---

## Stream: [general](index.html)
### Topic: [über-tactic](88094bertactic.html)

---


{% raw %}
#### [ Patrick Massot (Oct 03 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098666):
<p>I'm trying to automate my demo file, for comparison. Is there any reason not to try to write a monster tactic trying all automation we have (except speed reason)? Something like:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">do_it</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span> <span class="n">do</span>
<span class="bp">`</span><span class="o">[</span><span class="n">try</span> <span class="o">{</span><span class="n">ext</span><span class="o">}],</span>
<span class="bp">`</span><span class="o">[</span><span class="n">try</span> <span class="o">{</span><span class="n">split</span><span class="o">}],</span>
<span class="bp">`</span><span class="o">[</span><span class="n">apply_eq</span><span class="o">],</span>
<span class="bp">`</span><span class="o">[</span><span class="n">all_goals</span> <span class="o">{</span><span class="n">finish</span> <span class="bp">&lt;|&gt;</span> <span class="n">tauto</span> <span class="bp">&lt;|&gt;</span> <span class="n">tidy</span><span class="o">}]</span> <span class="bp">&lt;|&gt;</span> <span class="n">failure</span>
</pre></div>


<p>can do everything that should be automatic in my demo file. It could even do more without the tidy bug.</p>

#### [ Patrick Massot (Oct 03 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098676):
<p>It uses Simon's apply function equalities tactic</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span>
<span class="n">meta</span> <span class="n">def</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">apply_eq</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">l</span> <span class="err">←</span> <span class="n">local_context</span><span class="o">,</span>
   <span class="n">l</span><span class="bp">.</span><span class="n">mmap</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">try</span> <span class="err">$</span> <span class="n">do</span> <span class="o">{</span>
     <span class="bp">`</span><span class="o">(</span><span class="err">%%</span><span class="n">x</span> <span class="bp">=</span> <span class="err">%%</span><span class="n">y</span><span class="o">)</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">h</span><span class="o">,</span>
     <span class="o">(</span><span class="n">vs</span><span class="o">,</span><span class="n">t</span><span class="o">)</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">x</span> <span class="bp">&gt;&gt;=</span> <span class="n">mk_local_pis</span><span class="o">,</span>
     <span class="n">p&#39;</span> <span class="err">←</span> <span class="n">mk_app</span> <span class="bp">`</span><span class="n">eq</span> <span class="o">[</span><span class="n">x</span><span class="bp">.</span><span class="n">mk_app</span> <span class="n">vs</span><span class="o">,</span> <span class="n">y</span><span class="bp">.</span><span class="n">mk_app</span> <span class="n">vs</span><span class="o">],</span>
     <span class="n">p&#39;</span> <span class="err">←</span> <span class="n">pis</span> <span class="n">vs</span> <span class="n">p&#39;</span><span class="o">,</span>
     <span class="n">assert</span> <span class="o">(</span><span class="n">to_string</span> <span class="n">h</span><span class="bp">.</span><span class="n">local_pp_name</span> <span class="bp">++</span> <span class="s2">&quot;_ev&quot;</span> <span class="o">:</span> <span class="n">string</span><span class="o">)</span> <span class="n">p&#39;</span><span class="o">,</span>
     <span class="n">vs</span> <span class="err">←</span> <span class="n">intros</span><span class="o">,</span>
     <span class="n">vs</span><span class="bp">.</span><span class="n">reverse</span><span class="bp">.</span><span class="n">mmap</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">v</span><span class="o">,</span>
       <span class="n">do</span> <span class="n">revert</span> <span class="n">v</span><span class="o">,</span>
          <span class="n">applyc</span> <span class="bp">``</span><span class="n">congr_fun</span><span class="o">),</span>
     <span class="n">exact</span> <span class="n">h</span> <span class="o">},</span>
  <span class="n">return</span> <span class="o">()</span>
</pre></div>

#### [ Scott Morrison (Oct 03 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098839):
<p>Patrick, you should investigate whether we could put <code>finish</code> or <code>tauto</code> inside <code>tidy</code>. I suspect they would be fine, I've actually never used them!</p>

#### [ Johan Commelin (Oct 03 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098888):
<p>While you're at it, you should also add <code>cc</code> and <code>linarith</code> to <code>über</code>.</p>

#### [ Scott Morrison (Oct 03 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098891):
<p>(A big downside, by the way, of using <code>tidy</code> merely as a tactic script writing tool is that we don't build up a library of test cases for it, making it harder to safely tweak.)</p>

#### [ Simon Hudon (Oct 03 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098893):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span>, didn't you add congr_fun to <code>solve_by_elim</code> recently?</p>

#### [ Scott Morrison (Oct 03 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098899):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>, yes, but the PR hasn't landed yet.</p>

#### [ Simon Hudon (Oct 03 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098908):
<p>Aaaaah! That's why!</p>

#### [ Johan Commelin (Oct 03 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098947):
<blockquote>
<p>(A big downside, by the way, of using <code>tidy</code> merely as a tactic script writing tool is that we don't build up a library of test cases for it, making it harder to safely tweak.)</p>
</blockquote>
<p>We need caching.</p>

#### [ Scott Morrison (Oct 03 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098949):
<p>(I need to deal with your suggestion to use <code>with</code> when passing attributes.)</p>

#### [ Scott Morrison (Oct 03 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098965):
<p>(I've also realised there is a mistake in <code>solve_by_elim</code> when dealing with multiple sub-goals, more on that later :-)</p>

#### [ Simon Hudon (Oct 03 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135098977):
<p>I keep getting confused with the PRs that haven't been merged yet</p>

#### [ Simon Hudon (Oct 03 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099176):
<blockquote>
<p>I'm trying to automate my demo file, for comparison. Is there any reason not to try to write a monster tactic trying all automation we have (except speed reason)?</p>
</blockquote>
<p>Because proofs in first order logic and anything more expressive is undecidable, you can't build a tactic so that, when it fails, you can say "it tried everything". You could always try a little harder, maybe one more call to <code>ext</code> and then <code>simp</code> will do it.</p>

#### [ Scott Morrison (Oct 03 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099531):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>, another way to achieve this is to add the @[tidy] annotation to tactics that you want to try.</p>

#### [ Johan Commelin (Oct 03 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099543):
<p>Well, maybe if it fails we could conclude "it tried everything that is straightforward up to a reasonable depth". And then "probably this proof needs an <em>idea</em>".</p>

#### [ Scott Morrison (Oct 03 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099562):
<p>For example, if you write <code>@[tidy] meta def la := `[linarith]</code>, then after that <code>tidy</code> will also try calling linarith.</p>

#### [ Scott Morrison (Oct 03 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099620):
<p>You could make an import, for example, that super-charged <code>tidy</code> with all these other things.</p>

#### [ Johan Commelin (Oct 03 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099623):
<p>Can you just <code>local attibute [tidy] linarith</code>?</p>

#### [ Scott Morrison (Oct 03 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099636):
<p>Probably not quite that: the <code>[tidy]</code> attribute has to be on a <code>tactic unit</code> or <code>tactic string</code>.</p>

#### [ Scott Morrison (Oct 03 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099643):
<p>Any arguments (e.g. to interactive tactics) will break it.</p>

#### [ Scott Morrison (Oct 03 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099649):
<p>Although this is completely fixable.</p>

#### [ Scott Morrison (Oct 03 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099666):
<p>(and we should do so at some point...)</p>

#### [ Mario Carneiro (Oct 03 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099892):
<p>I think super-tactics like this are not uncommon</p>

#### [ Mario Carneiro (Oct 03 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099919):
<p>Everyone wants to be the one tactic to rule them all</p>

#### [ Mario Carneiro (Oct 03 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135099975):
<p>I think <code>tidy</code> has too unassuming a name for a supertactic</p>

#### [ Mario Carneiro (Oct 03 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100008):
<p>It should be called <code>crush</code> or <code>blast</code> or some similarly violent thing</p>

#### [ Simon Hudon (Oct 03 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100025):
<p>What about <code>nuke</code>?</p>

#### [ Simon Hudon (Oct 03 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100094):
<p>Either that or <code>solve_violently</code></p>

#### [ Johan Commelin (Oct 03 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100271):
<p>We're all still waiting for Mjölnir</p>

#### [ Simon Hudon (Oct 03 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100412):
<p>I was always disappointed by what <code>destruct</code> does because it feels like a synonym to <code>destroy</code>. And now we can't use <code>destroy</code> as the name of a super tactic.</p>

#### [ Simon Hudon (Oct 03 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100421):
<p>But we can use <code>annihilate</code></p>

#### [ Johan Commelin (Oct 03 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100510):
<p>You know Grothendieck's parable about proving strategies?</p>

#### [ Johan Commelin (Oct 03 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100516):
<p>We should also have <code>soak</code></p>

#### [ Johan Commelin (Oct 03 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100524):
<p>But it is very time-expensive</p>

#### [ Simon Hudon (Oct 03 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100529):
<p>I do not. Please educate me</p>

#### [ Johan Commelin (Oct 03 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100536):
<p>Might take a couple of years to run. But it will produce a couple 1000 pages of beautiful math in the end....</p>

#### [ Johan Commelin (Oct 03 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100575):
<p>I'm searching for it... give me a second</p>

#### [ Simon Hudon (Oct 03 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100632):
<p>:D</p>

#### [ Simon Hudon (Oct 03 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100648):
<p>A similar approach to <code>by grad_student</code></p>

#### [ Johan Commelin (Oct 03 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100679):
<p><a href="https://mathoverflow.net/a/7156" target="_blank" title="https://mathoverflow.net/a/7156">https://mathoverflow.net/a/7156</a></p>

#### [ Johan Commelin (Oct 03 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100757):
<p>I think <code>soak</code> or <code>immerse</code> is different from <code>grad_student</code>. It is even more expensive...</p>

#### [ Scott Morrison (Oct 03 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100786):
<p><span class="emoji emoji-1f951" title="avocado">:avocado:</span></p>

#### [ Simon Hudon (Oct 03 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135100881):
<p>I love it :D That's what I call putting a problem on the back burner</p>

#### [ Patrick Massot (Oct 03 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104489):
<p>Blindly adding the tidy attribute to tactics only gives me deterministic timeout</p>

#### [ Patrick Massot (Oct 03 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104631):
<p>especially with norm_num</p>

#### [ Patrick Massot (Oct 03 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104661):
<p>and apply_eq</p>

#### [ Simon Hudon (Oct 03 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104737):
<p><code>apply_eq</code> never fails and I believe neither does <code>norm_num</code>. Does <code>tidy</code> repeated try its tactics?</p>

#### [ Patrick Massot (Oct 03 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104776):
<p>Wow, you're still not sleeping? Did you decide to simply skip that step?</p>

#### [ Simon Hudon (Oct 03 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104850):
<p>Yeah, I'll pick it up later. I have an appointment this morning so at some point I got afraid I would sleep right passed it if I managed to fall asleep so I got out of bed</p>

#### [ Scott Morrison (Oct 03 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104875):
<p>Yes, tidy relies on the "do something or fail" model for tactics.</p>

#### [ Scott Morrison (Oct 03 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104876):
<p>Speaking of sleeping.</p>

#### [ Patrick Massot (Oct 03 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135104959):
<p>Do you still see a way to make use of norm_num inside tidy?</p>

#### [ Simon Hudon (Oct 03 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105003):
<p>You can write a tactic that checks if progress was made and fails if none was made</p>

#### [ Patrick Massot (Oct 03 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105026):
<p>how? comparing the new goal with previous goal?</p>

#### [ Scott Morrison (Oct 03 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105072):
<p>And a better solution is to change the behaviour of norm_num... Who wants tactics to silently fail, anyway? :-)</p>

#### [ Scott Morrison (Oct 03 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105092):
<p>Exactly. It's a fun exercise, perhaps the first tactic I ever wrote. :-)</p>

#### [ Simon Hudon (Oct 03 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105096):
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">guard_progress</span> <span class="o">(</span><span class="n">tac</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">gs</span> <span class="bp">&lt;-</span> <span class="n">get_goals</span><span class="o">,</span>
   <span class="n">tac</span><span class="o">,</span>
   <span class="n">gs&#39;</span> <span class="bp">&lt;-</span> <span class="n">get_goals</span><span class="o">,</span>
   <span class="n">guard</span> <span class="o">(</span><span class="n">gs</span> <span class="bp">≠</span> <span class="n">gs&#39;</span><span class="o">)</span>
</pre></div>

#### [ Patrick Massot (Oct 03 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105120):
<p>It was too fun for Simon to resist</p>

#### [ Simon Hudon (Oct 03 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105126):
<blockquote>
<p>Exactly. It's a fun exercise, perhaps the first tactic I ever wrote. :-)</p>
</blockquote>
<p>Which one?</p>

#### [ Simon Hudon (Oct 03 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105132):
<p>I'm so greedy. Sorry</p>

#### [ Patrick Massot (Oct 03 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105229):
<p>But you are both maligning norm_num, it can actually fail</p>

#### [ Simon Hudon (Oct 03 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105261):
<p>I can make up for this theft. <span class="user-mention" data-user-id="110031">@Patrick Massot</span> If you didn't have <code>assert</code>, <code>assertv</code>, <code>define</code>, <code>definev</code>, <code>note</code> or <code>pose</code>, how to you create a new goal and an associated assumption?</p>

#### [ Johan Commelin (Oct 03 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105355):
<p>What are <code>note</code> and <code>pose</code>?</p>

#### [ Patrick Massot (Oct 03 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105364):
<p>I don't even understand the question</p>

#### [ Johan Commelin (Oct 03 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105380):
<p>Actually, I don't recognise any of those tactics.</p>

#### [ Johan Commelin (Oct 03 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105394):
<p>I only use <code>have foo : blah,</code></p>

#### [ Johan Commelin (Oct 03 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105405):
<p>Or <code>suffices</code></p>

#### [ Patrick Massot (Oct 03 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105407):
<p>Johan, this is all meta</p>

#### [ Patrick Massot (Oct 03 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105428):
<p>we are discussing tactic writing here, not plebeian proof writing</p>

#### [ Simon Hudon (Oct 03 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105524):
<p>You got it. There's also a non-condescending way to put it :P</p>

#### [ Patrick Massot (Oct 03 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105640):
<p>Hopefully the fact <em>I</em> wrote this (instead of Scott, you or any other tactic writer) was a clear enough hint about how to read it <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Simon Hudon (Oct 03 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105736):
<p>I thought so too. I just had to react to the tone <span class="emoji emoji-1f606" title="laughing">:laughing:</span></p>

#### [ Mario Carneiro (Oct 03 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105831):
<p>By the way, those all used to be interactive tactics. I was the one who advocated for simplifying it all down to <code>have</code> and <code>let</code></p>

#### [ Mario Carneiro (Oct 03 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105852):
<p>and <code>suffices</code> because why not</p>

#### [ Simon Hudon (Oct 03 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135105990):
<p>That's a nice improvement</p>

#### [ Simon Hudon (Oct 03 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106008):
<p>It's especially nice that the same keywords work in tactic mode and in term mode</p>

#### [ Patrick Massot (Oct 03 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106062):
<p>it's also slightly confusing that the accepted syntaxes are not quite the same</p>

#### [ Patrick Massot (Oct 03 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106078):
<p>fortunately that issue is easily fixed by working only in tactic mode</p>

#### [ Patrick Massot (Oct 03 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106213):
<p>Returning to norm_num and tidy, I'm not able to make any progress on getting <code>example : (0 : ℝ) &lt; (1 : ℝ) := by tidy</code> to work. I tried adding norm_num to the tidy set, either with or without progress guard but no luck</p>

#### [ Simon Hudon (Oct 03 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106356):
<p>That's annoying</p>

#### [ Patrick Massot (Oct 03 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106366):
<p>That's probably only me</p>

#### [ Simon Hudon (Oct 03 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106393):
<p>That's what I meant, you keep complaining ... <span class="emoji emoji-1f61c" title="stuck out tongue wink">:stuck_out_tongue_wink:</span></p>

#### [ Patrick Massot (Oct 03 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106409):
<p>What's fun is that the guard_progress trick works with apply_eq which is not meant to modify the goal</p>

#### [ Patrick Massot (Oct 03 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106424):
<p>My tactic writing is pure Brownian motion</p>

#### [ Simon Hudon (Oct 03 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106468):
<p>Ah! It's time for the next lesson</p>

#### [ Johan Commelin (Oct 03 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106484):
<p>If we have Brownian motions in mathlib, would this help you with tactic writing <span class="emoji emoji-1f61c" title="stuck out tongue wink">:stuck_out_tongue_wink:</span> ?</p>

#### [ Simon Hudon (Oct 03 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106499):
<p>When you use <code>get_goals</code>, what exactly does it give you? First wrong assumption: it tells you the proposition that the goal aims to prove.</p>

#### [ Simon Hudon (Oct 03 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106574):
<blockquote>
<p>If we have Brownian motions in mathlib, would this help you with tactic writing <span class="emoji emoji-1f61c" title="stuck out tongue wink">:stuck_out_tongue_wink:</span> ?</p>
</blockquote>
<p>Sorry to disappoint: my research area is scheduling in distributed and cyber-physical systems (keyword: scheduling) and I'm still constantly procrastinating and arriving late</p>

#### [ Simon Hudon (Oct 03 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106597):
<p>You may know all the theory there is on a subject, that doesn't mean that you can do the thing yourself</p>

#### [ Simon Hudon (Oct 03 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106704):
<blockquote>
<p>When you use <code>get_goals</code>, what exactly does it give you? First wrong assumption: it tells you the proposition that the goal aims to prove.</p>
</blockquote>
<p>What it actually gives you is a list of unassigned meta variables. An unassigned meta variable has a type and a set of local constants that it can see. It doesn't have a value yet. Just like a proof goal: you know what you have to prove but you don't have a proof yet.</p>

#### [ Simon Hudon (Oct 03 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106832):
<p>If your goal is <code>⊢ succ x &lt; succ y</code>, you have a meta variable <code>?m_1 : succ x &lt; succ y</code>. If you want to apply <code>succ_lt_succ</code>, It</p>

#### [ Simon Hudon (Oct 03 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135106985):
<p>it's like creating a meta variable <code>?m_2 : x &lt; y</code> and then you construct an expression <code>succ_lt_succ ?m_2</code> which you assign to <code>?m_1</code>. Then, you remove <code>?m_1</code> from the list of goals and you put <code>?m_2</code> instead. The goal changes because you have a different meta variable in the list of goals now.</p>

#### [ Patrick Massot (Oct 03 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135107297):
<p>so the short version is: the goal comes with its local context, right?</p>

#### [ Simon Hudon (Oct 03 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135107588):
<p>That is correct</p>

#### [ Patrick Massot (Oct 03 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135107927):
<p>I should stop playing, and focus on the archaic manual referee process, but I have <a href="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/auto_demo.lean" target="_blank" title="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/auto_demo.lean">https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/auto_demo.lean</a></p>

#### [ Patrick Massot (Oct 03 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135108002):
<p>This is part of my demo file with tidy everywhere</p>

#### [ Patrick Massot (Oct 03 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135108465):
<p>Thanks for all your help!</p>

#### [ Edward Ayers (Oct 03 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135111366):
<blockquote>
<p>What about <code>nuke</code>?</p>
</blockquote>
<p>Can emoji be tactic names?</p>

#### [ Kevin Buzzard (Oct 03 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135113179):
<p>This has come up before</p>

#### [ Kevin Buzzard (Oct 03 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135113199):
<p>and I believe there was a trick using quotations somehow</p>

#### [ Patrick Massot (Oct 03 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%C3%BCber-tactic/near/135113247):
<p><a href="#narrow/stream/116395-maths/subject/algebra.20on.20subtypes/near/129927817" title="#narrow/stream/116395-maths/subject/algebra.20on.20subtypes/near/129927817">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/algebra.20on.20subtypes/near/129927817</a></p>


{% endraw %}
