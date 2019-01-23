---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08893setindefinitedescription.html
---

## Stream: [general](index.html)
### Topic: [set.indefinite_description](08893setindefinitedescription.html)

---

#### [Kenny Lau (Dec 04 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150884816):
Is it possible to fill in this sorry?
```lean
universes u
protected def set.indefinite_description {α : Type u}
  {p : set α → Prop} (h : ∃ s, p s) : { s : set α // p s} := sorry
```

#### [Reid Barton (Dec 04 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150885388):
I guess you mean without adding `noncomputable`? Interesting question

#### [Mario Carneiro (Dec 05 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150890461):
yes
```lean
universes u
protected def set.indefinite_description {α : Type u}
  {p : set α → Prop} (h : ∃ s, p s) : { s : set α // p s} :=
⟨{x : α | x ∈ classical.some h}, classical.some_spec h⟩
```

#### [Mario Carneiro (Dec 05 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150890503):
I've mentioned before about "trivially computable" types, which includes subtypes of functions returning Prop

#### [Mario Carneiro (Dec 05 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150890525):
Any term of such a type can be made computable with appropriate wrapping

#### [Mario Carneiro (Dec 05 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150890612):
If you meant "without axioms", then no it's not possible, it would imply the axiom of choice

#### [Mario Carneiro (Dec 05 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150890927):
However there is an interesting construction here for *definite* description with no axioms (well extensionality)
```lean
import data.set.basic

universes u
protected def set.definite_description {α : Type u}
  {p : set α → Prop} (h : ∃! s, p s) : { s : set α // p s} :=
⟨{x : α | ∃ s, x ∈ s ∧ p s ∧ ∀ y, p y → y = s},
let ⟨s, ps, al⟩ := h in
have s = {x : α | ∃ s, x ∈ s ∧ p s ∧ ∀ y, p y → y = s},
from set.ext $ λ x, ⟨λ xs, ⟨_, xs, ps, al⟩,
  λ ⟨s', xs', ps', al'⟩, (al' _ ps).symm ▸ xs'⟩,
this ▸ ps⟩
```

#### [Kenny Lau (Dec 05 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150891656):
@**Mario Carneiro** so... we can have a "computable" basis?

#### [Mario Carneiro (Dec 05 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150891676):
"computable" but not computable

#### [Mario Carneiro (Dec 05 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150891740):
when I revisited bases recently, we discussed changing the definition of a basis from a set to a family over a type. In that case it wouldn't be computationally irrelevant

