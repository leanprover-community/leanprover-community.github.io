---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86728usinginductionhypothesisinmatch.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [using induction hypothesis in match](https://leanprover-community.github.io/archive/113488general/86728usinginductionhypothesisinmatch.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Jan 27 2019 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20induction%20hypothesis%20in%20match/near/156987200):
<p>Why does the second one work but not the first?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">id1</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">x</span> <span class="k">with</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">_</span><span class="n">match</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span> <span class="c1">--fails</span>
<span class="kn">end</span>

<span class="n">def</span> <span class="n">id2</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">x</span> <span class="k">with</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">exact</span> <span class="bp">_</span><span class="n">match</span> <span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span> <span class="c1">--works</span>
<span class="kn">end</span>
</pre></div>

#### [ Mohammad Pedramfar (Jan 27 2019 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20induction%20hypothesis%20in%20match/near/156987454):
<p>(deleted)</p>

#### [ Sebastian Ullrich (Jan 27 2019 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20induction%20hypothesis%20in%20match/near/156987699):
<p>Because the first one is intended to not work and the second one is not intended to work</p>

#### [ Bryan Gin-ge Chen (Jan 27 2019 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20induction%20hypothesis%20in%20match/near/156987903):
<p>I noticed this too, back <a href="#narrow/stream/113489-new-members/topic/Recursively.20prove/near/137114175" title="#narrow/stream/113489-new-members/topic/Recursively.20prove/near/137114175">here</a>; I guess we're "supposed to" put <code>x</code> to the right of the colon like Mario did in that thread.</p>

#### [ Chris Hughes (Jan 27 2019 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20induction%20hypothesis%20in%20match/near/156989018):
<p>Sometimes <code>x</code> isn't an argument to the function however, it's something defined later.</p>

#### [ Mario Carneiro (Jan 27 2019 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using%20induction%20hypothesis%20in%20match/near/156989577):
<p>the "official" solution is to just have an auxiliary function, or use <code>induction</code> to construct the function. In lean 4, if my suggestion to sebastian worked, we will have an actual term mode notation for this using <code>let</code></p>


{% endraw %}
