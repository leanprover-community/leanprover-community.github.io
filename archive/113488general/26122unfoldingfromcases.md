---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26122unfoldingfromcases.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [unfolding from cases](https://leanprover-community.github.io/archive/113488general/26122unfoldingfromcases.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Nov 28 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20from%20cases/near/148714917):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">+</span> <span class="mi">1</span>

<span class="kn">inductive</span> <span class="n">P</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">p</span> <span class="o">:</span> <span class="n">P</span> <span class="n">x</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">a</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">P</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">4</span> <span class="o">:=</span> <span class="k">begin</span>
  <span class="n">cases</span> <span class="n">h</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>Goal is <code>⊢ nat.succ (nat.add (1 + 1 + 1) 0) = 4</code>. Is all this unfolding expected? I wanted <code>x = 4</code>.</p>

#### [ Kenny Lau (Nov 28 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20from%20cases/near/148716159):
<p>interestingly <code>induction h</code> produces the expected <code>x = 0</code>:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="mi">0</span>

<span class="kn">inductive</span> <span class="n">P</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">p</span> <span class="o">:</span> <span class="n">P</span> <span class="n">x</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">a</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">P</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span> <span class="k">begin</span>
  <span class="n">induction</span> <span class="n">h</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


{% endraw %}
