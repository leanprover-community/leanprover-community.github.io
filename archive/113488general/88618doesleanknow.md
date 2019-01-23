---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88618doesleanknow.html
---

## Stream: [general](index.html)
### Topic: [does lean know?](88618doesleanknow.html)

---

#### [Sean Leather (Mar 01 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/does%20lean%20know%3F/near/123130945):
Is this in the standard library or mathlib?
```lean
theorem if_distrib {c : Prop} [decidable c] {α β : Type} {f : α → β} {a b : α}:
  f (if c then a else b) = if c then f a else f b :=
by by_cases h : c; [simp [if_pos h], simp [if_neg h]]
```

#### [Sean Leather (Mar 01 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/does%20lean%20know%3F/near/123131013):
@**Kenny Lau**: FYI, the topic title is in homage to your questions. :simple_smile:

#### [Kenny Lau (Mar 01 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/does%20lean%20know%3F/near/123131018):
:D

