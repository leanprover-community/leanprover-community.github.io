---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/35417attributeintro.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [attribute [intro]](https://leanprover-community.github.io/archive/113489newmembers/35417attributeintro.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Oct 19 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/attribute%20%5Bintro%5D/near/136080016):
<p>What does this attribute do? I saw it here:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">Exists</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">intro</span> <span class="o">(</span><span class="n">w</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">p</span> <span class="n">w</span><span class="o">)</span> <span class="o">:</span> <span class="n">Exists</span>

<span class="n">attribute</span> <span class="o">[</span><span class="n">intro</span><span class="o">]</span> <span class="n">Exists</span><span class="bp">.</span><span class="n">intro</span>
</pre></div>


<p>and when I hover it says "introduction rule for backward chaining"</p>


{% endraw %}
