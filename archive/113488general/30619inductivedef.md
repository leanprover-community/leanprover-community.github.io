---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30619inductivedef.html
---

## Stream: [general](index.html)
### Topic: [inductive def](30619inductivedef.html)

---


{% raw %}
#### [ Patrick Massot (Dec 01 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20def/near/150691842):
<p>I very rarely use inductive def so I'm a bit confused by:</p>
<div class="codehilite"><pre><span></span><span class="c1">-- Works ok</span>
<span class="n">def</span> <span class="n">find</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="n">a</span> <span class="o">[]</span>     <span class="o">:=</span> <span class="n">ff</span>
<span class="bp">|</span> <span class="n">a</span> <span class="o">(</span><span class="n">h</span><span class="bp">::</span><span class="n">t</span><span class="o">)</span> <span class="o">:=</span> <span class="k">if</span> <span class="o">(</span><span class="n">a</span> <span class="bp">=</span> <span class="n">h</span><span class="o">)</span> <span class="k">then</span> <span class="n">tt</span> <span class="k">else</span> <span class="n">find</span> <span class="n">a</span> <span class="n">t</span>

<span class="c1">-- Lean complains: type mismatch at application  find&#39; a, term  a has type  ℕ but is expected to have type   list ℕ</span>
<span class="n">def</span> <span class="n">find&#39;</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="o">[]</span>     <span class="o">:=</span> <span class="n">ff</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">h</span><span class="bp">::</span><span class="n">t</span><span class="o">)</span> <span class="o">:=</span> <span class="k">if</span> <span class="o">(</span><span class="n">a</span> <span class="bp">=</span> <span class="n">h</span><span class="o">)</span> <span class="k">then</span> <span class="n">tt</span> <span class="k">else</span> <span class="n">find&#39;</span> <span class="n">a</span> <span class="n">t</span>
</pre></div>


<p>Is there a way to get something like my second attempt to work?</p>

#### [ Gabriel Ebner (Dec 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20def/near/150691886):
<p><code>find' t</code> (without the <code>a</code>)</p>

#### [ Gabriel Ebner (Dec 01 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20def/near/150692066):
<p>(The parameters before the colon---<code>a</code> in this case---are assumed to be constant in the recursive calls, so you don't have to repeat them.)</p>

#### [ Kevin Buzzard (Dec 01 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20def/near/150692420):
<p>That used to confuse me so much. </p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">eq</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">refl</span> <span class="o">:</span> <span class="n">eq</span> <span class="n">a</span>
</pre></div>


<p>I was like "...yeah, but what is <code>a</code> equal to??". It's equal to the <code>a</code> before the colon.</p>

#### [ Patrick Massot (Dec 01 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20def/near/150692857):
<p>Thanks!</p>


{% endraw %}
