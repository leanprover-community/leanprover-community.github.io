---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90874Cannotfindinstance.html
---

## [general](index.html)
### [Cannot find instance](90874Cannotfindinstance.html)

#### [AHan (Dec 04 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cannot find instance/near/150826554):
In `mathlib/data/finsupp.lean` the instance `has_add` of `finsupp` structure was already proved,
but in t he following example, it failed to synthesize type class instance for `has_add`...
Don't understand what instance I missed...

```lean
import data.finsupp
variables {α : Type*} {β : Type*} [has_zero α] [has_zero β] [add_monoid α] [add_monoid β] 
variables [decidable_eq α] [decidable_eq β]

lemma support_contain_a' (a b : α →₀ β) : a.support ⊆ (a + b).support := sorry
```

