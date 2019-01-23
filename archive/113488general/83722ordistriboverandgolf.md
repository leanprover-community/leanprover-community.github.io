---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83722ordistriboverandgolf.html
---

## Stream: [general](index.html)
### Topic: [or distrib over and golf](83722ordistriboverandgolf.html)

---

#### [Kevin Buzzard (Oct 18 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136067247):
A student just asked me this:

```lean
example (P Q R : Prop) : P ∨ (Q ∧ R) ↔ (P ∨ Q) ∧ (P ∨ R) := sorry
```

They proved it in 60 lines :-) I said that there were probably quicker proofs. How quick can we get it?

#### [Chris Hughes (Oct 18 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136067269):
`by finish`

#### [Sebastien Gouezel (Oct 18 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136067327):
`by tauto` (one letter less)

#### [Kevin Buzzard (Oct 18 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136067345):
I couldn't get finish to work :-/

#### [Kevin Buzzard (Oct 18 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136067349):
But I got `or_and_distrib_left` to work :-)

#### [Rob Lewis (Oct 18 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136067355):
`finish` doesn't work for me, but `split; finish` does.

#### [Chris Hughes (Oct 18 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136067468):
```lean
example (P Q R : Prop) : P ∨ (Q ∧ R) ↔ (P ∨ Q) ∧ (P ∨ R) :=
⟨λ h, h.elim (λ h, ⟨or.inl h, or.inl h⟩) (λ h, ⟨or.inr h.1, or.inr h.2⟩),
  λ h, h.1.elim or.inl (λ hQ, h.2.elim or.inl (λ hR, or.inr ⟨hQ, hR⟩))
```

#### [Scott Olson (Oct 18 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136072685):
If one didn't want to use a high level tactic, I'm fond of pattern matching for this style of "take it apart and put it back together in another shape" proof:

```lean
lemma ltr {P Q R : Prop} : P ∨ (Q ∧ R) → (P ∨ Q) ∧ (P ∨ R)
| (or.inl hp) := ⟨or.inl hp, or.inl hp⟩
| (or.inr ⟨hq, hr⟩) := ⟨or.inr hq, or.inr hr⟩

lemma rtl {P Q R : Prop} : (P ∨ Q) ∧ (P ∨ R) → P ∨ (Q ∧ R)
| ⟨or.inl hp, _⟩ := or.inl hp
| ⟨_, or.inl hp⟩ := or.inl hp
| ⟨or.inr hq, or.inr hr⟩ := or.inr ⟨hq, hr⟩

example {P Q R : Prop} : P ∨ (Q ∧ R) ↔ (P ∨ Q) ∧ (P ∨ R) :=
iff.intro ltr rtl
```

#### [Scott Olson (Oct 18 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136072824):
This isn't exactly golfing it, but I find it really clear for proofs that are merely reorganizing "data"

#### [Kevin Buzzard (Oct 19 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136075871):
Thanks for all of these -- I believe the student is a learner and is reading the answers so it's great to see the options which are available

