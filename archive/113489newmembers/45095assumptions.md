---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/45095assumptions.html
---

## Stream: [new members](index.html)
### Topic: [assumptions](45095assumptions.html)

---

#### [Geoffrey Yeung (Jan 21 2019 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156558856):
is there something similar to ``meta def assumptions : tactic unit := `[ repeat { assumption } ]`` somewhere in the library?

#### [Chris Hughes (Jan 21 2019 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156560625):
`; assumption`

#### [Bryan Gin-ge Chen (Jan 21 2019 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156561395):
What about `assumption'`?

#### [Wojciech Nawrocki (Jan 21 2019 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156562900):
Isn't `; assumption`, which applies once to every goal different from `repeat {assumption}`, which applies until it fails? `assumption'` also seems to do the former

#### [Geoffrey Yeung (Jan 21 2019 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156563787):
I just learned about `;`. In mosts cases I can replace `assumptions` with `; assumption`, but in a few places I need `; try {assumption}` instead, because some branches need furthur processing

#### [Rob Lewis (Jan 21 2019 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156563836):
`assumption` fails when the goal can't be closed by something in the local context. So `repeat {assumption}` will close the first goals until it finds one that can't be closed. `; assumption` will succeed if every subgoal produced by the previous tactic can be closed by `assumption`, and fail otherwise. `assumption'` will close all open goals that can be closed by `assumption`, and fail if none of them can be closed.

#### [Rob Lewis (Jan 21 2019 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156563928):
They're all subtly different. But I guess `repeat {assumption}` is rarely the one you want.

#### [Geoffrey Yeung (Jan 21 2019 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156564007):
yeah `assumption'` seems to be the solution

#### [Rob Lewis (Jan 21 2019 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156564011):
`; assumption'` should have the same effect as `; try {assumption}`.

#### [Geoffrey Yeung (Jan 21 2019 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156564038):
side question: why does
`example {a b c : Prop} : a → b → c → (a ∧ b) ∧ c := by { intros , repeat{ split } ; assumption }` work, but
`example {a b c : Prop} : a → b → c → (a ∧ b) ∧ c := by { intros , split , split ; assumption }` doesn't?

#### [Geoffrey Yeung (Jan 21 2019 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156564127):
oh never mind figured it out, the `;` is only applying to the second split

