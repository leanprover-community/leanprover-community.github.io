---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63223gitrebase.html
---

## Stream: [general](index.html)
### Topic: [git rebase](63223gitrebase.html)

---

#### [Scott Morrison (Sep 10 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20rebase/near/133660217):
@**Kevin Buzzard**, if you're interested in a quick tutorial on `git rebase`, let me know. I finally worked out how to do it (with some help from Johannes) at Orsay. You might in the end find it easier than what you just went through! [Screenshot-2018-09-10-23.30.11.png](/user_uploads/3121/N0ltaWQLM-4x4MmnvZVlAmvW/Screenshot-2018-09-10-23.30.11.png)

#### [Scott Morrison (Sep 10 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20rebase/near/133660847):
I can see from the history of the `zerology` branch that you've also merged in lots of "dead" branches, which had in fact already made it into mathlib. This isn't fatal, but it does make the history look a lot more complicated, and make it much harder to judge whether everything has been merged or discarded correctly.

#### [Kevin Buzzard (Sep 10 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20rebase/near/133681508):
I tried to read up about this business recently. My understanding was that git rebase rewrites history so should not be used on public repos. I understand that we don't want horrible history in mathlib, but if a PR is accepted by mathlib then they can fix things up (e.g. by squishing the entire commit history into one commit). Are you saying I should rebase anyway? Of course anything is fine by me, I'm happy to do what I'm told here.

#### [Johannes Hölzl (Sep 10 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20rebase/near/133681974):
rebaseing branches in your private repository is okay. But it's dangerous if you rebase in leanprover-community, as others might have commits based on this branch and get into trouble if the branch gets rewritten

#### [Kevin Buzzard (Sep 10 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20rebase/near/133682288):
Aah so maybe when I notice that leanprover/mathlib has some commits, and leanprover-community/mathlib has a different number, and my clone has some new branch which is not up to date with either of these, I do all the rebasing from upstream in the comfort of my own home, and then push acceptable lies to the community mathlib. Is that how it works? Sorry to ask such basic questions, we don't get taught git in math school.

#### [Scott Morrison (Sep 11 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20rebase/near/133709762):
I realise that maybe I've been overly aggressive: I was sort of assuming that it was okay to force push branches to leanprover-community that overwrite history.

#### [Johan Commelin (Sep 11 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20rebase/near/133711027):
@**Scott Morrison** Do you want Linus Torvalds shouting at you? :lol:

