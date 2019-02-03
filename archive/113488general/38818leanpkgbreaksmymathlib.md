---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/38818leanpkgbreaksmymathlib.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [leanpkg breaks my mathlib](https://leanprover-community.github.io/archive/113488general/38818leanpkgbreaksmymathlib.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jul 10 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401172):
<div class="codehilite"><pre><span></span>buzzard@bob:~/Lean/lean-projects/xena-UROP-2018$ more leanpkg.toml
[package]
name = &quot;xena-UROP-2018&quot;
version = &quot;0.1&quot;
lean_version = &quot;3.4.1&quot;
path = &quot;src&quot;

[dependencies]
mathlib = {git = &quot;https://github.com/leanprover/mathlib&quot;, rev = &quot;c8ad5cfd793153bff38c49c54940f04d86cb7616&quot;}
buzzard@bob:~/Lean/lean-projects/xena-UROP-2018$ # commit number is mathlib HEAD
buzzard@bob:~/Lean/lean-projects/xena-UROP-2018$ leanpkg upgrade
mathlib: trying to update _target/deps/mathlib to revision c8ad5cfd793153bff38c49c54940f04d86cb7616
&gt; git checkout --detach c8ad5cfd793153bff38c49c54940f04d86cb7616    # in directory _target/deps/mathlib
Previous HEAD position was a30b7c7... feat(data/string): fix string_lt, add repr for multiset, pnat
HEAD is now at c8ad5cf... fix(computability/turing_machine): fix import
configuring xena-UROP-2018 0.1
mathlib: trying to update _target/deps/mathlib to revision a30b7c773db17cf7d1b551ba0f24645079296628
&gt; git checkout --detach a30b7c773db17cf7d1b551ba0f24645079296628    # in directory _target/deps/mathlib
Previous HEAD position was c8ad5cf... fix(computability/turing_machine): fix import
HEAD is now at a30b7c7... feat(data/string): fix string_lt, add repr for multiset, pnat
buzzard@bob:~/Lean/lean-projects/xena-UROP-2018$ more leanpkg.toml
[package]
name = &quot;xena-UROP-2018&quot;
version = &quot;0.1&quot;
lean_version = &quot;3.4.1&quot;
path = &quot;src&quot;

[dependencies]
mathlib = {git = &quot;https://github.com/leanprover/mathlib&quot;, rev = &quot;a30b7c773db17cf7d1b551ba0f24645079296628&quot;}
buzzard@bob:~/Lean/lean-projects/xena-UROP-2018$ # mathlib now a commit from 19 days ago which doesn&#39;t compile
buzzard@bob:~/Lean/lean-projects/xena-UROP-2018$
</pre></div>

#### [ Kevin Buzzard (Jul 10 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401237):
<p>My <code>leanpkg.toml</code> for a Xena project repo on GH seems to want to use commit <code>a30b7c773db17cf7d1b551ba0f24645079296628</code> of mathlib, which does not compile. I can edit <code>leanpkg.toml</code> manually and point it at the mathlib revision I want, but <code>leanpkg upgrade</code> then rolls it back. What am I doing wrong?</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401302):
<div class="codehilite"><pre><span></span>$ lean --version
Lean (version 3.4.1, commit 17fe3decaf8a, Release)
</pre></div>

#### [ Chris Hughes (Jul 10 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401496):
<p>I tried cloning and typing <code>leanpkg upgrade</code> and <code>leanpkg</code> changed the toml to the latest update.</p>

#### [ Chris Hughes (Jul 10 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401543):
<p>I've pushed, so it might work now</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401632):
<p>This does not fix it for me.</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401653):
<p>I just cloned and ran <code>leanpkg upgrade</code></p>

#### [ Johan Commelin (Jul 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401666):
<p>"Have you tried turning <code>bob</code> off and on again"</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401669):
<p>are you serious?</p>

#### [ Chris Hughes (Jul 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401710):
<p>Who's bob?</p>

#### [ Johan Commelin (Jul 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401712):
<p>His computer</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401714):
<p>I saw this behaviour on Luca's mac yesterday</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401718):
<p>and I'm now experiencing it myself on linux</p>

#### [ Johan Commelin (Jul 10 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401726):
<p>I guess Chris is running Windows...?</p>

#### [ Chris Hughes (Jul 10 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401733):
<p>Correct.</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401734):
<p>I cloned and ran <code>leanpkg upgrade</code> and I'm back to <code>a30b7c7</code></p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401737):
<p>which doesn't compile</p>

#### [ Johan Commelin (Jul 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401822):
<p>Hmm, and you both have the same version of Lean, hence the same leanpkg, right?</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401830):
<p>I can't guarantee that we're using the same version of Lean.</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401837):
<p>I am using 3.4.1 stable and I think Chris might be using the 20/4 nightly</p>

#### [ Chris Hughes (Jul 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401844):
<p>I'm using <code>Lean (version 3.4.1, nightly-2018-04-20, commit f59c2f0ef59f, Release)</code></p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401846):
<p>they differ by about one commit</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129401889):
<div class="codehilite"><pre><span></span>$ lean --version
Lean (version 3.4.1, commit 17fe3decaf8a, Release)
</pre></div>

#### [ Kevin Buzzard (Jul 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402002):
<p>Aah!</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402013):
<p>Mathlib branch 3.4.1 which Mario didn't want to make -- he has clearly decided to get his own back by pointing it at the <code>a30b7c7</code> commit and leaving it there!</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402065):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> help! Can you change the <code>3.4.1</code> branch of mathlib to something which compiles?</p>

#### [ Chris Hughes (Jul 10 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402085):
<p>So the issue is that you're version wants to use the <code>3.4.1</code> branch and my version wants to use master?</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402103):
<p>Maybe.</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402149):
<p>The underlying issue is that I want everyone (except people like you who know what they're doing) to be using the exact same version of Lean and mathlib.</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402155):
<p>Because that is the sane way to proceed, in my opinion.</p>

#### [ Chris Hughes (Jul 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402157):
<p>Why are there two identical branches anyway?</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402173):
<p>Same answer.</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402186):
<p>I want to tell my users "download Lean 3.4.1 and mathlib 3.4.1" and I want the consequence of this to be that everyone downloads the same thing</p>

#### [ Kevin Buzzard (Jul 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402209):
<p>Mario says "mathlib does not work like this, I will not release a 3.4.1"</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402271):
<p>The compromise was that he released a 3.4.1 branch and used to keep it up to date with mathlib HEAD but maybe he forgot to do this recently and unfortunately we've settled on a version of mathlib which doesn't compile.</p>

#### [ Chris Hughes (Jul 10 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402481):
<p>That's not really necessary until master uses <code>3.4.2</code> is it?</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402531):
<p>Actually I left <code>3.4.1</code> branch there because Leo pushed a commit on lean repo after that, so technically <code>master</code> is back on nightlies</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402535):
<p>Chris -- currently when my users say "what version of Lean should I download"? I say "3.4.1 stable, here's the link" and when they say "what version of mathlib should I download" I say "don't worry about mathlib, let leanpkg do the magic for you".</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402577):
<p>and currently the magic it does is that it downloads a broken version</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402578):
<p>It should be a working version though</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402584):
<p>It has a red X on the list of commits and I just failed to compile it.</p>

#### [ Kenny Lau (Jul 10 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402591):
<p>just pick a working version</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402604):
<p>Which version of Lean should I be using with it? 3.4.1 stable as advertised here: <a href="https://github.com/leanprover/lean/releases/tag/v3.4.1" target="_blank" title="https://github.com/leanprover/lean/releases/tag/v3.4.1">https://github.com/leanprover/lean/releases/tag/v3.4.1</a> ?</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402609):
<p>Kenny it's not as simple as that. I can get it working myself, it's my users that are having problems.</p>

#### [ Kenny Lau (Jul 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402616):
<p>I see</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402620):
<p>Currently if you follow the readme here</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402622):
<p><a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/README.md" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/README.md">https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/README.md</a></p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402627):
<p>then compilation of mathlib fails</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402678):
<p>Oh, I see what you mean</p>

#### [ Mario Carneiro (Jul 10 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402682):
<p>fixed</p>

#### [ Kevin Buzzard (Jul 10 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20breaks%20my%20mathlib/near/129402686):
<p>Many thanks for the prompt work!</p>


{% endraw %}
