---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49720OutdatedexampleinProgramminginLean.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Outdated example in Programming in Lean](https://leanprover-community.github.io/archive/113488general/49720OutdatedexampleinProgramminginLean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Miko de Amsterdamo (May 01 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Outdated%20example%20in%20Programming%20in%20Lean/near/125939264):
<p>The example didn't work with my lean 3.3.0. It seems that <code>for</code> has become <code>map</code></p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">destruct_conjunctions</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">repeat</span> <span class="o">(</span><span class="n">do</span>
  <span class="n">l</span> <span class="err">←</span> <span class="n">local_context</span><span class="o">,</span>
  <span class="n">first</span> <span class="err">$</span> <span class="n">l</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">do</span>
    <span class="n">ht</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">h</span> <span class="bp">&gt;&gt;=</span> <span class="n">whnf</span><span class="o">,</span>
    <span class="k">match</span> <span class="n">ht</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="n">and</span> <span class="err">%%</span><span class="n">a</span> <span class="err">%%</span><span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="n">do</span>
      <span class="n">n</span> <span class="err">←</span> <span class="n">mk_fresh_name</span><span class="o">,</span>
      <span class="n">mk_mapp</span> <span class="bp">``</span><span class="n">and</span><span class="bp">.</span><span class="n">left</span> <span class="o">[</span><span class="n">none</span><span class="o">,</span> <span class="n">none</span><span class="o">,</span> <span class="n">some</span> <span class="n">h</span><span class="o">]</span> <span class="bp">&gt;&gt;=</span> <span class="n">assertv</span> <span class="n">n</span> <span class="n">a</span><span class="o">,</span>
      <span class="n">n</span> <span class="err">←</span> <span class="n">mk_fresh_name</span><span class="o">,</span>
      <span class="n">mk_mapp</span> <span class="bp">``</span><span class="n">and</span><span class="bp">.</span><span class="n">right</span> <span class="o">[</span><span class="n">none</span><span class="o">,</span> <span class="n">none</span><span class="o">,</span> <span class="n">some</span> <span class="n">h</span><span class="o">]</span> <span class="bp">&gt;&gt;=</span> <span class="n">assertv</span> <span class="n">n</span> <span class="n">b</span><span class="o">,</span>
      <span class="n">clear</span> <span class="n">h</span>
    <span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">failed</span>
    <span class="kn">end</span><span class="o">))</span>
</pre></div>


{% endraw %}
