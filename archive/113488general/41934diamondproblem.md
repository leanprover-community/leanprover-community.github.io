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
I'm not sure if this is an instance of the type class diamond problem, but what do you do when you have `has_add` from `add_comm_monoid` and need `has_add` from `distrib`, given that you have `[add_comm_monoid α] [distrib α]`? One solution seems to be to use `[semiring α]` instead, but that seems to me to add unnecessary constraints, since `semiring` also extends `monoid` and `mul_zero_class`. I'm guessing there is another, better way.

#### [ Reid Barton (Sep 06 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diamond%20problem/near/133430751):
I think you should avoid being in that situation in the first place.
But I don't understand why there isn't a problem with `semiring` itself.
Maybe old_structure_cmd magic?

#### [ Reid Barton (Sep 06 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diamond%20problem/near/133430881):
Maybe you could make your own "old structure" containing just what you need?

#### [ Sean Leather (Sep 06 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/diamond%20problem/near/133430955):
Sorry, Reid, I haven't used `old_structure_cmd` and don't know what you mean.


{% endraw %}
