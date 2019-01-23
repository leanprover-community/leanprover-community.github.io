---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/91640derivehasreflect.html
---

## Stream: [general](index.html)
### Topic: [@[derive has_reflect]](91640derivehasreflect.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 21 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Bderive%20has_reflect%5D/near/148090195):
For long-enough structure definitions, e.g.
````
@[derive has_reflect]
structure config :=
(max_iterations  : ℕ := 500)
(max_discovers   : ℕ := 0)
(optimal         : bool := tt)
(exhaustive      : bool := ff)
(trace           : bool := ff)
(trace_summary   : bool := ff)
(trace_rules     : bool := ff)
(trace_discovery : bool := tt)
(explain         : bool := ff)
(explain_using_conv : bool := tt)
````
the `@[derive has_reflect]` takes multiple seconds to execute. Does anyone know why this is?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 21 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Bderive%20has_reflect%5D/near/148090203):
Actually, without at least some of those fields deleted, I haven't even seen it finish

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 21 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Bderive%20has_reflect%5D/near/148090210):
ok it does, eventually!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 21 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Bderive%20has_reflect%5D/near/148090213):
(but why?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 21 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Bderive%20has_reflect%5D/near/148090351):
Turn on profiling and see if it tells you something useful?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 21 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%40%5Bderive%20has_reflect%5D/near/148090946):
turns out its the fault of `tactic.add_decl` :(

