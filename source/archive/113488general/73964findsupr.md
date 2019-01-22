---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73964findsupr.html
---

## [general](index.html)
### [find supr](73964findsupr.html)

#### [Johan Commelin (Nov 09 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20supr/near/147368449):
I have found
```lean
@[simp] lemma supr_pos {p : Prop} {f : p → α} (hp : p) : (⨆ h : p, f h) = f hp :=
le_antisymm (supr_le $ assume h, le_refl _) (le_supr _ _)
```
in the library. I would like to have
```lean
lemma supr_xyzzy {p : Prop} {f : p → α} (hp : p) : (⨆ h : p, f h) ≤ f hp := sorry
```
I have never succesfully used find. Somehow it just doesn't give me any results. What should I type into VScode to find this lemma? (Assuming it is there...)

#### [Johan Commelin (Nov 09 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20supr/near/147372143):
Ok, I've figured out that I should just use `supr_le` for this one.

#### [Johan Commelin (Nov 09 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20supr/near/147372222):
Here is another one. Should there be a lemma called `mem_of_mem_supr`?
It would state that if `x ∈ ⊔s ∈ S, s` then there is an `s ∈ S` such that `x ∈ s`.

