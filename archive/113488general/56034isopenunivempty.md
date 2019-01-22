---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56034isopenunivempty.html
---

## [general](index.html)
### [is_open_{univ,empty}](56034isopenunivempty.html)

#### [Johan Commelin (Dec 04 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open_{univ,empty}/near/150866118):
Is there a reason for the following discrepancy?
```lean
#print is_open_univ
/- @[reducible]
def topological_space.is_open_univ : ∀ {α : Type u} (c : topological_space α), is_open c univ :=
λ (α : Type u) (c : topological_space α), [topological_space.is_open_univ c] -/
#print is_open_empty
/- @[simp]
theorem is_open_empty : ∀ {α : Type u} [_inst_1 : topological_space α], is_open ∅ :=
λ {α : Type u} [_inst_1 : topological_space α],
  eq.mpr (id (eq.rec (eq.refl (is_open ∅)) (eq.symm sUnion_empty))) (is_open_sUnion (λ (a : set α), false.elim)) -/
```

#### [Reid Barton (Dec 04 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open_{univ,empty}/near/150866186):
You have the wrong `is_open_univ` I think

#### [Reid Barton (Dec 04 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open_{univ,empty}/near/150866213):
You probably want the root namespace one

#### [Johan Commelin (Dec 04 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open_{univ,empty}/near/150866296):
Aahrg, I see.

#### [Johan Commelin (Dec 04 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open_{univ,empty}/near/150866331):
Otoh, because of proof irrelevance it doesn't really matter which one I'm using, I guess.

#### [Reid Barton (Dec 04 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open_{univ,empty}/near/150866363):
I assumed you were concerned about the type: `()` vs `[]`

#### [Johan Commelin (Dec 04 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open_{univ,empty}/near/150866808):
Yes, I was.

#### [Johan Commelin (Dec 04 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_open_{univ,empty}/near/150866893):
There is all sorts of asymmetry. But using the `_root_` version solves all my headaches (-;

