---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/41934diamondproblem.html
---

## Stream: [general](index.html)
### Topic: [diamond problem](41934diamondproblem.html)

---


{% raw %}
#### [ Sean Leather (Sep 06 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diamond%20problem/near/133430283):
<p>I'm not sure if this is an instance of the type class diamond problem, but what do you do when you have <code>has_add</code> from <code>add_comm_monoid</code> and need <code>has_add</code> from <code>distrib</code>, given that you have <code>[add_comm_monoid α] [distrib α]</code>? One solution seems to be to use <code>[semiring α]</code> instead, but that seems to me to add unnecessary constraints, since <code>semiring</code> also extends <code>monoid</code> and <code>mul_zero_class</code>. I'm guessing there is another, better way.</p>

#### [ Reid Barton (Sep 06 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diamond%20problem/near/133430751):
<p>I think you should avoid being in that situation in the first place.<br>
But I don't understand why there isn't a problem with <code>semiring</code> itself.<br>
Maybe old_structure_cmd magic?</p>

#### [ Reid Barton (Sep 06 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diamond%20problem/near/133430881):
<p>Maybe you could make your own "old structure" containing just what you need?</p>

#### [ Sean Leather (Sep 06 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diamond%20problem/near/133430955):
<p>Sorry, Reid, I haven't used <code>old_structure_cmd</code> and don't know what you mean.</p>


{% endraw %}
