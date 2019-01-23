---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/38818leanpkgbreaksmymathlib.html
---

## Stream: [general](index.html)
### Topic: [leanpkg breaks my mathlib](38818leanpkgbreaksmymathlib.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401172):
```
buzzard@bob:~/Lean/lean-projects/xena-UROP-2018$ more leanpkg.toml 
[package]
name = "xena-UROP-2018"
version = "0.1"
lean_version = "3.4.1"
path = "src"

[dependencies]
mathlib = {git = "https://github.com/leanprover/mathlib", rev = "c8ad5cfd793153bff38c49c54940f04d86cb7616"}
buzzard@bob:~/Lean/lean-projects/xena-UROP-2018$ # commit number is mathlib HEAD
buzzard@bob:~/Lean/lean-projects/xena-UROP-2018$ leanpkg upgrade
mathlib: trying to update _target/deps/mathlib to revision c8ad5cfd793153bff38c49c54940f04d86cb7616
> git checkout --detach c8ad5cfd793153bff38c49c54940f04d86cb7616    # in directory _target/deps/mathlib
Previous HEAD position was a30b7c7... feat(data/string): fix string_lt, add repr for multiset, pnat
HEAD is now at c8ad5cf... fix(computability/turing_machine): fix import
configuring xena-UROP-2018 0.1
mathlib: trying to update _target/deps/mathlib to revision a30b7c773db17cf7d1b551ba0f24645079296628
> git checkout --detach a30b7c773db17cf7d1b551ba0f24645079296628    # in directory _target/deps/mathlib
Previous HEAD position was c8ad5cf... fix(computability/turing_machine): fix import
HEAD is now at a30b7c7... feat(data/string): fix string_lt, add repr for multiset, pnat
buzzard@bob:~/Lean/lean-projects/xena-UROP-2018$ more leanpkg.toml 
[package]
name = "xena-UROP-2018"
version = "0.1"
lean_version = "3.4.1"
path = "src"

[dependencies]
mathlib = {git = "https://github.com/leanprover/mathlib", rev = "a30b7c773db17cf7d1b551ba0f24645079296628"}
buzzard@bob:~/Lean/lean-projects/xena-UROP-2018$ # mathlib now a commit from 19 days ago which doesn't compile
buzzard@bob:~/Lean/lean-projects/xena-UROP-2018$ 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401237):
My `leanpkg.toml` for a Xena project repo on GH seems to want to use commit `a30b7c773db17cf7d1b551ba0f24645079296628` of mathlib, which does not compile. I can edit `leanpkg.toml` manually and point it at the mathlib revision I want, but `leanpkg upgrade` then rolls it back. What am I doing wrong?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401302):
```
$ lean --version
Lean (version 3.4.1, commit 17fe3decaf8a, Release)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 10 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401496):
I tried cloning and typing `leanpkg upgrade` and `leanpkg` changed the toml to the latest update.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 10 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401543):
I've pushed, so it might work now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401632):
This does not fix it for me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401653):
I just cloned and ran `leanpkg upgrade`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401666):
"Have you tried turning `bob` off and on again"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401669):
are you serious?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401710):
Who's bob?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401712):
His computer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401714):
I saw this behaviour on Luca's mac yesterday

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401718):
and I'm now experiencing it myself on linux

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 10 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401726):
I guess Chris is running Windows...?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 10 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401733):
Correct.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401734):
I cloned and ran `leanpkg upgrade` and I'm back to `a30b7c7`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401737):
which doesn't compile

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401822):
Hmm, and you both have the same version of Lean, hence the same leanpkg, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401830):
I can't guarantee that we're using the same version of Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401837):
I am using 3.4.1 stable and I think Chris might be using the 20/4 nightly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401844):
I'm using `Lean (version 3.4.1, nightly-2018-04-20, commit f59c2f0ef59f, Release)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401846):
they differ by about one commit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401889):
```
$ lean --version
Lean (version 3.4.1, commit 17fe3decaf8a, Release)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402002):
Aah!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402013):
Mathlib branch 3.4.1 which Mario didn't want to make -- he has clearly decided to get his own back by pointing it at the `a30b7c7` commit and leaving it there!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402065):
@**Mario Carneiro** help! Can you change the `3.4.1` branch of mathlib to something which compiles?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 10 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402085):
So the issue is that you're version wants to use the `3.4.1` branch and my version wants to use master?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402103):
Maybe.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402149):
The underlying issue is that I want everyone (except people like you who know what they're doing) to be using the exact same version of Lean and mathlib.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402155):
Because that is the sane way to proceed, in my opinion.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402157):
Why are there two identical branches anyway?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402173):
Same answer.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402186):
I want to tell my users "download Lean 3.4.1 and mathlib 3.4.1" and I want the consequence of this to be that everyone downloads the same thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402209):
Mario says "mathlib does not work like this, I will not release a 3.4.1"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402271):
The compromise was that he released a 3.4.1 branch and used to keep it up to date with mathlib HEAD but maybe he forgot to do this recently and unfortunately we've settled on a version of mathlib which doesn't compile.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 10 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402481):
That's not really necessary until master uses `3.4.2` is it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402531):
Actually I left `3.4.1` branch there because Leo pushed a commit on lean repo after that, so technically `master` is back on nightlies

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402535):
Chris -- currently when my users say "what version of Lean should I download"? I say "3.4.1 stable, here's the link" and when they say "what version of mathlib should I download" I say "don't worry about mathlib, let leanpkg do the magic for you".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402577):
and currently the magic it does is that it downloads a broken version

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 10 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402578):
It should be a working version though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402584):
It has a red X on the list of commits and I just failed to compile it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 10 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402591):
just pick a working version

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402604):
Which version of Lean should I be using with it? 3.4.1 stable as advertised here: https://github.com/leanprover/lean/releases/tag/v3.4.1 ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402609):
Kenny it's not as simple as that. I can get it working myself, it's my users that are having problems.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402616):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402620):
Currently if you follow the readme here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402622):
https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/README.md

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402627):
then compilation of mathlib fails

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 10 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402678):
Oh, I see what you mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 10 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402682):
fixed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 10 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402686):
Many thanks for the prompt work!

