---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90874Cannotfindinstance.html
---

## Stream: [general](index.html)
### Topic: [Cannot find instance](90874Cannotfindinstance.html)

---


{% raw %}
#### [ AHan (Dec 04 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Cannot%20find%20instance/near/150826554):
<p>In <code>mathlib/data/finsupp.lean</code> the instance <code>has_add</code> of <code>finsupp</code> structure was already proved,<br>
but in t he following example, it failed to synthesize type class instance for <code>has_add</code>...<br>
Don't understand what instance I missed...</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finsupp</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">has_zero</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">has_zero</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">add_monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">add_monoid</span> <span class="n">β</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">β</span><span class="o">]</span>

<span class="kn">lemma</span> <span class="n">support_contain_a&#39;</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span><span class="err">₀</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span><span class="bp">.</span><span class="n">support</span> <span class="err">⊆</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span><span class="bp">.</span><span class="n">support</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


{% endraw %}
