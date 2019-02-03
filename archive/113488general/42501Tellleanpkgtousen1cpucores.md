---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42501Tellleanpkgtousen1cpucores.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Tell leanpkg to use (n-1) cpu cores](https://leanprover-community.github.io/archive/113488general/42501Tellleanpkgtousen1cpucores.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Aug 07 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029086):
<p>Yesterday I rebuilt mathlib and it froze my desktop for &gt; 2hrs. I would like to tell leanpkg to use only 3 of my 4 cores. I'm on Linux. Should I use fancy <code>cgroups</code> for this, or is there some easy method?</p>

#### [ Johan Commelin (Aug 07 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029518):
<p>Hmm, maybe <code>nice leanpkg build</code> will do the job.</p>

#### [ Johan Commelin (Aug 07 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029520):
<p>Let's see if I stay responsive (-;</p>

#### [ Johan Commelin (Aug 07 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029818):
<p>Nope... on my laptop again...</p>

#### [ Johan Commelin (Aug 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029823):
<p>Stupid <code>nice</code></p>

#### [ Gabriel Ebner (Aug 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029867):
<p>You can use <code>lean -j3 --make</code>.  But I don't think that using all cores is the cause for your computer freezing.  It's much more likely to be memory usage.</p>

#### [ Johan Commelin (Aug 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029873):
<p>I've got 8 GB, shouldn't that be sufficient?</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029882):
<p>the answer is always no</p>

#### [ Johan Commelin (Aug 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029957):
<p>Whelp... it is indeed using &gt;7 GB</p>

#### [ Johan Commelin (Aug 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131029977):
<p>No, something is off. The lean process with niceness 10 is using only 10% of my memory.</p>

#### [ Johan Commelin (Aug 07 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030025):
<p>I've got to kill some other memory hog.</p>

#### [ Johan Commelin (Aug 07 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030051):
<p>So, do you guys have a strategy for keeping your system responsive during rebuilds? Or you only rebuild during lunch?</p>

#### [ Gabriel Ebner (Aug 07 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030201):
<p>What are you building?  I know that Lean eats memory for breakfast, but mathlib takes only 7 minutes and 1.5G of RAM here.</p>

#### [ Johan Commelin (Aug 07 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030367):
<p>I am trying to rebuild mathlib. The 1.5GB seems to be what my system is using as well.</p>

#### [ Johan Commelin (Aug 07 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030370):
<p>The 7 minutes... not really.</p>

#### [ Johan Commelin (Aug 07 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030379):
<p>It is still frozen to the core.</p>

#### [ Johan Commelin (Aug 07 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030557):
<p>Might it be a problem that I launched the rebuild from a feature branch?</p>

#### [ Johan Commelin (Aug 07 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030565):
<p>It only had changes in 1 file, compared to mathlib HEAD.</p>

#### [ Gabriel Ebner (Aug 07 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030633):
<p>No the small change should make it faster.  But maybe the change causes a <code>by simp</code> to time out?</p>

#### [ Gabriel Ebner (Aug 07 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030649):
<p>Wait, by frozen you just mean that lean is frozen, not your whole machine?  What is the last line that lean printed?</p>

#### [ Johan Commelin (Aug 07 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030659):
<p>No, the machine is frozen.</p>

#### [ Johan Commelin (Aug 07 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030669):
<p>I currently have a frozen <code>top</code> in front of me. I can't even issue a kill.</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030723):
<p>you are awfully chatty for someone with a bricked computer</p>

#### [ Johan Commelin (Aug 07 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030732):
<p>I'm on a laptop...</p>

#### [ Johan Commelin (Aug 07 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030738):
<p>People have &gt;3 devices with Zulip on it nowadays, don't they?</p>

#### [ Johan Commelin (Aug 07 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030757):
<p>Ok, so the last line that lean printed says that it is making stuff on Turing machines.</p>

#### [ Johan Commelin (Aug 07 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030761):
<p>That shouldn't get me stuck.</p>

#### [ Gabriel Ebner (Aug 07 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030813):
<p>Which branch are you on?</p>

#### [ Johan Commelin (Aug 07 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030832):
<p><code>map2</code></p>

#### [ Johan Commelin (Aug 07 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131030875):
<p>It is a feature branch that I'm trying to PR containing about 25 lines of changes in <code>linear_algebra/multivariate_polynomial.lean</code></p>

#### [ Gabriel Ebner (Aug 07 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131031229):
<p>Good news!  The branch builds!  (Not very helpful, I know.)<br>
Can you try <code>rm **/*.olean</code> and build again?</p>

#### [ Johan Commelin (Aug 07 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131031311):
<p>Nope, I can't... It is still frozen...</p>

#### [ Kevin Buzzard (Aug 07 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131031724):
<p>isn't it time to reboot?</p>

#### [ Johan Commelin (Aug 07 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131031732):
<p>It made a bit of progress! But it is still really slow.</p>

#### [ Johan Commelin (Aug 07 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131031778):
<p>I'm one of those guys that don't like to reboot a linux box. It feels like epic failure.</p>

#### [ Johan Commelin (Aug 07 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131033097):
<p>Yoochai! It survived. I managed to execute <code>killall code</code>, which closed 3 instances of VScode working on different Lean projects.</p>

#### [ Johan Commelin (Aug 07 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131033139):
<p>Now the compile is running smoothly again!</p>

#### [ Johan Commelin (Aug 07 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tell%20leanpkg%20to%20use%20%28n-1%29%20cpu%20cores/near/131033155):
<p>I guess I need more RAM</p>


{% endraw %}
