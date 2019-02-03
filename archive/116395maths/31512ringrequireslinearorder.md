---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/31512ringrequireslinearorder.html
---

## Stream: [maths](index.html)
### Topic: [ring requires linear order](31512ringrequireslinearorder.html)

---


{% raw %}
#### [ Chris Hughes (Dec 02 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20requires%20linear%20order/near/150704740):
<p>Is this a non-trivial upgrade? The support for division in ring only works on ordered fields.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span> <span class="n">data</span><span class="bp">.</span><span class="n">complex</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">/</span> <span class="mi">3</span> <span class="bp">+</span> <span class="n">x</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">5</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">/</span> <span class="mi">6</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">ring</span> <span class="c1">--works</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">/</span> <span class="mi">3</span> <span class="bp">+</span> <span class="n">x</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">5</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">/</span> <span class="mi">6</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">ring</span> <span class="c1">--fails</span>
</pre></div>

#### [ Kevin Buzzard (Dec 02 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ring%20requires%20linear%20order/near/150717509):
<p>I vaguely remember a conversation at one point where I asked Mario why something had to be ordered, and at the time it was because actually the thing had to be characteristic zero and there was no characteristic zero predicate at the time, but ordered implied it</p>


{% endraw %}
