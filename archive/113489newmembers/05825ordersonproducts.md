---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/05825ordersonproducts.html
---

## Stream: [new members](index.html)
### Topic: [orders on products](05825ordersonproducts.html)

---


{% raw %}
#### [ Alistair Tucker (Dec 08 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151190056):
<p>I want definitions like</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">prod_has_le</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">has_le</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">has_le</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span> <span class="n">has_le</span> <span class="o">(</span><span class="n">prod</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">le</span>            <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="n">a</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">≤</span> <span class="n">b</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">∧</span> <span class="n">a</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">≤</span> <span class="n">b</span><span class="bp">.</span><span class="mi">2</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="n">prod_preorder</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span> <span class="n">preorder</span> <span class="o">(</span><span class="n">prod</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">le_refl</span>       <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">le_refl</span> <span class="n">a</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">le_refl</span> <span class="n">a</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">le_trans</span>      <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">h₁</span> <span class="n">h₂</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">le_trans</span> <span class="n">h₁</span><span class="bp">.</span><span class="mi">1</span> <span class="n">h₂</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">le_trans</span> <span class="n">h₁</span><span class="bp">.</span><span class="mi">2</span> <span class="n">h₂</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="bp">..</span> <span class="n">prod_has_le</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="n">prod_partial_order</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">partial_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">partial_order</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span> <span class="n">partial_order</span> <span class="o">(</span><span class="n">prod</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">le_antisymm</span>   <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">h₁</span> <span class="n">h₂</span><span class="o">,</span> <span class="n">prod</span><span class="bp">.</span><span class="n">ext</span> <span class="o">(</span><span class="n">le_antisymm</span> <span class="n">h₁</span><span class="bp">.</span><span class="mi">1</span> <span class="n">h₂</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">le_antisymm</span> <span class="n">h₁</span><span class="bp">.</span><span class="mi">2</span> <span class="n">h₂</span><span class="bp">.</span><span class="mi">2</span><span class="o">),</span>
  <span class="bp">..</span> <span class="n">prod_preorder</span> <span class="o">}</span>
</pre></div>


<p>(At the moment just for ℕ × ℕ, Cauchy sequences and contraction mapping theorem, but probably for more later on.)</p>
<p>These don't seem already to be in mathlib, so should I assume there is some good reason to exclude them? And if so, can I use some namespace trick to define them 'locally'?</p>

#### [ Kevin Buzzard (Dec 08 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151190145):
<p>I think <code>attribute local instance</code> works for something which is already defined.</p>

#### [ Kevin Buzzard (Dec 08 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151190211):
<p>For example this is from TPIL:</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">classical</span>
<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">prop_decidable</span>
</pre></div>


<p>(after <code>prop_decidable</code> has been defined)</p>

#### [ Kevin Buzzard (Dec 08 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151190359):
<p>"However, such commands can often be prefixed with the local modifier, which indicates that they only have effect until the current section or namespace is closed, or until the end of the current file."</p>

#### [ Alistair Tucker (Dec 08 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151190458):
<p>Thanks, I'll do that then.</p>

#### [ Kevin Buzzard (Dec 08 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151190659):
<p>It would not surprise me if there were a trick to do it all in one go. Does <code>local instance...</code> not work?</p>

#### [ Kevin Buzzard (Dec 08 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151190672):
<p>Oh! Do you need to import <code>pi_instances</code> or something? Maybe they're there?</p>

#### [ Alistair Tucker (Dec 08 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151194606):
<p>Hmm possibly. I didn't know about pi_instances.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">pi_instances</span>

<span class="n">def</span> <span class="n">a</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="k">if</span> <span class="n">i</span> <span class="k">then</span> <span class="mi">1</span> <span class="k">else</span> <span class="mi">2</span>
<span class="n">def</span> <span class="n">b</span> <span class="o">:</span> <span class="n">bool</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="k">if</span> <span class="n">i</span> <span class="k">then</span> <span class="mi">3</span> <span class="k">else</span> <span class="mi">4</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span>
</pre></div>

#### [ Kevin Buzzard (Dec 08 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151194675):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">pi_instances</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">partial_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">partial_order</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span>
<span class="n">partial_order</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="c1">-- fails</span>
</pre></div>


<p>I thought it might work out of the box. But no.</p>

#### [ Kevin Buzzard (Dec 08 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/orders%20on%20products/near/151194686):
<p>Maybe the reason it's not an instance is that some people might want to use lex order in some cases</p>


{% endraw %}
