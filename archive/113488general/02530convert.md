---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02530convert.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [convert](https://leanprover-community.github.io/archive/113488general/02530convert.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (May 31 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert/near/127339342):
<p>maybe <code>convert</code> can automatically <code>apply_instance</code>?</p>

#### [ Simon Hudon (May 31 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert/near/127340761):
<p>Are you thinking in writing or asking for help?</p>

#### [ Kenny Lau (May 31 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert/near/127340762):
<p>I'm suggesting</p>

#### [ Simon Hudon (May 31 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert/near/127340806):
<p>There's no context accompanying your comment, it's in a brand new thread</p>

#### [ Kenny Lau (May 31 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert/near/127340807):
<p>sorry</p>

#### [ Mario Carneiro (May 31 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert/near/127340997):
<p>This doesn't make any sense. <code>convert</code> generates an equality goal, it is never something that can be <code>apply_instance</code> solvable</p>

#### [ Kenny Lau (May 31 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert/near/127341033):
<p>oh, <code>convert</code> generates auxiliary goals, some of which are <code>apply_instance</code> solvable</p>

#### [ Kenny Lau (May 31 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/convert/near/127341039):
<p>e.g. <code>finsupp.sum_zero_index</code></p>


{% endraw %}
