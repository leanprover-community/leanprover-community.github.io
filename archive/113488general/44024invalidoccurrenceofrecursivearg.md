---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/44024invalidoccurrenceofrecursivearg.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [invalid occurrence of recursive arg](https://leanprover-community.github.io/archive/113488general/44024invalidoccurrenceofrecursivearg.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Jan 13 2019 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurrence%20of%20recursive%20arg/near/155020104):
<p>What does this error message mean and is there a workaround?</p>
<div class="codehilite"><pre><span></span><span class="kn">universe</span> <span class="n">v</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span>
<span class="kn">inductive</span> <span class="n">closure</span> <span class="o">(</span><span class="n">φ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">clos</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">t</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">},</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">t</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">closure</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">φ</span> <span class="n">t</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">closure</span> <span class="n">x</span>
<span class="c1">-- error: invalid occurrence of recursive arg#5 of &#39;closure.clos&#39;, the body of the functional type depends on it.</span>
</pre></div>

#### [ Reid Barton (Jan 13 2019 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurrence%20of%20recursive%20arg/near/155021253):
<p>I guess I can just use the impredicative definition</p>

#### [ Kenny Lau (Jan 13 2019 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurrence%20of%20recursive%20arg/near/155021376):
<p>what is the impredicative definition?</p>

#### [ Reid Barton (Jan 13 2019 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurrence%20of%20recursive%20arg/near/155021674):
<p>The intersection of all the closed subsets of α</p>

#### [ Reid Barton (Jan 13 2019 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurrence%20of%20recursive%20arg/near/155021995):
<p><code>def closure (φ : set α → set α) : set α := ⋂₀ {s | ∀ t, t ⊆ s → φ t ⊆ s}</code></p>

#### [ Gabriel Ebner (Jan 13 2019 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurrence%20of%20recursive%20arg/near/155022395):
<p>FTFY:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">closure</span> <span class="o">(</span><span class="n">φ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">clos</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">t</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">},</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">t</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">closure</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">φ</span> <span class="n">t</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">closure</span> <span class="n">x</span>
</pre></div>

#### [ Gabriel Ebner (Jan 13 2019 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurrence%20of%20recursive%20arg/near/155022473):
<p>Lean is a bit picky about the order of the arguments to constructors.  A long time ago, you couldn't even write <code>| node : tree → α → tree → tree</code> (you had to write <code>α</code> at the beginning and not in the middle).</p>

#### [ Reid Barton (Jan 13 2019 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20occurrence%20of%20recursive%20arg/near/155022542):
<p>Interesting, thanks!</p>


{% endraw %}
