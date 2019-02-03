---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03149inconsistencyoftheoremnaming.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [inconsistency of theorem naming](https://leanprover-community.github.io/archive/113488general/03149inconsistencyoftheoremnaming.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Jul 27 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inconsistency%20of%20theorem%20naming/near/130393117):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">check</span> <span class="n">list</span><span class="bp">.</span><span class="n">index_of_nth_le</span> <span class="bp">_</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">list.nth_le ?M_4 (list.index_of ?M_3 ?M_4) ?M_5 = ?M_3</span>
<span class="cm">-/</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">list</span><span class="bp">.</span><span class="n">nth_le_index_of</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">list.index_of (list.nth_le ?M_3 ?M_5 ?M_6) ?M_3 = ?M_5</span>
<span class="cm">-/</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">list</span><span class="bp">.</span><span class="n">nth_le_of_fn</span> <span class="bp">_</span> <span class="bp">_</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">list.nth_le (list.of_fn ?M_3) (?M_4.val) _ = ?M_3 ?M_4</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kenny Lau (Jul 27 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inconsistency%20of%20theorem%20naming/near/130393127):
<p>all three examples consist of a function followed by another function in the name</p>

#### [ Kenny Lau (Jul 27 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inconsistency%20of%20theorem%20naming/near/130393168):
<p>in the last example, the actual order in the statement is the same as the order in the name, i.e. <code>nth_le</code> and then <code>of_fn</code></p>

#### [ Kenny Lau (Jul 27 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inconsistency%20of%20theorem%20naming/near/130393173):
<p>but in the first two examples, the order is swapped</p>


{% endraw %}
