---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63693untypedexpressions.html
---

## [general](index.html)
### [untyped expressions](63693untypedexpressions.html)

#### [Jakob von Raumer (Apr 19 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/untyped%20expressions/near/125308427):
When referring to local constants it's pretty annoying that I have to give the type every time. Can't I used leave the type unelaborated until the local constant is abstracted away anyway?

#### [Kenny Lau (Apr 19 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/untyped%20expressions/near/125308443):
for example?

#### [Sebastian Ullrich (Apr 19 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/untyped%20expressions/near/125308537):
@**Jakob von Raumer** Sure, you can use any dummy type as long as you don't need type inference

#### [Jakob von Raumer (Apr 19 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/untyped%20expressions/near/125308550):
@**Kenny Lau** When I use them in expressions that I later on treat with `expr.pis` for example

#### [Jakob von Raumer (Apr 19 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/untyped%20expressions/near/125308601):
Well, so I just use `(Type)?

#### [Sebastian Ullrich (Apr 19 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/untyped%20expressions/near/125308733):
yeah

