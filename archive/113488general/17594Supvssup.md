---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17594Supvssup.html
---

## Stream: [general](index.html)
### Topic: [Sup vs sup](17594Supvssup.html)

---


{% raw %}
#### [ Johan Commelin (Dec 06 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sup%20vs%20sup/near/150984986):
<p>Is there something in mathlib expressing compatibility between <code>Sup</code> and <code>sup</code> for complete lattices?<br>
I would expect something like</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">Sup_eq_sup</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span> <span class="n">Sup</span> <span class="o">{</span><span class="n">x</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">a</span> <span class="err">\</span><span class="n">or</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">b</span><span class="o">}</span> <span class="bp">=</span> <span class="n">a</span> <span class="err">\</span><span class="n">sqcup</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Mario Carneiro (Dec 06 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sup%20vs%20sup/near/150985082):
<p>that's <code>Sup {a, b}</code> on the left, did you look for that?</p>

#### [ Mario Carneiro (Dec 06 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sup%20vs%20sup/near/150985130):
<p>also it might be expressed in terms of <code>Sup (insert a s)</code></p>

#### [ Johan Commelin (Dec 06 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Sup%20vs%20sup/near/150985153):
<p>Aah, there is a <code>Sup_insert</code>. And that can be chained with <code>Sup_singleton</code></p>


{% endraw %}
