---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63146testingtactics.html
---

## Stream: [general](index.html)
### Topic: [testing tactics](63146testingtactics.html)

---

#### [Scott Morrison (Mar 16 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/testing%20tactics/near/123790056):
I have a `meta def T : expr → tactic expr := ...` that I've written that isn't behaving properly, and I want to do some debugging. Inside the definition there are some `trace` statements that explain to me what's going on --- I just need a convenient way to invoke my tactic. Suppose I have some other `def f := ...`, and I want to invoke `T` on `f`. What do I do?

#### [Scott Morrison (Mar 16 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/testing%20tactics/near/123790062):
I'm hoping there's just something easy involving quotations that I don't know.

#### [Mario Carneiro (Mar 16 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/testing%20tactics/near/123790083):
Something like ``to_expr `(f) >>= T`` should work

#### [Scott Morrison (Mar 16 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/testing%20tactics/near/123790135):
```term `(f) has type reflected f but is expected to have type pexpr```

#### [Mario Carneiro (Mar 16 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/testing%20tactics/near/123790137):
Actually, `` `(f)`` is already an `expr`, so ``T `(f)`` should work

#### [Scott Morrison (Mar 16 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/testing%20tactics/near/123790146):
``` to_expr ``(f)``` works, however

#### [Mario Carneiro (Mar 16 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/testing%20tactics/near/123790148):
You would use `to_expr` if you need to parse the expression at run time rather than parse time

#### [Scott Morrison (Mar 16 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/testing%20tactics/near/123790199):
thanks!

