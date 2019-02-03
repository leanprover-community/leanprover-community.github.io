---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11441isuserleanpkgpathfalse.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: ["is_user_leanpkg_path": false](https://leanprover-community.github.io/archive/113488general/11441isuserleanpkgpathfalse.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Nov 28 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148726964):
<p><code>lean --path</code>. If I run it on my home machine I get <code>"is_user_leanpkg_path": true,</code> and if I run it in CoCalc I get <code>"is_user_leanpkg_path": false,</code>. What does this variable even mean? I am having trouble with paths in CoCalc and am trying to debug.</p>

#### [ Gabriel Ebner (Nov 28 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148727956):
<p>Try running <code>lean -p</code> inside and outside of <code>mathlib</code> to see the difference.  The <code>is_user_leanpkg_path</code> indicates whether you are inside a directory containing a <code>leanpkg.path</code> file.  If it is false, then lean looks for imports in the directories listed in the <code>leanpkg.path</code> file.  If it is false, then it consults <code>~/.lean/leanpkg.path</code>.</p>

#### [ Kevin Buzzard (Nov 28 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148728778):
<p>Aah! Thanks Gabriel.</p>

#### [ Kevin Buzzard (Nov 28 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148729505):
<p>Hmm, I need more information. Is there any way of telling inside a live Lean session what paths Lean is using when it looks for imports? I don't know exactly how Lean is being invoked (and in particular in which directory it's being invoked) in CoCalc.</p>

#### [ Kevin Buzzard (Nov 28 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148733549):
<p>OK so in CoCalc the line which starts a new Lean server is here:</p>
<p><a href="https://github.com/sagemathinc/cocalc/blob/master/src/smc-project/lean/lean.ts#L71" target="_blank" title="https://github.com/sagemathinc/cocalc/blob/master/src/smc-project/lean/lean.ts#L71">https://github.com/sagemathinc/cocalc/blob/master/src/smc-project/lean/lean.ts#L71</a></p>
<p>using <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> 's <a href="https://github.com/leanprover/lean-client-js/blob/master/lean-client-js-node/src/process.ts#L5" target="_blank" title="https://github.com/leanprover/lean-client-js/blob/master/lean-client-js-node/src/process.ts#L5">https://github.com/leanprover/lean-client-js/blob/master/lean-client-js-node/src/process.ts#L5</a> . Where will Lean be looking for imports with this method?</p>

#### [ Gabriel Ebner (Nov 28 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148734474):
<p>The second argument is the working directory, and cocalc passes the home directory (~).  So either <code>~/leanpkg.path</code> or <code>.lean/leanpkg.path</code> depending on whether the first file exists.  The cocalc code breaks if you clone mathlib and then open a file there.</p>

#### [ Kevin Buzzard (Nov 28 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148734755):
<p>Aah again! So what if I open a random .lean file in <code>~/Assignments/homework_01/src/</code> [which is what I want my students to do]? What will the path be then?</p>

#### [ Gabriel Ebner (Nov 28 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735038):
<p>It will always look in the same place.  It only depends on the directory where you start the lean server from.  (Which is the home directory here.)</p>

#### [ Gabriel Ebner (Nov 28 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735106):
<p>As an easy workaround, you could create a <code>~/leanpkg.path</code> file with the appropriate imports.</p>

#### [ Kevin Buzzard (Nov 28 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735389):
<p>I tried this and couldn't get it to work. Perhaps I have so many <code>leanpkg.path</code>s that I have confused things even more. I'll try again.</p>

#### [ Gabriel Ebner (Nov 28 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735503):
<p><code>cd; lean -p | grep leanpkg_path_file</code> should tell you which one it uses.  You have to restart the server for it to pick up changes though.</p>

#### [ Kevin Buzzard (Nov 28 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735593):
<p>I can't type this in a .lean file though.</p>

#### [ Gabriel Ebner (Nov 28 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735672):
<p>CoCalc has a terminal though?</p>

#### [ Gabriel Ebner (Nov 28 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735695):
<p>Besides, we have <code>io.cmd</code>.</p>

#### [ Kevin Buzzard (Nov 28 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735784):
<p>Hmm. Maybe I'm not restarting the server when I think I am?</p>

#### [ Kevin Buzzard (Nov 28 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735800):
<p>Bingo! Got it. <em>Many</em> thanks Gabriel.</p>

#### [ Kevin Buzzard (Nov 28 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735887):
<p>[noises of someone who has been banging his head against a wall for hours and has finally got it to work now emanating from my office]</p>

#### [ Patrick Massot (Nov 28 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148736165):
<p>Kevin, I'd be interested in any information about using Lean in CoCalc with real students, and dependencies beyond the core lib</p>

#### [ Kevin Buzzard (Nov 28 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148736343):
<p>So would <span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> I think. Hopefully by tomorrow at noon I will have got something coherent to say.</p>

#### [ Chris Hughes (Nov 28 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148736647):
<p>I tried using Cocalc but I couldn't work out how to import mathlib.</p>

#### [ Jeremy Avigad (Nov 29 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148752688):
<p>Indeed, I'll be trying to assign homework in CoCalc next semester, so any information you share as to how to do it will be most welcome.</p>

#### [ William Stein (Nov 29 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148758612):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  do I need to do anything or change anything?  It sounds like you figured something out...</p>
<p>Right now CoCalc has native support for editing .lean files, and also -- just in case you are desparate -- you can also run VSCode via an x11 session by clicking +New --&gt; X11 Desktop (but you have to install the lean extension).</p>

#### [ Kevin Buzzard (Nov 29 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148773021):
<blockquote>
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  do I need to do anything or change anything?  It sounds like you figured something out...</p>
</blockquote>
<p><span class="user-mention" data-user-id="116034">@William Stein</span>  I figured out (a) where to put a <code>leanpkg.path</code> so that invoking Lean via clicking on a <code>.lean</code> file will read it [answer: <code>~</code>] and (b) after you screwed up by not putting it there, exiting the GUI view of the <code>.lean</code> file and then clicking on it again might not actually restart the server (so you remain screwed), however clicking on the "restart service" icon will restart it. You don't need to do anything I guess. My problem as an instructor is that I now have to set an assignment and persuade my students that they need to create the appropriate <code>leanpkg.path</code> file in their home directories before clicking on any <code>.lean</code> files, and I don't know the best way of doing that.</p>

#### [ Kevin Buzzard (Nov 29 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148773037):
<p>Thanks once again to Gabriel, who made debugging this issue far easier than it could have been. I will write some notes and put them in another thread.</p>

#### [ Gabriel Ebner (Nov 29 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148773092):
<p>The way the emacs extension does this is by starting one server per <code>leanpkg.path</code> file.  It looks at the parent directories of the current file and then starts the lean server in the first directory that has that <code>leanpkg.path</code> file.</p>

#### [ Kevin Buzzard (Nov 29 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148778499):
<p><a href="#narrow/stream/113488-general/subject/Lean.20homework.20in.20CoCalc/near/148778475" title="#narrow/stream/113488-general/subject/Lean.20homework.20in.20CoCalc/near/148778475">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/Lean.20homework.20in.20CoCalc/near/148778475</a></p>
<p>I've got Lean homework working in CoCalc.</p>


{% endraw %}
