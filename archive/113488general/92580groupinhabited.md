---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/92580groupinhabited.html
---

## Stream: [general](index.html)
### Topic: [group.inhabited](92580groupinhabited.html)

---


{% raw %}
#### [ Kenny Lau (Apr 21 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group.inhabited/near/125476491):
<p>Should we show that every group is inhabited? Should we generalize it to has_one and has_zero? Which one will ring choose?</p>

#### [ Mario Carneiro (Apr 21 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group.inhabited/near/125476942):
<p>I'm inclined to say no. <code>inhabited</code> is more of a programming notion, a way to acquire a "default" value when it doesn't matter what value is picked. The value has no semantic meaning, so it doesn't matter if one or zero is picked. But I don't think that a typeclass search for <code>inhabited</code> should go on an algebraic quest to prove that it's an R-module just because that implies it's inhabited. It would be better to have the types themselves register as inhabited, to keep it simple.</p>

#### [ Kenny Lau (Apr 21 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/group.inhabited/near/125476982):
<p>ok</p>


{% endraw %}
