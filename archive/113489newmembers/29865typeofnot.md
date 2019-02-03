---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/29865typeofnot.html
---

## Stream: [new members](index.html)
### Topic: [type of `not`](29865typeofnot.html)

---


{% raw %}
#### [ Scott Olson (Oct 09 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/type%20of%20%60not%60/near/135432721):
<p>Is there a reason we have <code>def not : Prop → Prop</code> rather than <code>def not : Sort u → Prop</code>?</p>
<p>I had some proofs of <code>¬foo</code> which I had to change to <code>foo → false</code> when I changed <code>foo</code> from a simple <code>∃</code> Prop to a <code>structure</code> sigma Type, but it seems like it would make sense to still say <code>¬foo</code>.</p>

#### [ Simon Hudon (Oct 09 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/type%20of%20%60not%60/near/135433027):
<p>It's probably a matter of convention. <code>¬p</code>, you usually assume that <code>p</code> is a proposition . An operation such as you describe might more usefully be called <code>is_empty</code></p>

#### [ Mario Carneiro (Oct 09 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/type%20of%20%60not%60/near/135434043):
<p>there used to be a <code>~A</code> notation for this, but it didn't get used enough to be worth it.</p>


{% endraw %}
