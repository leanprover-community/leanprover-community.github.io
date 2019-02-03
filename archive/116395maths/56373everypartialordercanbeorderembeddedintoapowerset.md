---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/56373everypartialordercanbeorderembeddedintoapowerset.html
---

## Stream: [maths](index.html)
### Topic: [every partial order can be order-embedded into a powerset](56373everypartialordercanbeorderembeddedintoapowerset.html)

---


{% raw %}
#### [ Kenny Lau (Apr 27 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125781096):
<div class="codehilite"><pre><span></span><span class="kn">section</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">partial_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>

<span class="n">def</span> <span class="n">partial_order</span><span class="bp">.</span><span class="n">embed</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">z</span> <span class="bp">|</span> <span class="n">z</span> <span class="bp">≤</span> <span class="n">x</span> <span class="o">}</span>

<span class="kn">theorem</span> <span class="n">partial_order</span><span class="bp">.</span><span class="n">embed</span><span class="bp">.</span><span class="n">injective</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">injective</span> <span class="o">(</span><span class="bp">@</span><span class="n">partial_order</span><span class="bp">.</span><span class="n">embed</span> <span class="n">α</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">hxy</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H1</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">partial_order</span><span class="bp">.</span><span class="n">embed</span> <span class="n">y</span><span class="o">,</span> <span class="k">from</span> <span class="n">hxy</span> <span class="bp">▸</span> <span class="n">le_refl</span> <span class="bp">_</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">partial_order</span><span class="bp">.</span><span class="n">embed</span> <span class="n">x</span><span class="o">,</span> <span class="k">from</span> <span class="n">hxy</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">le_refl</span> <span class="bp">_</span><span class="o">,</span>
<span class="n">le_antisymm</span> <span class="n">H1</span> <span class="n">H2</span>

<span class="kn">theorem</span> <span class="n">partial_order</span><span class="bp">.</span><span class="n">embed</span><span class="bp">.</span><span class="n">ord</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">partial_order</span><span class="bp">.</span><span class="n">embed</span> <span class="n">x</span> <span class="err">⊆</span> <span class="n">partial_order</span><span class="bp">.</span><span class="n">embed</span> <span class="n">y</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">z</span> <span class="n">hz</span><span class="o">,</span> <span class="n">le_trans</span> <span class="n">hz</span> <span class="n">H</span>

<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Apr 27 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125781102):
<p>is there a more compact version of the title using category language?</p>

#### [ Kenny Lau (Apr 27 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125781113):
<p>and I used all three properties of a partial order</p>

#### [ Kenny Lau (Apr 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125781335):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">converse</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">r</span> <span class="err">≼</span><span class="n">o</span> <span class="o">((</span><span class="err">⊆</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">β</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">))</span> <span class="o">:</span> <span class="n">partial_order</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">le</span> <span class="o">:=</span> <span class="n">inv_image</span> <span class="o">(</span><span class="err">⊆</span><span class="o">)</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">le_refl</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">le_trans</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">trans</span><span class="o">,</span>
  <span class="n">le_antisymm</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H1</span> <span class="n">H2</span><span class="o">,</span> <span class="n">H</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">antisymm</span> <span class="n">H1</span> <span class="n">H2</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Apr 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125781342):
<p>and the converse :P</p>

#### [ Kenny Lau (Apr 27 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125781353):
<p>wait, that's the wrong converse</p>

#### [ Reid Barton (Apr 27 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125783616):
<p>It's the enriched Yoneda lemma where the enriching category is the poset of truth values {false -&gt; true}</p>

#### [ Reid Barton (Apr 27 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125783685):
<p><code>{ z | z ≤ x }</code> is the characteristic feature of Yoneda things.</p>

#### [ Reid Barton (Apr 27 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/every%20partial%20order%20can%20be%20order-embedded%20into%20a%20powerset/near/125783948):
<p>I guess there's slightly more going on here because you said "embedded into a powerset" = all functions from \a to V = {false -&gt; true}, while the Yoneda embedding lands in order-reversing maps \a to V, i.e., lower sets of \a.</p>


{% endraw %}
