---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21663behaviourofsimpachanged.html
---

## Stream: [general](index.html)
### Topic: [behaviour of simpa changed](21663behaviourofsimpachanged.html)

---


{% raw %}
#### [ Chris Hughes (Sep 05 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/behaviour%20of%20simpa%20changed/near/133365192):
<p>A few of my proofs have broken since the recent changes to <code>simpa</code>. For example this one.</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">zero_pow</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">hn</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">cases</span> <span class="n">n</span><span class="bp">;</span> <span class="n">simpa</span> <span class="o">[</span><span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">pow_succ</span><span class="o">,</span> <span class="n">lt_irrefl</span><span class="o">]</span> <span class="kn">using</span> <span class="n">hn</span>
</pre></div>


<p>It fails if it solves the goal without using <code>hn</code></p>

#### [ Mario Carneiro (Sep 05 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/behaviour%20of%20simpa%20changed/near/133392023):
<p>You should just use <code>by cases n; simp [_root_.pow_succ, lt_irrefl, hn]</code> here. <code>simpa</code> is not supposed to be a replacement for <code>simp</code></p>


{% endraw %}
