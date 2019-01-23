---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52425noobresusevariablenamequestion.html
---

## Stream: [general](index.html)
### Topic: [noob "resuse variable name" question](52425noobresusevariablenamequestion.html)

---

#### [Kevin Buzzard (Sep 16 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noob%20%22resuse%20variable%20name%22%20question/near/134048259):
Dammit I can never remember how to go from `H : P` and `HPQ : P -> Q` to `H : Q` in tactic mode, the point being that I want to throw the original `H` away and reuse the name. There's a tactic that does this but I can never remember the name and I can't come up with an algorithm to find out for myself, my searches have been futile, so sorry, I have to ask.

#### [Chris Hughes (Sep 16 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noob%20%22resuse%20variable%20name%22%20question/near/134048665):
`specialize` or `replace`

#### [Kevin Buzzard (Sep 16 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/noob%20%22resuse%20variable%20name%22%20question/near/134048907):
`replace` -- that was it. I knew it was something like `rewrite`. Thanks.

