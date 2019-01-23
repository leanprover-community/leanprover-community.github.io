---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11441isuserleanpkgpathfalse.html
---

## Stream: [general](index.html)
### Topic: ["is_user_leanpkg_path": false](11441isuserleanpkgpathfalse.html)

---


{% raw %}
#### [ Kevin Buzzard (Nov 28 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148726964):
`lean --path`. If I run it on my home machine I get `"is_user_leanpkg_path": true,` and if I run it in CoCalc I get `"is_user_leanpkg_path": false,`. What does this variable even mean? I am having trouble with paths in CoCalc and am trying to debug.

#### [ Gabriel Ebner (Nov 28 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148727956):
Try running `lean -p` inside and outside of `mathlib` to see the difference.  The `is_user_leanpkg_path` indicates whether you are inside a directory containing a `leanpkg.path` file.  If it is false, then lean looks for imports in the directories listed in the `leanpkg.path` file.  If it is false, then it consults `~/.lean/leanpkg.path`.

#### [ Kevin Buzzard (Nov 28 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148728778):
Aah! Thanks Gabriel.

#### [ Kevin Buzzard (Nov 28 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148729505):
Hmm, I need more information. Is there any way of telling inside a live Lean session what paths Lean is using when it looks for imports? I don't know exactly how Lean is being invoked (and in particular in which directory it's being invoked) in CoCalc.

#### [ Kevin Buzzard (Nov 28 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148733549):
OK so in CoCalc the line which starts a new Lean server is here:

https://github.com/sagemathinc/cocalc/blob/master/src/smc-project/lean/lean.ts#L71

using @**Gabriel Ebner** 's https://github.com/leanprover/lean-client-js/blob/master/lean-client-js-node/src/process.ts#L5 . Where will Lean be looking for imports with this method?

#### [ Gabriel Ebner (Nov 28 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148734474):
The second argument is the working directory, and cocalc passes the home directory (~).  So either `~/leanpkg.path` or `.lean/leanpkg.path` depending on whether the first file exists.  The cocalc code breaks if you clone mathlib and then open a file there.

#### [ Kevin Buzzard (Nov 28 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148734755):
Aah again! So what if I open a random .lean file in `~/Assignments/homework_01/src/` [which is what I want my students to do]? What will the path be then?

#### [ Gabriel Ebner (Nov 28 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735038):
It will always look in the same place.  It only depends on the directory where you start the lean server from.  (Which is the home directory here.)

#### [ Gabriel Ebner (Nov 28 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735106):
As an easy workaround, you could create a `~/leanpkg.path` file with the appropriate imports.

#### [ Kevin Buzzard (Nov 28 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735389):
I tried this and couldn't get it to work. Perhaps I have so many `leanpkg.path`s that I have confused things even more. I'll try again.

#### [ Gabriel Ebner (Nov 28 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735503):
`cd; lean -p | grep leanpkg_path_file` should tell you which one it uses.  You have to restart the server for it to pick up changes though.

#### [ Kevin Buzzard (Nov 28 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735593):
I can't type this in a .lean file though.

#### [ Gabriel Ebner (Nov 28 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735672):
CoCalc has a terminal though?

#### [ Gabriel Ebner (Nov 28 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735695):
Besides, we have `io.cmd`.

#### [ Kevin Buzzard (Nov 28 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735784):
Hmm. Maybe I'm not restarting the server when I think I am?

#### [ Kevin Buzzard (Nov 28 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735800):
Bingo! Got it. *Many* thanks Gabriel.

#### [ Kevin Buzzard (Nov 28 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148735887):
[noises of someone who has been banging his head against a wall for hours and has finally got it to work now emanating from my office]

#### [ Patrick Massot (Nov 28 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148736165):
Kevin, I'd be interested in any information about using Lean in CoCalc with real students, and dependencies beyond the core lib

#### [ Kevin Buzzard (Nov 28 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148736343):
So would @**Jeremy Avigad** I think. Hopefully by tomorrow at noon I will have got something coherent to say.

#### [ Chris Hughes (Nov 28 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148736647):
I tried using Cocalc but I couldn't work out how to import mathlib.

#### [ Jeremy Avigad (Nov 29 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148752688):
Indeed, I'll be trying to assign homework in CoCalc next semester, so any information you share as to how to do it will be most welcome.

#### [ William Stein (Nov 29 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148758612):
@**Kevin Buzzard**  do I need to do anything or change anything?  It sounds like you figured something out...

Right now CoCalc has native support for editing .lean files, and also -- just in case you are desparate -- you can also run VSCode via an x11 session by clicking +New --> X11 Desktop (but you have to install the lean extension).

#### [ Kevin Buzzard (Nov 29 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148773021):
```quote
@**Kevin Buzzard**  do I need to do anything or change anything?  It sounds like you figured something out...
```
@**William Stein**  I figured out (a) where to put a `leanpkg.path` so that invoking Lean via clicking on a `.lean` file will read it [answer: `~`] and (b) after you screwed up by not putting it there, exiting the GUI view of the `.lean` file and then clicking on it again might not actually restart the server (so you remain screwed), however clicking on the "restart service" icon will restart it. You don't need to do anything I guess. My problem as an instructor is that I now have to set an assignment and persuade my students that they need to create the appropriate `leanpkg.path` file in their home directories before clicking on any `.lean` files, and I don't know the best way of doing that.

#### [ Kevin Buzzard (Nov 29 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148773037):
Thanks once again to Gabriel, who made debugging this issue far easier than it could have been. I will write some notes and put them in another thread.

#### [ Gabriel Ebner (Nov 29 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148773092):
The way the emacs extension does this is by starting one server per `leanpkg.path` file.  It looks at the parent directories of the current file and then starts the lean server in the first directory that has that `leanpkg.path` file.

#### [ Kevin Buzzard (Nov 29 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22is_user_leanpkg_path%22%3A%20false/near/148778499):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/Lean.20homework.20in.20CoCalc/near/148778475

I've got Lean homework working in CoCalc.


{% endraw %}
