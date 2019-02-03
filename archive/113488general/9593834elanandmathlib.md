---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/9593834elanandmathlib.html
---

## Stream: [general](index.html)
### Topic: [3.4, elan, and mathlib](9593834elanandmathlib.html)

---


{% raw %}
#### [ Johan Commelin (Apr 19 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295801):
<p>I just installed <code>elan</code>. Succesfully it seems. I then ran <code>mkdir ~/mess/leantest</code> and inside that directory, I ran <code>elan toolchain install nightly</code>. This provided me with a <code>leanpkg</code> command, and I ran <code>leanpkg add https://github.com/leanprover/mathlib</code>. After cloning from github, it complained <code>cannot find revision lean-3.4.0 in repository _target/deps/mathlib</code>. I guess this is somehow expected, because mathlib is not 3.4.0 ready. Right?</p>

#### [ Johan Commelin (Apr 19 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295811):
<p>So which permutation of command should I run, to get the most up to date version of lean + mathlib on my box?</p>

#### [ Mario Carneiro (Apr 19 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295909):
<p>do you have a <code>leanpkg.toml</code> file? What is in it?</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295915):
<p>You're probably using Lean stable, which is installed by elan by default - see <code>lean -v</code> or <code>elan show</code></p>

#### [ Mario Carneiro (Apr 19 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295926):
<p>What do I need to do to make this work?</p>

#### [ Mario Carneiro (Apr 19 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295931):
<p>Is it just adding a tag with the name <code>lean-3.4.0</code>?</p>

#### [ Johan Commelin (Apr 19 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295932):
<div class="codehilite"><pre><span></span>elan show
installed toolchains
--------------------

stable-x86_64-unknown-linux-gnu
nightly-x86_64-unknown-linux-gnu

active toolchain
----------------

stable-x86_64-unknown-linux-gnu (default)
Lean (version 3.4.0, commit 4be96eaaaf71, Release)
</pre></div>

#### [ Johan Commelin (Apr 19 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295935):
<p>I do not have a <code>.toml</code> file</p>

#### [ Johan Commelin (Apr 19 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295974):
<p>Should I write this myself?</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295992):
<p><code>leanpkg init &lt;package name&gt;</code> will create it for you. You can use <code>leanpkg +nightly init ...</code> to set the Lean version to a nightly, but I'm not sure there is any point in encouraging users to use nightlies any more. <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> What do you think?</p>

#### [ Johan Commelin (Apr 19 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296038):
<p>Ok, I see</p>

#### [ Johan Commelin (Apr 19 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296039):
<p>Is there a concensus?</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296049):
<p>Not yet I think. Right now, <code>stable</code> and <code>nightly</code> are functionally the same Lean version.</p>

#### [ Mario Carneiro (Apr 19 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296050):
<p>Assuming lean is completely frozen now, I guess we can move to building against 3.4.0, but I expect some occasional bugfixes will come along, and then I will want to go back to nightlies</p>

#### [ Johan Commelin (Apr 19 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296051):
<p>I hope that, now that 3.4 is out, there is a stable way to get everything working together</p>

#### [ Johan Commelin (Apr 19 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296104):
<p>And then we document this, so that users know which 5 commands to run in a fresh directory to get a lean project up and running</p>

#### [ Mario Carneiro (Apr 19 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296106):
<p>For now, though, you want to make sure that your lean version is nightly-2018-04-06 since that's what mathlib master is using</p>

#### [ Johan Commelin (Apr 19 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296113):
<p>Ok, and how should I make sure I get that nightly, using <code>elan</code></p>

#### [ Sebastian Ullrich (Apr 19 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296116):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Yeah, I guess a tag should work. Not sure if force-updating it will work too :) .</p>

#### [ Johan Commelin (Apr 19 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296119):
<p>(Because it seems using <code>elan</code> is wise)</p>

#### [ Mario Carneiro (Apr 19 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296123):
<p>I am not the elan guru in this conversation :)</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296124):
<p><code>leanpkg +nightly-2018-04-06 init mypackage</code></p>

#### [ Johan Commelin (Apr 19 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296125):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> When do you expect mathlib to use 3.4? (No pressure...)</p>

#### [ Mario Carneiro (Apr 19 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296130):
<p>Probably tomorrow or the day after, when I get a chance to sit down and look at the changes</p>

#### [ Johan Commelin (Apr 19 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296178):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> But to have a <code>leanpkg</code> command, I already need to first run an <code>elan</code> command, right?</p>

#### [ Johan Commelin (Apr 19 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296180):
<p>Because <code>elan</code> provides me with a <code>leanpkg</code></p>

#### [ Sebastian Ullrich (Apr 19 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296187):
<p>No, you just need to have elan installed</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296194):
<p>It's the same as <code>elan run nightly-2018-04-06 leanpkg init mypackage</code>, if you like that better :)</p>

#### [ Johan Commelin (Apr 19 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296237):
<p>Ok, so I empty my leantest directory</p>

#### [ Johan Commelin (Apr 19 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296245):
<p>And I get</p>

#### [ Johan Commelin (Apr 19 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296248):
<div class="codehilite"><pre><span></span>$ elan run nightly-2018-04-06 leanpkg init leantest
error: toolchain &#39;nightly-2018-04-06-x86_64-unknown-linux-gnu&#39; is not installed
</pre></div>

#### [ Sebastian Ullrich (Apr 19 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296340):
<p>Oops, I was hoping this worked... then you need to run <code>elan toolchain install nightly-2018-04-06</code> first</p>

#### [ Johan Commelin (Apr 19 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296348):
<p>Ok, I'll try that</p>

#### [ Johan Commelin (Apr 19 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296393):
<p>My first goal now, is to write a 10-line readme, that will explain how to start a fresh project.</p>

#### [ Johan Commelin (Apr 19 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296394):
<p>Including VScode integration, I hope</p>

#### [ Johan Commelin (Apr 19 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296406):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> That worked. And now I also ran <code>elan run nightly-2018-04-06 leanpkg init leantest</code></p>

#### [ Johan Commelin (Apr 19 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296411):
<p>Should the next step be <code>leanpkg add https://github.com/leanprover/mathlib
</code>?</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296465):
<p>Yes</p>

#### [ Mario Carneiro (Apr 19 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296473):
<p>is there a way to get the version number from mathlib?</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296480):
<p>You mean the <code>lean_version</code>?</p>

#### [ Mario Carneiro (Apr 19 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296481):
<p>yes</p>

#### [ Johan Commelin (Apr 19 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296483):
<p>Ok, that worked. I assume now I should run <code>leanpkg build</code>. Right?</p>

#### [ Mario Carneiro (Apr 19 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296484):
<p>The mathlib elan setup doesn't say anything about lean versions</p>

#### [ Mario Carneiro (Apr 19 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296536):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> If you get that 10 line startup script working, pr it to the mathlib readme</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296537):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> That should work, but not do much. Lean only builds the part of the dependencies you actually import in your <code>src</code> directory</p>

#### [ Johan Commelin (Apr 19 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296546):
<p>Ok, so there is no need to run <code>leanpkg build</code> right now?</p>

#### [ Johan Commelin (Apr 19 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296547):
<p>Then I won't do it</p>

#### [ Johan Commelin (Apr 19 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296589):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Ok, I'll do that. Once I've got it working (^;</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296591):
<p>I was surprised you were able to run <code>leanpkg add</code> before initializing the package. I guess you got a "failed to open file 'leanpkg.toml'" only at the very end? Pretty much a bug in leanpkg, oh well.</p>

#### [ Johan Commelin (Apr 19 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296604):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> I love breaking things. Hehe</p>

#### [ Johan Commelin (Apr 19 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296650):
<p>Right, so I did not run <code>leanpkg build</code>. Only fired up VScode</p>

#### [ Johan Commelin (Apr 19 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296660):
<p>It says <code>No Lean file active</code> in the Lean messages, after I opened a <code>.lean</code> file</p>

#### [ Moses Schönfinkel (Apr 19 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296729):
<p>Clicking anywhere in the file usually fixes this for me.</p>

#### [ Johan Commelin (Apr 19 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296749):
<p>Ok, that works. Never had to do that...</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296786):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Not sure what you're trying to achieve. The Travis build will select the correct version from <code>lean_version</code> automatically.</p>

#### [ Mario Carneiro (Apr 19 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296794):
<p>well, I'm mildly surprised that the default setup gave the wrong version of lean for mathlib</p>

#### [ Mario Carneiro (Apr 19 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296804):
<p>I want a short command or script to give to a newbie that wants the latest version of mathlib and a compatible version of lean</p>

#### [ Mario Carneiro (Apr 19 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296858):
<p>I'd prefer that the script not contain the literal string <code>nightly-2018-04-06</code> since that ages</p>

#### [ Johan Commelin (Apr 19 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296877):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> But I need to tell VScode to use the correct version of lean, right? So I edit the settings, to point it to <code>~/.elan/toolchains/nightly-2018-04-06-x86_64-unknown-linux-gnu/bin/lean</code>, is that correct?</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296932):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> I've only tested emacs so far, but specifying <code>~/.elan/bin/lean</code> should work</p>

#### [ Johan Commelin (Apr 19 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297004):
<div class="codehilite"><pre><span></span>Lean: Unable to start the Lean server process: Error: spawn ~/.elan/bin/lean ENOENT The lean.executablePath may be incorrect, make sure it is a valid Lean executable
</pre></div>

#### [ Johan Commelin (Apr 19 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297007):
<p>Alas, it is still complaining</p>

#### [ Mario Carneiro (Apr 19 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297029):
<p>put <code>.exe</code> at the end?</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297072):
<p>On Linux?</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297074):
<p>Maybe it doesn't like the <code>~</code></p>

#### [ Johan Commelin (Apr 19 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297080):
<p>Yes, I'm on linux</p>

#### [ Johan Commelin (Apr 19 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297134):
<p>Ok, that seems to have done it. I expanded the <code>~</code> to my homedir</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297136):
<p>Nice, good to know</p>

#### [ Johan Commelin (Apr 19 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297144):
<p>Ok, I'm now try to compile Kevin's result that Spec(R) is quasi-compact</p>

#### [ Johan Commelin (Apr 19 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297145):
<p>If that works, then I'll write the little readme</p>

#### [ Johan Commelin (Apr 19 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297154):
<p>Also, is there a way to tell lean not to use all my CPU threads?</p>

#### [ Johan Commelin (Apr 19 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297269):
<div class="codehilite"><pre><span></span>mkdir leantest/
cd leantest/
elan run nightly-2018-04-06 leanpkg init leantest
elan toolchain install nightly-2018-04-06
elan run nightly-2018-04-06 leanpkg init leantest
ls
ls -a
leanpkg add https://github.com/leanprover/mathlib
leanpkg add https://github.com/kbuzzard/lean-stacks-project
ls
elan show

# Change VScode settings to point to &quot;/home/&lt;user&gt;/.elan/bin/lean&quot;
</pre></div>

#### [ Johan Commelin (Apr 19 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297276):
<p>That is my current bash history</p>

#### [ Johan Commelin (Apr 19 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297290):
<p>So, I'll clean it up, and write a bit of details. But I thought I would log it here as well</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297293):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> So, this looks like a chicken and egg problem - when selecting the Lean version for creating the package, we don't know what dependencies the user will install yet. Well, it doesn't really matter what version to use for creating the package, so we could suggest to the user to change their Lean version after the fact when adding mathlib. I'm planning to do the same on <code>leanpkg upgrade</code>; we can also discuss this at <a href="https://github.com/Kha/elan/issues/5" target="_blank" title="https://github.com/Kha/elan/issues/5">https://github.com/Kha/elan/issues/5</a></p>

#### [ Johan Commelin (Apr 19 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297535):
<p>O.o.....</p>
<div class="codehilite"><pre><span></span>Lean: Server has stopped due to signal SIGSEGV
</pre></div>


<p>That doesn't sound good...</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298604):
<p>Johan -- one possibility is that you just get everything working in the old way, and just wait until mathlib is running with 3.4.</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298643):
<p>The reason this might be useful is that what we will ultimately really need</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298644):
<p>is a clear and concise set of instructions</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298645):
<p>on how to get Lean 3.4 and mathlib running.</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298647):
<p>And at the minute mathlib doesn't work with Lean 3.4, and elan still has teething troubles</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298654):
<p>in other words, I guess what I'm saying is that I am waiting until mathlib works with Lean 3.4 before I start thinking about writing down some succinct explanation of how to use elan</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298656):
<p>and for me there is no hurry because I have a set-up that works without elan</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298707):
<p>OTOH I'm sure Sebastian is appreciating your comments on elan.</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298709):
<p>As for the segv</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298710):
<p>you do occasionally get these, although they are quite rare</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298717):
<p>a good way of getting them is to compile a project, thus getting a bunch of .olean files, and then changing the version of Lean you're using</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298720):
<p>so the first thing you need to do is to rule this out</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298759):
<p>and the second big question is whether you can reliably reproduce the segfault</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298764):
<p>and if you can, then you get an achievement</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298766):
<p>and you're allowed to post an issue to the lean repo</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298780):
<p>I've had a couple recently but I couldn't reproduce them, annoyingly</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298821):
<p>(the moment I get one, I hit ctrl-Z to go back a bit, ctrl-shift-P Lean:restart to restart Lean, and then try typing exactly the same keys again)</p>

#### [ Kevin Buzzard (Apr 19 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298842):
<p>I am really really looking forwards to the stability of 3.4 + mathlib, but until then I have plenty to do :-)</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125299255):
<p>Just to be clear, any issues happening _after_ Lean was started successfully should not be elan's fault :)</p>

#### [ Johan Commelin (Apr 19 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125301335):
<p>So <code>find . -name *.olean</code> finds nothing. Which means the first option is ruled out. I guess. Now I will start the backtracking.</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125301402):
<p>The .olean version mismatch problem has been fixed for quite some time</p>

#### [ Johan Commelin (Apr 19 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125306980):
<p>Can Lean segfault if it runs out of memory? I opened a file from Kevin's lean-stacks-project and I had not compiled anything before. I only have 4GB in my rusty Thinkpad (no swap). So I think that Lean maybe ran out of memory.</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125307443):
<p>There have been many ways for Lean to segfault so far, but that one would be new :)</p>

#### [ Johan Commelin (Apr 19 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125307469):
<p>So, should I run <code>leanpkg build</code> or something similar? Ought that work?</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125307522):
<p>Worth a try, at least then you know it's easily reproducible</p>

#### [ Johan Commelin (Apr 19 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125307543):
<div class="codehilite"><pre><span></span>$ leanpkg build
configuring leantest 0.1
mathlib: trying to update _target/deps/mathlib to revision 7d1ab388bb097db5d631d11892e8f110e1f2e9cd
&gt; git checkout --detach 7d1ab388bb097db5d631d11892e8f110e1f2e9cd    # in directory _target/deps/mathlib
HEAD is now at 7d1ab38 feat(list/basic,...): minor modifications &amp; additions
lean-stacks-project: trying to update _target/deps/lean-stacks-project to revision a2204862a0c20c4ea4f98d5685c1a51a3b0279d3
&gt; git checkout --detach a2204862a0c20c4ea4f98d5685c1a51a3b0279d3    # in directory _target/deps/lean-stacks-project
HEAD is now at a220486 Merge branch &#39;master&#39; of github.com:kbuzzard/lean-stacks-project
&gt; lean --make src
</pre></div>

#### [ Johan Commelin (Apr 19 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125307604):
<p>This completed immediately...</p>

#### [ Johan Commelin (Apr 19 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125307607):
<p>Doesn't do any compiling at all</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125307844):
<p>Is your segfaulting file saved in the <code>src</code> directory?</p>

#### [ Johan Commelin (Apr 19 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125316120):
<p>No, the <code>src/</code> dir is empty</p>

#### [ Sebastian Ullrich (Apr 19 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125325431):
<p>You should save your Lean files in <code>src</code>, as described in <a href="https://leanprover.github.io/reference/using_lean.html#directory-layout" target="_blank" title="https://leanprover.github.io/reference/using_lean.html#directory-layout">https://leanprover.github.io/reference/using_lean.html#directory-layout</a></p>

#### [ Johan Commelin (Apr 20 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125384466):
<p>Sorry, I'm completely confused. As you can see from my log above, I only ran <code>leanpkg add</code> to add mathlib and lean-stacks-project. Both are added to <code>_target/deps/</code>. The leave <code>src/</code> empty. What am I doing wrong?</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391323):
<p>Here's how you're supposed to run the stacks project.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391361):
<p>First, clone the stacks project.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391523):
<p>Then make it into a lean package with some leanpkg command which I forgot</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391558):
<p>then build it</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391670):
<p>Here's how you're supposed to make a new project with the stacks project as a dependency</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391716):
<p>First make a directory for your new project</p>

#### [ Johan Commelin (Apr 20 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391732):
<p>Ok, I see. I thought you had to <code>leanpkg add</code> it</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391813):
<p>then use leanpkg add to add the stacks project</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391845):
<p>I think I've got it straight.</p>

#### [ Johan Commelin (Apr 20 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391887):
<p>Aha, I hope this helps...</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391925):
<p>On behalf of the community I apologise for the lack of docs and the general difficulty of finding the docs you need</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391958):
<p>we are working on this problem</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392130):
<p>What happens in practice is that Sebastian does a really good job of writing all these package managers</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392200):
<p>and then he explains how things work here</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392247):
<p>and everyone learns</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392513):
<p>and then either stuff doesn't get written, or stuff gets written but in some place you might not expect, or stuff doesn't get written and then the older stuff is written but out of date and wrong.</p>

#### [ Johan Commelin (Apr 20 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392533):
<p>Right, I'll try to figure out the command to turn the clone into a lean package</p>

#### [ Patrick Massot (Apr 20 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392547):
<p>Yes we are working on it. I really for big improvements in the next few weeks</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392876):
<p>To make matters worse, and by "worse" I mean "better", we now have elan, which is something else</p>

#### [ Johan Commelin (Apr 20 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392932):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Could it be that you mean <code>leanpkg configure</code> to download the dependencies?</p>

#### [ Patrick Massot (Apr 20 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392979):
<p>Mathlib goes 3.4, elan matures, TPIL and refman get updated and everything will become much easier</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125393016):
<p>and the most comprehensive docs on elan are obtained by searching for elan here :-)</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125393109):
<p>"Mathlib goes 3.4" -- here's hoping!</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125393225):
<p>Presumably you noticed the rather terrifying-looking stumbling block</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125393596):
<p>One thing I love about Lean is that we are free to add various type annotations everywhere if we get confused</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125393614):
<p>and I get confused a lot</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125394557):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> line 16 of an old commit</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125394572):
<p><a href="https://github.com/leanprover/lean/commit/37bde20d07dc28b7fd3e84a1c768b9ce547bd5a8#diff-93c4834f2a585510be668daf86b8e81fR16" target="_blank" title="https://github.com/leanprover/lean/commit/37bde20d07dc28b7fd3e84a1c768b9ce547bd5a8#diff-93c4834f2a585510be668daf86b8e81fR16">https://github.com/leanprover/lean/commit/37bde20d07dc28b7fd3e84a1c768b9ce547bd5a8#diff-93c4834f2a585510be668daf86b8e81fR16</a></p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125394649):
<p>That was when mathlib was called library_dev</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125394787):
<p>When the docs moved into the reference manual, some of those old docs got lost</p>

#### [ Johan Commelin (Apr 20 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125394963):
<p>Ok, thanks!</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125395693):
<p>You seem to be right -- the "creating new packages" docs survived but the "working on existing packages" para got lost.</p>

#### [ Johan Commelin (Apr 20 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125396463):
<p>Whoohoo, now <code>leanpkg build</code> is actually doing something!</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125396803):
<p>I would go and have a cup of tea</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125396981):
<p>I would also recommend maximising your console window and using ctrl-(minus key) to minimise your font size</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125397420):
<p>that way successful compilation of a file whose full path is more than 80 characters doesn't result in your terminal being filled with garbage</p>

#### [ Johan Commelin (Apr 20 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125397837):
<p>I see... I'm already running fullscreen. I'm about to get a computer account at the department, and I'm going to ask for a second screen on my desk.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125397850):
<p>[and note the message I sent you yesterday about certain files which have errors in as they are WIPs; I know it's a bit unprofessional but I develop on more than one machine and github is just a convenient way to store my half-written files]</p>

#### [ Johan Commelin (Apr 20 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125397980):
<p>Running VScode on a 12" Thinkpad is horrible</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398040):
<p>I am absolutely serious when I say</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398142):
<p>that I run VS Code on a laptop with a medium size screen</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398190):
<p>and the fact that it was horrible</p>

#### [ Johan Commelin (Apr 20 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398203):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Yes, I saw that message. No problem. I think branches could help you there. You can push WIP branches to github as well.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398209):
<p>actually made me bite the bullet and start wearing glasses</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398256):
<p>and now I have glasses (for reading)</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398298):
<p>I can just minimise the font to quite small :-)</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398440):
<p>I am not good at branches yet.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398475):
<p>but I am getting there.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398688):
<p>I never needed them before because Kenny and Chris work on localised code and don't care if other stuff doesn't compile</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398741):
<p>and nobody else has ever paid any attention to the project :-)</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398791):
<p>We are nearly done though.</p>

#### [ Johan Commelin (Apr 20 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125399260):
<blockquote>
<p>and nobody else has ever paid any attention to the project :-)</p>
</blockquote>
<p>I'm sorry for being curious</p>

#### [ Johan Commelin (Apr 20 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125399367):
<p>I should just wait a couple of days (-;</p>

#### [ Kevin Buzzard (Apr 20 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125399566):
<p>I just this morning pushed a version of tah01HR which contains a concrete endgame</p>

#### [ Kevin Buzzard (Apr 20 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125399695):
<p>i.e. "we need to prove this lemma and that lemma and then just glue everything together"</p>

#### [ Kevin Buzzard (Apr 20 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125399936):
<p>I think I am right when I say that mathlib compiles with the nightly of 6th April</p>

#### [ Kevin Buzzard (Apr 20 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125399993):
<p>and the project should work with that</p>

#### [ Johan Commelin (Apr 20 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125400371):
<p>So far the compile is doing its job perfectly (-;</p>

#### [ Patrick Massot (Apr 20 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125400434):
<p>You don't have to guess here, it's right there: <a href="https://github.com/leanprover/mathlib/blob/master/leanpkg.toml#L4" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/leanpkg.toml#L4">https://github.com/leanprover/mathlib/blob/master/leanpkg.toml#L4</a></p>

#### [ Kevin Buzzard (Apr 20 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125400646):
<p>aah, another undocumented gem ;-)</p>

#### [ Johan Commelin (Apr 20 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125400783):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Yes, now I only need to convince my laptop of that (-;</p>

#### [ Patrick Massot (Apr 20 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408071):
<p>Did you put that same line in your own project <code>leanpkg.toml</code>?</p>

#### [ Kevin Buzzard (Apr 20 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408162):
<p>if he cloned my project then it should be there</p>

#### [ Johan Commelin (Apr 20 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408164):
<p>Atm I just cloned the lean-stacks-project repo, which has its own toml</p>

#### [ Kevin Buzzard (Apr 20 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408296):
<p>So the system does actually work</p>

#### [ Patrick Massot (Apr 20 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408297):
<p>what does <code>which leanpkg</code> tells you?</p>

#### [ Kevin Buzzard (Apr 20 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408321):
<p>it's just that we need to document it better</p>

#### [ Johan Commelin (Apr 20 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408391):
<p>And <code>elan</code> parsed it, and made me use the right version of <code>leanpkg</code> and <code>lean</code> <span class="emoji emoji-1f389" title="tada">:tada:</span></p>

#### [ Johan Commelin (Apr 20 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408557):
<div class="codehilite"><pre><span></span>$ which leanpkg
/home/jmc/.elan/bin/leanpkg
</pre></div>

#### [ Patrick Massot (Apr 20 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408605):
<p>ok, it's all fine</p>

#### [ Patrick Massot (Apr 20 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408758):
<p>also, make sure you never ever define a leanpath variable in VScode</p>

#### [ Patrick Massot (Apr 20 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408832):
<p>this only leads to confusion</p>

#### [ Johan Commelin (Apr 20 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125409071):
<p>I set it to <code>/home/jmc/.elan/bin/lean</code></p>

#### [ Patrick Massot (Apr 20 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125409118):
<p>You shouldn't</p>

#### [ Johan Commelin (Apr 20 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125409169):
<p>So what <em>should</em> I do?</p>

#### [ Patrick Massot (Apr 20 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125409362):
<p>You should simply launch VScode from a terminal where the shell path variable is set correctly (ie <code>which lean</code> points to <code>.elan/bin/lean</code>)</p>

#### [ Patrick Massot (Apr 20 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125409629):
<p>which will happen if you have <code>source $HOME/.elan/env</code> in your initialization file (<code>.profile</code> or <code>.bashrc</code> or...)</p>

#### [ Johan Commelin (Apr 20 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125410457):
<p>Ok, that makes sense</p>

#### [ Johan Commelin (Apr 20 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125410489):
<p>I'll do that from now on</p>

#### [ Kevin Buzzard (Apr 20 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125411324):
<p>ha ha, I use leanpath all the time; it points to a symlink :-)</p>

#### [ Kevin Buzzard (Apr 20 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125411592):
<p>Johan -- I haven't used elan at all yet but I just changed the README in lean-stacks-project to explain what I think you just did.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125411895):
<p>Feel free to submit a PR explaining elan. I have not even attempted to find out whether elan has docs; I have other things to worry about currently :-)</p>

#### [ Johan Commelin (Apr 20 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125412651):
<p>If my compile succeeds, then the first thing I will do is write some small docs and PR them.</p>

#### [ Patrick Massot (Apr 20 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125423318):
<p>Let me try something (we'll see if we can PR later). Instruction for a first time user of Lean under linux:</p>
<ul>
<li>make sure <a href="https://code.visualstudio.com/download" target="_blank" title="https://code.visualstudio.com/download">VScode</a> is installed</li>
<li>launch VScode and install the Lean extension by clicking the extension icon in the view bar at left and searching for lean. quit VScode for ow</li>
<li>make sure <code>git</code> and <code>curl</code> are installed, using your distrib package manager</li>
<li><code>curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh</code> and type enter when a question is asked. Then add <code>source .elan/env</code> to your shell initialization script, say <code>~/.bashrc</code>, and source it in the current terminal (or relaunch a new terminal).</li>
<li>The previous step downloaded the latest stable release, that may be too recent or too old for mathlib, and you really want mathlib. Have a look at <a href="https://github.com/leanprover/mathlib/blob/master/leanpkg.toml#L4" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/leanpkg.toml#L4">https://github.com/leanprover/mathlib/blob/master/leanpkg.toml#L4</a> to see what is the nightly mathlib currently wants. Say you see <code>nightly-2018-04-06</code>. Then run <code>elan toolchain install nightly-2018-04-06</code>.</li>
<li>Now we want some playground to experiment. Use <code>elan run nightly-2018-04-06 leanpkg new my_playground</code>. This will  create a <code>my_playground</code> directory with a lean project layout. </li>
<li>Go to that directory and type <code>leanpkg add leanprover/mathlib</code> this will download mathlib and put it inside <code>my_playground/_target/deps</code>,</li>
<li>At this point you can already create some lean file in <code>my_playground/src</code>, launch VScode, go to and play with Lean by opening the file, typing <code>Ctrl-shift-enter</code> to open Lean message windows, and type, say <code>#check 1</code> to see the result</li>
<li>You cant also use <code>import group_theory.subgroup</code> and then <code>#check is_subgroup</code>. But this will use uncompiled version of mathlib, which is very inefficient. If you run <code>leanpkg build</code> from inside <code>my_playground</code> then it will compile only files which are dependencies of mathlib <code>group_theory/subgroup.lean</code>.</li>
<li>If you want to play more, it's better to compile all mathlib once and for all. You can do this by going into <code>my_playground/_target/deps/mathlib</code>, type <code>lean --make</code>and go get some coffee.</li>
</ul>

#### [ Patrick Massot (Apr 20 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125424229):
<p>That being said, we really need mathlib nightlies (ie. precompiled mathlib)</p>

#### [ Patrick Massot (Apr 20 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125424479):
<p>It makes no sense that curious potential users have to wait for mathlib to compile</p>

#### [ Johan Commelin (Apr 20 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125428649):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> I think that is a very good start</p>

#### [ Johan Commelin (Apr 20 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125428740):
<p>I would also like a small section on how to work on an existing project, like lean-stacks-project</p>

#### [ Kevin Buzzard (Apr 20 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125428806):
<p>You can copy that from my README</p>

#### [ Kevin Buzzard (Apr 20 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125428860):
<p>except that it should be updated to use elan</p>

#### [ Simon Hudon (Apr 21 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125495917):
<p>In elan, when downloading Lean and its library, would it be possible to add a <code>leanpkg.toml</code> file at the root of <code>library</code>. That would make it easier to browse with emacs.</p>

#### [ Sebastian Ullrich (Apr 21 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125496101):
<p>What parts of browsing would that change?</p>

#### [ Simon Hudon (Apr 21 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125496250):
<p>When I open <code>init/meta/tactic.lean</code> in emacs, it tries to start a lean server and fails and <code>M-.</code> won't help <br>
me go to a definition</p>

#### [ Sebastian Ullrich (Apr 21 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125496453):
<p>Oh, it looks like we forgot to include <code>library/leanpkg.path</code> in the releases. I'll fix it for the future.</p>

#### [ Simon Hudon (Apr 21 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125496722):
<p>Can <code>leanpkg.path</code> specify the version of <code>lean</code> to launch when editing the files?</p>

#### [ Sebastian Ullrich (Apr 21 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125496876):
<p>Ah, you are right. I guess injecting a <code>leanpkg.toml</code> file could indeed be the best solution.</p>


{% endraw %}
