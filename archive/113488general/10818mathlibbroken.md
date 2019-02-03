---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10818mathlibbroken.html
---

## Stream: [general](index.html)
### Topic: [mathlib broken?](10818mathlibbroken.html)

---


{% raw %}
#### [ Scott Morrison (Apr 04 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124599682):
<p>Actually, it seems like the problem is just in mathlib.</p>

#### [ Scott Morrison (Apr 04 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124599728):
<p>Does anyone else get</p>
<div class="codehilite"><pre><span></span>/Users/scott/projects/lean/lean-category-theory/_target/deps/mathlib/data/nat/sqrt.lean:103:48: error: solve1 tactic failed, focused goal has not been solved

state:

n : ℕ,
sqrt_aux_is_sqrt :
 ∀ (m r : ℕ),
 r * r ≤ n →
 n &lt; (r + 2 ^ (m + 1)) * (r + 2 ^ (m + 1)) → is_sqrt n (sqrt_aux (2 ^ m * 2 ^ m) (2 * r * 2 ^ m) (n - r * r)),
m r : ℕ,
h₁ : r * r ≤ n,
h₂ : n &lt; (r + 2 ^ (m + 1 + 1)) * (r + 2 ^ (m + 1 + 1)),
a : n &lt; (r + 2 ^ (m + 1)) * (r + 2 ^ (m + 1)),
this : is_sqrt n (sqrt_aux (2 ^ m * 2 ^ m) (r * 2 * 2 ^ m) (n - r * r))
⊢ is_sqrt n (sqrt_aux (2 ^ m * 2 ^ m) (r * (2 * 2 ^ m)) (n - r * r))
 ````
</pre></div>

#### [ Scott Morrison (Apr 04 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124599971):
<p>The <code>finish</code> <a href="https://github.com/leanprover/mathlib/blob/master/order/complete_boolean_algebra.lean#L42" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/order/complete_boolean_algebra.lean#L42">here</a> in mathlib/order/complete_boolean_algebra seems to take a long time to execute.</p>

#### [ Mario Carneiro (Apr 04 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601878):
<p>mathlib is currently broken. I am working on a fix</p>

#### [ Kenny Lau (Apr 04 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601879):
<p>actually what is the cause of the problem?</p>

#### [ Kenny Lau (Apr 04 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601880):
<p>I roughly saw something to do with <code>punit.eq</code></p>

#### [ Kenny Lau (Apr 04 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601881):
<p>I checked the init and it is indeed there</p>

#### [ Mario Carneiro (Apr 04 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601909):
<p>The biggest change was the <code>has_pow</code> typeclass, which changes the way power functions are used across the library</p>

#### [ Kenny Lau (Apr 04 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601924):
<p>then why do I see <code>punit.eq</code>?</p>

#### [ Mario Carneiro (Apr 04 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601925):
<p><code>group_power</code> needed to be heavily edited, and that caused downstream changes</p>

#### [ Kenny Lau (Apr 04 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601936):
<p>alright, good luck</p>

#### [ Mario Carneiro (Apr 04 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601982):
<p>(plus I have some HW due tomorrow which is interfering with my maintenance work)</p>

#### [ Kenny Lau (Apr 04 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124601983):
<p>I see</p>

#### [ Scott Morrison (Apr 04 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124602377):
<p>Let us know if there is work that can be delegated. (Right now delegating might be more work than just fixing, but in the long run it may be worth thinking about sustainable models of mathlib maintenance.)</p>

#### [ Mario Carneiro (Apr 04 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124602936):
<p>For the moment I think I would rather do this work myself, and would indeed discourage others from trying to fix it on their own, because this creates merge headaches, especially in this sort of cross-library modification.</p>

#### [ Mario Carneiro (Apr 04 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124602984):
<p>I've got it 99% working, there's just one error in ordinal_notation that I need to check the original proof to fix. I could push it now, but it won't compile in travis</p>

#### [ Scott Morrison (Apr 04 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124608602):
<p>A  99% fix would still be helpful, as at the moment huge chunks of mathlib recompile every time I run leanpkg. This makes it almost impossible to work.</p>

#### [ Mario Carneiro (Apr 04 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124609640):
<p>I'll push a 99% fix if I can't get it working tonight.</p>

#### [ Scott Morrison (Apr 04 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124609646):
<p>no problem --- I'm managing as is, actually.</p>

#### [ Kevin Buzzard (Apr 04 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616232):
<blockquote>
<p>For the moment I think I would rather do this work myself, and would indeed discourage others from trying to fix it on their own, because this creates merge headaches, especially in this sort of cross-library modification.</p>
</blockquote>
<p>The folly of youth :-)</p>

#### [ Kevin Buzzard (Apr 04 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616233):
<p>"I am young and enthusiastic and I know I can fix it myself, so let me fix it myself"</p>

#### [ Kevin Buzzard (Apr 04 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616270):
<p>I am just the opposite nowadays</p>

#### [ Kenny Lau (Apr 04 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616280):
<p>a loucura da juventude</p>

#### [ Kevin Buzzard (Apr 04 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616282):
<p>"I am old and busy, and I know I can do it, so sure go ahead and do it, and then I can remove it from my job list and furthermore I can blame you later ;-)"</p>

#### [ Mario Carneiro (Apr 04 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616285):
<p>I see your point, but given that I've already done most of it, someone else jumping in at this point will only make things worse</p>

#### [ Mario Carneiro (Apr 04 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616292):
<p>If I hadn't started the work I'd agree with you</p>

#### [ Kevin Buzzard (Apr 04 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616294):
<p>I am sure you're right on this occasion.</p>

#### [ Kevin Buzzard (Apr 04 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616300):
<p>If you're in the middle then it's surely easiest just to keep going.</p>

#### [ Kevin Buzzard (Apr 04 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616305):
<p>I know now that the wise move is just to sit and wait and not upgrade Lean</p>

#### [ Kevin Buzzard (Apr 04 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616306):
<p>see my comment in travis</p>

#### [ Mario Carneiro (Apr 04 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616356):
<p>Indeed. My fix includes updating the leanpkg.toml file to explicitly reference the nightly it should work with, so hopefully going forward we shouldn't have the problem that updating breaks mathlib</p>

#### [ Kevin Buzzard (Apr 04 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616437):
<p>I think that all this leanpkg.toml tinkering is a really good idea</p>

#### [ Kevin Buzzard (Apr 04 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616477):
<p>because in the medium term future things will get more chaotic (when lean 4 appears)</p>

#### [ Kevin Buzzard (Apr 04 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616484):
<p>and if we have some pretty robust stuff available for making lean and mathlib not break for people wanting to stay on the bleeding edge</p>

#### [ Kevin Buzzard (Apr 04 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124616486):
<p>this will be brilliant</p>

#### [ Mario Carneiro (Apr 04 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124617600):
<p>okay, I missed my self imposed deadline, have my 99% fix</p>

#### [ Kenny Lau (Apr 04 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124617601):
<p>e o teu HW?</p>

#### [ Mario Carneiro (Apr 04 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124617650):
<p>nao terminei</p>

#### [ Kenny Lau (Apr 04 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124617665):
<p>oh hey finalmente me falas em portugues</p>

#### [ Mario Carneiro (Apr 04 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124617667):
<p>lol</p>

#### [ Kenny Lau (Apr 04 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124617669):
<p>mdr</p>

#### [ Mario Carneiro (Apr 04 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124619310):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> Could you troubleshoot the mathlib leanpkg.toml setup? Adding the lean_version just makes travis complain about it, and doesn't change the result.</p>

#### [ Sebastian Ullrich (Apr 04 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124619473):
<p>I'll try to build an MVP of leanup today that is sufficient for using it with Travis</p>

#### [ Mario Carneiro (Apr 05 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124656640):
<p>I think I've figured out the problem: Travis is using <a href="https://github.com/leanprover/lean-nightly/blob/gh-pages/build/lean-nightly-linux.tar.gz" target="_blank" title="https://github.com/leanprover/lean-nightly/blob/gh-pages/build/lean-nightly-linux.tar.gz">https://github.com/leanprover/lean-nightly/blob/gh-pages/build/lean-nightly-linux.tar.gz</a>, which hasn't been updated in 15 days, presumably since the nightly publication process changed. Now I guess I have to go to <a href="https://github.com/leanprover/lean-nightly/releases" target="_blank" title="https://github.com/leanprover/lean-nightly/releases">https://github.com/leanprover/lean-nightly/releases</a> and download the appropriate nightly, but that either requires parsing the TOML file or inserting the date in two more places in the travis.yml file. I assume this is what <code>leanup</code> is going to do?</p>

#### [ Gabriel Ebner (Apr 05 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124660148):
<p>Yes, see previous discussion here: <a href="#narrow/stream/113488-general/subject/lean.20travis.20problems/near/124359348" title="#narrow/stream/113488-general/subject/lean.20travis.20problems/near/124359348">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/lean.20travis.20problems/near/124359348</a></p>

#### [ Sebastian Ullrich (Apr 05 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20broken%3F/near/124660826):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Thanks for the quickfix :) . I'll have to supervise an exam today first, but after that I'll continue working on a proper leanup.</p>


{% endraw %}
