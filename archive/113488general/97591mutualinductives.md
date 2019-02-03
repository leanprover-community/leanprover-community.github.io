---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/97591mutualinductives.html
---

## Stream: [general](index.html)
### Topic: [mutual inductives](97591mutualinductives.html)

---


{% raw %}
#### [ Chris Hughes (Nov 04 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mutual%20inductives/near/137132804):
<p>What's the "canonical" proof that the Types A and B are empty. I proved it by reference to the auxiliary <code>A._mut_</code>. Is there a nicer way?</p>
<div class="codehilite"><pre><span></span><span class="n">mutual</span> <span class="kn">inductive</span> <span class="n">A</span><span class="o">,</span> <span class="n">B</span>
<span class="k">with</span> <span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">mk</span> <span class="o">:</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">A</span>
<span class="k">with</span> <span class="n">B</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">mk</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span>
</pre></div>

#### [ Kenny Lau (Nov 04 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mutual%20inductives/near/137132957):
<div class="codehilite"><pre><span></span><span class="n">mutual</span> <span class="kn">inductive</span> <span class="n">A</span><span class="o">,</span> <span class="n">B</span>
<span class="k">with</span> <span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">mk</span> <span class="o">:</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">A</span>
<span class="k">with</span> <span class="n">B</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">mk</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">B</span>

<span class="n">def</span> <span class="n">A</span><span class="bp">.</span><span class="n">to_sort</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">)</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">l</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">A</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">B</span><span class="bp">.</span><span class="n">mk</span> <span class="n">x</span><span class="o">))</span> <span class="o">:=</span> <span class="n">A</span><span class="bp">.</span><span class="n">to_sort</span> <span class="n">x</span>
</pre></div>

#### [ Chris Hughes (Nov 04 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mutual%20inductives/near/137132960):
<p>Of course.</p>

#### [ Chris Hughes (Nov 04 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mutual%20inductives/near/137133128):
<p>Are there any recursors that look a bit like this?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">AB</span><span class="bp">.</span><span class="n">reca</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">Ca</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">Cb</span> <span class="o">:</span> <span class="n">B</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span>
  <span class="o">(</span><span class="n">ha</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">a</span> <span class="o">:</span> <span class="n">A</span><span class="o">,</span> <span class="n">Ca</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">Cb</span> <span class="o">(</span><span class="n">B</span><span class="bp">.</span><span class="n">mk</span> <span class="n">a</span><span class="o">))</span>
  <span class="o">(</span><span class="n">hb</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">b</span> <span class="o">:</span> <span class="n">B</span><span class="o">,</span> <span class="n">Cb</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">Ca</span> <span class="o">(</span><span class="n">A</span><span class="bp">.</span><span class="n">mk</span> <span class="n">b</span><span class="o">))</span>
  <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">A</span><span class="o">),</span> <span class="n">Ca</span> <span class="n">a</span>
</pre></div>

#### [ Kenny Lau (Nov 04 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mutual%20inductives/near/137133175):
<p>you can write one</p>


{% endraw %}
