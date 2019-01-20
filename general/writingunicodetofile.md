---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: general/writingunicodetofile.html
---

## [general](index.html)
### [writing unicode to file](writingunicodetofile.html)

#### Rob Lewis (Jan 18 2019 at 13:30):
Does anyone have experience using file i/o with unicode characters? Lean seems to be mangling them. But I'm pretty sure something like this has worked for me in the past.
```lean
import system.io
open io tactic
run_cmd unsafe_run_io $ do h ← mk_file_handle "oops.txt" mode.write, fs.put_str h "α β γ"
```
The contents of `oops.txt` are `� � �`. This is on my desktop, so no Windows nonsense going on.

#### Reid Barton (Jan 18 2019 at 13:31):
@**Keeley Hoek** ^

#### Patrick Massot (Jan 18 2019 at 14:24):
https://github.com/leanprover/lean/commit/4e16bc7192f9f32b03222142e659fa3dae4b8025

#### Rob Lewis (Jan 18 2019 at 14:31):
Aha. I suppose this is related to this conversation: https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Character.20encoding.20of.20VM/near/132250034

#### Rob Lewis (Jan 18 2019 at 14:33):
And it looks like I'm using an old version of Lean that doesn't include that commit!

#### Sebastian Ullrich (Jan 18 2019 at 14:41):
*starts writing the 3.4.2 changelog*

#### Patrick Massot (Jan 18 2019 at 16:06):
I'm currently compiling mathlib from scratch using Lean 3.4.2 (building on work by Bryan). I hope to open a mathlib PR very soon

#### Patrick Massot (Jan 18 2019 at 16:11):
I'm now merging Johannes' latest commit, but it touches `order/basic` so I guess this is most recompiling from scratch...

#### Patrick Massot (Jan 18 2019 at 16:20):
https://github.com/leanprover/mathlib/pull/609

#### Kevin Buzzard (Jan 18 2019 at 16:30):
Is the general idea that the moment lean 3.4.2 and mathlib are playing well together, we should all switch? ooh -- I see that https://leanprover.github.io/download/ now links to 3.4.2 so any new users are going to end up with 3.4.2. @**Scott Morrison|110087** do any installation procedures of yours or mine need updating I wonder?

#### Bryan Gin-ge Chen (Jan 18 2019 at 16:34):
Not quite at the moment but as soon as this PR is merged https://github.com/leanprover/mathlib/pull/610

#### Patrick Massot (Jan 18 2019 at 16:45):
I was faster

#### Bryan Gin-ge Chen (Jan 18 2019 at 16:47):
Hah, I missed that, probably because I was adding comments to mine.

#### Patrick Massot (Jan 18 2019 at 16:48):
My PR includes your commits (using it cherry-pick`) but also the latest upstream commits

#### Bryan Gin-ge Chen (Jan 18 2019 at 16:49):
I rebased mine on master before I PR'd so it should be up to date as well.

#### Patrick Massot (Jan 18 2019 at 16:50):
Ok, they should have the same effect then. I'll close mine

#### Scott Morrison (Jan 19 2019 at 01:41):
@**Kevin Buzzard** I think my installation instructions are still correct.

#### Scott Morrison (Jan 19 2019 at 01:42):
On <https://github.com/leanprover/mathlib/blob/master/docs/elan.md>, it suggests using `leanpkg +nightly new my_playground` to create a new repository.

#### Scott Morrison (Jan 19 2019 at 01:43):
That still seems reasonable, but it might be better to add a comment explaining what `+nightly` actually does, and explaining the alternatives.

#### Scott Morrison (Jan 19 2019 at 01:43):
If anyone has advice about what should go there, I'm happy to update that file.

