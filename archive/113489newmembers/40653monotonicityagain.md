---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/40653monotonicityagain.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [monotonicity again](https://leanprover-community.github.io/archive/113489newmembers/40653monotonicityagain.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Simon Hudon (Aug 04 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/monotonicity%20again/near/130874956):
<p>I just gave another shot to implementing <code>mono</code> and <code>ac_mono</code> (for reasoning with monotonicity with and without considerations for associativity / commutativity). For those who would like to use those, I'd love to hear if it's useful as it is. I have written a lot of examples, I hope it will be informative.</p>
<p><a href="https://github.com/cipher1024/mathlib/blob/monotonicity/tests/monotonicity.lean" target="_blank" title="https://github.com/cipher1024/mathlib/blob/monotonicity/tests/monotonicity.lean">https://github.com/cipher1024/mathlib/blob/monotonicity/tests/monotonicity.lean</a><br>
<a href="https://github.com/cipher1024/mathlib/tree/monotonicity/docs" target="_blank" title="https://github.com/cipher1024/mathlib/tree/monotonicity/docs">https://github.com/cipher1024/mathlib/tree/monotonicity/docs</a></p>

#### [ Johan Commelin (Aug 04 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/monotonicity%20again/near/130876196):
<p>This seems quite useful! I wonder if it would help with proving some of my stuff on simplicial sets: <a href="https://github.com/jcommelin/mathlib/blob/ece70f307edc5fdebe7aed154ab8aaa3a12bb5a3/algebraic_topology/simplex_category.lean#L33" target="_blank" title="https://github.com/jcommelin/mathlib/blob/ece70f307edc5fdebe7aed154ab8aaa3a12bb5a3/algebraic_topology/simplex_category.lean#L33">https://github.com/jcommelin/mathlib/blob/ece70f307edc5fdebe7aed154ab8aaa3a12bb5a3/algebraic_topology/simplex_category.lean#L33</a> or <a href="https://github.com/jcommelin/mathlib/blob/ece70f307edc5fdebe7aed154ab8aaa3a12bb5a3/algebraic_topology/simplex_category.lean#L67" target="_blank" title="https://github.com/jcommelin/mathlib/blob/ece70f307edc5fdebe7aed154ab8aaa3a12bb5a3/algebraic_topology/simplex_category.lean#L67">https://github.com/jcommelin/mathlib/blob/ece70f307edc5fdebe7aed154ab8aaa3a12bb5a3/algebraic_topology/simplex_category.lean#L67</a></p>

#### [ Johan Commelin (Aug 04 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/monotonicity%20again/near/130876208):
<p>(Also, wrong stream? Or do you propose <code>mono</code> and <code>ac_mono</code> as "new members" of the community?)</p>

#### [ Simon Hudon (Aug 04 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/monotonicity%20again/near/130876506):
<p><em>cough cough</em> of course they would be! They're just such awesome tactics :D</p>

#### [ Simon Hudon (Aug 04 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/monotonicity%20again/near/130876631):
<p>I'm not sure how they would help for those proofs though. I'm really targeting goals of the shape <code>x + y ≤ w + z</code> for some relation <code>≤</code>.</p>

#### [ Johan Commelin (Aug 04 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/monotonicity%20again/near/130877226):
<p>Ok, I see. Well, maybe at some point <code>cooper</code> will turn my proofs into a 1-liner.</p>

#### [ Simon Hudon (Aug 04 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/monotonicity%20again/near/130877412):
<p>Isn't <code>cooper</code> mostly about integer arithmetic?</p>

#### [ Johan Commelin (Aug 04 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/monotonicity%20again/near/130877614):
<p>It is, but I think so are my proofs.</p>

#### [ Simon Hudon (Aug 04 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/monotonicity%20again/near/130877706):
<p>Ok, I squinted at them and started to see integers. I wonder if <code>fin</code> will make it harder. Does Presburger arithmetic include modulo?</p>

#### [ Mario Carneiro (Aug 04 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/monotonicity%20again/near/130877768):
<p>modulo by constants yes</p>

#### [ Johan Commelin (Aug 04 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/monotonicity%20again/near/130887896):
<p>There is no modular arithmetic in my code. <code>fin</code> should just unpack to some inequalities, and <code>cooper</code> should be able to deal with those...</p>


{% endraw %}
