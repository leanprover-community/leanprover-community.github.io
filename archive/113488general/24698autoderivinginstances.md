---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24698autoderivinginstances.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [auto deriving instances](https://leanprover-community.github.io/archive/113488general/24698autoderivinginstances.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Zesen Qian (Jun 07 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20instances/near/127688095):
<p>Is there a quick way to derive instances for type definitions like <code>def boolean : Type := bool</code>?</p>

#### [ Kenny Lau (Jun 07 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20instances/near/127688100):
<p>don't use them :)</p>

#### [ Zesen Qian (Jun 07 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20instances/near/127688156):
<p>I feel type synonym is useful in development.</p>

#### [ Kenny Lau (Jun 07 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20instances/near/127688161):
<p>pretty sure you can't find it anywhere in mathlib</p>

#### [ Simon Hudon (Jun 07 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20instances/near/127688204):
<p>If you mark your definition as reducible, I think, the instances will simply be inherited</p>

#### [ Simon Hudon (Jun 07 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20instances/near/127688215):
<p>Otherwise, you can do </p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">my_class</span> <span class="n">some_synonym</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">dsimp</span> <span class="o">[</span><span class="n">some_synonym</span><span class="o">]</span> <span class="bp">;</span> <span class="n">apply_instance</span>
</pre></div>

#### [ Zesen Qian (Jun 07 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auto%20deriving%20instances/near/127688285):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> very nice, sir.</p>


{% endraw %}
