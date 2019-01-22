---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/64217addcommgrouptactic.html
---

## [maths](index.html)
### [add_comm_group tactic](64217addcommgrouptactic.html)

#### [Patrick Massot (Aug 08 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120526):
Could we get a scaled down `ring` tactic handling `add_comm_group`? My current goal is `φ (x', y') - φ (x, y) =   φ (x', y₁) - φ (x, y₁) + (φ (x', y') - φ (x', y₁) - (φ (x, y') - φ (x, y₁))) + (φ (x₁, y') - φ (x₁, y)) + (φ (x, y') - φ (x, y) - (φ (x₁, y') - φ (x₁, y)))` and I can't face proving it by hand

#### [Mario Carneiro (Aug 08 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120596):
it's on the todo list

#### [Patrick Massot (Aug 08 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120597):
(this is a generalization of the thing I called a `ring` bug the other day because I forgot to tell Lean rings are commutative)

#### [Kevin Buzzard (Aug 08 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120730):
Why not put a ring structure on your group? ;-)

#### [Kevin Buzzard (Aug 08 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120750):
I think once someone showed me a group for which they could prove that this could not be done, unfortunately.

#### [Mario Carneiro (Aug 08 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120759):
I think I know how to do modules; maybe you could use that

#### [Kevin Buzzard (Aug 08 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120813):
Oh yeah, Q/Z. No possibility for 1 because it would be killed by some n, but not everything is killed by n

#### [Mario Carneiro (Aug 08 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120860):
any non-unital ring satisfies this criterion

#### [Mario Carneiro (Aug 08 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120979):
oh, actually I think you stand to gain just a bit by using a module tactic to solve abelian group problems

#### [Patrick Massot (Aug 08 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131120989):
It makes me think I should try the `rcases_hint` tactic now that you pushed it

#### [Mario Carneiro (Aug 08 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131121036):
since it would be able to handle `(m * n) . x = m . (n . x)` where m,n : Z

#### [Mario Carneiro (Aug 08 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131121042):
but a standard abelian group tactic can't deal with Z variables

#### [Mario Carneiro (Aug 08 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131121067):
You should definitely try `rcases_hint`. I wrote 200 lines of lean in one sitting and tested it once at the end, and it seemed to work

#### [Mario Carneiro (Aug 08 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131121113):
...at least it's type correct

#### [Johan Commelin (Aug 08 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131121736):
Unfortunately, `add_comm_group` is not the same as `module \Z`

#### [Mario Carneiro (Aug 08 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131121833):
that's not a significant problem for a tactic, it can supply the instance when needed

#### [Mario Carneiro (Aug 08 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131121859):
speaking of which, someone should prove that instance. All the hard work is already done

#### [Patrick Massot (Aug 08 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131123895):
I can't use the depth parameter

#### [Mario Carneiro (Aug 08 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131123968):
The syntax is `rcases_hint e {depth := 4}` or `rintro_hint {depth := 4}`

#### [Mario Carneiro (Aug 08 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131123979):
the lack of delimiter between `e` and the cfg may cause a problem

#### [Patrick Massot (Aug 08 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131123982):
it complains `e` is not a function

#### [Patrick Massot (Aug 08 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131123992):
so yes, a delimiter may help

#### [Mario Carneiro (Aug 08 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131123998):
I'm open to suggestions

#### [Mario Carneiro (Aug 08 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131124080):
would `rcases_hint e : 4` be too weird?

#### [Patrick Massot (Aug 08 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131124093):
it's not meant to stay in the final Lean file anyway

#### [Patrick Massot (Aug 08 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131124101):
so I would say it's fine

#### [Patrick Massot (Aug 08 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131124410):
What about trying to guess better names?

#### [Johan Commelin (Aug 08 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131125303):
```quote
speaking of which, someone should prove that instance. All the hard work is already done
```
Do we want an actual `instance`, or just 2 lemmas that convert either way. I think we can't have instances both ways, right? That would blow up the type class system :boom:

#### [Mario Carneiro (Aug 08 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131125618):
We already have an instance one way, the other one should just be a def

#### [Mario Carneiro (Aug 08 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131125639):
I changed `rcases_hint` to `rcases?`, `hint`  takes too long to write

#### [Mario Carneiro (Aug 08 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131125657):
the depth thing should be fixed

#### [Patrick Massot (Aug 08 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131131422):
```quote
My current goal is `φ (x', y') - φ (x, y) =   φ (x', y₁) - φ (x, y₁) + (φ (x', y') - φ (x', y₁) - (φ (x, y') - φ (x, y₁))) + (φ (x₁, y') - φ (x₁, y)) + (φ (x, y') - φ (x, y) - (φ (x₁, y') - φ (x₁, y)))` and I can't face proving it by hand
```
This was the last missing piece, so I decided to try it. After about 15 minutes of misery, I found out that `apply eq_of_sub_eq_zero, simp` does the trick!

#### [Kevin Buzzard (Aug 08 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131133991):
```quote
Unfortunately, `add_comm_group` is not the same as `module \Z`
```
OK so in the perfectoid mathlib pile-up there is `quotient_group.lean`, which I wrote based on `quotient_module.lean`. But what I actually want is `quotient_add_group.lean` so I can use it to improve `quotient_ring.lean`. I see three possibilities for making `quotient_add_group.lean` : 

(1) just copy `quotient_group.lean` changing all the `*`s to `+`s etc. 

(2) Some sort of tactic magic

(3) *deduce* the results from `quotient_module.lean` using the fact that, as we mathematicians say, an abelian group "is" a $$\mathbb{Z}$$-module.

Which is the best idea?

@**Patrick Massot** Do you mind if I put our names on the top of `quotient_group.lean` (remember -- I wrote it, basically copying from `quotient_module.lean` and then you fixed up a bunch of stuff and made it better) and PR it to mathlib via the community mathlib?

#### [Patrick Massot (Aug 08 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/add_comm_group%20tactic/near/131134156):
No problem, go ahead

