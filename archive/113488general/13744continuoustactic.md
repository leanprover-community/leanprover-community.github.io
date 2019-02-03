---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/13744continuoustactic.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [continuous tactic](https://leanprover-community.github.io/archive/113488general/13744continuoustactic.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Nov 01 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/continuous%20tactic/near/136888333):
<p>Can we have a tactic that solves continuity goals, matching e.g. <code>continuous (f o g)</code> and splitting it into two goals?</p>

#### [ Kevin Buzzard (Nov 01 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/continuous%20tactic/near/136888372):
<p><code>meta def continuity_goals := `[apply continuous.comp]</code> or something?</p>

#### [ Reid Barton (Nov 01 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/continuous%20tactic/near/136891384):
<p>I have this but it is based on <code>backwards_reasoning</code> and it seemed better to wait for that to land in mathlib first.</p>

#### [ Kenny Lau (Nov 01 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/continuous%20tactic/near/136891435):
<p>nice</p>

#### [ Scott Morrison (Nov 01 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/continuous%20tactic/near/136903346):
<p>Sorry, I haven’t given the backwards reasoning PR much attention recently. I’ll try to get back to it!</p>


{% endraw %}
