---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35331leanpkg.html
---

## Stream: [general](index.html)
### Topic: [leanpkg](35331leanpkg.html)

---


{% raw %}
#### [ Simon Hudon (Feb 27 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123021774):
<p>It is possible to specify git branches in <code>leanpkg</code>?</p>

#### [ Mario Carneiro (Feb 27 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123022299):
<div class="codehilite"><pre><span></span>[package]
name = &quot;my_awesome_pkg&quot;
version = &quot;0.1&quot;         # no semantic significance currently
lean_version = &quot;3.3.0&quot;  # optional, prints a warning on mismatch with Lean executable
path = &quot;src&quot;            # hard-coded, will be removed in the future
timeout = 100           # optional, passed to `lean` as `-T` parameter

[dependencies]
# local dependency
demopkg = { path = &quot;relative/path/to/demopkg&quot; }
# git dependency
mathlib =
  { git = &quot;https://github.com/leanprover/mathlib&quot;,
    rev = &quot;62f7883d937861b618ae8bd645ee16ec137dd0bd&quot; }
</pre></div>


<p>You should be able to specify a branch using the <code>rev</code> field</p>

#### [ Simon Hudon (Feb 27 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123022372):
<p>When doing that, I keep getting something saying that that revision is not a part of the tree. It's odd</p>

#### [ Simon Hudon (Feb 27 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123028434):
<p>update: I managed to make it work. It might not be a leanpkg issue but I'm not sure. It seemed to be having a hard time cloning repositories for some reason. I wonder if it has anything to do that I wasn't pointing at the usual <code>mathlib</code> repo</p>

#### [ Sebastian Ullrich (Feb 27 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123033857):
<p>Can you reproduce it if you copy the toml to a fresh directory?</p>

#### [ Simon Hudon (Feb 27 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123033928):
<p>Actually, if you clone my repo, the problem should occur again:</p>
<div class="codehilite"><pre><span></span>git clone https://github.com/cipher1024/lean-pipes
</pre></div>

#### [ Simon Hudon (Feb 27 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123033977):
<p>Sorry, you asked for a naked toml file. Let's see</p>

#### [ Simon Hudon (Feb 27 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123034036):
<p>So, yes the problem occurs even if the toml file is left on its own</p>

#### [ Sebastian Ullrich (Feb 27 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123034038):
<p>Okay, I'll try your repo</p>

#### [ Sebastian Ullrich (Feb 28 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123086767):
<p>I don't see your leanpkg.toml referencing a branch</p>

#### [ Simon Hudon (Feb 28 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/123102397):
<p>Here's the contents of <code>leanpkg.toml</code>:</p>
<div class="codehilite"><pre><span></span>[package]
name = &quot;pipes&quot;
version = &quot;0.1&quot;
lean_version = &quot;master&quot;
path = &quot;src&quot;

[dependencies]
mathlib = {git = &quot;https://github.com/cipher1024/mathlib&quot;, rev = &quot;ce8da6ab07a68dca1743bd7d8f9768157d644736&quot;}
</pre></div>


<p>It is on my fork of <code>mathlib</code> and that commit is the head of my <code>coinductive-types</code> branch</p>

#### [ Reid Barton (Sep 22 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134435061):
<p>This is a really basic question, but what's the right way to start and maintain a new package that depends on mathlib?<br>
I see mathlib's <code>leanpkg.toml</code> specifies <code>lean_version = "3.4.1"</code>, so I guess I should use Lean 3.4.1.<br>
So let's say I run <code>elan run --install 3.4.1 leanpkg new my_project</code>, as recommended by <a href="https://github.com/leanprover/mathlib/blob/master/docs/elan.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/elan.md">https://github.com/leanprover/mathlib/blob/master/docs/elan.md</a>. Now I get a new project whose <code>leanpkg.toml</code> also specifies <code>lean_version = "3.4.1"</code>.<br>
Continuing to follow those directions, I run <code>leanpkg add leanprover/mathlib</code>. But now I end up with the <code>lean-3.4.1</code> branch of mathlib, which hasn't been updated since June 20. I wanted the latest version. And <code>leanpkg upgrade</code> makes no difference.</p>

#### [ Reid Barton (Sep 22 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134435107):
<p>Is this behavior intentional? At best, it's confusing if following the instructions in that elan.md file doesn't give you the latest version of mathlib, I think.</p>

#### [ Reid Barton (Sep 22 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134435173):
<p>Even though I should supposedly know how all of this works (e.g., I know there is a <code>lean-3.4.1</code> branch of mathlib and leanpkg will select it), I still get caught by surprise since starting a new project is so infrequent--I just made a new project and built mathlib in it and then a half hour later discovered I had the June 20 version which didn't have the new features I wanted to use.</p>

#### [ Kevin Buzzard (Sep 22 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134435346):
<p>I once thought that editing the toml file and changing 3.4.1 to "master" would fix this, but maybe the issue is that you are using 3.4.1's <code>leanpkg</code>?</p>

#### [ Reid Barton (Sep 22 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134435466):
<p>It probably would fix it, especially since I am using elan (although I'm not sure whether it is the version of leanpkg that matters, or what you write in the <code>lean_version</code> field of the toml file).<br>
The elan.md instructions (I'm talking about "Scenario 1: Start a new package") suggest that you might see <code>nightly-2018-04-06</code> as the Lean version, and I found that <code>elan run --install nightly-2018-04-06 leanpkg new my_playground</code> does give you master mathlib, maybe because there is no branch corresponding to <code>nightly-2018-04-06</code>.<br>
But it seems strange that the way to get mathlib master is to tell elan/leanpkg to use any other Lean version than the one actually used by mathlib...</p>

#### [ Reid Barton (Sep 22 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134435506):
<p>Presumably when those instructions were written, mathlib really did specify a version other than 3.4.1 and so the instructions worked</p>

#### [ Reid Barton (Sep 22 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134435557):
<p>By the way I should say explicitly that I'm assuming the current behavior is incorrect and I'm not supposed to get what appears to me to be this random version from June 20, but maybe others (like perhaps you Kevin) think it's working as intended because you want a fixed version for all your students.</p>

#### [ Kevin Buzzard (Sep 22 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134436089):
<p>That is all over now. I wanted a fixed version for my summer students just so I could see the advantages and the disadvantages. One of the advantages is that they don't ever have to update mathlib. What happened in practice was that people generally wanted more recent mathlib stuff and they learnt how to upgrade anyway, because sufficiently many of them knew how to use git because they were on a joint maths/computer science degree, so it worked out fine in the end and everyone was using different mathlibs anyway, and there didn't seem to be a problem.</p>

#### [ Reid Barton (Sep 22 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134436346):
<p>Okay, great. In that case I'm going to push for making it impossible to get this random old version of mathlib without asking for it, since I think that results in a potentially confusing experience for new users (e.g., one hears "mathlib has X" but then makes a project to try it out and X is missing).</p>

#### [ Reid Barton (Sep 22 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134436566):
<p>Moved discussion to github: <a href="https://github.com/leanprover/lean/issues/365" target="_blank" title="https://github.com/leanprover/lean/issues/365">#365</a></p>

#### [ Reid Barton (Sep 22 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134436567):
<p>Dang that's not a link to a mathlib issue.</p>

#### [ Reid Barton (Sep 22 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134436607):
<p><a href="https://github.com/leanprover/mathlib/issues/365" target="_blank" title="https://github.com/leanprover/mathlib/issues/365">https://github.com/leanprover/mathlib/issues/365</a></p>

#### [ Scott Morrison (Sep 23 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134456778):
<p>I think this is a really good idea. I've been confused by this, too.</p>

#### [ Mario Carneiro (Sep 23 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457081):
<p>I guess leanpkg and elan have been designed for reproducible builds, which is the popular option these days. Unfortunately the usual thing new lean/mathlib users want is master + master, which goes against this idea, and so the tools fight them on this.</p>

#### [ Mario Carneiro (Sep 23 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457122):
<p>I guess you could say they are being "too smart for their own good"</p>

#### [ Simon Hudon (Sep 23 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457124):
<p>Is this something a switch could fix?</p>

#### [ Mario Carneiro (Sep 23 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457132):
<p><code>elan</code> in particular should strive for setting up users with the latest everything unless the user specifically asks for an old version</p>

#### [ Reid Barton (Sep 23 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457135):
<p>Well you still get reproducible builds because the mathlib commit hash is in the leanpkg.toml file. It's just a matter of where you want to start a new project.</p>

#### [ Mario Carneiro (Sep 23 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457182):
<p>Does <code>elan</code> know that mathlib exists? Or does the default thing just get you lean on its own</p>

#### [ Reid Barton (Sep 23 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457187):
<p>I'm definitely happy that I can still build my lean-homotopy-theory project against the version of mathlib specified in the file, otherwise I would have no idea how any of the proofs that broke when building against master were supposed to work :)</p>

#### [ Simon Hudon (Sep 23 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457228):
<p>I think elan only gets you Lean and the lean version in your toml file selects the tag of mathlib</p>

#### [ Reid Barton (Sep 23 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457230):
<p>elan doesn't know about mathlib. The process is <code>elan run --install 3.4.1 leanpkg new myproject</code>, <code>cd myproject</code>, <code>leanpkg add leanprover/mathlib</code>.</p>

#### [ Reid Barton (Sep 23 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457237):
<p>Then <code>leanpkg</code> picks the 3.4.1 branch of mathlib because that is what is specified in the <code>leanpkg.toml</code> file that elan wrote. I think</p>

#### [ Reid Barton (Sep 23 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457238):
<p>Sorry--that leanpkg wrote</p>

#### [ Mario Carneiro (Sep 23 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457240):
<p>Right, and this is backwards since it says "get me the version of mathlib compatible with 3.4.1" rather than "get me the version of lean compatible with mathlib master"</p>

#### [ Reid Barton (Sep 23 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457298):
<p>Yes, that is definitely a bit weird.</p>

#### [ Mario Carneiro (Sep 23 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457304):
<p>I think you should be able to ask elan to target a particular version/branch of any lean project, not just lean itself</p>

#### [ Mario Carneiro (Sep 23 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457305):
<p>and then it derives the lean version from the toml file of that project</p>

#### [ Reid Barton (Sep 23 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457403):
<p>I think the current situation is a consequence of the fact that the "package manager" leanpkg is shipped/versioned with lean itself</p>

#### [ Reid Barton (Sep 23 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457445):
<p>that is, only leanpkg (not elan) knows about packages at all, but in order to get (any) leanpkg, you first must choose a lean version</p>

#### [ Reid Barton (Sep 23 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134457902):
<p>I wonder how crazy it would be to just replace leanpkg with crate or some other language's tool</p>

#### [ Mario Carneiro (Sep 23 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458086):
<p>Note that <code>elan</code> <em>is</em> some other language's tool (it is forked from Rust's <code>cargo</code>)</p>

#### [ Sebastian Ullrich (Sep 23 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458484):
<blockquote>
<p>I think you should be able to ask elan to target a particular version/branch of any lean project, not just lean itself<br>
and then it derives the lean version from the toml file of that project</p>
</blockquote>
<p>But that's exactly what it's doing :) . Check out a Lean project at some commit and elan sets up the right Lean version for you.<br>
What you're asking for is for elan not to set up some existing project, but a _new_ project based on its intended _dependencies_, no? What I could imagine is a command <code>elan new</code> that works like <code>leanpkg new</code>, but also takes a list of initial dependencies and selects the new package's Lean version based on that</p>

#### [ Mario Carneiro (Sep 23 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458530):
<p>That sounds good to me. Is it currently possible to write stuff in a file to get the equivalent of <code>elan new</code> using <code>elan</code>?</p>

#### [ Sebastian Ullrich (Sep 23 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458543):
<p>Though that seems like much more work than documenting "active mathlib development is happening for Lean version $VERSION, so use <code>elan +$VERSION leanpkg new</code> if you want to use it"</p>

#### [ Mario Carneiro (Sep 23 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458597):
<p>It also sounds like it might be possible for me to set up a "template" project that depends on mathlib but otherwise contains very little, as a target for users to download and make elan understand</p>

#### [ Mario Carneiro (Sep 23 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458609):
<p>Is it possible for a project like this to target the master branch of mathlib?</p>

#### [ Mario Carneiro (Sep 23 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458660):
<p>What does <code>elan +$VERSION leanpkg new</code> mean here? Do you mean <code>$VERSION = 3.4.1</code>?</p>

#### [ Mario Carneiro (Sep 23 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458663):
<p>the really important part is being able to tell elan "get mathlib master" without having to specify a commit</p>

#### [ Mario Carneiro (Sep 23 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458711):
<p>I'm fine with telling people to get 3.4.1, since it's basically going to stay that way until lean 4 and then everything will be different anyway, but mathlib won't stay still and elan has to be able to adapt to that</p>

#### [ Sebastian Ullrich (Sep 23 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458754):
<p>Okay, that <code>leanpkg upgrade</code> doesn't allow you to customize which branch it uses is a related but separate issue (and specific to leanpkg, not elan)</p>

#### [ Mario Carneiro (Sep 23 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458814):
<p>So what is the current recommendation? Do users need to go into <code>_target/deps/mathlib</code> and checkout master?</p>

#### [ Sebastian Ullrich (Sep 23 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458817):
<p>I guess we can agree that leanpkg using a separate branch per Lean version was a good idea but didn't work out in practice, since nobody wants to maintain code for multiple Lean versions. We could definitely change that in Lean 4, ie. when development on leanpkg continues</p>

#### [ Mario Carneiro (Sep 23 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458860):
<p>The problem isn't maintaining multiple lean versions, it's not allowing other kinds of branches</p>

#### [ Mario Carneiro (Sep 23 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458870):
<p>in particular master branches, which are going to be, ehm, rather common</p>

#### [ Sebastian Ullrich (Sep 23 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458974):
<p>If you use the master branch for development against a Lean version that is not master, it does look like you don't agree with leanpkg at all how branches should be handled</p>

#### [ Sebastian Ullrich (Sep 23 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134458994):
<p>Given the current leanpkg, the only real solution would be to rename the master branch to <code>lean-3.4.1</code>. If we don't want that, we'll have to change leanpkg... at some point</p>

#### [ Reid Barton (Sep 23 2018 at 03:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459118):
<p>Is deleting the <code>lean-3.4.1</code> branch not a solution, or merely not a "real solution"?</p>

#### [ Sebastian Ullrich (Sep 23 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459128):
<p>Then <code>leanpkg upgrade</code> will simply do nothing except complain, afaik</p>

#### [ Reid Barton (Sep 23 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459129):
<p>When Lean 4 arrives we will be able to modify leanpkg at the same time, so is it reasonable to assume for now that there is only one version of Lean in existence?</p>

#### [ Reid Barton (Sep 23 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459132):
<p>Hmm, let me try.</p>

#### [ Sebastian Ullrich (Sep 23 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459171):
<p><a href="https://github.com/leanprover/lean/blob/b13ac127fd83f3724d2f096b1fb85dc6b15e3746/leanpkg/leanpkg/git.lean#L10-L14" target="_blank" title="https://github.com/leanprover/lean/blob/b13ac127fd83f3724d2f096b1fb85dc6b15e3746/leanpkg/leanpkg/git.lean#L10-L14">https://github.com/leanprover/lean/blob/b13ac127fd83f3724d2f096b1fb85dc6b15e3746/leanpkg/leanpkg/git.lean#L10-L14</a></p>

#### [ Reid Barton (Sep 23 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459228):
<p>I have a toy project here using <code>nightly-2018-04-06</code> and I changed the mathlib commit to an older version and ran leanpkg configure and verified that it checked out the old version. Then I ran <code>leanpkg upgrade</code> and it successfully upgraded to mathlib master:</p>
<div class="codehilite"><pre><span></span>rwbarton@bridge:~/lean/my_playground2$ leanpkg upgrade
mathlib: trying to update _target/deps/mathlib to revision f53c776c2e09eff5358c5de6902e402c641a1673
&gt; git checkout --detach f53c776c2e09eff5358c5de6902e402c641a1673    # in directory _target/deps/mathlib
HEAD is now at f53c776... feat(analysis/topology): pi-spaces: topolopgy generation, prove second countability
configuring my_playground2 0.1
mathlib: trying to update _target/deps/mathlib to revision ca7f118058342a2f077e836e643d26e0ad1f3ca6
&gt; git checkout --detach ca7f118058342a2f077e836e643d26e0ad1f3ca6    # in directory _target/deps/mathlib
Previous HEAD position was f53c776... feat(analysis/topology): pi-spaces: topolopgy generation, prove second countability
HEAD is now at ca7f118... fix(docs/tactics.md): missing backquote, formatting
rwbarton@bridge:~/lean/my_playground2$ echo $?
0
rwbarton@bridge:~/lean/my_playground2$ cat leanpkg.toml
[package]
name = &quot;my_playground2&quot;
version = &quot;0.1&quot;
lean_version = &quot;nightly-2018-04-06&quot;
path = &quot;src&quot;

[dependencies]
mathlib = {git = &quot;https://github.com/leanprover/mathlib&quot;, rev = &quot;ca7f118058342a2f077e836e643d26e0ad1f3ca6&quot;}
</pre></div>

#### [ Reid Barton (Sep 23 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459230):
<p>Is that something special about using nightly lean vs a stable version number?</p>

#### [ Sebastian Ullrich (Sep 23 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459253):
<p>Yes, see the link above</p>

#### [ Reid Barton (Sep 23 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459273):
<p>Ah...</p>

#### [ Sebastian Ullrich (Sep 23 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459287):
<blockquote>
<p>When Lean 4 arrives we will be able to modify leanpkg at the same time, so is it reasonable to assume for now that there is only one version of Lean in existence?</p>
</blockquote>
<p>I suppose that is a reasonable assumption right now. Even if we don't change the leanpkg semantics, it will just work if Lean 4 porting efforts happen on the mathlib master branch and development for Lean 3 on the <code>lean-3.4.1</code> branch</p>

#### [ Mario Carneiro (Sep 23 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459337):
<blockquote>
<p>If you use the master branch for development against a Lean version that is not master, it does look like you don't agree with leanpkg at all how branches should be handled</p>
</blockquote>
<p>I think the master branch of lean is basically 3.4.1, so if this is what is needed then I'm okay with it. How do I sign up?</p>

#### [ Reid Barton (Sep 23 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134459715):
<p>So before I incorrectly "realized" that we could just delete the lean-3.4.1 branch, options I was considering were:</p>
<ul>
<li>Development happens on the lean-3.4.1 branch, not master. (You can set lean-3.4.1 as the "default" branch in the github UI to help with this--I did it for <a href="https://github.com/rwbarton/lean-homotopy-theory" target="_blank" title="https://github.com/rwbarton/lean-homotopy-theory">https://github.com/rwbarton/lean-homotopy-theory</a>. But I don't know whether changing this for an existing project like mathlib with many forks would have some ramifications.)</li>
<li>There are some obscure git features like <code>git symbolic-ref</code> which might allow us to make lean-3.4.1 an alias to master, but it's not clear whether they would really work for us or whether they can be configured through github.</li>
<li>We could try to keep lean-3.4.1 up to date with master by some technical or semi-technical means (like a pre-push hook for mathlib committers--there are few enough of them that it should be feasible).</li>
</ul>

#### [ Kevin Buzzard (Sep 23 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134469763):
<p>Why don't people use the latest lean nightly? It's 3.4.1 with some broken stuff fixed.</p>

#### [ Kevin Buzzard (Sep 23 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134469804):
<p>6th April, 20th April -- why? I use the June version</p>

#### [ Bryan Gin-ge Chen (Sep 23 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134469964):
<p>Actually, there's an August version out now...</p>

#### [ Mario Carneiro (Sep 23 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134470067):
<p>The fixes aren't so important to me. More important is whether switching back to nightlies will improve or exacerbate the <code>leanpkg</code> situation</p>

#### [ Mario Carneiro (Sep 23 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134470078):
<p>Is Kevin's blog post still the best option for installing lean + mathlib on windows?</p>

#### [ Scott Morrison (Sep 23 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134472306):
<p>As far as I can tell. We really need something like elan for windows.</p>

#### [ Olli (Sep 23 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134472811):
<p>elan works fine on Windows</p>

#### [ Olli (Sep 23 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134472866):
<p>the Windows specific issue I and a few others seem to run into is leanpkg failing with "failed to start child process", for which I have found no solution for</p>

#### [ Bryan Gin-ge Chen (Sep 23 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134473291):
<p>For which subcommands and under what precise circumstances does leanpkg fail on your machine? Does it output anything else?</p>

#### [ Olli (Sep 23 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474398):
<p>any command that has to do with creating a project, adding dependencies etc. here is an example, where I have modified the leanpkg script (i.e. leanpkg.bat on Windows) to ignore the <code>@ECHO OFF</code> directive so that the commands getting ran are printed:</p>
<div class="codehilite"><pre><span></span>PS C:\Users\Olli\Dev\Lean&gt; leanpkg new playground

C:\Users\Olli\Dev\Lean&gt;SET LEANDIR=C:\Users\Olli\.elan\toolchains\stable\bin\../

C:\Users\Olli\Dev\Lean&gt;SET LIBDIR=C:\Users\Olli\.elan\toolchains\stable\bin\../\lib\lean

C:\Users\Olli\Dev\Lean&gt;IF NOT EXIST C:\Users\Olli\.elan\toolchains\stable\bin\../\lib\lean SET LIBDIR=C:\Users\Olli\.ela
n\toolchains\stable\bin\../

C:\Users\Olli\Dev\Lean&gt;SET LEAN_PATH=C:\Users\Olli\.elan\toolchains\stable\bin\../\lib\lean\library;C:\Users\Olli\.elan\toolchains\stable\bin\../\lib\lean\leanpkg

C:\Users\Olli\Dev\Lean&gt;SET PATH=C:\Users\Olli\.elan\toolchains\stable\bin\../\bin;C:\Users\Olli\.elan\bin;C:\Users\Olli\.elan\toolchains\stable\bin;C:\Users\Olli\lean-3.4.1-windows\bin;;C:\Users\Olli\AppData\Local\Programs\Microsoft VS Code\bin

C:\Users\Olli\Dev\Lean&gt;lean --run C:\Users\Olli\.elan\toolchains\stable\bin\../\lib\lean\leanpkg\leanpkg\main.lean new playground
failed to start child process
PS C:\Users\Olli\Dev\Lean&gt;
</pre></div>


<p>I also tried modifying the script to get rid of the funny looking <code>\../</code> part of the path, but I get the same result</p>

#### [ Olli (Sep 23 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474483):
<p>This is what I have installed:</p>
<div class="codehilite"><pre><span></span>PS C:\Users\Olli\Dev\Lean&gt; lean --version
Lean (version 3.4.1, commit 17fe3decaf8a, Release)
PS C:\Users\Olli\Dev\Lean&gt; elan --version
elan 0.7.0 (0dd8c5ce4 2018-09-16)
</pre></div>

#### [ Keeley Hoek (Sep 23 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474485):
<p>At your terminal what happens if you type <code>test -f foo</code></p>

#### [ Olli (Sep 23 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474491):
<p>this is PowerShell, so there is no such command</p>

#### [ Olli (Sep 23 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474530):
<p>what are we trying to find out?</p>

#### [ Keeley Hoek (Sep 23 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474536):
<p>this is precisely the problem!</p>

#### [ Keeley Hoek (Sep 23 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474537):
<p>(and maybe other things)</p>

#### [ Keeley Hoek (Sep 23 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474539):
<p><code>leanpkg</code> attempts to spawn <code>test</code> when it runs, and it fails, so you see that message</p>

#### [ Olli (Sep 23 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474605):
<p>ah I see, so if I installed a version of that utility compiled for Windows, then that might be a workaround?</p>

#### [ Keeley Hoek (Sep 23 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474648):
<p>If you'd be willing to help diagnose, try opening <code>C:\Users\Olli\.elan\toolchains\stable\bin\../\lib\lean\leanpkg\leanpkg\main.lean</code> in a text editor, and navigate to line <code>199</code>. You should see a line:</p>
<div class="codehilite"><pre><span></span>  ex ← exists_file user_toml_fn,
</pre></div>


<p>Try replacing that line with</p>
<div class="codehilite"><pre><span></span> let ex := tt,
</pre></div>


<p>Does your command before work then?</p>

#### [ Keeley Hoek (Sep 23 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474660):
<p>Yes I suppose having a unix-like environment with coreutils would work, but it really shouldn't be necessary. <code>leanpkg</code> should be better<br>
If this works for you I can get you a less dodgy solution cooked up in a second, since you're using elan</p>

#### [ Keeley Hoek (Sep 23 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474704):
<p>Actually my line number is wrong.... But I still mean that line I quoted</p>

#### [ Keeley Hoek (Sep 23 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474705):
<p>Should be line <code>196</code></p>

#### [ Olli (Sep 23 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474757):
<p>Like this?</p>
<div class="codehilite"><pre><span></span>  <span class="k">let</span> <span class="n">user_toml_fn</span> <span class="o">:=</span> <span class="n">dot_lean_dir</span> <span class="bp">++</span> <span class="s2">&quot;/&quot;</span> <span class="bp">++</span> <span class="n">leanpkg_toml_fn</span><span class="o">,</span>
  <span class="n">ex</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">,</span>
  <span class="n">when</span> <span class="o">(</span><span class="bp">¬</span> <span class="n">ex</span><span class="o">)</span> <span class="err">$</span> <span class="n">write_manifest</span> <span class="o">{</span>
      <span class="n">name</span> <span class="o">:=</span> <span class="s2">&quot;_user_local_packages&quot;</span><span class="o">,</span>
      <span class="n">version</span> <span class="o">:=</span> <span class="s2">&quot;1&quot;</span>
    <span class="o">}</span> <span class="n">user_toml_fn</span><span class="o">,</span>
</pre></div>


<p>I get:</p>
<div class="codehilite"><pre><span></span>C:\Users\Olli\.elan\toolchains\stable\lib\lean\leanpkg\leanpkg\main.lean:182:4: error: non-exhaustive match, the followi
ng cases are missing:
main &quot;configure&quot; list.nil ({data := _} :: _)
main &quot;configure&quot; ({data := _} :: _) _
main &quot;new&quot; list.nil _
main &quot;new&quot; [_] ({data := _} :: _)
main &quot;new&quot; (_ :: {data := _} :: _) _
main &quot;init&quot; list.nil _
main &quot;init&quot; [_] ({data := _} :: _)
main &quot;init&quot; (_ :: {data := _} :: _) _
main &quot;add&quot; list.nil _
main &quot;add&quot; [_] ({data := _} :: _)
main &quot;add&quot; (_ :: {data := _} :: _) _
main &quot;upgrade&quot; list.nil ({data := _} :: _)
main &quot;upgrade&quot; ({data := _} :: _) _
main &quot;install&quot; list.nil _
main &quot;install&quot; [_] ({data := _} :: _)
main &quot;install&quot; (_ :: {data := _} :: _) _
main _ _ _
C:\Users\Olli\.elan\toolchains\stable\lib\lean\leanpkg\leanpkg\main.lean:196:5: error: command expected
failed to start child process
</pre></div>

#### [ Keeley Hoek (Sep 23 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474819):
<p>you need a <code>let</code> in front of the <code>ex</code>, but I'm reading more now and this won't solve your problem :(( (it will still be the same)<br>
<code>leanpkg</code> wants <code>test</code> and (unix) <code>mkdir</code></p>

#### [ Keeley Hoek (Sep 23 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134474837):
<p>I should be able to cook something up which does help you, though! Let me dig in a for a sec</p>

#### [ Olli (Sep 23 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134475008):
<p>thanks, yeah I now see what the issue is, I have been meaning to install Lean in WSL but so far haven't had any need to use libraries yet so I didn't get around to it</p>

#### [ Keeley Hoek (Sep 23 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134475208):
<p>Yeah there are very many pieces which assume a unix-y environment, even just down to the directory separator character<br>
Setting something like WSL up sounds like your best bet :)</p>

#### [ Keeley Hoek (Sep 23 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134475210):
<p>(at the moment)</p>

#### [ Olli (Sep 23 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134475526):
<p>if making leanpkg natively support Windows is too tall of a task, I would say the next best thing would be improving the error messages for this particular situation</p>

#### [ Keeley Hoek (Sep 23 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134475862):
<p>I didn't write it, but the comments in there make sure to say the intention was to add windows support later<br>
I didn't realise that it was just broken on windows</p>
<p>I might try to make a version that runs natively later this week</p>

#### [ Andrew Ashworth (Sep 23 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134477434):
<p>don't all the lean installation instructions assume a mingw installation?</p>

#### [ Olli (Sep 23 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134477522):
<p>I do have MinGW installed, but that does not include <code>test</code> which is not an executable but rather a shell built-in as far as I can tell</p>

#### [ Andrew Ashworth (Sep 23 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134477633):
<p>ahh. I never noticed this issue, because a bash shell is required to compile lean</p>

#### [ Keeley Hoek (Sep 23 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134477915):
<p>So I have no idea about MinGW anything, but for what its worth I've built coreutils before and it has a <code>test</code> binary<br>
Idk if it's in MinGW though</p>

#### [ Reid Barton (Sep 23 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134477924):
<p>Yeah, on a normal unix system, <code>test</code> is both a shell built-in (for speed) and an executable</p>

#### [ Reid Barton (Sep 23 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134477978):
<p>I don't know how POSIX-like the MinGW shell is, but you can try <code>which test</code> or <code>command test</code> (if nothing happens, it worked)</p>

#### [ Olli (Sep 23 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478025):
<p>it's not included with the installation of MinGW that I have, and I've tried googling if I can download it separately from somewhere but unfortunately <code>test</code> is a rather tricky name when it comes to search engines</p>

#### [ Reid Barton (Sep 23 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478027):
<p>Yes, I found that as well...</p>

#### [ Keeley Hoek (Sep 23 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478030):
<p>does MinGW ship with a shell?</p>

#### [ Reid Barton (Sep 23 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478035):
<p>Are you using MSYS?</p>

#### [ Olli (Sep 23 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478074):
<p>yes</p>

#### [ Keeley Hoek (Sep 23 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478075):
<p>doesn't msys have bash?</p>

#### [ Olli (Sep 23 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478088):
<p>yes it does, I will try that next</p>

#### [ Reid Barton (Sep 23 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478095):
<p>The question is whether it has <code>/usr/bin/test</code> though, right?</p>

#### [ Keeley Hoek (Sep 23 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478136):
<p>I'd be blown away if it didn't!</p>

#### [ Reid Barton (Sep 23 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478138):
<p>Well, yeah...</p>

#### [ Olli (Sep 23 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478194):
<div class="codehilite"><pre><span></span>PS C:\MSYS\1.0\bin&gt; ./bash.exe
bash.exe&quot;-3.1$ which test
which: test: unknown command
bash.exe&quot;-3.1$ exit
</pre></div>

#### [ Keeley Hoek (Sep 23 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478200):
<p>classic!</p>

#### [ Olli (Sep 23 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478206):
<p>Git bash for windows has it</p>

#### [ Olli (Sep 23 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478228):
<p>and there it does work as expected</p>

#### [ Reid Barton (Sep 23 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478294):
<p>I have no idea whether this is useful, but I did find through Google some log <a href="https://gist.github.com/choco-bot/eec2966667c148959f417ca93995222e#file-install-txt-L523" target="_blank" title="https://gist.github.com/choco-bot/eec2966667c148959f417ca93995222e#file-install-txt-L523">https://gist.github.com/choco-bot/eec2966667c148959f417ca93995222e#file-install-txt-L523</a> where it installs something called <code>msys2-base-x86_64-20180531.tar</code> and on line 1054 it installs a certain <code>test.exe</code></p>

#### [ Keeley Hoek (Sep 23 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478303):
<p>a few windows people here seem to use MSYS2, maybe its less insane! (I dare say that's why they have been oblivious to these issues on windows)</p>

#### [ Andrew Ashworth (Sep 23 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478459):
<p>you can't just run bash exe</p>

#### [ Andrew Ashworth (Sep 23 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478460):
<p>the mingw bash script sets a bunch of environment variables</p>

#### [ Andrew Ashworth (Sep 23 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478461):
<p>also, I use MSYS2 with no issues</p>

#### [ Olli (Sep 23 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134478505):
<p>I see, yeah I will try installing MSYS2, and I just confirmed that I was able to add mathlib to a new project and it appears to work fine from VSCode which is good</p>

#### [ Reid Barton (Sep 23 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134482297):
<p><span class="user-mention" data-user-id="126113">@Olli</span>, so is your conclusion that leanpkg is not compatible with MSYS, but is compatible with MSYS2?</p>

#### [ Olli (Sep 23 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134482841):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> yes that appears to be correct</p>

#### [ Olli (Sep 23 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134483308):
<p>MSYS2 contains <code>test.exe</code></p>

#### [ Bryan Gin-ge Chen (Sep 23 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134485601):
<p>Is it also true that using the git-for-windows bash shell also works for you? I don't think I have msys2 on my windows 10 machine and I got leanpkg working there.</p>

#### [ Olli (Sep 23 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134486944):
<p>yes, I should probably have tried that first, but had totally forgot I even had it installed</p>

#### [ Bryan Gin-ge Chen (Sep 23 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134487071):
<p>That's great, thanks for being so patient and looking into it. Now we should look into editing these solutions into the various docs that are floating around out there...</p>

#### [ Mario Carneiro (Sep 23 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134487567):
<p>I don't think git bash is fully usable for lean, although I forget why. I made some attempts to do this when I started and some necessary packages were missing with no clear way to get them</p>

#### [ Mario Carneiro (Sep 23 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134487588):
<p>Certainly CMD and powershell won't work</p>

#### [ Mario Carneiro (Sep 23 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134487622):
<p>I haven't tested Cygwin extensively, but it has its own issues to deal with and I found MSYS2 much easier</p>

#### [ Mario Carneiro (Sep 23 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134487642):
<p>I'd be curious to see if anyone makes lean work with WSL</p>

#### [ Bryan Gin-ge Chen (Sep 23 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/134487844):
<p>I've been using git bash up to now and haven't noticed anything wrong, but all I'm doing with regards to lean is just running <code>leanpkg upgrade</code> and <code>leanpkg build</code> occasionally. I did have to mess around with my console program to get unicode characters to print properly though.</p>

#### [ Scott Morrison (Oct 25 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/136440118):
<p>Hi <span class="user-mention" data-user-id="110032">@Reid Barton</span>, did you ever sort this out? Can we just delete the <code>lean-3.4.1</code> branch of <code>mathlib</code>? I see that Mario has been occasionally updating, but it still requires manual intervention.</p>

#### [ Reid Barton (Oct 25 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/136440150):
<p>No, we can't just delete it unfortunately--leanpkg requires a branch matching the lean version to exist, when that version is a stable version</p>

#### [ Reid Barton (Oct 25 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/136440338):
<p>I think the best "solution" we have for now is for somebody to figure out how to write a git hook that Mario can use to update the branch head automatically</p>

#### [ Neil Strickland (Jan 18 2019 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/156376118):
<p>I am also using git bash without obvious problems.  I have msys2 installed but it is not in the path so that should not make a difference.<br>
<span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> , what did you do to fix the unicode?</p>

#### [ Bryan Gin-ge Chen (Jan 18 2019 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/156376424):
<p>For me it was an issue with a setting in my console program, <a href="http://cmder.net/" target="_blank" title="http://cmder.net/"><code>cmder</code></a> which seems to be a reskin or repackaging of <a href="https://conemu.github.io/" target="_blank" title="https://conemu.github.io/"><code>conemu</code></a>. I had to add the setting <code>chcp utf8</code> to the environment per <a href="https://conemu.github.io/en/UnicodeSupport.html" target="_blank" title="https://conemu.github.io/en/UnicodeSupport.html">this page</a>.</p>

#### [ Neil Strickland (Jan 18 2019 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg/near/156378147):
<p>Thanks.  That suggestion doesn't seem immediately applicable to me as I am just using git bash in vscode (and git bash outside vscode seems to handle unicode correctly).  I poked around a bit more and found this page <a href="https://github.com/Microsoft/vscode/issues/60330" target="_blank" title="https://github.com/Microsoft/vscode/issues/60330">https://github.com/Microsoft/vscode/issues/60330</a>, but the suggestions there seemed to have no effect.  I'll probably just leave it now as it is not really causing me any trouble, it's just untidy.</p>


{% endraw %}
