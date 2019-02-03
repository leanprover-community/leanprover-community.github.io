---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86354simpconfigplaceholder.html
---

## Stream: [general](index.html)
### Topic: [simp_config placeholder](86354simpconfigplaceholder.html)

---


{% raw %}
#### [ Sean Leather (Oct 01 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_config%20placeholder/near/134955856):
<p>I just discovered this by accident:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="bp">_</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="n">error</span><span class="o">:</span> <span class="n">don&#39;t</span> <span class="n">know</span> <span class="n">how</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">placeholder</span>
<span class="kn">context</span><span class="o">:</span>
<span class="err">⊢</span> <span class="n">opt_param</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">simp_config_ext</span>
    <span class="o">{</span><span class="n">to_simp_config</span> <span class="o">:=</span> <span class="o">{</span><span class="n">max_steps</span> <span class="o">:=</span> <span class="n">simp</span><span class="bp">.</span><span class="n">default_max_steps</span><span class="o">,</span>
                        <span class="n">contextual</span> <span class="o">:=</span> <span class="n">ff</span><span class="o">,</span>
                        <span class="n">lift_eq</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">,</span>
                        <span class="n">canonize_instances</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">,</span>
                        <span class="n">canonize_proofs</span> <span class="o">:=</span> <span class="n">ff</span><span class="o">,</span>
                        <span class="n">use_axioms</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">,</span>
                        <span class="n">zeta</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">,</span>
                        <span class="n">beta</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">,</span>
                        <span class="n">eta</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">,</span>
                        <span class="n">proj</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">,</span>
                        <span class="n">iota</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">,</span>
                        <span class="n">iota_eqn</span> <span class="o">:=</span> <span class="n">ff</span><span class="o">,</span>
                        <span class="n">constructor_eq</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">,</span>
                        <span class="n">single_pass</span> <span class="o">:=</span> <span class="n">ff</span><span class="o">,</span>
                        <span class="n">fail_if_unchanged</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">,</span>
                        <span class="n">memoize</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">},</span>
     <span class="n">discharger</span> <span class="o">:=</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">failed</span> <span class="n">unit</span><span class="o">}</span>
</pre></div>

#### [ Reid Barton (Oct 01 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_config%20placeholder/near/134961539):
<p>Nice! <code>rw [] _</code> also works to see <code>rw</code> options.</p>


{% endraw %}
