---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74858warnings.html
---

## Stream: [general](index.html)
### Topic: [warnings](74858warnings.html)

---

#### [Reid Barton (Dec 27 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152612059):
There isn't any way to suppress all warnings or specific warnings from lean, is there?

#### [Johan Commelin (Dec 27 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152612571):
In the editor? Or in compiler output in the terminal?

#### [Reid Barton (Dec 27 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152612608):
In the terminal

#### [Reid Barton (Dec 27 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152612612):
preferably, from the command line

#### [Johan Commelin (Dec 27 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152612613):
You could just pipe via grep...

#### [Johan Commelin (Dec 27 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152612615):
Completely customisable, but maybe not exactly user friendly

#### [Johan Commelin (Dec 27 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152612626):
What kind of filtering are you looking for?

#### [Reid Barton (Dec 27 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152612765):
Often I want to suppress the many "warning: imported file uses sorry" messages, and sometimes I want to ignore the messages about using sorry as well

#### [Johan Commelin (Dec 27 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/warnings/near/152613016):
That seems like something that `grep` could do for you.

