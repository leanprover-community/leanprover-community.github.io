---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30795propdecidablebreaksdectrivial.html
---

## Stream: [general](index.html)
### Topic: [prop_decidable breaks dec_trivial?](30795propdecidablebreaksdectrivial.html)

---


{% raw %}
#### [ Kevin Buzzard (Jul 26 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prop_decidable%20breaks%20dec_trivial%3F/near/130351758):
<div class="codehilite"><pre><span></span><span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>
<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">-</span><span class="mi">1</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">)</span> <span class="bp">≠</span> <span class="o">(</span><span class="mi">0</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">dec_trivial</span> <span class="c1">-- fails</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">exact tactic failed, type mismatch, given expression has type</span>
<span class="cm">  true</span>
<span class="cm">but is expected to have type</span>
<span class="cm">  as_true (-1 ≠ 0)</span>
<span class="cm">state:</span>
<span class="cm">⊢ as_true (-1 ≠ 0)</span>
<span class="cm">-/</span>
</pre></div>


<p>In practice this is in the middle of a big file which needs decidable props but occasionally also needs simple calculations like this. Is this expected behaviour?</p>

#### [ Patrick Massot (Jul 26 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prop_decidable%20breaks%20dec_trivial%3F/near/130352293):
<p>Did you try <code>local attribute [instance, priority 0] classical.prop_decidable</code>?</p>

#### [ Kevin Buzzard (Jul 26 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prop_decidable%20breaks%20dec_trivial%3F/near/130352343):
<p>Works! Thanks!</p>

#### [ Kevin Buzzard (Jul 26 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prop_decidable%20breaks%20dec_trivial%3F/near/130352372):
<p>What's happening here? Oh -- we have two instances</p>

#### [ Patrick Massot (Jul 26 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prop_decidable%20breaks%20dec_trivial%3F/near/130352384):
<p>We really need that <code>tips_and_tricks.md</code> in  mathlib docs</p>

#### [ Kevin Buzzard (Jul 26 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prop_decidable%20breaks%20dec_trivial%3F/near/130352766):
<p>I sometimes wonder why we can't solve diamond issues using priorities. "now we have two instances of topological_space (X x Y) and they're equal but not defeq so we have rw problems" -- "well just make the one you want a higher priority"</p>

#### [ Patrick Massot (Jul 26 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/prop_decidable%20breaks%20dec_trivial%3F/near/130353004):
<p>Good question!</p>


{% endraw %}
