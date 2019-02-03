---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68222UpdatingMathlib.html
---

## Stream: [general](index.html)
### Topic: [Updating Mathlib](68222UpdatingMathlib.html)

---


{% raw %}
#### [ Morenikeji Neri (Aug 10 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131239650):
<p>I typed leanpkg upgrade on msys2 but my mathlib doesn't update. Help!</p>

#### [ Kevin Buzzard (Aug 10 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131242157):
<p>If you're trying it with the xena-UROP project, it's probably because I set it to track Mathlib 3.4.1, which is fixed. I thought it might make life easier if we were all singing from the same hymn-sheet, as it were.</p>

#### [ Chris Hughes (Aug 10 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131242193):
<p>Keji wants to use signatures of permutations, which has just been merged.</p>

#### [ Kevin Buzzard (Aug 10 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131242302):
<p>To be honest I'm not sure of a slick way of sorting this out. I am guessing Keji is using Lean 3.4.1. If he were to download the latest nightly, and then switch his msys2 so that when he typed <code>leanpkg</code> it used the latest nightly, then maybe this would fix it. I don't know if he can just edit <code>leanpkg.toml</code> to fix it.</p>

#### [ Kevin Buzzard (Aug 10 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131242320):
<p>I'm currently in an airport which is not really the most ideal place to be experimenting with this sort of thing.</p>

#### [ Mario Carneiro (Aug 10 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131242470):
<p>I think you can just specify your mathlib dependency to point to <code>"master"</code></p>

#### [ Mario Carneiro (Aug 10 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131242478):
<p>in <code>leanpkg.toml</code></p>

#### [ Kevin Buzzard (Aug 10 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131243629):
<p>Keji I just edited <code>leanpkg.toml</code> following Mario's suggestion; try pulling the latest version of the repo (with <code>git pull</code> perhaps, if you have <code>git</code> working in msys2) and then try <code>leanpkg upgrade</code> again.</p>
<p>I must be honest -- I hadn't expected this to happen. I was envisaging people on the Xena summer project just playing around with basic stuff and nothing we needed getting PR'ed to mathlib. Really I just wanted to avoid having to spend hours showing people how to upgrade mathlib :-) We now run the risk that some of us will write code which will not run for others, but I guess in the long run most people have got Lean running on their laptops and it's in their interest to learn how to upgrade mathlib.</p>
<p>One could envisage a one-click solution to all of this for Windows users. An "upgrade mathlib" button which just requires someone to type in their github credentials (or perhaps not even that). For mac users it's often easier because they have a terminal pre-installed, and when they install git it might well end up in a directory which is already in their path.</p>

#### [ Mario Carneiro (Aug 10 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131243695):
<p>you can't stop progress</p>

#### [ Kevin Buzzard (Aug 10 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131244304):
<p>You said this back when I was pleading for mathlib 3.4.1, and as is usually the case I am now coming round to your way of thinking. It's not going to be so easy with CoCalc I suspect, but with my course running on CoCalc I really do think I want a frozen mathlib [famous last words]</p>

#### [ Chris Hughes (Aug 10 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131244397):
<p>Keji tried updating it with <code>leanpkg upgrade</code>, but it just unupdated instead, and reverted to some old version.</p>

#### [ Kevin Buzzard (Aug 10 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131832343):
<p>Did you pull or otherwise edit leanpkg.toml?</p>

#### [ Sebastian Ullrich (Aug 10 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131835840):
<p>I don't think there is a way to tell leanpkg to track a different branch for a dependency yet</p>

#### [ Mario Carneiro (Aug 10 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131835920):
<p>isn't the dependency item a git repo and a branch or commit hash?</p>

#### [ Sebastian Ullrich (Aug 10 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131836124):
<p>Yes, but <code>leanpkg upgrade</code> will still <em>track</em> the branch associated with the executed Lean version</p>

#### [ Sebastian Ullrich (Aug 10 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131836139):
<p>I.e. if you're running 3.4.1, <code>leanpkg upgrade</code> will always update to the head of <code>lean-3.4.1</code></p>

#### [ Mario Carneiro (Aug 10 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131836251):
<p>so what does that branch info do?</p>

#### [ Sebastian Ullrich (Aug 10 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131836614):
<p>It points to the <em>currently used</em> commit, so it doesn't really make sense to store anything other than a commit hash or tag in that field. <code>leanpkg upgrade</code> ignores the field.</p>

#### [ Scott Morrison (Aug 11 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/131852105):
<p>Is it reasonable to be able to change this? I would really like to be able to track arbitrary branches of dependencies.</p>

#### [ Scott Morrison (Aug 25 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753539):
<p>I'm having trouble with the UROP repo.</p>

#### [ Scott Morrison (Aug 25 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753573):
<div class="codehilite"><pre><span></span>&gt; leanpkg upgrade
error: override toolchain &#39;master&#39; is not installed
info: caused by: the toolchain file at &#39;/Users/scott/scratch/xena-UROP-2018/leanpkg.toml&#39; specifies an uninstalled toolchain
</pre></div>

#### [ Scott Morrison (Aug 25 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753575):
<div class="codehilite"><pre><span></span>&gt; elan toolchain list
stable (default)
nightly-2018-04-06
nightly-2018-04-20
nightly-2018-06-21
khoek-klean-3.4.2
khoek-klean-3.4.3
3.4.0
3.4.1
</pre></div>

#### [ Scott Morrison (Aug 25 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753579):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>, do you know what's going on?</p>

#### [ Kevin Buzzard (Aug 25 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753588):
<p>I wouldn't trust our <code>leanpkg.toml</code> :-)</p>

#### [ Kevin Buzzard (Aug 25 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753632):
<p>The last time I pulled the project, it had at least one <code>&lt;&lt;&lt;&lt;&lt; .. ==== .. &gt;&gt;&gt;&gt;&gt;</code>in it :-)</p>

#### [ Kevin Buzzard (Aug 25 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753645):
<p><code>leanpkg upgrade</code> just worked for me</p>

#### [ Kevin Buzzard (Aug 25 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753650):
<div class="codehilite"><pre><span></span>WARNING: Lean version mismatch: installed version is nightly-2018-06-21, but package requires master
</pre></div>

#### [ Scott Morrison (Aug 25 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753694):
<p>I really wouldn't put <code>leanpkg upgrade</code> as part of your install instructions: <a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018">https://github.com/ImperialCollegeLondon/xena-UROP-2018</a></p>

#### [ Scott Morrison (Aug 25 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753696):
<p><code>leanpkg configure</code> is what you want</p>

#### [ Scott Morrison (Aug 25 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753704):
<p>(that doesn't touch your leanpkg.toml file, making it more likely it will survive multiple users)</p>

#### [ Kevin Buzzard (Aug 25 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753706):
<p>Oh thanks. This was an attempt to get users to install mathlib in <code>_target</code></p>

#### [ Scott Morrison (Aug 25 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753708):
<p>btw --- we need to make sure you update/replace your blog post on installing on Windows, to tell people to use <code>elan</code>.</p>

#### [ Scott Morrison (Aug 25 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753719):
<p>At Dagstuhl, Neil Strickland made a valiant effort to have someone show him how to install and prove the infinitude of primes in as many theorem provers as he could.</p>

#### [ Kevin Buzzard (Aug 25 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753724):
<p>Neil just asked me to give a colloquium in Sheffield</p>

#### [ Scott Morrison (Aug 25 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753725):
<p>I really struggled helping him install Lean on his (windows) laptop.</p>

#### [ Kevin Buzzard (Aug 25 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753788):
<p>You need a terminal and git, and you need to understand how your chosen terminal's path can be configured to globally remember where git and lean are installed</p>

#### [ Keeley Hoek (Aug 25 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753798):
<p>I don't think 'master' could ever work with the latest version of elan<br>
it has to be 'stable', 'nightly-xxx', or something on this list <a href="https://github.com/leanprover/lean/releases" target="_blank" title="https://github.com/leanprover/lean/releases">https://github.com/leanprover/lean/releases</a> with the prefix "v" removed</p>

#### [ Kevin Buzzard (Aug 25 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753800):
<p>Aah there's the problem then. I don't use <code>elan</code></p>

#### [ Kevin Buzzard (Aug 25 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753842):
<p>Thanks.</p>

#### [ Scott Morrison (Aug 25 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753915):
<p>Yeah --- we were definitely having problems with paths, and it wasn't helping that Neil had already tried and failed, so had left things affecting the paths.</p>

#### [ Scott Morrison (Aug 25 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753920):
<p>It also didn't help that his system had 3 different notions of "path", between windows, cygwin, and msys2.</p>

#### [ Scott Morrison (Aug 25 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753924):
<p>(He wanted to use cygwin, because that was the windows shell he was familiar with)</p>

#### [ Scott Morrison (Aug 25 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753969):
<p><code>elan</code> has a really big advantage here: it tries to take care of the paths for you, and I trust <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> to play with paths better than I trust users. :-)</p>

#### [ Johan Commelin (Aug 25 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132753982):
<p>Would Docker be an option for such showcasing purposes?</p>

#### [ Johan Commelin (Aug 25 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132754022):
<p>I hear that Docker also runs on Windows.</p>

#### [ Kevin Buzzard (Aug 25 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132754025):
<p>Here's a proposal for Windows users only: we make a "one size fits all" download. One zip file, that you put in <code>C:/Users/Neil</code> and then unpack, giving you a directory <code>C:/Users/Neil/leanstuff/</code>.</p>

#### [ Kevin Buzzard (Aug 25 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132754042):
<p>You then tell users to install VS Code, and then "open folder" the folder <code>C:/Users/Neil/leanstuff/sample_project/</code>, and to tell VS Code where the Lean binary is, which is <code>C:/Users/Neil/leanstuff/lean-3.4.2/bin/lean.exe</code></p>

#### [ Kevin Buzzard (Aug 25 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132754045):
<p>and then everything just works.</p>

#### [ Kevin Buzzard (Aug 25 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132754083):
<p>No git, no command line, no nothing</p>

#### [ Johan Commelin (Aug 25 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132754090):
<p>Couldn't you even package VS code, with the right path setting, into that zipfile?</p>

#### [ Kevin Buzzard (Aug 25 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132754092):
<p>and that's because the sample project directory has got a correct leanpkg.toml, and <code>_target/deps/mathlib</code> exists and has all the <code>.olean</code> files and everything</p>

#### [ Kevin Buzzard (Aug 25 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132754100):
<p>I have no idea about how Windows works and whether you can package a complicated thing like VS Code in a zip file</p>

#### [ Reid Barton (Aug 25 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132755190):
<p>I also don't know how Windows works or how Docker on Windows works but it sounds like something worth looking into.<br>
The examples I've managed to find involve VS Code running inside Docker on a Linux virtual system, and connecting to an X window server running under Windows. That sounds ... workable, but a little awkward (you still have at least two pieces to download).</p>

#### [ Reid Barton (Aug 25 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132755208):
<p>Some links:<br>
<a href="https://hub.docker.com/r/joengenduvel/docker-vscode/" target="_blank" title="https://hub.docker.com/r/joengenduvel/docker-vscode/">https://hub.docker.com/r/joengenduvel/docker-vscode/</a><br>
<a href="http://blog.ctaggart.com/2016/05/visual-studio-code-served-from-docker.html" target="_blank" title="http://blog.ctaggart.com/2016/05/visual-studio-code-served-from-docker.html">http://blog.ctaggart.com/2016/05/visual-studio-code-served-from-docker.html</a><br>
<a href="https://www.aaron-powell.com/posts/2017-09-21-vscode-linux-docker-windows/" target="_blank" title="https://www.aaron-powell.com/posts/2017-09-21-vscode-linux-docker-windows/">https://www.aaron-powell.com/posts/2017-09-21-vscode-linux-docker-windows/</a></p>

#### [ Reid Barton (Aug 25 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132755429):
<p>There's probably no advantage to putting VS Code in the Docker container, and requiring the end user to download an X server and the Lean/mathlib/VS Code container, over just using the native VS Code, and requiring the end user to download VS Code and the Lean/mathlib container. And there are almost certainly advantages to native VS Code over one running over X11.</p>

#### [ Reid Barton (Aug 25 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132755441):
<p>I do sort of like the idea of Windows users having Lean/mathlib/git/etc. running inside a Docker container, though, since it reduces the support surface area</p>

#### [ Reid Barton (Aug 25 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Updating%20Mathlib/near/132755483):
<p>It might become a very large download though, not sure.</p>


{% endraw %}
