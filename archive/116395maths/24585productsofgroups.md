---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/24585productsofgroups.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [products of groups?](https://leanprover-community.github.io/archive/116395maths/24585productsofgroups.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Jun 25 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/products%20of%20groups%3F/near/128578863):
<p>Do we have instances that provide (pairwise) products of groups in mathlib? I know about <code>pi_instances</code> for indexed products, but can't find anything for the pairwise case.</p>

#### [ Mario Carneiro (Jun 25 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/products%20of%20groups%3F/near/128579293):
<p>I think Patrick might have a local version, but it's pretty easy to define in any case.</p>

#### [ Scott Morrison (Jun 25 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/products%20of%20groups%3F/near/128580657):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span>, do you have any plans to PR the instances for pairwise products of the basic algebraic hierarchy? (My preference is that there is not a single file with all of these, but they happen in each of the relevant files --- as we add more algebra we'll have to add things like this all along the way.)</p>

#### [ Scott Morrison (Jun 25 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/products%20of%20groups%3F/near/128580659):
<p>If not I can do it sometime.</p>

#### [ Patrick Massot (Jun 25 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/products%20of%20groups%3F/near/128597115):
<p>All mathlib product instances are hidden in <a href="https://github.com/leanprover/mathlib/blob/master/linear_algebra/prod_module.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/linear_algebra/prod_module.lean">https://github.com/leanprover/mathlib/blob/master/linear_algebra/prod_module.lean</a>, in particular product groups. At some point I tried to move them when preparing a PR but I gave up because everything broke?</p>


{% endraw %}
