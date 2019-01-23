---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/50755ContrapositionProof.html
---

## Stream: [new members](index.html)
### Topic: [Contraposition Proof](50755ContrapositionProof.html)

---

#### [Cameron Crossman (Dec 04 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Contraposition%20Proof/near/150809932):
I am a new user and I am just getting my bearings with the platform.  Would someone be able to walk me through a proof of Contraposition written in Lean? (p → q) → (¬q → ¬p). Much appreciated!  I know the general steps but am getting confused about how to translate that into Lean.
(p → q)
¬(p ^ ¬q)
¬( ¬q ^ p)
r = ¬q, s = ¬p substitution
¬(r ^ ¬s )
(r → s)
substitute back in
¬q → ¬p

#### [Kevin Buzzard (Dec 04 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Contraposition%20Proof/near/150810178):
In tactic mode? If you keep using the `intro` tactic you will find yourself with hypotheses `p->q`, `not q` and `p` and with a goal of `false`. Now apply your hypotheses until you're done. Sorry, on phone and just off to bed, hope this helps

#### [Mario Carneiro (Dec 04 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Contraposition%20Proof/near/150813490):
Lean's logic is similar to natural deduction, where `¬p` means `p -> false` so the proof is actually a lot easier than the one you sketched

#### [Bryan Gin-ge Chen (Dec 04 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Contraposition%20Proof/near/150816360):
[Here's the proof in lean core](https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/logic.lean#L34), called "mt" for "modus tollens".

#### [Cameron Crossman (Dec 04 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Contraposition%20Proof/near/150816560):
Thank you!

