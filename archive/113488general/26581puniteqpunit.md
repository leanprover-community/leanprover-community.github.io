---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26581puniteqpunit.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [punit_eq_punit](https://leanprover-community.github.io/archive/113488general/26581puniteqpunit.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Apr 23 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/punit_eq_punit/near/125550617):
<p>This definition (from <code>library/init/data/punit.lean</code>) is less general than probably intended because <code>()</code> is (apparently) built-in notation for <code>unit.star</code> only, and so the full inferred type is actually <code>punit_eq_punit : ∀ (a : punit.{1}), @eq.{1} punit.{1} a unit.star</code>.</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">punit_eq_punit</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">punit</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="o">()</span> <span class="o">:=</span>
<span class="n">punit_eq</span> <span class="n">a</span> <span class="o">()</span>
</pre></div>


<p>Since this is in the core Lean library, is there any hope to change it?</p>

#### [ Patrick Massot (Apr 23 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/punit_eq_punit/near/125558322):
<blockquote>
<p>Since this is in the core Lean library, is there any hope to change it?</p>
</blockquote>
<p>Someone should really read that Zulip bot documentation. Programming a bot to detect this question and answer "no" is probably a nice exercise then.</p>


{% endraw %}
