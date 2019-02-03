---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/18934instance.html
---

## Stream: [general](index.html)
### Topic: [instance](18934instance.html)

---


{% raw %}
#### [ Kenny Lau (Aug 13 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132041055):
<p><code>algebra/module.lean</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">range</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">}</span> <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">is_linear_map</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_submodule</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">set</span><span class="bp">.</span><span class="n">image_univ</span><span class="o">]</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">is_submodule</span><span class="bp">.</span><span class="n">image</span> <span class="n">hf</span>
</pre></div>


<p>should this be an instance?</p>

#### [ Mario Carneiro (Aug 13 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132041241):
<p>no good, unless <code>is_linear_map</code> is a typeclass</p>

#### [ Kenny Lau (Aug 13 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132043377):
<p>what to do about it then</p>

#### [ Mario Carneiro (Aug 13 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132043635):
<p>fix it?</p>

#### [ Guy Leroy (Aug 14 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132121087):
<p>I'm struggling with instances, I have the error:<br>
failed to synthesize type class instance for</p>
<div class="codehilite"><pre><span></span><span class="n">a</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">pos_nat</span> <span class="n">n</span><span class="o">,</span>
<span class="n">em</span> <span class="o">:</span> <span class="n">coprime</span> <span class="n">a</span> <span class="n">n</span>
<span class="err">⊢</span> <span class="n">decidable_eq</span> <span class="o">(</span><span class="n">coprime</span> <span class="n">a</span> <span class="n">n</span> <span class="bp">→</span> <span class="bp">Π</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">pos_nat</span> <span class="n">n</span><span class="o">],</span> <span class="n">units</span> <span class="o">(</span><span class="n">zmod</span> <span class="n">n</span><span class="o">))</span>
</pre></div>


<p>How should I state the instance that would solve this?</p>

#### [ Patrick Massot (Aug 14 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132121699):
<p>You should give us more context, this goal is probably not what you actually want</p>

#### [ Mario Carneiro (Aug 14 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132121881):
<p>While I agree with patrick, I doubt that this is the right goal to solve, it is incidentally provable. Probably the missing piece is <code>decidable (pos_nat n)</code></p>

#### [ Guy Leroy (Aug 14 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132121916):
<p>Thanks Patrick, you're right, I made a mistake when writing my goal and it's all fixed now.<br>
I would still be curious as to what this instance actually means.<br>
As for the context I wrote </p>
<div class="codehilite"><pre><span></span><span class="k">have</span> <span class="o">:</span> <span class="o">(</span><span class="n">units_zmod_mk</span> <span class="n">a</span> <span class="n">n</span><span class="o">)</span> <span class="err">^</span> <span class="n">order_of</span> <span class="o">(</span><span class="n">units_zmod_mk</span> <span class="n">a</span> <span class="n">n</span><span class="o">),</span> <span class="k">from</span> <span class="n">pow_order_of_eq_one</span> <span class="o">(</span><span class="n">units_zmod_mk</span> <span class="n">a</span> <span class="n">n</span><span class="o">),</span>
</pre></div>


<p>instead of </p>
<div class="codehilite"><pre><span></span><span class="k">have</span>  <span class="o">:</span> <span class="o">(</span><span class="n">units_zmod_mk</span> <span class="n">a</span> <span class="n">n</span> <span class="n">em</span><span class="o">)</span> <span class="err">^</span> <span class="n">order_of</span> <span class="o">(</span><span class="n">units_zmod_mk</span> <span class="n">a</span> <span class="n">n</span> <span class="n">em</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">,</span> <span class="k">from</span> <span class="n">pow_order_of_eq_one</span> <span class="o">(</span><span class="n">units_zmod_mk</span> <span class="n">a</span> <span class="n">n</span> <span class="n">em</span><span class="o">),</span>
</pre></div>


<p>and I have defined above </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">units_zmod_mk</span> <span class="o">(</span><span class="n">a</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">coprime</span> <span class="n">a</span> <span class="n">n</span><span class="o">)</span> <span class="o">[</span><span class="n">pos_nat</span> <span class="n">n</span><span class="o">]</span> <span class="o">:</span> <span class="n">units</span> <span class="o">(</span><span class="n">zmod</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span>
    <span class="n">val</span> <span class="o">:=</span> <span class="n">a</span><span class="o">,</span>
    <span class="n">inv</span> <span class="o">:=</span> <span class="n">a</span><span class="bp">⁻¹</span><span class="o">,</span>
    <span class="n">val_inv</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">mul_inv_eq_gcd</span> <span class="n">n</span> <span class="n">a</span><span class="o">,</span> <span class="n">coprime</span><span class="bp">.</span><span class="n">gcd_eq_one</span> <span class="n">h</span><span class="o">]</span><span class="bp">;</span><span class="n">dsimp</span><span class="bp">;</span><span class="n">rw</span> <span class="n">zero_add</span><span class="o">,</span>
    <span class="n">inv_val</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">mul_comm</span><span class="o">,</span> <span class="n">mul_inv_eq_gcd</span> <span class="n">n</span> <span class="n">a</span><span class="o">,</span> <span class="n">coprime</span><span class="bp">.</span><span class="n">gcd_eq_one</span> <span class="n">h</span><span class="o">]</span><span class="bp">;</span><span class="n">dsimp</span><span class="bp">;</span><span class="n">rw</span> <span class="n">zero_add</span><span class="o">,</span>
<span class="o">}</span>
</pre></div>

#### [ Guy Leroy (Aug 14 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132121924):
<p>Okay thanks Mario</p>

#### [ Mario Carneiro (Aug 14 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132122004):
<p>I assume the <code>decidable_eq</code> goal is coming from <code>order_of</code></p>

#### [ Guy Leroy (Aug 14 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance/near/132122352):
<p>Very well thanks, I'm slowly trying to get a grasp of instances</p>


{% endraw %}
