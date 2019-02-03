---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67899existsdata.html
---

## Stream: [general](index.html)
### Topic: [exists data](67899existsdata.html)

---


{% raw %}
#### [ Johan Commelin (Dec 24 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20data/near/152455922):
<p>Is there a clean way to avoid the <code>, true</code> in this condition?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">generate_sieve</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">covering_family</span> <span class="n">U</span><span class="o">)</span> <span class="o">:</span> <span class="n">covering_family</span> <span class="n">U</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">V</span> <span class="o">:</span> <span class="n">over</span> <span class="n">U</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">Ui</span> <span class="o">:</span> <span class="n">over</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">hUi</span> <span class="o">:</span> <span class="n">Ui</span> <span class="err">∈</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">V</span> <span class="err">⟶</span> <span class="n">Ui</span><span class="o">),</span> <span class="n">true</span> <span class="o">}</span>
</pre></div>


<p>I guess I should use <code>nonempty</code>? Somehow, that doesn't feel clean to me, and in the past I found it harder to use.</p>

#### [ Mario Carneiro (Dec 24 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20data/near/152456610):
<p>that's <code>nonempty</code></p>

#### [ Mario Carneiro (Dec 24 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20data/near/152456613):
<p><code>{ V : over U | ∃ Ui ∈ c, nonempty (V ⟶ Ui) }</code></p>

#### [ Johan Commelin (Dec 24 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20data/near/152456723):
<p>Ok, I'll try using it again.</p>


{% endraw %}
