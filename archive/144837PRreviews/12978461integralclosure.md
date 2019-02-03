---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/12978461integralclosure.html
---

## Stream: [PR reviews](index.html)
### Topic: [#461 integral closure](12978461integralclosure.html)

---


{% raw %}
#### [ Kenny Lau (Nov 10 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/147449667):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I've finished adding content to my PR, you can review it now</p>

#### [ Kevin Buzzard (Dec 07 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/151108155):
<p>I will be finished with teaching in 1 week and will be very keen to move back to do some algebra in Lean. What is the status of this PR? Can Kenny or I do anything to help? There seem to have been no activity for almost a month. Would the devs rather it were broken into smaller pieces?</p>

#### [ Johan Commelin (Dec 17 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024252):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I see you changed the title of the PR to indicate that it is WIP. What is WIP about it?</p>

#### [ Kenny Lau (Dec 17 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024273):
<p>I intend to use <code>algebra</code> which I'm developing</p>

#### [ Johan Commelin (Dec 17 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024278):
<p>Does it make sense to split the PR into smaller pieces, that are mergeabler than a big one?</p>

#### [ Johan Commelin (Dec 17 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024327):
<p>Aha, I see. But that won't touch everything, right?</p>

#### [ Johan Commelin (Dec 17 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024334):
<p>Will Hilbert basis be affected?</p>

#### [ Kenny Lau (Dec 17 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024346):
<p>I think not</p>

#### [ Johan Commelin (Dec 17 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024355):
<p>Ok, so should we factor that out?</p>

#### [ Kenny Lau (Dec 17 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024376):
<p>perhaps</p>

#### [ Johan Commelin (Dec 17 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024514):
<p>I think we're repeatedly seeing that smaller PRs get merged faster than big PRs. So I vote for chopping PRs into the smallest pieces that are still "sensible".</p>

#### [ Kenny Lau (Dec 17 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024599):
<p>hence my earlier question (for <code>faster</code>) about 1 big PR vs 25 small PR's</p>

#### [ Johan Commelin (Dec 17 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152025155):
<p>Right. So would you want to split this PR into two pieces? On for Hilbert basis, and one for int.clos.?</p>

#### [ Patrick Massot (Dec 17 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152025266):
<p>It looks like we have some PR crisis again. PR piled up in topology, category theory and algebra. We should probably all stop what we are doing, and start reviewing PRs to help Mario and Johannes (I know at least Reid seems to be already doing this, and of course I don't want to stop what <em>I</em> am doing...).</p>

#### [ Johan Commelin (Dec 17 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152025539):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Like so: <a href="https://github.com/leanprover/mathlib/issues/520" target="_blank" title="https://github.com/leanprover/mathlib/issues/520">#520</a> ??</p>

#### [ Patrick Massot (Dec 17 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152025644):
<p>?</p>

#### [ Johan Commelin (Dec 17 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152025673):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> I just helped increase the PR crisis by adding a trivial PR to the queue...</p>

#### [ Johan Commelin (Jan 30 2019 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/157171627):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Can you tell us what is left of this PR? I guess all the stuff on integral closure?</p>

#### [ Kenny Lau (Jan 30 2019 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/157171631):
<p>indeed</p>


{% endraw %}
