---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96716inductionbug.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [induction bug](https://leanprover-community.github.io/archive/113488general/96716inductionbug.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Nov 20 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20bug/near/148074216):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">wtf</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span><span class="o">)</span> <span class="o">:</span> <span class="n">C</span> <span class="n">r</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">r</span> <span class="kn">using</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">induction</span>
  <span class="c">/-</span><span class="cm"></span>
<span class="cm">2 goals</span>
<span class="cm">case h₁</span>
<span class="cm">α : Type u,</span>
<span class="cm">C : multiset α → Prop</span>
<span class="cm">⊢ C 0</span>

<span class="cm">case h₂</span>
<span class="cm">α : Type u,</span>
<span class="cm">C : multiset α → Prop,</span>
<span class="cm">r_a : list α,</span>
<span class="cm">r_s : multiset (list α),</span>
<span class="cm">r_a_1 : C r_s</span>
<span class="cm">⊢ C (r_a :: r_s)</span>
<span class="cm">  -/</span><span class="o">,</span>
  <span class="n">sorry</span><span class="o">,</span> <span class="n">sorry</span>
<span class="kn">end</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">type mismatch at application</span>
<span class="cm">  @multiset.induction (list α)</span>
<span class="cm">term</span>
<span class="cm">  list α</span>
<span class="cm">has type</span>
<span class="cm">  Type u</span>
<span class="cm">but is expected to have type</span>
<span class="cm">  Type (u+1)</span>
<span class="cm">-/</span>
</pre></div>


{% endraw %}
