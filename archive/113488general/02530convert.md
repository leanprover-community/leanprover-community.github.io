---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02530convert.html
---

## Stream: [general](index.html)
### Topic: [convert](02530convert.html)

---


{% raw %}
#### [ Kenny Lau (May 31 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert/near/127339342):
maybe `convert` can automatically `apply_instance`?

#### [ Simon Hudon (May 31 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert/near/127340761):
Are you thinking in writing or asking for help?

#### [ Kenny Lau (May 31 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert/near/127340762):
I'm suggesting

#### [ Simon Hudon (May 31 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert/near/127340806):
There's no context accompanying your comment, it's in a brand new thread

#### [ Kenny Lau (May 31 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert/near/127340807):
sorry

#### [ Mario Carneiro (May 31 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert/near/127340997):
This doesn't make any sense. `convert` generates an equality goal, it is never something that can be `apply_instance` solvable

#### [ Kenny Lau (May 31 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert/near/127341033):
oh, `convert` generates auxiliary goals, some of which are `apply_instance` solvable

#### [ Kenny Lau (May 31 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert/near/127341039):
e.g. `finsupp.sum_zero_index`


{% endraw %}
