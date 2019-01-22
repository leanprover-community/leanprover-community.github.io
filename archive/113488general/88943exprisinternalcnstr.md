---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88943exprisinternalcnstr.html
---

## [general](index.html)
### [expr.is_internal_cnstr](88943exprisinternalcnstr.html)

#### [Edward Ayers (Oct 09 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.is_internal_cnstr/near/135479383):
What does `expr.is_internal_cnstr` do?

#### [Edward Ayers (Oct 09 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.is_internal_cnstr/near/135479414):
I've fiddled around with it but I can't get it to return anything except `none`.

#### [Edward Ayers (Oct 09 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.is_internal_cnstr/near/135479658):
In the C++ it looks like it's just checking if the expr is a constant and checking that the name of the constant ends with `_cnstr`. What would be an example of that?

#### [Edward Ayers (Oct 09 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.is_internal_cnstr/near/135480278):
Also `get_nat_value`, extracts a nat from a "nat value macro". But I can't see where nat value macros are used.

#### [Edward Ayers (Oct 09 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.is_internal_cnstr/near/135480811):
What do I need to do to get rid of the `failed to synthesize type class instance for ⊢ reflected e` error?
```lean
universes u v
def e := Π a : Type u, Π b : Type v, a × b
#check e
#eval to_string $ expr.collect_univ_params $ `(e)
```

#### [Simon Hudon (Oct 09 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.is_internal_cnstr/near/135493468):
I think `is_internal_cnstr` will rarely give you an answer. When it does, your expression will likely give you a bunch of trouble and that's why I wrote `tactic.pis` in mathlib to replace `expr.pis`.

#### [Simon Hudon (Oct 09 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr.is_internal_cnstr/near/135493562):
```quote
What do I need to do to get rid of the `failed to synthesize type class instance for ⊢ reflected e` error?
```lean
universes u v
def e := Π a : Type u, Π b : Type v, a × b
#check e
#eval to_string $ expr.collect_univ_params $ `(e)
```
```
I don't know if there is a `reflected` instance for types in general. You may have to go through `to_expr`

