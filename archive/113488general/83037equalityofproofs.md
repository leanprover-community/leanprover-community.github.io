---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83037equalityofproofs.html
---

## Stream: [general](index.html)
### Topic: [equality of proofs](83037equalityofproofs.html)

---


{% raw %}
#### [ Reid Barton (Apr 28 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20proofs/near/125803504):
<p>Is this lemma true and what is it (or should it be) called?</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">hpropext</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">==</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Reid Barton (Apr 28 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20proofs/near/125803608):
<p><code>proof_irrel</code> is the non-heterogeneous version</p>

#### [ Reid Barton (Apr 28 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equality%20of%20proofs/near/125803658):
<p>OK, I managed to prove it</p>


{% endraw %}
