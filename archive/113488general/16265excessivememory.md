---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16265excessivememory.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [excessive memory](https://leanprover-community.github.io/archive/113488general/16265excessivememory.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Sep 24 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134535868):
<p>On my laptop I get the following error pretty often:</p>
<div class="codehilite"><pre><span></span>excessive memory consumption detected at &#39;replace&#39; (potential solution: increase memory consumption threshold)
</pre></div>

#### [ Kenny Lau (Sep 24 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134535884):
<p>maybe you should increase memory consumption threshold</p>

#### [ Johan Commelin (Sep 24 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134535887):
<p>I also see in <code>top</code> that there are 8 processes of VScode open, whereas I just <code>kill -9</code>ed all of them.</p>

#### [ Johan Commelin (Sep 24 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134535895):
<p>This is on an almost empty file</p>

#### [ Johan Commelin (Sep 24 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134535903):
<p>I just killed all Lean and VScodes</p>

#### [ Johan Commelin (Sep 24 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134535922):
<p>Does this just mean that my laptop is too old for Lean?</p>

#### [ Johan Commelin (Sep 24 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536066):
<p>Hmm.. if I close the VScode window, all the processes are gone in <code>top</code>. I don't know why VScode spawns so many subprocesses if I have only one file open.</p>

#### [ Johan Commelin (Sep 24 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536204):
<p>I have at least 2.5 GB of unused RAM on this box. I wish that would be enough.</p>

#### [ Johan Commelin (Sep 24 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536228):
<p>Maybe I should try a reinstall of VScode. But this feels like cargo-cult troubleshooting.</p>

#### [ Reid Barton (Sep 24 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536373):
<p>Were they really different processes? Do you have 8 cpus?</p>

#### [ Reid Barton (Sep 24 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536388):
<p>I guess probably not if your laptop is 11 years old</p>

#### [ Johan Commelin (Sep 24 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536454):
<p>I have two single thread cpu's I think</p>

#### [ Johan Commelin (Sep 24 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536484):
<p>One socket with 2 cores; and 1 thread per core.</p>

#### [ Johan Commelin (Sep 24 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536505):
<p>They had different process id's</p>

#### [ Reid Barton (Sep 24 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536515):
<p>Ah, okay</p>

#### [ Reid Barton (Sep 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536625):
<p>I think "excessive memory" means Lean hit a limit it set for itself, though. Not "the machine is out of memory".</p>

#### [ Reid Barton (Sep 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536641):
<p>I see this error a lot and just restart lean</p>

#### [ Johan Commelin (Sep 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536649):
<p>But it is annoying when you get it right at startup</p>

#### [ Johan Commelin (Sep 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134536668):
<p>If I'dd get it once a day I could live with it.</p>

#### [ Kevin Buzzard (Sep 25 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134579407):
<p>It's a shame. So many people here, serious people, talk about issues with compile times and stuff like this. I use Lean on a 2-year-old PC with 8 cores and 16 gigs of ram, and mathlib compiles in 6 minutes. I think we need to crowd fund for better hardware for the community. I should edit the mathoverflow post -- "instead of upvoting, consider a $5 donation to the Lean Hardware Hardship fund"</p>

#### [ Scott Morrison (Sep 25 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134580139):
<p>On the subject of hardware, I managed to install a version of CoCalc inside Docker yesterday, running on my hardware.</p>

#### [ Scott Morrison (Sep 25 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134580140):
<p>It's at &lt;<a href="https://54.91.0.213:8080/app" target="_blank" title="https://54.91.0.213:8080/app">https://54.91.0.213:8080/app</a>&gt; for now (no promises about uptime yet!)</p>

#### [ Scott Morrison (Sep 25 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134580182):
<p>(and apologies that it is over https but there's no certificate; you may have to click through a warning, depending on your browser)</p>

#### [ Scott Morrison (Sep 25 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134580183):
<p>I think for now anyone can create an account there.</p>

#### [ Scott Morrison (Sep 25 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134580184):
<p>It's running on quite fast hardware.</p>

#### [ Scott Morrison (Sep 25 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134580201):
<p>Unfortunately <code>cocalc</code> by default seems to kill long-running processes, so I can't actually run <code>leanpkg build</code> on mathlib to time it...</p>

#### [ Scott Morrison (Sep 25 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134580202):
<p>Hopefully there is a setting somewhere to disable this, but I haven't found it.</p>

#### [ Kevin Buzzard (Sep 25 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134581116):
<p>You might have to pay. I will learn more about this today (cocalc admin is on my list). I think the idea is that I get some credits for a project, and one of the things I can spend credits on is leaving processes to run for longer.</p>

#### [ Reid Barton (Sep 25 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134590013):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span>, in case you're unfamiliar with it, <a href="https://certbot.eff.org/" target="_blank" title="https://certbot.eff.org/">https://certbot.eff.org/</a> is a very easy way to set up a properly-signed SSL certificate, at least on Ubuntu systems or similar.</p>

#### [ Reid Barton (Sep 25 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134590071):
<p>Though if you have some strange firewall setup, it might be a bit more complicated.</p>

#### [ Patrick Massot (Sep 25 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134590794):
<p>I created an account and tried to use Lean but it doesn't seem to work.</p>

#### [ William Stein (Sep 26 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134686294):
<blockquote>
<p>Unfortunately <code>cocalc</code> by default seems to kill long-running processes, so I can't actually run <code>leanpkg build</code> on mathlib to time it...</p>
</blockquote>
<p>Send me a link to your project (or open a support request by clicking Help with your project open in cocalc) and I'll increase the "idle timeout" from the default (30 minutes) to something much longer.</p>

#### [ William Stein (Sep 26 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134686311):
<blockquote>
<p>You might have to pay. I will learn more about this today (cocalc admin is on my list). I think the idea is that I get some credits for a project, and one of the things I can spend credits on is leaving processes to run for longer.</p>
</blockquote>
<p>Yep, that's the "idle timeout" quota.</p>

#### [ Reid Barton (Sep 26 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134691657):
<p>But Scott is running the CoCalc software on his own server, right? So Scott needs to make that idle timeout change in his own copy</p>

#### [ Scott Morrison (Sep 26 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134705207):
<p>Yes, <span class="user-mention" data-user-id="116034">@William Stein</span>, this was a question about cocalc in Docker.</p>
<p>(Don't worry, I'm not being distracted by Docker; I'm working on getting courses signed up to the real cocalc too. :-)</p>
<p>At least in docker, the processes are being killed (exit code 137) much faster than every 30 minutes; it's more like 3 minutes.</p>

#### [ William Stein (Sep 27 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/excessive%20memory/near/134707301):
<blockquote>
<p>At least in docker, the processes are being killed (exit code 137) much faster than every 30 minutes; it's more like 3 minutes.</p>
</blockquote>
<p>OK, that's weird.  By default, I don't think anything is ever killed by cocalc in Docker, since there are no quotas/upgrades/etc. for docker-cocalc.  Also, CoCalc doesn't kill processes when something is idle -- it kills entire projects.  So it may be something particular to your Docker setup.   What's the simplest example that I can try to reproduce of what you're observing?</p>


{% endraw %}
