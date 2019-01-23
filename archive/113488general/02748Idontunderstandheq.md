---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02748Idontunderstandheq.html
---

## Stream: [general](index.html)
### Topic: [I don't understand heq](02748Idontunderstandheq.html)

---

#### [Kevin Buzzard (Apr 14 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125071940):
Here's a self-contained extract from `analysis/topology/topological.space_lean`:

#### [Kevin Buzzard (Apr 14 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125071981):
```lean
import analysis.topology.topological_space
open topological_space
universes u v w
variables {α : Type u} {β : Type v} {ι : Sort w} {a a₁ a₂ : α} {s s₁ s₂ : set α} {p p₁ p₂ : α → Prop}
variables [topological_space α]

lemma is_open_Union_orig {f : ι → set α} (h : ∀i, is_open (f i)) : is_open (⋃i, f i) :=
is_open_sUnion $ assume t ⟨i, (heq : t = f i)⟩, heq.symm ▸ h i

lemma is_open_Union' {f : ι → set α} (h : ∀i, is_open (f i)) : is_open (⋃i, f i) :=
begin
  refine is_open_sUnion _,
  intro t,
  intro Ht,
  cases Ht with i Hi,
  exact eq.symm Hi ▸ h i,
end 

lemma is_open_Union'' {f : ι → set α} (h : ∀i, is_open (f i)) : is_open (⋃i, f i) :=
is_open_sUnion $ assume t ⟨i, (rfl : t = f i)⟩, eq.symm ▸ h i -- doesn't compile
```

#### [Kevin Buzzard (Apr 14 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125071983):
well, the first lemma is the extract -- it's called `is_open_Union` in the actual file.

#### [Kevin Buzzard (Apr 14 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125071988):
I should perhaps say `lemma is_open_sUnion {s : set (set α)} (h : ∀t ∈ s, is_open t) : is_open (⋃₀ s)`

#### [Kevin Buzzard (Apr 14 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125071992):
So I realised I didn't really understand the mathlib proof of `is_open_Union_orig` (which is the proof given in the extract above, with its `heq`)

#### [Kevin Buzzard (Apr 14 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072033):
so I proved the lemma "in the same way", in tactic mode

#### [Kevin Buzzard (Apr 14 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072034):
and that's `is_open_Union'`

#### [Kevin Buzzard (Apr 14 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072035):
and everything works fine with eq

#### [Kevin Buzzard (Apr 14 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072043):
Oh -- got it:

#### [Kevin Buzzard (Apr 14 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072045):
```lean
lemma is_open_Union'' {f : ι → set α} (h : ∀i, is_open (f i)) : is_open (⋃i, f i) :=
is_open_sUnion $ assume t ⟨i, (eq : t = f i)⟩, eq.symm ▸ h i
```

#### [Kevin Buzzard (Apr 14 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072085):
What's with this `heq` in the mathlib version?

#### [Kevin Buzzard (Apr 14 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072130):
Oh!

#### [Kevin Buzzard (Apr 14 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072131):
Got it :-)

#### [Kevin Buzzard (Apr 14 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072132):
`heq` has nothing to do with `heq`, it's just a variable name :-)

#### [Kevin Buzzard (Apr 14 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072138):
Oh OK, so I do understand this particular use of heq, we're calling a variable by the same name as a Lean function :-)

