---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74703writingunicodetofile.html
---

## Stream: [general](index.html)
### Topic: [writing unicode to file](74703writingunicodetofile.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156363926):
Does anyone have experience using file i/o with unicode characters? Lean seems to be mangling them. But I'm pretty sure something like this has worked for me in the past.
```lean
import system.io
open io tactic
run_cmd unsafe_run_io $ do h ← mk_file_handle "oops.txt" mode.write, fs.put_str h "α β γ"
```
The contents of `oops.txt` are `� � �`. This is on my desktop, so no Windows nonsense going on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 18 2019 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156363965):
@**Keeley Hoek** ^

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 18 2019 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156366966):
https://github.com/leanprover/lean/commit/4e16bc7192f9f32b03222142e659fa3dae4b8025

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156367421):
Aha. I suppose this is related to this conversation: https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character.20encoding.20of.20VM/near/132250034

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 18 2019 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156367559):
And it looks like I'm using an old version of Lean that doesn't include that commit!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jan 18 2019 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156368083):
*starts writing the 3.4.2 changelog*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 18 2019 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156374294):
I'm currently compiling mathlib from scratch using Lean 3.4.2 (building on work by Bryan). I hope to open a mathlib PR very soon

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 18 2019 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156374710):
I'm now merging Johannes' latest commit, but it touches `order/basic` so I guess this is most recompiling from scratch...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 18 2019 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156375416):
https://github.com/leanprover/mathlib/pull/609

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 18 2019 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156376140):
Is the general idea that the moment lean 3.4.2 and mathlib are playing well together, we should all switch? ooh -- I see that https://leanprover.github.io/download/ now links to 3.4.2 so any new users are going to end up with 3.4.2. @**Scott Morrison|110087** do any installation procedures of yours or mine need updating I wonder?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Jan 18 2019 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156376525):
Not quite at the moment but as soon as this PR is merged https://github.com/leanprover/mathlib/pull/610

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 18 2019 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156377384):
I was faster

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Jan 18 2019 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156377551):
Hah, I missed that, probably because I was adding comments to mine.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 18 2019 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156377662):
My PR includes your commits (using it cherry-pick`) but also the latest upstream commits

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Jan 18 2019 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156377704):
I rebased mine on master before I PR'd so it should be up to date as well.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 18 2019 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156377836):
Ok, they should have the same effect then. I'll close mine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jan 19 2019 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156412063):
@**Kevin Buzzard** I think my installation instructions are still correct.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jan 19 2019 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156412120):
On <https://github.com/leanprover/mathlib/blob/master/docs/elan.md>, it suggests using `leanpkg +nightly new my_playground` to create a new repository.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jan 19 2019 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156412132):
That still seems reasonable, but it might be better to add a comment explaining what `+nightly` actually does, and explaining the alternatives.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jan 19 2019 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/writing%20unicode%20to%20file/near/156412135):
If anyone has advice about what should go there, I'm happy to update that file.

