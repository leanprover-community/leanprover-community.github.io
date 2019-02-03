---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/28135cleardenominator.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [clear_denominator](https://leanprover-community.github.io/archive/116395maths/28135cleardenominator.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (May 30 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127303903):
<p>Let's start a new thread about this</p>

#### [ Patrick Massot (May 30 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127303917):
<p>It's a dream about a tactic called <code>clear_denominator</code></p>

#### [ Patrick Massot (May 30 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127303920):
<p>Assume the current goal is either an equality or an inequality</p>

#### [ Patrick Massot (May 30 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127303973):
<p>It has a bunch of +, -, *, /, maybe • (scalar multiplication)</p>

#### [ Patrick Massot (May 30 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127303979):
<p>we want to get rid of all divisions</p>

#### [ Patrick Massot (May 30 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127303981):
<p>the tactic walks through the goal and builds a list of all denominators (right-hand argument of a /)</p>

#### [ Patrick Massot (May 30 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127304035):
<p>It creates sub-goals <code>x ≠ 0</code> for all denominators <code>x</code>, and immediately tries to discharge them by <code>assumption</code> or applying <code>ne_of_gt</code> or <code>ne_of_lt</code> to all assumptions</p>

#### [ Patrick Massot (May 30 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127304043):
<p>then it multiplies both sides of the goal by the product of all denominators, using the relevant lemmas (assuming the subgoals)</p>

#### [ Patrick Massot (May 30 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127304095):
<p>and then simplifies the goal to get rid of divisions by using <code>x/x = 1</code></p>

#### [ Patrick Massot (May 30 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127304100):
<p>Of course nested divisions would be problematic</p>

#### [ Patrick Massot (May 30 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127304107):
<p>The Cauchy-Schwarz thread is an example where you could use this</p>

#### [ Assia Mahboubi (May 30 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127304282):
<p>The inequality case is more difficult because of sign conditions, isn't it? But even in the equality case, the size of the formula to be proved can become quite large. Coq has a <code>field</code> tactic, built on top of <code>ring</code>, that does about the same thing as what you describe I think.</p>

#### [ Patrick Massot (May 30 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127304898):
<p>Indeed signs matter in inequalities</p>

#### [ Patrick Massot (May 30 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127304904):
<p>And we clearly need this field tactic (but Mario always want us to suffer instead of using automation)</p>

#### [ Assia Mahboubi (May 30 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/clear_denominator/near/127306985):
<p>The <code>field</code> problem is more difficult than the <code>ring</code> one. It probably has to start as a partial procedure, like the one you describe, because a complete one is much more delicate from an algorithmic point of view (you need stuff like subresultants or even may be probabilistic methods otherwise the complexity and growth of the polynomials are dreadful).</p>


{% endraw %}
