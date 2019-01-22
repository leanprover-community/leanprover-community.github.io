---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39096travisfailedtoexpandmacro.html
---

## [general](index.html)
### [travis "failed to expand macro"](39096travisfailedtoexpandmacro.html)

#### [Scott Morrison (Nov 13 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis "failed to expand macro"/near/147562010):
I just got another of these:
```
44.13s$ lean --recursive --export=mathlib.txt
<unknown>:1:1: error: failed to expand macro
The command "lean --recursive --export=mathlib.txt" exited with 1.
```
on travis.

#### [Scott Morrison (Nov 13 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis "failed to expand macro"/near/147562012):
https://travis-ci.org/leanprover/mathlib/jobs/454247679

#### [Scott Morrison (Nov 13 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis "failed to expand macro"/near/147562019):
`lean --make .` and `lean --make .` return happily.

#### [Reid Barton (Nov 13 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis "failed to expand macro"/near/147562026):
that's because you used `sorry`, I'm pretty sure

#### [Scott Morrison (Nov 13 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis "failed to expand macro"/near/147562029):
I remember someone else hitting this recently, but can't find it.

#### [Scott Morrison (Nov 13 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/travis "failed to expand macro"/near/147562036):
ah, okay, you're absolutely right, my mistake!

