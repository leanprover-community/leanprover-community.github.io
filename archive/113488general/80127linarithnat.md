---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/80127linarithnat.html
---

## Stream: [general](index.html)
### Topic: [linarith nat](80127linarithnat.html)

---


{% raw %}
#### [ Patrick Massot (Dec 23 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20nat/near/152434102):
<p>Is it part of the known limitations of <code>linarith</code> that I can't do better than</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span>  <span class="o">(</span><span class="n">n</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">h&#39;</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">-</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">m</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_lt</span> <span class="bp">;</span>
  <span class="n">linarith</span>
<span class="kn">end</span>
</pre></div>


<p>I would like to get rid of the first line?</p>

#### [ Patrick Massot (Dec 23 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20nat/near/152434103):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span></p>

#### [ Rob Lewis (Dec 23 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/linarith%20nat/near/152436375):
<p>To <code>linarith</code>, <code>m - n</code> is some arbitrary constant with type <code>nat</code> that it knows no extra information about. So no, it shouldn't be expected to solve that.</p>


{% endraw %}
