---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73211cleanupoldfiles.html
---

## Stream: [general](index.html)
### Topic: [clean up old files](73211cleanupoldfiles.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 22 2019 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/clean%20up%20old%20files/near/156607187):
I wrote two Python scripts this morning to help with the transition of moving everything to `src/`. One deletes `.olean` files without a corresponding `.lean` file, the other deletes directory trees that contain no files.
I notice @**Simon Hudon** also wrote an equivalent shell script in the fold PR (https://github.com/leanprover/mathlib/pull/376/files#diff-81a7c4de26bf82dac09e943b11b95792).
Windows users: is one of shell scripts/Python scripts more usable than the other?

