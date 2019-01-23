---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/52031doublenegationimpliesexcludedmiddle.html
---

## Stream: [new members](index.html)
### Topic: [double negation implies excluded middle??](52031doublenegationimpliesexcludedmiddle.html)

---

#### [Shaun Steenkamp (Nov 07 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/double%20negation%20implies%20excluded%20middle%3F%3F/near/146927399):
In section "3.5 Classical Logic" it says that "As an exercise, you might try proving the converse, that is, showing that em can be proved from dne." Can someone give me a proof of this in Lean without using open classical?

#### [Mario Carneiro (Nov 07 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/double%20negation%20implies%20excluded%20middle%3F%3F/near/146927466):
hint: use it right at the start. That is, `¬ ¬ (p ∨ ¬ p)` is provable outright

#### [Mario Carneiro (Nov 07 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/double%20negation%20implies%20excluded%20middle%3F%3F/near/146927540):
hint 2: try to prove `¬ p` from the assumption `¬ (p ∨ ¬ p)`

#### [Rob Lewis (Nov 07 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/double%20negation%20implies%20excluded%20middle%3F%3F/near/146927544):
Notice that Jeremy also gave you a hint here: https://github.com/leanprover/theorem_proving_in_lean/issues/67

#### [Rob Lewis (Nov 07 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/double%20negation%20implies%20excluded%20middle%3F%3F/near/146927545):
(The same hint Mario is giving. :slight_smile: )

#### [Shaun Steenkamp (Nov 07 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/double%20negation%20implies%20excluded%20middle%3F%3F/near/146929907):
Okay, I got it! I had to try it in Agda first because I'm still not really familiar with the syntax of Lean

#### [Shaun Steenkamp (Nov 07 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/double%20negation%20implies%20excluded%20middle%3F%3F/near/146929913):
Thanks for your help!

