---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/44024invalidoccurrenceofrecursivearg.html
---

## Stream: [general](index.html)
### Topic: [invalid occurrence of recursive arg](44024invalidoccurrenceofrecursivearg.html)

---


{% raw %}
#### [ Reid Barton (Jan 13 2019 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurrence%20of%20recursive%20arg/near/155020104):
What does this error message mean and is there a workaround?
```lean
universe v
variables {α : Type v}
inductive closure (φ : set α → set α) : α → Prop
| clos : ∀ {t : set α}, (∀ x, t x → closure x) → ∀ x, φ t x → closure x
-- error: invalid occurrence of recursive arg#5 of 'closure.clos', the body of the functional type depends on it.
```

#### [ Reid Barton (Jan 13 2019 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurrence%20of%20recursive%20arg/near/155021253):
I guess I can just use the impredicative definition

#### [ Kenny Lau (Jan 13 2019 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurrence%20of%20recursive%20arg/near/155021376):
what is the impredicative definition?

#### [ Reid Barton (Jan 13 2019 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurrence%20of%20recursive%20arg/near/155021674):
The intersection of all the closed subsets of α

#### [ Reid Barton (Jan 13 2019 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurrence%20of%20recursive%20arg/near/155021995):
`def closure (φ : set α → set α) : set α := ⋂₀ {s | ∀ t, t ⊆ s → φ t ⊆ s}`

#### [ Gabriel Ebner (Jan 13 2019 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurrence%20of%20recursive%20arg/near/155022395):
FTFY:
```lean
inductive closure (φ : set α → set α) : α → Prop
| clos : ∀ {t : set α}, ∀ x, (∀ x, t x → closure x) → φ t x → closure x
```

#### [ Gabriel Ebner (Jan 13 2019 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurrence%20of%20recursive%20arg/near/155022473):
Lean is a bit picky about the order of the arguments to constructors.  A long time ago, you couldn't even write `| node : tree → α → tree → tree` (you had to write `α` at the beginning and not in the middle).

#### [ Reid Barton (Jan 13 2019 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurrence%20of%20recursive%20arg/near/155022542):
Interesting, thanks!


{% endraw %}
