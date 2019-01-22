---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/15473Emptyornotempty.html
---

## [general](index.html)
### [Empty or not empty](15473Emptyornotempty.html)

#### [Patrick Massot (Dec 17 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Empty or not empty/near/152017713):
How can I prove something by case splitting depending on whether or not a type is inhabited? I know about the `inhabited` and `nonempty` classes, but it looks like I can't do anything when I assume `not (nonempty a)` or `not (inhabited a)`. So what I do is `by_cases H : ∃ x : α, true,`. Is that right?

#### [Chris Hughes (Dec 17 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Empty or not empty/near/152018000):
You can prove `a -> false` from `h : not (nonempty a)`, it's just `assume x, h ⟨x⟩`. Not sure what else you'd need apart from this.

#### [Patrick Massot (Dec 17 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Empty or not empty/near/152018113):
Strange, I thought I tried that. Thanks! I does look slightly less stupid that way

