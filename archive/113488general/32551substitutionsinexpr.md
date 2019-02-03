---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32551substitutionsinexpr.html
---

## Stream: [general](index.html)
### Topic: [substitutions in `expr`](32551substitutionsinexpr.html)

---


{% raw %}
#### [ Simon Hudon (Apr 17 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/substitutions%20in%20%60expr%60/near/125176108):
<p>If I have <code>e : expr</code> and I have a pattern <code>p : expr</code> which I would like to substitute for a variable (a bit like <code>generalize</code> does for a proof goal) what is the best way to do it?</p>

#### [ Simon Hudon (Apr 17 2018 at 03:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/substitutions%20in%20%60expr%60/near/125176166):
<p>Is there something better than making a goal that contains <code>e</code> and calling <code>generalize p</code> on it?</p>

#### [ Mario Carneiro (Apr 17 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/substitutions%20in%20%60expr%60/near/125177661):
<p><code>kabstract</code> is the core function that does this</p>

#### [ Simon Hudon (Apr 17 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/substitutions%20in%20%60expr%60/near/125177712):
<p>Nice! Thanks!</p>


{% endraw %}
