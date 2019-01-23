---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/28866Stronginductioninlean.html
---

## Stream: [new members](index.html)
### Topic: [Strong induction in lean](28866Stronginductioninlean.html)

---

#### [Calle Sönne (Nov 19 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Strong%20induction%20in%20lean/near/147975900):
I want to prove strong induction in lean but Im having a hard time writing it out. Is it possible to do and-statements of variable length in lean? Something like this is what I want to do in lean:
```lean
theorem strong_induction (P : ℕ → Prop) (H0 : P 0) (Hn : ∀ 
    (n : ℕ), P 1 ∧ P 2 ∧ ... ∧ P n → P (n+1)) : ∀ m : ℕ, P m := sorry
```
or maybe like this if that's possible:
```lean
theorem strong_induction' (P : ℕ → Prop) (H0 : P 0) (Hn : ∀ 
    (n : ℕ), P s → P (n+1), ∀ (s:ℕ) (Hs : s ≤ n) : ∀ m : ℕ, P m := sorry
```

#### [Rob Lewis (Nov 19 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Strong%20induction%20in%20lean/near/147976238):
You might want to look at `nat.strong_induction_on` and `nat.case_strong_induction_on`, which follow the pattern of your second example.

#### [Kevin Buzzard (Nov 19 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Strong%20induction%20in%20lean/near/147980492):
`theorem strong_induction (P : ℕ → Prop) (H : ∀ n : ℕ, (∀ m : ℕ, m < n → P m) → P n) (n : ℕ) : P n := sorry` would be the way I'd formalise it.

#### [Kevin Buzzard (Nov 19 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Strong%20induction%20in%20lean/near/147980545):
Note that the devious case `H 0` says that if something is true for all elements of the empty set, then `P 0` follows, which is a trick I mentioned in lectures. There is something called "well-founded induction" which works on any set with a well-founded ordering -- for example the naturals, but also many other ordered sets.

#### [Calle Sönne (Nov 19 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Strong%20induction%20in%20lean/near/147984947):
Ah forgot about that trick, thank you!

