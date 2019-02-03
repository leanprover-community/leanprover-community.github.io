---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/63394583moveeverythingintosrc.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#583 move everything into `src`](https://leanprover-community.github.io/archive/144837PRreviews/63394583moveeverythingintosrc.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jan 15 2019 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155153163):
<p>What is the status of this PR? I think we should bite the bullet and make it happen. I'm waiting for it before implementing the topology part of <a href="https://github.com/leanprover/mathlib/issues/586" target="_blank" title="https://github.com/leanprover/mathlib/issues/586">https://github.com/leanprover/mathlib/issues/586</a> I'm willing to update the PR, but then it needs to be merged right away, otherwise it will have conflict at every single future commit</p>

#### [ Patrick Massot (Jan 15 2019 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155153170):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span></p>

#### [ Reid Barton (Jan 15 2019 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155154177):
<p>I agree we should do this now, and then follow up with the reorganization at the level of whole files, which we now have an outline for and should be straightforward. I don't think we need to wait for the details of how to reorganize individual files like <code>topological_space.lean</code>.</p>

#### [ Kevin Buzzard (Jan 15 2019 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155154237):
<p>I vote for pain today as opposed to more pain tomorrow.</p>

#### [ Reid Barton (Jan 15 2019 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155165674):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Jan 15 2019 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155165734):
<p>ok, it has to be redone though of course</p>

#### [ Patrick Massot (Jan 15 2019 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155172935):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what do you mean here? Do you mean: if someone redoes it then I'll merge right away?</p>

#### [ Mario Carneiro (Jan 15 2019 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155172952):
<p>yes</p>

#### [ Mario Carneiro (Jan 15 2019 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155173107):
<p>are we ready for the reorganization though? I guess both should be done around the same time</p>

#### [ Patrick Massot (Jan 15 2019 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155173342):
<p>Ok, it's rebased</p>

#### [ Patrick Massot (Jan 15 2019 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155173376):
<p>I'm ready to move analysis files around. I don't know about the stuff in <code>basic</code></p>

#### [ Mario Carneiro (Jan 15 2019 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155173697):
<p>ok, so the first reorg PR can be moving files around with no splitting, and we can split files in later PRs</p>

#### [ Patrick Massot (Jan 15 2019 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155173773):
<p>Yes, that's the plan</p>

#### [ Mario Carneiro (Jan 15 2019 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155180006):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> I merged, but it looks a bit incomplete. Could you follow up moving the rest of the files?</p>

#### [ Patrick Massot (Jan 15 2019 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155180043):
<p>So weird... I guess I trusted Simon too much</p>

#### [ Mario Carneiro (Jan 15 2019 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155180095):
<p>you should redone it instead of rebase, I think</p>

#### [ Mario Carneiro (Jan 15 2019 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155180119):
<p>the files that were left behind are new since simon's version</p>

#### [ Patrick Massot (Jan 15 2019 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155180172):
<p>Ok, it's probably my fault then</p>

#### [ Patrick Massot (Jan 15 2019 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155180604):
<p><a href="https://github.com/leanprover/mathlib/pull/597" target="_blank" title="https://github.com/leanprover/mathlib/pull/597">https://github.com/leanprover/mathlib/pull/597</a></p>

#### [ Patrick Massot (Jan 15 2019 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155180612):
<p>sorry about the inconvenience</p>

#### [ Johan Commelin (Jan 16 2019 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155273357):
<p>I'm a git noob. I just did <code>git pull upstream master</code> to get the latest version from <a href="https://github.com/leanprover/mathlib" target="_blank" title="https://github.com/leanprover/mathlib">https://github.com/leanprover/mathlib</a><br>
So now I have a directory <code>src/</code> with all of mathlib in it. But all the old directories are also still there. So everything is duplicated. Is it easy to fix this? (Otherwise I'll just reclone.)</p>

#### [ Johannes Hölzl (Jan 16 2019 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155273485):
<p>the old directories are not deleted, usually there are still the <code>olean</code> files in them. One option is to clean your repository using <code>git clean -xfd</code>, but be careful to not have any uncommited stuff in your repo</p>

#### [ Johan Commelin (Jan 16 2019 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155273603):
<p>Ok, now the old directories are empty, but they are still there...</p>

#### [ Johannes Hölzl (Jan 16 2019 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155274121):
<p>hm the <code>-d</code> should have removed them</p>

#### [ Johan Commelin (Jan 16 2019 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23583%20move%20everything%20into%20%60src%60/near/155275903):
<p>Aah, <code>git clean -fd</code> worked</p>


{% endraw %}
