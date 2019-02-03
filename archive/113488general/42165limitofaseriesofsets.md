---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42165limitofaseriesofsets.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [limit of a series of sets](https://leanprover-community.github.io/archive/113488general/42165limitofaseriesofsets.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Simon Hudon (Apr 06 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/limit%20of%20a%20series%20of%20sets/near/124704503):
<p>I have an infinite series of sets that each include their successor and such that each is non-empty. How do I prove that the intersection of all sets is also non-empty?</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span>
   <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">stream</span> <span class="o">(</span><span class="n">set</span> <span class="n">α</span><span class="o">))</span>
   <span class="o">(</span><span class="n">h₀</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">s</span> <span class="n">i</span> <span class="bp">≠</span> <span class="err">∅</span><span class="o">)</span>
   <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span><span class="o">,</span> <span class="n">s</span> <span class="o">(</span><span class="n">i</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="err">⊆</span> <span class="n">s</span> <span class="n">i</span><span class="o">)</span>
<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="err">⋂</span> <span class="n">i</span><span class="o">,</span> <span class="n">s</span> <span class="n">i</span><span class="o">)</span> <span class="bp">≠</span> <span class="err">∅</span> <span class="o">:=</span> <span class="bp">...</span>
</pre></div>

#### [ Mario Carneiro (Apr 06 2018 at 07:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/limit%20of%20a%20series%20of%20sets/near/124705712):
<p>it's false? For example take <code>s n := {m : nat // n &lt;= m}</code></p>

#### [ Kenny Lau (Apr 06 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/limit%20of%20a%20series%20of%20sets/near/124705718):
<p>right, it’s false</p>

#### [ Kenny Lau (Apr 06 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/limit%20of%20a%20series%20of%20sets/near/124705719):
<p>i was thinking for 5 minutes whether it is true or false</p>

#### [ Kenny Lau (Apr 06 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/limit%20of%20a%20series%20of%20sets/near/124705721):
<p>take (0,1/n)</p>

#### [ Simon Hudon (Apr 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/limit%20of%20a%20series%20of%20sets/near/124716057):
<p>Damn it! You guys are right! I was hoping to generalize a theorem. I guess I'll have to keep thinking about restrictions</p>

#### [ Chris Hughes (Apr 06 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/limit%20of%20a%20series%20of%20sets/near/124719698):
<p>(deleted)</p>


{% endraw %}
