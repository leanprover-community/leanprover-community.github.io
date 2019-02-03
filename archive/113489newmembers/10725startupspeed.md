---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/10725startupspeed.html
---

## Stream: [new members](index.html)
### Topic: [startup speed](10725startupspeed.html)

---


{% raw %}
#### [ Scott Olson (Sep 29 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895169):
<p>Is it normal for Lean to take several minutes to catch up when I freshly open my project in VSCode, even if I've completely precompiled the mathlib dependency to .olean files?</p>

#### [ Scott Olson (Sep 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895228):
<p>Maybe not several minutes, but at least around 1 minute</p>

#### [ Scott Olson (Sep 29 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895274):
<p>And once it's caught up it seems to spend a significant amount of time after that "checking import for sorry" every time</p>

#### [ Reid Barton (Sep 29 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895497):
<p>I use emacs but it doesn't sound normal. How did you build the mathlib dependency?</p>

#### [ Reid Barton (Sep 29 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895503):
<p><code>leanpkg build</code> in your project should help. <code>leanpkg build</code> inside <code>_target/deps/mathlib</code> will confuse lean and lead to this kind of behavior</p>

#### [ Scott Olson (Sep 29 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895598):
<p>Oh, interesting. I ended up doing the latter because the former wouldn't actually build mathlib at all</p>

#### [ Scott Olson (Sep 29 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895605):
<p>So I probably need to go back and debug what caused the original problem instead</p>

#### [ Patrick Massot (Sep 29 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895650):
<p>If you really want to make sure all of mathlib is built, even the pieces not currently needed in your project, you need do do <code>lean --make</code> inside <code>_targets/deps/mathlib</code>, not <code>leanpkg build</code></p>

#### [ Reid Barton (Sep 29 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895692):
<p>The original problem is just that lean is "smart" and only compiles the parts of the dependencies that are actually needed--which is annoying if that subset might increase in the future and you'd rather just build it once and be done with it.</p>

#### [ Scott Olson (Sep 29 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895694):
<p>I thought it might be something like that but I wasn't sure how to get around it, thanks!</p>

#### [ Scott Olson (Sep 29 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895704):
<p>Do I need to "undo" the <code>leanpkg build</code> I did inside <code>_target/deps/mathlib</code> somehow, or just run the correct command now?</p>

#### [ Patrick Massot (Sep 29 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895755):
<p>running the correct command should be enough</p>

#### [ Scott Olson (Sep 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895905):
<p>How exactly does Lean get confused here - do the .olean files mark themselves in some way, so that my project would not recognize the .olean files I previously built as its own? I'm scanning for hidden files or some other way it would possibly distinguish and finding nothing so far</p>

#### [ Kevin Buzzard (Sep 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895906):
<p>What OS are you using?</p>

#### [ Scott Olson (Sep 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895907):
<p>Windows 10</p>

#### [ Scott Olson (Sep 29 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895909):
<p>I run linux as well but haven't checked if I get the same behavior there yet</p>

#### [ Kevin Buzzard (Sep 29 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895949):
<p>Sebastian was saying the other day that sometimes Windows, or maybe some standard anti-virus, goes through the files and maybe randomly touches them messing up "last updated" times. I think Lean tries to recompile an olean file if it thinks that the lean file was modified after the olean file was built, and maybe it gets confused on Windows? I don't use this OS though and this is all second hand.</p>

#### [ Reid Barton (Sep 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895956):
<p>I think it has something to do with the <code>leanpkg.path</code> file, but I don't know exactly what</p>

#### [ Scott Olson (Sep 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895957):
<p>I'll keep an eye on the last updated times</p>

#### [ Kevin Buzzard (Sep 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895958):
<p>Sebastian was saying this in an attempt to explain why <code>leanpkg</code> regularly takes 10 seconds to start running on windows</p>

#### [ Kevin Buzzard (Sep 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134895959):
<p>despite core lean shipping with the olean files</p>

#### [ Kevin Buzzard (Sep 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134896009):
<p>(leanpkg is written in lean)</p>

#### [ Scott Olson (Sep 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134896015):
<p>I haven't had that trouble with <code>leanpkg</code> startup times. I installed it via <code>elan</code> if it makes a difference</p>

#### [ Scott Olson (Sep 29 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134896024):
<p>but perhaps I just don't have an AV that causes that specific problem</p>

#### [ Scott Olson (Sep 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134896067):
<p>I can confirm <code>leanpkg build</code> in the correct directory solved the problem for me, thanks all</p>

#### [ Scott Olson (Sep 29 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134896070):
<p>My problem before was misinterpreting the docs I was reading and assuming it would build all of mathlib, but I was running it before adding any imports so it actually built none of it</p>

#### [ Scott Olson (Sep 29 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134896197):
<p>Incidentally this solved another problem I had where VSCode's lean.exe would rise to over 2GiB of RAM during the initial build and never drop back down. Apparently it doesn't get as high when the precompiled stuff is available</p>

#### [ Reid Barton (Sep 29 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134896408):
<p>Oh--does your <code>mathlib</code> dependency specify a different version of lean than your top-level project, by any chance?</p>

#### [ Scott Olson (Sep 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134896991):
<p>Oh yeah, that would probably cause the .olean incompatibility by itself. <code>mathlib</code>'s toml says <code>3.4.1</code> but I'm using a recently nightly in my project, because if I used <code>3.4.1</code> it checks out the <code>lean-3.4.1</code> branch of <code>mathlib</code> and I wanted <code>master</code></p>

#### [ Scott Olson (Sep 29 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897030):
<p>This is probably a problem for even running <code>lean --make</code> inside the mathlib dir, right?</p>

#### [ Scott Olson (Sep 29 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897132):
<p>I did just run <code>lean --make</code> earlier and we can see the olean version difference:</p>
<div class="codehilite"><pre><span></span>$ head -c 60 src/regular.olean | xxd
00000000: 6f6c 6561 6e66 696c 6500 332e 342e 322c  oleanfile.3.4.2,
00000010: 206e 6967 6874 6c79 2d32 3031 382d 3038   nightly-2018-08
00000020: 2d32 332c 2063 6f6d 6d69 7420 6231 3361  -23, commit b13a
00000030: 6331 3237 6664 3833 00ff d828            c127fd83...(

$ head -c 60 _target/deps/mathlib/data/nat/basic.olean | xxd
00000000: 6f6c 6561 6e66 696c 6500 332e 342e 312c  oleanfile.3.4.1,
00000010: 2063 6f6d 6d69 7420 3137 6665 3364 6563   commit 17fe3dec
00000020: 6166 3861 00ff f2e4 59f1 0004 0002 696e  af8a....Y.....in
00000030: 6974 0000 0402 6c6f 6769 6300            it....logic.
</pre></div>

#### [ Reid Barton (Sep 29 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897190):
<blockquote>
<p>This is probably a problem for even running <code>lean --make</code> inside the mathlib dir, right?</p>
</blockquote>
<p>Yes if you already ran <code>leanpkg build</code> which created the <code>leanpkg.path</code> file there.</p>

#### [ Reid Barton (Sep 29 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897191):
<p>Or wait.</p>

#### [ Reid Barton (Sep 29 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897226):
<p>Actually I guess it is a question of elan.</p>

#### [ Scott Olson (Sep 29 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897231):
<p>Yeah, <code>elan</code> will automatically download and build with whatever version the toml specifies</p>

#### [ Scott Olson (Sep 29 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897241):
<p>I can probably do the mathlib dir manual <code>lean --make</code> by telling elan which specific version to build with, which seems fair to me for an optional manual step</p>

#### [ Reid Barton (Sep 29 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897242):
<p>I guess the <code>lean --make _target/deps/mathlib</code> instructions are safer in this particular situation then, assuming that elan uses the current working directory to start its search for the toml file</p>

#### [ Scott Olson (Sep 29 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897282):
<p>Ah yeah I should double check what it does in that case</p>

#### [ Scott Olson (Sep 29 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897291):
<p>I gotta say it's rather convenient for me coming from Rust that <code>elan</code> is based on <code>rustup</code> because I have a pretty good grasp on exactly how it works already =)</p>

#### [ Scott Olson (Sep 29 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/startup%20speed/near/134897501):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> You're right, using <code>lean --make _target/deps/mathlib</code> is the simplest/safest way to make sure it builds the whole thing with your current project's Lean version</p>


{% endraw %}
