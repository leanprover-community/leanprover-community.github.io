---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52473monotonicitylemma.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [monotonicity lemma](https://leanprover-community.github.io/archive/113488general/52473monotonicitylemma.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Rob Lewis (Sep 28 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/monotonicity%20lemma/near/134821924):
<p>I feel like this lemma (or similar) must exist somewhere already, but I'm coming up empty -- anyone recognize this?</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">partial_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">f</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">f</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">m</span> <span class="n">n</span><span class="o">,</span> <span class="n">m</span> <span class="bp">≤</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">n</span> <span class="bp">≤</span> <span class="n">f</span> <span class="n">m</span>
</pre></div>


{% endraw %}
