---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/06660metatacticwithunfold.html
---

## Stream: [new members](index.html)
### Topic: [meta tactic with unfold](06660metatacticwithunfold.html)

---


{% raw %}
#### [ Sarah Mameche (Nov 19 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/meta%20tactic%20with%20unfold/near/147963936):
<p>Is there an equivalent to 'tactic.apply' with unfold? I have a <code>meta</code>tactic that rewrites with specific lemmas which are given as a <code>pexpr</code> : </p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">rw_pexpr</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">pexpr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">e</span> <span class="err">←</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">to_expr</span> <span class="n">e</span><span class="o">,</span>
  <span class="n">t</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
  <span class="o">(</span><span class="n">p</span><span class="o">,</span><span class="n">h</span><span class="o">,</span><span class="bp">_</span><span class="o">)</span> <span class="err">←</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">rewrite</span> <span class="n">e</span> <span class="n">t</span><span class="o">,</span>
  <span class="n">replace_target</span> <span class="n">p</span> <span class="n">h</span>
</pre></div>


<p>It works for rewriting if the <code>pexpr</code>is a lemma, but not if it is a definition (even though doing rw with the definition interactively works). What can I do if I want to unfold the definition using the meta tactic?</p>

#### [ Mario Carneiro (Nov 19 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/meta%20tactic%20with%20unfold/near/147964349):
<p>use <code>get_equation_lemmas</code> to get a list of simp lemmas for a definition</p>


{% endraw %}
