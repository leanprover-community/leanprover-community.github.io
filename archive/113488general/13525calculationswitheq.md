---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/13525calculationswitheq.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [calculations with eq](https://leanprover-community.github.io/archive/113488general/13525calculationswitheq.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Jun 22 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calculations%20with%20eq/near/128483780):
<p>Is this provable?</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">eq_mpr_val</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">subtype</span> <span class="n">p</span> <span class="bp">=</span> <span class="n">subtype</span> <span class="n">q</span><span class="o">)</span>
  <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">subtype</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">mpr</span> <span class="n">e</span> <span class="n">x</span><span class="o">)</span><span class="bp">.</span><span class="n">val</span> <span class="bp">=</span> <span class="n">x</span><span class="bp">.</span><span class="n">val</span> <span class="o">:=</span>
<span class="n">sorry</span>
</pre></div>

#### [ Reid Barton (Jun 22 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calculations%20with%20eq/near/128483850):
<p>(<code>subtype</code> here is just an example of a type which has a field whose type doesn't depend on the type indices being changed by <code>e</code>.)</p>

#### [ Reid Barton (Jun 22 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calculations%20with%20eq/near/128483937):
<p>Or if I find myself needing to prove this sort of thing, do I need to back up and make sure that instead of this <code>eq.mpr e x</code>, I have an expression that recurses on a proof of <code>p = q</code>?</p>

#### [ Simon Hudon (Jun 22 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calculations%20with%20eq/near/128484399):
<p>Yeah, I don't see an alternative. <code>eq.mpr</code> is going to be difficult to get rid of. I tried various things with generalize and congr but to no avail</p>

#### [ Chris Hughes (Jun 22 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calculations%20with%20eq/near/128493634):
<p>I think it's probably not provable. I don't see a reason why <code>@subtype.val α p == @subtype.val α q</code> without <code>p = q</code>. I think in lean two types of the same size are indistinguishable, so if <code>p ≠ q</code>, but <code>subtype p = subtype q</code>, there's no contradiction, provided they're the same size, but there's no canonical isomorphism or way of identifying <code>@subtype.val α p</code> with <code>@subtype.val α q</code>. Mario will know.</p>

#### [ Chris Hughes (Jun 22 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calculations%20with%20eq/near/128493734):
<p>I couldn't actually prove a contradiction from assuming <code>subtype p = subtype q</code>, where <code>p ≠ q</code> and your lemma though.</p>

#### [ Mario Carneiro (Jun 23 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calculations%20with%20eq/near/128504956):
<p>These sorts of things are independent in lean. Injectivity of inductive type constructors is either independent or false in every case I'm aware of.</p>


{% endraw %}
