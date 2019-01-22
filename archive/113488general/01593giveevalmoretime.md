---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01593giveevalmoretime.html
---

## [general](index.html)
### [give #eval more time](01593giveevalmoretime.html)

#### [Chris Hughes (Sep 09 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give #eval more time/near/133615259):
Is there a way to give `#eval` more time before a deterministic timeout?

#### [Kevin Buzzard (Sep 09 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give #eval more time/near/133615377):
On the command line there is a `--timeout=num` option.

#### [Kevin Buzzard (Sep 09 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give #eval more time/near/133615398):
So I guess you could try editing your VS Code preferences (if you want to do this in VS Code)

#### [Kevin Buzzard (Sep 09 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give #eval more time/near/133615458):
wooah Ctrl-comma in VS Code has changed.

#### [Kevin Buzzard (Sep 09 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give #eval more time/near/133615530):
oh actually I've just found that it is an option in VS Code: 

```
  // Set a deterministic timeout (it is approximately the maximum number of memory allocations in thousands) for the Lean server.
  "lean.timeLimit": 100000
```

So try ctrl-comma (or file -> preferences -> settings) and then search for `lean.timeLimit` and try changing that (maybe you have to click on a pencil and say you want to edit it before you can edit it)

#### [Kevin Buzzard (Sep 09 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give #eval more time/near/133615544):
I only half-know what I'm talking about here though, so no guarantee of success.

#### [Chris Hughes (Sep 09 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give #eval more time/near/133615727):
Doesn't seem to make any difference.

#### [Keeley Hoek (Sep 09 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give #eval more time/near/133615731):
did you restart the lean server after you did it? I forget this more often than I'd like...

#### [Chris Hughes (Sep 09 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give #eval more time/near/133616137):
No I didn't. Thanks @**Keeley Hoek**

#### [Chris Hughes (Sep 09 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give #eval more time/near/133616412):
Thanks. I have now managed to compute that my proof of quadratic reciprocity used exactly 5000 theorems, definitions, axioms and constants traced all the way back to axioms.

#### [Bryan Gin-ge Chen (Sep 09 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/give #eval more time/near/133617608):
That's cool! Have you posted the script for doing that somewhere?

