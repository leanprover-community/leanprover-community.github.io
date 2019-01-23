---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42501Tellleanpkgtousen1cpucores.html
---

## Stream: [general](index.html)
### Topic: [Tell leanpkg to use (n-1) cpu cores](42501Tellleanpkgtousen1cpucores.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029086):
Yesterday I rebuilt mathlib and it froze my desktop for > 2hrs. I would like to tell leanpkg to use only 3 of my 4 cores. I'm on Linux. Should I use fancy `cgroups` for this, or is there some easy method?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029518):
Hmm, maybe `nice leanpkg build` will do the job.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029520):
Let's see if I stay responsive (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029818):
Nope... on my laptop again...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029823):
Stupid `nice`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Aug 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029867):
You can use `lean -j3 --make`.  But I don't think that using all cores is the cause for your computer freezing.  It's much more likely to be memory usage.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029873):
I've got 8 GB, shouldn't that be sufficient?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029882):
the answer is always no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029957):
Whelp... it is indeed using >7 GB

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029977):
No, something is off. The lean process with niceness 10 is using only 10% of my memory.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030025):
I've got to kill some other memory hog.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030051):
So, do you guys have a strategy for keeping your system responsive during rebuilds? Or you only rebuild during lunch?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Aug 07 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030201):
What are you building?  I know that Lean eats memory for breakfast, but mathlib takes only 7 minutes and 1.5G of RAM here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030367):
I am trying to rebuild mathlib. The 1.5GB seems to be what my system is using as well.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030370):
The 7 minutes... not really.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030379):
It is still frozen to the core.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030557):
Might it be a problem that I launched the rebuild from a feature branch?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030565):
It only had changes in 1 file, compared to mathlib HEAD.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Aug 07 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030633):
No the small change should make it faster.  But maybe the change causes a `by simp` to time out?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Aug 07 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030649):
Wait, by frozen you just mean that lean is frozen, not your whole machine?  What is the last line that lean printed?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030659):
No, the machine is frozen.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030669):
I currently have a frozen `top` in front of me. I can't even issue a kill.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 07 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030723):
you are awfully chatty for someone with a bricked computer

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030732):
I'm on a laptop...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030738):
People have >3 devices with Zulip on it nowadays, don't they?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030757):
Ok, so the last line that lean printed says that it is making stuff on Turing machines.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030761):
That shouldn't get me stuck.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Aug 07 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030813):
Which branch are you on?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030832):
`map2`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030875):
It is a feature branch that I'm trying to PR containing about 25 lines of changes in `linear_algebra/multivariate_polynomial.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Aug 07 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131031229):
Good news!  The branch builds!  (Not very helpful, I know.)
Can you try `rm **/*.olean` and build again?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131031311):
Nope, I can't... It is still frozen...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 07 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131031724):
isn't it time to reboot?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131031732):
It made a bit of progress! But it is still really slow.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131031778):
I'm one of those guys that don't like to reboot a linux box. It feels like epic failure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131033097):
Yoochai! It survived. I managed to execute `killall code`, which closed 3 instances of VScode working on different Lean projects.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131033139):
Now the compile is running smoothly again!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 07 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131033155):
I guess I need more RAM

