---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/93477computablefunctionType2Type1.html
---

## Stream: [general](index.html)
### Topic: [computable function Type 2 -> Type 1](93477computablefunctionType2Type1.html)

---

#### [Kenny Lau (Jul 31 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20function%20Type%202%20-%3E%20Type%201/near/130632607):
is there any computable non-constant function Type 2 -> Type 1?

#### [Chris Hughes (Jul 31 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20function%20Type%202%20-%3E%20Type%201/near/130632741):
`def f : Type 2 → Type := λ α , plift (nonempty α)`

#### [Kenny Lau (Jul 31 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20function%20Type%202%20-%3E%20Type%201/near/130632762):
nice

#### [Gabriel Ebner (Jul 31 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/computable%20function%20Type%202%20-%3E%20Type%201/near/130632821):
`Type` != `Type 1`.  You need one more `plift`.

