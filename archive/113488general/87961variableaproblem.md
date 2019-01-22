---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87961variableaproblem.html
---

## [general](index.html)
### [variable a problem](87961variableaproblem.html)

#### [Kevin Buzzard (Mar 08 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/variable%20a%20problem/near/123463049):
This is presumably well-known but it has just bitten one of my undergraduates. They wrote `have Ht2 : (a < nat.succ t) → (nat.succ t < c) → (a < c),` in the middle of a tactic proof, with a,t,c nats, and get a type mismatch error: `term a has type  nat.succ t < c : Prop`. Chris tells me that this is because you can't use `have` in a tactic proof with an implies sign and a variable `a`. That sounds like a bug to me. Is it officially not a bug though?

#### [Sebastian Ullrich (Mar 08 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/variable%20a%20problem/near/123463243):
Oh, it is https://github.com/leanprover/lean/issues/1822

#### [Kevin Buzzard (Mar 08 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/variable%20a%20problem/near/123463326):
So we have to wait for the parser refactoring?

#### [Sebastian Ullrich (Mar 08 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/variable%20a%20problem/near/123463636):
Yes

