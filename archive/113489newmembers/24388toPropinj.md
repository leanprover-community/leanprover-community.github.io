---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/24388toPropinj.html
---

## [new members](index.html)
### [to_Prop_inj](24388toPropinj.html)

#### [Kenny Lau (Jan 11 2019 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/to_Prop_inj/near/154908038):
```lean
lemma to_Prop_inj : Π {a b : bool} (H : (a : Prop) ↔ (b : Prop)), a = b
| a tt H := H.2 rfl
| a ff H := bool.eq_ff_of_ne_tt $ λ h, absurd (H.1 h) dec_trivial
```

#### [Kenny Lau (Jan 11 2019 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/to_Prop_inj/near/154908043):
@**Mario Carneiro** is this currently in mathlib?

