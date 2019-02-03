---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/06120tactictoexpr.html
---

## Stream: [general](index.html)
### Topic: [tactic.to_expr](06120tactictoexpr.html)

---


{% raw %}
#### [ Edward Ayers (Dec 11 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.to_expr/near/151462345):
<p>How can I get <code>tactic.to_expr</code> to not apply metavariables to implicit arguments? That is;</p>
<div class="codehilite"><pre><span></span><span class="kn">constant</span> <span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="kn">axiom</span> <span class="n">P</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span><span class="o">:</span><span class="n">α</span><span class="o">},</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span>
<span class="n">run_cmd</span> <span class="n">do</span>
    <span class="n">p</span> <span class="err">←</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">resolve_name</span> <span class="bp">`</span><span class="n">P</span><span class="o">,</span>
    <span class="n">e</span> <span class="err">←</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">to_expr</span> <span class="n">p</span><span class="o">,</span>
    <span class="n">t</span> <span class="err">←</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">infer_type</span> <span class="n">e</span><span class="o">,</span>
    <span class="n">trace</span> <span class="n">t</span><span class="o">,</span>  <span class="c1">-- gives &quot;?m_1 = ?m_1&quot;</span>
    <span class="n">pure</span> <span class="o">()</span>
</pre></div>


<p>I really want to find a way of getting <code>trace t</code> to say <code>∀ {a:α}, a = a</code> given only the declaration name <code>P</code></p>

#### [ Reid Barton (Dec 11 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.to_expr/near/151468593):
<p>Do you need to go through <code>to_expr</code>?</p>

#### [ Rob Lewis (Dec 11 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.to_expr/near/151468620):
<p><code>e ← tactic.to_expr p.mk_explicit</code> should work for this case.</p>

#### [ Reid Barton (Dec 11 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.to_expr/near/151468935):
<p>I was going to suggest</p>
<div class="codehilite"><pre><span></span><span class="n">run_cmd</span> <span class="n">do</span>
    <span class="n">d</span> <span class="err">←</span> <span class="n">get_decl</span> <span class="bp">`</span><span class="n">P</span><span class="o">,</span>
    <span class="n">trace</span> <span class="n">d</span><span class="bp">.</span><span class="n">type</span><span class="o">,</span>
    <span class="n">pure</span> <span class="o">()</span>
</pre></div>

#### [ Rob Lewis (Dec 11 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic.to_expr/near/151470588):
<p>Yeah, that's better here, although I guess it depends on the real context.</p>


{% endraw %}
