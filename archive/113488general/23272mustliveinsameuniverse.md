---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23272mustliveinsameuniverse.html
---

## Stream: [general](index.html)
### Topic: [must live in same universe](23272mustliveinsameuniverse.html)

---


{% raw %}
#### [ Reid Barton (Jul 17 2018 at 05:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/must%20live%20in%20same%20universe/near/129790411):
<p>Any insight into this error?</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">value</span>
<span class="bp">|</span> <span class="n">object</span> <span class="o">:</span> <span class="n">rbmap</span> <span class="n">string</span> <span class="n">value</span> <span class="bp">→</span> <span class="n">value</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">nested inductive type compiled to invalid inductive type</span>
<span class="cm">nested exception message:</span>
<span class="cm">nested inductive type compiled to invalid inductive type</span>
<span class="cm">nested exception message:</span>
<span class="cm">nested inductive type compiled to invalid inductive type</span>
<span class="cm">nested exception message:</span>
<span class="cm">nested occurrence &#39;rbnode.well_formed.{0} _nest_3_3.prod.json.value (fun (a : _nest_3_3.prod.json.value) (b : _nest_3_3.prod.json.value), (has_lt.lt.{0} string string.has_lt (prod.fst.{0 0} string _nest_3_3.json.value a) (prod.fst.{0 0} string _nest_3_3.json.value b)))&#39; lives in universe &#39;0&#39; but must live in the same universe as the inductive types being declared, which is &#39;1&#39;</span>
<span class="cm">-/</span>
</pre></div>

#### [ Reid Barton (Jul 17 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/must%20live%20in%20same%20universe/near/129790488):
<p>I think it's because <code>rbtree</code> is defined as a subtype, and so contains a field which is a Prop, but I don't know what I should do about it</p>

#### [ Simon Hudon (Jul 17 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/must%20live%20in%20same%20universe/near/129790726):
<p>You can only use inductive types this way. <code>rbnode</code> is inductive so you may be able to write your definition as:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">value</span>
<span class="bp">|</span> <span class="n">object</span> <span class="o">:</span> <span class="k">forall</span> <span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="n">rbnode</span> <span class="c">/-</span><span class="cm"> something in terms of value -/</span><span class="o">),</span> <span class="n">t</span><span class="bp">.</span><span class="n">well_formed</span> <span class="n">lt</span> <span class="bp">-&gt;</span> <span class="n">value</span>
</pre></div>

#### [ Simon Hudon (Jul 17 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/must%20live%20in%20same%20universe/near/129790735):
<p>Then you can write a function that puts the <code>rbmap</code> back together.</p>

#### [ Mario Carneiro (Jul 17 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/must%20live%20in%20same%20universe/near/129790740):
<p>You can define it if you use <code>meta inductive</code></p>

#### [ Reid Barton (Jul 17 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/must%20live%20in%20same%20universe/near/129790781):
<p>Oh nice, <code>meta</code> is good enough for me (for now anyways)</p>


{% endraw %}
