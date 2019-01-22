---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99873falseelim.html
---

## [general](index.html)
### [false.elim](99873falseelim.html)

#### [Kenny Lau (Sep 08 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/false.elim/near/133574791):
Why can `false` elim to anything even though it is only a `Prop`?

#### [Chris Hughes (Sep 08 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/false.elim/near/133574907):
More or less because even if it wasn't a Prop it would still be a subsingleton. Same reason for `and` `eq` and `acc`. I think more precisely any constructors whose type is not a `Prop` have to be mentioned in the type of the `Prop`. So `acc` is okay, because it's non-Prop constructor is mentioned in the type.

