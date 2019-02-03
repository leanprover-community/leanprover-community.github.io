---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83252nonemptyquotient.html
---

## Stream: [general](index.html)
### Topic: [nonempty quotient](83252nonemptyquotient.html)

---


{% raw %}
#### [ Patrick Massot (Sep 30 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nonempty%20quotient/near/134934075):
<p>Do we already have something like:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">nonempty_quotient_iff</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">nonempty</span> <span class="o">(</span><span class="n">quotient</span> <span class="n">s</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">nonempty</span> <span class="n">α</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span> <span class="bp">;</span> <span class="n">rintro</span> <span class="bp">⟨</span><span class="n">c</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">cases</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">exists_rep</span> <span class="n">c</span> <span class="k">with</span> <span class="n">a</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">exact</span> <span class="bp">⟨</span><span class="n">a</span><span class="bp">⟩</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="err">⟦</span><span class="n">c</span><span class="err">⟧</span><span class="bp">⟩</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Sep 30 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nonempty%20quotient/near/134935619):
<p>That would be in <code>data/quot</code> and I don't see it there.</p>


{% endraw %}
