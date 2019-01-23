---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/28135cleardenominator.html
---

## Stream: [maths](index.html)
### Topic: [clear_denominator](28135cleardenominator.html)

---

#### [Patrick Massot (May 30 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127303903):
Let's start a new thread about this

#### [Patrick Massot (May 30 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127303917):
It's a dream about a tactic called `clear_denominator`

#### [Patrick Massot (May 30 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127303920):
Assume the current goal is either an equality or an inequality

#### [Patrick Massot (May 30 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127303973):
It has a bunch of +, -, *, /, maybe • (scalar multiplication)

#### [Patrick Massot (May 30 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127303979):
we want to get rid of all divisions

#### [Patrick Massot (May 30 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127303981):
the tactic walks through the goal and builds a list of all denominators (right-hand argument of a /)

#### [Patrick Massot (May 30 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127304035):
It creates sub-goals `x ≠ 0` for all denominators `x`, and immediately tries to discharge them by `assumption` or applying `ne_of_gt` or `ne_of_lt` to all assumptions

#### [Patrick Massot (May 30 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127304043):
then it multiplies both sides of the goal by the product of all denominators, using the relevant lemmas (assuming the subgoals)

#### [Patrick Massot (May 30 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127304095):
and then simplifies the goal to get rid of divisions by using `x/x = 1`

#### [Patrick Massot (May 30 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127304100):
Of course nested divisions would be problematic

#### [Patrick Massot (May 30 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127304107):
The Cauchy-Schwarz thread is an example where you could use this

#### [Assia Mahboubi (May 30 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127304282):
The inequality case is more difficult because of sign conditions, isn't it? But even in the equality case, the size of the formula to be proved can become quite large. Coq has a ``field`` tactic, built on top of ``ring``, that does about the same thing as what you describe I think.

#### [Patrick Massot (May 30 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127304898):
Indeed signs matter in inequalities

#### [Patrick Massot (May 30 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127304904):
And we clearly need this field tactic (but Mario always want us to suffer instead of using automation)

#### [Assia Mahboubi (May 30 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127306985):
The ``field`` problem is more difficult than the ``ring`` one. It probably has to start as a partial procedure, like the one you describe, because a complete one is much more delicate from an algorithmic point of view (you need stuff like subresultants or even may be probabilistic methods otherwise the complexity and growth of the polynomials are dreadful).

