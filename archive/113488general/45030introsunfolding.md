---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45030introsunfolding.html
---

## Stream: [general](index.html)
### Topic: [intros unfolding](45030introsunfolding.html)

---


{% raw %}
#### [ Patrick Massot (Jun 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intros%20unfolding/near/128723966):
<p>Is this normal?</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span>  <span class="o">:</span> <span class="n">P</span> <span class="bp">→</span> <span class="n">Q</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">intros</span><span class="o">,</span> <span class="c1">-- context has a: P, goal is now Q</span>
<span class="n">sorry</span>
<span class="kn">end</span>

<span class="n">def</span> <span class="n">f</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:=</span> <span class="n">P</span> <span class="bp">→</span> <span class="n">Q</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span>  <span class="o">:</span> <span class="n">f</span> <span class="n">P</span> <span class="n">Q</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">intros</span><span class="o">,</span> <span class="c1">-- nothing happen :-(</span>
<span class="n">intros</span> <span class="n">a</span><span class="o">,</span> <span class="c1">-- context is a : P, goal is now Q</span>
<span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>It seems this prevents <code>finish</code> to work successfully in some cases without a preliminary <code>intros a b c d e f</code></p>

#### [ Kevin Buzzard (Jun 27 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intros%20unfolding/near/128724587):
<p>that's kind of interesting. If you make f reducible, or unfold it explicitly, maybe <code>intros</code> works.</p>

#### [ Patrick Massot (Jun 27 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intros%20unfolding/near/128725099):
<p>Of course explicit unfolding works. But reducible is not enough.</p>

#### [ Simon Hudon (Jun 27 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/intros%20unfolding/near/128725144):
<p>you can also try <code>intros _</code></p>


{% endraw %}
