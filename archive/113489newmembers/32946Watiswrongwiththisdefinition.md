---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/32946Watiswrongwiththisdefinition.html
---

## Stream: [new members](index.html)
### Topic: [Wat is wrong with this definition?](32946Watiswrongwiththisdefinition.html)

---


{% raw %}
#### [ Ken Roe (Jul 24 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Wat%20is%20wrong%20with%20this%20definition%3F/near/130214027):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">evv</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">-&gt;</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">Base</span> <span class="o">:=</span> <span class="o">(</span><span class="n">evv</span> <span class="mi">0</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">Inductive</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">even</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">even</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span><span class="bp">.</span>
</pre></div>


<p>gives the following error:</p>
<div class="codehilite"><pre><span></span><span class="n">invalid</span> <span class="n">return</span> <span class="n">type</span> <span class="n">for</span> <span class="err">&#39;</span><span class="n">evv</span><span class="bp">.</span><span class="n">Base&#39;</span>
</pre></div>

#### [ Simon Hudon (Jul 24 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Wat%20is%20wrong%20with%20this%20definition%3F/near/130214285):
<p>Try:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">evv</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">-&gt;</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">Base</span> <span class="o">:</span> <span class="o">(</span><span class="n">evv</span> <span class="mi">0</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">Inductive</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">evv</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">evv</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span><span class="bp">.</span>
</pre></div>


{% endraw %}
