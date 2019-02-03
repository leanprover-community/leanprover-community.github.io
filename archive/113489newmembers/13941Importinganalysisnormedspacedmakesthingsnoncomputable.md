---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/13941Importinganalysisnormedspacedmakesthingsnoncomputable.html
---

## Stream: [new members](index.html)
### Topic: [Importing analysis.normed_spaced makes things noncomputable](13941Importinganalysisnormedspacedmakesthingsnoncomputable.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Dec 18 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Importing%20analysis.normed_spaced%20makes%20things%20noncomputable/near/152088656):
<p>The following code:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">def</span> <span class="n">seq</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">:=</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">ℝ</span>
<span class="n">def</span> <span class="n">seq_add</span> <span class="o">:</span> <span class="n">seq</span> <span class="bp">→</span> <span class="n">seq</span> <span class="bp">→</span> <span class="n">seq</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">s</span> <span class="n">t</span> <span class="n">n</span><span class="o">,</span> <span class="n">s</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">t</span> <span class="n">n</span>
</pre></div>


<p>Works perfectly fine, but if I add <code>import analysis.normed_space</code>to the top, <code>seq_add</code> becomes noncomputable, it <code>depends on real.normed_field</code>. But this line works perfectly with or without the import:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">seq_smul</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="n">seq</span> <span class="bp">→</span> <span class="n">seq</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">s</span> <span class="n">n</span><span class="o">,</span> <span class="n">c</span> <span class="bp">*</span> <span class="o">(</span><span class="n">s</span> <span class="n">n</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Dec 18 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Importing%20analysis.normed_spaced%20makes%20things%20noncomputable/near/152088730):
<p>hm, I guess the instance priorities need adjustment</p>


{% endraw %}
