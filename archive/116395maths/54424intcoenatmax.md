---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/54424intcoenatmax.html
---

## Stream: [maths](index.html)
### Topic: [int.coe_nat_max](54424intcoenatmax.html)

---


{% raw %}
#### [ Kevin Buzzard (Sep 06 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.coe_nat_max/near/133455883):
<p>I don't <em>think</em> <code>int.coe_nat_max : {m n : ℕ} : (↑(max m n) : ℤ) = max m n</code> is in mathlib, and I needed it today. Kenny produced this proof:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_max</span> <span class="o">{</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="err">↑</span><span class="o">(</span><span class="n">max</span> <span class="n">m</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="bp">=</span> <span class="n">max</span> <span class="n">m</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">max</span><span class="o">,</span><span class="n">simp</span> <span class="o">[</span><span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_le</span><span class="o">],</span>
  <span class="n">split_ifs</span><span class="bp">;</span><span class="n">refl</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>but I was thinking that the result probably lived near the beginning of <code>data.int.basic</code> and I'm not sure that the devs will want <code>split_ifs</code> to be used in such a low-level file. Should it go later on or should we think of a more low-level proof? (or is it there already?)</p>

#### [ Mario Carneiro (Sep 06 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/int.coe_nat_max/near/133456744):
<p>I agree this belongs in <code>data.int.basic</code>, and there is no problem using <code>split_ifs</code>. The mathlib tactics are all very low in the dependency order so that mathlib can use them</p>


{% endraw %}
