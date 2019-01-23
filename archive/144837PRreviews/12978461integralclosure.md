---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/12978461integralclosure.html
---

## Stream: [PR reviews](index.html)
### Topic: [#461 integral closure](12978461integralclosure.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 10 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/147449667):
@**Johannes Hölzl** I've finished adding content to my PR, you can review it now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 07 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/151108155):
I will be finished with teaching in 1 week and will be very keen to move back to do some algebra in Lean. What is the status of this PR? Can Kenny or I do anything to help? There seem to have been no activity for almost a month. Would the devs rather it were broken into smaller pieces?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024252):
@**Kenny Lau** I see you changed the title of the PR to indicate that it is WIP. What is WIP about it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024273):
I intend to use `algebra` which I'm developing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024278):
Does it make sense to split the PR into smaller pieces, that are mergeabler than a big one?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024327):
Aha, I see. But that won't touch everything, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024334):
Will Hilbert basis be affected?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024346):
I think not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024355):
Ok, so should we factor that out?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024376):
perhaps

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024514):
I think we're repeatedly seeing that smaller PRs get merged faster than big PRs. So I vote for chopping PRs into the smallest pieces that are still "sensible".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152024599):
hence my earlier question (for `faster`) about 1 big PR vs 25 small PR's

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152025155):
Right. So would you want to split this PR into two pieces? On for Hilbert basis, and one for int.clos.?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152025266):
It looks like we have some PR crisis again. PR piled up in topology, category theory and algebra. We should probably all stop what we are doing, and start reviewing PRs to help Mario and Johannes (I know at least Reid seems to be already doing this, and of course I don't want to stop what *I* am doing...).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152025539):
@**Patrick Massot** Like so: #520 ??

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152025644):
?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23461%20integral%20closure/near/152025673):
@**Patrick Massot** I just helped increase the PR crisis by adding a trivial PR to the queue...

