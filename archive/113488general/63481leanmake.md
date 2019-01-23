---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63481leanmake.html
---

## Stream: [general](index.html)
### Topic: [lean --make](63481leanmake.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 15 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132187468):
When I rebuild mathlib, I get the impression that it is recreating olean files for all lean files, even if they (and their dependencies) were not touched since the last build. Is that impression correct?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Aug 15 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132187640):
Only touched files will be recompiled.  Touched = changed modification time.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 15 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132187780):
I think it recompiles anything that depends on a file that changed, so if there's a change in `nat.basic` that pretty much means everything is recompiled.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 17 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132283339):
```shell
time leanpkg build
configuring mathlib 0.1
WARNING: leanpkg configurations not specifying `path = "src"` are deprecated.
> lean --make .

real    70m6.346s
user    135m39.224s
sys     0m24.410s
```
Is this normal? This is on my (t)rusty Thinkpad X61 with > 3GB of free RAM. Does this mean I'm doomed to replace it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Aug 17 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132285528):
It only takes 7 minutes here.  This is with a i7-6700K and 16G RAM (not that it matters).
```
± time leanpkg build
configuring mathlib 0.1
WARNING: leanpkg configurations not specifying `path = "src"` are deprecated.
> lean --make .
3200.96user 8.01system 7:18.76elapsed 731%CPU (0avgtext+0avgdata 1617680maxresident)k
37824inputs+53080outputs (77major+2781504minor)pagefaults 0swaps
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 17 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132285548):
That's with 8 threads?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Aug 17 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132285607):
The cpu has only 4 cores.  Each core can run two threads (via hyperthreading), but that doesn't improve performance by much.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 18 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357383):
```shell
[jmc@atarrimbo mathlib]$ time leanpkg build
configuring mathlib 0.1
WARNING: leanpkg configurations not specifying `path = "src"` are deprecated.
> lean --make .

real    7m39.967s
user    102m20.003s
sys     0m46.845s
```
That's on my (still rather ancient) server with 8 cores. I'll see if I can offload compilation to this mammoth.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 18 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357388):
did that actually take an hour or 7 minutes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 18 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357390):
7m39

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 18 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357400):
The `user` time is measured across all cores and threads.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 18 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357403):
have you tried running with the `-j` option?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 18 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357406):
How would `-j` help?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 18 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357463):
```shell
[jmc@atarrimbo mathlib]$ echo $((7*16))
112
```
So there were 16 threads running almost full-time for 7 minutes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 18 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357586):
```shell
[jmc@atarrimbo mathlib]$ cat /proc/cpuinfo | grep name | uniq
model name      : Intel(R) Xeon(R) CPU           E5540  @ 2.53GHz
```
I guess these are about 10 years old. All those modern i7's probably beat 4 of these hands-down. And I have only 16 of them. So if you have a quad-core...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 18 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357634):
Mario, did you ever time a fresh build of mathlib on your hardware?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 18 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357706):
I'll get back to you in an hour

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 18 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132360198):
```
$ time lean --make

real    18m43.275s
user    0m0.000s
sys     0m0.015s
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 18 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132360342):
I have 2 cores, 4 logical processors @ 2.90 GHz on my laptop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Aug 18 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132360657):
Ok cool. But why is `user` equal to `0`? What OS do you have?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 18 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132361017):
windows

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 18 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132361020):
running MSYS2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/136914467):
I wish `lean --make` could have some debugging output, like at least how many files have been compiled

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 01 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/136919856):
It actually does print a bunch of output, just apparently not on Windows? I was really confused when I tried Lean on a Windows machine for the first time and `lean --make` was silent

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 01 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/136920069):
It prints a bunch of output on my windows machine with the latest nightly. With April nightly it didn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 01 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/136920234):
Interesting. I think I was using 3.4.1.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 01 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/136924729):
I already `git pull`ed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 01 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/136928284):
I have to use `winpty lean --make` on msys2 to get output

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 01 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/136928309):
I think the terminal detection is broken


{% endraw %}
