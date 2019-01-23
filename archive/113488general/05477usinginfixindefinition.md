---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05477usinginfixindefinition.html
---

## Stream: [general](index.html)
### Topic: [using infix in definition](05477usinginfixindefinition.html)

---

#### [Minchao Wu (Mar 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20infix%20in%20definition/near/124004353):
I remember that in Lean 2 we could use `infix` inside a definition, referring  to the thing being defined.
Is this implemented in the latest master branch?

#### [Mario Carneiro (Mar 21 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20infix%20in%20definition/near/124004476):
I don't think there is anything like that

#### [Sebastian Ullrich (Mar 21 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20infix%20in%20definition/near/124004526):
```
inductive sub : env → type → type → Prop
  notation e ` ⊢ `:40 a ` <: `:40 b:40 := sub e a b
| ...
```

#### [Sebastian Ullrich (Mar 21 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20infix%20in%20definition/near/124004527):
The only change is the removal of `:=` after the type

#### [Minchao Wu (Mar 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20infix%20in%20definition/near/124004632):
Worked for me! Thanks Sebastian and Mario.

#### [Mario Carneiro (Mar 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20infix%20in%20definition/near/124004639):
Wait, does that work for `def` as well? I thought it only worked in `inductive` and `structure`

#### [Minchao Wu (Mar 21 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20infix%20in%20definition/near/124004662):
My bad, I should have said `inductive` definitions

