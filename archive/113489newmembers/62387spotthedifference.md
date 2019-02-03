---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/62387spotthedifference.html
---

## Stream: [new members](index.html)
### Topic: [spot the difference](62387spotthedifference.html)

---


{% raw %}
#### [ Kenny Lau (Jan 11 2019 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/spot%20the%20difference/near/154913709):
<div class="codehilite"><pre><span></span><span class="n">invalid</span> <span class="n">type</span> <span class="n">ascription</span><span class="o">,</span> <span class="n">term</span> <span class="n">has</span> <span class="n">type</span>
  <span class="bp">@</span><span class="n">function</span><span class="bp">.</span><span class="n">injective</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span> <span class="mi">1</span><span class="o">}</span> <span class="o">(</span><span class="n">pre_von_Neumann</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">pre_von_Neumann</span> <span class="n">m</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_rec_on</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span><span class="o">}</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">),</span> <span class="n">pre_von_Neumann</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">),</span> <span class="bp">@</span><span class="n">pre_von_Neumann</span><span class="bp">.</span><span class="n">next</span> <span class="n">n</span><span class="o">)</span> <span class="n">n</span> <span class="n">m</span> <span class="n">H</span><span class="o">)</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="bp">@</span><span class="n">function</span><span class="bp">.</span><span class="n">injective</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span> <span class="mi">1</span><span class="o">}</span> <span class="o">(</span><span class="n">pre_von_Neumann</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">pre_von_Neumann</span> <span class="n">m</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_rec_on</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span><span class="o">}</span> <span class="n">pre_von_Neumann</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">),</span> <span class="bp">@</span><span class="n">pre_von_Neumann</span><span class="bp">.</span><span class="n">next</span> <span class="n">n</span><span class="o">)</span> <span class="n">n</span> <span class="n">m</span> <span class="n">H</span><span class="o">)</span>

<span class="n">state</span><span class="o">:</span>
<span class="n">n</span> <span class="n">m</span> <span class="o">:</span> <span class="n">nat</span><span class="o">,</span>
<span class="n">H</span> <span class="o">:</span> <span class="bp">@</span><span class="n">has_le</span><span class="bp">.</span><span class="n">le</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span> <span class="n">nat</span> <span class="n">nat</span><span class="bp">.</span><span class="n">has_le</span> <span class="n">n</span> <span class="n">m</span>
<span class="err">⊢</span> <span class="bp">@</span><span class="n">function</span><span class="bp">.</span><span class="n">injective</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span> <span class="mi">1</span><span class="o">}</span> <span class="o">(</span><span class="n">pre_von_Neumann</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">pre_von_Neumann</span> <span class="n">m</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_rec_on</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span><span class="o">}</span> <span class="n">pre_von_Neumann</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">),</span> <span class="bp">@</span><span class="n">pre_von_Neumann</span><span class="bp">.</span><span class="n">next</span> <span class="n">n</span><span class="o">)</span> <span class="n">n</span> <span class="n">m</span> <span class="n">H</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Jan 11 2019 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/spot%20the%20difference/near/154913801):
<p>Ouch... that must hurt. <code>(λ (n : nat), pre_von_Neumann n)</code> ought to be defeq to <code>pre_von_Neumann</code>.</p>

#### [ Kenny Lau (Jan 11 2019 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/spot%20the%20difference/near/154913885):
<p>ok <code>convert [...]; ext; refl</code> worked</p>

#### [ Kenny Lau (Jan 11 2019 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/spot%20the%20difference/near/154914109):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> will this be fixed in Lean 4?</p>

#### [ Kenny Lau (Jan 11 2019 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/spot%20the%20difference/near/154915053):
<p>MWE:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">A</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero</span>     <span class="o">:=</span> <span class="n">empty</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">A</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">empty</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">=</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">A</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">rfl</span> <span class="c1">-- fails</span>
</pre></div>


<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Kevin Buzzard (Jan 11 2019 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/spot%20the%20difference/near/154923694):
<p>"Probably a bug", says Sebastian</p>


{% endraw %}
