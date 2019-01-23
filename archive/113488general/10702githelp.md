---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10702githelp.html
---

## Stream: [general](index.html)
### Topic: [git help](10702githelp.html)

---


{% raw %}
#### [ Scott Morrison (Apr 11 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926688):
Sorry to have to ask about mundane things like how to use git, but... Say that I've got a fork of mathlib that is borked in some way (in my case, I merged in a commit from master, that Mario shortly thereafter deleted, but I have a branch that includes it).

Should I:
1) Just delete my whole fork (this is a good moment to do so, I have only two modified files).
2) Learn about ... rebasing? something else? Is it possible to actually get my master branch back to matching the main repository's master branch?

#### [ Sebastian Ullrich (Apr 11 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926741):
> Is it possible to actually get my master branch back to matching the main repository's master branch?

`git reset --hard origin/master`

#### [ Scott Morrison (Apr 11 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926745):
But what about all the pushed commits to master on my github fork?

#### [ Scott Morrison (Apr 11 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926784):
That won't bring my fork hosted on github back to matching the corresponding branch on the main github repo, will it?

#### [ Sebastian Ullrich (Apr 11 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926797):
Ah. It will after a `git push --force <your remote>`.

#### [ Scott Morrison (Apr 11 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926866):
But ... don't I have to strip commits or something?

#### [ Scott Morrison (Apr 11 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926869):
I want my master branch in my fork to really look (history and everything) just like the master branch in origin.

#### [ Scott Morrison (Apr 11 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926911):
Or is it okay to just continue on with my fork having its own alternative borked history?

#### [ Sebastian Ullrich (Apr 11 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926913):
After these two commands, your fork's master will look exactly like the one in origin

#### [ Scott Morrison (Apr 11 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124926967):
Ah, and the `--hard` you added above means I don't even need to `git checkout -- .`. Thanks.

#### [ Scott Morrison (Apr 11 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124927019):
Wow, amazing! Everything is beautiful. :-)

#### [ Sebastian Ullrich (Apr 11 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/git%20help/near/124927025):
:)


{% endraw %}
