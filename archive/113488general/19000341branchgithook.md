---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19000341branchgithook.html
---

## Stream: [general](index.html)
### Topic: [3.4.1 branch git hook](19000341branchgithook.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 01 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4.1%20branch%20git%20hook/near/150678029):
Mathlib has this annoying `3.4.1` branch which occasionally users get burned by -- `leanpkg upgrade` can sometimes dump you on this branch, which is usually behind. I forget when it happens -- maybe something to do with the version of lean being used or the version of lean being recommended by the package. The github 3.4.1 branch should track master really (at least that would solve the problem of users occasionally being stranded without the latest mathlib despite having just attempted to upgrade their lean package). Mario suggested solving this with a git hook. I've just been reading about them. Is the correct solution that someone writes a client-side hook that which makes is so that every time someone pushes to master, the 3.4.1 branch also gets updated to master? Mario and Johannes then let this client side hook run on all of the machines they use to push to github mathlib. Is that how it is supposed to work?  I would imagine that this is a triviality to write in bash but presumably on Windows one might have to ensure that it works with all versions of all shells that the devs are running. I don't understand server side hooks well enough to know whether a server side hook is a better solution.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Dec 01 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4.1%20branch%20git%20hook/near/150687330):
I'm not addressing your question Kevin but just by-the-way: my `branch = "xxx"` patch was merged into lean and has been released in the nightlies. So as long as you are running the latest version of lean (if you have elan setting `lean_version=...` will do) you can just put in `branch = "master"` (along with the existing `url` and `rev`) and you'll be safe forever, and `leanpkg upgrade` will push you forward on that branch instead. (or any other branch you so desire and specify in this way)

