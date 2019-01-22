---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31671cpuonmac.html
---

## [general](index.html)
### [cpu on mac](31671cpuonmac.html)

#### [Yulia Zaplatina (Aug 13 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132034358):
Anyone had an issue with lean using > 95% cpu on mac?

#### [Mario Carneiro (Aug 13 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132034433):
lean often takes up as much cpu as it can. It depends on what you are doing

#### [Yulia Zaplatina (Aug 13 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132034448):
Just opened the workspace

#### [Mario Carneiro (Aug 13 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132034604):
If you import a heavy theory, it may take a few minutes

#### [Mario Carneiro (Aug 13 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132034617):
You can also try building the lean files with `lean --make` to help speed it up

#### [Yulia Zaplatina (Aug 13 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132034639):
thanks, I'll try

#### [Kevin Buzzard (Aug 13 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132034729):
Yulia -- I'll be in the MLC in about an hour. You might want to build your mathlib (make all the .olean files) if this is constantly happening.

#### [Yulia Zaplatina (Aug 13 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132034783):
it went down to 20%, but now that i've open

#### [Yulia Zaplatina (Aug 13 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132034787):
*opened a file, it's back up to over 300%

#### [Yulia Zaplatina (Aug 13 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132034805):
@**Kevin Buzzard** I'll do that now 👍🏼

#### [Kevin Buzzard (Aug 13 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132035136):
This is not abnormal behaviour -- the first time Lean starts up it might have to do a lot of work. It could be building the real numbers from the axioms of mathematics, for example. It only needs to do this once though.

#### [Yulia Zaplatina (Aug 13 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132036385):
Ok, so I've built lean and the cpu remains around 90% - is that normal? or is there a way of decreasing it even more?

#### [Mario Carneiro (Aug 13 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132036480):
are there yellow bars in the gutter of vscode?

#### [Yulia Zaplatina (Aug 13 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132036563):
nope

#### [Yulia Zaplatina (Aug 13 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132036614):
only green, blue and red

#### [Mario Carneiro (Aug 13 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132036632):
does lean have the :check: in the status bar?

#### [Yulia Zaplatina (Aug 13 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132036633):
oh actually, yes, in some files

#### [Yulia Zaplatina (Aug 13 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132036698):
yep, there's a :check: but some files are highlighted yellow

#### [Mario Carneiro (Aug 13 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132036726):
maybe it would be best to wait for Kevin

#### [Yulia Zaplatina (Aug 13 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132036829):
O

#### [Yulia Zaplatina (Aug 13 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu on mac/near/132036883):
it's down to 10 now :sweat_smile: I think it should be fine, thank you!

