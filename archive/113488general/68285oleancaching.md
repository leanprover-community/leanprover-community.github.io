---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68285oleancaching.html
---

## Stream: [general](index.html)
### Topic: [olean caching](68285oleancaching.html)

---

#### [Simon Hudon (Oct 07 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366355):
I just created a PR to get `git` to preserve your `olean` files and restore them when you switch branches. I'd like to know if it works for people. Please let me know if you try it and if it helps.

#### [Kenny Lau (Oct 07 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366398):
:D

#### [Simon Hudon (Oct 07 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366500):
In particular, I'd like to know if it needs to be adapter for windows because I use shell scripts

#### [Patrick Massot (Oct 07 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366580):
If you manage to allow us to switch mathlib branches back and forth without recompiling I phone the inquisition.

#### [Simon Hudon (Oct 07 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366585):
Let me just delete a branch, one sec

#### [Patrick Massot (Oct 07 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366589):
That would be one sorcery prowess too many for your own good.

#### [Simon Hudon (Oct 07 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366693):
Can the quota be negotiated?

#### [Simon Hudon (Oct 07 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366699):
If you want to try it before the branch is merged, here are the files

[cache_olean.zip](/user_uploads/3121/KxJGKo8Df8IDgnEp7wUA57ar/cache_olean.zip)

#### [Simon Hudon (Oct 07 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366707):
You unzip them in your mathlib directory and call `./install_hooks.sh`

#### [Patrick Massot (Oct 07 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366752):
I'll negociate for you if you manage to convince Travis to put mathlib olean for linux somewhere git will find them each we git pull mathlib

#### [Simon Hudon (Oct 07 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366768):
What it does is:
  * when you commit, it makes a copy of your olean files
  * when you checkout a branch, it checks if a cache exists for that branch and restores it if one exists
  * when you rebase a branch A on top of branch B, it caches the files of A and restores the files of B

#### [Kenny Lau (Oct 07 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366769):
just the olean files?

#### [Simon Hudon (Oct 07 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366770):
Yes, just the olean files

#### [Simon Hudon (Oct 07 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366815):
```quote
I'll negociate for you if you manage to convince Travis to put mathlib olean for linux somewhere git will find them each we git pull mathlib
```
That's a tall order. You're asking for a complete new feature, all I did was a small hack :P

#### [Simon Hudon (Oct 07 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366831):
Actually ... that's feasible

#### [Simon Hudon (Oct 07 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366894):
Actually, I think doing it half-way is more than half-way useful

#### [Simon Hudon (Oct 07 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366921):
Do you guys feel like giving it a spin?

#### [Patrick Massot (Oct 07 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366972):
I'll definitely try tomorrow, but I really need to go to bed now

#### [Simon Hudon (Oct 07 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135366985):
I thought you enjoyed working with Lean

#### [Simon Hudon (Oct 07 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135367104):
Sleep well :)

#### [Bryan Gin-ge Chen (Oct 08 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135368285):
@**Simon Hudon** Does this work the same way for packages that include `mathlib` as a dependency?

#### [Bryan Gin-ge Chen (Oct 08 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135368290):
Wait, maybe that question doesn't make sense.

#### [Simon Hudon (Oct 08 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135368396):
You can make it work in that situation I believe. Once you configured the package, go in `_target/deps/mathlib` and call `./install_hooks.sh`. If different versions of the same package use different branches of mathlib, switching between the versions of your package might get cheaper (we'd have to test it to make sure)

#### [Bryan Gin-ge Chen (Oct 08 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135368397):
```
hint: The '.git/hooks/post-checkout' hook was ignored because it's not set as executable.
hint: You can disable this warning with `git config advice.ignoredHook false`.
```
Should I change the permissions on these files?

#### [Simon Hudon (Oct 08 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135368405):
Yes good idea. And I'll make fixes to the scripts

#### [Simon Hudon (Oct 08 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369137):
Any luck?

#### [Bryan Gin-ge Chen (Oct 08 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369336):
I've been switching back and forth between `master` and `tutorials` and running `lean --make` and each time it does a full rebuild. If I do `lean --make` does that force a rebuild no matter what?

#### [Bryan Gin-ge Chen (Oct 08 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369338):
I'm on my macbook.

#### [Scott Morrison (Oct 08 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369347):
No, it doesn't/

#### [Bryan Gin-ge Chen (Oct 08 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369392):
Hmm, my master was out of date. Let me try again.

#### [Scott Morrison (Oct 08 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369401):
The problem is likely that master has introduced changes to stuff way down the dependency tree.

#### [Scott Morrison (Oct 08 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369406):
If you rebase tutorial onto master it should make life better.

#### [Bryan Gin-ge Chen (Oct 08 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369458):
I think I see what you're saying, but shouldn't caching all the olean files associated to a given commit also preserve the build status?

#### [Simon Hudon (Oct 08 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369461):
It should. Can you `ls .bin/branches` and tell me what you get?

#### [Bryan Gin-ge Chen (Oct 08 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369505):
Where's `.bin`?

#### [Bryan Gin-ge Chen (Oct 08 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135369569):
Oh I see, I guess `.bin` somehow hasn't been created.

#### [Simon Hudon (Oct 08 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135370095):
It is created when you commit or rebase. You can also manually call `.git/hooks/cache_olean.sh`

#### [Bryan Gin-ge Chen (Oct 08 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371074):
I ran `cache_olean.sh` after building on tutorials and master, and the olean files seem to be in .bin/branches/ but running lean --make still starts a rebuild.

#### [Simon Hudon (Oct 08 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371280):
What if you run `restore_olean.sh` before rebuilding?

#### [Scott Morrison (Oct 08 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371281):
> ./install_hooks.sh 
> cp: .git/hooks: Not a directory

#### [Scott Morrison (Oct 08 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371293):
Just needs a `mkdir -p .git/hooks` in `install_hooks.sh`.

#### [Bryan Gin-ge Chen (Oct 08 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371296):
I tried running `restore_olean.sh` and it's rebuilding again.

#### [Scott Morrison (Oct 08 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371359):
I pushed a commit that fixes this.

#### [Simon Hudon (Oct 08 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371360):
@**Bryan Gin-ge Chen** Can you check what the time stamp is on the most recently modified file in `.bin/branches/tutorial`? I'm assuming that's the one you're trying to cache.

#### [Simon Hudon (Oct 08 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371362):
@**Scott Morrison|110087** You're too fast! Thanks!

#### [Scott Morrison (Oct 08 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371403):
Ah, but I fixed the wrong problem.

#### [Scott Morrison (Oct 08 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371406):
The actual problem is that I don't have a .git directory.

#### [Scott Morrison (Oct 08 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371409):
I have a .git file, because I'm using a submodule.

#### [Scott Morrison (Oct 08 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371412):
Crap...

#### [Scott Morrison (Oct 08 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371419):
This is not going to affect many people at all, but I guess I want a fix myself. :-)

#### [Simon Hudon (Oct 08 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371422):
Darn! How come you work without git?

#### [Scott Morrison (Oct 08 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371433):
The problem is that I work with git for _everything_. My entire home directory is a giant git repository, and everything else is a git submodule, so things get synchronised between my computers.

#### [Simon Hudon (Oct 08 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371473):
Actually, if you go in `_target/deps/mathlib` and call `install_hooks.sh` there, I'm hoping that will do the job

#### [Scott Morrison (Oct 08 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371478):
Well, but I mostly want this for mathlib itself.

#### [Scott Morrison (Oct 08 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371479):
Switching between branches that touch tactic/basic.lean is unpleasant...

#### [Bryan Gin-ge Chen (Oct 08 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371534):
The timestamps all seem to be from when I ran `cache_olean.sh`.

#### [Scott Morrison (Oct 08 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371560):
@**Simon Hudon**, why do you put `cache_olean.sh` and `restore_olean.sh` in the `.git/hooks` directory, rather than leaving them in the root directory?

#### [Simon Hudon (Oct 08 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371597):
@**Bryan Gin-ge Chen** That is useful information. I'll look into preserving time stamps properly

#### [Simon Hudon (Oct 08 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371606):
@**Scott Morrison|110087** I want to be able to use the hooks even on branches where the files aren't in the repo

#### [Scott Morrison (Oct 08 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371621):
Ah, good point.

#### [Bryan Gin-ge Chen (Oct 08 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371622):
The timestamps of the `.lean` files are bumped when I checkout a new branch. So do we need the timestamps of the olean files to be more recent than that?

#### [Simon Hudon (Oct 08 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371782):
@**Bryan Gin-ge Chen** do you mean that the .lean timestamps are set to the time at which you checkout the files?

#### [Bryan Gin-ge Chen (Oct 08 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371788):
Yes.

#### [Simon Hudon (Oct 08 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371797):
@**Scott Morrison|110087** Maybe there's a way to include a search step at the beginning of the script to climb up the directory structure until a `.git` is found.

#### [Simon Hudon (Oct 08 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371843):
@**Bryan Gin-ge Chen** What platform are you on?

#### [Scott Morrison (Oct 08 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371844):
There's a nice fix, almost pushed.

#### [Scott Morrison (Oct 08 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371847):
`git rev-parse --git-dir` tells you where your `.git` directory really is.

#### [Scott Morrison (Oct 08 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371856):
e.g. for me: `/Users/scott/.git/modules/projects/lean/mathlib`

#### [Scott Morrison (Oct 08 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371910):
Okay, pushed that change.

#### [Scott Morrison (Oct 08 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371918):
I think we need more hooks. I want my olean files cached even if we don't  make a commit!

#### [Simon Hudon (Oct 08 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371919):
Thanks! Did you put that `.git` dir in a variable?

#### [Scott Morrison (Oct 08 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371922):
e.g. I never commit to master, but I want a cache.

#### [Simon Hudon (Oct 08 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371923):
Yeah, me too! I haven't found a good hook for that

#### [Scott Morrison (Oct 08 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371959):
I just have ``GITDIR=`git rev-parse --git-dir`` in most of the scripts.

#### [Scott Morrison (Oct 08 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371971):
What if when we checkout, we _first_ restore, _then_ cache.

#### [Simon Hudon (Oct 08 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371973):
I think we might need to get `leanpkg` or, emacs / VS code to do that after you build

#### [Bryan Gin-ge Chen (Oct 08 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371974):
macOS. Not all of the .lean files have their timestamps bumped, but the ones that don't exist in `master` certainly do.

#### [Scott Morrison (Oct 08 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371977):
If there was something to restore, then it just harmlessly puts it back again.

#### [Scott Morrison (Oct 08 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371978):
But if there was nothing to restore, then we build a cache?

#### [Scott Morrison (Oct 08 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371979):
hmm...

#### [Scott Morrison (Oct 08 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371980):
no

#### [Scott Morrison (Oct 08 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135371996):
because that cache will be wrong. :-)

#### [Bryan Gin-ge Chen (Oct 08 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372054):
All the files that are changed between branches have their timestamps set to the time I do the checkout.

#### [Scott Morrison (Oct 08 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372179):
What if on every checkout we:
1) run cache before checkout (saving the state of the branch we're leaving)

#### [Scott Morrison (Oct 08 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372180):
2) run restore after checkout

#### [Scott Morrison (Oct 08 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372181):
3) run cache after that

#### [Simon Hudon (Oct 08 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372182):
What a bummer. I found this information here. https://confluence.atlassian.com/bbkb/preserving-file-timestamps-with-git-and-mercurial-781386524.html

It recommends a certain build system as a solution

#### [Simon Hudon (Oct 08 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372223):
@**Scott Morrison|110087** run cache after the restore or after build?

#### [Scott Morrison (Oct 08 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372227):
I was thinking just immediately after the restore.

#### [Scott Morrison (Oct 08 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372229):
This has the effect of actually creating the cache merely by checking out.

#### [Scott Morrison (Oct 08 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372240):
Otherwise I don't see how a cache for master will ever be created

#### [Bryan Gin-ge Chen (Oct 08 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372244):
Could we just `touch` all the `.olean` files right before restoring?

#### [Scott Morrison (Oct 08 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372295):
I think the problem is that risk making things worse.

#### [Simon Hudon (Oct 08 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372296):
Yeah

#### [Scott Morrison (Oct 08 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372301):
(deleted)

#### [Scott Morrison (Oct 08 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372304):
(deleted)

#### [Simon Hudon (Oct 08 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372307):
What I'm thinking of is, after a checkout, look at each lean file and set its time stamp to that of the latest commit that changed it

#### [Scott Morrison (Oct 08 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372309):
oof...

#### [Scott Morrison (Oct 08 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372341):
(Presumably you mean to the time stamp of the corresponding olean file.)

#### [Reid Barton (Oct 08 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372349):
What if you just don't use `cp -a`?

#### [Simon Hudon (Oct 08 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372408):
The olean files will all be interpreted as up-to-date but some might not be

#### [Simon Hudon (Oct 08 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372469):
```quote
(Presumably you mean to the time stamp of the corresponding olean file.)
```
No. For any source file we need to determine if we need to rebuild it. One information we need is when we last built it which is why we shouldn't overwrite the time stamp of the olean file. The other one is when we last change it which is why we wouldn't want git to overwrite the time stamp of a file but it does.

#### [Simon Hudon (Oct 08 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135372480):
I think we'd like to know if the file was built since the last commit that changed it

#### [Scott Morrison (Oct 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135386341):
This olean caching stuff is really important, and I will be super happy if we can get it working smoothly. I'm not sure I can help at the moment with the timestamp issues, but let me know if there's anything I can do.

#### [Scott Morrison (Oct 08 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135386369):
I hope one day we could even build a distributed cache; I could certainly contribute CPU cycles building olean files for central distribution.

#### [Simon Hudon (Oct 08 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135407646):
I'll keep at it

#### [Chris Hughes (Oct 08 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135420726):
I just have 17 copies of mathlib saved, so I never have to switch branches.

#### [Johan Commelin (Oct 08 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135420896):
Diskspace is cheap...

#### [Simon Hudon (Oct 08 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135421237):
I used to work like that. As the number of branches changes, I find it hard to manage

#### [Tobias Grosser (Oct 09 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451769):
Interesting. I am not really up-to-speed here, but i might be interesting to look at existing tools which address these issues.

#### [Tobias Grosser (Oct 09 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451775):
Specifically, there is 'ninja' a very fast alternative for make.

#### [Tobias Grosser (Oct 09 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451788):
And 'ccache' which caches the compilation of C/C++ files.

#### [Tobias Grosser (Oct 09 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451800):
If lean would have a way to export the "include" files, it might be possible to adapt these tools (or use at least their design).

#### [Tobias Grosser (Oct 09 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451863):
My feeling is that connecting .olean files to git branches is pretty fragile "hacky".

#### [Tobias Grosser (Oct 09 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451886):
Hashing the source files and having a proxy for returning the right source file in case a hash is already known is a strategy that works well in the OS projects I have been working on.

#### [Mario Carneiro (Oct 09 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451892):
lean already uses ninja for compilation

#### [Mario Carneiro (Oct 09 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451958):
You would have to hash the file plus the hashes of dependent files, git-style

#### [Tobias Grosser (Oct 09 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135451968):
Right. The ccache docu explains well what is needed to do this kind of caching.

#### [Tobias Grosser (Oct 09 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452307):
@**Mario Carneiro** , are you saying lean is using 'ninja' for compiling the lean binary, or is it called as part of 'lean --make'?

#### [Gabriel Ebner (Oct 09 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452480):
ninja can optionally be used to compile lean itself.  lean --make doesn't use ninja (the equivalent linja tool in Lean 2 did though).  Ninja doesn't do anything more fancy than lean --make, I believe.  (Does ninja use content hashes or modification times?)  Something like ccache might be interesting when switching between branches.

#### [Tobias Grosser (Oct 09 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452491):
Also, to get the dependent files lean already has a command '--deps'.

#### [Tobias Grosser (Oct 09 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452558):
Ninja does not do anything more fancy than lean --make, I assume.

#### [Tobias Grosser (Oct 09 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452561):
However, it is _very_ fast.

#### [Tobias Grosser (Oct 09 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452568):
in checking if files have been modified.

#### [Gabriel Ebner (Oct 09 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452580):
That is pretty much the least expensive part of running `lean --make` though.

#### [Tobias Grosser (Oct 09 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452581):
This does not matter for the perf problems we have today, but I feel it will matter in the future.

#### [Mario Carneiro (Oct 09 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452640):
the problem is that the usual dependency analysis will say that too many files are affected and compile them all

#### [Tobias Grosser (Oct 09 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452658):
Right, it's more a difference between 5 seconds and 0.01 second on clean builds. It really improves productivity on large C++ code bases and might be useful for lean as well (especially if we interactively want to update proofs).

#### [Tobias Grosser (Oct 09 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452665):
Right. Most of likely requires changes in lean proper.

#### [Mario Carneiro (Oct 09 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452711):
0.01 second vs 1 second to tell me that nothing needs doing doesn't seem so useful

#### [Mario Carneiro (Oct 09 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452724):
but if you could reason that most of the library is unaffected by a new theorem in `logic.basic` that would be a HUGE gain

#### [Mario Carneiro (Oct 09 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452727):
like an hour compilation

#### [Tobias Grosser (Oct 09 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452737):
I mean these are orthogonal.

#### [Mario Carneiro (Oct 09 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452748):
is it? I'm talking about proper caching and dependency analysis

#### [Tobias Grosser (Oct 09 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452800):
You need all a) proper dependency analysis, b) good caching, c) worry about how to check if files have changed.

#### [Tobias Grosser (Oct 09 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452808):
ninja is really good in minimizing file IO and stat calls to very quickly check for c)

#### [Mario Carneiro (Oct 09 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452818):
If there were thousands of files then I can see this being a problem

#### [Mario Carneiro (Oct 09 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452822):
but at that point total compile times will dwarf all of this

#### [Gabriel Ebner (Oct 09 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452860):
In server mode we don't even do any file IO?  We actually have a precomputed dependency graph.

#### [Tobias Grosser (Oct 09 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452893):
But it does not help with a) and b).

#### [Tobias Grosser (Oct 09 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452900):
I see.

#### [Tobias Grosser (Oct 09 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452946):
So my feeling is at some point we would just need proper caching in server mode.

#### [Tobias Grosser (Oct 09 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135452960):
Which would be a lean specific thing, that just needs to be implemented, right?

#### [Sebastian Ullrich (Oct 09 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135479143):
"just"

#### [Sebastian Ullrich (Oct 09 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135479146):
:)

#### [Simon Hudon (Oct 09 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500213):
I have created a branch of `ccache` to try and add support for Lean. I saw an issue discussion that suggests that it might be a simple business so I thought I'd try it out: https://github.com/leanprover-community/ccache

#### [Sebastian Ullrich (Oct 09 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500355):
Wow, I've been thinking about doing this for a long time, but didn't think anyone would ever actually go ahead with it...

#### [Sebastian Ullrich (Oct 09 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500422):
Though are you sure you don't want to modify https://github.com/mozilla/sccache instead :) ?

#### [Sebastian Ullrich (Oct 09 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500445):
(No idea if it would actually be easier, just newer code base, cloud support, and my preference for Rust)

#### [Simon Hudon (Oct 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500578):
That sounds like an even more useful tool. I don't know what it would take to adapt though

#### [Simon Hudon (Oct 09 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500603):
Do I understand correctly that it allows sharing binaries between team members or community members?

#### [Sebastian Ullrich (Oct 09 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500732):
I assume it's intended for sharing with trusted team members. Securing public r/w access to some cloud storage doesn't sound like a simple issue.

#### [Simon Hudon (Oct 09 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500844):
I think I'll put that issue aside to handle a simpler problem :)

#### [Patrick Massot (Oct 09 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500878):
Sounds like an important issues, I've seen people discussing assuming `nat = int`, they probably shouldn't be trusted

#### [Kenny Lau (Oct 09 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135500931):
how about we remove `*.olean` from `gitignore`?

#### [Simon Hudon (Oct 09 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135501059):
It is a big no-no. We don't want to keep the history of those files, we just want appropriate binaries. Keeping those binaries will make `git` slower and will make merging more complicated.

#### [Chris Hughes (Oct 09 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135501140):
Also `olean` is OS dependent

#### [Simon Hudon (Oct 09 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135501243):
@**Sebastian Ullrich** it looks like `sccache` works with Lean out of the box. You just call `sccache leanpkg build`. Does that make sense to you?

#### [Sebastian Ullrich (Oct 09 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135501295):
I have no idea. Does it look like it actually does anything?

#### [Sebastian Ullrich (Oct 09 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135501320):
(@**Chris Hughes** It's not, AFAIK. Though it will be architecture-dependent in Lean 4)

#### [Simon Hudon (Oct 09 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135501394):
It does look like it actually calls `leanpkg` but I'll have to experiment and see if a cache is created.

#### [Sebastian Ullrich (Oct 09 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135501476):
Yes, that would be the important part :smiley:

#### [Simon Hudon (Oct 09 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135501579):
If it does work out of the box, the next step would be integration: how do we make it invisible to the Lean user

#### [Simon Hudon (Oct 10 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135502099):
I think part of it working with `leanpkg` and `elan` is to create a symbolic link so that when `lean` is called, it calls `sccache lean` instead. @**Sebastian Ullrich** Does that sound like that could break the build system?

#### [Sebastian Ullrich (Oct 10 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135502577):
That could work

#### [Simon Hudon (Oct 10 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135502811):
Right now, I put a shell script called `~/.sccache/bin/lean` that just prints "calling lean" and I put it in my path (I checked with `which lean`) but `leanpkg` does not seem to call it

#### [Sebastian Ullrich (Oct 10 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503095):
oh https://github.com/leanprover/lean/blob/b13ac127fd83f3724d2f096b1fb85dc6b15e3746/bin/leanpkg#L24

#### [Simon Hudon (Oct 10 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503113):
So how does `elan` redirect to the right version of `lean`?

#### [Sebastian Ullrich (Oct 10 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503160):
It doesn't in that case, it just calls the right version of `leanpkg` :)

#### [Simon Hudon (Oct 10 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503203):
argh!

#### [Simon Hudon (Oct 10 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503261):
Any chance we might hard code `ccache` or `sccache` into `elan`?

#### [Sebastian Ullrich (Oct 10 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503278):
How would that help?

#### [Simon Hudon (Oct 10 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503369):
Maybe it could call a `leanpkg-2` bash script instead of `leanpkg` and also produce the `leanpkg-2` script so that the paths are set properly (for `sccache`). I have a feeling that that bash script did not change a lot between versions. Am I right?

#### [Sebastian Ullrich (Oct 10 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503577):
I see. But if you want to support both `sccache leanpkg` and `sccache lean` anyway, are you sure you save any code by making the former call the latter?

#### [Simon Hudon (Oct 10 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503683):
Actually, what I'd like to do is just replace every call to `lean` to `sccache lean`. `sccache` seems to index its cache by command line arguments.

#### [Simon Hudon (Oct 10 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135503859):
Actually, it might be enough to have `elan` rename `lean` to `lean-2` and create a bash script `lean` in its place to call `sccache` when `elan` downloads a version of `lean`

#### [Simon Hudon (Oct 10 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135570892):
@**Sebastian Ullrich** It's starting to look to me like we may have to alter the way `lean --make` works for either of `sccache` or `ccache` to be useable

#### [Sebastian Ullrich (Oct 10 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135570906):
I wouldn't be surprised :)

#### [Simon Hudon (Oct 10 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135570924):
Bummer, I was hoping it might be a small(-ish) thing to do

#### [Sebastian Ullrich (Oct 10 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135571003):
I was fully prepared that someone might at some point write an alternative `leanpkg` that fixes many issues with it (and would probably not be written in Lean)

#### [Simon Hudon (Oct 11 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135571113):
Is there a way to use `lean` to export all the dependencies in a project? `lean --deps` seems to interact poorly with leanpkg.toml files

#### [Simon Hudon (Oct 11 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135571264):
If I could use it, maybe I could generate a Makefile (or ninja config?) and that might be a better starting point than `lean --make`

#### [Sebastian Ullrich (Oct 11 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135571728):
I don't think so, you basically have to parse the file header...

#### [Tobias Grosser (Oct 11 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135614724):
+1 for 'ninja + make', at best if it's auto-generated from the lean files.

#### [Simon Hudon (Oct 11 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135614792):
The other tool I've heard of is Bazel. Have you heard of it and would you endorse it?

#### [Tobias Grosser (Oct 11 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615005):
Never used it.

#### [Tobias Grosser (Oct 11 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615032):
I feel it might be too high level.

#### [Tobias Grosser (Oct 11 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615039):
In the end we know all dependences.

#### [Tobias Grosser (Oct 11 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615050):
And just want to declare them and execute.

#### [Tobias Grosser (Oct 11 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615213):
I mean, you might also try to use cmake:
https://cmake.org/pipermail/cmake/2011-April/043761.html

#### [Tobias Grosser (Oct 11 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615236):
Not sure if this makes things easier.

#### [Tobias Grosser (Oct 11 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615286):
I fell, getting dependences out of lean files is certainly a useful component in any of these tools.

#### [Simon Hudon (Oct 11 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615513):
In the end, we'll probably need to parse the Lean files ourselves though, no? Unless we can get `lean` to get them out for us.

#### [Simon Hudon (Oct 11 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615802):
In the meantime, I started a branch in `sccache` and I talked to the developers on how to support Lean. It sounds doable. I just need to learn a bit more of Rust. And they seem willing to take our patch

#### [Tobias Grosser (Oct 11 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615854):
Cool. This sounds very exciting, indeed.

#### [Tobias Grosser (Oct 11 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615893):
What is the problem with --deps?

#### [Reid Barton (Oct 11 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135615984):
As far as I can tell, it just doesn't work properly

#### [Simon Hudon (Oct 11 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135616006):
I can't get it to work at the scale of a project. It seems to work off of `LEAN_PATH` which is no longer required (and indeed harmful) to work with `leanpkg`

#### [Tobias Grosser (Oct 11 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135616582):
I see. I have no idea of this code, but fixing it seems the most direct thing to do. In fact, does it do a lot more than parsing the imports?

#### [Tobias Grosser (Oct 11 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135616638):
AFAIU it should just parse the imports and then print this to stdout in some way.

#### [Reid Barton (Oct 11 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135616639):
Simon, have you gotten it to work under any circumstances?

#### [Reid Barton (Oct 11 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135617597):
Oh, I figured out why it is broken. It thinks that the presence of both `foo.lean` and `foo.olean` means that the import of `foo` is ambiguous.

#### [Reid Barton (Oct 11 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135617619):
So, this is something we could work around (in principle, at least)

#### [Simon Hudon (Oct 11 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135618364):
I was actually thinking that temporarily setting `LEAN_PATH` might fix it but I'm not done experimenting with it

#### [Reid Barton (Oct 11 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135618381):
I looked at `strace -e trace=file` output and it's clearly not failing to find the files it's looking for

#### [Reid Barton (Oct 11 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135618449):
And it is looking in the correct paths as reported by `lean -p` (and examining the source seems to indicate that `lean -p` is using the same path information as `lean --deps`)

#### [Simon Hudon (Oct 11 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135618997):
@**Sebastian Ullrich** Any chance we may get a fix for `lean --deps`?

#### [Sebastian Ullrich (Oct 11 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619199):
@**Simon Hudon** Yes, I feel that could be a reasonable change. It would be great if you or someone else could investigate fixing it

#### [Simon Hudon (Oct 11 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619323):
Sure I'll look into it. Do you have a suggestion of where I should start?

#### [Sebastian Ullrich (Oct 11 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619525):
The relevant call should be this one: https://github.com/leanprover/lean/blob/b13ac127fd83f3724d2f096b1fb85dc6b15e3746/src/shell/lean.cpp#L698

#### [Sebastian Ullrich (Oct 11 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619547):
Wow, `display_deps` is still testing for `.hlean` and `.lua`

#### [Reid Barton (Oct 11 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619731):
What I have inferred from looking at the source and the strace output: Say the module imports `data.rbmap`. `display_deps` calls
```c++
std::string find_file(search_path const & paths, std::string const & base, optional<unsigned> const & rel, name const & fname,
                      std::initializer_list<char const *> const & extensions) {
```
in `src/util/lean_path.cpp`. That calls `file_path` just above, because the import is not relative. That one tries each extension in the given list and pushes all the successes into a list of results.

#### [Reid Barton (Oct 11 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619803):
Because both `data/rbmap/default.lean` and `data/rbmap/default.olean` are found, that function raises an "ambiguous import" exception. Then `display_deps` catches the exception and reports an uninformative "file not found" error message.

#### [Reid Barton (Oct 11 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619828):
You may want to verify this by inserting tracing printfs and/or having `display_deps` show the original exception

#### [Simon Hudon (Oct 11 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619830):
Wow! you're fast!

#### [Sebastian Ullrich (Oct 11 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619917):
Nice work! This is the code the regular path uses for importing, you may want to adapt that https://github.com/leanprover/lean/blob/b13ac127fd83f3724d2f096b1fb85dc6b15e3746/src/library/module_mgr.cpp

#### [Reid Barton (Oct 11 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135619925):
I was just looking into this earlier (see my messages of 42 minutes ago)

#### [Sebastian Ullrich (Oct 11 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135620046):
Note that this code already looks completely different in Lean 4. So fixing this would only make sense if it was a big win for Lean 3 users (which a working `sccache` would probably be)

#### [Simon Hudon (Oct 11 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135620153):
I think it would be. It seems like a small fix on the Lean side and I'm hopeful `sccache` should be easily ported from Lean 3 to Lean 4 (once it works for Lean 3)

#### [Simon Hudon (Oct 11 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135620168):
@**Reid Barton** Can I leave that fix to you?

#### [Reid Barton (Oct 11 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135620573):
I can take a shot at it. We should make sure we have some working setup for `sccache` before upstreaming the change to Lean though. For testing purposes, you should be able to just remove `".olean"` from the list of extensions in `display_deps`.

#### [Simon Hudon (Oct 11 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135620680):
```quote
we have some working setup for sccache before upstreaming the change to Lean though
```

I think the fix is usable on its own. Why do you think we should wait?

#### [Reid Barton (Oct 11 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135620813):
Only because Lean 3 is currently in this state where it doesn't change without a particularly good reason

#### [Simon Hudon (Oct 11 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135620982):
It makes it harder to progress if we wait for everything to be ready before we push anything. If we do the heavy lifting, I don't think they will begrudge us fixing a problem even if the `sccache` idea doesn't pan out.

#### [Simon Hudon (Oct 11 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135624103):
I just tried removing `.olean` from the list in `display_deps` and it's working. Is that a good enough fix?

#### [Reid Barton (Oct 11 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135627574):
It seems like it should be good enough for us, though there could be other bugs lurking underneath. The other question is whether it would break any other users of Lean and specifically of `lean --deps`. The only way I could imagine the change breaking a working system is if that system uses out-of-tree builds (output `.olean` files not located in the same place as the corresponding source files) and also relies on `.olean` files as inputs without corresponding source `.lean` files. That seems pretty unlikely to me, considering that lean's library itself is not built out-of-tree, so at a minimum the implicit import of `init` will fail.

#### [Simon Hudon (Oct 11 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135627687):
That's also my impression. I wonder if they had anything else in mind when they put `.olean` in that list.

#### [Simon Hudon (Oct 11 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135627908):
@**Sebastian Ullrich** Here's the fix that did it for me: https://github.com/cipher1024/lean/commit/d2d81a3539bdf952eaf6126d2be69f2fda0b2f1f

#### [Simon Hudon (Oct 11 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135628632):
Also, is `--make` the only way to produce `.olean` files? For me, even if I give a file name, it seems to build the whole project. Is there any way around that?

#### [Reid Barton (Oct 11 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135628799):
It should only build the file you specify (and its dependencies if necessary)

#### [Simon Hudon (Oct 11 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135628948):
You're right, I misinterpreted what I saw

#### [Simon Hudon (Oct 11 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135629007):
Now with the fix, I managed to build a make file that discovers dependencies and builds what it needs.

#### [Tobias Grosser (Oct 11 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135629452):
Nice!

#### [Simon Hudon (Oct 11 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135629798):
I decided to go for bare minimum and only use `make`. We can make it more sophisticated once we see it is working.

#### [Tobias Grosser (Oct 11 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135629867):
Seems like a good idea. Looking forward to checkout the make file.

#### [Simon Hudon (Oct 11 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135631243):
I'll push it in a branch in a moment. If you have comments, I'd love to hear them

#### [Simon Hudon (Oct 11 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135631248):
It won't be functional because I hard coded a path to my Lean version

#### [Sebastian Ullrich (Oct 11 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135632212):
You can use elan to manage your local Lean fork :)

#### [Simon Hudon (Oct 11 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135632230):
Niiice! How?

#### [Sebastian Ullrich (Oct 11 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135632317):
`elan help toolchain link`

#### [Sebastian Ullrich (Oct 11 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135632390):
"crate", oops

#### [Simon Hudon (Oct 11 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135632476):
Haha! I didn't even notice! I was thinking that you've been pretty thorough in replacing Rust with Lean :)

#### [Simon Hudon (Oct 11 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135632579):
Btw, have you looked at my commit?

#### [Sebastian Ullrich (Oct 11 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135632845):
Yeah, I think it should be fine. You can remove ".lua" too.

#### [Simon Hudon (Oct 11 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135632879):
Will do!

#### [Simon Hudon (Oct 11 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135634431):
Here we go: https://github.com/leanprover/lean/pull/1978

#### [Simon Hudon (Oct 11 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135637248):
Is it possible to use `elan` to refer to a specific git commit on github?

#### [Simon Hudon (Oct 12 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135641178):
@**Tobias Grosser** here is what I did for the Makefile. It generates dependency files for each `.lean` file before it gets started building any files and the first time you get a lot of error messages because they are missing.

https://github.com/leanprover-community/mathlib/commit/d090d711c0b438223479635b663e720dab2d07e7

#### [Simon Hudon (Oct 12 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135642448):
@**Sebastian Ullrich** You use emacs right? What do you use for Rust?

#### [Tobias Grosser (Oct 12 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135655934):
Nice. 
```quote
@**Tobias Grosser** here is what I did for the Makefile. It generates dependency files for each `.lean` file before it gets started building any files and the first time you get a lot of error messages because they are missing.

https://github.com/leanprover-community/mathlib/commit/d090d711c0b438223479635b663e720dab2d07e7
```
Now just the sccache needs to work. I feel this might indeed be a great improvement. 

Best Tobias

#### [Johan Commelin (Oct 16 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135919858):
My laptop just crashed while compiling mathlib. This is the first time it crashed in a couple of years. We really need to make mathlib easier on prehistoric hardware :dragon:

#### [Simon Hudon (Oct 16 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135923867):
I'm sciencing as fast as I can ... it's coming

#### [Kenny Lau (Oct 16 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135924071):
or we can make mathlib compile *faster*

#### [Simon Hudon (Oct 16 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/135924198):
I don't think we should pick just one

#### [Scott Morrison (Nov 19 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/147996200):
Hi @**Simon Hudon**, would you have time to give a status update on `sccache` integration, in particular pointing out if there are places someone else could help write code/investigate issues/do some research?

#### [Simon Hudon (Nov 19 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/147996348):
Sure. I can push what I currently have

#### [Simon Hudon (Nov 19 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/147996392):
What I did is provide a way for sscache to determine if an olean file is outdated or not through hashing.

#### [Simon Hudon (Nov 19 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/147996477):
I'm still struggling to get the tests to pass. I think once that work, we should have a version sscache that can locally cache any lean build we like.

#### [Simon Hudon (Nov 19 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/147996521):
I wrote a Makefile to take advantage of it and I pushed it on leanprover-community. I also made a patch to lean itself to fix the way it computes dependencies

#### [Simon Hudon (Nov 19 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/147996650):
After I'm done with this part, one possible extension (if you want to spend the time) is figure out how to get some cloud storage to store a Lean cache. That would involve configuring sccache itself and setting up instructions for people who want to access the cache.

#### [Simon Hudon (Nov 19 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/147996663):
At this point I see that more as goody than as a must have though

#### [Scott Morrison (Nov 20 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148010429):
I pushed two minor changes to the `build-system` branch.

#### [Scott Morrison (Nov 21 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148089909):
Where is that "is an olean file outdated, via hashing" code?

#### [Scott Morrison (Nov 21 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090026):
Using timestamps to decide whether to recompile makes life really difficult. Do we know an obstacle (besides patching Lean), to instead have each olean file contain a hash of its source file and of the olean files for each of its imports? To decide if an olean file is stale or not you would read those hash from the olean file, and compare them against the current hashes of those files.

#### [Scott Morrison (Nov 21 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090031):
Once one `.lean` file changes, this would propagate staleness of all dependent `.olean` files.

#### [Scott Morrison (Nov 21 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090032):
And no timestamps would ever be considered.

#### [Scott Morrison (Nov 21 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090072):
Or, @**Simon Hudon**, is this what you've already done?

#### [Simon Hudon (Nov 21 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090145):
That's what I'm working on yes. More exactly, when calling `sccache lean --make foo.lean`, we get the list of modules imported (directly or indirectly) by `foo.lean`, we hash all of them (including `foo.lean`) and recompile only if that hash changes.

#### [Scott Morrison (Nov 21 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090216):
I see -- you hash the source files of the imports, or the olean files?

#### [Scott Morrison (Nov 21 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090260):
And this is all being done by the sccache wrapper, with no modification of Lean?

#### [Simon Hudon (Nov 21 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090261):
The sources

#### [Simon Hudon (Nov 21 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090263):
That's correct

#### [Scott Morrison (Nov 21 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090270):
But won't we then get burnt still by Lean being wrong about what is stale?

#### [Simon Hudon (Nov 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090279):
I'd like to hash the olean but all the ways I have thought of are flawed

#### [Simon Hudon (Nov 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090284):
What do you mean?

#### [Scott Morrison (Nov 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090288):
Say we have files A < B < C, and A and B are already built correctly, according to their hashes, while C needs to be rebuilt.

#### [Scott Morrison (Nov 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090292):
But suppose the timestamps on A.olean and B.olean are messed up.

#### [Scott Morrison (Nov 21 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090339):
When sccache invokes Lean on C.lean, what is to stop Lean from going and recompiling A and B?

#### [Simon Hudon (Nov 21 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090365):
I don't think this will be happening but I have to double check. Maybe @**Sebastian Ullrich** can tell us. If we call `lean --make foo.lean`, will Lean attempt to rebuild any of the dependencies? If so, is there a way to tell it not to?

#### [Simon Hudon (Nov 21 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148090473):
One thing I have considered is to manually set the modification time of the `olean` files when they don't need to be rebuilt. That should solve the issue.

#### [Sebastian Ullrich (Nov 21 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/148095554):
Yeah, that's what I would have proposed, too

#### [Johan Commelin (Dec 15 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/151848308):
@**Scott Morrison|110087** @**Simon Hudon** Any updates on the caching front? (Yes, indeed, I thought of it again because I'm currently recompiling... :lol:)

#### [Simon Hudon (Dec 15 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/151848324):
Haha! I actually managed to make progress on it today and yesterday. Now I'm testing it and I'm hoping I can roll out a version soon

#### [Johan Commelin (Dec 15 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/151848327):
Awesome news!

#### [Simon Hudon (Dec 17 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/152043694):
I managed to build a version that passes all their tests:

https://github.com/leanprover-community/sccache/tree/lean-support-2

#### [Simon Hudon (Dec 17 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/152043765):
When I try it with my Makefile though, it fails. There seems to be issue with the timing when `sccache` produces the binaries

#### [Simon Hudon (Dec 17 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/olean%20caching/near/152043832):
If someone wants to try it for themselves, I can share the Makefile

