---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/14768increasememoryconsumptionthreshold.html
---

## [general](index.html)
### [increase memory consumption threshold](14768increasememoryconsumptionthreshold.html)

#### [Kevin Buzzard (Aug 02 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase memory consumption threshold/near/130780966):
Someone is trying to use Lean on a Win 7 machine here and we're constantly running into memory issues. Lean suggests "increase memory consumption threshold" -- is this something which is possible to do and which might actually work? It's a Windows 7 machine using `.olean` files which were built on Windows 10 :-/ but that's only because none of us are using Win7 so we can't make the .olean files for Win7.

#### [Kevin Buzzard (Aug 02 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase memory consumption threshold/near/130781134):
Every third time we hit `Lean : restart` we get away with it :-)

#### [Kenny Lau (Aug 02 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase memory consumption threshold/near/130781144):
go to task manager and look at memory consumption?

#### [Reid Barton (Aug 02 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase memory consumption threshold/near/130781228):
That sometimes means Lean thinks it needs to rebuild things

#### [Gabriel Ebner (Aug 02 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase memory consumption threshold/near/130791589):
1) As @**Reid Barton** said, try `leanpkg build` first.  2) In vscode, go to user settings (ctrl+shift+p user settings), and search for lean. :smile:

#### [Kevin Buzzard (Aug 02 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase memory consumption threshold/near/130791671):
It didn't look unreasonable. I initially felt like we were on the boundary of what the machine was capable of, but it didn't make much sense because the machine had 16 gigs of ram and it never got filled up. Maybe it's the dodgy .olean files (and the fact that they were zipped up from some other computer and I'm not sure the timestamps would have survived -- I don't know anything about Windows timestamps).

#### [Kevin Buzzard (Aug 02 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase memory consumption threshold/near/130791708):
I don't think I can run `leanpkg build` -- I didn't try, but the machine did not have git and I didn't have admin privileges and I think that in the past this has been enough to stop the build from working -- it fails right at the start before trying to build anything. That was the root of the problem.

#### [Reid Barton (Aug 02 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase memory consumption threshold/near/130791965):
The default limit is a mere 1GB, so it makes sense that you did not see the machine's memory fill up.
My guess is also a timestamp issue.

#### [Reid Barton (Aug 02 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase memory consumption threshold/near/130791987):
When lean is invoked by the editor, does it write out `.olean` files for modules it compiles?

#### [Reid Barton (Aug 02 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase memory consumption threshold/near/130791991):
My impression is that it does not

#### [Reid Barton (Aug 02 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase memory consumption threshold/near/130792165):
It's also easy to accidentally modify a mathlib source file (especially if you are using jump-to-definition) and that also tends to cause this behavior.

#### [Gabriel Ebner (Aug 02 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase memory consumption threshold/near/130793805):
```quote
I don't think I can run `leanpkg build` -- I didn't try, but the machine did not have git 
```
You can also do `lean --make`

