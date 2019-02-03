---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53591abbreviation.html
---

## Stream: [general](index.html)
### Topic: [abbreviation](53591abbreviation.html)

---


{% raw %}
#### [ Reid Barton (Dec 03 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abbreviation/near/150746902):
<p>I don't suppose <code>abbreviation</code> is documented anywhere?</p>

#### [ Reid Barton (Dec 03 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abbreviation/near/150746904):
<p>It seems to do something very specific that I want (MWE incoming)</p>

#### [ Reid Barton (Dec 03 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abbreviation/near/150746954):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">test1</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">has_add</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">x</span>
<span class="bp">@</span><span class="o">[</span><span class="n">class</span><span class="o">,</span> <span class="kn">reducible</span><span class="o">]</span> <span class="n">def</span> <span class="n">my_add</span> <span class="o">:=</span> <span class="n">has_add</span>
<span class="n">def</span> <span class="n">test2</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">my_add</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">x</span> <span class="c1">-- failed to synthesize type class instance for has_add α</span>
<span class="kn">abbreviation</span> <span class="n">my_add&#39;</span> <span class="o">:=</span> <span class="n">has_add</span>
<span class="n">def</span> <span class="n">test3</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">my_add&#39;</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">x</span> <span class="c1">-- ok!</span>
</pre></div>

#### [ Reid Barton (Dec 03 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abbreviation/near/150746955):
<p>Is there a catch?</p>

#### [ Reid Barton (Dec 03 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abbreviation/near/150747018):
<p>You can also do more interesting things like <code>abbreviation my_add' (α : Type) := has_add (list α)</code></p>


{% endraw %}
