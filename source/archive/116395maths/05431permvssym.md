---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/05431permvssym.html
---

## [maths](index.html)
### [perm vs sym](05431permvssym.html)

#### [Johan Commelin (Sep 28 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/perm%20vs%20sym/near/134819090):
In the determinants PR https://github.com/leanprover/mathlib/pull/378#issuecomment-425396841 I have copy-pasted @**Kenny Lau**s take on the symmetric group (`group_theory/sym.lean`). But in `group_theory/perm.lean` we already have a version by @**Chris Hughes**. Both files are several hundred lines long. There is substantial overlap, but both take their own approach in several places. I would like to use this thread to discuss how to merge these two files.

#### [Johan Commelin (Sep 28 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/perm%20vs%20sym/near/134819387):
Oh, the PR is from the `determinants` branch on community mathlib.

#### [Chris Hughes (Sep 28 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/perm%20vs%20sym/near/134821943):
I think I've done everything necessary for determinants, now that fintype is in mathlib, so anything that Kenny's done should probably be PRed separately from determinants.

#### [Johan Commelin (Sep 28 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/perm%20vs%20sym/near/134826417):
@**Kenny Lau** @**Chris Hughes** I removed `group_theory/sym.lean`.

