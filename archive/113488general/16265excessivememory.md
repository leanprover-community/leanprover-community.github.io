---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16265excessivememory.html
---

## Stream: [general](index.html)
### Topic: [excessive memory](16265excessivememory.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134535868):
On my laptop I get the following error pretty often:
```
excessive memory consumption detected at 'replace' (potential solution: increase memory consumption threshold)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 24 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134535884):
maybe you should increase memory consumption threshold

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134535887):
I also see in `top` that there are 8 processes of VScode open, whereas I just `kill -9`ed all of them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134535895):
This is on an almost empty file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134535903):
I just killed all Lean and VScodes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134535922):
Does this just mean that my laptop is too old for Lean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536066):
Hmm.. if I close the VScode window, all the processes are gone in `top`. I don't know why VScode spawns so many subprocesses if I have only one file open.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536204):
I have at least 2.5 GB of unused RAM on this box. I wish that would be enough.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536228):
Maybe I should try a reinstall of VScode. But this feels like cargo-cult troubleshooting.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536373):
Were they really different processes? Do you have 8 cpus?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536388):
I guess probably not if your laptop is 11 years old

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536454):
I have two single thread cpu's I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536484):
One socket with 2 cores; and 1 thread per core.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536505):
They had different process id's

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536515):
Ah, okay

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536625):
I think "excessive memory" means Lean hit a limit it set for itself, though. Not "the machine is out of memory".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536641):
I see this error a lot and just restart lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536649):
But it is annoying when you get it right at startup

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536668):
If I'dd get it once a day I could live with it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 25 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134579407):
It's a shame. So many people here, serious people, talk about issues with compile times and stuff like this. I use Lean on a 2-year-old PC with 8 cores and 16 gigs of ram, and mathlib compiles in 6 minutes. I think we need to crowd fund for better hardware for the community. I should edit the mathoverflow post -- "instead of upvoting, consider a $5 donation to the Lean Hardware Hardship fund"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 25 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134580139):
On the subject of hardware, I managed to install a version of CoCalc inside Docker yesterday, running on my hardware.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 25 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134580140):
It's at <https://54.91.0.213:8080/app> for now (no promises about uptime yet!)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 25 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134580182):
(and apologies that it is over https but there's no certificate; you may have to click through a warning, depending on your browser)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 25 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134580183):
I think for now anyone can create an account there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 25 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134580184):
It's running on quite fast hardware.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 25 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134580201):
Unfortunately `cocalc` by default seems to kill long-running processes, so I can't actually run `leanpkg build` on mathlib to time it...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 25 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134580202):
Hopefully there is a setting somewhere to disable this, but I haven't found it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 25 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134581116):
You might have to pay. I will learn more about this today (cocalc admin is on my list). I think the idea is that I get some credits for a project, and one of the things I can spend credits on is leaving processes to run for longer.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 25 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134590013):
@**Scott Morrison|110087**, in case you're unfamiliar with it, https://certbot.eff.org/ is a very easy way to set up a properly-signed SSL certificate, at least on Ubuntu systems or similar.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 25 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134590071):
Though if you have some strange firewall setup, it might be a bit more complicated.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 25 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134590794):
I created an account and tried to use Lean but it doesn't seem to work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) William Stein (Sep 26 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134686294):
```quote
Unfortunately `cocalc` by default seems to kill long-running processes, so I can't actually run `leanpkg build` on mathlib to time it...
```
Send me a link to your project (or open a support request by clicking Help with your project open in cocalc) and I'll increase the "idle timeout" from the default (30 minutes) to something much longer.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) William Stein (Sep 26 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134686311):
```quote
You might have to pay. I will learn more about this today (cocalc admin is on my list). I think the idea is that I get some credits for a project, and one of the things I can spend credits on is leaving processes to run for longer.
```

Yep, that's the "idle timeout" quota.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 26 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134691657):
But Scott is running the CoCalc software on his own server, right? So Scott needs to make that idle timeout change in his own copy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 26 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134705207):
Yes, @**William Stein**, this was a question about cocalc in Docker.

(Don't worry, I'm not being distracted by Docker; I'm working on getting courses signed up to the real cocalc too. :-)

At least in docker, the processes are being killed (exit code 137) much faster than every 30 minutes; it's more like 3 minutes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) William Stein (Sep 27 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134707301):
> At least in docker, the processes are being killed (exit code 137) much faster than every 30 minutes; it's more like 3 minutes.

OK, that's weird.  By default, I don't think anything is ever killed by cocalc in Docker, since there are no quotas/upgrades/etc. for docker-cocalc.  Also, CoCalc doesn't kill processes when something is idle -- it kills entire projects.  So it may be something particular to your Docker setup.   What's the simplest example that I can try to reproduce of what you're observing?

