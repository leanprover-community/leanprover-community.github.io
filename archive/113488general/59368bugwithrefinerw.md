---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59368bugwithrefinerw.html
---

## Stream: [general](index.html)
### Topic: [bug with refine + rw](59368bugwithrefinerw.html)

---


{% raw %}
#### [ Kenny Lau (Dec 18 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20refine%20%2B%20rw/near/152093977):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="n">true</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine</span> <span class="n">H</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="bp">_</span><span class="o">),</span> <span class="n">rw</span> <span class="n">h</span> <span class="c1">--fails</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">rewrite tactic failed, lemma is not an equality nor a iff</span>
<span class="cm">state:</span>
<span class="cm">H : (0 = 0 → 0 = 1) → true,</span>
<span class="cm">h : 0 = 0</span>
<span class="cm">⊢ 0 = 1</span>
<span class="cm">-/</span>
<span class="kn">end</span>


<span class="kn">example</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="n">true</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine</span> <span class="n">H</span> <span class="bp">_</span><span class="o">,</span> <span class="n">intro</span> <span class="n">h</span><span class="o">,</span> <span class="n">rw</span> <span class="n">h</span> <span class="c1">--works</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Dec 18 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20refine%20%2B%20rw/near/152094049):
<p>and also workaround:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="n">true</span><span class="o">)</span> <span class="o">:</span> <span class="n">true</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine</span> <span class="n">H</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">change</span> <span class="bp">_</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span> <span class="n">rw</span> <span class="n">h</span> <span class="c1">--works</span>
<span class="kn">end</span>
</pre></div>


{% endraw %}
