---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/82287simplistmapid.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [simp list.map id](https://leanprover-community.github.io/archive/113488general/82287simplistmapid.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Sep 28 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20list.map%20id/near/134810749):
<p>Interesting that <code>simp</code> doesn't solve <code>list.map (λ t, t) l = l</code>.</p>

#### [ Sean Leather (Sep 28 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20list.map%20id/near/134810792):
<p>I suppose I could add this to the <code>simp</code>:</p>
<div class="codehilite"><pre><span></span> <span class="kn">theorem</span> <span class="n">map_id&#39;</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">map</span> <span class="n">f</span> <span class="n">l</span> <span class="bp">=</span> <span class="n">l</span>
</pre></div>

#### [ Sean Leather (Sep 28 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20list.map%20id/near/134810856):
<p>Yep, <code>simp [list.map_id']</code> does the job.</p>


{% endraw %}
