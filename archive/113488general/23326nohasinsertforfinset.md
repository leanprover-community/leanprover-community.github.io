---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23326nohasinsertforfinset.html
---

## Stream: [general](index.html)
### Topic: [no `has_insert` for `finset`](23326nohasinsertforfinset.html)

---


{% raw %}
#### [ Chris Hughes (Jul 04 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20%60has_insert%60%20for%20%60finset%60/near/129094565):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">:</span> <span class="n">has_insert</span> <span class="n">α</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="c1">-- doesn&#39;t work</span>
</pre></div>


<p>Shouldn't there be a <code>has_insert</code> instance on <code>finset</code>? Without it I can't use the notation <code>{0,1,2}</code></p>

#### [ Mario Carneiro (Jul 04 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20%60has_insert%60%20for%20%60finset%60/near/129094776):
<p>there is an insert operation, but it requires decidable_eq</p>


{% endraw %}
