---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/75284subringvssubmodule.html
---

## Stream: [maths](index.html)
### Topic: [subring vs submodule](75284subringvssubmodule.html)

---


{% raw %}
#### [ Patrick Massot (Oct 09 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subring%20vs%20submodule/near/135464064):
<p>Let me bring up old news since it looks like the module refactor is almost done. The following works nicely:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">ring_theory</span><span class="bp">.</span><span class="n">subring</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">R</span><span class="o">)</span> <span class="o">[</span><span class="n">is_subring</span> <span class="n">S</span><span class="o">]</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="n">S</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">has_add</span> <span class="n">S</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
</pre></div>


<p>Now add <code>import linear_algebra.quotient_module</code> at top, and the second example no-longer works. In particular this breaks the cast from nat to S. Is this fixed in the module refactor?</p>

#### [ Patrick Massot (Nov 03 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subring%20vs%20submodule/near/137121150):
<p>Let me bring up that thread. Kenny or Mario, do you think this problem is now fixed by the module refactor?</p>

#### [ Kenny Lau (Nov 03 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subring%20vs%20submodule/near/137122003):
<p><code>linear_algebra.quotient_module</code> is deleted (and its content is migrated to <code>linear_algebra.basic</code>), so I imported that instead, and it worked</p>


{% endraw %}
