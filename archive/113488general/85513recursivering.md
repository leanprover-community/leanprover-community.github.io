---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85513recursivering.html
---

## Stream: [general](index.html)
### Topic: [recursive ring](85513recursivering.html)

---


{% raw %}
#### [ Patrick Massot (May 29 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20ring/near/127272896):
<p>Is that a bug?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span>  <span class="bp">-</span><span class="n">x</span><span class="bp">*</span><span class="n">y</span><span class="bp">*</span><span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="n">b</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span> <span class="bp">+</span> <span class="n">y</span><span class="bp">*</span><span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="n">y</span><span class="o">)</span><span class="bp">*</span><span class="n">a</span><span class="err">^</span><span class="mi">2</span> <span class="bp">+</span> <span class="n">x</span><span class="bp">*</span><span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="n">y</span><span class="o">)</span><span class="bp">*</span><span class="n">b</span><span class="err">^</span><span class="mi">2</span> <span class="bp">-</span> <span class="o">(</span><span class="n">a</span><span class="bp">*</span><span class="n">y</span><span class="bp">-</span><span class="n">b</span><span class="bp">*</span><span class="n">x</span><span class="o">)</span><span class="err">^</span><span class="mi">2</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">ring</span><span class="o">,</span>
  <span class="n">ring</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (May 29 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20ring/near/127273575):
<p>so <code>ring</code> is not idempotent ^^</p>

#### [ Mario Carneiro (May 29 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20ring/near/127273638):
<p><code>ring</code> has a bug in it currently</p>

#### [ Mario Carneiro (May 29 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20ring/near/127273640):
<p>I think there's an issue for it</p>

#### [ Patrick Massot (May 29 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20ring/near/127273728):
<p>The example in the issue actually works here</p>

#### [ Mario Carneiro (May 29 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20ring/near/127273791):
<p>It's because when <code>ring</code> fails, it tries to rewrite the expression into a "nice" SOP form, and this rewriting causes it to circumvent the bug the second time around</p>

#### [ Sebastian Ullrich (May 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20ring/near/127273899):
<p><code>begin ring, ring, ring, ring, ring, ring, ring, banana_phone end</code></p>

#### [ Patrick Massot (May 29 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20ring/near/127274422):
<p>I really mean: I copy and paste the example in the github issue and it works here</p>


{% endraw %}
