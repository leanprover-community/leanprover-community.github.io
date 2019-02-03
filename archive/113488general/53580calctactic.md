---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53580calctactic.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [calc tactic](https://leanprover-community.github.io/archive/113488general/53580calctactic.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (Jan 02 2019 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20tactic/near/154178076):
<p>I just noticed that <code>calc</code> is an interactive tactic which somehow unfolds to <code>exact calc</code> by magic</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">0</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">calc</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">+</span> <span class="n">x</span> <span class="o">:</span> <span class="n">add_comm</span> <span class="bp">_</span> <span class="bp">_</span>
         <span class="bp">...</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:</span> <span class="n">zero_add</span> <span class="bp">_</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Jan 02 2019 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20tactic/near/154178117):
<p>I'm not sure exactly how this works, since <code>tactic.interactive.calc</code> doesn't exist</p>

#### [ Mario Carneiro (Jan 02 2019 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20tactic/near/154178355):
<p>yep, it's hardcoded - <code>calc</code> turns into <code>exact calc</code> (<a href="https://github.com/leanprover/lean/blob/master/src/frontends/lean/tactic_notation.cpp#L273-L276" target="_blank" title="https://github.com/leanprover/lean/blob/master/src/frontends/lean/tactic_notation.cpp#L273-L276">https://github.com/leanprover/lean/blob/master/src/frontends/lean/tactic_notation.cpp#L273-L276</a>)</p>


{% endraw %}
