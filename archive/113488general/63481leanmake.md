---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63481leanmake.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [lean --make](https://leanprover-community.github.io/archive/113488general/63481leanmake.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Aug 15 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132187468):
<p>When I rebuild mathlib, I get the impression that it is recreating olean files for all lean files, even if they (and their dependencies) were not touched since the last build. Is that impression correct?</p>

#### [ Gabriel Ebner (Aug 15 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132187640):
<p>Only touched files will be recompiled.  Touched = changed modification time.</p>

#### [ Chris Hughes (Aug 15 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132187780):
<p>I think it recompiles anything that depends on a file that changed, so if there's a change in <code>nat.basic</code> that pretty much means everything is recompiled.</p>

#### [ Johan Commelin (Aug 17 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132283339):
<div class="codehilite"><pre><span></span><span class="nb">time</span> leanpkg build
configuring mathlib <span class="m">0</span>.1
WARNING: leanpkg configurations not specifying <span class="sb">`</span><span class="nv">path</span> <span class="o">=</span> <span class="s2">&quot;src&quot;</span><span class="sb">`</span> are deprecated.
&gt; lean --make .

real    70m6.346s
user    135m39.224s
sys     0m24.410s
</pre></div>


<p>Is this normal? This is on my (t)rusty Thinkpad X61 with &gt; 3GB of free RAM. Does this mean I'm doomed to replace it?</p>

#### [ Gabriel Ebner (Aug 17 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132285528):
<p>It only takes 7 minutes here.  This is with a i7-6700K and 16G RAM (not that it matters).</p>
<div class="codehilite"><pre><span></span>± time leanpkg build
configuring mathlib 0.1
WARNING: leanpkg configurations not specifying `path = &quot;src&quot;` are deprecated.
&gt; lean --make .
3200.96user 8.01system 7:18.76elapsed 731%CPU (0avgtext+0avgdata 1617680maxresident)k
37824inputs+53080outputs (77major+2781504minor)pagefaults 0swaps
</pre></div>

#### [ Johan Commelin (Aug 17 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132285548):
<p>That's with 8 threads?</p>

#### [ Gabriel Ebner (Aug 17 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132285607):
<p>The cpu has only 4 cores.  Each core can run two threads (via hyperthreading), but that doesn't improve performance by much.</p>

#### [ Johan Commelin (Aug 18 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357383):
<div class="codehilite"><pre><span></span><span class="o">[</span>jmc@atarrimbo mathlib<span class="o">]</span>$ <span class="nb">time</span> leanpkg build
configuring mathlib <span class="m">0</span>.1
WARNING: leanpkg configurations not specifying <span class="sb">`</span><span class="nv">path</span> <span class="o">=</span> <span class="s2">&quot;src&quot;</span><span class="sb">`</span> are deprecated.
&gt; lean --make .

real    7m39.967s
user    102m20.003s
sys     0m46.845s
</pre></div>


<p>That's on my (still rather ancient) server with 8 cores. I'll see if I can offload compilation to this mammoth.</p>

#### [ Mario Carneiro (Aug 18 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357388):
<p>did that actually take an hour or 7 minutes</p>

#### [ Johan Commelin (Aug 18 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357390):
<p>7m39</p>

#### [ Johan Commelin (Aug 18 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357400):
<p>The <code>user</code> time is measured across all cores and threads.</p>

#### [ Mario Carneiro (Aug 18 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357403):
<p>have you tried running with the <code>-j</code> option?</p>

#### [ Johan Commelin (Aug 18 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357406):
<p>How would <code>-j</code> help?</p>

#### [ Johan Commelin (Aug 18 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357463):
<div class="codehilite"><pre><span></span><span class="o">[</span>jmc@atarrimbo mathlib<span class="o">]</span>$ <span class="nb">echo</span> <span class="k">$((</span><span class="m">7</span><span class="o">*</span><span class="m">16</span><span class="k">))</span>
<span class="m">112</span>
</pre></div>


<p>So there were 16 threads running almost full-time for 7 minutes.</p>

#### [ Johan Commelin (Aug 18 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357586):
<div class="codehilite"><pre><span></span><span class="o">[</span>jmc@atarrimbo mathlib<span class="o">]</span>$ cat /proc/cpuinfo <span class="p">|</span> grep name <span class="p">|</span> uniq
model name      : Intel<span class="o">(</span>R<span class="o">)</span> Xeon<span class="o">(</span>R<span class="o">)</span> CPU           E5540  @ <span class="m">2</span>.53GHz
</pre></div>


<p>I guess these are about 10 years old. All those modern i7's probably beat 4 of these hands-down. And I have only 16 of them. So if you have a quad-core...</p>

#### [ Johan Commelin (Aug 18 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357634):
<p>Mario, did you ever time a fresh build of mathlib on your hardware?</p>

#### [ Mario Carneiro (Aug 18 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132357706):
<p>I'll get back to you in an hour</p>

#### [ Mario Carneiro (Aug 18 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132360198):
<div class="codehilite"><pre><span></span>$ time lean --make

real    18m43.275s
user    0m0.000s
sys     0m0.015s
</pre></div>

#### [ Mario Carneiro (Aug 18 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132360342):
<p>I have 2 cores, 4 logical processors @ 2.90 GHz on my laptop</p>

#### [ Johan Commelin (Aug 18 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132360657):
<p>Ok cool. But why is <code>user</code> equal to <code>0</code>? What OS do you have?</p>

#### [ Mario Carneiro (Aug 18 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132361017):
<p>windows</p>

#### [ Mario Carneiro (Aug 18 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/132361020):
<p>running MSYS2</p>

#### [ Kenny Lau (Nov 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/136914467):
<p>I wish <code>lean --make</code> could have some debugging output, like at least how many files have been compiled</p>

#### [ Reid Barton (Nov 01 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/136919856):
<p>It actually does print a bunch of output, just apparently not on Windows? I was really confused when I tried Lean on a Windows machine for the first time and <code>lean --make</code> was silent</p>

#### [ Chris Hughes (Nov 01 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/136920069):
<p>It prints a bunch of output on my windows machine with the latest nightly. With April nightly it didn't</p>

#### [ Reid Barton (Nov 01 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/136920234):
<p>Interesting. I think I was using 3.4.1.</p>

#### [ Kenny Lau (Nov 01 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/136924729):
<p>I already <code>git pull</code>ed</p>

#### [ Mario Carneiro (Nov 01 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/136928284):
<p>I have to use <code>winpty lean --make</code> on msys2 to get output</p>

#### [ Mario Carneiro (Nov 01 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20--make/near/136928309):
<p>I think the terminal detection is broken</p>


{% endraw %}
