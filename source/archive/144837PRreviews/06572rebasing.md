---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/06572rebasing.html
---

## [PR reviews](index.html)
### [rebasing](06572rebasing.html)

#### [Scott Morrison (Nov 13 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147631335):
Hi @**Reid Barton**, @**Johan Commelin**. I'm about to rebase `limits-others-new`. This is going to leave `adjunctions` and `sheaf` in a strange position.

#### [Scott Morrison (Nov 13 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147631352):
Would it be okay if I rebased either of both of those onto the new `limits` branch?

#### [Scott Morrison (Nov 14 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147632148):
It would mean doing a force push to `community/adjunctions` and/or to `community/sheaf`, so I'd need to get the okay that you're not actively working on that branch.

#### [Reid Barton (Nov 14 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147634851):
Yes, feel free, or I am also happy to take care of the rebase myself.

#### [Scott Morrison (Nov 14 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147635786):
Maybe it's best if you do it, so I don't mess up authorship information.

#### [Scott Morrison (Nov 14 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147635875):
oh, worked it out :-)

#### [Johan Commelin (Nov 14 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147649877):
@**Scott Morrison|110087** Please go ahead with rebasing `sheaf`. I have no idea how to do that...

#### [Scott Morrison (Nov 14 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147651466):
Done! Your old history is now on the `sheaf-old` branch, but if everything looks okay we can delete that.

#### [Johan Commelin (Nov 14 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147651669):
Thanks, I'll take a look!

#### [Johan Commelin (Nov 14 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147651728):
@**Scott Morrison|110087** Hmm, that's easier said than done.

#### [Johan Commelin (Nov 14 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147651730):
How do I take a look?

#### [Johan Commelin (Nov 14 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147651733):
`git pull origin sheaf` gives me an aweful lot of merge conflicts in files that are not `sheaf.lean`

#### [Keeley Hoek (Nov 14 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147652154):
Hi Johan, Try
````
git merge --abort
git checkout sheaf
git branch -m sheaf-old
git branch sheaf-old -u origin/sheaf-old
git fetch
git checkout -b sheaf origin/sheaf
````

#### [Keeley Hoek (Nov 14 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147652156):
@**Johan Commelin**

#### [Keeley Hoek (Nov 14 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147652200):
The new sheafs will be `sheaf`, the old sheafs will be `sheaf-old`

#### [Johan Commelin (Nov 14 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147652317):
Thanks @**Keeley Hoek**, that seems to have worked git-wise. Now checking if Lean is happy by recompiling.

#### [Johan Commelin (Nov 14 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147653409):
Oh boy, lots of red squiggles....

#### [Kevin Buzzard (Nov 14 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147653417):
how christmassy

#### [Scott Morrison (Nov 14 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147653467):
Thanks Keeley for the instructions!

#### [Scott Morrison (Nov 14 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147653470):
Are things working, Johan?

#### [Johan Commelin (Nov 14 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147653475):
Nope, not really...

#### [Johan Commelin (Nov 14 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147653484):
I feel like I should start taking a more structured approach. Because this file has been growing like a kludge of hacks.

#### [Scott Morrison (Nov 14 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147653492):
Sorry, let me try compiling here. :-)

#### [Scott Morrison (Nov 14 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147655679):
@**Johan Commelin**, all but one error fixed, which is just an unfinished proof at the bottom.

#### [Scott Morrison (Nov 14 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147655692):
There was a universe issue, a missing simp lemma, and the syntax of yoneda had changed.

#### [Johan Commelin (Nov 14 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/rebasing/near/147661373):
@**Scott Morrison|110087** Thanks a lot! (Sorry, I had seminars and then lunch...)

