---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96918rewritingclassoperations.html
---

## [general](index.html)
### [rewriting class operations](96918rewritingclassoperations.html)

#### [Reid Barton (Jun 05 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127602788):
I have this instance:
```lean
instance Xplus.setoid : setoid Xplus :=
⟨Xplus_rel, Xplus_rel.refl, Xplus_rel.symm, Xplus_rel.trans⟩
```
How can I use a tactic to rewrite `a ≈ b` somewhere in the goal to `Xplus_rel a b`?

#### [Reid Barton (Jun 05 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127602900):
Is there some name I can pass to `rw` or `simp`?

#### [Kenny Lau (Jun 05 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127602930):
`set_option pp.notations false`

#### [Simon Hudon (Jun 05 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127602986):
Does `change Xplus_rel a b` do it for you?

#### [Sebastian Ullrich (Jun 05 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127603021):
`simp [(≈)]` should do it

#### [Reid Barton (Jun 05 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127603023):
`change` works if I write out the whole new goal (which isn't bad at all using copious `_`s)

#### [Reid Barton (Jun 05 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127603087):
`simp [(≈)]` turned it into `setoid.r`, not `Xplus_rel`

#### [Reid Barton (Jun 05 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127603093):
Oh, but `[(≈), setoid.r]` worked

#### [Kenny Lau (Jun 05 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127603099):
`≈` is literally `setoid.r`

#### [Reid Barton (Jun 05 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127603112):
No, it's literally `has_equiv.equiv`

#### [Kenny Lau (Jun 05 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127603118):
oh

#### [Reid Barton (Jun 05 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127603181):
Great, this is better than what I had before. I feel like I run into this a lot

#### [Chris Hughes (Jun 05 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127604658):
I often use `show Xplus_rel a b` in these situtations.

#### [Simon Hudon (Jun 05 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127604971):
That's similar to `change` but @**Reid Barton** pointed out that that only works if there's nothing else in your goal.

#### [Chris Hughes (Jun 05 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127605892):
`show Xplus_rel _ _`

#### [Simon Hudon (Jun 05 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127606006):
That doesn't work if the goal is `p ∧ Xplus_rel a b`

#### [Kenny Lau (Jun 05 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127606012):
`split`

#### [Simon Hudon (Jun 05 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127606149):
This is an ad hoc response to it. @**Reid Barton** Is looking for one solution that will work for a variety of goals

#### [Reid Barton (Jun 05 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting class operations/near/127606159):
And won't get longer the longer my goal is

