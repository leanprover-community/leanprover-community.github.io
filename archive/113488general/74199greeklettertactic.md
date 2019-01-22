---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74199greeklettertactic.html
---

## [general](index.html)
### [greek letter tactic](74199greeklettertactic.html)

#### [Patrick Massot (May 28 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127201952):
Is there a tactic doing only that greek letter which transforms `(λ  a, f a) x` to `f x`?

#### [Andrew Ashworth (May 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127202121):
I think `dsimp` with one of its special options does it, but I don't remember exactly what it is

#### [Kenny Lau (May 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127202123):
that's eta reduction

#### [Kenny Lau (May 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127202126):
no

#### [Andrew Ashworth (May 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127202127):
beta

#### [Kenny Lau (May 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127202128):
that's delta reduction

#### [Kenny Lau (May 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127202129):
oh

#### [Kenny Lau (May 28 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127202131):
beta it is then

#### [Patrick Massot (May 28 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127202136):
I say alpha!

#### [Kenny Lau (May 28 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127202143):
no, that's also eta reduction

#### [Patrick Massot (May 28 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127202148):
We need printable DTT cheat sheets

#### [Kenny Lau (May 28 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127202151):
it's not even DTT

#### [Kenny Lau (May 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127202391):
```lean
-- (λ (a : X), f a) x = f x
example : (λ a, f a) x = f x :=
by dsimp { eta := false, beta := false }

-- (λ (a : X), f a) x = f x
example : (λ a, f a) x = f x :=
by dsimp { eta := true, beta := false }

-- f x = f x
example : (λ a, f a) x = f x :=
by dsimp { eta := false, beta := true }
```

#### [Kenny Lau (May 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127202394):
why isn't it eta?

#### [Kenny Lau (May 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127202400):
@**Andrew Ashworth**

#### [Andrew Ashworth (May 28 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127202649):
i don't know how dsimp does it, but I remember it as eta is the sorta useless thing that turns `lam x, f x --> f`, while beta is `(lam x, f x) y --> f y`

#### [Andrew Ashworth (May 28 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127202697):
basically eta only cleans up useless lambdas

#### [Reid Barton (May 28 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127213902):
An amazing feature I only discovered recently: `set_option pp.beta true` will hide those useless `(λ a, f a) x` in displayed types

#### [Chris Hughes (May 28 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127214374):
The slightly annoying thing about that is sometimes it won't rewrite because it's not reduced, and you get frustrated trying to work out why.

#### [Kevin Buzzard (May 28 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek letter tactic/near/127222466):
You need to set pp.beta true in rw as well :-)

