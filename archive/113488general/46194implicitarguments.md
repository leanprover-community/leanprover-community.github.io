---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/46194implicitarguments.html
---

## [general](index.html)
### [implicit arguments](46194implicitarguments.html)

#### [petercommand (Jan 10 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments/near/154824603):
Is there any way to tell lean to show all the implicit arguments in an error message?
For example, sometimes when rewrite fails, I would want to know if there are different implicit args that caused the rewrite to fail

#### [petercommand (Jan 10 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments/near/154824649):
Or in a type mismatch error

#### [petercommand (Jan 10 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments/near/154824655):
Sometimes it shows all the implicit arguments sometimes it doesn't

#### [Johan Commelin (Jan 10 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments/near/154824659):
`set_option pp.all true` will show you everything... that might be too much though...

#### [Rob Lewis (Jan 10 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments/near/154824660):
`set_option pp.implicit true` before the declaration.

#### [Johan Commelin (Jan 10 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments/near/154824663):
Aah, there you go.

#### [petercommand (Jan 10 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments/near/154824664):
Thanks

#### [Rob Lewis (Jan 10 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/implicit%20arguments/near/154824669):
There are other `pp` options that autocomplete should show you. `all` is difficult to read.

