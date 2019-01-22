---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/82983rwinsidelambda.html
---

## [general](index.html)
### [rw inside lambda](82983rwinsidelambda.html)

#### [Kenny Lau (Sep 09 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133624964):
from my experience, `simp` can change things inside lambda, but `rw` cannot. Is there a way to bypass this and let `rw` change inside lambda?

#### [Mario Carneiro (Sep 09 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133624971):
`conv` + `rw`

#### [Reid Barton (Sep 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133625661):
Also see topic https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/rw.20under.20lambda/near/126107890 and the more verbose topic https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/Why.20can't.20.60rw.60.20look.20inside.20lambda.20expressions.3F/near/130212033

#### [Kenny Lau (Sep 10 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133640326):
so exactly which tactics are avaiblale inside `conv`?

#### [Kevin Buzzard (Sep 10 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133641348):
rw

#### [Kenny Lau (Sep 10 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133641426):
I mean, a complete list of tactics available inside `conv`

#### [Kevin Buzzard (Sep 10 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133641504):
There's probably a file in core which lists them. There's to_lhs, something called something like whnf and you might want to skim Patrick's docs

#### [Kevin Buzzard (Sep 10 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133641835):
https://github.com/leanprover/lean/blob/master/library/init/meta/converter/interactive.lean

#### [Kevin Buzzard (Sep 10 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133641838):
Maybe that's the definitive answer

#### [Kevin Buzzard (Sep 10 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133641952):
Funext, change, simp and dsimp

#### [Kevin Buzzard (Sep 10 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133642024):
https://github.com/leanprover/mathlib/blob/master/docs/extras/conv.md

#### [Kevin Buzzard (Sep 10 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133642027):
Has a couple of nice tricks

#### [Kenny Lau (Sep 10 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133642625):
well I would like to be able to use `apply/exact/refine` inside `conv`

#### [Kenny Lau (Sep 10 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133642672):
`conv` inside `conv` would also be useful

#### [Kenny Lau (Sep 10 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133642676):
I feel like `conv` has a lot of potential to be the most powerful tactic ever

#### [Kenny Lau (Sep 10 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133644854):
@**Mario Carneiro** I don't understand why there's no basic tactics (i.e. `exact`) inside conv

#### [Mario Carneiro (Sep 10 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645090):
`conv` is a different monad from `tactic`

#### [Mario Carneiro (Sep 10 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645145):
`exact` doesn't even make sense

#### [Kenny Lau (Sep 10 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645146):
I mean, why didn't we implement exact inside conv

#### [Kenny Lau (Sep 10 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645150):
conv is just a bunch of congr_arg and funext right

#### [Mario Carneiro (Sep 10 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645172):
the tactic state in the conv monad is basically `?p : X = ?m` where `?p` and `?m` are to be determined

#### [Kenny Lau (Sep 10 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645178):
if we have `a + b = c + d`, and I do `conv { to_lhs, congr, skip, }` then the current state is `a + b = a + ?m` right

#### [Kenny Lau (Sep 10 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645187):
if I do `exact (sorry : b = foo b)` then I can tell Lean exactly that `?m` should be `foo b` right

#### [Mario Carneiro (Sep 10 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645201):
by comparison to the regular tactic state which is just `?m : t`

#### [Mario Carneiro (Sep 10 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645300):
I think `update_lhs` does that

#### [Johan Commelin (Sep 10 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645375):
I've never heard about that one. Sounds good!

#### [Johan Commelin (Sep 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645390):
Can you also *zoom out* in `conv`?

#### [Johan Commelin (Sep 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645411):
You zoom in with `congr` and `funext`. But I sometimes also want to zoom out again.

#### [Mario Carneiro (Sep 10 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645430):
No, zoom out doesn't make sense

#### [Mario Carneiro (Sep 10 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645496):
what is possible instead is a split lhs/rhs that produces multiple subgoals

#### [Mario Carneiro (Sep 10 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645527):
also, lhs/rhs is so passe. We need rcases patterns in conv!

#### [Kenny Lau (Sep 10 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645626):
what is update_lhs?

#### [Mario Carneiro (Sep 10 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645646):
I guess it is not an interactive command, but it is available as a conv tactic

#### [Mario Carneiro (Sep 10 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645670):
```lean
meta def update_lhs (new_lhs : expr) (h : expr) : conv unit :=
do transitivity,
   rhs >>= unify new_lhs,
   exact h,
   t ← target >>= instantiate_mvars,
   change t
```

#### [Johan Commelin (Sep 10 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645872):
@**Mario Carneiro** Why would zoom out not make sense? If I drill down into a nested sum, do some `rw` there, then I would want to zoom out again and play with the sum that is 1 level up.

#### [Mario Carneiro (Sep 10 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133645979):
As I said, the conv monad has a state which is `?p : X = ?m`. If you zoom in then `?m` is assigned, so you can't return to it any more than you can rewind in a proof

#### [Mario Carneiro (Sep 10 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133646109):
I think that `to_lhs` would make more sense as a tactic combinator, i.e. `to_lhs { <conv> }, <conv>`

#### [Mario Carneiro (Sep 10 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133646119):
that would allow you to return to the outer context in the second part

#### [Kenny Lau (Sep 10 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133646183):
also if I go deep inside using `conv` then all the variables have the same name and I can't even `dedup`

#### [Mario Carneiro (Sep 10 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133646218):
note that `find` is actually a combinator like this inside conv, so you can use it to temporarily zoom in

#### [Mario Carneiro (Sep 10 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20inside%20lambda/near/133646274):
however, find patterns never work the way I want them to

