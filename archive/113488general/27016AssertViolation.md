---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27016AssertViolation.html
---

## Stream: [general](index.html)
### Topic: [Assert Violation](27016AssertViolation.html)

---


{% raw %}
#### [ Namdak Tonpa (Jan 09 2019 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Assert%20Violation/near/154711246):
```
LEAN ASSERTION VIOLATION
File: /tmp/lean-20180823-20161-4hyzri/lean-3.4.1/src/frontends/lean/elaborator.cpp
Line: 3167
Task: /Users/maxim/depot/groupoid/lean/homotopy_theory/formal/i_category/drag.lean: homotopy_theory.cofibrations.drag_equiv
m_ctx.match(e, *val2)
```

Just catch in Reid Barton's code :-) Unfortunately non-reproducable.

#### [ Reid Barton (Jan 09 2019 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Assert%20Violation/near/154713023):
I've seen errors like this as well, not sure what caused them. I thought they were related to things like changing branches or mathlib versions. They seem to go away on their own


{% endraw %}
