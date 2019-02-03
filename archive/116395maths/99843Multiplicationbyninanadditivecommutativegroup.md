---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/99843Multiplicationbyninanadditivecommutativegroup.html
---

## Stream: [maths](index.html)
### Topic: [Multiplication by n in an additive commutative group](99843Multiplicationbyninanadditivecommutativegroup.html)

---


{% raw %}
#### [ Johan Commelin (May 14 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Multiplication%20by%20n%20in%20an%20additive%20commutative%20group/near/126531796):
<p>Is this somewhere in mathlib?</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">mul_n</span> <span class="o">{</span><span class="n">G</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">G</span><span class="o">]</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">G</span><span class="o">)</span> <span class="o">:</span> <span class="n">G</span> <span class="o">:=</span> <span class="n">n</span> <span class="err">•</span> <span class="n">g</span> <span class="c1">-- sorry</span>
</pre></div>

#### [ Johannes Hölzl (May 14 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Multiplication%20by%20n%20in%20an%20additive%20commutative%20group/near/126533667):
<p>Its <code>gsmul</code> (generalized(?) scalar multiplication) in <code>algebra.group_power</code></p>

#### [ Johan Commelin (May 14 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Multiplication%20by%20n%20in%20an%20additive%20commutative%20group/near/126534062):
<p>Thanks!</p>

#### [ Mario Carneiro (May 14 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Multiplication%20by%20n%20in%20an%20additive%20commutative%20group/near/126550514):
<p>the "g" stands for "group" in gsmul and gpow.</p>


{% endraw %}
