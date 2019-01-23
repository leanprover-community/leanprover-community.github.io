---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/23264noobquestionaboutcardinal.html
---

## Stream: [new members](index.html)
### Topic: [noob question about cardinal](23264noobquestionaboutcardinal.html)

---


{% raw %}
#### [ Kenny Lau (Sep 13 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%20about%20cardinal/near/133871212):
```lean
import set_theory.cardinal

example (α : Type*) (S T : set α)
  (HS : set.finite S) (HT : set.finite T)
  (H : finset.card (set.finite.to_finset HS) ≤ finset.card (set.finite.to_finset HT)) :
  cardinal.mk S ≤ cardinal.mk T :=
sorry
```

#### [ Chris Hughes (Sep 13 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%20about%20cardinal/near/133873000):
```lean
open cardinal

example (α : Type*) (S T : set α)
  (HS : set.finite S) (HT : set.finite T)
  (H : finset.card (set.finite.to_finset HS) ≤ finset.card (set.finite.to_finset HT)) :
  cardinal.mk S ≤ cardinal.mk T :=
begin
  haveI := classical.choice HS,
  haveI := classical.choice HT,
  rwa [fintype_card S, fintype_card T, nat_cast_le, 
    set.card_fintype_of_finset' (set.finite.to_finset HS),
    set.card_fintype_of_finset' (set.finite.to_finset HT)];
  simp
end
```

#### [ Kenny Lau (Sep 13 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%20about%20cardinal/near/133873086):
```lean
import set_theory.cardinal

example (α : Type*) (S T : set α)
  (HS : set.finite S) (HT : set.finite T)
  (H : finset.card (set.finite.to_finset HS) ≤ finset.card (set.finite.to_finset HT)) :
  cardinal.mk S ≤ cardinal.mk T :=
begin
  tactic.unfreeze_local_instances,
  cases HS, cases HT,
  rw [cardinal.fintype_card, cardinal.fintype_card, cardinal.nat_cast_le],
  rw [← fintype.card_coe, ← fintype.card_coe] at H,
  convert H;
  { ext z, rw [finset.mem_coe, set.finite.mem_to_finset] }
end

```

#### [ Kenny Lau (Sep 13 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%20about%20cardinal/near/133873150):
anyway why do we need so many lines


{% endraw %}
