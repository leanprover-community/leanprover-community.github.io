---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90904quotmkvsquotientmk.html
---

## [general](index.html)
### [quot.mk vs quotient.mk](90904quotmkvsquotientmk.html)

#### [Patrick Massot (Dec 17 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quot.mk vs quotient.mk/near/152047620):
Do we already have `lemma quot_mk_quotient_mk {α :Type*} [setoid α] (a : α) : quot.mk setoid.r a = ⟦a⟧ := rfl`? I need this because `rintro` typically produces the left-hand side.

