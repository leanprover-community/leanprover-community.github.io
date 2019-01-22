---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86303helpwithtravis.html
---

## [general](index.html)
### [help with travis](86303helpwithtravis.html)

#### [Scott Morrison (Oct 14 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/help with travis/near/135790347):
Hmm, a strange error:

```
> lean --make .
> lean --make test
> lean --recursive --export=mathlib.txt
<unknown>:1:1: error: invalid object declaration, environment already has an object named 'category_theory.limits.category_theory.limits.has_limits._proof_1'
```

#### [Scott Morrison (Oct 14 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/help with travis/near/135790352):
How come it doesn't complain with `lean --make`?

#### [Scott Morrison (Oct 14 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/help with travis/near/135790362):
Is this that two files, which are never imported in the same place, have the same named definition? And this isn't detected until the last run of lean?

#### [Scott Morrison (Oct 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/help with travis/near/135790418):
(Doesn't matter too much, there was an instance that should have been a def anyway, that should solve this.)

#### [Simon Hudon (Oct 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/help with travis/near/135790980):
```quote
Is this that two files, which are never imported in the same place, have the same named definition? And this isn't detected until the last run of lean?
```
That's right

