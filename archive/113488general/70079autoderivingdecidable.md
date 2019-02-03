---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70079autoderivingdecidable.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [auto deriving decidable](https://leanprover-community.github.io/archive/113488general/70079autoderivingdecidable.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Zesen Qian (Jun 20 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20decidable/near/128374348):
<p>Is there some way to derive decidable instance from a inductive definition?</p>

#### [ Zesen Qian (Jun 20 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20decidable/near/128374554):
<p>sorry, I mean the decidable instance for equality on this inductive type.</p>

#### [ Simon Hudon (Jun 20 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20decidable/near/128374581):
<p>Try:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="n">my_type</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">mk_dec_eq_instance</span>
</pre></div>

#### [ Mario Carneiro (Jun 20 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20decidable/near/128377002):
<p>or <code>@[derive decidable_eq]</code></p>


{% endraw %}
