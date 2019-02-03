---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43990orderedcommmonoid.html
---

## Stream: [general](index.html)
### Topic: [ordered_comm_monoid](43990orderedcommmonoid.html)

---


{% raw %}
#### [ Johan Commelin (Sep 29 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134890643):
<p>Why is <code>ordered_comm_monoid</code> additive? I thought <code>{x : real | x ≥ 1}</code> is a really nice ordered commutative monoid...</p>

#### [ Chris Hughes (Sep 29 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134890739):
<p>Because most ordered comm monoids are additive, like reals, ints, nats, rats, with_bot nat</p>

#### [ Johan Commelin (Sep 29 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134890797):
<p>Sure, but we could still have the <code>add</code> in the name right? And I think there are enough examples where they aren't additive, like positive reals, nats, positive rats...</p>

#### [ Simon Hudon (Sep 29 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134894040):
<p>That makes sense. Btw, isn't <code>{x : real | x ≥ 1}</code> a commutative group?</p>

#### [ Kenny Lau (Sep 29 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134894089):
<p>inverse?</p>

#### [ Sebastian Zimmer (Sep 29 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134894526):
<p>Is your group operation (x, y) -&gt; (x - 1)(y - 1) + 1 or something crazy like that?</p>

#### [ Kenny Lau (Sep 29 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134894577):
<p>that would make 1 have no inverse</p>

#### [ Sebastian Zimmer (Sep 29 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134894578):
<p>ah good point</p>

#### [ Simon Hudon (Sep 29 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ordered_comm_monoid/near/134894978):
<p>Right, somehow, the fact that the inverse is less than one escaped me. You'd need { x : real | x &gt; 0 } for a group.</p>


{% endraw %}
