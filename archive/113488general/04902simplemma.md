---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04902simplemma.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [simp lemma](https://leanprover-community.github.io/archive/113488general/04902simplemma.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Sep 07 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20lemma/near/133500344):
<p>Should these two be simp lemmas?</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">subset_union_left</span> <span class="o">{</span><span class="n">s₁</span> <span class="n">s₂</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">s₁</span> <span class="err">⊆</span> <span class="n">s₁</span> <span class="err">∪</span> <span class="n">s₂</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">mem_union_left</span> <span class="bp">_</span>

<span class="kn">theorem</span> <span class="n">subset_union_right</span> <span class="o">{</span><span class="n">s₁</span> <span class="n">s₂</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">s₂</span> <span class="err">⊆</span> <span class="n">s₁</span> <span class="err">∪</span> <span class="n">s₂</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">mem_union_right</span> <span class="bp">_</span>
</pre></div>


{% endraw %}
