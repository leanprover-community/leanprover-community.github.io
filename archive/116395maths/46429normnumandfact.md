---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/46429normnumandfact.html
---

## Stream: [maths](index.html)
### Topic: [norm_num and fact](46429normnumandfact.html)

---


{% raw %}
#### [ Kevin Buzzard (Nov 18 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20and%20fact/near/147921330):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span>

<span class="kn">open</span> <span class="n">nat</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">fact</span> <span class="mi">7</span> <span class="bp">≥</span> <span class="mi">3</span> <span class="err">^</span> <span class="mi">7</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="c1">--  unfold fact, norm_num, -- fails, perhaps because of succ&#39;s</span>
  <span class="k">show</span> <span class="mi">7</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">6</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">5</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">4</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">3</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">*</span> <span class="mi">1</span><span class="o">))))))</span> <span class="bp">≥</span> <span class="mi">3</span> <span class="err">^</span> <span class="mi">7</span><span class="o">,</span>
  <span class="n">norm_num</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  Can you get <code>norm_num</code> to know enough about <code>fact</code> to make this work? After unfolding <code>fact</code> I get a goal with a lot of <code>nat.succ</code>'s in. Or is this harder than it looks?</p>

#### [ Mario Carneiro (Nov 18 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20and%20fact/near/147921503):
<p>I think you can rewrite <code>nat.succ</code> to <code>+1</code> and then apply <code>norm_num</code></p>

#### [ Mario Carneiro (Nov 18 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20and%20fact/near/147922308):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">fact</span> <span class="mi">7</span> <span class="bp">≥</span> <span class="mi">3</span> <span class="err">^</span> <span class="mi">7</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">dsimp</span> <span class="n">only</span> <span class="o">[</span><span class="n">fact</span><span class="o">,</span> <span class="n">succ_eq_add_one</span><span class="o">]</span><span class="bp">;</span> <span class="n">norm_num</span>
</pre></div>


{% endraw %}
